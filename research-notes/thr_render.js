/*THRJS-BEGIN*/
const THR_DC={E:{l:'Induced E (dB/dt)',d:'The response follows the electric field induced by the changing flux, so rise time, frequency and loop size matter. Nerve and retina are the firm cases.'},
 B:{l:'Field amplitude B',d:'The field itself, its direction or its ratio to a static field. Works with dB/dt = 0 and is insensitive to rise time at mains-type frequencies.'},
 T:{l:'Timing / waveform',d:'Pulse pattern, frequency, burst structure, B_AC/B_DC ratio, session length or schedule. Amplitude is secondary and the optimum is often a window.'},
 U:{l:'Unresolved',d:'B, dB/dt and frequency were changed together, or the exposure was not reported, so the driver cannot be named from the data.'},
 X:{l:'Context, not a target',d:'Safety limits and dosimetry logic that frame every other card.'}};
const THR_GR=['speculative','very low','low','low–moderate','moderate','high'];
let THF={q:'',g:'all',d:'all',ax:'B'};
const THR_AX={B:{u:'mT',lo:-5,hi:4.5,k:'B',t:'B peak (mT)'},D:{u:'T/s',lo:-6,hi:2,k:'D',t:'dB/dt peak (T/s)'},E:{u:'V/m',lo:-8,hi:2.3,k:'E',t:'Induced E (V/m)'}};
function thrN(x){ if(x===0) return '0'; const a=Math.abs(x); if(a>=1e4||a<1e-3) return x.toExponential(2).replace(/\.?0+e/,'e').replace('e+','e'); return String(+x.toPrecision(3)); }
function thrRng(r){ if(!r) return '–'; if(r[0]===r[1]) return thrN(r[0]); return thrN(r[0])+'–'+thrN(r[1]); }
const THR_LAB={B_mT:'B (mT)',B_uT:'B (µT)',B_T:'B (T)',dBdt_Ts:'dB/dt (T/s)',E_Vm:'E (V/m)',f_Hz:'f (Hz)',J_mAm2:'J (mA/m²)',pulse_ms:'pulse (ms)'};
function thrLab(k){ return THR_LAB[k]||k.replace(/_/g,' '); }
function thrFlat(o,pre){ const out=[]; if(o==null) return out;
 if(typeof o!=='object'){ out.push([pre||'',typeof o==='number'?thrN(o):String(o)]); return out; }
 if(Array.isArray(o)){ if(o.every(x=>typeof x==='number')) out.push([pre||'',o.length===2?thrN(o[0])+'–'+thrN(o[1]):o.map(thrN).join(', ')]); else o.forEach((x,i)=>out.push(...thrFlat(x,(pre||'')+' '+(i+1)))); return out; }
 for(const [k,v] of Object.entries(o)){ const lab=pre?pre+' › '+thrLab(k):thrLab(k);
  if(v!==null&&typeof v==='object') out.push(...thrFlat(v,lab)); else out.push([lab,typeof v==='number'?thrN(v):String(v)]); }
 return out; }
function thrCard(c){ return THR_DATA.cards.find(x=>x.id===c); }
function thrRefs(list){ const P=THR_DATA.pml,T=THR_DATA.tit; return list.map(p=>`<a class="tref" target="_blank" rel="noopener" href="https://pubmed.ncbi.nlm.nih.gov/${esc(p)}/" title="${esc(T[p]||'PubMed '+p)}">${esc(P[p]||('PMID '+p))}</a>`).join(''); }
function thrCmp(v,r){ if(!(v>0)||!r||!(r[1]>0)) return null; const lo=r[0]>0?r[0]:r[1]; if(v<lo/1.001) return {c:'lo',t:`${thrN(lo/v)}× below`}; if(v>r[1]*1.001) return {c:'hi',t:`${thrN(v/r[1])}× above`}; return {c:'in',t:'inside'}; }
function thrDesignVals(){ try{ if(typeof R==='undefined'||!R) return null; const B=Math.abs(R.Bt)*1e3, D=Math.abs(R.dBdt), E=Math.abs(R.E); if(!(B>0)&&!(D>0)) return null; return {B,D,E}; }catch(e){ return null; } }
function thrRecHtml(r){ const w=thrFlat(r.win); return `<div class="thr-rec"><h4>${esc(r.name)}<span class="cg" style="margin-left:8px">${esc(r.level||'')}</span></h4>
  <p><span class="lab">Driver</span>${esc(r.driver)}</p>${r.note?`<p>${esc(r.note)}</p>`:''}
  ${w.length?`<dl class="thr-win">${w.map(([a,b])=>`<dt>${esc(a)}</dt><dd>${esc(b)}</dd>`).join('')}</dl>`:''}
  ${r.ev?`<p><span class="lab">Evidence</span>${esc(r.ev)}</p>`:''}${r.conf?`<p><span class="lab">Confidence</span>${esc(r.conf)}</p>`:''}${r.cav?`<p class="thr-cav"><span class="lab">Caveats</span>${esc(r.cav)}</p>`:''}</div>`; }
function thrExtHtml(e){ return `<div class="thr-ext"><span class="eyebrow">Second review pass · ${esc(e.name)}</span>
  ${e.expl?`<p style="margin:0;font-size:13px">${esc(e.expl)}</p>`:''}${e.win?`<p style="margin:0;font-size:13px"><b>Window.</b> ${esc(e.win)}</p>`:''}
  ${e.rep?`<p style="margin:0;font-size:13px"><b>Replication.</b> ${esc(e.rep)}</p>`:''}${e.cav?`<p style="margin:0;font-size:13px"><b>Caveats.</b> ${esc(typeof e.cav==='string'?e.cav:JSON.stringify(e.cav))}</p>`:''}
  ${e.de&&e.de.length?`<ul>${e.de.map(d=>`<li>${esc(d.d)} → ${esc(d.f)} ${d.p?`<a class="tref" target="_blank" rel="noopener" href="https://pubmed.ncbi.nlm.nih.gov/${esc(d.p)}/">${esc(THR_DATA.pml[d.p]||'PMID '+d.p)}</a>`:''}</li>`).join('')}</ul>`:''}</div>`; }
function thrCardHtml(c){ const dv=thrDesignVals();
 const rows=c.rows.length?`<div class="thr-scroll"><table class="thr-rows"><thead><tr><th>Window</th><th>B (mT)</th><th>dB/dt (T/s)</th><th>E (V/m)</th><th>basis</th></tr></thead><tbody>${c.rows.map(r=>`<tr><td>${esc(r.l)}</td><td class="num">${thrRng(r.B)}</td><td class="num">${thrRng(r.D)}</td><td class="num">${thrRng(r.E)}</td><td><span class="rtag ${r.k}">${r.k==='rep'?'reported':'computed'}</span></td></tr>`).join('')}</tbody></table></div>`:'';
 let cmp=''; if(dv&&c.rows.length){ const parts=[]; c.rows.forEach(r=>{ const a=thrCmp(dv.B,r.B),b=thrCmp(dv.D,r.D),e=thrCmp(dv.E,r.E); if(!a&&!b&&!e) return; parts.push(`<div class="thr-cmp"><b style="font-weight:600;font-size:12px;margin-right:4px">${esc(r.l)}:</b>${a?`<span class="${a.c}">B ${a.t}</span>`:''}${b?`<span class="${b.c}">dB/dt ${b.t}</span>`:''}${e?`<span class="${e.c}">E ${e.t}</span>`:''}</div>`); });
  if(parts.length) cmp=`<div style="display:grid;gap:4px"><span class="eyebrow">Your current design against these windows</span>${parts.join('')}</div>`; }
 return `<details class="thr-card dc-${c.dc}" id="thr-${c.id}"><summary><span class="tbadge ${c.dc}">${THR_DC[c.dc].l}</span><span class="ttl">${esc(c.title)}</span><span class="cg g${c.gr}"><i></i>threshold confidence: ${THR_GR[c.gr]}</span></summary>
  <div class="thr-body">${rows}${cmp}${c.recs.map(thrRecHtml).join('')}${c.ext.map(thrExtHtml).join('')}
  <div><span class="eyebrow">PubMed records (${c.refs.length})</span><div class="thr-refs">${thrRefs(c.refs)}</div></div></div></details>`; }
function thrFiltered(){ const q=THF.q.trim().toLowerCase(); return THR_DATA.cards.filter(c=>(THF.g==='all'||c.g===THF.g)&&(THF.d==='all'||c.dc===THF.d)&&(!q||(c.title+' '+c.recs.map(r=>r.name+' '+r.note+' '+r.driver).join(' ')+' '+c.ext.map(e=>e.name).join(' ')).toLowerCase().includes(q))); }
function thrChips(id,items,key){ $(id).innerHTML=items.map(([k,l])=>`<button type="button" class="chip${THF[key]===k?' on':''}" data-k="${k}">${esc(l)}</button>`).join('');
 $(id).querySelectorAll('.chip').forEach(b=>b.addEventListener('click',()=>{ THF[key]=b.dataset.k; thrChips(id,items,key); renderThrList(); if(key==='ax') renderThrChart(); })); }
function renderThrList(){ const op=new Set([...document.querySelectorAll('.thr-card[open]')].map(d=>d.id)); const cs=thrFiltered(); let h='',last='';
 cs.forEach(c=>{ if(THF.g==='all'&&c.g!==last){ last=c.g; h+=`<div class="thr-grp">${esc(THR_DATA.groups.find(g=>g[0]===c.g)[1])}</div>`; } h+=thrCardHtml(c); });
 $('thrList').innerHTML=h||'<p class="tc-note">No targets match these filters.</p>'; op.forEach(id=>{ const d=$(id); if(d) d.open=true; }); }
function renderThrChart(){ const A=THR_AX[THF.ax], dv=thrDesignVals(), span=A.hi-A.lo; const pos=v=>Math.max(0,Math.min(100,(Math.log10(v)-A.lo)/span*100));
 const st=(typeof innerWidth!=='undefined'&&innerWidth<600)?2:1; let ticks=''; for(let e=Math.ceil(A.lo/st)*st;e<=A.hi;e+=st){ ticks+=`<span style="left:${pos(Math.pow(10,e))}%">1e${e}</span>`; }
 let grid=''; for(let e=Math.ceil(A.lo);e<=A.hi;e+=1) grid+=`<i class="gl" style="left:${pos(Math.pow(10,e))}%"></i>`;
 const me=dv&&dv[A.k]>0?`<i class="tc-me" style="left:${pos(dv[A.k])}%" title="your design: ${thrN(dv[A.k])} ${A.u}"></i>`:'';
 let rows='',skipped=0;
 THR_DATA.cards.forEach(c=>c.rows.forEach(r=>{ const rg=r[A.k]; if(!rg||!(rg[1]>0)){ if(rg&&rg[1]===0) skipped++; return; } const lo=rg[0]>0?rg[0]:rg[1], hi=rg[1]; const l=pos(lo), w=Math.max(0.8,pos(hi)-l);
  rows+=`<div class="tc-row" data-c="${c.id}" title="${esc(r.l)}: ${thrRng(rg)} ${A.u} (${r.k==='rep'?'reported':'computed'}) · ${esc(c.title)}"><div class="tc-lab">${esc(r.l)}</div><div class="tc-plot">${grid}<i class="tc-bar dc${c.dc}${r.k==='calc'?' calc':''}" style="left:${l}%;width:${w}%"></i>${me}</div></div>`; }));
 $('thrChart').innerHTML=`<div class="tc-head"><div class="tc-note">${A.t}, log scale</div><div class="tc-ticks">${ticks}</div></div>${rows}${skipped?`<p class="tc-note">${skipped} static-field window${skipped>1?'s':''} (dB/dt or E = 0) not drawn on a log axis.</p>`:''}`;
 $('thrChart').querySelectorAll('.tc-row').forEach(el=>el.addEventListener('click',()=>{ THF.q='';THF.g='all';THF.d='all'; $('thrQ').value=''; renderThrFilters(); renderThrList(); const d2=$('thr-'+el.dataset.c); if(!d2) return; d2.open=true; d2.scrollIntoView({behavior:'smooth',block:'start'}); }));
 $('thrDesign').innerHTML=dv?`Your current design (from the Bench tab): B <b class="num">${thrN(dv.B)}</b> mT · dB/dt <b class="num">${thrN(dv.D)}</b> T/s · induced E <b class="num">${thrN(dv.E)}</b> V/m at the tissue radius set there. The red line marks it.`:'Open the Bench tab and choose a design to overlay it here.'; }
function renderThrFilters(){ thrChips('thrFg',[['all','All areas'],...THR_DATA.groups],'g'); thrChips('thrFd',[['all','Any driver'],...Object.keys(THR_DC).map(k=>[k,THR_DC[k].l])],'d'); }
function renderThr(){ const cs=THR_DATA.cards;
 $('thrKey').innerHTML=Object.keys(THR_DC).map(k=>{ const L=cs.filter(c=>c.dc===k); return `<div class="thr-k dc-${k}"><b>${THR_DC[k].l} <span class="num" style="color:var(--muted);font-weight:400">· ${L.length}</span></b><p>${THR_DC[k].d}</p><div class="tl">${L.map(c=>`<button type="button" data-c="${c.id}">${esc(c.title.length>46?c.title.slice(0,44)+'…':c.title)}</button>`).join('')}</div></div>`; }).join('');
 $('thrKey').querySelectorAll('[data-c]').forEach(b=>b.addEventListener('click',()=>{ THF.q='';THF.g='all';THF.d='all'; $('thrQ').value=''; renderThrFilters(); renderThrList(); const d=$('thr-'+b.dataset.c); d.open=true; d.scrollIntoView({behavior:'smooth',block:'start'}); }));
 $('thrFind').innerHTML=`<span class="eyebrow">What the evidence supports</span><ul>
  <li><b>Induced E (so dB/dt) is firmly the driver only for excitable tissue.</b> Peripheral nerve fires at roughly 1–2 V/m (15–26 T/s from MRI gradients), and retinal magnetophosphenes appear near 0.06 V/m at 20–60 Hz (a median with a very wide interval, 0.002–1.3 V/m). Typical PEMF coils (1–5 mT at 10–100 Hz) induce about 0.0002–0.08 V/m (computed for culture-well to tissue-scale loops), which is below nerve threshold.</li>
  <li><b>A cell cannot sense those fields directly.</b> Thermal noise limits direct detection to about 0.1 V/m broad-band, or about 0.0001 V/m for a narrow-band or signal-averaging detector. Any biochemical effect of milli-tesla ELF pulses must therefore act through amplification, a narrow-band mechanism, or a B-dependent route.</li>
  <li><b>B-driven routes exist but are weak at ELF.</b> Radical-pair chemistry and magnetite torque respond to B with dB/dt = 0 (milli-tesla fields are large enough to shift yields, on the order of 10 % for ROS product ratios), but neither is frequency-selective at 10–100 Hz.</li>
  <li><b>Timing matters more than amplitude in most cell studies.</b> Pulse grouping flipped macrophage polarity at the same 52 Hz fundamental, daily exposure time flipped the sign of muscle differentiation at fixed field, and the same 2 mT, 50 Hz sine suppressed angiogenesis where pulsed bursts promoted it.</li>
  <li><b>No clean dB/dt threshold exists for any biochemical target.</b> Almost every dose-response varies B with a fixed waveform, so B, dB/dt and E move together. The one direct test (Liburdy 1992, lymphocyte Ca²⁺) followed induced E, and it has not been repeated for other targets.</li></ul>`;
 thrChips('thrAx',[['B','B (mT)'],['D','dB/dt (T/s)'],['E','E (V/m)']],'ax'); renderThrFilters(); renderThrChart(); renderThrList();
 $('thrQ').addEventListener('input',e=>{ THF.q=e.target.value; renderThrList(); }); }
/*THRJS-END*/
