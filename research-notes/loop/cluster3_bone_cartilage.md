# Cluster 3 - Bone, cartilage and connective-tissue repair: PEMF/ELF threshold dossier

Scope: osteoblast/osteocyte/osteoclast signalling, chondrocyte matrix, tendon/fibroblast, classical Bassett/Brighton/Pilla/Cadossi signals.
Modalities: fracture/non-union, osteoporosis, osteoarthritis, tendinopathy, spinal fusion.

## 0. Method, provenance and caveats (read first)

- Source: PubMed via MCP tools in this session (search_articles, get_article_metadata, one get_full_text_article call). Every PMID and DOI below was returned by the tool in this session. "DOI none" means the tool returned no DOI.
- About 32 distinct searches were run. Several long or boolean-heavy queries returned 0 hits because the server ANDs every term. Many classical papers (Bassett 1974 non-union series, Brighton CCEF dose papers, Pilla's early dosimetry, Cadossi's dosimetry papers) were NOT retrievable by search, so they are not listed. Their numbers are not asserted here.
- Only abstracts were read for almost all records. The single full text retrieved (Ferroni 2018, PMC5865106) contains no field parameters (device is a commercial dental-implant unit, parameters "not reported"). Where a parameter is not in the abstract it is marked "not reported (abstract)". The paper itself may report it.
- Nothing in this cluster reports a directly measured dB/dt. Induced E is reported by one group only (Chang, Chung-Yuan Christian University). All other dB/dt and E values are marked "computed by me", with formula and assumptions. These computed values are order-of-magnitude plausibility checks, not findings.
- Computation conventions (mine): uniform B over a circular loop of radius r gives E = (r/2) dB/dt. For a sinusoid, dB/dt_peak = 2 pi f B_peak. For a pulse, dB/dt ~ B_pk / t_rise. Unit reminder: 1 V/m = 10 mV/cm; 1 mV/m = 10 uV/cm.
- Quality shorthand: RCT = randomised controlled trial; n = sample size; "single-lab" = no independent replication found in this search.

## 1. Table of studies

### 1a. Bone cells in vitro and ex vivo

| PMID | First author, year, journal | System / model | Modality | B | dB/dt | Induced E / J | Frequency / waveform / pulse width | Dose / schedule | Key result | Quality |
|---|---|---|---|---|---|---|---|---|---|---|
| 11052501 | Lohmann 2000, J Orthop Res | MG63 human osteoblast-like, Helmholtz coils | Fracture/non-union (clinical signal) | not reported (abstract) | not reported | not reported | Burst of 20 pulses repeating at 15 Hz (a later paper, PMID 19139991, gives 4.5 ms bursts) | 8 h/day, 1, 2 or 4 days | Proliferation down, ALP-specific activity up (max day 1), collagen and osteocalcin up, PGE2 down and TGF-b1 up at days 1-2 then back to control at day 4 | In vitro, sham coils alternated between incubators (temperature controlled); single-lab; n not in abstract |
| 12568966 | Lohmann 2003, J Orthop Res | MLO-Y4 osteocyte-like and ROS 17/2.8 osteoblast-like | Fracture (clinical signal) | not reported (abstract) | not reported | not reported | PEMF (waveform not in abstract) | 8 h/day for 1, 2 or 4 days (MLO-Y4); 24-72 h (ROS) | MLO-Y4: ALP up, TGF-b1 and PGE2 up (via Cox-1, not Cox-2), no change in cell number or osteocalcin. Both cell types: connexin 43 protein down. ROS 17/2.8: no effect on cell number or osteocalcin (partial null) | In vitro, single-lab |
| 19139991 | Schwartz 2009, Ann Biomed Eng | Human MSC (+BMP-2), NHOst, MG63, SaOS-2 on calcium phosphate vs plastic | Fracture/non-union; osteoporosis (OPG/RANKL) | not reported (abstract) | not reported | not reported | 4.5 ms bursts of 20 pulses, 15 Hz | 8 h/day | On CaP: cell number down, OPG up, RANKL unchanged (OPG/RANKL ratio up). Effect is substrate dependent: not evident on tissue-culture plastic | In vitro, multiple cell lines; same lab as Lohmann |
| 12111759 | Diniz 2002, Bioelectromagnetics | MC3T3-E1 at different maturation stages | Fracture | 7 mT peak | not reported | not reported | 15 Hz pulse burst | Applied at proliferation, differentiation or mineralisation stage | Stimulatory at proliferation and differentiation stages (proliferation, ALP, mineralised area up). INHIBITORY (less bone-like tissue) when applied at mineralisation stage | In vitro; stage-dependence is the key finding; n not in abstract |
| 18230298 | Yang 2007, Zhonghua Lao Dong Wei Sheng Zhi Ye Bing Za Zhi (DOI none) | MC3T3-E1 and primary rat calvarial osteoblasts | Bone (occupational-exposure framing) | 1.55 mT | not reported | not reported | 48 Hz (waveform not in abstract) | 24 or 48 h continuous | MC3T3-E1: NO effect on cell number or differentiation (null). Primary osteoblasts: proliferation up at 48 h; ALP down at 24 h, up at 48 h | In vitro; cell-type- and time-dependent; n not in abstract |
| 17516509 | Tsai 2007, Bioelectromagnetics | Rat calvarial osteoblasts in PLGA scaffolds in bioreactor | Bone tissue engineering | 0.13, 0.24, 0.32 mT (rms) | Computed by me: >= 0.43, 0.8, 1.07 T/s (B_rms/300 us; a lower bound because rms < peak) | Induced-E waveform described as single narrow 300 us quasi-rectangular pulses; value not reported (abstract). Computed by me, E_rms about 1.5-7.6 uV/cm for r = 1.5-3 cm | 7.5 Hz, 300 us quasi-rectangular induced-E pulses | 2 or 8 h/day for 18 days | 0.13 mT: cell number up (days 6, 12), later down; ALP first down then up. 0.32 mT (any duration): proliferation INHIBITED but ALP up. Opposite sign of proliferative effect between 0.13 and 0.32 mT | In vitro 3D; single-lab; n not in abstract |
| 12929162 | Chang 2003, Bioelectromagnetics | Rat bone-marrow cultures, osteoclast-like cell formation | Osteoporosis | not reported | not reported | 4.8, 8.7, 12.2 uV/cm rms (reported by authors) | ELF-PEMF (frequency not in abstract) | 0.5, 2, 8 h/day for 7 days | Osteoclast-like cell formation enhanced (~50%) or suppressed (~27%) depending on induced-E level. TNF-a, IL-1b correlated with osteoclast number | In vitro; only study here that reports induced E; non-monotonic |
| 16987754 | Chang 2006, Connect Tissue Res | Osteoclasts from osteoblast/marrow co-cultures | Osteoporosis | not reported | not reported | 3.0 uV/cm (reported) | 7.5 Hz | 1, 8, 16 h | Apoptosis up at 8 h (+105%) and 16 h (+30%); NO effect at 1 h (duration threshold) | In vitro, single-lab |
| 26891468 | Zhai 2016, Bioelectromagnetics | MC3T3-E1 | Fracture/osteoporosis (Wnt/b-catenin) | 0.5, 1, 2 mT (5, 10, 20 G) | not reported | not reported | 15.38 Hz burst (pulse width not in abstract) | 0.5, 1, 2 or 6 h/day for 3 days | Best proliferation at 2 mT, 2 h/day (highest B and not the longest duration tested). Wnt1, Lrp6, b-catenin, Runx2, collagen I, ALP, OCN up | In vitro; factorial dose x time; single-lab; amplitude window top not bracketed (2 mT was the maximum tested) |
| 25661534 | Yan 2015, Mol Cell Endocrinol | Rat calvarial osteoblasts | Osteoporosis | 0.6 to 3.6 mT in 0.6 mT steps | Computed by me, only if sinusoid: 2 pi x 50 x 0.6e-3 = 0.19 T/s for 0.6 mT; waveform is called "PEMF", shape not in abstract | not reported | 50 Hz | 90 min/day | All intensities raised proliferation, MAXIMUM at 0.6 mT (lowest tested). 0.6 mT also gave top ALP, CFU-f, mineralisation, COL-1, BMP-2. Effect abolished by IFT88 siRNA (primary cilia) | In vitro; amplitude series; same group replicates 0.6 mT/50 Hz in PMIDs 27622883, 30996361, 35355482; not independent of that lab |
| 27622883 | Xie 2016, Bone | Rat calvarial osteoblasts | Osteoporosis (BMP) | 0.6 mT (stated in abstract) | see above | not reported | 50 Hz | not in abstract | Upregulation of BMPRII at cilium base, BMP-Smad1/5/8 activation; knockdown of BMPRII or IFT88 abolishes effect | In vitro mechanism; same lab |
| 30996361 | Ren 2019, Beijing Da Xue Xue Bao (DOI 10.19723/j.issn.1671-167X.2019.02.008) | Rat calvarial osteoblasts | Osteoporosis | 0.6 mT | see above | not reported | 50 Hz | 0.5-2 h | PI3K/AKT up (PI3K peak at 0.5 h, falls with longer exposure), BMP-2, COL-1, OSX up; blocked by LY294002 and by cilia knockdown | In vitro; same lab |
| 35355482 | He 2022, Sheng Wu Gong Cheng Xue Bao (DOI 10.13345/j.cjb.210356) | Rat calvarial osteoblasts | Osteoporosis | 0.6 mT | see above | not reported | 50 Hz | not in abstract | Polycystin-2 on primary cilia required for ALP, Runx2, BMP-2, COL-1, OSX increase (amiloride, RNAi) | In vitro; same lab |
| 29658660 | Zhu 2017, Zhejiang Da Xue Xue Bao (DOI 10.3785/j.issn.1008-9292.2017.12.03) | Rat calvarial osteoblasts | Osteoporosis | 1.8 mT sinusoidal vs 0.6 mT pulsed | Computed by me: sinusoid dB/dt_pk = 2 pi x 50 x 1.8e-3 = 0.57 T/s; PEMF pulse shape not reported, so its dB/dt cannot be computed | not reported | 50 Hz both | 90 min/day, 12 days | Both raise maturation/mineralisation. PEMF at 3x LOWER B is more effective (Col-1, BMP-2 mRNA, ALP staining area, nodules) than 1.8 mT sinusoid | In vitro head-to-head; suggests waveform, not B, matters; shape of PEMF unknown |
| 28741320 | Wang P 2017, Bioelectromagnetics | RAW264.7 + RANKL (osteoclastogenesis) | Osteoporosis | 0.5, 1, 2, 3 mT | not reported | not reported | 15 Hz | 2 h/day, 7 days | 0.5 mT DECREASED osteoclast formation/resorption (RANK, NFATc1, TRAP, CTSK down). 3 mT INCREASED apoptosis, BAX/BCL-2 up and resorption enhanced. Authors report an "intensity window" | In vitro; clear non-monotonic window; single-lab |
| 30422320 | Wang P 2019, J Cell Physiol | MLO-Y4 osteocyte-like cells + osteoclast co-culture | Osteoporosis | 0, 5 G (0.5 mT), 30 G (3 mT) | not reported | not reported | 15 Hz | 2 h | Intensity-dependent. 5 G reduced apoptosis genes and the RANKL/OPG ratio; conditioned medium suppressed osteoclast formation; requires primary cilia (polaris siRNA) | In vitro; same lab as Zhai |
| 28965919 | He 2017, Bone | Human marrow macrophage to osteoclast; mixed cultures | Osteoporosis | not reported (commercial Physio-Stim) | not reported | not reported | Commercial Orthofix PEMF | not in abstract | Osteoclast formation strongly inhibited via osteoblast-lineage cells; RNAseq upregulated TGF-b pathway genes, RANKL and OPG, larger changes in cells from older women | In vitro, human primary cells; industry-linked device |
| 27859405 | Wang 2016, Bioelectromagnetics | Human periodontal ligament stem cells +/- BMP9 | Bone/dental | 1.8 or 2.4 mT (other intensities tested, not listed) | not reported | not reported | 15 Hz | 1 h daily | PEMF alone: no effect on proliferation (null). Synergy with BMP9 for osteogenic genes only at 1.8 or 2.4 mT | In vitro; ligand-dependent |
| 28833306 | Tong 2017, Bioelectromagnetics | Osteoblasts, high-extracellular-Ca transient model | Fracture | not reported (abstract) | not reported | not reported | not reported | not reported | PEMF raised proliferation/differentiation AND IGF-1, ALP, Runx2, OCN only when intracellular Ca transients were present; BAPTA-AM abolished; no effect without Ca transients | In vitro; shows cell-state/timing dependence |
| 29572540 | Ferroni 2018, Sci Rep | Human adipose MSC on Ti implants, TNF-a inflammation | Osseointegration | not reported (full text read: no parameters given) | not reported | not reported | Miniaturised commercial device (Magdent) | Continuous for 30 days in incubator | Proliferation, adhesion, osteogenic genes, mTOR-pathway activation up even in TNF-a | In vitro; exposure parameters absent; device-specific |
| 33630907 | Kar 2021, PLoS One | MC3T3-E1, CRISPR Adora2A/Adora3 knockouts | Fracture | not reported (abstract) | not reported | not reported | PEMF (not in abstract) | not in abstract | Adora3 disruption blunts PEMF-driven ALP and differentiation genes; Adora2A disruption delays Alp mRNA only; rescue by re-expression | In vitro genetic loss/rescue, strong mechanistic design |
| 11679602 | Brighton 2001, J Bone Joint Surg Am | MC3T3-E1 | Non-union / spinal fusion (CC, inductive, combined) | not reported (abstract, "appropriate field strengths") | not reported | not reported | Capacitive coupling vs inductive coupling vs combined EM field | 30 min to 24 h; 2 h with inhibitors | All three signals raised DNA content (p<0.05). CC: voltage-gated Ca channel influx (verapamil-sensitive), then PGE2. Inductive and combined: Ca2+ release from intracellular stores (TMB-8-sensitive). All converge on cytosolic Ca2+ and calmodulin (W-7-sensitive) | In vitro; pharmacological inhibitors; Brighton/Pollack |
| 9268690 | Zhuang 1997, Biochem Biophys Res Commun | MC3T3-E1 | Non-union (CCEF) | not applicable (capacitive) | not applicable | not reported | CCEF | not reported | TGF-b1 mRNA up; blocked by verapamil and W-7 (Ca/calmodulin) | In vitro |
| 7639117 | Fitzsimmons 1995, J Bone Miner Res | TE-85 osteosarcoma | Bone | Combined AC + static field (values not reported in abstract) | Computed by me: if E_max = 1e-5 V/m (authors) at 15.3 Hz and r = 1.5 cm, E = (r/2) 2 pi f B_ac gives B_ac about 14 uT (assumes a circular dish of r = 1.5 cm) | 1e-5 V/m (10 uV/m = 0.1 uV/cm), calculated max in medium (reported) | 15.3 Hz combined AC/DC | 30 min | IGF-II receptor number up, FREQUENCY-dependent; IGF-I receptor unchanged | In vitro; extremely low E; supports a non-Faradaic (field/frequency-specific) mechanism, not E magnitude |
| 10228567 | Pilla 1999, Bioelectrochem Bioenerg | Theory + myosin phosphorylation, neurite outgrowth, rabbit fracture model | Fracture | not reported (abstract) | not reported | not reported | Pulsed RF (PRF) with burst duration re-tuned to ion/ligand binding kinetics | not reported | Re-tuned waveform gave bioeffects (phosphorylation, neurite outgrowth, fracture strength) equal to clinical signal at 10x lower peak amplitude, ~800x lower average amplitude, ~10^6x lower average power | Theory-driven; includes animal fracture arm; authors' own model; no independent replication seen |
| 12483712 | Torricelli 2003, J Biomed Mater Res A | MG63 on PMMA +/- alpha-TCP | Bone substitute | 2.3 mT | Computed by me: 2.3 mT / 1.3 ms = ~1.8 T/s (assumes the 1.3 ms pulse is the ramp time; real rise may be faster) | not reported; computed by me, E_pk about 13 mV/m at r = 1.5 cm | 75 Hz, 1.3 ms pulse | 12 h/day, 3 days | Positive on ALP, PICP, OC, TGF-b1; IL-6 down | In vitro; Cadossi/IGEA-type signal |
| 10541767 | Pezzetti 1999, Calcif Tissue Int | Human nasal/articular chondrocytes; osteoblast comparison | Cartilage/bone | 2.3 mT | as above | not reported | 75 Hz | 6-30 h time course | Proliferation up only when serum present (10% or 0.5% FCS in chondrocytes; osteoblasts need 10% FCS); no effect in serum-free medium | In vitro; growth-factor-dependent |

### 1b. Cartilage and joint

| PMID | First author, year, journal | System / model | Modality | B | dB/dt | Induced E / J | Frequency / waveform / pulse width | Dose / schedule | Key result | Quality |
|---|---|---|---|---|---|---|---|---|---|---|
| 11913771 | De Mattei 2001, Connect Tissue Res | Human articular chondrocytes | OA | 2.3 mT | Computed by me ~1.8 T/s (as for PMID 12483712) | not reported | 75 Hz | up to 6 days | Proliferation up in low-density cultures for 6 days if fresh serum added; high-density cultures only first 3 days | In vitro |
| 21412809 | Ongaro 2011, Bioelectromagnetics | Human OA cartilage explants (Outerbridge I and III), +/- IL-1b | OA | 1.5 mT | not reported | not reported | 75 Hz | 1 and 7 days | 35S-sulfate incorporation +49% (PEMF) vs +53% (IGF-I) at 7 d in grade I; additive with IGF-I; counteracts IL-1b | Ex vivo human tissue; n not in abstract |
| 11853089 | Ciombor 2002, J Orthop Res | Rat demineralised-bone-matrix endochondral model | Fracture / cartilage | not reported (abstract) | not reported | not reported | ELF pulsed EMF (waveform not in abstract) | not in abstract | Accelerated chondrogenesis: 35SO4, GAG, aggrecan and type II collagen mRNA up; NO change in DNA or thymidine (no proliferation) | In vivo ectopic model; same Brown group as PMID 11918302 |
| 11918302 | Aaron 2002, J Orthop Res | Same DBM model | Fracture | not reported | not reported | not reported | EMF | not reported | TGF-b1 mRNA +158%, protein +23%, TGF-b-positive cells +343% at peak; temporal pattern preserved | In vivo, rat |
| 32014064 | Parate 2020, Stem Cell Res Ther | MSC conditioned medium to chondrocytes | OA / cartilage | 2 mT (2D culture), 3 mT (3D) optimal | not reported | not reported | PEMF (single-pulse BICEPS system, not described in abstract) | 10 min sufficient | Platform-dependent optimum amplitude (2D 2 mT vs 3D 3 mT); 10 min enough to boost chondrogenic paracrine activity | In vitro; amplitude window depends on culture geometry |
| 30793837 | Kavand 2019, J Tissue Eng Regen Med | Rabbit MSC chondrogenesis | OA / cartilage | not reported | not reported | not reported | Pulsed EMF at "ubiquitous parameters" vs Ca2+ ion-cyclotron-resonance tuned AC+DC | 3 weeks | ONLY the Ca2+ ICR-tuned group increased GAG, collagen II, COL2A1, SOX9, ACAN. PEMF groups showed NO change (null for PEMF) | In vitro with positive and negative controls; single-lab |
| 36377077 / 36854553 | Xu 2022 (Cartilage) / Xu 2023 (Sheng Wu Yi Xue Gong Cheng Xue Za Zhi) | Rat AMSC-derived exosomes on chondrocytes; ACLT OA rat | OA | 1 mT | not reported | not reported | 15, 45, 75 Hz | not in abstract | At fixed 1 mT, 75 Hz > 45 Hz > 15 Hz for anti-inflammatory/matrix effect (COL2A1, ACAN up; MMP13 down); 75 Hz exosomes reduced OARSI score in vivo | In vitro + in vivo; direct frequency comparison; single-lab |
| 34612715 | Yang 2021, Cartilage | Mouse destabilisation-induced OA; WT vs IL-6-/- and TNF-a-/- | OA | 3.8 mT | not reported | not reported | 75 Hz | 1 h/day for 4 weeks | Pain, cartilage degeneration, synovitis improved in WT; protection reduced in knockouts | In vivo, sham-controlled; n = 10/group |
| 31985051 | Stefani 2020, Biotechnol Bioeng | Canine chondrocyte-agarose constructs; canine osteochondral defect | Cartilage repair | not reported (abstract) | not reported | not reported | IGEA device; coil orientation parallel vs perpendicular to the articular surface | not in abstract | Coil PARALLEL to surface gave higher repair stiffness than perpendicular (p = .026) and control; GAG up in both orientations | In vitro + preliminary in vivo; shows field-direction dependence |
| 17698373 / 23741498 | Varani 2007 (Osteoarthritis Cartilage) / Vincenzi 2013 (PLoS One) | Bovine chondrocytes and synoviocytes / human T/C-28a2 and hFOB 1.19 | OA | not reported in abstracts | not reported | not reported | "Low frequency low energy PEMF" (IGEA-type) | not in abstracts | A2A and A3 adenosine receptor density up; cAMP and agonist potency up; OPG up in hFOB | In vitro; same Ferrara/IGEA group |

### 1c. Animal bone models (osteoporosis, implant)

| PMID | First author, year, journal | System / model | B | dB/dt | Induced E | Frequency / waveform | Dose / schedule | Key result | Quality |
|---|---|---|---|---|---|---|---|---|---|
| 24244491 | Jing 2013, PLoS One | OVX rats, n=10/group | 2.4 mT peak | not reported | not reported | 15 Hz | 8 h/day, 10 weeks | BMD, Tb.N, BV/TV up; Wnt1, LRP5, b-catenin up; RANKL/RANK unchanged | In vivo, OVX control; single-lab |
| 28510268 | Zhou 2017, Bioelectromagnetics | OVX rats, early vs late start, n=10/group | 3.8 mT peak | not reported | not reported | 8 Hz pulse-burst repetition | 12 weeks, whole body | Early start prevented BMD loss in vertebra and femur; late start only vertebra; RANK protein down | In vivo; timing of initiation matters |
| 27711964 / 22948539 | Zhou 2016 / Zhou 2012 | OVX rats | not reported (abstracts) | not reported | not reported | PEMF | daily, 12 weeks | Lumbar BMD 119.5% of OVX model; with ibandronate 139.6%. 2012: RANKL down, OPG up, serum TRAP down | In vivo |
| 12669302 | Chang 2003, Bioelectromagnetics | OVX rats, n=35 | "extremely low intensity" (value not in abstract) | not reported | not reported | Single pulse, ELF | 30 days restored trabecular bone to intact level; serum PGE2 normalised | In vivo |
| 41152178 | An 2025, Sheng Wu Yi Xue Gong Cheng Xue Za Zhi | OVX rats, n=10/group | 0.6 mT | Computed by me if sinusoid: 0.19 T/s | not reported | 50 Hz | 90 min/day, 6 weeks | BMD, micro-CT, femur strength, bone-formation markers up | In vivo; same lab as Yan 2015 |
| 17634134 | Akca 2007, Head Face Med | OVX rat tibia Ti implants, n=5/group | 0.2 mT | not reported | not reported | not reported | 4 h/day, 2 weeks | Relative bone volume around implants up; low-magnitude vibration (50 Hz, 14 min/day) was MORE effective than PEMF | In vivo; n=5 |
| 25047554 | Jing 2014, PLoS One | Hindlimb-unloaded rats, n=10-12/group | Rotating magnetic field 0.60 to 0.38 T | Computed by me, crude assumption of sinusoidal variation at 7 Hz: dB/dt_pk about 17-26 T/s; E about 0.17-0.26 V/m at r = 2 cm. Geometry is a guess | not reported | 7 Hz rotating | 2 h/day, 4 weeks | NULL: no effect on bone microarchitecture, strength, formation or resorption despite very large B. Authors infer waveform dependence | In vivo; NULL |
| 27555216 | Jing 2016, Sci Rep | Porous Ti implant, osteoblasts + rabbit femoral defect | not reported (abstract) | not reported | not reported | PEMF | 6 and 12 weeks in vivo | Osseointegration, bone ingrowth up; Runx2, BMP2, Wnt/b-catenin up | In vitro + in vivo |
| 34657312 | Huegel 2021, J Orthop Res | Rat rotator cuff repair | not reported (abstract) | not reported | not reported | Orthofix signal | 3-28 days | BMP-2 pathway and pro-osteogenic genes up; fibrotic genes down; bone formation rate at enthesis up | In vivo; industry co-authors |

### 1d. Clinical evidence (parameters as far as abstracts give them)

| PMID | First author, year, journal | Population / design | Modality | B | dB/dt and E | Frequency / waveform | Dose | Key result | Quality |
|---|---|---|---|---|---|---|---|---|---|
| 21491410 | Griffin 2011, Cochrane Database Syst Rev (DOI 10.1002/14651858.CD008471.pub2) | 4 RCTs, 125 adults, delayed/non-union long bone (3 PEMF, 1 CCEF) | Non-union | not reported | not reported | mixed | mixed | Union RR 1.96 (95% CI 0.86-4.48), not significant, I2 58% | Systematic review; "inconclusive and insufficient" |
| 24895156 | Hannemann 2014, Arch Orthop Trauma Surg | 13 RCTs, 737 patients, acute fractures (PEMF or LIPUS) | Fracture | not reported | not reported | mixed | mixed | No effect on non-union proportion; faster radiological union only in non-operative or upper-limb fractures | Meta-analysis; heterogeneous |
| 21915570 | Adie 2011, J Bone Joint Surg Am | 259 acute tibial shaft fractures, double-blind RCT, 218 analysed | Fracture | not reported (abstract) | not reported | not reported | 10 h/day for 12 weeks; mean actual use 6.2 h/day | NULL: secondary surgery 16/106 vs 15/112, RR 1.02 (0.95-1.14) | Good design; moderate compliance |
| 39387850 | Picelli 2024, Eur J Phys Rehabil Med | 3 RCTs, 197 patients, acute fractures 2014-2022 | Fracture | not reported | not reported | mixed | mixed | NULL on acute bone healing; pain results contradictory | Systematic review update |
| 10758655 | Satter 1999, Bangladesh Med Res Counc Bull (DOI none) | 19 patients (13 completed), non-/delayed union long bones | Non-union | 0.01 to 0.1 mT peak ("100 to 1000 times smaller than Bassett") | Computed by me: 0.1 mT / 0.3 ms ~ 0.33 T/s and 0.01 mT / 0.3 ms ~ 0.03 T/s (assumes ramp over pulse width; rough) | Single 0.3 ms pulse every 12 ms (~80 Hz), Bassett-like shape | average 14 weeks | 11/13 healed; authors say result "negates Bassett's claim for a narrow window" | Uncontrolled case series; low quality; do not treat as evidence of efficacy |
| 1933587 | Bassett 1991, Calcif Tissue Int | 91 congenital pseudarthrosis of tibia, treated since 1973 | Non-union | not reported | not reported | PEMF | not reported | Type I/II healed 72% (43/60) | Uncontrolled long-term series |
| 2218718 | Mooney 1990, Spine | 195 patients, interbody lumbar fusion, double-blind sham | Spinal fusion | not reported | not reported | PEMF brace | not reported | Fusion 92% active vs 65% sham (p < 0.005); long-term follow-up PMID 10549700 (1999): fusion maintenance fell 25% overall, unrelated to treatment, related to smoking | Double-blind, sham; the foundation of FDA indication |
| 10941887 | Jenis 2000, J Spinal Disord | 61 patients, instrumented posterolateral lumbar fusion, 3 arms (PEMF n=22, DC n=17, control n=22) | Spinal fusion | not reported | not reported | Spinal-Stim 8212 | not reported | NULL: fusion and fusion-mass BMD not different at 1 year | Randomised; small; not blinded for DC |
| 17983841 | Foley 2007, Spine J | 323 patients, ACDF in smokers or multilevel, randomised, blinded radiology | Spinal fusion | not reported | not reported | PEMF | not reported | 6 months: 83.6% vs 68.6% (p=.0065); 12 months: 92.8% vs 86.7% (p=.1129, not significant); no difference in pain, NDI, SF-12 | Randomised but device/control not sham-matched |
| 32165697 / 39278993 / 25278882 | Akhter 2020 (Sci Rep) / Luo 2024 (Neurosurg Rev) / Park 2014 (Evid Based Spine Care J) | Meta-analyses of electrical stimulation in spinal fusion | Spinal fusion | not reported | not reported | PEMF, DC, CC pooled | pooled | OR 2.53 (1.86-3.43; 7 RCTs, n=941) and OR 2.66; PEMF subgroup OR 2.60 (1.29-5.27). Park 2014: six RCTs, inconsistent, "unable to conclude", low strength | Moderate quality; no subgroup interaction by stimulation type |
| 9355215 | Glazer 1997, Spine | Rabbit posterolateral fusion, n=10/group | Spinal fusion | not reported | not reported | PEMF | 4 h/day, 6 weeks | Pseudarthrosis 40% to 20% (NS); stiffness +35%, load to failure +42% | Animal; small |
| 2195843 | Tabrah 1990, J Bone Miner Res | 20 osteoporosis-prone women | Osteoporosis | not reported | not reported | 72 Hz | 10 h/day for 12 weeks | Radial BMD increased then fell over following 36 weeks | Small, uncontrolled / opposite-arm comparison; low quality |
| 35586276 / 32508140 / 32251502 / 31583420 / 30552258 / 23973142 / 22870682 | Tong 2022 / Vigano 2020 / Yang 2020 / Chen 2019 / Wu 2018 / Negm 2013 / Cao 2012 | OA meta-analyses (most knee) | OA | not reported | not reported | mixed | mixed | Pain SMD 0.71 (11 RCTs, n=614); Vigano 2020: pain SMD -0.41, activity NS, not superior to other conservative therapy; Yang 2020: pain SMD 1.06, "PEMF parameters did not influence symptoms"; Chen 2019: function better but NO pain/stiffness benefit; Wu 2018: knee and hand benefit, not cervical; sessions <=30 min better than >30 min; Negm 2013 (<=100 Hz): function SMD 0.22, pain NS; Cao 2012 (5 RCTs): no benefit | Mixed; high heterogeneity; low-to-moderate evidence |
| 28624853 / 26756278 | Collarile 2017 (Knee Surg Sports Traumatol Arthrosc) / Servodio Iammarrone 2016 (Bioelectromagnetics) | MACI n=30 / patellofemoral pain n=31 | Cartilage repair / PFPS | not reported | not reported | PEMF | MACI: 4 h/day for 60 days | Improved IKDC at 60 months (p=0.001); VISA/VAS better at 6-12 months | Small randomised, not sham-controlled |

### 1e. Tendon / fibroblast

| PMID | First author, year, journal | System | B | Frequency | Dose | Key result | Quality |
|---|---|---|---|---|---|---|---|
| 33261301 | Marmotti 2020, J Biol Regul Homeost Agents (DOI none) | Human hamstring tendon-derived cells, 13 donors | 1.5 mT | 75 Hz (IGEA) | 8 h/day, up to 21 days | Collagen I, collagen VI and scleraxis up (p<0.05) while proliferation markers (PCNA, b-catenin) were LOWER than control | In vitro; primary human cells |
| 42738823 | Taiana 2026, Cells | Human tenocytes, IL-1b acute/prolonged models | not reported (abstract) | not reported | not reported | Proliferation up in acute models; benefit mainly in acute or mild inflammation; no effect on wound closure in high-dose/prolonged inflammation; MMP activity unchanged | In vitro |
| 39534390 | Ko 2024, Orthop J Sports Med | 65 Achilles tendinopathy patients, sham-controlled RCT | not reported (abstract) | not reported | 10 min twice weekly for 8 weeks | NULL: VISA-A and NPRS improved in both arms, no difference (p=.527); neovascularity unchanged | Level 1, small |
| 39172175 | Wilms 2024, Orthopade | 34 tendinopathy patients, single 10 min bout, sham | 0.78 T (high-energy) | not reported | single 10 min | Pressure-pain threshold +83 to +139% vs +10 to +36% sham (p=0.045); HSP70 unchanged | Small RCT; regime unrelated to the mT-range mechanisms above |

### 1f. Reviews and other

| PMID | Reference | Relevance |
|---|---|---|
| 32159242 | Zhang 2020, Bioelectromagnetics (DOI 10.1002/bem.22258) | 32 papers: pulsed EMF promotes osteoblast proliferation at 7.5-15 Hz or 50-75 Hz with 0.40-1.55 mT or 3.8-4 mT; sinusoidal EMF 0.9-4.8 mT at 45-60 Hz and static 0.1-0.4 mT or 400 mT promote differentiation/maturation (authors' narrative summary, not a pooled estimate) |
| 30908726 | Galli 2019, Bioelectromagnetics | In vitro osteoblast PEMF review; highlights primary cilia and inconsistent parameters across literature |
| 33970582 | Cadossi 2020, JAAOS Glob Res Rev | Mechanism review: A2A/A3 adenosine receptors as site of action and "dose-response" for matrix |
| 16831948 | Aaron 2006, Ann N Y Acad Sci | DBM endochondral model, "signal dosimetry", TGF-b via AP-1/JNK |
| 8496242 | Bassett 1993, J Cell Biochem | PEMF parameters "designed to induce voltages similar to those produced during dynamic mechanical deformation" (design principle, not a threshold measurement) |
| 18427315 / 28337895 | Denaro 2008 (Spine) / Bambini 2017 (J Biol Regul Homeost Agents) | Static fields: corrosion-current SMF lowered ALP, Runx2, collagen I (inhibitory); implant-cover-screw magnet SMF slightly lowered proliferation but raised differentiation genes (opposite directions; B not reported in abstracts) |
| 22940137 | Pilla 2012, Biochem Biophys Res Commun | PRF signal modulating Ca/calmodulin-dependent NO signalling in neuronal and fibroblast cultures within seconds; not bone, but same Ca/CaM target as Brighton |

## 2. Synthesis per target

General rule: the in vitro literature in this cluster almost always changes B (mT) at a fixed waveform and frequency, so B and dB/dt (and induced E) rise together. Studies that can separate them are few (Section 3).

### 2.1 Osteoblast proliferation and differentiation (ALP, collagen I, osteocalcin, Runx2)

- Typical effective window (in vitro): 0.13-3 mT peak, 7.5-75 Hz, 0.5-8 h/day, days of repetition. Retrieved lowest effective B: 0.13 mT (Tsai 2007, 7.5 Hz, 300 us pulses). Highest reported positive B in cells: 7 mT peak (Diniz 2002, 15 Hz burst). Rat OVX in vivo: 2.4-3.8 mT peak (Jing 2013, Zhou 2017), also 0.2 mT with a positive result (Akca 2007, n=5) and 0.6 mT at 50 Hz (An 2025).
- Amplitude windows (from the few multi-intensity studies): Yan 2015 (0.6-3.6 mT, 50 Hz): optimum is the LOWEST tested, 0.6 mT, all higher doses less effective but still positive for proliferation. Zhai 2016 (0.5-2 mT, 15.38 Hz): optimum at the highest tested, 2 mT, with 2 h/day better than 0.5, 1 or 6 h. Tsai 2007: 0.13 mT increases proliferation, 0.32 mT inhibits proliferation but increases ALP. So the optimum is not at a common B across labs and waveforms; the dose-response curve is non-monotonic and depends on the endpoint (proliferation vs differentiation).
- Minimum effective duration: Zhai: 2 h/day was better than 6 h; Chang 2006 (osteoclast apoptosis): 8 h and 16 h effective, 1 h not. Pilla and Aaron suggest that effects need chronic repetition; no sharp duration threshold was measured in any osteoblast study here.
- Null and contradictory findings: Yang 2007 (1.55 mT, 48 Hz): MC3T3-E1 unaffected; primary cells' ALP down at 24 h but up at 48 h. Wang 2016: PEMF alone no effect on hPDLSC proliferation. Diniz 2002: inhibition when applied at the mineralisation stage. Lohmann 2000: proliferation DOWN while differentiation UP. Pezzetti 1999 and De Mattei 2001: response requires serum growth factors. Schwartz 2009: effect depends on substrate (CaP but not plastic). Tong 2017: effect requires Ca transients. Kar 2021: requires A3 adenosine receptor.
- What drives it: Not established. Evidence for each candidate:
  - B amplitude: supported only as an empirical dose variable within one waveform; no study varies B at fixed dB/dt.
  - dB/dt / induced E: the only direct data (Chang, 3-12 uV/cm rms) are far below mV/cm values quoted for Bassett-type signals; Fitzsimmons reports 1e-5 V/m and a frequency dependence. These argue against a simple "E above X mV/cm" threshold in cell culture. My computed E for Tsai (1.5-7.6 uV/cm rms, assumptions in table) falls in Chang's range, so within that lab's system, the active induced-E level is a few uV/cm.
  - Frequency/timing/waveform: Pilla 1999 (burst-duration tuning gave equal effect at 10x lower peak amplitude), Zhu 2017 (0.6 mT pulsed beats 1.8 mT sinusoid at the same 50 Hz), Jing 2014 (0.4-0.6 T rotating field at 7 Hz has no effect), Kavand 2019 (only ICR-tuned AC+DC works), Xu 2022 (75 Hz > 15 Hz at 1 mT). Taken together these favour waveform/frequency structure plus cell state as the controlling variables, with B amplitude as a secondary dose scaler.
- Confidence: amplitude/frequency windows for osteoblast proliferation/differentiation: MODERATE for existence of an effect and non-monotonic dose dependence in vitro (replicated across labs for 15 Hz/mT range and 50 Hz/0.6 mT but with differing optima); LOW for any specific numeric threshold; SPECULATIVE for B vs dB/dt attribution.

### 2.2 Ca2+, calmodulin, PGE2, adenosine receptors, cAMP (upstream transduction)

- Brighton 2001 (MC3T3-E1): inductive coupling and combined fields act by release of Ca2+ from intracellular stores (TMB-8 sensitive), unlike capacitive coupling, which acts through voltage-gated channels (verapamil). Field magnitudes not in abstract. Convergence on cytosolic Ca2+/calmodulin.
- Tong 2017: PEMF effect on osteoblasts exists only when intracellular Ca transients are present - a timing/cell-state condition rather than an amplitude threshold.
- Adenosine A2A/A3 (Varani 2007, Vincenzi 2013, Kar 2021): receptor density rises after IGEA-type PEMF (75 Hz, ~1.5-2.3 mT in related papers); A3 is necessary for part of the osteoblast differentiation response (Kar 2021, CRISPR knockout with rescue). No threshold amplitude is reported in the abstracts.
- Confidence: pathway identity MODERATE-HIGH (inhibitor and knockout evidence); amplitude threshold LOW (not measured).

### 2.3 TGF-b, BMP-2, Wnt/b-catenin, IGF-II, cilia (growth-factor signalling)

- TGF-b1: Lohmann 2000 (up on days 1-2 then back to control at 4 days), Lohmann 2003 (osteocyte-like cells via Cox-1), Aaron 2002 (rat DBM: +158% mRNA), Zhuang 1997 (CCEF, Ca/CaM-dependent). These show transient induction; parameters of the inductive signal beyond 15 Hz burst structure are not in the abstracts.
- BMP-2: upregulated in Yan 2015 (0.6 mT, 50 Hz), Zhu 2017, Wang 2014 (implant surfaces), Huegel 2021 (in vivo rotator cuff); BMPRII at the cilium base is required (Xie 2016, 0.6 mT, 50 Hz).
- Wnt/b-catenin: Zhai 2016 (2 mT, 15.38 Hz), Jing 2013 (2.4 mT, 15 Hz, in vivo OVX), Jing 2016 (porous Ti, in vitro and rabbit). Same Fourth Military Medical University group; not independently replicated in the retrieved set.
- IGF-II: Fitzsimmons 1995, IGF-II receptor number up after 30 min at 15.3 Hz combined AC/DC field with E_max of 1e-5 V/m and frequency dependence. Lowest E-field in this cluster, argues against Faraday-induced E being the driver for this effect.
- Primary cilium: Yan 2015, Xie 2016, Ren 2019, He 2022, Wang 2019 (osteocytes) all show loss of effect after IFT88/polaris knockdown, using 0.6 mT/50 Hz or 15 Hz/0.5-3 mT. Cilia are the best-supported transducer, but most data come from two labs.
- Confidence: HIGH that these pathways are engaged downstream; MODERATE for cilia requirement (consistent but concentrated in two labs); LOW for numeric thresholds.

### 2.4 Osteocyte, osteoclast and OPG/RANKL (osteoporosis)

- Osteocytes (Wang 2019): 0.5 mT (5 G) at 15 Hz for 2 h reduced apoptosis genes and RANKL/OPG; 3 mT (30 G) did not (reported as intensity-dependent). Osteoclast precursors (Wang 2017): 0.5 mT inhibits osteoclastogenesis; 3 mT promotes osteoclast apoptosis and resorption. This is the clearest published amplitude window (0.5 mT beneficial for bone mass; 3 mT opposite in the osteoclast arm).
- Induced E dose-response (Chang 2003): 4.8, 8.7, 12.2 uV/cm rms gave bidirectional effects (enhancement ~50% vs suppression ~27%) - the only cluster-wide demonstration that induced E level, not a fixed B, can flip the sign of an effect. Chang 2006: 3 uV/cm at 7.5 Hz induced osteoclast apoptosis after 8-16 h but not 1 h.
- OPG/RANKL: Schwartz 2009 (OPG up, RANKL unchanged on CaP), Zhou 2012 (OVX rats: RANKL down, OPG up), Zhou 2016/2017 (RANK protein down), Vincenzi 2013 (OPG up in hFOB), He 2017 (human cells: osteoclast formation inhibited via osteoblasts). Jing 2013 reported NO change in RANKL/RANK gene expression, so findings conflict.
- In vivo OVX: 2.4-3.8 mT peak with 8-15 Hz bursts improved BMD and microarchitecture (n = 10/group); timing of start matters (Zhou 2017). Clinical: only Tabrah 1990 (72 Hz, n=20, uncontrolled) was retrieved; no RCT of osteoporosis was retrieved in this session.
- Rotating field null (Jing 2014): 0.38-0.6 T at 7 Hz did not protect hindlimb-suspended rat bone.
- Confidence: animal efficacy MODERATE (consistent, mostly one or two labs); amplitude window for osteoclast arm LOW-MODERATE (single study at 15 Hz); human osteoporosis efficacy LOW (no controlled data retrieved).

### 2.5 Chondrocyte matrix synthesis and OA

- In vitro windows: 1.5 mT/75 Hz (Ongaro 2011: sulfate incorporation +49% in OA explants after 7 days), 2.3 mT/75 Hz (Pezzetti, De Mattei; proliferation needs serum), 2-3 mT MSC paracrine effect depending on 2D/3D culture (Parate 2020, 10 min exposure). At fixed 1 mT, 75 Hz outperformed 45 and 15 Hz for chondroprotection (Xu 2022/2023). In mice, 3.8 mT/75 Hz for 1 h/day for 4 weeks reduced OA progression via TNF-a/IL-6 (Yang 2021).
- Nulls: Kavand 2019 - generic PEMF failed while Ca2+ ICR-tuned fields worked; Ciombor 2002 - no proliferation change in the DBM model (matrix effect without cell-number effect).
- Direction dependence: Stefani 2020 - coil parallel to joint surface outperformed perpendicular, which implicates the induced-E direction/orientation relative to tissue and cell polarity, not only B magnitude.
- Clinical OA: meta-analyses disagree (Section 1d). Yang 2020 reports no influence of PEMF parameters on symptoms; Wu 2018 found sessions <=30 min superior to >30 min (a non-monotonic dose-duration finding). Treatment effect SMDs range from 0.2 to 1.5 and several analyses are null (Chen 2019 pain, Negm 2013 pain, Cao 2012).
- Confidence: chondrocyte anabolic effect at 1.5-3.8 mT, 75 Hz: MODERATE in vitro; frequency preference (75 Hz > 15 Hz): LOW (one lab, one cell-derived intermediate); clinical OA benefit: LOW-MODERATE with high heterogeneity and no consensus on optimal parameters.

### 2.6 Tendon and fibroblast

- 1.5 mT/75 Hz for 8 h/day raised collagen I/VI and scleraxis in human tendon cells with lower proliferation (Marmotti 2020). Context-dependent effects of PEMF on inflamed tenocytes (Taiana 2026). Rat rotator-cuff: BMP-2 pathway up, fibrosis genes down (Huegel 2021). Clinical: Achilles tendinopathy RCT (Ko 2024) NULL; single 0.78 T bout gives short-term pain-threshold increase (Wilms 2024), which is unrelated to bone/cartilage mechanisms.
- No tendon study retrieved reports induced E, dB/dt or an amplitude series, so no tendon threshold can be given.
- Confidence: LOW.

### 2.7 Fracture healing and non-union

- Strongest dataset (negative): Cochrane 2011 (4 RCTs, n=125): union RR 1.96 (0.86-4.48); Hannemann 2014 (13 RCTs): no effect on non-union rate; Adie 2011 (n=259, double blind): RR 1.02; Picelli 2024: null for acute fractures.
- Positive: Bassett 1991 congenital pseudarthrosis series (72% for types I/II), uncontrolled.
- Parameter evidence: Satter 1999 (0.01-0.1 mT peak, 0.3 ms pulse ~80 Hz, uncontrolled n=19) raises the possibility of effects at 100-1000x lower B than Bassett signals; this conflicts with a narrow amplitude window but is weak evidence.
- Confidence: efficacy for delayed/non-union: LOW-MODERATE; efficacy for acute fracture: LOW (net null); numeric thresholds: SPECULATIVE.

### 2.8 Spinal fusion

- Double-blind sham RCT (Mooney 1990: 92% vs 65%), later subgroup meta-analyses OR ~2.5-2.7 across modalities (Akhter 2020; Luo 2024), but Jenis 2000 (null, n=61) and Park 2014 (inconsistent) temper this. Foley 2007: significant difference at 6 months, not at 12 months.
- Parameters are not given in the retrieved abstracts.
- Confidence: MODERATE for benefit as adjunct in high-risk fusions; LOW for any parameter threshold.

## 3. What drives activation? (B vs dB/dt vs E vs frequency/timing)

Direct evidence is thin. The findings that bear on it:

| Question | Evidence | Reading |
|---|---|---|
| Does B amplitude alone control response? | Yan 2015: optimum at the lowest B (0.6 mT) of a 0.6-3.6 mT series. Zhai 2016: optimum at the highest B (2 mT) of 0.5-2 mT. Tsai 2007: sign of proliferative effect flips between 0.13 and 0.32 mT. Wang 2017: 0.5 mT and 3 mT have opposite osteoclast effects. Jing 2014: 0.4-0.6 T rotating field: null. | B is not a monotonic driver; optimum differs with waveform, frequency and endpoint. A 1000-fold larger B (rotating tesla range) does nothing. |
| Does induced E (dB/dt) set the response? | Chang 2003/2006: 3-12 uV/cm rms is active and non-monotonic; Fitzsimmons 1995: E_max 1e-5 V/m with frequency dependence; Pilla 1999: 10x lower peak B and ~800x lower average amplitude gave the same bioeffect with a re-tuned burst. | Active levels in culture are uV/cm, far below the mV/cm often quoted for Bassett/Brighton signals; E magnitude alone does not predict outcome. Whether dB/dt (E) is the actual variable cannot be separated from B in the retrieved studies, since none held one fixed. |
| Does frequency/timing matter? | Xu 2022: 75 > 45 > 15 Hz at 1 mT in chondroprotection. Zhai/Wang (15 Hz) and Yan (50 Hz) work at overlapping mT but different optima. Fitzsimmons: frequency-dependent IGF-II receptor change. Kavand: Ca-ICR frequency/B_DC relationship worked, generic PEMF did not. Zhu: same 50 Hz, pulse beats sinusoid despite 3x lower B. | Frequency and waveform structure are at least as important as amplitude. |
| Does exposure duration/timing matter? | Chang 2006: 8-16 h but not 1 h; Zhai: 2 h/day better than 6 h; Wu 2018: <=30 min clinical sessions better; Diniz: stage-dependent sign; Tong: needs Ca transients; Lohmann: TGF-b1 and PGE2 changes vanish by day 4. | Exposure duration and cell state/timing are strong effect modifiers. |

Bottom line: in this cluster the field-parameter that "drives" activation is best described as a combination - a waveform/frequency window that sets the pulse shape, a modest amplitude window (roughly 0.1-3 mT peak in vitro; roughly 2-4 mT peak for rodent whole-body osteoporosis protocols), and a cell-state/timing window. No study here isolates dB/dt from B, and no study measures a threshold below which nothing happens: lowest studied values still produced effects (0.13 mT; 3 uV/cm; 10 uV/m in a combined AC/DC system).

Amplitude summary of retrieved data (peak B, in vitro unless stated):
- Lowest effective: 0.13 mT (Tsai); 0.5 mT (Wang osteocyte/osteoclast); 0.2 mT in vivo (Akca, n=5); 0.01-0.1 mT clinical (Satter, uncontrolled).
- Typical optimum: 0.6 mT at 50 Hz (Yan); 1.5-2.3 mT at 75 Hz (IGEA-type); 2 mT at 15 Hz (Zhai); 2.4-3.8 mT in vivo rats.
- Saturating/inhibitory: Yan: monotonic decline above 0.6 mT; Tsai: 0.32 mT inhibits proliferation; Wang 2017: 3 mT reverses osteoclast effect; Diniz: 7 mT beneficial early, harmful in mineralisation stage.
- Ineffective: 1.55 mT/48 Hz in MC3T3-E1 (Yang 2007); 0.4-0.6 T rotating at 7 Hz (Jing 2014); generic PEMF for chondrogenesis (Kavand 2019); Achilles tendinopathy RCT (Ko 2024); acute tibial fracture RCT (Adie 2011).

## 4. Evidence-strength overview

| Target | Threshold evidence | Overall confidence |
|---|---|---|
| Osteoblast proliferation/differentiation | Multi-intensity series at 15 Hz and 50 Hz; non-monotonic; cell-state dependent | Moderate (effect), Low (numbers) |
| Ca2+/CaM, adenosine A2A/A3 | Pathway evidence only, no amplitude series | Moderate-High (mechanism), Low (thresholds) |
| TGF-b, BMP-2, Wnt, IGF-II, cilia | Strong mechanistic knockouts; two labs; Fitzsimmons E_max 10 uV/m | Moderate (mechanism), Low (thresholds) |
| Osteocyte/osteoclast/OPG-RANKL | Intensity window 0.5 vs 3 mT at 15 Hz; induced-E series (Chang) | Low-Moderate |
| Chondrocyte matrix | 75 Hz and 1.5-3.8 mT effective; frequency preference one lab | Moderate (effect), Low (windows) |
| Tendon/fibroblast | Single-amplitude (1.5 mT, 75 Hz) in vitro; clinical null | Low |
| Fracture/non-union | Mostly null or inconclusive RCTs | Low-Moderate |
| Spinal fusion | One sham RCT strongly positive, one null; meta-analyses positive | Moderate |
| Osteoporosis (animal) | Positive in OVX rats at 2.4-3.8 mT; rotating-field null | Moderate (animal), Low (human) |
| Osteoarthritis (clinical) | Meta-analyses discordant; parameters not predictive | Low-Moderate |

## 5. Most important references (PMID, DOI)

1. 12929162 - Chang K, 2003, Bioelectromagnetics. Induced E 4.8/8.7/12.2 uV/cm rms in osteoclast-like cell formation. DOI 10.1002/bem.10118
2. 7639117 - Fitzsimmons RJ, 1995, J Bone Miner Res. IGF-II receptors, E_max 1e-5 V/m at 15.3 Hz. DOI 10.1002/jbmr.5650100519
3. 10228567 - Pilla AA, 1999, Bioelectrochem Bioenerg. Kinetics-based waveform tuning, 10x lower peak amplitude. DOI 10.1016/s0302-4598(98)00148-2
4. 25661534 - Yan, 2015, Mol Cell Endocrinol. 0.6-3.6 mT, 50 Hz intensity series, cilia dependence. DOI 10.1016/j.mce.2015.01.031
5. 26891468 - Zhai M, 2016, Bioelectromagnetics. 0.5/1/2 mT x 0.5-6 h/day at 15.38 Hz, Wnt/b-catenin. DOI 10.1002/bem.21961
6. 28741320 - Wang P, 2017, Bioelectromagnetics. 0.5-3 mT intensity window on osteoclastogenesis. DOI 10.1002/bem.22070
7. 17516509 - Tsai, 2007, Bioelectromagnetics. 0.13/0.24/0.32 mT, 300 us pulses, 7.5 Hz. DOI 10.1002/bem.20336
8. 11679602 - Brighton CT, 2001, J Bone Joint Surg Am. Capacitive vs inductive vs combined transduction pathways. DOI 10.2106/00004623-200110000-00009
9. 12111759 - Diniz P, 2002, Bioelectromagnetics. 7 mT, 15 Hz, stage-dependent sign. DOI 10.1002/bem.10032
10. 36377077 - Xu Y, 2022, Cartilage. 15/45/75 Hz at 1 mT, chondroprotection. DOI 10.1177/19476035221137726
11. 30793837 - Kavand H, 2019, J Tissue Eng Regen Med. PEMF null vs Ca2+ ICR positive for chondrogenesis. DOI 10.1002/term.2829
12. 25047554 - Jing D, 2014, PLoS One. 0.38-0.6 T rotating field null in rat bone. DOI 10.1371/journal.pone.0102956
13. 21491410 - Griffin, 2011, Cochrane Database Syst Rev. Non-union meta-analysis. DOI 10.1002/14651858.CD008471.pub2
14. 21915570 - Adie S, 2011, J Bone Joint Surg Am. Null double-blind RCT, acute tibial fracture. DOI 10.2106/JBJS.J.00869
15. 2218718 - Mooney, 1990, Spine. Double-blind spinal fusion trial 92% vs 65%. DOI 10.1097/00007632-199007000-00016
