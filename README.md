# Coil Workbench

An offline-capable web app for designing electromagnets driven by an **ESP32-S3 + Si5351**, from low-frequency PEMF through pulsed eddy-current induction to magnetic induction tomography (MIT). It pairs a live physics bench with a cited research library on how pulsed and alternating magnetic fields interact with nervous, vascular, immune and muscular tissue.

**Live app:** https://combsbw.github.io/coil-workbench/ (after GitHub Pages is enabled, see below)

## Install for offline use

Open the live app once while online. A service worker caches the whole app, its fonts and icons; after that it runs with no connection.

- **Desktop Chrome / Edge:** click **Install app** in the header, or the install icon in the address bar.
- **Android Chrome:** menu → *Install app* / *Add to Home screen*.
- **iPhone / iPad Safari:** Share → *Add to Home Screen*.

When a new version is pushed, an **Update available · reload** button appears in the header. Citation links (PubMed, DOI) need a connection; everything else works offline.

## What it does

**Workbench**
- Coil geometry (solenoid, flat spiral, Helmholtz pair), AWG and litz wire, air / iron / powdered-iron / ferrite cores
- Inductance (Wheeler, mutual inductance), DC and AC resistance (Dowell skin + proximity), self-capacitance and self-resonance
- Drive: sine, bipolar square, unipolar pulse with diode/TVS turn-off, burst; transient RLC simulation; series-resonant tuning
- ESP32-S3 direct-gate MOSFET model (gate charge, switching time, MOSFET loss), Si5351 PLL/MultiSynth plan, generated Arduino sketch
- Field map from exact ring-current Biot–Savart with flux lines; B, dB/dt, induced E, tissue J, SAR at the target; nerve threshold and ICNIRP comparisons
- MIT receive analysis: secondary-field ratio, phase shift, receiver EMF
- **Live effect panel**: every slider move, typed value or chart click shows what changed in field, dose, heat and resonance, which checks appeared or resolved, and gauges with a "before" marker. Charts draw dashed "before" traces.
- **Interactive charts**: hover any chart for readouts; click the frequency-response chart to set the drive frequency; click inside the tissue on the field map to move the target
- Bench calibration from measured L, R and B; baseline pinning; sensitivity table

**Build sheet · composite coils** (select *My build · composite* under Coil type; the default preset is a 7-solenoid array in a 5 in aluminium winding)
- Describe a hand-built magnet as groups: a ring of premade solenoids, an outer winding of any wire/length/form, a central steel core, optional bore pole pins; every group has polarity and series/ordering
- Exact ring Biot–Savart superposition, mutual inductance, ferromagnet demagnetisation, eddy-current permeability roll-off and saturation, per-group heating
- Field map with streamlines and an E-field mode; contribution table (which part makes the field at depth) and what-if table
- Hand-parts discrete BJT gate driver (no driver IC), fuse/flyback/shunt sizing against the parts you own
- Wiring diagram, series-wiring and polarity-test figure, bill of materials with on-hand/buy column
- **Generated ESP32-S3 soft-AP firmware** (`firmware/coil_ap/coil_ap.ino`, also downloadable from the Firmware card): start/stop, frequency, duty, intensity, session timer, live current/temperature graphs, lifetime stats

**Research** (`#research`)
- 80 PubMed-indexed references with PMID, DOI and free-full-text links
- 10 mechanism dossiers (Faraday induction, Ca²⁺/calmodulin → NO, adenosine receptors, TRPC1–mitochondria, growth factors and cytokines, radical pairs, VGCC hypothesis, ion cyclotron resonance, magnetite, endogenous fields) with evidence status and coil-design implications
- System syntheses for nervous, vascular, immune, muscular, and measurement/dosimetry
- Evidence map, filterable library, citation export
- Published exposure protocols load into the workbench with drive scaled to the reported field

## Enable GitHub Pages

Settings → Pages → *Build and deployment* → Source: **Deploy from a branch** → Branch: `main`, folder `/ (root)` → Save. The site appears at `https://combsbw.github.io/coil-workbench/` within a minute or two. Service workers require HTTPS, which GitHub Pages provides.

## Files

| Path | Purpose |
|---|---|
| `index.html` | The whole app (HTML, CSS, JS in one file) |
| `sw.js` | Service worker: offline app shell, versioned by content hash |
| `manifest.webmanifest` | Install metadata, icons, shortcuts |
| `fonts/` | Self-hosted Saira Condensed and IBM Plex (SIL Open Font License) |
| `icons/` | App, maskable and Apple touch icons |
| `firmware/coil_ap/coil_ap.ino` | ESP32-S3 soft-AP controller generated for the default build (Arduino-ESP32 3.x, no extra libraries) |
| `.nojekyll` | Serve files as-is |

## Caveats

Engineering estimates from closed-form models; expect 10–30 % error before calibrating against bench measurements. Bibliographic data from PubMed (U.S. National Library of Medicine); summaries are paraphrased. Not medical advice. Check the generated firmware constants against your own measurements (coil resistance, shunt value) before the first run, start at low voltage, and fit the fuse. Do not use near pacemakers, neurostimulators or other implants.
