# Cluster 2: adenosine receptors (A2A/A3), anti-inflammatory signalling, PEMF analgesia

Therapeutic-threshold dossier, Cluster 2. All papers below were retrieved via the PubMed MCP tools in this session. PMIDs, DOIs and abstract numbers come from tool output. Anything not in the record is written "not reported" (n.r.). Values marked **[computed by me]** are my own calculations.

Source: PubMed (NCBI), https://pubmed.ncbi.nlm.nih.gov/ ; DOI links resolve at https://doi.org/<DOI>.

## 0. Conventions and the dosimetry caveat

Formulas used for computed values (uniform B over a circular loop of radius r):

- E = (r/2)·dB/dt.
- Sinusoid: dB/dt_pk = 2π·f·B_pk.
- Pulse: dB/dt ≈ B_pk / t_rise.
- Probe-coil measurement: dB/dt = V / (N·A).

**IGEA / I-ONE / Ferrara signal** (the signal behind almost all A2A/A3 data). Parameters: 1.3 ms pulses at 75 Hz (~10% duty), 1.5 mT peak (2.5 mT for osteoblasts). Lin 2011 (PMID 21448989) gives the induced voltage as "2.5 mV"; my earlier reading of the Ferrara descriptions gave 2.0±0.5 mV in a 50-turn, 0.5 cm-ID probe. The Ferrara papers do not report dB/dt or induced E.

- **[computed by me]** dB/dt = 2.0e-3 V / (50 × π(0.25 cm)²) = **2.04 T/s** (1.5–2.5 T/s for 1.5–2.5 mV). The equivalent rise time is B_pk/(dB/dt) ≈ 0.74 ms, which is plausible for a 1.3 ms pulse.
- **[computed by me]** E at loop radius r = 0.5, 1, 2, 3.5, 5 cm is 5.1, 10.2, 20.4, 35.7, 51 mV/m. This assumes uniform B and a circular path. The real well/flask geometry is not reported, so treat these as order-of-magnitude values.
- **[computed by me]** If the same pulse shape is scaled linearly with amplitude, 0.5 mT gives about 0.7 T/s, 3 mT about 4.1 T/s and 2.5 mT about 3.4 T/s.

The central problem for threshold work is that in almost every experiment amplitude (B) and slew rate (dB/dt) were varied together, because the pulse shape was fixed. The data therefore cannot separate B from dB/dt, except in a few non-Ferrara studies (section 3).

**Physical classes that must not be pooled:**

1. mT-range low-frequency pulsed or sinusoidal fields (Ferrara/IGEA, Chinese groups, Demirkazik).
2. µT-range whole-body or specialised pulsed fields (Shupak, Prato).
3. 105 mT sinusoidal 4–12 Hz (MAGCELL).
4. Pulse-modulated RF at 27.12 MHz (Ivivi/Pilla/Rohde/Taylor, ActiPatch/Bagnato). This is a different mechanism (Ca/CaM/NO/cGMP) and a different dose metric (a time-averaged E-field in the kHz–MHz band, not dB/dt in the ELF band).
5. Strong peripheral stimulation (rPMS), which is nerve stimulation and not covered here.

## 1. Study table

Column key: B = peak flux density; dB/dt and E are only filled where reported or computed; "dur." = exposure duration. Quality: IV = in vitro, AN = animal, RCT = randomised controlled trial, MA = meta-analysis, SR = systematic review.

### 1a. Adenosine receptors (A2A, A3): Ferrara group and relatives

| PMID | First author, year, journal | System | Modality | B | dB/dt / E | Freq / waveform / pulse | Dose / schedule | Key result (direction) | Quality |
|---|---|---|---|---|---|---|---|---|---|
| 11976268 | Varani 2002, Br J Pharmacol | Human neutrophils, [3H]-ZM241385 binding | PEMF, Helmholtz-like coils | Intensity-dependent (see section 2.1); plateau ~1.5–3.5 mT, lowest doses smaller or n.s. (from full-text page, **not verified against the table**) | n.r.; computed above for IGEA signal | 1.3 ms pulses, 75 Hz (group's standard; not stated in the abstract) | 1 h gave the main effect; time- and temperature-dependent (abstract) | A2A Bmax 126±10 to 215±15 fmol/mg (P<0.01); Kd unchanged (1.05 vs 1.08 nM); cAMP EC50 of HE-NECA 43 to 10 nM; O2- inhibition EC50 3.6 to 1.6 nM | IV; single group; no independent replication found by me |
| 22012856 | Varani 2011, Bioelectromagnetics | Rat cerebral cortex (intact tissue), cortical neurons, membranes | PEMF | 1.5 and 3 mT | n.r. | n.r. in abstract | Intact tissue: 1.5 mT gave 2.0-fold at 4 h, 1.4-fold at 6 h; 3 mT gave 2.0-fold at 2 h, 1.6-fold at 4 h. Membranes: 1.9-fold (1.5 mT) and 2.2-fold (3 mT) at 2 h | A2A up transiently; A1 and A2A mRNA unchanged. Amplitude and time trade off (3 mT×2 h ≈ 1.5 mT×4 h) | IV/ex vivo; same group |
| 21830213 | Ongaro 2012, J Cell Physiol | Human OA synovial fibroblasts + IL-1β | EMF (Ferrara protocol) | n.r. in abstract | n.r. | n.r. in abstract | n.r. in abstract | A2A and A3 up; PGE2, IL-6, IL-8 down; IL-10 up; no effect on matrix-degrading enzymes | IV; primary human cells; same group |
| 23741498 | Vincenzi 2013, PLoS One | T/C-28a2 chondrocytes; hFOB 1.19 osteoblasts | PEMF | 1.5 mT chondrocytes, 2.5 mT osteoblasts (group standard; not stated in abstract) | n.r. | 1.3 ms, 75 Hz (group standard) | n.r. in abstract | A2A/A3 up; PEMF + agonist further reduced IL-6, IL-8, PGE2, VEGF after IL-1β; OPG up | IV; cell lines |
| 22761760 | Vincenzi 2012, PLoS One | PC12, U87MG tumour lines; cortical neurons | PEMF | n.r. in abstract | n.r. | n.r. | n.r. | A2A/A3 up; NF-κB down (A2A and A3); anti-tumour effect of A3 agonist enhanced | IV; off-target for analgesia but shows NF-κB readout |
| 27639248 | Vincenzi 2016, J Cell Physiol | SH-SY5Y, PC12, N9 microglia, hypoxia/LPS | PEMF | n.r. in abstract | n.r. | n.r. | 2–48 h hypoxia; LPS 24–48 h | HIF-1α down; ROS down; TNF-α, IL-1β, IL-6, IL-8 down in N9 | IV |
| 32998161 | Vinhas 2020, PLoS One | Human tendon cells + IL-1β | PEMF 48 h | n.r. in abstract | n.r. | n.r. | 48 h | Abstract reports A2A modulation and IL-6, PGE2 down, IL-33 up. Note: my full-text read found part of the receptor-binding comparison not significant; **I could not re-verify this at write-up, so treat as unresolved** | IV; human cells |
| 28255202 | Varani 2017, Biomed Res Int | Review | n/a | n/a | n/a | n/a | n/a | Review of the adenosine pathway; no new primary data | Review |
| 37373237 | Moretti 2023, Int J Mol Sci | Knee chondropathy | Adenosine signalling (PDRN) + PEMF | Not extracted | n.r. | Not extracted | Not extracted | Combined-action paper; not used for thresholds | Not appraised |

### 1b. Anti-inflammatory signalling: cells and animals

| PMID | First author, year, journal | System | Modality | B | dB/dt / E | Freq / waveform / pulse | Dose / schedule | Key result (direction) | Quality |
|---|---|---|---|---|---|---|---|---|---|
| 32596310 | Ouyang 2020, Biomed Res Int | Mouse DMM synovitis and air-pouch model | PEMF | 1.5 mT | **[computed by me]** ~2 T/s if the Ferrara pulse shape applies (assumption) | Pulse, 75 Hz, 10% duty | n.r. in abstract | IL-1β and TNF-α down; fewer neutrophils, more macrophages; efferocytosis up; p-p38 down | AN; sham-controlled not stated in abstract |
| 39953605 | Zhou 2025, Arthritis Res Ther | C28/I2 chondrocytes + IL-1β; DMM mice | PEMF | n.r. in abstract | n.r. | n.r. | n.r. | Sirt1 up; IL-1β-induced NF-κB activation down; Sirt1 inhibitor EX-527 blocked the effect | IV + AN |
| 34994274 | Liu 2022, Electromagn Biol Med | ACLT + ovariectomy rat OA (n=6/group) | PEMF | 3.82 mT | **[computed by me]** if sinusoidal: dB/dt_pk 0.19 T/s, E 0.96 mV/m at r=1 cm (waveform stated only as "pulse") | 8 Hz pulse | 40 min/day, 5 d/week, 12 weeks | NLRP3, caspase-1, GSDMD, IL-1β, MMP-13 down; cartilage preserved | AN, small n; sham group present |
| 28173722 | Zou 2017, J Int Med Res | Rat nucleus pulposus cells | LF-PEMF | 0.5–3.0 A/m (field strength, not B) | n.r. | 2 Hz | n.r. | Secreted IL-1β and TNF-α fell in an intensity-dependent manner; cellular expression unchanged | IV |
| 28370033 | Kim 2017, Bioelectromagnetics | RAW 264.7 macrophages | Sinusoidal ELF-MF | 0.8 mT | **[computed by me]** dB/dt_pk 0.30 T/s; E 1.5 mV/m at r=1 cm | 60 Hz sinusoid | n.r. in abstract | **Opposite direction:** NO, TNF-α, IL-1β, IL-6 up; NF-κB nuclear translocation up; Ca influx and NFAT2 up | IV; naive cells |
| 21448989 | Lin 2011, Bioelectromagnetics | 7F2 osteoblasts + LPS-stimulated RAW 264.7 co-culture | PEMF | 1.5 mT | Induced voltage 2.5 mV (as reported, geometry n.r.) | 75 Hz, 1.3 ms | 9 h | NO 65 vs 17 µM at day 7 (higher with PEMF); osteoblast proliferation +23%, COL I mRNA 3.4-fold | IV; confirms that the Ferrara signal can raise NO in macrophages |
| 34821733 | Chen 2021, Bioengineering | Macrophages (blinded screen of 22 ELF-PEMF) | ELF-PEMF | n.r. in abstract | n.r. | Fields A and B: fundamental 51.8 and 52.3 Hz, differing **only in send-pause pulse grouping** | n.r. in abstract | A: pro-inflammatory (p-Stat1, CD86, ROS). B: anti-inflammatory (Arg1, IL-10-type, growth factors) | IV; blinded screen; strongest discriminator for "pattern vs amplitude" |
| 32751697 | Vinhas 2020, Int J Mol Sci | Macrophage and IL-1β-primed tendon-cell co-culture | PEMF | n.r. in abstract | n.r. | n.r. | n.r. | Pro-regenerative macrophage phenotype; anti-inflammatory mediators up; FAK implicated | IV |
| 31400640 | Merighi 2019, Cytokine | N9 microglia + LPS | PEMF | n.r. in abstract | n.r. | n.r. (group standard 1.3 ms, 75 Hz) | n.r. | TNF-α and IL-1β down via JNK1/2; IL-6 down independent of AC, PLC, PKC, p38, ERK, Akt, caspase-1; ROS, invasion, phagocytosis down | IV |
| 39684558 | Merighi 2024, Int J Mol Sci | SH-SY5Y, N9 microglia (H2O2, Aβ, LPS) | PEMF | n.r. in abstract | n.r. | 1.3 ms, 75 Hz | n.r. | Oxidative stress, mitochondrial damage, cell death down | IV |
| 36048344 | Yang 2022, J Mol Neurosci | Mouse ICH model, BV2 | PEMF | n.r. in abstract | n.r. | n.r. | 4 h/day for 7 days, from 4 h after ICH | Hematoma volume and pro-inflammatory factors down; microglial erythrophagocytosis up via CD36 | AN |
| 36377077 | Xu 2022, Cartilage | AMSC-derived exosomes on IL-1β chondrocytes; rat ACLT | PEMF on donor cells | 1 mT | **[computed by me]** if sinusoidal: 75 Hz 0.47 T/s; 15 Hz 0.094 T/s | 15, 45, 75 Hz | n.r. in abstract | **Frequency comparison at fixed B:** 75 Hz > 45 Hz > 15 Hz for suppressing inflammation and ECM loss | IV + AN |
| 28741320 | Wang 2017, Bioelectromagnetics | RAW 264.7 + RANKL (osteoclastogenesis) | PEMF | 0.5, 1, 2, 3 mT | n.r. | 15 Hz | 2 h/day, 7 days | **Amplitude window:** 0.5 mT inhibited resorption and osteoclast genes; 3 mT enhanced resorption through apoptosis | IV; direct amplitude comparison, bone not inflammation |
| 28842627 | Parate 2017, Sci Rep | MSC chondrogenesis | PEMF | 2 mT | n.r. | 6 ms bursts, 15 Hz | 10 min once, at induction | **Efficacy window** in amplitude, duration and frequency; one dose beat repeated doses; TRP/Ca entry implicated | IV |
| 40391205 | Guarnaccia 2025, JOR Spine | Cell model of inflammation (title: PEMF as countermeasure against inflammatory ...) | PEMF | Not extracted | n.r. | Not extracted | Not extracted | Listed for completeness; I did not extract parameters | Not appraised |
| 42549352 | Sukumar 2026, Smart Med | Macrophages, TRPC1-STING | Magnetic field | Not extracted | n.r. | Not extracted | Not extracted | Cancer-phagocytosis context; **not a failed replication, a different question**; I did not find parameters | Not appraised |

### 1c. Pain: preclinical and mechanistic

| PMID | First author, year, journal | System | Modality | B | dB/dt / E | Freq / waveform | Dose / schedule | Key result (direction) | Quality |
|---|---|---|---|---|---|---|---|---|---|
| 31408675 | Demirkazik 2019, Nitric Oxide | 72 rats, tail-flick and hot-plate | ELF-PEMF | 5 mT | **[computed by me]** if sinusoidal: 1.57 T/s; E 7.9 mV/m at r=1 cm | 50 Hz | 4×30 min/day with 15 min gaps, 15 days; peak effect day 7 | Analgesia increased with NO donor or sGC activator; L-NAME no change. Authors infer analgesia works through the NO pathway | AN; sham not described in abstract |
| 28836499 | Ozdemir 2017, Gen Physiol Biophys | 78 rats, morphine tolerance | ELF-EMF | 5 mT | as above | 50 Hz | same schedule, 15 days | Morphine analgesia up, tolerance down; peak effect day 7 | AN |
| 21381048 | Prato 2011, Bioelectromagnetics | Mouse anti-nociception in shielded environment | ELF-MF added to ~100x-shielded space | 25–500 nT peak | **[computed by me]** at 1000 nT·Hz: dB/dt_pk = 2π×1e-6 = 6.3 µT/s; E ≈ 3 × 10^-8 V/m at r=1 cm | 10–240 Hz | 1 h daily exposure | Attenuation of induced analgesia scales with the **B×f product**; threshold at or below ~1000 nT·Hz | AN; replicated across frequencies; very low field regime |
| 22940137 | Pilla 2012, Biochem Biophys Res Commun | MN9D, fibroblasts | Pulse-modulated RF | n.r. | n.r. | n.r. | 15 min | NO up ~2–3-fold within seconds of LPS; blocked by W-7 | IV; RF, different mechanism |
| 21968643 | Shiiba 2011, Cell Mol Neurobiol | Rat chronic pain | Cutaneous magnetic stimulation | Not extracted | n.r. | Not extracted | Not extracted | Listed for completeness; not used | Not appraised |

### 1d. Clinical: knee OA and other musculoskeletal pain

| PMID | First author, year, journal | Design | Modality | B / field | dB/dt / E | Freq / waveform | Dose / schedule | Key result (direction) | Quality |
|---|---|---|---|---|---|---|---|---|---|
| 24338431 | Li 2013, Cochrane | MA of 9 RCTs, 636 OA patients | EMF | varied | n.r. | varied | 4–26 weeks | Pain MD 15.10/100 (95% CI 9.08–21.13); function MD 4.55 (−2.23 to 11.32, n.s.); QoL n.s.; unclear selective reporting in all nine | MA; low-moderate certainty |
| 42075549 | Chang 2026, Medicina | SR/MA, knee OA | PEMF | varied | n.r. | varied | varied | Included for recency; numbers not extracted here | MA |
| 30552258 | Wu 2018, BMJ Open | MA, OA | PEMF | varied | n.r. | varied | varied | Pooled results as reported by authors; not extracted here | MA |
| 35586276 | Tong 2022, Pain Res Manag | SR/MA, OA | PEMF | varied | n.r. | varied | varied | Not extracted here | MA |
| 42652114 | Leyva Martínez 2026, Biomedicines | SR (28 studies, 1060 participants) | EMTT and PEMF | "Low-intensity" < 5 mT vs high-intensity EMTT >60 kT/s | n.r. | varied | varied | **Authors' conclusion:** low-intensity protocols (<5 mT) often indistinguishable from placebo or active control, especially in nociplastic pain; high-slew EMTT better for structural pathologies; waveform and dB/dt rarely reported | SR with narrative synthesis (SWiM); heterogeneous, exploratory |
| 15979009 | Thamsborg 2005, Osteoarthritis Cartilage | RCT, n=83, knee OA | PEMF | n.r. in abstract | n.r. | n.r. | 2 h/day, 5 d/week, 6 weeks | **Null:** no significant between-group difference; within-group improvement in both arms | RCT, double-blind, sham-controlled |
| 20473540 | Özgüçlü 2010, Clin Rheumatol | RCT, n=40, knee OA | PEMF + hot pack + ultrasound + exercise | n.r. | n.r. | n.r. | 30 min PEMF, 5 d/week, 2 weeks | **Null:** both groups improved; no between-group difference (p = 0.81–0.91) | RCT, sham-controlled; small |
| 11900312 | Pipitone 2001, Curr Med Res Opin | RCT, n=75 (69 analysed), knee OA | Unipolar magnetic device (Medicur) | n.r. | n.r. | n.r. | 6 weeks | **Null on primary comparison;** paired within-group improvements only in the active arm | RCT, double-blind |
| 26705327 | Bagnato 2016, Rheumatology | RCT, n=66 (60 completers), knee OA | Wearable PEMF | 27.12 MHz pulsed RF: 1000 Hz pulse rate, 100 µs burst, ~0.0098 W peak (my full-text read) | **Not ELF; dB/dt not applicable** | RF pulse train | 12 h/day, 1 month | VAS effect −0.73 (95% CI −1.24 to −0.19); WOMAC effect −0.34 (−0.85 to 0.17, n.s.); PPT up | RCT, double-blind, placebo-controlled; RF class |
| 26562074 | Wuschech 2015, Bioelectromagnetics | Partly randomised RCT, n=57, knee OA | MAGCELL, sinusoidal | 105 mT at 1 cm depth | **[computed by me]** dB/dt_pk 2.6 T/s (4 Hz) to 7.9 T/s (12 Hz); E 13–40 mV/m at r=1 cm | 4–12 Hz sinusoid | 2×5 min/day, 18 days | WOMAC pain P<0.001 vs sham | RCT; "partly randomised" is a weakness |
| 41588476 | Lau 2026, J Cachexia Sarcopenia Muscle | RCT, n=60, knee OA | PEMF | n.r. in abstract | n.r. | n.r. | 30 min, 3×/week, 8 weeks | Knee extension torque up at 6 months (p=0.042 vs sham); pain was not the primary endpoint | RCT, sham-controlled |
| 36514244 | Xiang 2022, BMJ Open | **Protocol only** (428 planned), PEMF vs celecoxib | PEMF | 30 mT | **[computed by me]** if sinusoidal: 2.8 T/s | 15 Hz | 40 min/day, 5 d/week, 6 weeks | No results; do not cite as evidence | Protocol |
| 20527063 | Rohde 2010, Plast Reconstr Surg | RCT, n=24, breast reduction | Pulsed RF (device configured to modulate Ca/CaM/NO) | n.r. in abstract | n.r. | n.r. | n.r. | Pain −57% at 1 h, ~3-fold lower at 5 h; narcotics 2.2-fold less; wound IL-1β 275% lower; TNF-α, VEGF, FGF-2 unchanged | RCT, double-blind, sham |
| 25919263 | Rohde 2015, Plast Reconstr Surg | RCT, n=32, TRAM flap | Same device class | n.r. | n.r. | n.r. | n.r. | Pain 2-fold (5 h) and 4-fold (72 h) lower; IL-1β 5-fold lower at 24 h; narcotics 2-fold less | RCT, double-blind |
| 18506512 | Hedén 2008, Aesthetic Plast Surg | RCT pilot, n=42, breast augmentation | Disposable pulsed device | n.r. in abstract | n.r. | n.r. | n.r. | Pain ~3-fold faster fall by POD 3 (p<0.001) | RCT pilot, double-blind |
| 25199571 | Taylor 2014, J Surg Res | Non-randomised cohorts vs historical sham | Pulsed RF | n.r. | n.r. | n.r. | Q4 (20 min per 4 h), Q2 (15 min per 2 h), 5/20 (5 min per 20 min) | **Schedule window:** Q4 and Q2 worked (24 h VAS 43% and 35% of 1 h); 5/20 failed (87%, vs 74% in historical sham, P=0.451) | Prospective, non-randomised, historical sham |
| 29950893 | Sorrell 2018, J Pain Res | RCT, n=36, post-lumbar-surgery pain | PEMF, two pulse widths | n.r. in abstract | n.r. | 42 µs vs 38 µs pulse width | 2×/day, 60 days | 42 µs: back pain −40.2%, leg pain −45.0%; 38 µs: −18.6%, −17.0%; sham −25.6%, −24.5%. Between-group P>0.05 | RCT, double-blind; underpowered; trends only |
| 16770449 | Shupak 2006, Pain Res Manag | RCT, RA (n=13) and fibromyalgia (n=18) | Pulsed LF field | ≤400 µT peak | n.r. | <3 kHz | single 30 min | MPQ pain reduced; effect-size estimates 0.32–0.52, power 0.54 in RA | Small RCT, double-blind |

Not extracted but retrieved (kept out of the analysis above): 26957530 Sværdborg 2016 (abstract not available), 24352823 Paolo 2013 (TKA), 30868475 Lisi 2019, 30177406 Elshiwi 2018, 31575112 Alzayed 2019, 41745713 Lara-Reyes 2026, 38102884 Dana 2023, 39985539 Ilfeld 2025, 36239249 Figueroa 2022, 22451021 Nelson 2012.

## 2. Synthesis per target

### 2.1 A2A adenosine receptor

- **Threshold / range (Ferrara signal).** Upregulation (Bmax up, Kd unchanged) is reported at 1.5 mT peak, 75 Hz, 1.3 ms pulses, after about 1 h or more in neutrophils and 2–6 h in tissue. In human neutrophils the lowest amplitudes tested gave smaller or non-significant increases, with an apparent threshold of about 0.5–1 mT and a plateau at about 1.5–3.5 mT (full-text page, **not verified against the table**). Rat cortex: 1.5 mT peaks at 4 h (2.0-fold), 3 mT at 2 h (2.0-fold), and the effect is transient.
- **Computed exposure at threshold.** The 1.5 mT effective point corresponds to dB/dt ≈ 2 T/s and E ≈ 5–50 mV/m depending on loop radius **[computed by me, section 0]**. The putative ~0.5–1 mT threshold corresponds to ~0.7–1.4 T/s **[computed by me, assuming linear scaling of the same pulse shape]**.
- **Driving variable.** Undetermined. Within the Ferrara data, B and dB/dt are collinear because pulse shape is fixed. The dose behaves like an amplitude × time product (3 mT×2 h ≈ 1.5 mT×4 h), which is a property of B (or dB/dt) integrated over time, not of frequency, since frequency was fixed at 75 Hz.
- **Amplitude window.** Plateau, not a documented decline, up to 3–3.5 mT. No dose-response above 3.5 mT, so no upper boundary is established.
- **Nulls and caveats.** (i) Almost all data come from one network of labs (Ferrara/IGEA), measured by radioligand binding, with no independent replication that I found. (ii) Isolated membranes respond differently from intact cells (Varani 2011: mRNA unchanged), so the effect is not simple transcriptional upregulation. (iii) The tendon-cell paper (32998161) shows A2A modulation in the abstract but I could not re-verify my note that part of the binding comparison was not significant. (iv) Sham/blinding procedures for the in vitro work are not detailed in the abstracts.
- **Confidence: moderate for the existence of the effect at ~1.5 mT with the IGEA signal; low for any threshold below 1 mT; speculative for the B-vs-dB/dt attribution.**

### 2.2 A3 adenosine receptor

- Evidence is parallel to A2A and mostly co-reported with it (synoviocytes, chondrocytes, osteoblasts, tumour lines, neurons), always with the 75 Hz, 1.3 ms signal at 1.5–2.5 mT (group standard; not stated in each abstract). No A3-specific amplitude series was found.
- **Driving variable and window:** not established. **Nulls:** none found, which signals publication/lab concentration and not robustness.
- **Confidence: low to moderate** (same lab network, binding and functional agreement, no independent confirmation).

### 2.3 NF-κB and cytokines (TNF-α, IL-1β, IL-6, IL-8, IL-10, PGE2)

- **Anti-inflammatory direction, mT-range pulses (reasonably consistent):** Ongaro 2012 (PGE2, IL-6, IL-8 down; IL-10 up), Vincenzi 2013 (IL-6, IL-8, PGE2 down), Vincenzi 2016 and Merighi 2019 (TNF-α, IL-1β, IL-6 down in microglia), Ouyang 2020 (1.5 mT, 75 Hz: IL-1β, TNF-α down in vivo), Zhou 2025 (NF-κB down via Sirt1), Liu 2022 (3.82 mT, 8 Hz: IL-1β, MMP-13, NLRP3 down), Zou 2017 (intensity-dependent fall in secreted IL-1β and TNF-α at 2 Hz).
- **Context dependence:** the effect is documented in IL-1β- or LPS-primed or injured cells, not in naive cells. Sinusoidal 60 Hz, 0.8 mT in naive RAW 264.7 raised TNF-α, IL-1β, IL-6, NO and NF-κB translocation (Kim 2017), and the Ferrara signal at 1.5 mT with LPS-stimulated macrophages raised NO (Lin 2011). So "anti-inflammatory" is not a general property of ELF exposure.
- **Threshold:** the only amplitude data are 1.5 mT (Ferrara signal) and Zou's intensity dependence in A/m (not convertible to B without the coil description). Lowest effective B ≈ 1 mT (Xu 2022, 1 mT, frequency-dependent) and the sinusoidal 0.8 mT pro-inflammatory result mark the practical lower range.
- **Driving variable:** frequency/pattern matter (Xu 2022: 75 > 45 > 15 Hz at fixed 1 mT; Chen 2021: grouping alone flips macrophage polarity at similar fundamental frequency). The amplitude evidence is thin.
- **Nulls:** Wound-exudate TNF-α unchanged in Rohde 2010 even where IL-1β fell; clinical OA trials largely null on pain (section 2.5).
- **Confidence: moderate that pulsed fields in the 1–4 mT range can lower IL-1β/IL-6/PGE2 in primed cells; low for numeric thresholds; speculative for the NF-κB mechanism being A2A/A3-mediated in vivo.**

### 2.4 Macrophage / microglia polarisation

- Chen 2021 is the key discriminating dataset: two fields with fundamental ~51.8 and 52.3 Hz, differing in send-pause grouping, produced opposite polarisation (A: Stat1, CD86, ROS up; B: Arg1, anti-inflammatory secretion up). A blinded screen of 22 fields found only two with diverging effects. This argues that the *pulse pattern/timing* matters more than peak B alone, but B, dB/dt and pulse widths were not decomposed in the abstract.
- Microglia: PEMF (Ferrara signal) lowers LPS-induced TNF-α/IL-1β via JNK and reduces ROS, invasion and phagocytosis (Merighi 2019); in ICH, PEMF increases erythrophagocytosis via CD36 (Yang 2022). The direction on phagocytosis differs by context, so "microglial suppression" is also not general.
- Synoviocytes/macrophages in vivo: Ouyang 2020, efferocytosis up with p38 inhibition.
- **Confidence: low to moderate** (few independent labs; no dose-response).

### 2.5 Analgesia

**Preclinical:** 5 mT, 50 Hz in rats gives analgesia that peaks around day 7 (Demirkazik 2019, Ozdemir 2017), and the authors attribute it to the NO pathway; no sham details in the abstracts. Prato 2011 sets a µT-range detection window where the B×f product (~1000 nT·Hz) is the relevant variable in a shielded mouse paradigm, so it is not an OA-relevant dose.

**Clinical, OA:**

- Cochrane 2013: pain MD 15.1/100 but with unclear reporting bias; function and quality of life not significant.
- Individual trials split: positive (Bagnato 2016, RF, effect size small; Wuschech 2015, 105 mT, partly randomised) versus null (Thamsborg 2005, Özgüçlü 2010, Pipitone 2001 primary comparison).
- Leyva Martínez 2026 reports a dosimetric dichotomy: <5 mT often indistinguishable from placebo, high-slew-rate EMTT better for structural conditions (a narrative conclusion on heterogeneous trials, exploratory by the authors' own description).
- **Post-operative pain** is the strongest sham-controlled signal (Rohde 2010/2015, Hedén 2008), but it comes mainly from one device class (pulsed RF with a Ca/CaM/NO design), not ELF/adenosine; I did not find independent replication in my retrieved set, and the Hedén abstract does not state parameters.
- **Schedule window:** Taylor 2014 shows Q4 and Q2 dosing working and 5 min per 20 min failing (non-randomised, historical sham).
- **Pulse width:** Sorrell 2018 shows 42 µs ahead of 38 µs and of sham, but between-group P>0.05; sham arm itself improved 25%.
- **Thresholds for analgesia:** no ELF B or dB/dt threshold can be set from this evidence. The nearest numeric statements are authors' classes (<5 mT low-intensity, EMTT >60 kT/s high-intensity).
- **Confidence: low overall; moderate that some post-operative RF-pulsed regimens reduce early pain; speculative for any adenosine mediation of clinical analgesia (no direct clinical measurement of A2A/A3 was found).**

## 3. Discriminating evidence: B vs dB/dt vs frequency vs timing

1. **Pulse pattern/timing:** Chen 2021 (same ~52 Hz, different send-pause: opposite polarisation). Taylor 2014 (same device, different duty schedule: works vs fails). Parate 2017 (one 10 min exposure beats repeats). Timing is the best-supported "driver" in this cluster.
2. **Frequency at fixed B:** Xu 2022 (1 mT; 75 Hz best).
3. **Amplitude windows (non-monotonic):** Wang 2017 (0.5 mT inhibits, 3 mT enhances, 15 Hz).
4. **Slew rate:** Physio-Stim classic signal (~10 T/s, from my earlier reading, not recomputed here) vs HSR (PMID 34872332, rat distraction osteogenesis, DOI 10.1302/2046-3758.1012.BJR-2021-0274.R1; PMID 35834942, Wang 2022, Am J Sports Med, rat meniscal tear, DOI 10.1177/03635465221105874): HSR 1 h/day matched classic 3 h/day for bone and gave better meniscal repair, but those are bone/meniscus endpoints and the B and pulse shape changed together with slew.
5. **B×f (induced-current) metric:** Prato 2011, in the µT regime only.
6. **Pulse width:** Sorrell 2018 (42 vs 38 µs), a 4 µs difference, trend-level.
7. **Conclusion:** the evidence does not show that B alone drives the effect. Dose appears to depend on *time-varying* properties (pulse pattern, frequency, and likely dB/dt), but no study varied dB/dt at constant B, constant waveform and constant frequency, so a clean dB/dt threshold cannot be stated. For adenosine receptors specifically, B and dB/dt are collinear in all available data.

## 4. Gaps and cautions

- No independent replication of A2A/A3 upregulation outside the Ferrara network was retrieved.
- No induced E or dB/dt was reported in any adenosine paper; all E values here are computed under stated geometry assumptions.
- Several rows (Guarnaccia 2025, Sukumar 2026, Moretti 2023, Shiiba 2011) were retrieved but their parameters were not extracted; they should not be used for thresholds without checking the full text.
- Meta-analytic pain effects are small, heterogeneous and at risk of bias; individual OA trials are frequently null.
- The 27.12 MHz RF literature is included for context only. Its dose metric (average power, pulse repetition) is not comparable with ELF dB/dt.

## 5. Key references (PMID, DOI)

1. 11976268, Varani 2002, Br J Pharmacol, A2A upregulation in neutrophils. DOI 10.1038/sj.bjp.0704695
2. 22012856, Varani 2011, Bioelectromagnetics, A2A in rat cortex at 1.5 and 3 mT. DOI 10.1002/bem.20704
3. 21830213, Ongaro 2012, J Cell Physiol, OA synoviocytes, A2A/A3, PGE2/IL-6/IL-8/IL-10. DOI 10.1002/jcp.22981
4. 23741498, Vincenzi 2013, PLoS One, chondrocytes and osteoblasts. DOI 10.1371/journal.pone.0065561
5. 31400640, Merighi 2019, Cytokine, microglia signalling. DOI 10.1016/j.cyto.2019.154777
6. 34821733, Chen 2021, Bioengineering, send-pause pattern flips macrophage polarity. DOI 10.3390/bioengineering8110167
7. 28370033, Kim 2017, Bioelectromagnetics, pro-inflammatory ELF in naive macrophages. DOI 10.1002/bem.22049
8. 28741320, Wang 2017, Bioelectromagnetics, amplitude window 0.5 vs 3 mT. DOI 10.1002/bem.22070
9. 36377077, Xu 2022, Cartilage, frequency comparison at 1 mT. DOI 10.1177/19476035221137726
10. 25199571, Taylor 2014, J Surg Res, schedule window. DOI 10.1016/j.jss.2014.08.007
11. 20527063, Rohde 2010, Plast Reconstr Surg, pain and IL-1β. DOI 10.1097/PRS.0b013e3181c9f6d3
12. 29950893, Sorrell 2018, J Pain Res, pulse width. DOI 10.2147/JPR.S164303
13. 24338431, Li 2013, Cochrane, EMF for OA. DOI 10.1002/14651858.CD003523.pub2
14. 15979009, Thamsborg 2005, Osteoarthritis Cartilage, null RCT. DOI 10.1016/j.joca.2005.02.012
15. 42652114, Leyva Martínez 2026, Biomedicines, dosimetric dichotomy review. DOI 10.3390/biomedicines14081731

Also cited: 21381048 Prato 2011 (DOI 10.1002/bem.20661); 21448989 Lin 2011 (DOI 10.1002/bem.20668); 26705327 Bagnato 2016 (DOI 10.1093/rheumatology/kev426); 20473540 Özgüçlü 2010 (DOI 10.1007/s10067-010-1453-z); 11900312 Pipitone 2001 (DOI 10.1185/0300799039117061); 28842627 Parate 2017 (DOI 10.1038/s41598-017-09892-w); 32596310 Ouyang 2020 (DOI 10.1155/2020/4307385); 39953605 Zhou 2025 (DOI 10.1186/s13075-025-03492-0).
