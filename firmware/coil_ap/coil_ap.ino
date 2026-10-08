/*
  Coil Workbench: soft-AP controller for the series coil array
  Generated from the workbench design "My build · acute pain".

  Board  : ESP32-S3 (Arduino-ESP32 core 3.x). No extra libraries needed.
  Network: the board makes its own Wi-Fi network (CoilBench-xxxx, password below).
           Join it from a phone, then open http://192.168.4.1/

  Wiring (see the wiring diagram in the workbench):
    GPIO4  -> 1 kΩ -> base of the NPN level shifter (BJT gate driver); HIGH = MOSFET on
    GPIO1  <- 1 kΩ + 10 nF RC from the top of the 1.0 Ω source shunt (ADC1)
    GPIO2  <- optional 10 kΩ NTC divider on the hottest solenoid (set USE_NTC 1)
    3V3 / GND as usual. The 12 V gate rail comes from an L7812 on the 24 V input.

  Safety built in: stuck-low GPIO keeps the MOSFET off, over-current latch, thermal model
  with cool-down lock, session timer, and a dead-man stop if the browser disconnects.
  This is an engineering aid, not a medical device. Do not use near implants.
*/
#include <WiFi.h>
#include <WebServer.h>
#include <Preferences.h>
#include <esp_timer.h>
#include <math.h>

// ---------------- design constants (from the workbench model) ----------------
#define GATE_PIN        4
#define ISENSE_PIN      1
#define NTC_PIN         2
#define USE_NTC         0                    // 1 = read a 10k NTC (B=3950) on NTC_PIN
#define HAVE_SENSE      1                    // 0 = no shunt fitted: current comes from the model
const char* AP_SSID_PREFIX = "CoilBench";
const char* AP_PASS        = "coil1234";   // change this (8+ characters)

const float V_SUPPLY   = 24.0f;          // V
const float R_TOTAL    = 28.362f;          // ohm, whole series loop incl. leads and MOSFET
const float TAU_S      = 1.2896e-4f;           // s, L/R of the loop
const float I_DC       = 0.846f;           // A, V/R
const float IPK_MODEL  = 0.835f;           // A, model peak current at the default pulse
const float B_PER_A    = 8.8126e-4f;           // T per A at the target ("20 mm deep, 0 mm off-centre")
const float RSH_OHM    = 1.0f;           // ohm, source shunt
const float OC_LIMIT_A = 1.058f;            // A, latch a fault above this
const float R_HOT      = 3.900f;          // ohm, hottest winding (one solenoid)
const float RTH_KW     = 176.3f;           // K/W, hot winding to air (still air, h = 10 W/m2K)
const float CTH_JK     = 2.82f;           // J/K, hot winding thermal mass
const float DT_LIMIT_C = 20.0f;         // K above ambient, pauses the session above this
const float DUTY_CAP   = 0.35f;              // never exceed this pulse duty

const float F_DEF = 80.0f, ON_MS_DEF = 0.563f;

// ---------------- state ----------------
struct Cfg { float fLo = F_DEF, fHi = F_DEF, sweepS = 0, onMs = ON_MS_DEF; int inten = 100; int sessMin = 20; bool deadman = true; } cfg;
volatile bool running = false;
volatile uint32_t pulseCnt = 0;
volatile float ipkLast = 0;
volatile int ocCount = 0; volatile bool ocFlag = false;
volatile uint32_t chopDuty = 1023;
bool fault = false, coolLock = false;
String faultMsg = "", prog = "manual";
uint32_t sessStartMs = 0, lastPollMs = 0, sampleCostUs = 40;
float dT = 0, ipkAvg = 0, irmsEst = 0, tempC = NAN, fNow = F_DEF;
uint64_t runTotalS = 0, pulsesTotal = 0; uint32_t sessions = 0; uint32_t sessS = 0;
const int NH = 120; float hI[NH], hR[NH], hT[NH], hF[NH]; int hN = 0;
struct Log { uint32_t dur; float ipk; float f; char prog[10]; }; Log logs[8]; int logN = 0;
WebServer server(80); Preferences prefs;
static esp_timer_handle_t tPer = nullptr, tOff = nullptr;

// ---------------- pulse engine ----------------
static inline void gateSet(bool on) { ledcWrite(GATE_PIN, on ? chopDuty : 0); }
static float currentF() {
  if (cfg.sweepS <= 0.5f || cfg.fHi <= cfg.fLo) return cfg.fLo;
  float ph = fmodf((millis() - sessStartMs) / 1000.0f, cfg.sweepS) / cfg.sweepS;
  return cfg.fLo + (cfg.fHi - cfg.fLo) * 0.5f * (1.0f - cosf(6.2831853f * ph));
}
static void onOff(void*) {
#if HAVE_SENSE
  uint32_t mv = 0;
  for (int i = 0; i < 2; i++) { uint32_t v = analogReadMilliVolts(ISENSE_PIN); if (v > mv) mv = v; }
  float a = mv / 1000.0f / RSH_OHM;
  ipkLast = a;
  if (a > OC_LIMIT_A) { if (++ocCount >= 3) { gateSet(false); ocFlag = true; return; } } else ocCount = 0;
#else
  ipkLast = IPK_MODEL * (cfg.inten / 100.0f);
#endif
  gateSet(false);
}
static void onPeriod(void*) {
  if (!running || ocFlag) return;
  fNow = currentF();
  uint32_t perUs = (uint32_t)(1e6f / fNow);
  uint32_t onUs = (uint32_t)(cfg.onMs * 1000.0f);
  if (onUs > perUs * DUTY_CAP) onUs = (uint32_t)(perUs * DUTY_CAP);
  if (onUs > sampleCostUs + 60) onUs -= sampleCostUs;
  chopDuty = (uint32_t)(1023UL * cfg.inten / 100);
  gateSet(true); pulseCnt++;
  esp_timer_start_once(tOff, onUs);
  esp_timer_start_once(tPer, perUs);
}
static void startRun() {
  if (fault || coolLock || running) return;
  sessStartMs = millis(); sessS = 0; ocCount = 0; ocFlag = false; lastPollMs = millis();
  running = true; esp_timer_start_once(tPer, 2000);
}
static void saveTotals() {
  prefs.putULong64("runS", runTotalS); prefs.putULong64("pulses", pulsesTotal); prefs.putUInt("sess", sessions);
  prefs.putBytes("logs", logs, sizeof(logs)); prefs.putInt("logN", logN);
}
static void stopRun(const char* why) {
  bool was = running; running = false;
  esp_timer_stop(tPer); esp_timer_stop(tOff); gateSet(false);
  if (was) {
    sessions++; if (logN < 8) logN++; for (int i = 7; i > 0; i--) logs[i] = logs[i - 1];
    logs[0].dur = sessS; logs[0].ipk = ipkAvg; logs[0].f = fNow; strncpy(logs[0].prog, prog.c_str(), 9); logs[0].prog[9] = 0;
    saveTotals();
  }
  if (why && why[0] && String(why) != "user") { faultMsg = why; }
}

// ---------------- 1 Hz housekeeping: stats, thermal model, safety ----------------
static float irmsFromIpk(float ipk, float onS, float perS) {
  if (ipk <= 0 || onS <= 0) return 0;
  float k = 1.0f - expf(-onS / TAU_S), iinf = ipk / fmaxf(k, 1e-3f);
  float a = iinf * iinf * (onS - 2 * TAU_S * (1 - expf(-onS / TAU_S)) + 0.5f * TAU_S * (1 - expf(-2 * onS / TAU_S)));
  float offS = fmaxf(perS - onS, 0);
  float b = ipk * ipk * 0.5f * TAU_S * (1 - expf(-2 * offS / TAU_S));
  return sqrtf((a + b) / perS);
}
static void housekeeping() {
  static uint32_t lastTick = 0, lastSave = 0; uint32_t now = millis();
  if (now - lastTick < 1000) return;
  lastTick = now;
  float ipkNow = running ? ipkLast : 0; ipkAvg = running ? (ipkAvg * 0.7f + ipkNow * 0.3f) : 0;
  if (running) {
    float perS = 1.0f / fNow, onS = fminf(cfg.onMs / 1000.0f, perS * DUTY_CAP);
    irmsEst = irmsFromIpk(ipkAvg, onS, perS); sessS++; runTotalS++;
    pulsesTotal += (uint32_t)fNow;
  } else irmsEst = 0;
  float P = irmsEst * irmsEst * R_HOT;                 // W in the hottest solenoid
  dT += (P - dT / RTH_KW) / CTH_JK;                     // 1 s step of the lumped thermal model
  if (dT < 0) dT = 0;
#if USE_NTC
  { float v = analogReadMilliVolts(NTC_PIN) / 3300.0f; if (v > 0.01f && v < 0.99f) { float r = 10000.0f * v / (1 - v); tempC = 1.0f / (logf(r / 10000.0f) / 3950.0f + 1.0f / 298.15f) - 273.15f; } }
#endif
  if (hN < NH) hN++;
  for (int i = NH - 1; i > 0; i--) { hI[i] = hI[i - 1]; hR[i] = hR[i - 1]; hT[i] = hT[i - 1]; hF[i] = hF[i - 1]; }
  hI[0] = ipkAvg; hR[0] = irmsEst; hT[0] = dT; hF[0] = running ? fNow : 0;
  if (ocFlag) { ocFlag = false; fault = true; stopRun("over-current latch"); }
  if (running) {
    if (cfg.sessMin > 0 && sessS >= (uint32_t)cfg.sessMin * 60) { stopRun("session complete"); }
    else if (dT >= DT_LIMIT_C) { coolLock = true; stopRun("thermal limit: cooling"); }
    else if (cfg.deadman && now - lastPollMs > 20000) { stopRun("connection lost"); }
    if (now - lastSave > 60000) { lastSave = now; saveTotals(); }
  }
  if (coolLock && dT < 0.8f * DT_LIMIT_C) coolLock = false;
}

// ---------------- web ----------------
static void sendJson(const String& s) { server.sendHeader("Cache-Control", "no-store"); server.send(200, "application/json", s); }
static String num(float v, int d = 3) { if (isnan(v)) return "null"; return String(v, d); }
static void apiState() {
  lastPollMs = millis();
  String s = "{\"run\":" + String(running ? 1 : 0) + ",\"fault\":" + String(fault ? 1 : 0) + ",\"cool\":" + String(coolLock ? 1 : 0) + ",\"msg\":\"" + faultMsg + "\",\"prog\":\"" + prog + "\"";
  s += ",\"f\":" + num(running ? fNow : cfg.fLo, 2) + ",\"fLo\":" + num(cfg.fLo, 2) + ",\"fHi\":" + num(cfg.fHi, 2) + ",\"sweep\":" + num(cfg.sweepS, 1) + ",\"on\":" + num(cfg.onMs, 3) + ",\"int\":" + String(cfg.inten) + ",\"sessMin\":" + String(cfg.sessMin) + ",\"dead\":" + String(cfg.deadman ? 1 : 0);
  s += ",\"ipk\":" + num(ipkAvg, 3) + ",\"irms\":" + num(irmsEst, 3) + ",\"dT\":" + num(dT, 1) + ",\"temp\":" + num(tempC, 1) + ",\"B\":" + num(ipkAvg * B_PER_A * 1e6f, 1);
  s += ",\"el\":" + String(sessS) + ",\"left\":" + String(running && cfg.sessMin > 0 ? (int)(cfg.sessMin * 60) - (int)sessS : 0) + ",\"pulses\":" + String((unsigned long)pulseCnt) + ",\"runTot\":" + String((unsigned long)runTotalS) + ",\"pulTot\":" + String((double)pulsesTotal, 0) + ",\"sess\":" + String(sessions) + ",\"clients\":" + String(WiFi.softAPgetStationNum()) + ",\"heap\":" + String(ESP.getFreeHeap()) + ",\"up\":" + String(millis() / 1000);
  s += ",\"dutyPct\":" + num(100.0f * fminf(cfg.onMs / 1000.0f * (running ? fNow : cfg.fLo), DUTY_CAP), 2) + ",\"ipkModel\":" + num(IPK_MODEL, 3) + ",\"dtLim\":" + num(DT_LIMIT_C, 1) + ",\"idc\":" + num(I_DC, 3) + ",\"tau\":" + num(TAU_S * 1000, 3) + "}";
  sendJson(s);
}
static void apiHist() {
  String s = "{\"n\":" + String(hN) + ",\"i\":[", r = "", t = "", f = ""; 
  for (int i = 0; i < hN; i++) { s += num(hI[i], 3) + (i < hN - 1 ? "," : ""); r += num(hR[i], 3) + (i < hN - 1 ? "," : ""); t += num(hT[i], 1) + (i < hN - 1 ? "," : ""); f += num(hF[i], 1) + (i < hN - 1 ? "," : ""); }
  s += "],\"r\":[" + r + "],\"t\":[" + t + "],\"f\":[" + f + "],\"log\":[";
  for (int i = 0; i < logN; i++) s += "{\"d\":" + String(logs[i].dur) + ",\"i\":" + num(logs[i].ipk, 3) + ",\"f\":" + num(logs[i].f, 1) + ",\"p\":\"" + String(logs[i].prog) + "\"}" + (i < logN - 1 ? "," : "");
  s += "]}"; sendJson(s);
}
static float argF(const char* k, float d, float lo, float hi) { if (!server.hasArg(k)) return d; float v = server.arg(k).toFloat(); return v < lo ? lo : v > hi ? hi : v; }
static void apiCmd() {
  lastPollMs = millis();
  String c = server.arg("c");
  if (c == "set" || c == "start") {
    if (server.hasArg("prog")) prog = server.arg("prog");
    cfg.fLo = argF("fLo", cfg.fLo, 0.5f, 200); cfg.fHi = argF("fHi", cfg.fHi, 0.5f, 200); if (cfg.fHi < cfg.fLo) cfg.fHi = cfg.fLo;
    cfg.sweepS = argF("sweep", cfg.sweepS, 0, 600); cfg.onMs = argF("on", cfg.onMs, 0.05f, 50);
    cfg.inten = (int)argF("int", cfg.inten, 10, 100); cfg.sessMin = (int)argF("sessMin", cfg.sessMin, 0, 120);
    if (server.hasArg("dead")) cfg.deadman = server.arg("dead") == "1";
    float fmax = cfg.fHi, d = cfg.onMs / 1000.0f * fmax; if (d > DUTY_CAP) cfg.onMs = DUTY_CAP / fmax * 1000.0f;
  }
  if (c == "start") { faultMsg = ""; startRun(); }
  if (c == "stop") stopRun("user");
  if (c == "clear") { fault = false; faultMsg = ""; ocCount = 0; ocFlag = false; }
  if (c == "reset") { runTotalS = 0; pulsesTotal = 0; sessions = 0; logN = 0; saveTotals(); }
  apiState();
}
static const char PAGE[] PROGMEM = R"HTML(<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Coil controller</title>
<style>
:root{--bg:#e9edf0;--p:#f8fafb;--p2:#eef2f4;--ink:#162027;--mut:#56646d;--ln:#cfd7dc;--cu:#a9561f;--cus:#f3e2d4;--fd:#24598c;--ok:#24784a;--wn:#9a6a10;--cr:#b0302f}
@media (prefers-color-scheme:dark){:root{--bg:#0e1316;--p:#151c20;--p2:#1b2328;--ink:#e1e8eb;--mut:#93a1a9;--ln:#2a353b;--cu:#e2915a;--cus:#3a2617;--fd:#7fb3e3;--ok:#62c48e;--wn:#e3b553;--cr:#ec7a76}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.4 system-ui,-apple-system,Segoe UI,sans-serif}
.w{max-width:760px;margin:0 auto;padding:12px 14px 40px;display:grid;gap:12px}
.c{background:var(--p);border:1px solid var(--ln);border-radius:10px;padding:12px}
h1{font-size:19px;margin:0}h2{font-size:14px;margin:0 0 8px;color:var(--mut);letter-spacing:.04em;text-transform:uppercase}
.top{display:flex;justify-content:space-between;align-items:center;gap:8px}
.pill{font:600 12px ui-monospace,Menlo,monospace;border-radius:99px;padding:4px 10px;background:var(--p2);border:1px solid var(--ln)}
.pill.run{background:var(--ok);color:#fff;border-color:var(--ok)}.pill.cool{background:var(--wn);color:#fff;border-color:var(--wn)}.pill.flt{background:var(--cr);color:#fff;border-color:var(--cr)}
.go{width:100%;font:700 20px system-ui;padding:16px;border:0;border-radius:10px;background:var(--ok);color:#fff;cursor:pointer}.go.stop{background:var(--cr)}.go:disabled{opacity:.45}
.prog{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}
.prog button{border:1px solid var(--ln);background:var(--p2);color:var(--ink);border-radius:8px;padding:9px 6px;cursor:pointer;font:600 13px system-ui}
.prog button.on{border-color:var(--cu);background:var(--cus);box-shadow:inset 0 -3px 0 var(--cu)}.prog small{display:block;font:500 11px ui-monospace,monospace;color:var(--mut)}
.row{display:grid;grid-template-columns:130px 1fr 74px;gap:8px;align-items:center;margin:7px 0;font-size:13.5px}.row label{color:var(--mut)}
.row input[type=range]{width:100%;accent-color:var(--cu)}.row output{font:600 13px ui-monospace,monospace;text-align:right}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:8px}
.k{background:var(--p2);border:1px solid var(--ln);border-radius:8px;padding:8px 10px}.k b{display:block;font:600 19px ui-monospace,Menlo,monospace}.k span{font-size:11.5px;color:var(--mut)}
canvas{width:100%;height:150px;display:block;background:var(--p2);border:1px solid var(--ln);border-radius:8px}
table{width:100%;border-collapse:collapse;font:12.5px ui-monospace,monospace}td,th{padding:4px 6px;border-bottom:1px solid var(--ln);text-align:right}th:first-child,td:first-child{text-align:left}th{color:var(--mut);font-weight:600}
.msg{font-size:13px;color:var(--cr);min-height:18px}.btn{border:1px solid var(--ln);background:var(--p2);color:var(--ink);border-radius:7px;padding:7px 11px;cursor:pointer;font:13px system-ui}
.note{font-size:12px;color:var(--mut)}
</style></head><body><div class="w">
<div class="c top"><h1>Coil controller</h1><span class="pill" id="st">…</span></div>
<div class="c"><button class="go" id="go">START</button><div class="msg" id="msg"></div>
<div class="grid" style="margin-top:8px"><div class="k"><b id="kT">–</b><span>time left / elapsed</span></div><div class="k"><b id="kF">–</b><span>pulse rate</span></div><div class="k"><b id="kB">–</b><span>B at target (model × measured I)</span></div><div class="k"><b id="kI">–</b><span>peak current (measured)</span></div></div></div>
<div class="c"><h2>Program</h2><div class="prog"><button data-p="acute">Acute pain<small>50–100 Hz sweep</small></button><button data-p="recover">Recovery<small>10–20 Hz sweep</small></button><button data-p="manual">Manual<small>fixed rate</small></button></div>
<div class="row"><label>Rate low</label><input type="range" id="fLo" min="1" max="150" step="0.5"><output id="oFLo"></output></div>
<div class="row"><label>Rate high</label><input type="range" id="fHi" min="1" max="150" step="0.5"><output id="oFHi"></output></div>
<div class="row"><label>Sweep period</label><input type="range" id="sw" min="0" max="120" step="1"><output id="oSw"></output></div>
<div class="row"><label>Pulse width</label><input type="range" id="on" min="0.1" max="12" step="0.05"><output id="oOn"></output></div>
<div class="row"><label>Intensity</label><input type="range" id="int" min="10" max="100" step="1"><output id="oInt"></output></div>
<div class="row"><label>Session</label><input type="range" id="sm" min="1" max="60" step="1"><output id="oSm"></output></div>
<label class="note"><input type="checkbox" id="dead" checked> Stop if this page loses connection (dead-man)</label>
<div class="note" id="duty"></div></div>
<div class="c"><h2>Live</h2><div class="grid"><div class="k"><b id="kR">–</b><span>rms current (estimate)</span></div><div class="k"><b id="kD">–</b><span>hot-winding rise (model)</span></div><div class="k"><b id="kN">–</b><span>pulse duty</span></div><div class="k"><b id="kP">–</b><span>pulses this session</span></div></div></div>
<div class="c"><h2>Current, last 2 minutes</h2><canvas id="gI" width="700" height="150"></canvas></div>
<div class="c"><h2>Hot-winding temperature rise (model)</h2><canvas id="gT" width="700" height="150"></canvas></div>
<div class="c"><h2>Pulse rate</h2><canvas id="gF" width="700" height="150"></canvas></div>
<div class="c"><h2>Device stats</h2><div class="grid"><div class="k"><b id="sRun">–</b><span>lifetime run time</span></div><div class="k"><b id="sSes">–</b><span>sessions</span></div><div class="k"><b id="sPul">–</b><span>pulses delivered</span></div><div class="k"><b id="sUp">–</b><span>uptime</span></div><div class="k"><b id="sCl">–</b><span>Wi-Fi clients</span></div><div class="k"><b id="sHp">–</b><span>free memory</span></div></div>
<h2 style="margin-top:12px">Recent sessions</h2><table id="lg"></table>
<div style="margin-top:10px;display:flex;gap:8px;flex-wrap:wrap"><button class="btn" id="csv">Download history CSV</button><button class="btn" id="clr">Clear fault</button><button class="btn" id="rst">Reset lifetime stats</button></div></div>
<div class="note">Model constants: L/R = <span id="mt"></span> ms, DC limit <span id="mi"></span> A, thermal limit <span id="ml"></span> °C. Engineering aid, not a medical device.</div>
</div>
<script>
const $=id=>document.getElementById(id);let S={},H={i:[],r:[],t:[],f:[]},busy=0,touched=0;
const P={acute:{fLo:50,fHi:100,sw:20,on:0.55,int:100,sm:10},recover:{fLo:10,fHi:20,sw:30,on:2.15,int:80,sm:20},manual:{}};
const sl=['fLo','fHi','sw','on','int','sm'],un={fLo:' Hz',fHi:' Hz',sw:' s',on:' ms',int:' %',sm:' min'},ou={fLo:'oFLo',fHi:'oFHi',sw:'oSw',on:'oOn',int:'oInt',sm:'oSm'};
function show(){sl.forEach(k=>{$(ou[k]).textContent=(+$(k).value)+un[k]});const f=Math.max(+$('fHi').value,+$('fLo').value),d=+$('on').value/1000*f*100;$('duty').textContent='Highest duty at these settings: '+d.toFixed(1)+' %. Heat in the small solenoids scales with duty, so shorter pulses allow longer sessions.'}
sl.forEach(k=>$(k).addEventListener('input',()=>{touched=Date.now();show()}));
document.querySelectorAll('[data-p]').forEach(b=>b.addEventListener('click',()=>{const p=P[b.dataset.p];S.prog=b.dataset.p;for(const k in p)$(k).value=p[k];touched=Date.now();show();mark()}));
function mark(){document.querySelectorAll('[data-p]').forEach(b=>b.classList.toggle('on',b.dataset.p===S.prog))}
function q(c){return '/api/cmd?c='+c+'&prog='+(S.prog||'manual')+'&fLo='+$('fLo').value+'&fHi='+$('fHi').value+'&sweep='+$('sw').value+'&on='+$('on').value+'&int='+$('int').value+'&sessMin='+$('sm').value+'&dead='+($('dead').checked?1:0)}
async function cmd(c){try{const r=await fetch(c);S=Object.assign(S,await r.json());paint()}catch(e){$('msg').textContent='no connection'}}
$('go').addEventListener('click',()=>cmd(S.run?'/api/cmd?c=stop':q('start')));
$('clr').addEventListener('click',()=>cmd('/api/cmd?c=clear'));
$('rst').addEventListener('click',()=>{if(confirm('Reset lifetime stats?'))cmd('/api/cmd?c=reset')});
$('csv').addEventListener('click',()=>{let s='seconds_ago,ipk_A,irms_A,dT_C,rate_Hz\n';for(let i=0;i<H.i.length;i++)s+=i+','+H.i[i]+','+H.r[i]+','+H.t[i]+','+H.f[i]+'\n';const a=document.createElement('a');a.href=URL.createObjectURL(new Blob([s],{type:'text/csv'}));a.download='coil_history.csv';a.click()});
const hm=s=>{s=Math.round(s);return Math.floor(s/3600)+'h '+String(Math.floor(s%3600/60)).padStart(2,'0')+'m'},mm=s=>{s=Math.max(0,Math.round(s));return Math.floor(s/60)+':'+String(s%60).padStart(2,'0')};
function paint(){const s=S;if(s.run===undefined)return;
 const st=$('st');st.textContent=s.fault?'FAULT':s.cool?'COOLING':s.run?'RUNNING':'IDLE';st.className='pill '+(s.fault?'flt':s.cool?'cool':s.run?'run':'');
 $('go').textContent=s.run?'STOP':'START';$('go').className='go'+(s.run?' stop':'');$('go').disabled=!!(s.fault||s.cool);
 $('msg').textContent=s.msg||'';$('kT').textContent=s.run?(s.left>0?mm(s.left):mm(s.el)):'–';$('kF').textContent=s.run?s.f.toFixed(1)+' Hz':'–';$('kB').textContent=s.run?(s.B>=1000?(s.B/1000).toFixed(2)+' mT':s.B.toFixed(0)+' µT'):'–';$('kI').textContent=s.run?s.ipk.toFixed(2)+' A':'–';
 $('kR').textContent=s.run?s.irms.toFixed(3)+' A':'–';$('kD').textContent=s.dT.toFixed(1)+' °C'+(s.temp!=null?' / '+s.temp.toFixed(1)+' °C NTC':'');$('kN').textContent=s.dutyPct.toFixed(1)+' %';$('kP').textContent=s.pulses;
 $('sRun').textContent=hm(s.runTot);$('sSes').textContent=s.sess;$('sPul').textContent=Number(s.pulTot).toLocaleString();$('sUp').textContent=hm(s.up);$('sCl').textContent=s.clients;$('sHp').textContent=Math.round(s.heap/1024)+' kB';
 $('mt').textContent=s.tau;$('mi').textContent=s.idc;$('ml').textContent=s.dtLim;
 if(Date.now()-touched>4000&&!busy){$('fLo').value=s.fLo;$('fHi').value=s.fHi;$('sw').value=s.sweep;$('on').value=s.on;$('int').value=s.int;$('sm').value=s.sessMin;$('dead').checked=!!s.dead;show()}mark()}
function chart(id,a,col,lab,fixed){const c=$(id),x=c.getContext('2d'),w=c.width,h=c.height,cs=getComputedStyle(document.body);x.clearRect(0,0,w,h);if(!a.length)return;
 let mx=Math.max(...a,fixed||0.001)*1.15;const n=a.length;x.strokeStyle=cs.getPropertyValue('--ln');x.fillStyle=cs.getPropertyValue('--mut');x.font='11px monospace';x.lineWidth=1;
 for(let g=0;g<=3;g++){const y=h-18-(h-26)*g/3;x.beginPath();x.moveTo(36,y);x.lineTo(w-4,y);x.stroke();x.fillText((mx*g/3).toFixed(mx<10?2:0),2,y+3)}
 x.strokeStyle=col;x.lineWidth=2;x.beginPath();for(let i=0;i<n;i++){const px=w-4-(w-40)*i/Math.max(NH-1,1),py=h-18-(h-26)*(a[i]/mx);i?x.lineTo(px,py):x.moveTo(px,py)}x.stroke();x.fillStyle=cs.getPropertyValue('--mut');x.fillText(lab,40,12);x.fillText('now',w-26,h-4);x.fillText('−2 min',40,h-4)}
const NH=120;
async function poll(){try{busy=0;const r=await fetch('/api/state');S=await r.json();paint()}catch(e){$('st').textContent='OFFLINE'}}
async function hist(){try{const r=await fetch('/api/hist');const j=await r.json();H=j;chart('gI',j.i,'#a9561f','peak current, A',S.ipkModel);chart('gT',j.t,'#c0392b','°C above ambient',S.dtLim);chart('gF',j.f,'#24598c','Hz',20);
 $('lg').innerHTML='<tr><th>Program</th><th>Length</th><th>Avg peak</th><th>Last rate</th></tr>'+j.log.map(l=>'<tr><td>'+l.p+'</td><td>'+mm(l.d)+'</td><td>'+l.i.toFixed(2)+' A</td><td>'+l.f.toFixed(1)+' Hz</td></tr>').join('')}catch(e){}}
show();poll();hist();setInterval(poll,1000);setInterval(hist,2500);
</script>
</body></html>
)HTML";
static void handleRoot() { server.sendHeader("Cache-Control", "no-store"); server.send_P(200, "text/html", PAGE); }

void setup() {
  Serial.begin(115200);
  pinMode(GATE_PIN, OUTPUT); digitalWrite(GATE_PIN, LOW);   // off before anything else
  ledcAttach(GATE_PIN, 20000, 10); ledcWrite(GATE_PIN, 0);
  analogReadResolution(12); analogSetPinAttenuation(ISENSE_PIN, ADC_11db);
#if USE_NTC
  analogSetPinAttenuation(NTC_PIN, ADC_11db);
#endif
  { uint32_t t0 = micros(); for (int i = 0; i < 16; i++) analogReadMilliVolts(ISENSE_PIN); sampleCostUs = (micros() - t0) / 16 * 2; }
  prefs.begin("coil", false);
  runTotalS = prefs.getULong64("runS", 0); pulsesTotal = prefs.getULong64("pulses", 0); sessions = prefs.getUInt("sess", 0);
  logN = prefs.getInt("logN", 0); if (logN > 8 || logN < 0) logN = 0; if (logN) prefs.getBytes("logs", logs, sizeof(logs));
  esp_timer_create_args_t a1 = {}; a1.callback = onPeriod; a1.name = "per"; esp_timer_create(&a1, &tPer);
  esp_timer_create_args_t a2 = {}; a2.callback = onOff; a2.name = "off"; esp_timer_create(&a2, &tOff);
  uint8_t mac[6]; WiFi.macAddress(mac); char ssid[32]; snprintf(ssid, sizeof ssid, "%s-%02X%02X", AP_SSID_PREFIX, mac[4], mac[5]);
  WiFi.mode(WIFI_AP); WiFi.softAP(ssid, AP_PASS);
  Serial.printf("AP %s  http://%s/\n", ssid, WiFi.softAPIP().toString().c_str());
  server.on("/", handleRoot); server.on("/api/state", apiState); server.on("/api/hist", apiHist); server.on("/api/cmd", apiCmd);
  server.begin();
}
void loop() { server.handleClient(); housekeeping(); delay(2); }
