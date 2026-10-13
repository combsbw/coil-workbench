# Cluster 7 - Cross-cutting physics and dosimetry: does B or dB/dt (induced E) drive PEMF/ELF effects?

Source of literature: PubMed (via the PubMed MCP tools), session of 2026-10-12. About 40 query attempts were made (several returned zero hits because PubMed ANDs every word; several hit rate limits and were retried). Every PMID/DOI below was returned by a PubMed tool call in this session unless marked otherwise.

Labels used throughout:
- **[abstract]** = number or statement taken from the retrieved PubMed record (abstract or PMC full text).
- **[computed by me]** = my arithmetic; formula and geometry stated. Not from a paper.
- **[background, not retrieved]** = textbook physics or recalled standard text that I could not verify through PubMed in this session. Treat as "verify before use".
- "not reported" = the retrieved record does not give the number.

---

## 0. Bottom line

1. **Two physically distinct channels exist, and both have positive in-vitro evidence.**
   - **E-channel (Faraday).** Any time-varying B induces E (V/m) in conductive tissue. E scales with dB/dt and with the loop/geometry size: E = (r/2)·dB/dt for an axisymmetric uniform field. Everything "electrical" (membrane polarisation, channel gating, electrodiffusion, nerve stimulation) is driven by E, not by B itself.
   - **B-channel (direct).** Spin chemistry (radical pairs), magnetite torque, and ion-binding models respond to B. Static-field experiments, where dB/dt = 0 and no E is induced, still produce cell effects (PMID 25171788, 28751716), so a B-only pathway is not excluded. For ELF coils the B-channel is far from proven.
2. **For a coil at ~1 mT, 10-100 Hz, the induced E in tissue is milli-V/m scale** (0.6 to 31 mV/m peak for loop radii 2-10 cm, my table below). Transmembrane polarisation is then nano- to sub-micro-volt (1.5·E·a), against kT/C thermal membrane noise of tens of µV and against the ~mV needed for ordinary channel gating. A single-cell, classical-electrical mechanism is therefore **not credible** at this dose by the Weaver/Astumian/Adair thermal-noise arguments (PMIDs 2300806, 9788920, 7731976), which put lower bounds at about 10^-4 to 9x10^-3 V/m depending on assumptions. Yet several in-vitro papers report effects at **0.5-1.2 mV/m** (PMIDs 10790296, 10653624, 12929162, 8213260). This is an **unresolved conflict**; it is the single most important open point in the field.
3. **What the in-vitro evidence says about the driver.** Where B was held uniform and E varied (position in the dish, cell orientation relative to E), the response followed **E** (McLeod & Collazo 2000, PMID 10790296; Lee & McLeod 2000, PMID 10653624). Where E was applied with no B, effects occur (McLeod 1993, PMID 8213260). Where B was applied with dB/dt = 0, effects also occur but through different transducers (L-type Ca channels) and at much higher B (5 mT to 0.3 T; PMIDs 25171788, 28751716).
4. **No retrieved study cleanly separates B amplitude from dB/dt by varying rise time at constant B, or frequency at constant B with matched E.** This is the key evidence gap. Most "amplitude windows" (Parate 2017, Tsai 2007, Chang 2003) change B and dB/dt together.
5. **B alone is a poor dose metric.** Across carriers it fails badly: 5 µT of RF-modulated field has a dB/dt of order 10^2-10^3 T/s [computed by me, carrier frequency assumed], versus 0.3 T/s for 1 mT at 50 Hz. Report B_peak, dB/dt_peak (or rise time), waveform, burst structure, duty cycle, geometry (loop radius / container geometry) and calculated E.
6. **Where the field is genuinely unsettled:** (a) the thermal-noise bound versus the sub-mV/m in-vitro reports; (b) whether amplitude/frequency "windows" are real, reproducible, or artefacts of dosimetry; (c) whether radical-pair or Ca-binding models are quantitatively adequate at 1 mT; (d) whether tissue-level (network, multicellular) amplification lowers thresholds; (e) published thresholds are mostly single-lab, and in-vitro dosimetry is often incomplete.

---

## 1. Classification table: mechanism | what drives it | threshold magnitude | applicable to ~1 mT, 10-100 Hz coil? | confidence

| # | Mechanism / coupling | Drives it | Threshold or magnitude (with source) | Applies to coil at ~1 mT, 10-100 Hz? | Confidence |
|---|---|---|---|---|---|
| 1 | **Nerve/muscle excitation by induced E (action potentials)** | **E ∝ dB/dt**, plus **timing** (strength-duration; chronaxie) | Peripheral-nerve sensation threshold in MRI gradients: dB/dt = b(1 + c/d), rheobase b = 15 T/s (y-gradient) and 26 T/s (z-gradient), chronaxie c = 0.37-0.38 ms, d = pulse duration [abstract, PMID 10318720]. Thresholds are not monotonic in frequency above ~25 kHz (PMID 40740830). ICNIRP 2010 basic restrictions are written as induced E (see Section 2). | **No** for sine at 1 mT (max 0.63 T/s at 100 Hz, about 25-40x below rheobase) [computed by me]. **Marginal to yes** for 1 mT with 50 µs edges (20 T/s, same order as rheobase) [computed by me]. | High for the E-based physics; high that a 1 mT/10-100 Hz sine is far below it |
| 2 | **Subthreshold membrane polarisation modulating channel gating / network excitability** | **E** (ΔVm = 1.5·E·a·cosθ, low-frequency limit) | Needs ~mV for ordinary gating [background, not retrieved]. At E = 0.0157 V/m (1 mT, 50 Hz, r = 10 cm), a = 10 µm: ΔVm = 0.24 µV [computed by me]. Sham TMS with ~5% of real TMS E still altered EEG dynamics [abstract, PMID 25620925] | Polarisation is 10^3-10^4 below gating levels. Network-level sensitivity to weak fields is plausible but untested at these E values here | Medium-high for the cell-level calculation; low for network amplification |
| 3 | **Thermal-noise-limited detection by a single cell** (the bound that mechanisms 2, 4, 5 must overcome) | **E** (signal) versus thermal membrane voltage noise | Broad-band minimum E about 10^-3 V/cm = 0.1 V/m; narrow-band or enzyme signal averaging down to about 10^-6 V/cm = 10^-4 V/m [abstract, PMID 2300806]. Lower bound for elongated cell with shot-noise limit and 10^4 s exposure: E_min ≈ 9x10^-3 V/m, giving B_min ≈ 6x10^-4 T for a 0.3 m loop [abstract, PMID 9788920]. Kaune argues the net thermal noise may be lower than assumed, so there may be no barrier [abstract, PMID 12395418]. Adair disputes [PMIDs 12929166, 12483664] | At 1 mT the induced E (0.6-31 mV/m) straddles the Weaver 1998 bound (9 mV/m) and sits above the narrow-band bound (0.1 mV/m). So it is **not excluded** only under favourable assumptions (long exposure, narrow band, signal averaging) | Medium (theory, assumptions-laden) |
| 4 | **Rectification / signal averaging of weak ELF E by membrane proteins (enzymes, pumps, transporters)** | **E**, with integration time and noise | Possible only if exposure is long and noise is favourable; "difficult to reconcile biological effects with low field strengths" [abstract, PMID 7731976]. Stochastic resonance can raise SNR with excess biological noise [same] | Possible in principle for hours-long daily sessions. Not demonstrated at 1 mT in the retrieved set | Low-medium |
| 5 | **Cell-sheet / multicellular amplification (gap-junction coupled, elongated cells, fibre bundles)** | **E** (collective length scale) | Effect depended on cell density: 6 µV/cm (0.6 mV/m), 30 Hz E exposure had no effect at 6x10^3 cells/cm², reduced cell number 25% and doubled ALP at 30x10^3 cells/cm² [abstract, PMID 8213260]. For elongated cell L = 1 mm, polarisation ≈ E·L/2 = 4.5 µV at 9 mV/m [computed by me] | Yes, E at mV/m is the regime tested; the mechanism remains hypothetical | Low-medium |
| 6 | **Electrochemical / ion-binding kinetics (Ca²⁺/calmodulin; "configured signal")** | **Frequency / timing window** set by binding time constants, with **amplitude** relative to thermal noise (Pilla); E at the cell surface | Retuning burst duration allowed 10x lower peak amplitude, about 800x lower average amplitude, about 10^6x lower average power with equal bioeffect (myosin phosphorylation, neurite outgrowth, bone repair) [abstract, PMID 10228567]. Absolute E in V/m or mV/cm: **not reported** in the retrieved abstracts | Pilla's clinical signals are mostly **pulse-modulated RF** (carrier frequency not given in the retrieved abstracts), not ELF. The ELF coil is a different regime | Medium for the "timing window" idea; low for quantitative thresholds |
| 7 | **Lorentz model / ion-parametric / cyclotron resonance (Liboff, Lednev; Muehsam-Pilla)** | **B** (AC and DC amplitude, ratio, frequency) | µT-range fields; resonances at Larmor frequency, dependent on binding lifetime [abstract, PMIDs 19437460, 19437458]. Criticised on physical grounds [abstract, PMIDs 1590822, 9554696, 16437542]. Ca²⁺ cyclotron frequency at 50 µT is 38 Hz; at 1 mT it would be 766 Hz [computed by me, f = qB/2πm] | Defined for µT-scale geomagnetic-like DC plus AC. At 1 mT the resonance condition is far from the 10-100 Hz range | Low (theory contested) |
| 8 | **Radical-pair (spin chemistry, cryptochrome, ROS)** | **B** (quasi-static; frequency-independent up to ~MHz because spin relaxation is µs) | Adair: a 50 µT field changes recombination by a few percent only under narrow conditions; fields as small as 5 µT cannot change rate by 1% [abstract, PMID 10230939]. Zadeh-Haghighi & Simon: "hundreds of studies" show weak-field effects, RPM proposed unifier [abstract, PMID 35919980]. Krylov: RPM could explain frequency-amplitude windows [abstract, PMID 37446167] | Physically allowed and larger at mT than µT (effects of radical pairs are largest when B is comparable to hyperfine fields, order mT) [background, not retrieved]. A pulsed waveform acts through instantaneous |B|, not dB/dt. Unipolar pulse trains carry a DC component | Low-medium (mechanism plausible, in-vivo quantitative link missing) |
| 9 | **Biogenic magnetite torque / mechanical gating** | **B** (and gradient) | Human brain contains ≥5x10^6 single-domain crystals per gram, clumps of 50-100 particles [abstract, PMID 1502184]. Thermal noise masks 60 Hz fields below 5 µT [abstract, PMID 8159681]. Nothing quantitative retrieved at 1 mT | Untested at 1 mT, 10-100 Hz | Low |
| 10 | **Static-field (dB/dt = 0) cell effects** | **B only** | 5 mT (50 G) for 7 days reduced etoposide apoptosis by 57% in cortical neurons via Cav1.2 [abstract, PMID 25171788]; 0.3 T, 2 h/day for 2 weeks changed OPC differentiation and Ca influx [abstract, PMID 28751716] | Shows B-only pathways exist near 5 mT upward. A 1 mT oscillating field has the same |B| order, but no study here compared static versus oscillating at equal B | Medium that B-only effects exist; low that they explain PEMF |
| 11 | **Joule heating** | **J, E** (σE²) | E_rms 0.22 V/m (worst case in my table) gives 1x10^-5 W/kg with σ = 0.2 S/m, ρ = 1000 kg/m³ [computed by me]. RF-AM calcium-efflux windows occurred at SAR ≤ 0.005 W/kg with ΔT < 4x10^-4 °C [abstract, PMIDs 2540755, 7284026] | Negligible | High |
| 12 | **Frequency/amplitude/time "efficacy windows" (empirical)** | Apparent combination of **B (or E) amplitude, pulse frequency, exposure duration, dose number** | MSC chondrogenesis best at 2 mT, 10 min, one exposure, 15 Hz, 6 ms bursts; 1 mT and >3 mT, 5 min or >20 min, and repeated exposures were worse [PMC full text, PMID 28842627]. Osteoblasts: 0.13 mT raised proliferation, 0.32 mT inhibited proliferation and raised ALP [abstract, PMID 17516509]. Induced E 4.8, 8.7, 12.2 µV/cm rms changed osteoclast formation by +50% and -27% depending on intensity [abstract, PMID 12929162]. Cartilage review: peak at 0.1 mT, 60 Hz in endochondral ossification model; 1.5 mT and 4 h in explants [PMC full text, PMID 33970582] | Yes: these are the experiments closest to a 1 mT coil. They do not separate B from dB/dt | Medium that windows are reported; low that they are mechanistically understood |

Short answer to "B or dB/dt?": **for the electrical mechanisms (1-6, 11), dB/dt (hence E) is the driver; for the magnetic mechanisms (7-10), B is the driver; the empirical windows (12) are confounded.** For an ELF coil at ~1 mT the E-driven mechanisms are quantitatively weak and the B-driven ones are unproven.

---

## 2. Standards and the nervous-system benchmark

ICNIRP 2010 (Health Phys 99:818-836; PMID 21068601, DOI 10.1097/HP.0b013e3181f06c86): the abstract is **not available** in PubMed ("[Abstract not available]"). **The PMID supplied in the task (20142652) did not come up; the correct record is 21068601.** The 2020 ICNIRP knowledge-gaps statement is PMID 32251081 (DOI 10.1097/HP.0000000000001261); its abstract confirms that the guidelines are the 1 Hz-100 kHz document and lists data gaps but contains no limit values.

What can be cited from retrieved records:
- Basic restrictions are expressed as **induced E in tissue**, not B (title and use in PMIDs 27340133, 23404214, 36595233).
- Magne & Deschamps 2016 (PMID 27340133): for uniform 50 Hz exposure, the ICNIRP 2010 **occupational** basic restrictions correspond to **2 mT (central nervous system) and 7 mT (peripheral nervous system)** magnetic field, or 35 kV/m electric field [abstract].
- Chen 2013 (PMID 23404214): in five anatomical models between 10 Hz and 100 kHz, exposure at ICNIRP and IEEE **reference levels is not always compliant with basic restrictions**; homogeneous models can underestimate peak spatially averaged E in heterogeneous tissue; revision recommended [abstract].
- Xi 2023 (PMID 36595233): coverage factors of 1-9 (99th percentile) are needed to go from a homogeneous phantom to anatomical models for local near-field sources [abstract].
- Kos 2013 (PMID 24203794): measured induction-heating worker exposure: lower bound of the 0.1 top-percentile induced E = 0.193 V/m at 30 cm from the furnace [abstract].

**Values recalled from the ICNIRP 2010 text, not retrievable here [background, not retrieved; verify]:**
- CNS (head) basic restriction, rms: occupational 0.5/f V/m for 1-10 Hz, 0.05 V/m for 10-25 Hz, 2x10^-3·f V/m for 25-400 Hz; general public 0.1/f, 0.01 V/m, 4x10^-4·f V/m over the same bands. So at 50 Hz: 0.1 V/m (occupational), 0.02 V/m (public); at 10 Hz: 0.05 and 0.01 V/m; at 100 Hz: 0.2 and 0.04 V/m.
- Peripheral nervous system (all tissues): about 0.8 V/m (occupational) and 0.4 V/m (public) up to 3 kHz.
- The CNS limits sit below retinal phosphene thresholds (order 100 mV/m near 20 Hz) with a reduction factor; PNS limits sit below nerve stimulation thresholds.
- IEEE C95.6-2002 / ICES 2019: **not found in PubMed**; numbers not reproduced. It also uses induced in-situ E (brain and heart limits, and a separate peripheral-nerve limit) with corner frequencies, as a function of frequency.

**Comparison using my table (ideal circular loop, uniform B; real bodies can differ by factors of 1-9 per Xi 2023):**
- 1 mT peak, 10 Hz, r = 10 cm: E_rms = 2.2 mV/m, below public CNS limit (recalled 10 mV/m).
- 1 mT peak, 50 Hz, r = 10 cm: 11 mV/m rms, below public limit (recalled 20 mV/m).
- 1 mT peak, 100 Hz, r = 10 cm: 22 mV/m rms, below public limit (recalled 40 mV/m).
- 10 mT peak, 100 Hz, r = 10 cm: 222 mV/m rms, **above** the recalled occupational CNS limit (200 mV/m) if applied to the head.
- 1 mT with 50 µs edges: 20 T/s; E_pk 0.5 V/m at r = 5 cm; this is the regime in which PNS (rheobase 15-26 T/s whole-body, PMID 10318720) and the PNS basic restriction become relevant.

Strength-duration (Bourland 1999, PMID 10318720): with b = 15-26 T/s and c = 0.37 ms, the fitted threshold would be 20.6-35.6 T/s for a 1 ms ramp, 26-45 T/s for 500 µs, and 126-218 T/s for 50 µs [computed by me from their formula; extrapolation of a fit made for MRI gradient pulses and subjects on axis].

Local enhancement near conductors: with 10 T/s uniform dB/dt, nerve excitation near an implanted spinal-fusion stimulator was predicted only within 0.14 mm of a bare wire tip; with 20 T/s within 1 mm (PMID 9408135) [abstract]. Metal implants, electrodes and culture-plate inserts alter E locally.

---

## 3. Thermal-noise and detection limit; how a cell polarises

### 3.1 Physics (computed by me, Schwan low-frequency limit; PMID 10920001 generalises it to spheroids)

- Sphere radius a in extracellular field E: **ΔVm = 1.5 · E · a · cosθ** (valid when the membrane charging time constant is short compared with the period).
- Charging time: τ = a·Cm·(1/σi + 1/2σe) with Cm = 0.01 F/m², σi = 0.5 S/m, σe = 1.5 S/m, a = 10 µm gives τ ≈ 0.23 µs [computed by me]; the low-frequency approximation holds well beyond 100 kHz, so for 10-100 Hz the ΔVm follows E in phase.
- Thermal (kT/C) membrane voltage noise, Cm = 1 µF/cm², 310 K: a = 5 µm: 37 µV rms; 10 µm: 18 µV rms; 50 µm: 3.7 µV rms [computed by me; integrated over all frequencies, so the in-band noise is lower]. Weaver & Astumian relate thermal fluctuation and maximal field-induced ΔVm to cell size [abstract, PMID 2300806].
- Elongated cell of length L along E: ΔVm ≈ E·L/2 (limit L ≪ electrotonic length) [computed by me]; Weaver 1998 uses L = 1 mm, r = 25 µm [abstract, PMID 9788920].

| E in tissue (V/m) | ΔVm, a = 5 µm (µV) | a = 10 µm (µV) | a = 50 µm (µV) |
|---|---|---|---|
| 0.001 | 0.0075 | 0.015 | 0.075 |
| 0.01 | 0.075 | 0.15 | 0.75 |
| 0.1 | 0.75 | 1.5 | 7.5 |
| 1 | 7.5 | 15 | 75 |
| 10 | 75 | 150 | 750 |

[All computed by me: ΔVm = 1.5·E·a, peak, at cosθ = 1.]

### 3.2 What the literature says

- Weaver & Astumian 1990 (PMID 2300806): broad-band detectable E about 10^-3 V/cm (0.1 V/m); 10^-6 V/cm (10^-4 V/m) if the response is narrow-band or the enzyme activity signal-averages.
- Astumian, Weaver, Adair 1995 (PMID 7731976): rectification and signal averaging; excess biological noise can increase SNR (stochastic-resonance-like); numerical results: "difficult to reconcile biological effects with low field strengths".
- Weaver, Vaughan, Adair, Astumian 1998 (PMID 9788920): E_min ≈ 9x10^-3 V/m, corresponding to B_min ≈ 6x10^-4 T with a 0.3 m loop. **My check:** a plain Faraday loop of r = 0.3 m gives E_rms = (r/2)·ω·B_rms; solving for 9 mV/m gives 0.16 mT at 60 Hz or 0.19 mT at 50 Hz, about 3-4x less than the quoted 0.6 mT. The abstract does not state the frequency or the conductivity/geometry assumptions, so I cannot say why the numbers differ (possibly a lower frequency; 10 Hz gives 0.95 mT). Flag: **do not reuse the 0.6 mT figure without reading the paper.**
- Kaune 2002 (PMID 12395418): published thermal arguments may omit membrane force fields of thermal origin; net thermal noise may be smaller at power frequency; "there may be no thermal noise barrier". Adair 2003 comment (PMID 12929166, no abstract) and Adair 2003 review (PMID 12483664): fields below thresholds cannot act through direct, resonance, electrostrictive, induced-dipole or radical-pair routes. This is a real disagreement between two sets of physicists, not a settled bound.
- Stochastic resonance: Gartzke & Lange 2002 propose F-actin in microvilli as a signal-averaging, noise-exploiting interaction site (PMID 12372794, review); Zhao 2016 shows SR for weak E in a model neural network of Izhikevich neurons, vanishing when coupling is removed (PMID 28174614, in silico). Both are hypothesis/model papers; neither measures a PEMF threshold. I did **not** find Bianco, Polk or Adair 1991 ELF papers in PubMed through the tools; Adair 1991 (PMID 1669366) concerns external pulsed E up to 100 kV/m producing small internal effects relative to thermal agitation.
- Observed effects at low E (i.e. below, or near, the narrow-band bound): 0.9 mV/m rms (PMID 10790296), 0.5 mV/m rms (PMID 10653624), 6 µV/cm = 0.6 mV/m rms (PMID 8213260), 4.8-12.2 µV/cm rms = 0.48-1.22 mV/m (PMID 12929162). These are 7-19x below the Weaver 1998 bound of 9 mV/m and above the Weaver 1990 narrow-band bound of 0.1 mV/m.

---

## 4. In-vitro dosimetry pitfalls

1. **E is not uniform in a dish; B (nearly) is.** For uniform axial dB/dt and a cylindrical container with insulating walls, E_φ = (r/2)·dB/dt about the container axis, zero at the centre and maximal at the wall [derived by me; standard result; confirm numerically for the actual geometry]. Cells at the centre of a well see about zero E at any B; cells near the wall see the maximum. Also, in a uniform B the E in an insulating-walled container is set by the container geometry about its own axis, not by its position relative to the coil axis [derived by me].
   Examples for 1 mT peak, 50 Hz [computed by me]: 35 mm dish (r = 17.5 mm): E_edge = 2.7 mV/m; 96-well (r ≈ 3.2 mm): 0.50 mV/m; 6-well (r ≈ 47.5 mm, if the plate is treated as one conductor, which it is not): 7.5 mV/m. For 10 mT, 100 Hz in a 35 mm dish: 55 mV/m.
2. **Evidence that response follows E, not B:**
   - McLeod & Collazo 2000 (PMID 10790296): 30 Hz, 1.8 mT rms, MC3T3-E1 monolayers; induced E up to 0.9 mV/m rms; inhibition of alkaline phosphatase at 4, 8, 16 and 64 h; pattern **maps to the intensity of the induced E (R² = 0.5, P < 0.001)** [abstract]. My check: with E = (r/2)ω B, 0.9 mV/m at 1.8 mT, 30 Hz corresponds to r ≈ 5.3 mm, so the effective radius is a few mm (geometry not given in the abstract).
   - Lee & McLeod 2000 (PMID 10653624): 60 Hz, 0.7 mT rms, E 0.5 mV/m rms; cells **oriented parallel to induced E (orthogonal to B)** showed the length decrease; the authors infer a threshold well below 1 mV/m [abstract]. My check: r ≈ 3.8 mm equivalent.
3. **Parasitic capacitive E can swamp induced E.** At 23 kHz, 532 µT rms: parasitic E = 157 V/m rms versus induced E = 1.9 V/m rms (PMID 17570495) [abstract]. Schuderer 2004 (PMID 15515036): sham isolation > 43 dB, parasitic incident E < 1 V/m, vibration < 0.1 m/s² [abstract]. Fields up to 3.6 mT rms. A coil that is not shielded or not grounded imposes an E that has no relation to dB/dt.
4. **Coil heating, vibration, field non-uniformity.** Uniformity of 4% (PMID 28842627) and 1% tolerance volume (PMID 15515036) are reported by careful groups; other studies do not report any.
5. **Sham design.** Sham TMS induced about 5% of the real E and still altered EEG dynamics (PMID 25620925) [abstract]; a "sham" coil that still generates stray E is not a null. In Parate 2017, controls were in the device with no current (0 mT) [PMC full text, PMID 28842627]: a good design, but it cannot separate B from dB/dt.
6. **Metal and geometry.** Implants/wires raise E locally (PMID 9408135); anatomical heterogeneity raises peak E by 1-9x relative to homogeneous phantoms (PMIDs 36595233, 23404214).
7. **3D constructs.** Grunert 2014 (PMID 24782061) validated an in-vitro setup with numerical simulation and measurement of induced potentials in 3D scaffolds at 20 Hz; it is a model for dosimetry reporting.
8. **Vague descriptors.** Rise time is often reported without amplitude; B is reported as "rms" or "peak" without waveform; e.g. Tsai 2007 gives rms amplitudes 0.13-0.32 mT and "300 µs quasi-rectangular induced E pulses at 7.5 Hz" (PMID 17516509) but not dB/dt or E amplitudes in the abstract.

---

## 5. Studies that try to separate B from dB/dt (or E)

| Design | What was held constant | Result | Verdict |
|---|---|---|---|
| Position in dish (McLeod & Collazo 2000, PMID 10790296) | B nearly uniform | Response maps to E | Supports **E** |
| Cell orientation versus E (Lee & McLeod 2000, PMID 10653624) | B and E magnitude fixed; orientation differs | Only cells parallel to induced E changed | Supports **E** |
| Direct E exposure without B (McLeod 1993, PMID 8213260) | B = 0 | 6 µV/cm, 30 Hz E: effects, density-dependent | **E is sufficient** |
| Static B (dB/dt = 0) (PMIDs 25171788, 28751716) | E = 0 | Effects at 5 mT and 0.3 T via Ca channels | **B is sufficient**, different regime |
| Waveform comparison (Zhang 2007, PMID 17886004): rectangular, triangular, sinusoidal, pulsed | Waveform differs, amplitudes not given in abstract | Different outcomes on proliferation, ALP, mineralization; PEMF effect required extracellular Ca and P2 receptor/PLC; sinusoidal only PLC | Waveform matters; cannot partition B from dB/dt without amplitudes (not reported in abstract) |
| Burst retuning (Pilla 1999, PMID 10228567) | Biological outcome | Same bioeffect at 10x lower peak amplitude after retuning burst duration to binding kinetics | Supports a **timing/frequency window** |
| Amplitude series with fixed waveform (Parate 2017, PMID 28842627; Tsai 2007, PMID 17516509; Strauch 2007, PMID 17632344) | Waveform and frequency fixed, B changed | B and dB/dt scale together; non-monotonic in Parate (2 mT optimum) and Tsai (0.13 mT up, 0.32 mT down) | **Confounded** |
| Fixed-B frequency scan or rise-time scan | - | **None found in this PubMed session** | Gap |
| Equal-B sine versus pulse | - | **None found** (Zhang 2007 compares waveforms without amplitude data in the abstract) | Gap |
| TMS-type pulses on cultures (Meyer 2009, PMID 19203881) | 500 µs biphasic rectangular pulses at 3-100 Hz mean pulse frequency | Action potentials not elicited directly; dose-dependent mostly inhibitory network effect; 20,000 pulses at 10 Hz gave 40% inhibition for > 30 min with recovery [abstract]. E amplitude: not reported in abstract | Pulse number and rate matter; E likely the driver |

---

## 6. Amplitude/frequency window evidence and conflict with linear dose models

- **RF carrier with ELF amplitude modulation (Blackman):** enhanced Ca efflux from chick forebrain within narrow power-density windows (1.44-1.67 and ~3.64 mW/cm² at 50 MHz, 16 Hz AM; effects at 1.75, 3.85, 5.57 ... 8.82 mW/cm² but none at 2.30, 4.50, 5.85 ... 14.7 mW/cm²) [abstract, PMIDs 7284026, 2540755]. SAR ≤ 0.005 W/kg. **These are RF, not ELF**, and the original ELF Blackman papers were not retrieved. They illustrate non-monotonic "windows" that a linear dose-response cannot produce.
- **Ion cyclotron/IPR (Liboff):** the Liboff papers were not specifically retrieved (searches returned recent papers; not examined). Criticism: Adair 1992 (PMID 1590822, "for four independent reasons no such mechanism can operate"), 1998 (PMID 9554696, "cannot account for any purported biological effects of weak ELF magnetic fields"), 2006 (PMID 16437542). Counter-model: Muehsam & Pilla 2009 (PMIDs 19437460, 19437458) claim thermal noise contributes to rather than inhibits the Larmor trajectory and fit Ca²⁺ flux, PC-12 neurite and myosin phosphorylation data by Mg²⁺ binding. Review: Krylov & Osipova 2023 (PMID 37446167) covers "resonance-like" frequency-amplitude windows and a radical-pair oscillator model.
- **Bawin-Adey (Ca efflux windows at ELF):** not retrieved.
- **PEMF windows in the therapeutic range:** Parate 2017 (PMID 28842627): efficacy window defined by amplitude, duration, frequency and number of exposures, with calcium influx via TRPC1/TRPV4 (not L-type VGCC: nifedipine had no effect). Intracellular Ca window: 1.25-fold increase promotes, 1.5-fold inhibits chondrogenesis [as cited in the paper]. Tsai 2007 (PMID 17516509): 0.13 mT raised proliferation at 2 and 8 h, 0.32 mT inhibited proliferation. Chang 2003 (PMID 12929162): 4.8, 8.7 and 12.2 µV/cm rms: both enhancement (≈50%) and suppression (≈27%) of osteoclast-like cell formation depending on intensity. Cadossi 2020 (PMID 33970582): 1.5 mT peak, 4 h for proteoglycan in bovine explants; MSC chondrogenesis dose-dependent up to 2 mT and 10 min; 0.1 mT, 60 Hz maximum in endochondral ossification; 7-9 h/day best, shorter and longer worse; early OA cartilage responds, Mankin ≥ 8 does not; 1 h more effective than 4 h on stiffness.
- **Clinical dichotomy** (Leyva Martínez 2026, PMID 42652114): 28 studies, 1060 participants; high-intensity protocols with rapid field variation (e.g. EMTT > 60 kT/s as stated) consistent with improvements in structural pathologies, whereas low-intensity (< 5 mT) protocols often indistinguishable from placebo; waveform and dB/dt are poorly reported. The 60 kT/s figure is quoted from the abstract and not independently checked.
- **Conflict with linear dose models:** a threshold-and-saturation or linear model (dose ∝ B or E × time) cannot give a response that rises, peaks, then falls at higher amplitude or longer time (Parate, Tsai, Chang, Cadossi). Possible explanations: homeostatic feedback (Ca window), receptor desensitisation, interacting resonance conditions, or irreproducible dosimetry. The dossier cannot tell which; I did not find an independent replication of any single window.

---

## 7. Dose metrics proposed or in use

| Metric | Physical meaning | Strength | Weakness |
|---|---|---|---|
| B_peak, B_rms (mT) | Flux density | Easy to measure; right for B-channel (radical pair, magnetite, static) | Blind to frequency and rise time; useless across carriers |
| dB/dt_peak (T/s) or rise time | Rate of change | Governs E; used for nerve thresholds (PMID 10318720) and in clinical reviews (PMID 42652114) | Needs geometry to become E; peak versus average ambiguous |
| Induced E_peak or E_rms (V/m or µV/cm) | Field acting on cells | Used in standards (ICNIRP, IEEE) and in bone-cell papers (PMIDs 10790296, 12929162); "µV/cm rms" is the Bassett-style unit | Position-dependent in vitro and in vivo; requires modelling (PMIDs 23404214, 36595233) |
| J (A/m²) = σE | Current density | Used in older standards; links to heating (σE²) | Depends on σ, which varies by tissue and frequency |
| "Magnetic dose" B × time (mT·h) | Exposure integral | Simple | Windows show it is not monotonic (PMIDs 28842627, 33970582) |
| Pulse number, burst structure, duty cycle, energy per pulse | Pulse-train description | Relevant to inhibitory TMS-like effects (PMID 19203881) and to Pilla's average power argument (PMID 10228567) | "Energy per pulse" is not defined consistently in the retrieved literature |
| Pilla "configured signal" | Burst duration/amplitude matched to Ca/CaM binding kinetics and signal-to-thermal-noise ratio | Explicit mechanism-based rationale (PMID 10228567, 23675615) | Absolute E not reported in the retrieved abstracts; clinical signals are pulse-modulated RF; the number "~1-100 mV/cm" the task asked me to check is **not confirmed** by anything retrieved |
| Amplitude rms for the Pilla PRF animal study | Strauch 2007: 1.0 G (100 µT) clinical signal and 0.02-0.05 G (2-5 µT) configured signals, 30 min twice daily; tensile strength +18% (n.s.), +44%, +59% at 21 days [abstract, PMID 17632344] | Monotonic amplitude-response in a small range | Carrier frequency and dB/dt not stated |

### 7.1 Why B alone misleads across carriers [computed by me]

If the carrier frequency of the pulse-modulated RF signals (PMIDs 17632344, 22940137) is taken to be 27.12 MHz (**my background assumption, not stated in the retrieved abstracts**), then dB/dt = 2π·f·B_peak is 341 T/s at 2 µT, 852 T/s at 5 µT and 1.7x10^4 T/s at 100 µT, with quasi-static E_peak = (r/2)·dB/dt at r = 5 cm of 8.5, 21 and 426 V/m inside a burst. These are orders of magnitude higher than the 0.3 T/s of a 1 mT, 50 Hz ELF coil. The quasi-static formula fails when the skin depth (about 12 cm for σ = 0.6 S/m) or wavelength is not much larger than the geometry, and the average power is lowered by duty cycle, so these numbers only illustrate that "B" does not rank dose across waveform families; they are not a statement about tissue exposure.

---

## 8. Worked computation table

Formulas [computed by me]:
- Sinusoid: B(t) = B_pk·sin(2πft): dB/dt_peak = 2π·f·B_pk.
- Induced E on a circular path of radius r in a uniform axial dB/dt (symmetric conductor): E_pk = (r/2)·dB/dt_pk. For rms values divide sinusoid peaks by √2.
- Trapezoidal pulse with flat top B_pk, linear edges of duration t_edge: dB/dt = B_pk / t_edge on each edge (opposite sign on the trailing edge); E = (r/2)·dB/dt during the edges and zero on the flat top.
- Real tissue: E depends on conductivity boundaries and geometry (factors of 1-9, PMID 36595233); this is an upper-bound-style idealisation for a homogeneous conducting cylinder.

### 8.1 Sinusoid

| f (Hz) | B_pk (mT) | dB/dt_pk (T/s) | E_pk, r = 2 cm (V/m) | r = 5 cm (V/m) | r = 10 cm (V/m) |
|---|---|---|---|---|---|
| 10 | 0.1 | 0.00628 | 6.3e-5 | 1.57e-4 | 3.14e-4 |
| 10 | 1 | 0.0628 | 6.3e-4 | 1.57e-3 | 3.14e-3 |
| 10 | 10 | 0.628 | 6.3e-3 | 1.57e-2 | 3.14e-2 |
| 50 | 0.1 | 0.0314 | 3.1e-4 | 7.9e-4 | 1.57e-3 |
| 50 | 1 | 0.314 | 3.1e-3 | 7.9e-3 | 1.57e-2 |
| 50 | 10 | 3.14 | 3.1e-2 | 7.9e-2 | 0.157 |
| 100 | 0.1 | 0.0628 | 6.3e-4 | 1.57e-3 | 3.14e-3 |
| 100 | 1 | 0.628 | 6.3e-3 | 1.57e-2 | 3.14e-2 |
| 100 | 10 | 6.28 | 6.3e-2 | 0.157 | 0.314 |

### 8.2 Rectangular 1 ms pulse with 50 µs and 500 µs edges

| B_pk (mT) | Edge | dB/dt (T/s) | E, r = 2 cm (V/m) | r = 5 cm (V/m) | r = 10 cm (V/m) |
|---|---|---|---|---|---|
| 0.1 | 50 µs | 2 | 0.02 | 0.05 | 0.1 |
| 0.1 | 500 µs | 0.2 | 0.002 | 0.005 | 0.01 |
| 1 | 50 µs | 20 | 0.2 | 0.5 | 1 |
| 1 | 500 µs | 2 | 0.02 | 0.05 | 0.1 |
| 10 | 50 µs | 200 | 2 | 5 | 10 |
| 10 | 500 µs | 20 | 0.2 | 0.5 | 1 |

Reading the tables:
- **Same B, 10x faster edge: 10x higher E.** B_pk is identical in rows "1 mT / 50 µs" and "1 mT / 500 µs", yet dB/dt and E differ 10-fold. This is the experiment that, to my retrieval, has not been done in cells.
- **A 1 mT sine at 100 Hz (0.63 T/s) has 32x lower dB/dt than a 1 mT pulse with 50 µs edges (20 T/s).** The pulse is near whole-body PNS rheobase (15-26 T/s, PMID 10318720), the sine is not.
- Sine at 1 mT, 50 Hz, r = 5 cm: 7.9 mV/m peak (5.6 mV/m rms), comparable to the lower in-vitro reports (0.5-1.2 mV/m) only for small radii (dish scale, r ~ 3-5 mm, as back-calculated from PMIDs 10790296, 10653624) and about 10x higher than those for r = 5 cm.
- Largest ELF case (10 mT, 100 Hz, r = 10 cm): 0.31 V/m peak, 0.22 V/m rms; this approaches the recalled occupational CNS limit (see Section 2).
- Membrane polarisation at E = 0.0157 V/m, a = 10 µm: 0.24 µV [computed by me], against kT/C noise of 18 µV rms and a needed ~mV.

---

## 9. Studies table (all retrieved via PubMed in this session)

| PMID | First author, year, journal | What it shows | Numbers |
|---|---|---|---|
| 21068601 | ICNIRP, 2010, Health Phys | Guidelines 1 Hz-100 kHz; basic restrictions as induced E; abstract not available | not reported in record (see Section 2) |
| 32251081 | ICNIRP, 2020, Health Phys | Knowledge gaps statement for the 1 Hz-100 kHz guidelines | not reported |
| 27340133 | Magne, 2016, J Radiol Prot | Conservative conversion of ICNIRP 2010 basic restrictions to B/E levels at 50 Hz | Occupational: 2 mT (CNS), 7 mT (PNS), 35 kV/m E |
| 23404214 | Chen, 2013, Bioelectromagnetics | Peak induced E in 5 anatomical head models at ICNIRP/IEEE reference levels, 10 Hz-100 kHz; reference levels not always compliant with basic restrictions | not reported in abstract |
| 36595233 | Xi, 2023, Phys Med Biol | Coverage factors for near-field sources, 12 anatomical models | 99th percentile factors 1-9 |
| 24203794 | Kos, 2013, Bioelectromagnetics | Induced E in workers at induction furnace | 0.193 V/m (lower bound of 0.1% top percentile) at 30 cm |
| 2300806 | Weaver, 1990, Science | Thermal noise limit for cell detection of weak periodic E | ~10^-3 V/cm broad-band; ~10^-6 V/cm narrow-band or signal averaging |
| 7731976 | Astumian, 1995, PNAS | Rectification and signal averaging; excess noise can give SR-like gain | "difficult to reconcile biological effects with low field strengths" |
| 9788920 | Weaver, 1998, Biophys J | Lower threshold for elongated cell (L = 1 mm, r = 25 µm), shot noise, 10^4 s | E_min ≈ 9x10^-3 V/m; B_min ≈ 6x10^-4 T (0.3 m loop) |
| 12395418 | Kaune, 2002, Bioelectromagnetics | Thermal noise may be smaller than assumed | not reported |
| 12929166 | Adair, 2003, Bioelectromagnetics | Comment on Kaune; abstract not available | not reported |
| 12483664 | Adair, 2003, Bioelectromagnetics | Biophysical limits on athermal effects (RF, microwave; interaction classes incl. radical pair) | RF < 10 mW/cm² unlikely athermal |
| 1669366 | Adair, 1991, Health Phys | Pulsed external E: internal fields small relative to thermal agitation | external E up to 100 kV/m |
| 10230939 | Adair, 1999, Bioelectromagnetics | Radical-pair recombination vs very weak fields | 50 µT: small change only in narrow conditions; 5 µT: < 1% |
| 8159681 | Adair, 1994, PNAS | Thermal noise vs 60 Hz fields on biological magnetite | masks fields < 5 µT |
| 1590822 | Adair, 1992, Bioelectromagnetics | Criticism of Lednev's mechanism | not reported |
| 9554696 | Adair, 1998, Bioelectromagnetics | Analysis of ion parametric resonance model | not reported |
| 16437542 | Adair, 2006, Bioelectromagnetics | AC/DC ion-orbit models cannot produce significant effects | not reported |
| 19437460, 19437458 | Muehsam, 2009, Bioelectromagnetics | Lorentz model (parts I, II): thermal noise contributes to Larmor trajectory; fits to Ca²⁺ flux, PC-12, myosin data; Mg²⁺ target | µT-range |
| 35919980 | Zadeh-Haghighi, 2022, J R Soc Interface | Radical pair mechanism as unifying model for weak-field biology (static, hypomagnetic, oscillating) | not reported |
| 37446167 | Krylov, 2023, Int J Mol Sci | Review of frequency-amplitude windows; RPM in biochemical oscillators | not reported |
| 1502184 | Kirschvink, 1992, PNAS | Biogenic magnetite in human brain | ≥5x10^6 crystals/g; > 10^8/g in pia, dura |
| 12372794 | Gartzke, 2002, Am J Physiol Cell | F-actin in microvilli as interaction site; SR and Brownian motor concept | not reported |
| 28174614 | Zhao, 2016, Cogn Neurodyn | SR in noisy network for weak E detection (model) | not reported |
| 10920001 | Kotnik, 2000, Biophys J | Analytical induced transmembrane voltage for spheroids (generalised Schwan) | formula only |
| 16547608 | Pucihar, 2006, Ann Biomed Eng | Numerical ITV on irregular cells | not reported |
| 10318720 | Bourland, 1999, Neuroimaging Clin N Am | PNS strength-duration for MRI gradients in 84 subjects | b = 15 (y), 26 (z) T/s; c = 0.37-0.38 ms; discomfort ~50% above sensation |
| 9408135 | Reilly, 1997, Magn Reson Imaging | Nerve excitation near implant, dB/dt thresholds | 10 T/s: 0.14 mm; 20 T/s: 1 mm |
| 40740830 | Barksdale, 2025, IEEE J Transl Eng Health Med | PNS thresholds 200 Hz-88.1 kHz in head | minimum near 25 kHz; +39% from 25 to 88.1 kHz |
| 10790296 | McLeod, 2000, Radiat Res | ALP inhibition tracks spatial map of induced E | 30 Hz, 1.8 mT rms, E max 0.9 mV/m rms; R² = 0.5 |
| 10653624 | Lee, 2000, Bioelectromagnetics | Morphology depends on cell orientation versus induced E | 60 Hz, 0.7 mT rms, 0.5 mV/m rms |
| 8213260 | McLeod, 1993, J Bone Miner Res | Direct E exposure, density-dependent | 30 Hz, 6 µV/cm rms; 25% fewer cells at 30x10^3 cells/cm² |
| 12929162 | Chang, 2003, Bioelectromagnetics | ELF-PEMF induced E dose on osteoclast formation | 4.8, 8.7, 12.2 µV/cm rms; +50% / -27% |
| 17516509 | Tsai, 2007, Bioelectromagnetics | PEMF on osteoblasts in scaffolds | 0.13, 0.24, 0.32 mT rms; 300 µs pulses, 7.5 Hz |
| 17886004 | Zhang, 2007, Electromagn Biol Med | Rectangular, triangular, sinusoidal, pulsed EMF on osteoblasts: waveform decides | amplitudes not reported in abstract |
| 28842627 | Parate, 2017, Sci Rep | MSC chondrogenesis window; TRPC1/TRPV4 Ca entry | 2 mT, 10 min, once; 6 ms bursts of 20 pulses (150 µs on/off), 15 Hz; "approximate rise time of 17 T/s"; 1-4 mT range; field non-uniformity ≤ 4% |
| 33970582 | Cadossi, 2020, JAAOS Glob Res Rev | PEMF cellular mechanism review (A2A/A3 receptors; dose windows) | 1.5 mT/4 h; 2 mT/10 min; 0.1 mT at 60 Hz; 7-9 h/day |
| 10228567 | Pilla, 1999, Bioelectrochem Bioenerg | Ion/ligand binding kinetics and configured waveform | 10x lower peak, ~800x lower average amplitude, ~10^6x lower average power |
| 23675615 | Pilla, 2013, Electromagn Biol Med | Review: CaM-dependent NO signalling; EMF configured a priori | not reported |
| 22940137 | Pilla, 2012, Biochem Biophys Res Commun | Pulse-modulated RF increases NO ~3-fold (MN9D), ~2-fold (fibroblasts); W-7 blocks | not reported |
| 17632344 | Strauch, 2007, Plast Reconstr Surg | Pulsed RF magnetic field, rat wound tensile strength | 1.0 G; 0.02-0.05 G; +48% (clinical signal); +18% n.s., +44%, +59% |
| 22451021 | Nelson, 2012, Rheumatol Int | Pilla-type PEMF pain reduction in early knee OA, 34 patients | VAS -50 ± 11% vs sham ns |
| 7284026, 2540755 | Blackman, 1980/1989, Bioelectromagnetics | Ca efflux power-density windows with 16 Hz AM RF | 1.44-1.67 and 3.64 mW/cm² (50 MHz); SAR ≤ 0.005 W/kg |
| 25171788 | Ben Yakir-Blumkin, 2014, Neuroscience | Static 50 G protects cortical neurons via Cav1.2 | -57% apoptosis at 7 d |
| 28751716 | Prasad, 2017, Sci Rep | Static 0.3 T on OPC differentiation, Ca influx | 2 h/day, 2 weeks |
| 17570495 | Fujita, 2007, Bioelectromagnetics | 23 kHz in-vitro exposure system | 532 µT rms; induced E 1.9 V/m; parasitic E 157 V/m rms |
| 15515036 | Schuderer, 2004, Bioelectromagnetics | ELF exposure apparatus with artefact characterisation | up to 3.6 mT rms; parasitic E < 1 V/m; sham isolation > 43 dB |
| 14696050 | Rao, 2004, Bioelectromagnetics | Coil system for real-time and downstream endpoints | not reported |
| 24782061 | Grunert, 2014, Cell Biochem Biophys | Simulation plus measurement of electric parameters for 3D scaffolds | 20 Hz; 3x45 min/day |
| 23457046 | Frisch, 2013, Bioelectromagnetics | Direct 10 Hz E fields, HSP70 induction | 20-500 V/m; ~3-fold; peak at 8 h |
| 19203881 | Meyer, 2009, IEEE Trans Biomed Eng | Magnetic pulses on neuronal networks: inhibitory, dose-dependent | 500 µs biphasic; 3-100 Hz; 20,000 pulses at 10 Hz: 40% inhibition |
| 40738401 | Lu, 2025, Brain Stimul | iTBS in organotypic slices; c-Fos depends on induced E orientation | direction-dependent |
| 25620925 | Opitz, 2015, Front Hum Neurosci | Sham cTBS (~5% E) alters EEG | ~5% of real E |
| 8576391 | Nielsen, 1995, J Clin Neurophysiol | Half-cosine pulse, 200 µs rise, 400 µs width; E vs coil geometry | not reported |
| 42652114 | Leyva Martínez, 2026, Biomedicines | Systematic review of dosimetry and clinical response | 28 studies, 1060 pts; EMTT > 60 kT/s (as stated); < 5 mT often placebo-like |
| 17454079, 22388335 | Markov, 2007 / Markov & Colbert, 2000 | Reviews of magnetotherapy, dosimetry principles | not reported in abstracts |
| 18532897 | Colbert, 2008, J Altern Complement Med | 10 essential SMF dosing parameters; dosimetry often not reconstructable from reports | not reported |
| 29887943, 16804297 | Funk, 2018 / Funk & Monsees, 2006 | PEMF/EMF coupling reviews (membrane potential, VGCC) | not reported |

Not found by the tools (so not cited as retrieved): Bianco, Polk, Liboff original papers, Bawin-Adey, Ross, Hu, IEEE C95.6-2002 / ICES 2019, Pilla's mV/cm values, any pulse rise-time-at-constant-B experiment.

---

## 10. Synthesis

**What counts as "dose" depends on the transducer.**
1. *Electrical transducers* (voltage-gated channels, electrodiffusion, nerve, membrane polarisation) respond to E in situ. E = (r/2)·dB/dt only for ideal geometry, so the same B and frequency give different E in a 35 mm dish, a limb or a head. Within these mechanisms there is a time-domain filter (nerve chronaxie 0.37 ms; membrane charging well below 1 µs; binding kinetics for Ca/CaM at the Pilla-type "window") that rewards waveform shape beyond peak dB/dt.
2. *Magnetic transducers* (spin chemistry, magnetite, ion-binding Lorentz/cyclotron models) respond to B (and static fields). dB/dt is irrelevant to them except as it changes instantaneous B.
3. *Empirical windows* (Parate; Tsai; Chang; Cadossi) cannot be assigned to either until B, dB/dt, frequency and exposure time are varied independently.

**Is a 1 mT, 10-100 Hz coil in the electrical regime?** Only weakly. At r ≤ 10 cm the peak E is 0.6-31 mV/m (sine), a polarisation of ≲ 0.5 µV for a 10 µm cell: 10^-2 of kT/C noise and 10^-4 of a gating voltage. It could matter only if (a) detection uses averaging over hours, (b) cells are electrically coupled so that the effective length is millimetres, or (c) the in-vitro low-E reports are right and some non-voltage-gated membrane process is exquisitely sensitive. The in-vitro papers (E ≈ 0.5-1.2 mV/m) are 7-19x below Weaver 1998's bound and none has, to my knowledge, been independently replicated in the retrieved set.

**Pulsed waveforms change the answer.** At the same 1 mT, shortening the edge from 500 µs to 50 µs raises dB/dt from 2 to 20 T/s and E 10x, taking the coil from deep subthreshold into the PNS rheobase range (15-26 T/s whole-body). Sine ELF coils and short-edge pulse coils are therefore different dosimetric classes even at the same B.

**What to report and control in any coil study** (consensus of the dosimetry papers above):
1. B_pk and B_rms at the sample, with measured spatial uniformity (PMID 15515036, 28842627).
2. Waveform, dB/dt_peak, edge times, frequency, burst length, duty cycle, pulse count, session length and number of sessions.
3. Container geometry and medium depth, then computed (or measured) E_peak/E_rms maps; state E at the centre, mean and wall (PMIDs 10790296, 24782061).
4. Parasitic capacitive E, vibration, heating, sham isolation (PMIDs 15515036, 17570495).
5. A control that decouples channels: same B with different dB/dt (rise time or frequency), and a static B or an E-only control (PMIDs 8213260, 25171788).

**Genuinely unsettled** (explicitly): the thermal-noise argument versus mV/m in-vitro reports; whether the efficacy windows survive independent replication; whether Ca/CaM and radical-pair models make quantitative, testable predictions at 1 mT; how much tissue-level amplification lowers thresholds; what the right "dose" for clinical PEMF is, given that clinical reviews report waveform and dB/dt inconsistently (PMID 42652114). Treat every threshold in this dossier as an upper-confidence bound on what a given in-vitro system showed, not as a universal activation threshold.

---

## 11. Key references (PubMed; cite PubMed and DOI)

1. ICNIRP. Guidelines for limiting exposure to time-varying electric and magnetic fields (1 Hz to 100 kHz). Health Phys 2010;99:818-36. PMID 21068601. DOI 10.1097/HP.0b013e3181f06c86. (Task listed PMID 20142652; the PubMed record found is 21068601.)
2. ICNIRP. Gaps in knowledge relevant to the 1 Hz-100 kHz guidelines. Health Phys 2020;118:533-42. PMID 32251081. DOI 10.1097/HP.0000000000001261.
3. Weaver JC, Astumian RD. The response of living cells to very weak electric fields: the thermal noise limit. Science 1990;247:459-62. PMID 2300806. DOI 10.1126/science.2300806.
4. Astumian RD, Weaver JC, Adair RK. Rectification and signal averaging of weak electric fields by biological cells. PNAS 1995;92:3740-3. PMID 7731976. DOI 10.1073/pnas.92.9.3740.
5. Weaver JC, Vaughan TE, Adair RK, Astumian RD. Theoretical limits on the threshold for the response of long cells to weak ELF electric fields. Biophys J 1998;75:2251-4. PMID 9788920. DOI 10.1016/S0006-3495(98)77669-6.
6. Kaune WT. Thermal noise limit on the sensitivity of cellular membranes to power frequency electric and magnetic fields. Bioelectromagnetics 2002;23:622-8. PMID 12395418. DOI 10.1002/bem.10060.
7. Adair RK. Biophysical limits on athermal effects of RF and microwave radiation. Bioelectromagnetics 2003;24:39-48. PMID 12483664. DOI 10.1002/bem.10061. (With: Adair, Effects of very weak magnetic fields on radical pair reformation, PMID 10230939, DOI 10.1002/(sici)1521-186x(1999)20:4<255::aid-bem6>3.0.co;2-w.)
8. McLeod KJ, Collazo L. Suppression of a differentiation response in MC-3T3-E1 osteoblast-like cells by sustained, low-level, 30 Hz magnetic-field exposure. Radiat Res 2000;153:706-14. PMID 10790296. DOI 10.1667/0033-7587(2000)153[0706:soadri]2.0.co;2.
9. Lee JH, McLeod KJ. Morphologic responses of osteoblast-like cells in monolayer culture to ELF electromagnetic fields. Bioelectromagnetics 2000;21:129-36. PMID 10653624. DOI 10.1002/(sici)1521-186x(200002)21:2<129::aid-bem8>3.0.co;2-q.
10. Bourland JD, Nyenhuis JA, Schaefer DJ. Physiologic effects of intense MR imaging gradient fields. Neuroimaging Clin N Am 1999;9:363-77. PMID 10318720. (No DOI in record.)
11. Kotnik T, Miklavcic D. Analytical description of transmembrane voltage induced by electric fields on spheroidal cells. Biophys J 2000;79:670-9. PMID 10920001. DOI 10.1016/S0006-3495(00)76325-9.
12. Magne I, Deschamps F. Electric field induced in the human body by uniform 50 Hz electric or magnetic fields. J Radiol Prot 2016;36:419-36. PMID 27340133. DOI 10.1088/0952-4746/36/3/419.
13. Parate D, et al. Enhancement of mesenchymal stem cell chondrogenesis with short-term low intensity pulsed electromagnetic fields. Sci Rep 2017;7:9421. PMID 28842627. DOI 10.1038/s41598-017-09892-w.
14. Pilla AA, Muehsam DJ, Markov MS, Sisken BF. EMF signals and ion/ligand binding kinetics: prediction of bioeffective waveform parameters. Bioelectrochem Bioenerg 1999;48:27-34. PMID 10228567. DOI 10.1016/s0302-4598(98)00148-2.
15. Fujita A, et al. Development and evaluation of intermediate frequency magnetic field exposure system. Bioelectromagnetics 2007;28:538-45. PMID 17570495. DOI 10.1002/bem.20339; and Schuderer J, et al. In vitro exposure apparatus for ELF magnetic fields. Bioelectromagnetics 2004;25:582-91. PMID 15515036. DOI 10.1002/bem.20037.

Attribution: all bibliographic information above is from PubMed (https://pubmed.ncbi.nlm.nih.gov/) records returned by the PubMed MCP tools; DOI links: https://doi.org/<DOI>.
