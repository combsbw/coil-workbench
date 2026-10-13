# Cluster 1: Ca2+ signalling, calmodulin, eNOS/NO/cGMP, VGCC, Ca2+ efflux / ion cyclotron-parametric resonance, cAMP

Source: PubMed records retrieved in this session via the PubMed MCP tools (search_articles, get_article_metadata, get_full_text_article). Every PMID/DOI below comes from tool output. Numbers come from abstracts unless stated; full text was read only for PMC4568470 (Petecchia 2015) and PMC3780531 (Pall 2013 review). The Yap 2019 full text returned empty.

Conventions:
- "NR" = not reported in the record I could read (usually the abstract). Absence of a value in this file means I did not see it, not that the paper omits it.
- "(computed by me)" marks values I derived. Formulas: sinusoid dB/dt_peak = 2*pi*f*B_peak; uniform B over a circular loop of radius r, E = (r/2)*dB/dt; ICR frequency f_c = qB/(2*pi*m), which for Ca2+ (m = 40.08 u) is 0.766 Hz per microtesla; crude pulse dB/dt ~ B_pk / pulse width, which assumes a linear ramp across the whole pulse and is only an order-of-magnitude figure.
- Whether a sinusoidal B is quoted as peak or rms is often not stated in abstracts. I flag this where it matters.

---------------------------------------------------------------------

## 1. Table of studies

### 1A. Direct tests of "what drives" Ca2+ signalling (B vs induced E vs frequency)

| PMID | First author, year, journal | System | Modality relevance | B | dB/dt | Induced E / J | Freq / waveform / pulse width | Dose / schedule | Key result and direction | Quality |
|---|---|---|---|---|---|---|---|---|---|---|
| 1333413 | Liburdy 1992, FEBS Lett | Rat thymic lymphocytes, ConA-activated; 45Ca influx; fura-2 [Ca]i | Immune/inflammation; Ca channel site | 22 mT (60 Hz) | 8.29 T/s peak (computed by me, assuming 22 mT is peak) | Einduced 1.7 mV/cm max (reported). A multi-ring annular plate gave different E at constant B | 60 Hz sine; also a pure 60 Hz E-field exposure | 60 min, 37 C | Ca influx rose, and the response tracked induced E at constant B. A pure E field and a magnetically induced E of equal strength gave similar changes. The plateau phase, not store release, was affected. No effect in Ca-free buffer on early release | In vitro; one lab; sham NR in abstract; replicated only by the same lab (1993) |
| 8243637 | Liburdy 1993, FEBS Lett | Same, with c-MYC mRNA | Immune/inflammation | 22 mT | 8.29 T/s (computed) | 1.7 mV/cm max | 60 Hz | 60 min | 1.5-fold higher Ca influx with sub-optimal ConA plus field. About 3-fold higher c-MYC mRNA. The field was a co-stimulus only | In vitro; n = 3 experiments for Ca; same lab |
| 1468568 | Walleczek, 1992, FEBS Lett | Rat thymic lymphocytes, 45Ca uptake | Immune; Ca signalling | Bpeak 0, 1.6, 6.5, 28 mT | NR (rise time NR) | At 6.5 mT: Emax 0.69 mV/cm, Jmax 2.6 uA/cm2 (reported). E scaled to about 0.17 and 3.0 mV/cm at 1.6 and 28 mT (computed by me, proportional scaling assumed) | 3 Hz, monopolar quasi-rectangular pulses | 30 min | At 6.5 mT, ConA-induced 45Ca uptake fell 45%. Effect size rose with B (1.6 to 28 mT). Sign depended on cell activation state (inhibit or stimulate). Resting cells did not respond | In vitro; B and E co-varied, so they cannot be separated; consistent with an earlier 3 Hz lab result (reported in abstract) |
| 7748202 | Lindstrom 1995, Bioelectromagnetics | Jurkat T cells; fura-2 microfluorometry, single cells | Immune; Ca oscillation | Threshold below 0.04 mT; plateau at 0.15 mT (50 Hz; peak vs rms NR) | 0.013 T/s at 0.04 mT and 0.047 T/s at 0.15 mT (computed by me, if peak sine) | NR. Computed by me: about 0.24 mV/m per centimetre of radius at 0.15 mT, if uniform B over a 1 cm loop; cell geometry unknown | Sine, 5 to 100 Hz tested at 0.15 mT; broad peak at 50 Hz | Acute exposure | [Ca]i oscillations resembling anti-CD3. No effect below 0.04 mT, plateau at 0.15 mT. Broad frequency tuning with optimum near 50 Hz | In vitro; cells preselected by the authors (92% response); not replicated, see next two rows |
| 10656853 | Wey 2000, Environ Health Perspect | Jurkat; fura-2 imaging; blinded and randomized | Null / replication failure | 0.15 mT (1.5 G), 50 Hz | 0.047 T/s (computed, if peak) | NR | 50 Hz | 8 min MF vs sham vs none | Transient incidence 16.5% (MF), 14.6% (sham), 14.2% (none), not different. No effect when many cells were scored blind | In vitro; sham and no-field controls; coded analysis. A genuine replication attempt that failed |
| 9261541 | Lyle 1997, Bioelectromagnetics | Jurkat E6-1; Fluo-3 flow cytometry; anti-CD3 | Null | 0.15 mT rms 60 Hz on a 78.2 uT DC background | about 0.08 T/s peak (computed by me: 0.15 mT rms = 0.212 mT peak; 2*pi*60*0.212e-3) | NR | 60 Hz | During or before stimulation; optimal and sub-optimal (24 C, low Ca, low anti-CD3) | No change in Ca signalling under any condition. The authors note effects further downstream (calmodulin etc.) are not excluded | In vitro; flow cytometry; null |
| 1733766 | Yost & Liburdy 1992, FEBS Lett | Rat thymocytes, ConA, 45Ca influx | ICR/parametric resonance | AC 42.1 uT at 16 Hz plus colinear DC 23.4 uT (AC/DC 1.8) | NR | NR | 16 Hz sine | 60 min, 37 C | Ca influx inhibited only with AC and DC together; neither alone worked. Resting cells did not respond. Authors say this is consistent with Lednev's parametric resonance. (For orientation, f_c(Ca2+) at 23.4 uT = 17.9 Hz, computed by me.) | In vitro; split-field controls; same lab |
| 8451278 | Coulton & Barker 1993, Phys Med Biol | Mouse lymphocytes; fluorescent [Ca]i probe | ICR; null | Range of DC amplitudes (values NR in abstract) | NR | NR | Resonance conditions at 16 Hz and 50 Hz; DC varied up to 25% either side of the calculated optimum | 60 min | No change in [Ca]i under any ICR combination. ConA positive control worked | In vitro; positive control; null; explicit test of the 1985 ICR claim |
| 10723019 | Coulton 2000, Bioelectromagnetics | Cell-free Ca/CaM-dependent myosin light chain phosphorylation | CaM; null | Static 0 to 200 uT | 0 (static) | none | static | cell-free assays; included a direct replication | No effect of static field strength on phosphorylation rate. Authors could not confirm the published Ca-CaM binding sensitivity | Biochemical; three series including direct replication; null |
| 12483663 | Liboff 2003, Bioelectromagnetics | Cell-free CaM-dependent cyclic nucleotide phosphodiesterase | CaM / cAMP-cGMP | About 20 uT static | 0 (static) | none | static | 30 min | Activity altered. Effect is nonlinear in free Ca2+ with a maximum near EC50 of Ca2+. Interpreted as sensitivity of Ca2+/CaM binding to the geomagnetic-scale field | Biochemical; single lab; conflicts with the null in 10723019 |

### 1B. ICR / parametric resonance, Ca2+ efflux windows

| PMID | First author, year, journal | System | Modality | B | dB/dt | E / J | Freq / waveform | Dose / schedule | Key result | Quality |
|---|---|---|---|---|---|---|---|---|---|---|
| 1064869 | Bawin & Adey 1976, PNAS | Chick and cat cerebral tissue, 45Ca efflux | Neural | none (electric field) | NA | 5, 10, 56, 100 V/m in air; tissue gradient estimated at 0.1 uV/cm (authors' estimate) | 1, 6, 16, 32, 75 Hz sine | 20 min | Efflux decreased 12 to 15%, maximum at 6 and 16 Hz. Thresholds about 10 V/m (chick) and 56 V/m (cat) in air. Frequency window and amplitude threshold both present | In vitro; matched controls; the original "window" paper; no replication in this set |
| 282648 | Bawin 1978, PNAS | Chick cerebral tissue | Neural | NA | NA | NR | RF amplitude-modulated at brain-wave frequencies | NR | Efflux increased; insensitive to bath Ca (0 to 4.16 mM); enhanced by H+; La3+ reversed the sign. Interpreted as a surface binding-site effect | In vitro |
| 6812594 | Adey 1982, Bioelectromagnetics | Awake cat cortex, 45Ca efflux | Neural | NA | NA | 33 V/m in tissue; 0.29 W/kg | 450 MHz, 16 Hz AM, 85% depth, 3.0 mW/cm2 | 60 min | Waves of increased efflux. Population difference from controls only at confidence 0.96 | Animal; weak statistics |
| 2540755 | Blackman 1989, Bioelectromagnetics | Chick forebrain, 45Ca efflux | Neural; amplitude windows | NA | NA | SAR up to 0.005 W/kg (too low for heating) | 50 MHz RF, AM 16 Hz | 20 min | Multiple power-density windows. Enhanced efflux at 1.75, 3.85, 5.57, 6.82, 7.65, 7.77, 8.82 mW/cm2; no change at 0.75, 2.30, 4.50, 5.85, 7.08, 8.19, 8.66, 10.6, 14.7 mW/cm2. Not monotone | In vitro; modulated RF, not ELF; an interleaved window pattern that is hard to use clinically |
| 9915588 | Blackman 1999, Bioelectromagnetics | PC-12 neurite outgrowth (not Ca read-out) | Neural; IPR | DC 2.97 uT; AC varied | NR | NR | 45 Hz = H+ resonance. 42.5, 47.5 Hz near resonance; 40, 50 Hz off | Repeated three times | Replicated Trillo's result. Response bandwidth no wider than +/-10% of resonance frequency. Narrow frequency window at fixed DC | In vitro; internal triple repeat; the result is on H+ not Ca2+ |
| 10453066 | Zhadin 1999, Bioelectromagnetics | Rat behaviour (open field) | Neural | DC 50 uT and 500 uT with proportional AC | If AC amplitude and frequency both scale with DC (as the abstract says), dB_ac/dt scales about 100x between the two DC settings (computed by me); the effect was qualitatively the same | NR | Cyclotron frequencies for Ca, Na, K, Cl, Mg, Li | NR | Ca-frequency fields lowered locomotor and exploratory activity; Mg-frequency fields raised it; other ions had no significant effect. Same effect at both DC levels | Animal; behavioural; no independent replication in this set |
| 10797457 | Prato 2000, Bioelectromagnetics | Land snail Cepaea, opioid analgesia | Pain / neural | 141 to 414 uT peak | NR | NR | ELF set to Lednev PRM predictions for Ca2+ or K+ | NR | Analgesia reduced, unchanged or increased depending on parameters, as the PRM predicts. Effects absent without light | Animal; single-blind; same group as 9795129 |
| 9795129 | Kavaliers 1998, Brain Res | Land snail, enkephalinase-induced analgesia | Pain; NO | 141 uT peak | NR | NR | 60 Hz | 15 min | Field reduced analgesia. Effect reduced by L-NAME and enhanced by an NO donor. Links ELF effect to NOS | Animal; pharmacological controls |
| 30793837 | Kavand 2019, J Tissue Eng Regen Med | Rabbit MSC chondrogenesis | Cartilage/bone | NR in abstract | NR | NR | Compared ubiquitous PEMF settings with Ca2+ ICR settings | 3 weeks | Only the Ca2+ ICR group raised GAG, type II collagen, COL2A1/SOX9/ACAN. Common PEMF settings did nothing | In vitro; includes positive and negative controls; no replication |
| 18288680 | Vincze 2008, Bioelectromagnetics | Theory | -- | -- | -- | -- | Damped ion in Lorentz force | -- | Drift velocity has resonance terms with Bessel dependence on AC/DC ratio and Omega/omega, and an explicit damping term | Theory |
| 19437458 | Muehsam & Pilla 2009, Bioelectromagnetics | Theory fit to published IPR data | -- | uT range | -- | -- | Lorentz/Larmor model | -- | Authors' fit suggests Mg2+ rather than Ca2+ as the target in Ca2+ flux, PC-12 neurite and CaM-myosin data | Theory |

### 1C. Pilla Ca/CaM first-messenger model, NO and cGMP

| PMID | First author, year, journal | System | Modality | B | dB/dt | E / J | Freq / waveform / pulse width | Dose / schedule | Key result | Quality |
|---|---|---|---|---|---|---|---|---|---|---|
| 22005645 | Pilla 2011, Biochim Biophys Acta | Cell-free CaM kinetics; chondrocyte, endothelial, neuronal cultures | Pain / wound / neural | NR in abstract | NR | NR | Pulse duration or carrier period shorter than bound-Ca2+ lifetime (numeric value NR in abstract) | NR | Several-fold rise in NO and cGMP (chondrocyte, endothelial) and cAMP (neuronal). CaM antagonists and downstream blockers abolished the effects | In vitro; model-driven; senior author's own lab |
| 22940137 | Pilla 2012, Biochem Biophys Res Commun | MN9D dopaminergic cells; human fibroblasts | Neural / pain / inflammation | NR | NR | NR | Pulse-modulated RF (PRF) | Fibroblasts: 15 min | Almost 3-fold NO rise from MN9D within seconds of LPS challenge (electrochemical electrode). In fibroblasts, nearly 2-fold NO rise, blocked by W-7. Only challenged cells responded | In vitro; antagonist control; one lab |
| 10228567 | Pilla 1999, Bioelectrochem Bioenerg | Cell-free CaM myosin phosphorylation; neurite outgrowth; rabbit fracture model | Bone / neural | NR | NR | NR | Burst duration of a PRF waveform retuned using ion-binding kinetics | NR | Retuned signal matched the clinical signal for phosphorylation, neurite outgrowth and fracture strength with 10x lower peak amplitude, about 800x lower average amplitude and about 10^6x lower average power | In vitro and animal; supports timing/spectral matching over amplitude |
| 23675615 | Pilla 2013, Electromagn Biol Med | Review | Pain / wound / bone | -- | -- | -- | -- | -- | CaM-dependent NO signalling as the EMF target; "a priori" signal configuration | Review, by the model's originator |
| 18240331 | Fitzsimmons 2008, J Orthop Res | Human chondrocytes, capacitively coupled pulsed electric field | Cartilage / pain | NR | NR | NR (electric coupling) | PEF; waveform NR | 30 min | DNA +150% at 72 h. NO and cGMP rose within 30 min. W7, L-NAME, LY83583 blocked it. Ionophore or extra Ca2+ alone raised NO | In vitro; inhibitor panel; electric not magnetic |
| 16677936 | Li 2006, Ultrasound Med Biol | Rat osteoblasts | Bone | NR | NR | NR | PEMF | 2 h | Proliferation via cytosolic Ca2+ and CaM; transduction pathways differ from those for ultrasound | In vitro |

### 1D. Clinical / animal PEMF studies in the Ca/CaM/NO framework (pain, circulation, wound)

| PMID | First author, year, journal | System | Modality | B / dB/dt / E | Freq / waveform | Dose / schedule | Key result | Quality |
|---|---|---|---|---|---|---|---|---|
| 18506512 | Heden 2008, Aesthetic Plast Surg | Breast augmentation, n = 42 (80 breasts) | Pain | NR in abstract | NR | NR in abstract | VAS fell about 3x faster than sham by POD 3 (p < 0.001); analgesic use also fell about 3x faster | RCT, double-blind, sham-controlled; Pilla co-author |
| 20527063 | Rohde 2010, Plast Reconstr Surg | Breast reduction, n = 24 | Pain / inflammation | NR | NR | NR | Pain -57% at 1 h, then larger falls to 48 h; narcotic use 2.2x lower; wound IL-1beta 275% lower; TNF-alpha, VEGF, FGF-2 unchanged | RCT, double-blind, placebo-controlled; small; Pilla co-author |
| 22451021 | Nelson 2013, Rheumatol Int | Early knee OA, n = 34 | Pain | NR | NR | NR | Active VAS -50 +/- 11% vs baseline from day 1 to day 42 (p < 0.001); sham not significant | RCT, double-blind pilot; Pilla co-author |
| 25199571 | Taylor 2014, J Surg Res | Breast reduction cohorts vs historical sham | Pain; schedule dependence | NR | NR | 20 min per 4 h (Q4), 15 min per 2 h (Q2), 5 min per 20 min (5/20) | Q4 and Q2 sped pain reduction; 5/20 did not (pain 87% of the 1 h value vs 74% in Q4 sham; narcotic use 2x higher than Q4 active). Authors suggest that faster NO build-up with 5/20 may trigger phosphodiesterase block of cGMP | Non-randomised active cohorts vs historical sham; Pilla co-author; the mechanism is a hypothesis |
| 25343187 | Bragin 2014, J Neurosurg | Rat cortex, in vivo two-photon imaging | Vasodilation / circulation / neural | NR in abstract (SofPulse device) | NR | 30 min, one exposure | Arteriole diameter 26.4 -> 29.1 um (p < 0.01); RBC velocity +5.5%; NADH fell to 94.7%. All blocked by L-NAME (10 mg/kg); no change in untreated controls | Animal, n = 11 active, 7 L-NAME, 5 time-controls. Effect size small |
| 31915323 | Peng 2020, Circ J | Mouse myocardial infarction | Circulation / angiogenesis | 1.5 mT at 15 Hz vs 3.0 mT at 30 Hz | NR. If pulse width is fixed, dB/dt ratio is 2x; if waveform scales with period, 4x (both computed by me) | NR | 45 min/day, 2 weeks | Both settings raised capillary density, VEGF, p-Akt, p-eNOS (S1177). Only 30 Hz/3.0 mT significantly improved function. B and frequency were varied together | Animal; sham PEMF group; dose-ordering is confounded |
| 26045885 | Li 2015, Am J Transl Res | Mouse hindlimb ischaemia; HUVEC | Circulation / wound | 5 mT | 30 +/- 3 Hz | 4 cycles x 8 min/day for 14 days | Faster wound healing, more neovascularization, higher VEGF, p-eNOS, p-Akt. Blocked by PI3K or eNOS inhibitors | Animal and in vitro; PMC record |
| 27780890 | Ma 2016, Biosci Rep | Rat ischaemia/reperfusion; cardiomyocytes | Circulation | NR | NR | NR | p-Akt and p-eNOS rose, NO release up, apoptosis down | Animal and in vitro |
| 19799606 | Patruno 2009, Br J Dermatol | HaCaT keratinocytes | Wound | NR | ELF | various exposure times | iNOS and eNOS expression up, NO up, COX-2 and PGE2 down, proliferation up | In vitro |
| 15208265 | Tepper 2004, FASEB J | Endothelial cells; mouse in vivo | Wound / angiogenesis | NR | PEMF | NR | Tubulization 7x, proliferation 3x; FGF-2 release; FGF-2 neutralizing antibody blocked it. Not a Ca/NO result, and shown here to contrast | In vitro and in vivo; single-blind |
| 17427956 | Schnoke 2007, J Orthop Res | Osteoblast-like cells | Bone | NR | PEMF | acute | eNOS, IRS-1, S6 phosphorylated like PTH or insulin; ERK and CREB were NOT activated by PEMF | In vitro; conflicts with CREB-pathway reports in 1E |
| 16222888 | Morimoto 2005, J Int Med Res | Cultured endothelial cells (HUVEC, microvascular, aortic) | Vasodilation | NR | EMF | dose-dependent | Thrombin-stimulated endothelin-1 reduced in all four cell types; reversed by the NOS inhibitor L-NMMA. Basal ET-1 reduced in only some types | In vitro |
| 20119972 | Martino 2010, Bioelectromagnetics | HUVEC | Vasodilation | weak static fields (values NR) | static | various doses | Effects on eNOS, NO and VEGF gene expression reported; dB/dt = 0, and author statement that induced E is the PEMF dose metric | In vitro |
| 27430265 | Nakayama 2016, Int J Radiat Biol | RAW264 macrophages | Inflammation; null for NO | 0.5 mT | 50 Hz | 24 h | Field alone did not change NO. With LPS, DNA single-strand breaks rose and viability fell, not through NO | In vitro; null for NO |

### 1E. Bone: NO/cGMP, cAMP, Ca2+ channels

| PMID | First author, year, journal | System | B / dB/dt / E | Freq / waveform | Dose | Key result | Quality |
|---|---|---|---|---|---|---|---|
| 35616355 | He 2022, FASEB J | Rat calvarial osteoblasts +/- primary cilia | 0.6 mT; dB/dt 0.19 T/s only if sinusoidal (computed by me; waveform NR) | 50 Hz | NR in abstract | Osteogenesis via NOS/NO/sGC/cGMP/PKG; eNOS phosphorylated in cilia; L-NAME blocks it; cilium removal blocks it | In vitro; inhibitors |
| 30350869 | Li 2018, Bioelectromagnetics | Hindlimb-suspended rats; osteoblasts | 0.6 mT, 50% duty cycle | 50 Hz | 90 min/day, 4 weeks. Parameters chosen from high-throughput screening of cultured osteoblasts | Prevented about 50% of BMD and strength loss; sAC/cAMP/PKA/CREB maintained | Animal; the screening range is NR in abstract |
| 30837038 | Wang 2019, Acta Acad Med Sin | Rat osteoblasts | 0.6 mT | 50 Hz | 3, 6, 9 days (ALP); minutes for signalling | ALP up at 3, 6 and 9 days. cAMP up at 30 and 60 min; p-PKA, p-CREB up from 15 min; cilium knockdown blunts it | In vitro; Chinese-language record |
| 36680558 | Hao 2023, J Bone Miner Res | Hypobaric-hypoxia rats; osteoblasts | 20 G (2 mT) | 15 Hz | 6 weeks | Improved bone mass; PC-1/PC-2 ciliary Ca channel -> sAC -> cAMP -> lower HIF-1alpha | Animal and in vitro |
| 26364969 | Petecchia 2015, Sci Rep (full text read) | Human BM-MSC osteogenesis | 2 +/- 0.2 mT; "induced electronic tension" 5 +/- 1 mV (a voltage, not E in V/m); dB/dt NR (about 1.5 T/s if a linear ramp over the whole 1.3 ms pulse; computed by me, crude) | 75 +/- 2 Hz, pulse 1.3 ms | 10 min/day for up to 27 days | Early Ca rise: day 9 [Ca]i 30% higher than ODM alone; L-type VGCC-expressing cells 40% -> 100%; Ca current 199 vs 70 pA at day 9. Mineral deposition was reduced by PEMF | In vitro; patch clamp plus Fura-2; no sham-field blinding described |
| 31518158 | Yap 2019, FASEB J | C2C12 myoblasts | 1.5 mT | pulsed | 10 min, single exposure | TRPC1-dependent Ca entry; CRISPR knock-down of TRPC1 abolished it; TRPM7 knock-down did not; aminoglycosides blocked it | In vitro; genetic loss-of-function; full text not retrievable, so dB/dt NR |
| 33644848 | Madanagopal 2021, Eur Cell Mater | Dental pulp stem cells | 2 mT | NR | 10 min | Neurogenic induction through TRPC1; blocked by penicillin/streptomycin | In vitro; same group as Yap |
| 27856256 | Zhang 2016, Biochem Biophys Res Commun | RAW264.7 osteoclastogenesis | NR | NR | NR | PEMF suppressed RANKL-induced Ca oscillations, calcineurin up, NFATc1 nuclear entry down, fewer osteoclasts | In vitro |
| 9699506 | Shankar 1998, J Cell Physiol | Rat osteoclasts, osteoblast cocultures | NR | PEMF | 18 h | 2x resorption only with osteoblasts present; PEMF removed calcitonin's block of the Ca receptor (Ni2+ response) | In vitro |
| 6287472 | Luben 1982, PNAS | MMB-1 osteoblast-like cells | Induced extracellular E 1 mV/cm or less (reported) | 15 Hz bursts or 72 Hz pulse train | NR | PTH-stimulated cAMP reduced by both signals; adenylate cyclase basal and NaF-activated unchanged; PTH-receptor-cyclase coupling blocked | In vitro; two clinical waveforms behaved alike |
| 2988718 | Farndale 1985, Calcif Tissue Int | Rabbit marrow fibroblasts | NR | PEMF | confluent cultures | Collagen production up; cAMP lowered; temperature rise below 0.1 C | In vitro |
| 30920672, 35129008 | Yang 2019; Ye 2022, Bioelectromagnetics; Electromagn Biol Med | Human amniotic FL cells | NR in abstract | 50 Hz | NR | [Ca]i rise via L-type channel; BAPTA blocks proliferation fully, nifedipine only partly; some Ca rise persisted in Ca-free medium (store release) | In vitro |

### 1F. VGCC / Ca influx dose-ranging and static-field comparators

| PMID | First author, year, journal | System | B / dB/dt | Freq | Key result | Quality |
|---|---|---|---|---|---|---|
| 16838272 | Lisi 2006, Bioelectromagnetics | Pituitary AtT20 D16V | 2 mT; 0.63 T/s if sinusoidal peak (computed by me) | 50 Hz | [Ca]i rose and pHi fell. 0.3 uM nifedipine blocked the differentiation marker | In vitro |
| 30312357 | Wu 2018, PLoS One | PC12, FL cells | 0.4 mT; 0.13 T/s if sinusoidal peak (computed by me) | 50 Hz | Microtubule reorganization needed L-type channel phosphorylation and [Ca]i rise | In vitro |
| 29784011 | Zhang 2018, Stem Cell Res Ther | Human BM-MSC migration | 1 mT at each of 7.5, 15, 30, 50, 70 Hz; sinusoid dB/dt would span 0.047 to 0.44 T/s (computed by me; waveform NR) | 7.5 to 70 Hz | All five frequencies promoted migration. Verapamil blocked it. No frequency window found in this range | In vitro; a single end point; response not graded across B |
| 9872934 | Fanelli 1999, FASEB J | Human cell lines, apoptosis | Static, 6 G (0.6 mT) to plateau at 6 mT | static | Intensity-dependent anti-apoptotic effect via Ca influx | In vitro; dB/dt = 0, so B alone can act without induction |
| 16528477 | Ghibelli 2006, Apoptosis | Jurkat and tumour cells | NMR device (1 T static plus RF) | NR | Ca influx via L-type channels raised apoptosis 1.8 to 2.5x; chelation or channel block prevented it | In vitro |
| 8045284 | Karabakhtsian 1994, FEBS Lett | HL-60 | NR | ELF | Low extracellular Ca2+ reduced c-fos and c-myc transcript responses | In vitro |
| 8986359 | Eichwald & Walleczek 1996, Bioelectromagnetics | Model | -- | -- | Biphasic or activation-dependent responses explained by cooperative enzyme kinetics | Theory |

### 1G. Reviews and advocacy sources (not primary data)

| PMID | Author, year | Content | Comment |
|---|---|---|---|
| 23802593 | Pall 2013, J Cell Mol Med | Reviews 23 studies in which VGCC blockers lower or block EMF effects (table has no exposure values). Proposes VGCC -> Ca/CaM -> NO -> cGMP/PKG as the therapeutic route, and NO -> peroxynitrite for harm | Narrative, single author; the table lists ELF, static, microwave and ns pulses together, so it cannot give a threshold. Same author also argues static fields work through VGCC, which conflicts with a pure dB/dt story |
| 25879308, 29573716, 35114921, 34043892, 26300312 | Pall 2015 to 2022 | VGCC mechanism applied to microwaves, Wi-Fi, Alzheimer's | Advocacy-style reviews; contain claims ("hundreds of studies", "non-monotone dose response") not supported by data given in the abstracts. Treat as hypothesis-level |
| 20707644, 19811395, 18097820, 31032646, 23323834, 19337897 | Liboff 2007 to 2019; Foletti 2009, 2013 | ICR-like mechanisms; ultraweak AC (0.05 uT) effects; commercial-device claims | Hypothesis papers; device studies lack exposure detail in abstracts |

---------------------------------------------------------------------

## 2. Synthesis per target

### 2.1 Ca2+ entry / [Ca2+]i (VGCC, TRPC1, store release)

What the data say:
- Ca2+ rises after ELF/PEMF in many cell types: Jurkat (Lindstrom 7748202), thymocytes (Liburdy 1333413), AtT20 (Lisi 16838272), amniotic FL cells (Yang 30920672), BM-MSC (Petecchia 26364969), myoblasts via TRPC1 (Yap 31518158). L-type channel blockers (nifedipine, verapamil) reduce downstream effects in several of these (Lisi, Wu, Zhang 2018, Yang). BAPTA blocks more completely than nifedipine (Ye 35129008), and some Ca rise persists in Ca-free medium, so store release contributes. This is not a VGCC-only story.
- Gating by cell state is consistent: thymocytes (Liburdy; Walleczek 1468568) and Jurkat (Lindstrom) respond only when Ca signalling is already active, with an inhibit-or-stimulate sign that depends on activation level. This fits a modulator of an active pathway rather than a trigger, which also fits Pilla's finding that only challenged cells make NO (22940137).

Quantitative window (best-supported numbers):
- Lymphocyte/Jurkat acute Ca response: threshold below 0.04 mT, plateau at about 0.15 mT at 50 Hz (Lindstrom, B-sweep, single study); dB/dt 0.013 to 0.047 T/s if sinusoidal peak (computed by me). Induced E in cells NR. This is the only study in the set with a true B threshold and saturation for [Ca]i. Two blinded or flow-cytometric attempts at the same exposure (Wey 10656853; Lyle 9261541) found nothing. The effect cannot be treated as established.
- Thymocyte 45Ca influx: positive at 22 mT/60 Hz with Einduced 1.7 mV/cm (Liburdy), and at 3 Hz pulsed 6.5 mT (E 0.69 mV/cm, J 2.6 uA/cm2) with magnitude increasing across 1.6 to 28 mT (Walleczek).
- Stem cell/myoblast, brief pulsed exposure: 1.5 to 2 mT, 10 min (Yap; Madanagopal; Petecchia 75 Hz/1.3 ms). No lower bound or saturating level was tested in the records I read; "minimum effective" is therefore unknown above 1.5 mT.
- Continuous 50 Hz studies at 0.4 to 2 mT (Wu, Lisi, FL cells) show Ca-dependent effects; none gave a threshold sweep.

What drives it:
- Evidence for induced E over B: Liburdy 1992 is the cleanest discrimination in this cluster. At constant 22 mT the response followed induced E in the annular rings, and a pure 60 Hz E field of equal strength gave the same Ca change. My own check (computed by me): 22 mT at 60 Hz gives 8.3 T/s peak, and E = 1.7 mV/cm implies a ring radius of 4.1 cm, which is a plausible dish size. That makes the induced-E interpretation internally consistent. This is one lab and has not been independently repeated in the set.
- Walleczek's B sweep cannot discriminate because E scaled with B.
- Against dB/dt as the sole driver: (a) static fields (dB/dt = 0) move Ca influx, apoptosis and CaM-linked enzymes (Fanelli 9872934, plateau 6 mT; Liboff 12483663, 20 uT; Ghibelli 16528477); some of these are single-lab and the cell-free CaM result was not reproduced (Coulton 10723019). (b) Zhang 2018 found a similar migration response at 1 mT across 7.5 to 70 Hz, a 9-fold dB/dt span (computed by me, waveform assumed sinusoidal). That is one end point with no dose gradation, so only weak evidence of frequency independence.
- Net view: for the Ca2+ entry step the evidence favors induced E (so dB/dt x geometry) at power-line and PEMF frequencies, with a separate B-dependent route (not induction) for static and geomagnetic-scale fields. Neither has a verified minimum E. Confidence: low.

Failures and nulls: Wey 2000, Lyle 1997, Coulton & Barker 1993 (all null for [Ca]i). Positive studies are mostly single-lab. Many used ConA or anti-CD3 co-stimulation, and effect sizes were 1.5-fold or smaller (Liburdy 1993) or -45% (Walleczek).

Confidence rating: Ca2+ rise exists but is cell-state dependent and poorly replicated at 50/60 Hz; the numeric threshold is low-confidence (the single sweep of Lindstrom was not replicated).

### 2.2 Calmodulin / Ca-CaM binding (Pilla model)

- Claim: signals with pulse (or carrier period) shorter than the bound-Ca2+ lifetime can accelerate Ca binding to CaM and be detectable above thermal noise; burst width, not amplitude, is the tuning variable (22005645; 10228567). Pilla 1999 reports an equal bioeffect from a retuned burst with a 10x lower peak amplitude, 800x lower average amplitude, and 10^6x lower average power (cell-free myosin phosphorylation, neurite outgrowth, rabbit fracture). If valid this is the strongest argument in the cluster that timing/spectral content rather than B or dB/dt magnitude sets the effect.
- Numbers I could not retrieve from the abstracts: the actual burst width, carrier frequency, B and dB/dt for the clinical PRF signal, and the CaM binding time constant. I will not supply them from memory.
- Independent tests: Coulton 2000 (10723019) did not reproduce a static-field effect on Ca/CaM-dependent MLC phosphorylation, including a direct replication; Liboff 2003 (12483663) found a CaM-dependent PDE effect at 20 uT static with a maximum near half-activation Ca2+. The two cell-free outcomes conflict. Muehsam & Pilla 2009 refit older IPR data to Mg2+ rather than Ca2+, which weakens Ca/CaM specificity of the resonance data.
- Drive variable: spectral/timing match to a kinetic constant (a frequency/pulse-width window) with amplitude secondary; model-derived, with the direct cell-free evidence from the originating lab. Confidence: low to moderate (mechanistic coherence and antagonist data in 22005645, 22940137, 18240331; but one lab, the abstracts lack the exposure values, and an independent null exists).

### 2.3 eNOS / NO / cGMP

- In vitro: Pilla's group shows NO and cGMP rise in chondrocytes and endothelial cells, with W-7 or L-NAME or guanylate cyclase inhibitors blocking (22005645; 18240331 with a capacitive electric field). Real-time NO about 3-fold in MN9D within seconds, and about 2-fold in fibroblasts (22940137). Outside that group: osteoblasts at 0.6 mT/50 Hz via NOS/NO/sGC/cGMP/PKG (35616355), eNOS phosphorylation after PEMF in osteoblasts (Schnoke 17427956), p-eNOS in mouse ischaemia models at 5 mT/30 Hz (26045885) and at 1.5 mT/15 Hz or 3.0 mT/30 Hz (31915323), HaCaT iNOS/eNOS up (19799606), ET-1 suppression by an NO route (16222888).
- Nulls: Nakayama 2016 (27430265): 0.5 mT, 50 Hz for 24 h alone did not alter NO in RAW264; RAW264 only changed with LPS present. This again says field effects need a challenge, but it also says there is no baseline NO effect.
- In vivo: PEMF-induced cerebral arteriolar dilation (+10%) and tissue oxygenation were abolished by L-NAME (Bragin 25343187). Exposure values NR in the abstract. Effect size is small and 3 h persistence is the main finding.
- Schedule dependence (clinical): Taylor 2014 (25199571): 20 min every 4 h and 15 min every 2 h worked, 5 min every 20 min did not (non-randomised, historical sham). The authors' proposal is that faster NO build-up in the 5/20 pattern triggers phosphodiesterase breakdown of cGMP and cancels the effect. That is a hypothesis; no cGMP data in the abstract. This is the only evidence in the cluster for an upper limit of dose frequency in a patient setting, and it is a single non-randomised cohort.
- Drive variable: no study retrieved varies B, dB/dt and frequency independently for NO. Within the Peng 2020 mouse data (31915323) the higher setting (3.0 mT/30 Hz) outperformed 1.5 mT/15 Hz for function, but both raised p-eNOS, so a threshold for eNOS phosphorylation lies at or below 1.5 mT/15 Hz and the functional benefit rose with the product (confounded B x f). Confidence: moderate that NO/eNOS participates (inhibitor data across many labs), low for any numerical threshold.

### 2.4 cAMP

- Direction depends on tissue and agonist. PEMF reduced PTH-stimulated cAMP in osteoblast-like cells at induced E <= 1 mV/cm (Luben 6287472) and lowered cAMP in marrow fibroblasts (Farndale 2988718). Conversely, 50 Hz 0.6 mT raised cAMP at 30 to 60 min with p-PKA/p-CREB in rat osteoblasts (Wang 30837038), and 15 Hz/2 mT raised cAMP via sAC through a ciliary PC-1/PC-2 Ca channel (Hao 36680558). Pilla reported cAMP rises in neuronal cultures (22005645). Schnoke (17427956) found CREB and ERK were not activated by PEMF. So the sign is context dependent, and CREB involvement conflicts.
- Amplitude: the only graded values are Luben's E <= 1 mV/cm (low) and the Lanzhou group's 0.6 mT (50 Hz, 50% duty), selected by screening in cultured osteoblasts; the screening range is NR. Confidence: low.

### 2.5 Ion cyclotron / parametric resonance (Liboff, Lednev, Zhadin, Blackman)

- Positive reports: Ca2+ influx inhibition in thymocytes with 16 Hz AC 42.1 uT plus 23.4 uT DC and no effect from either alone (Yost & Liburdy 1733766); Zhadin rat behaviour at Ca and Mg cyclotron frequencies that kept the same effect when DC rose from 50 to 500 uT with proportional AC (10453066); snail analgesia depending on PRM parameters and light (Prato 10797457); IPR hydrogen bandwidth within +/-10% of resonance, replicated across three runs and a prior lab (Blackman 9915588; this is H+ and PC-12 neurite outgrowth, not Ca2+); ICR-Ca-tuned fields promoting chondrogenesis where generic PEMF did not (Kavand 30793837).
- Nulls: Coulton & Barker 1993 (8451278) tested 16 and 50 Hz Ca conditions with DC shifts to +/-25% and saw no [Ca]i change. Coulton 2000 (10723019) failed on cell-free CaM. Muehsam & Pilla 2009 suggest Mg2+ fits the older data better.
- Which variable: the resonance claim is a statement about the AC/DC amplitude ratio and an f/B_DC relationship (f_c(Ca2+) = 0.766 Hz per uT, computed by me, e.g. 38 Hz at 50 uT). Amplitude windows are narrow (about +/-10% in frequency; Blackman 1999). Blackman's 1989 RF efflux data show multiple discontinuous power windows (7 enhanced and 9 null power densities, interleaved), which is hard to reconcile with a smooth threshold or saturation model. The Zhadin scaling (computed by me) means a 100-fold change in dB_ac/dt (AC frequency and amplitude both scaled 10x) gave a qualitatively unchanged outcome. Such an invariance argues against a dB/dt-threshold mechanism for this class and for a frequency-to-DC relation instead.
- Clinical relevance: the fields used are microtesla and sub-microtesla, with induced E far below the PEMF range; no bone or pain RCT in the retrieved set uses ICR settings. Confidence for ICR as a therapeutic dose rule: speculative to low. Confidence for ICR as a real, narrow-window laboratory effect: low (mixed replications).

### 2.6 Ca2+ efflux / ion-binding (Bawin & Adey)

- Original cerebral-tissue data give frequency-window and amplitude-threshold behaviour: efflux fell 12 to 15% with maximum at 6 and 16 Hz and thresholds of about 10 V/m in air for chick tissue and 56 V/m for cat (1064869). Tissue-level gradient estimate was about 0.1 uV/cm (authors' estimate), orders of magnitude below the E values used in the lymphocyte studies (0.7 to 1.7 mV/cm). The AM-RF efflux literature is non-monotone (Blackman 1989), and Adey 1982 had weak statistics (p = 0.96 confidence). I did not retrieve any direct independent replication or failed replication of efflux in this session. Confidence: low.

### 2.7 Pall's VGCC voltage-sensor hypothesis

- Evidence cited: 23 studies where VGCC blockers block or lower EMF effects (Pall 2013). The review table lists field type and channel class but no amplitude or frequency, so no threshold can be extracted. Pall proposes that therapeutic effects go through Ca/NO/cGMP/PKG, and says "non-monotone" and "pulsed fields more active" dose-response. In the primary data I retrieved: nifedipine or verapamil reduced effects in 4 independent labs (Lisi, Wu, Zhang 2018, Yang/Ye) but BAPTA did more, and Ca-free medium did not abolish the response (35129008). TRPC1, not L-type, was the Ca entry route in myoblasts (Yap). Therefore VGCC is a plausible entry route in some systems, not a single universal target. Confidence: moderate that L-type VGCC contributes in several cell types; low that it is the primary transducer. The mechanism is supported by pharmacology only, and blockers have non-specific actions.
- Where he claims "dirty electricity" or nanosecond pulses act through VGCC, the nanosecond data are in a different regime (kV/m, ns) and one Arabidopsis ns-pulse study found little response (37408527); not relevant to PEMF thresholds.

### 2.8 Modality summary

| Modality | Best-supported parameters (as reported) | Driver | Confidence |
|---|---|---|---|
| Pain / inflammation | Three small double-blind sham-controlled trials (n = 24 to 42) and one pilot (n = 34), all with Pilla as co-author, with exposure values NR in abstracts. Schedule evidence: 15 to 20 min every 2 to 4 h worked, 5 min every 20 min did not (non-randomised) | Cannot be assigned. Timing/schedule shows an effect; amplitude values not retrievable | Low to moderate (clinical effect), speculative (parameter dependence) |
| Vasodilation / circulation | One rat study with L-NAME block (Bragin; +10% diameter). Mouse MI: 1.5 mT/15 Hz and 3.0 mT/30 Hz for 45 min/day both raised p-eNOS; ischaemia: 5 mT/30 Hz, 4 x 8 min/day | NO/eNOS dependent; B and f confounded | Low |
| Wound repair | HaCaT iNOS/eNOS up; ischaemic hind-limb wound healing 5 mT/30 Hz; FGF-2 route (Tepper) is not Ca/NO | Not separable | Low |
| Bone | 0.6 mT/50 Hz (50% duty, 90 min/day) selected by screening; 2 mT/15 Hz rats; 2 mT/75 Hz/1.3 ms 10 min/day in MSC; E <= 1 mV/cm for cAMP effects | Both B (kept 0.6 to 2 mT) and signal shape; no threshold sweep retrieved | Low to moderate for NO/cGMP involvement |
| Neural | 1 mT/15 Hz/3.75 ms daily for 7 days raised spontaneous Ca signalling in iPSC neurons (Chen 40713855, no sham details in abstract); 2 mT/50 Hz AtT20; snail analgesia 141 to 414 uT | Not separable | Low |

---------------------------------------------------------------------

## 3. B vs dB/dt vs frequency: summary of what the evidence supports

1. The single direct B-vs-E discrimination for Ca2+ influx (Liburdy 1992) supports induced E (so dB/dt and geometry) at 60 Hz, 22 mT, E about 1.7 mV/cm. Replication by an independent lab: none retrieved.
2. The single B-threshold sweep for [Ca]i (Lindstrom 1995: threshold below 0.04 mT, plateau 0.15 mT at 50 Hz) was not reproduced by two independent labs. The implied dB/dt (0.013 to 0.047 T/s if sinusoidal peak, computed by me) is two to three orders of magnitude below Liburdy's, so the two positive studies are not consistent with a common dB/dt or E threshold. Combined with the nulls, no minimum effective dB/dt or E for Ca2+ signalling can be stated with confidence.
3. Static-field effects (Fanelli 6 G to 6 mT plateau; Liboff 20 uT; Ghibelli 1 T) show that a B-dependent route exists without induction, though one cell-free case failed (Coulton 2000).
4. Frequency/timing windows: Lindstrom's broad optimum near 50 Hz (5 to 100 Hz tested), Blackman's +/-10% IPR bandwidth, Bawin & Adey's 6 to 16 Hz maxima, and Pilla's burst-width tuning (10x lower peak amplitude, same effect) point to frequency or timing as an organizing variable. Zhang 2018 (no frequency preference from 7.5 to 70 Hz at 1 mT) points the other way for MSC migration.
5. Amplitude windows (non-monotone) are reported for modulated RF efflux (Blackman 1989), for biphasic sign changes in lymphocytes (Walleczek 1992; modelled by Eichwald & Walleczek), and for schedule saturation in pain (Taylor 2014). I found no study showing an ineffective high-amplitude level for ELF Ca/NO at the mT scale, other than the sign reversal in lymphocytes.
6. In short: B, dB/dt (via E) and frequency/pulse timing each have at least one supporting study; none is established as the single driver. The currently best-supported statement is that response depends on E (rather than B per se) for induction at 50/60 Hz in cell cultures, and on pulse timing relative to biochemical kinetics for the Pilla pathway. Overall confidence: low.

---------------------------------------------------------------------

## 4. Key references (PMID | DOI)

1. 1333413 | 10.1016/0014-5793(92)80209-y | Liburdy RP. FEBS Lett 1992. Ca signalling in lymphocytes follows induced E at constant B (22 mT, 60 Hz, 1.7 mV/cm).
2. 1468568 | 10.1016/0014-5793(92)81504-f | Walleczek J, Budinger TF. FEBS Lett 1992. 3 Hz pulsed field, B 0 to 28 mT, E 0.69 mV/cm at 6.5 mT, state-dependent sign.
3. 7748202 | 10.1002/bem.2250160110 | Lindstrom E et al. Bioelectromagnetics 1995. Jurkat Ca oscillations: threshold below 0.04 mT, plateau 0.15 mT, optimum 50 Hz.
4. 10656853 | 10.1289/ehp.00108135 | Wey HE et al. Environ Health Perspect 2000. Blinded failure to replicate Lindstrom.
5. 9261541 | 10.1002/(sici)1521-186x(1997)18:6<439::aid-bem6>3.0.co;2-3 | Lyle DB et al. Bioelectromagnetics 1997. Null for 0.15 mT 60 Hz on Jurkat Ca signalling.
6. 8451278 | 10.1088/0031-9155/38/3/002 | Coulton LA, Barker AT. Phys Med Biol 1993. Null for Ca ICR at 16 and 50 Hz.
7. 10723019 | 10.1002/(sici)1521-186x(200004)21:3<189::aid-bem6>3.0.co;2-l | Coulton LA et al. Bioelectromagnetics 2000. Failed replication of static-field effect on Ca/CaM-dependent phosphorylation.
8. 22005645 | 10.1016/j.bbagen.2011.10.001 | Pilla A et al. Biochim Biophys Acta 2011. EMF as first messenger, Ca/CaM/NO/cGMP.
9. 10228567 | 10.1016/s0302-4598(98)00148-2 | Pilla AA et al. Bioelectrochem Bioenerg 1999. Ion-binding kinetics predict waveform; 10x lower peak amplitude with same effect.
10. 22940137 | 10.1016/j.bbrc.2012.08.078 | Pilla AA. Biochem Biophys Res Commun 2012. Immediate NO rise in challenged cells, blocked by W-7.
11. 25199571 | 10.1016/j.jss.2014.08.007 | Taylor EM et al. J Surg Res 2014. Dosing schedule determines PEMF pain effect.
12. 20527063 | 10.1097/PRS.0b013e3181c9f6d3 | Rohde C et al. Plast Reconstr Surg 2010. Double-blind RCT, pain and IL-1beta.
13. 25343187 | 10.3171/2014.8.JNS132083 | Bragin DE et al. J Neurosurg 2014. NO-dependent cerebral arteriolar dilation.
14. 26364969 | 10.1038/srep13856 | Petecchia L et al. Sci Rep 2015. 2 mT, 75 Hz, 1.3 ms; Ca and L-type VGCC in MSC.
15. 31518158 | 10.1096/fj.201900057R | Yap JLY et al. FASEB J 2019. 1.5 mT, 10 min, TRPC1-dependent Ca entry.
16. 9915588 | 10.1002/(sici)1521-186x(1999)20:1<5::aid-bem2>3.0.co;2-r | Blackman CF et al. Bioelectromagnetics 1999. IPR bandwidth +/-10%.
17. 1064869 | 10.1073/pnas.73.6.1999 | Bawin SM, Adey WR. PNAS 1976. Frequency and amplitude sensitivity of Ca efflux.
18. 23802593 | 10.1111/jcmm.12088 | Pall ML. J Cell Mol Med 2013. VGCC hypothesis review (secondary).

---------------------------------------------------------------------

## 5. Limits of this dossier

- Most exposure parameters for the clinical PEMF devices and the Pilla signals were not in the abstracts, so dB/dt and induced E for the therapeutic signals could not be tabulated. They need device specifications or full text from outside this search.
- I did not retrieve Bassett/Brighton primary papers, Conti/Walleczek 1985 to 1990 work, the Trillo/Lednev-era Ca-flux replications, or any independent replication of Bawin-Adey efflux windows. Absence from this list is not evidence of absence.
- Several derived dB/dt values assume a sinusoidal waveform and peak (not rms) amplitudes; the original papers often do not say.
- PubMed's AND-style query handling returned few results for compound queries, so recall is limited, particularly for the 1980s to 1990s literature.
