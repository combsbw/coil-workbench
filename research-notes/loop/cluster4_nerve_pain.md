# Cluster 4 - Nerve and pain: therapeutic-threshold dossier (PEMF / ELF / peripheral magnetic stimulation)

Source: PubMed MCP tools, session of 2026-10-12. Every PMID/DOI below was returned by the tools in this session. Numbers come from abstracts (or PMC full text where stated). "n/r" = not reported in the retrieved text. "computed by me" = my arithmetic, formula and geometry stated. Where a number comes from my background knowledge rather than a retrieved paper it is marked UNVERIFIED-IN-SESSION. Rate limits (shared PubMed endpoint) restricted full-text reading, so most rows rest on abstracts.

Conventions used in all computed values:
- Sinusoid: dB/dt_peak = 2*pi*f*B_peak.
- Uniform B over a circular loop of radius r: E = (r/2) dB/dt; for a sinusoid E_peak = pi*f*r*B_peak.
- Strength-duration (SD) law: E_th = E_rheo (1 + t_chron / t). For a sinusoid I take t = half-period = 1/(2f) (an approximation, not a verified ICNIRP formula).

---

## 0. Physics deliverable: nerve-activation induced-E thresholds vs frequency / pulse width

### 0.1 Anchor values retrieved in this session

| Quantity | Value | Source (PMID) | Note |
|---|---|---|---|
| Lowest PNS *sensation* threshold, induced E | 2 V/m; "characteristic frequency above 3 kHz" | Wood 2008 (18381600) | Review/analysis of literature; sensation-to-pain margin small, large inter-individual variation |
| Magnetophosphene (retina) threshold | 56 mV/m (95% CI 2-1330 mV/m), characteristic frequency 20 Hz | Wood 2008 (18381600) | Wide CI; CNS/retina, not nerve axon |
| MR-gradient sensation threshold, SD fit dB/dt = b(1 + c/d) | b = 15 T/s (y-gradient), 26 T/s (z-gradient); c = 0.37 / 0.38 ms; n = 84 humans | Bourland 1999 (10318720) | dB/dt on bore axis. "Uncomfortable" at about +50% above sensation threshold |
| Same, E equivalent | 1.1 V/m (b=15) and 1.95 V/m (b=26) | computed by me: E = (r/2)*b with assumed r = 0.15 m torso radius | r not reported by the paper; E scales linearly with r |
| Chronaxie, forearm, 22 subjects | electrodes 109 +/- 11 us; figure-8 magnetic coil 651 +/- 53 us | Recoskie 2009 (19759411) | Discrepancy persists for ulnar sensory vs motor (Recoskie 2010, 20939088); Reilly 2010 (20124652) attributes part to pulse-width range, waveform fidelity and differing spatial E distributions |
| Chronaxie not a nerve constant | varies inversely with gradient-coil uniform-region size | Zhang 2003 (12815678) | The "chronaxie" depends on the spatial E profile, so SD constants are geometry-dependent |
| Discomfort/pain vs perception | discomfort 50-100% above perception threshold; respiratory stimulation about 300% (dogs) | Schaefer 2000 (10931561), Bourland 1999 | Aβ-sensation to Aδ/pain margin is only about 1.5-2x |
| Local field enhancement | with an implant wire, 10 T/s uniform dB/dt excites a 20-um fibre only within 0.14 mm of a bare tip; 20 T/s within 1 mm | Reilly 1997 (9408135) | Threshold is set by local induced E, not by B or the applied dB/dt |
| Motor-cortex TMS threshold, induced E at cortex | 95 +/- 20 V/m (biphasic), 120 +/- 24 V/m (monophasic) | Danner 2012 (22019330) | Also about 100 V/m (Salvador 2015, 26528134); 99 +/- 26 V/m (Reijonen 2020, 31733284). Short TMS pulses (hundreds of us), pulse width n/r in abstracts |
| Peripheral magnetic stimulation, 15-mm figure-8 mini-coil | E_max 39 V/m (simulated) at 70 A, elicits SNAPs in 11 subjects | Colella 2022 (36502488) | Pulse width n/r in abstract |
| Rat sciatic, rhombus-shaped coil | 25 V, 200 us rise time rectangular pulse evoked CMAPs | Park 2025 (40824993) | E and dB/dt n/r |
| 50 Hz current perception, 1071 people | inter-individual spread of two orders of magnitude; women 0.77x (p=50%) to 0.45x (p=0.5%) the male threshold | Leitgeb 2007 (17495660) | Surface-electrode current, not induced E |
| ICNIRP 2010 (1 Hz-100 kHz) | abstract not available in PubMed | 21068601 | The "E_rheo about 6 V/m, f about 3 kHz" figures in the brief are NOT verifiable from retrieved text (UNVERIFIED-IN-SESSION) |

### 0.2 Table: E needed to excite large myelinated axons at 10 / 50 / 100 Hz (sinusoidal or equivalent), using the SD law

Computed by me. Inputs: rheobase candidates 1.1 V/m (Bourland-derived), 2 V/m (Wood 2008), 6 V/m (brief / ICNIRP, UNVERIFIED-IN-SESSION); chronaxie candidates 0.109 ms (electrical, Recoskie), 0.38 ms (Bourland), 0.651 ms (magnetic, Recoskie). Half-cycle durations: 10 Hz = 50 ms, 50 Hz = 10 ms, 100 Hz = 5 ms.

| Frequency | Half-cycle t | SD factor (1+tau/t), tau = 0.109 / 0.38 / 0.651 ms | Predicted E_th, sensory/motor Aβ/Aα (E_rheo 1.1 - 6 V/m) |
|---|---|---|---|
| 10 Hz | 50 ms | 1.002 / 1.008 / 1.013 | about 1.1 - 6.1 V/m |
| 50 Hz | 10 ms | 1.011 / 1.038 / 1.065 | about 1.1 - 6.4 V/m |
| 100 Hz | 5 ms | 1.022 / 1.076 / 1.130 | about 1.1 - 6.8 V/m |
| 1 kHz (context) | 0.5 ms | 1.22 / 1.76 / 2.30 | about 1.4 - 13.8 V/m |
| 3 kHz (context) | 0.167 ms | 1.65 / 3.28 / 4.91 | about 1.8 - 29 V/m |
| TMS-like pulse, 0.1-0.4 ms | 0.1-0.4 ms | 2.6 - 7.5 (tau 0.38-0.651) | about 3 - 45 V/m; compare 39 V/m (Colella) and 95-120 V/m cortex |

Key reading of the table:
1. In the 10-100 Hz band the SD law says the threshold is essentially the rheobase (flat, within 13%). It does NOT say threshold rises steeply at low frequency. The brief's statement that "threshold rises at low frequency" is not supported by the SD law and not quantified in any retrieved paper. Physiologically, slow ramps are expected to raise threshold further through accommodation (nodal Na inactivation, K activation; Reilly's Frankenhaeuser-Huxley model, 2689806), but I found no retrieved number for the size of that factor at 10-100 Hz. Treat the 10-100 Hz values as lower bounds: sensory E_th >= about 1-6 V/m, probably higher.
2. Motor (Aα) vs sensory (Aβ): Recoskie 2010 (20939088) reports statistically different chronaxie between motor and sensory fibres of the ulnar nerve, but no ordering of rheobase can be read from the abstract. Aδ and C fibres (smaller diameter) require higher E at a given pulse width and are not separately quantified by any retrieved magnetic-stimulation paper (UNVERIFIED-IN-SESSION general knowledge; the retrieved quantitative proxy is the +50-100% sensation-to-discomfort margin).
3. Geometry matters: the same B gives E proportional to loop radius. Limb (r about 0.05 m) gives 3x lower E than torso (r about 0.15 m) for the same B and f.

### 0.3 How far below threshold is a typical PEMF device? (computed by me)

E_peak = pi*f*r*B_peak for a sinusoid; dB/dt_peak = 2*pi*f*B.

| Device setting | dB/dt_peak | E_peak (r = 0.10 - 0.15 m) | Margin below PNS E_th 2 V/m | Below 6 V/m |
|---|---|---|---|---|
| 1 mT, 10 Hz | 0.06 T/s | 0.003 - 0.005 V/m | 420 - 640x | 1300 - 1900x |
| 1 mT, 50 Hz | 0.31 T/s | 0.016 - 0.024 V/m | 85 - 127x | 255 - 382x |
| 2 mT, 50 Hz (Elshiwi) | 0.63 T/s | 0.031 - 0.047 V/m | 42 - 64x | 127 - 191x |
| 5 mT, 50 Hz (Taradaj arm B) | 1.57 T/s | 0.079 - 0.118 V/m | 17 - 25x | 51 - 76x |
| 10 mT, 50 Hz (Taradaj arm A, the effective arm) | 3.14 T/s | 0.157 - 0.236 V/m | 8.5 - 13x | 25 - 38x |
| 10 mT, 100 Hz | 6.3 T/s | 0.31 - 0.47 V/m | 4.2 - 6.4x | 13 - 19x |
| 0.3 mT, 2 Hz sinus-equivalent (Sisken protocol; actual pulse shape n/r) | 0.004 T/s | about 0.0002 V/m | about 10,000x | about 30,000x |

Conclusions: with sinusoidal-like waveforms PEMF at 1-10 mT and 10-100 Hz sits 4x to >1000x below the lowest reported PNS sensation threshold. The 50-250 mT uniform-field level would be needed at 50 Hz for E = 2-6 V/m on a 0.15 m radius (B_pk = E/(pi*f*r) = 85 - 255 mT; computed by me). Caveat: devices with fast edges can have much larger dB/dt than a sinusoid of the same peak B (e.g. 10 mT in 100 us = 100 T/s, giving E = 7.5 V/m at r = 0.15 m, which would be near the SD-law threshold for a 0.1 ms pulse); the actual waveform of most commercial PEMF devices is n/r in the trials below. All studies that report "Gauss" or "mT" without rise time cannot be assigned an E.

---

## 1. Table of studies

Column order: PMID | first author, year, journal | system/model | modality | B | dB/dt | induced E/J | freq/waveform/pulse width | dose/schedule | key result | quality

### 1A. Nerve-activation physics and perception thresholds

| PMID | Study | System | Modality | B | dB/dt | E / J | Freq / waveform / PW | Dose | Key result | Quality |
|---|---|---|---|---|---|---|---|---|---|---|
| 10318720 | Bourland 1999, Neuroimaging Clin N Am | 84 human volunteers, MR gradient coils | Switched gradient fields | n/r | rheobase 15 T/s (y), 26 T/s (z); chronaxie 0.37-0.38 ms | n/r (computed by me: 1.1 and 1.95 V/m, r = 0.15 m) | Trapezoid ramps, durations varied | Threshold tracking | SD fit dB/dt = b(1+c/d); discomfort at about +50% above sensation | Moderate-high (n=84, human) |
| 19759411 | Recoskie 2009, Phys Med Biol | 22 humans, forearm | Figure-8 magnetic coil vs surface electrodes | n/r | n/r | n/r | SD curves; chronaxie 651 +/- 53 us (magnetic) vs 109 +/- 11 us (electric) | Threshold | Chronaxie differs 6x between magnetic and electric stimulation of the same nerve | Moderate |
| 20939088 | Recoskie 2010, Magn Reson Med | Ulnar nerve, healthy volunteers | Electric vs magnetic | n/r | n/r | n/r | Chronaxie sensory vs motor differs | Threshold | Difference between fibre types does not explain electric-magnetic discrepancy; perceived threshold is a valid measure | Moderate |
| 20124652 | Reilly 2010, Phys Med Biol (comment) | Critique of Recoskie | - | - | - | - | - | - | Suggests pulse-width range, waveform fidelity and E-field spatial distribution may explain chronaxie discrepancy | Expert commentary |
| 12815678 | Zhang 2003, Magn Reson Med | Humans, 3 body + 1 head gradient coils | Gradient PNS | n/r | SR_min, dG_min | n/r | Chronaxie varies inversely with DSV | Threshold | Chronaxie is not a single nerve constant; depends on coil/E geometry | Moderate |
| 2689806 | Reilly 1989, Med Biol Eng Comput | Frankenhaeuser-Huxley model | Theory, monophasic/biphasic/sinusoid | - | - | thresholds for induced E | - | - | Neuroelectric model for excitation thresholds by induced currents | Theory (no abstract numbers) |
| 9408135 | Reilly 1997, Magn Reson Imaging | Model: spinal-fusion implant | dB/dt on myelinated fibre | n/r | 10 T/s and 20 T/s uniform | local E | 2 ms constant dB/dt gives lowest threshold | - | 10 T/s excites only within 0.14 mm of bare wire tip | Theory |
| 9799853 / 10931561 | Schaefer 1998 (Magn Reson Imaging Clin N Am); Schaefer 2000 (J Magn Reson Imaging) | Reviews | Gradient fields | - | - | - | - | - | Discomfort at 50-100% above perception; respiratory stimulation about 300% (dogs); cardiac far above | Review |
| 18381600 | Wood 2008, Bioelectromagnetics | Literature analysis | ELF 0-3 kHz | - | - | PNS sensation min 2 V/m; phosphene 56 mV/m (CI 2-1330) | Char. freq > 3 kHz (PNS), 20 Hz (phosphene) | - | E (not J) is the more direct metric | Review/analysis |
| 22004933 | Jokela 2011, Health Phys | Dosimetry review | Motion in static field | - | converted dB/dt | threshold E vs frequency plotted | < 10 Hz | - | ICNIRP 1998 basic restrictions prevent vertigo/other sensations above 1 Hz | Review (numbers not in abstract) |
| 17495660 | Leitgeb 2007, Health Phys | 1071 individuals | Surface-electrode current | - | - | J from simulation | 50 Hz | Threshold | Perception threshold log-normal, 2-order spread; women/children more sensitive | Moderate-high (n large) |
| 22559628 | Weinberg 2012, Med Phys | Humans | Sinusoidal B, 2-183 kHz | n/r | n/r | n/r | 2-183 kHz | Threshold | Thresholds rise sharply above 101 kHz | Context (out of band) |
| 36502488 | Colella 2022, Med Phys | 11 humans + virtual body | 15-mm figure-8 mini-coil, 70 A | n/r | n/r | peak 39 V/m (simulated) | n/r | Single stimuli | SNAPs elicited, 7 mm from coil centre | Moderate (small n) |
| 22019330 | Danner 2012, J Neurosci Methods | 50 healthy humans, TMS | Motor cortex | n/r | n/r | 95 +/- 20 (biphasic), 120 +/- 24 V/m (monophasic) at rMT | TMS pulse, PW n/r | Single | rMT in E terms | Moderate-high |
| 26528134 | Salvador 2015, Front Cell Neurosci | FEM head model | TMS vs tDCS | n/r | n/r | MEP generation threshold about 100 V/m | - | - | Premotor TMS E well below 100 V/m | Modelling |
| 12199550 | Saunders 2002, Health Phys | Review, brain slices | Weak E fields | - | - | in vitro > about 1 mV/mm (= 1 V/m) or about 100 mA/m2; retina 10 mA/m2 | - | - | Subthreshold effects possible below AP threshold; in vivo may be more sensitive | Review |
| 17599962 | Deans 2007, J Physiol | Rat hippocampal slices | Applied AC E field | - | - | 50 Hz: 1 V/m p-p (354 mV/m rms) significant in 71% of slices; 0.5 V/m p-p (177 mV/m rms) in 20% | AC 15-100 Hz; sensitivity at 50-60 Hz about 0.4x DC (0.18 mV per V/m DC) | Seconds | Timing of pyramidal firing within gamma oscillations altered at 70 uV somatic polarisation | Moderate (in vitro) |
| 21693787 | Hirata 2011, Phys Med Biol | Anatomical models | 20 Hz uniform B | 8.14 mT nominal (adult, 20 Hz) | peak about 1.0 T/s (computed by me: 2*pi*20*8.14e-3; rms/peak not stated) | IEEE retinal 53 mV/m; brain 10-70% higher | 20 Hz | - | Phosphene is the lowest-threshold ELF response | Modelling |
| 41865084 | Fresnel 2026, Sci Rep | 62 humans | tAMS sinusoidal B | 50% thresholds, whole-head: 31.5 mT (20 Hz), 22.1 mT (50 Hz), 23.8 mT (60 Hz) (rms as I infer: dB/dt check 2*pi*f*B matches) | 4.0, 6.9, 9.0 T/s (same frequencies) | n/r (EF proportional to dB/dt) | 20/50/60 Hz sine | 5 s exposures | dB/dt chosen as metric; lowest B threshold not at lowest f; 20 Hz most sensitive; retinal/rod origin | Moderate-high (replication) |
| 38740182 / 40973130 | Legros 2024 (Brain Stimul); Bouisset 2025 (Exp Physiol) | 81 / 41 humans | tAMS | 0-50 mT | n/r in abstract | current density; retinal rods | 20, 50, 60, 100 Hz | dark adaptation 42 min | Thresholds frequency-dependent, rising during dark adaptation | Moderate |
| 40610500 | Bouisset 2025, Sci Rep | 20 humans | tACS 0-2 mA | - | - | retinal E estimated | 20, 50, 60, 100 Hz | - | Lowest at 20 Hz; no perceptible phosphene at 100 Hz | Moderate |

### 1B. rPMS / magnetic stimulation: pain, spasticity, motor

| PMID | Study | System | Modality | B | dB/dt | E | Freq / waveform / PW | Dose | Key result | Quality |
|---|---|---|---|---|---|---|---|---|---|---|
| 42147836 | Hui 2026, Front Neurol | 14 RCTs (n=580), stroke upper limb | rPMS dose-response meta-regression | n/r | n/r | n/r | optimum 10 Hz (inverted-U) | 10-20 min/session; plateau at 20-55% MSO; course >= 21 days | FMA-UE SMD 0.91; spasticity SMD -1.15; nerve-targeted > muscle-targeted in subacute stroke | Moderate (meta-regression, heterogeneous) |
| 40248011 | Liao 2025, Front Neurol | 8 RCTs, stroke | rPMS | n/r | n/r | n/r | <= 20 Hz better than > 20 Hz | 15-20 min better than 30 min; round coil better | FMA-UE MD 3.34 (0.53-6.15); MAS MD -0.66; authors: "no articles give a suitable range for rPMS" | Moderate-low (small k) |
| 41594821 | Zschorlich 2026, Brain Sci | 17 vs 17 healthy | 5 Hz rPMS tibial nerve | n/r | n/r | n/r | 5 Hz | 105 to 840 stimuli | Reflex inhibition after as few as 105 stimuli; no dose-dependence (threshold-like) | Low-moderate (exploratory) |
| 38391694 | Zschorlich 2024, Brain Sci | 15 healthy, RCT | 5 Hz rPMS vs tapotement | n/r | n/r | n/r | 5 Hz | single | Tendon reflex -9.8% after rPMS; -17.4% after mechanical tapping | Low-moderate |
| 19763530 | Marz-Loose 2009, Nervenarzt | 53 children, spastic equinus | rPMS S1 root | n/r | n/r | 1.2x motor threshold | 20 Hz | 10 series x 10 s | Tone reduced, effect lasted 1 week; F-wave/H-reflex unchanged | Low (open) |
| 18498680 | Krause 2008, Neurol Res | Healthy | rPMS C7/C8 roots | n/r | n/r | 120% rMT | 20 Hz | 10 series x 10 s | Longer cortical silent period; more intracortical inhibition | Low-moderate |
| 32776765 / 35094616 | Kinoshita 2020 (Int J Rehabil Res); Yang 2022 (Int J Neurosci) | Stroke case series (7, 4) | rPMS 20 Hz (+10 Hz rTMS in Yang) | n/r | n/r | n/r | 20 Hz, 3 s on/27 s off | 4800 pulses/day x 15 days | Gait/tone improvements; no spasticity effect (Kinoshita) | Very low (uncontrolled) |
| 40807031 | Mahisanun 2025, J Clin Med | 27 neck MPS, sham crossover | rPMS | n/r | n/r | n/r | 5-10 Hz | 3900 pulses, 10 min, single | VAS -24.1 vs sham at day 4; effect over about 1 week | Moderate-low (n=27) |
| 40417075 | Vearasilp 2025, J Pain Res | Upper trapezius, post-needling | rPMS | n/r | n/r | n/r | 20 pulses/s, biphasic, 20 trains | 10 min | PPT up vs sham (P=0.002) | Moderate-low |
| 42848808 / 42058983 | Jongutchariya 2026 (PLoS One); Kalbiyev 2026 (Turk J Med Sci) | Trapezius MPS, n=66 / n=75 | rPMS 10 vs 15 min; rPMS vs TENS vs sham | n/r | n/r | n/r | n/r | 10 or 15 min weekly x 4; rPMS course with exercise | 10 vs 15 min equivalent (VAS -4.9/-5.0); rPMS PPT gain > TENS (p=0.013) | Moderate (no sham in first; single-blind second) |
| 40501206 | Pan 2025, Eur J Phys Rehabil Med | 8 RCTs, n=177, chronic MSK pain | rPMS | n/r | n/r | n/r | varies | varies | SMD -1.16 (-1.56 to -0.76), I2=21%; very low quality; all studies "some concerns" | Low (very low GRADE) |
| 38102884 | Dana 2023, Pain Pract | 23 studies (15 RCTs), peripheral neuropathic pain | PMS | n/r | n/r | n/r | n/r | 5-240 min/session, 1 day-1 year | Pain MD -1.64 NRS (-2.73 to -0.56) at 0-1 month only, I2=94%; none at 1-3 or > 3 months; 4 of 9 placebo-controlled RCTs significant | Low (very low GRADE) |
| 39885680 | Leenus 2025, Pain Manag | 6 RCTs (n=279), fibromyalgia | PMS | n/r | n/r | n/r | n/r | 8-40 min, 3-84 days | NRS MD -1.86 (-2.85 to -0.87) at 1-3 months; not at >= 3 months; low quality | Low |
| 24666606 | Leung 2014, Pain Med | 5 patients, neuroma/entrapment | Transcutaneous magnetic stimulation (mPNS) | n/r in abstract (review states up to 1.6 T devices) | n/r | n/r | 0.5 Hz | 400 pulses/session, 3-4 sessions over 2 months | NRS 5.0 -> 0.8 (-84%); allodynia resolved in 3 | Very low (uncontrolled n=5) |
| 25989482 | Leung 2015, Bioelectromagnetics | Healthy, RCT, ulnar nerve | Low-frequency tMS +/- TENS | n/r | n/r | n/r | "low frequency", n/r in abstract | n/r | Real LFTMS reversed TENS-induced sensory CV slowing; selective effect on slow (pain) fibres | Low-moderate (small, abstract only) |
| 42072201 | Bedder 2026, Bioengineering (review) | Narrative review of mPNS/LFPMF | mPNS | up to 1.6 T (RCTs) vs 1-100 mT (wound PEMF) | n/r | n/r | 0.5 Hz, pulse width "290 ms" in text (likely 290 us; typo) | 400 pulses, 13.33 min; 3 daily, then weekly, bi-weekly, monthly | Claims 60-75% immediate relief and Aβ recruitment only at 0.2-5 Hz with 240-290 us; mechanisms are asserted, primary sources not retrieved | Low (advocacy-leaning review, mechanisms unsupported) |
| 22032736 | Zunhammer 2010, Brain Stimul | 10 + control healthy | rTMS cerebellum vs rMS of neck | n/r | n/r | 120% rMT | 1 and 10 Hz | 1000 stimuli | Neck peripheral rMS reproduced the "cerebellar" sensory-threshold change | Moderate (control design) |
| 21415720 | Borckardt 2011, Clin J Pain | 65 healthy, sham-controlled crossover | Motor-cortex rTMS | n/r | n/r | 80-100% rMT | 1, 10 Hz, iTBS | 40 min | Largest effect 10 Hz 100% rMT (d = 0.34); iTBS d = 0.03 | Moderate |
| 42073404 | Modica 2026, Life | 37 LBP, case series | double-coil + handheld rPMS | n/r | n/r | n/r | n/r | n/r | Pain -62.5% post, -87.5% at 1 month; no control | Very low |

### 1C. PEMF / low-intensity pulsed fields for pain

| PMID | Study | System | Modality | B | dB/dt | E | Freq / waveform / PW | Dose | Key result | Quality |
|---|---|---|---|---|---|---|---|---|---|---|
| 29616749 | Taradaj 2018, Adv Clin Exp Med | 106 discopathy LBP, 5 arms, single-blind placebo | Magnetic therapy | A 10 mT; B 5 mT; D 49.2 uT | not reported (computed by me for sine: 3.1, 1.6 T/s; 0.06 T/s for D) | n/r (computed by me, r 0.10-0.15: 0.16-0.24, 0.08-0.12, about 0.003-0.0045 V/m for D) | A,B 50 Hz; D 195 Hz | 20 min, 15 sessions over 3 weeks | Abstract reports positive changes in all outcomes only in group A (10 mT, 50 Hz); effects mostly short-term; abstract does not describe B or D as effective | Moderate (single-blind, 3 active arms) |
| 30177406 | Elshiwi 2018, Braz J Phys Ther | 50 nonspecific LBP | PEMF + physio vs sham + physio | 20 G (2 mT) | n/r | n/r (computed by me 0.03-0.05 V/m) | 50 Hz | 12 sessions/4 weeks | Pain MD 1.52, 95% CI -0.34 to 3.35 (includes 0); function and ROM significant | Moderate-low (pain null by CI) |
| 42146884 | Silva 2026, Front Pain Res | 8 RCTs, orthopaedic pain | Systematic review | PEMF uT-mT; rPMS "10-50 mT" | n/r | n/r | PEMF 1-200 Hz; rPMS 5-100 Hz | 10-30 min, 2-4 weeks | Pain -2 to -3 VAS; authors note B values are device settings, not measured at target; Hartard 50 mT rPMS d=1.56 (acute LBP, 3 sessions); table lists "0.3-250 MHz carrier" for Hartard (implies an RF-modulated device, not ELF) | Low-moderate (no meta-analysis; B unreliable) |
| 41745713 | Lara-Reyes 2026, Neurol Int | 13 RCTs (n=688), neuropathic pain, PEMF vs sham | Meta-analysis | n/r | n/r | n/r | n/r | n/r | Global SMD -1.01 (p=0.03) but I2=92.8%, vanished after trim-and-fill; spinal/radicular SMD -2.35 (-4.42 to -0.29); peripheral neuropathy -0.38 (-0.86 to 0.10) NS | Moderate (honest about heterogeneity) |
| 36343068 | Eid 2022, Medicine | 56 post-herpetic neuralgia | PEMFT vs TENS | n/r | n/r | n/r | n/r | 20 min, 3x/week x 8 weeks | VAS -69% (PEMFT) vs -72% (TENS); no difference; no inert-sham arm | Low-moderate |
| 34238526 | Hochsprung 2020, Neurologia | 24 MS pain | monopolar dielectric PEMF | n/r | n/r | n/r | n/r | n/r | Improvement vs baseline but no significant treatment-placebo difference | Low (null vs placebo) |
| 24308025 | Maestu 2013, Pain Res Manag | 54 women, fibromyalgia, double-blind | Low-intensity transcranial magnetic | n/r in abstract | n/r | n/r | 8 Hz pulsed | 8 weekly sessions | Pressure pain threshold improved from session 1; other benefits by week 6; no difference in depression, fatigue, serotonin | Moderate-low (B n/r) |
| 34905482 | Pareja 2021, Clin Exp Rheumatol | 560 women, FM | Low-intensity TMS add-on | n/r | n/r | n/r | n/r | 20 min weekly x 8 | WPI/SS/FIQ improved, lasting to 24 weeks; add-on to standard treatment, no sham | Low-moderate (open label) |
| 36465321 | Giovale 2022, Rheumatol Immunol Res | 21 FM, pilot | PEMF-TEPT vs placebo | n/r | n/r | n/r | n/r | 4 and 8 weeks | VAS DD -31 points; WPI DD -11 | Low (pilot, n=21) |
| 23238789 | Bosi 2013, Diabetologia | 110 diabetic neuropathy, double-blind | FREMS (electrode-delivered electrical, not a magnetic exposure) | - | - | n/r | frequency-modulated | 3 x 10 sessions over 3 weeks | NCV unchanged; pain reduced transiently after sessions, not at 3 months | Moderate-high (RCT); note: electrical, not magnetic |
| 9111740 | Thomas 1997, Neurosci Lett | Land snail | Pulsed ELF magnetic | about 100 uT peak | n/r | n/r | frequency-modulated pulse; two other waveforms ineffective | 15 min | Antinociception, partially naloxone-reversible | Low (invertebrate; waveform-specific) |
| 10501522 | Kavaliers 1999, Neuroreport | Land snail | 60 Hz | n/r | n/r | n/r | 60 Hz | brief | Light-dependent NO-mediated effect on opioid analgesia | Low (invertebrate) |

### 1D. TENS / electrical mechanism references (suprathreshold E; comparator for frequency coding)

| PMID | Study | System | Modality | Freq | Dose | Key result | Quality |
|---|---|---|---|---|---|---|---|
| 10215661 | Sluka 1999, J Pharmacol Exp Ther | Rats, knee inflammation, spinal microdialysis | TENS | 4 Hz vs 100 Hz | n/r in abstract | Both give about 100% inhibition of hyperalgesia; 4 Hz blocked by low-dose naloxone (mu); 100 Hz needs delta (naltrindole), kappa irrelevant | Moderate (animal, mechanistic) |
| 16236028 | Sluka 2005, J Neurochem | Rats | TENS | 4 vs 100 Hz | n/r | 100 Hz (not 4 Hz) lowers spinal glutamate/aspartate via delta-opioid in inflamed animals | Moderate |
| 38446546 | Ikemoto 2024, Kaohsiung J Med Sci | Rats, formalin | TENS | 4 Hz vs 100 Hz, 30 min pre-emptive | 30 min | 4 Hz: effect 90 min, MOR; 100 Hz: 120 min, DOR | Moderate |
| 18061543 | Hingne 2007, J Pain | Rats | TENS | 4 / 100 Hz | 20 min daily x 4 days | Tolerance by day 4 (cross-tolerance at spinal opioid receptors); prevented by NMDA blockade | Moderate |
| 14614954 / 15911163 | Radhakrishnan 2003 (Neuropharmacology); King 2005 (Pain) | Rats / mice | TENS | 4 / 100 Hz | - | Spinal M1/M3 muscarinic and peripheral alpha-2A receptors also contribute | Moderate |
| 15698629 | Wang 2005, Exp Neurol | Rats | Electroacupuncture | 2/100 Hz alternating | 3 s blocks | Alternating 2/100 Hz 40% more potent than simultaneous, via endomorphin-2 + dynorphin | Moderate |

### 1E. Subthreshold neuromodulation

| PMID | Study | System | Modality | B | dB/dt | E | Freq / waveform | Dose | Key result | Quality |
|---|---|---|---|---|---|---|---|---|---|---|
| 24331545 | Rohan 2014, Biol Psychiatry | 63 depressed (41 BPD, 22 MDD), RCT sham | Low field magnetic stimulation (LFMS) | n/r | n/r | < 1 V/m | 1 kHz oscillating | single 20 min | VAS and HDRS-17 improved (p=0.01, 0.02) only in the combined secondary analysis; subgroup primaries NS | Moderate-low |
| 14702256 | Rohan 2004, Am J Psychiatry | 30 BPD EP-MRSI vs sham vs healthy | EP-MRSI | n/r | n/r | 0.7 V/m (vs rTMS 1-500 V/m) | 1 kHz trapezoid gradient train | single | Mood improved 23/30 vs 3/10 sham | Low (open/uncontrolled elements) |
| 15780843 | Carlezon 2005, Biol Psychiatry | Rats | LFMS | 1.5 G/cm gradient | n/r | 0.75 V/m | n/r | 3 x 20 min | Reduced forced-swim immobility; no locomotor or fear-conditioning effect | Low-moderate (animal) |
| 31692960 | Dufor 2019, Sci Adv | Mouse in vivo + ex vivo | Low-intensity rTMS | n/r in abstract | n/r | authors argue not induced currents | complex biomimetic patterns beat regular patterns | n/r | Axon outgrowth and synaptogenesis require pattern + cryptochrome | Moderate-low (single group, mechanism unreplicated) |

### 1F. Nerve regeneration and axon outgrowth

| PMID | Study | System | Modality | B | dB/dt | E | Freq / waveform | Dose | Key result | Quality |
|---|---|---|---|---|---|---|---|---|---|---|
| 21551571 | Sisken 1990, Restor Neurol Neurosci | DRG culture + rat sciatic crush | PEMF | 0.05 mT (in vitro), 0.3 mT (in vivo); 0.06 mT ineffective | n/r | n/r | 2 Hz | in vivo 3-6 d | Neurite outgrowth up in vitro; +22% regeneration rate in vivo; reducing 0.3 -> 0.06 mT removed pre-exposure effect | Moderate (foundational; single lab) |
| 8216387 | Kanje 1993, Bioelectromagnetics | Rat sciatic, pinch test | PEMF pretreatment | 60 uT and 300 uT | n/r | n/r | 2 pps | 4 h/day x 1-4 d, or 15 min/day x 2 d | Pretreatment increased regeneration distance (various durations; amplitude of each effective arm not given in abstract, tested 60 and 300 uT); 4 h/day x 2 d at 60 uT did not; effect persisted 14 days | Moderate-low |
| 8313945 | Walker 1994, Exp Neurol | Rat crush | PEMF | 0.3 mT | n/r | n/r | 2 Hz | 4 h/day days 1-5 | Toe-spread improved (P=0.001); gait-stance P=0.081; sciatic function index unchanged | Moderate-low |
| 17265446 | Walker 2007, Bioelectromagnetics | Rat crush, 3 amplitudes | EMF | 0.03, 0.3, 3 mT peak | about 3 T/s for 3 mT (computed by me from 1 ms ramp; r about 6.7 mm for the reported E) | 1, 10, 100 uV/cm = 0.1, 1, 10 mV/m at target | bipolar rectangular E, 1 and 0.3 ms; 2 per s | 4 h/day x 5 days | NULL: no difference from sham at any amplitude on toe-spread over 43 days | Moderate (3 doses, blinded) |
| 33797305 | Bademoglu 2021, Electromagn Biol Med | Rat crush | PEMF | 0.3 mT | n/r | n/r | 2 Hz | 4 h/day x 40 days | Better amplitude/latency in week 1 only; no effect at weeks 2, 4, 6 | Low-moderate |
| 37124111 | Lee 2023, Biomed Eng Lett | Rat crush, 6 groups | PEMF +/- BMSC +/- NGF | 1 mT | n/r | n/r | 50 Hz | 1 h/day x 3 weeks | PEMF alone no effect; benefit only with BMSC +/- NGF gene therapy | Low-moderate |
| 37277911 | Keyan 2023, Bioelectromagnetics | Rat, delayed repair at 1 month | PEMF | n/r | n/r | n/r | n/r | n/r | SFI, axon count, BDNF, VEGF up at 4-8 weeks | Low-moderate (parameters n/r) |
| 25448645 / 26044808 | Mohammadi 2014 (Int J Surg); 2015 (Curr Neurovasc Res) | Rat transection + chitosan conduit / BMSC | whole-body PEMF | 0.3 mT | n/r | n/r | 2 Hz | 4 h/day days 1-5 | Faster functional/morphometric recovery vs conduit alone (p<0.05) | Low-moderate (single lab, no blinding stated) |
| 28507996 | Tasbih-Forosh 2017, Bull Emerg Trauma | Rat vein graft | whole-body PEMF +/- predatory stress | n/r | n/r | n/r | n/r | n/r | Faster recovery in PEMF groups (p=0.001) | Low-moderate |
| 9972825 | Longo 1999, J Neurosci Res | Rat sciatic transection | PEMF | n/r | n/r | n/r | n/r | 4 h/day, 6-72 h | PEMF DECREASED NGF in injured nerve (opposite to "NGF up") | Moderate (blinded bioassay) |
| 11298388 | Shah 2001, Bioelectromagnetics | PC6 cells | PEMF | 0.3 mT | n/r | n/r | 2 Hz | 2 h/day x 2 days | NGF-induced neurite outgrowth significantly depressed by PEMF; proliferation unchanged | Moderate-low (negative) |
| 8600302 | Sisken 1995, J Neurosci Res | Rat sciatic fast axonal transport | PEMF | n/r | n/r | n/r | 2 Hz | 15 min-1 h/day x 2 days | NULL: fast axonal transport 373-393 mm/day unchanged | Moderate-low (negative) |
| 25769013 | Lin 2015, J Neural Eng | NS-1 cells, TMS coil | Magnetic stimulation | 30% or 40% machine output | n/r | zone 1 about 5% vs zone 2 about 95% of current density | 1, 5, 10 Hz | twice daily x 3 days | Longest-neurite growth and BDNF up, best at 10 Hz; effect was largest in LOW-current zone 1 | Moderate-low (in vitro) |
| 21712572 | Koppes 2011, J Neural Eng | DRG neurons + Schwann cells, DC E | Direct E | - | - | 0-100 mV/mm; best 50 mV/mm (= 50 V/m) | DC | 8 h | 2x neurite outgrowth with 50 mV/mm; 3.2x with Schwann cells | Moderate (in vitro) |
| 19494423 | Wood 2009, J Neural Eng | Chick DRG, uniform E | Direct E | - | - | 24 or 44 V/m (= 24-44 mV/mm) | DC | 10 min (up to 100 min) | Neurite length up 24 h later even after 10 min; longer stimulation helped on laminin only; branching unchanged | Moderate (in vitro) |
| 27529437 | Kim 2016, ACS Chem Neurosci | Rat hippocampal neurons | Direct E | - | - | >= 100 mV/mm or > 10 h at 10-30 mV/mm: collapse/death; 30 mV/mm at 4-5 DIV | DC | variable | Narrow window; developmental-stage dependent | Moderate (in vitro) |
| 24891494 | Koppes 2014, J Neural Eng | DRG on PLLA fibres | Direct E | - | - | n/r in abstract | - | - | +32% outgrowth by stimulation; +126% with aligned fibres; polarity irrelevant | Moderate |
| 41096580 | Piotrzkowska 2025, Int J Mol Sci | Review | PEMF/LIPUS | - | - | - | - | - | Claims optimal parameters exist; narrative | Low |

---

## 2. Synthesis per target

### Target 1: Direct axonal depolarisation by induced E (nerve stimulation, rPMS, TMS)

- Threshold range (induced E): about 2 V/m lowest reported human PNS sensation threshold (Wood 2008, 18381600), 1.1-2 V/m from MR-gradient rheobase (computed by me from Bourland 1999, 10318720), about 6 V/m per the brief (not verified here). With 0.1-0.4 ms TMS-type pulses the SD law lifts this 3-8x to roughly 3-45 V/m; a 15-mm coil needed about 39 V/m peak (Colella 2022, 36502488). Motor cortex needs about 100 V/m (Danner 2012, 22019330). Discomfort at +50-100% above perception (Schaefer, Bourland).
- Driver: induced E, i.e. dB/dt integrated by the nerve over the pulse (SD law: dB/dt_th = b(1 + c/d), Bourland 1999). B itself is not the variable (static fields of tesla scale do not stimulate; the phosphene/PNS literature uses dB/dt as the metric, Fresnel 2026, 41865084). Duration enters through chronaxie, which is geometry- and fibre-dependent: 0.109 ms electrical vs 0.651 ms magnetic in the same forearm (Recoskie 2009, 19759411); chronaxie scales inversely with coil uniform-region size (Zhang 2003, 12815678). Local field enhancement near conductors or fibre bends controls actual activation (Reilly 1997, 9408135).
- Frequency dependence at 10-100 Hz: SD law predicts approximately flat threshold at rheobase (within 13%), plus an unquantified accommodation penalty at slow ramps. The assertion that thresholds "rise at low frequency" is plausible physiologically but I could not source a number.
- Null / limits: no retrieved study shows direct Aβ activation by any device that delivers < 1 V/m. All rPMS studies that report intensity use it relative to motor threshold (120% MT; 20-55% MSO), i.e. they operate at or above peripheral motor threshold.
- Confidence: high for "E/dB/dt drives suprathreshold nerve stimulation" and for threshold magnitudes within a factor of about 3; moderate for pulse-width/chronaxie constants (they vary 6x between methods); low for any Aδ/C-selective window by frequency.

### Target 2: Pain modulation via Aβ gating and endogenous opioids (TENS-like 50-100 Hz vs 2-10 Hz)

- Evidence is electrical TENS in rats: 100 Hz acts through spinal delta-opioid receptors and suppresses glutamate/aspartate release; 4 Hz acts through mu-opioid receptors (Sluka 1999, 10215661; Sluka 2005, 16236028; Ikemoto 2024, 38446546); 2/100 Hz alternation is more potent than simultaneous delivery (Wang 2005, 15698629). Both involve peripheral alpha-2A and spinal muscarinic receptors (15911163, 14614954). Daily TENS shows tolerance by day 4, preventable by NMDA blockade (Hingne 2007, 18061543): a schedule warning for daily dosing.
- Driver: afferent recruitment (an E/amplitude gate) first, then pulse pattern/frequency to select the neurochemical output. This coding has been shown only for suprathreshold stimulation (TENS intensity is "strong but comfortable"; intensity n/r in the abstracts).
- Relevance to the 50-100 Hz acute / 10-20 Hz recovery use case: the 100 Hz-delta / 4 Hz-mu code supports a high-frequency analgesic band and a low-frequency band, but 10-20 Hz is not the low-frequency TENS band (2-10 Hz, tested at 4 Hz) and was not tested. No retrieved paper demonstrates opioid release or Aβ gating from sub-PNS-E magnetic fields. In human rPMS, sub-20 Hz was better than > 20 Hz for stroke motor recovery (Liao 2025, 40248011) and the dose-response peak was 10 Hz (Hui 2026, 42147836), but this is rPMS at contraction-level E on stroke motor outcomes, not pain.
- Reasonably consistent human clinical effect only for short-term pain relief after PMS (neuropathic NRS -1.64 at 0-1 month, Dana 2023; fibromyalgia -1.86, Leenus 2025; MSK SMD -1.16, Pan 2025), all low or very-low certainty, high heterogeneity, no effect beyond 1-3 months.
- Peripheral-afferent confound: neck rMS reproduced cerebellar rTMS effects on thermal and pain thresholds (Zunhammer 2010, 22032736).
- Confidence: moderate for the TENS frequency-opioid code in rodents; low for transfer to PEMF at sub-threshold E; speculative for 10-20 Hz "recovery" bands.

### Target 3: Subthreshold neuromodulation (cortical excitability, mood, network timing)

- Retinal: magnetophosphenes at 53-56 mV/m (20 Hz); 50% perception 31.5 / 22.1 / 23.8 mT (4.0 / 6.9 / 9.0 T/s) at 20 / 50 / 60 Hz global exposure (Fresnel 2026); none at 100 Hz (tACS, Bouisset 2025, 40610500). Frequency window tuned to rods, so neither B nor dB/dt alone is constant across frequency (B threshold falls 31.5 -> 22.1 mT while dB/dt threshold rises 4.0 -> 6.9 T/s).
- Network: in vitro, 50 Hz AC E of 0.18-0.35 V/m rms shifts firing timing in gamma oscillations (Deans 2007, 17599962); in vitro thresholds > about 1 V/m for classical effects (Saunders 2002, 12199550).
- Clinical: LFMS at 1 kHz, 0.7-1 V/m, single 20 min session; mood improvement only in the pooled secondary analysis (Rohan 2014, 24331545). Computed by me: 0.7 V/m is 6.6-20x below the SD-law PNS threshold at 1 kHz (2.3x rheobase). Fibromyalgia: 8 Hz low-intensity transcranial fields, pressure pain thresholds improved from session 1 (Maestu 2013, 24308025), B not reported; add-on cohort of 560 uncontrolled (Pareja 2021).
- Driver: induced E (and thus dB/dt) amplitude at the target, with frequency windows that are tissue-specific (20 Hz retinal, 1 kHz LFMS by design, 8-10 Hz cortical). Dufor 2019 (31692960) argues pattern and cryptochrome rather than induced currents in mice.
- Confidence: moderate that sub-V/m E affects network timing in vitro and retina; low for clinical neuromodulation efficacy at < 1 V/m; speculative for cryptochrome mechanisms.

### Target 4: Nerve regeneration and repair (axon outgrowth, Schwann cells, NGF/BDNF)

- In vitro direct E: 10-100 mV/mm (10-100 V/m) DC; best 50 mV/mm for DRG (Koppes 2011); 24-44 V/m for 10 min suffices on laminin (Wood 2009); >= 100 mV/mm or > 10 h at 10-30 mV/mm is toxic (Kim 2016). Window is therefore about 20-100 V/m, short duration.
- PEMF in animals uses vastly lower induced E: Walker 2007 estimated 0.1-10 mV/m for 0.03-3 mT and found nothing. Computed by me: 50 V/m / 0.01 V/m = 5000x gap to the in vitro DC optimum. The Sisken-type effects (0.3 mT, 2 Hz, 4 h/day days 1-5; 0.05 mT in vitro) therefore cannot be explained by E amplitude; amplitude windows exist but are narrow (0.3 mT effective, 0.06 mT not; Sisken 1990, Kanje 1993) and repeated nulls exist at the same 0.3 mT (Walker 2007; Bademoglu 2021 beyond week 1; Lee 2023 at 1 mT/50 Hz; Sisken 1995 on axonal transport).
- Biochemical direction is inconsistent: PEMF lowered NGF in injured nerve (Longo 1999) and depressed NGF-driven neurite growth (Shah 2001), but BDNF rose in other work (Lin 2015, Keyan 2023). Lin 2015 found the best neurite growth in the lowest-current zone, which argues against E amplitude as the driver in that dish.
- Driver: unresolved. Candidates: schedule/timing (early window, 2 Hz, 4 h/day), amplitude in B (0.05-0.3 mT, no dB/dt reported), frequency (10 Hz in NS-1), and pattern (Dufor). dB/dt-driven E is the least supported by the data.
- Confidence: moderate for in vitro DC E windows; low for PEMF regeneration (mixed, single-lab, small animal studies, repeated nulls, no clinical RCT retrieved); speculative for mechanism.

### Target 5: Neuropathic pain, fibromyalgia, low back pain trials with exposure parameters

- Effective-amplitude evidence is thin: Taradaj 2018 (10 mT, 50 Hz, 20 min x 15) reported benefit in only that arm of five; Elshiwi 2018 (2 mT, 50 Hz, 12 x 20 min) pain CI crosses zero; Silva 2026 notes device-setting B values are not comparable; Lara-Reyes 2026 shows significance disappears with trim-and-fill and no effect in peripheral neuropathy (SMD -0.38, CI -0.86 to 0.10); Hochsprung 2020 (MS pain) no significant difference to placebo; Bosi 2013 (FREMS, electrical) no NCV change and pain relief not sustained to 3 months.
- rPMS trials: typical 5-20 Hz, 10-15 min, 3,900-4,800 pulses per session, at motor-threshold-referenced intensity, with short-lived effects (about 1 week after one session, Mahisanun 2025) and equivalence of 10 vs 15 min (Jongutchariya 2026).
- Driver: for rPMS, suprathreshold induced E (contraction/afferent volley); for PEMF, not established. Effects are not shown to scale with B or dB/dt across studies because the B values are not comparable and dB/dt is never reported.
- Confidence: low (GRADE low/very low across reviews); short-term effect plausible, long-term not supported.

---

## 3. Direct answer: B vs dB/dt vs frequency vs timing

| Mechanism | Activation driver | Evidence strength |
|---|---|---|
| Action-potential initiation (PNS, rPMS, TMS) | Induced E = f(dB/dt, geometry), integrated over pulse width (SD law); not B | High |
| Pain gating / opioid release | Suprathreshold afferent recruitment (E) THEN frequency/pattern (4 Hz mu, 100 Hz delta in rodents) | Moderate (rodent, electrical) |
| Retinal / CNS subthreshold | E amplitude with tissue frequency tuning (20 Hz retina; B and dB/dt thresholds not frequency-invariant) | Moderate |
| Regeneration by low-B PEMF | Unresolved; narrow B windows (0.05-0.3 mT) and schedule; induced E 4-5 orders below in vitro DC thresholds | Low |
| Low-B analgesia by PEMF (mT range) | Unresolved; one trial suggests 10 mT > 5 mT at 50 Hz | Low |

The quantitative gap: typical PEMF 1-10 mT at 10-100 Hz induces about 0.003-0.5 V/m (computed), 4x to over 1000x below the lowest human PNS sensation threshold (2 V/m) and about 200-30,000x below a motor-cortex TMS threshold (about 100 V/m). Any benefit seen at those settings must be sub-threshold, and the retrieved literature does not establish a mechanism or an amplitude/frequency window for it.

---

## 4. Key references (PMID | DOI)

1. Bourland JD, Nyenhuis JA, Schaefer DJ. Physiologic effects of intense MR imaging gradient fields. Neuroimaging Clin N Am 1999. PMID 10318720 | DOI not returned by PubMed.
2. Recoskie BJ, Scholl TJ, Chronik BA. Discrepancy between human peripheral nerve chronaxie times as measured using magnetic and electric field stimuli. Phys Med Biol 2009. PMID 19759411 | DOI 10.1088/0031-9155/54/19/020
3. Wood AW. ELF electric and magnetic field exposure limits: rationale for basic restrictions (Australian standard). Bioelectromagnetics 2008. PMID 18381600 | DOI 10.1002/bem.20412
4. ICNIRP. Guidelines for limiting exposure to time-varying electric and magnetic fields (1 Hz to 100 kHz). Health Phys 2010. PMID 21068601 | DOI 10.1097/HP.0b013e3181f06c86 (no abstract retrieved)
5. Danner N et al. Effect of individual anatomy on resting motor threshold-computed electric field. J Neurosci Methods 2012. PMID 22019330 | DOI 10.1016/j.jneumeth.2011.10.004
6. Deans JK, Powell AD, Jefferys JGR. Sensitivity of coherent oscillations in rat hippocampus to AC electric fields. J Physiol 2007. PMID 17599962 | DOI 10.1113/jphysiol.2007.137711
7. Fresnel E et al. Reproducible magnetophosphene thresholds induced by tAMS in humans. Sci Rep 2026. PMID 41865084 | DOI 10.1038/s41598-026-44440-5
8. Rohan ML et al. Rapid mood-elevating effects of low field magnetic stimulation in depression. Biol Psychiatry 2014. PMID 24331545 | DOI 10.1016/j.biopsych.2013.10.024
9. Sluka KA et al. Spinal blockade of opioid receptors prevents the analgesia produced by TENS in arthritic rats. J Pharmacol Exp Ther 1999. PMID 10215661 | DOI not returned by PubMed.
10. Taradaj J et al. Impact of selected magnetic fields on the therapeutic effect in lumbar discopathy. Adv Clin Exp Med 2018. PMID 29616749 | DOI 10.17219/acem/68690
11. Dana E et al. Peripheral magnetic stimulation for chronic peripheral neuropathic pain: systematic review and meta-analysis. Pain Pract 2023. PMID 38102884 | DOI 10.1111/papr.13332
12. Lara-Reyes JA et al. Effectiveness of PEMF therapy on neuropathic pain: systematic review and meta-analysis. Neurol Int 2026. PMID 41745713 | DOI 10.3390/neurolint18020028
13. Hui et al. rPMS and upper-extremity motor recovery after stroke: meta-analysis and dose-response. Front Neurol 2026. PMID 42147836 | DOI 10.3389/fneur.2026.1824669
14. Sisken BF et al. Pulsed electromagnetic fields stimulate nerve regeneration in vitro and in vivo. Restor Neurol Neurosci 1990. PMID 21551571 | DOI 10.3233/RNN-1990-13419
15. Walker JL et al. EMF treatment of nerve crush injury in a rat model: effect of signal configuration. Bioelectromagnetics 2007. PMID 17265446 | DOI 10.1002/bem.20302
16. Koppes AN et al. Neurite outgrowth is significantly increased by simultaneous Schwann cells and moderate exogenous electric fields. J Neural Eng 2011. PMID 21712572 | DOI 10.1088/1741-2560/8/4/046023
17. Leung A et al. Transcutaneous magnetic stimulation in post-traumatic peripheral neuropathic pain: a case series. Pain Med 2014. PMID 24666606 | DOI 10.1111/pme.12426

## 5. Limitations of this dossier

- Most entries rest on abstracts. Primary text for Leung/mPNS, Hartard, Kanje, Sisken pulse shapes and ICNIRP/IEEE formulas was not retrievable.
- No retrieved paper gives dB/dt or induced E for any PEMF pain or regeneration trial; every dB/dt or E shown for those trials is computed by me from nominal B and f under a sinusoid assumption and is a lower-bound guess for real pulsed waveforms.
- Aβ vs Aδ vs C recruitment by frequency/pulse width was not found in magnetic-stimulation literature on PubMed in this session; the 0.2-5 Hz / 240-290 us claim comes from a secondary review (Bedder 2026) with no retrieved primary support.
- The brief's rheobase value (6 V/m) and the "threshold rises at low frequency" statement could not be confirmed from retrieved text; retrieved values (Wood 2008) put the lowest threshold at 2 V/m with characteristic frequency above 3 kHz, which means flat threshold below that.
- PubMed tool rate limits (shared across parallel researchers) constrained follow-up retrieval.
