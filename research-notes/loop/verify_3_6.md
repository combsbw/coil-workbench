# Independent fact-check: cluster 3 (bone/cartilage) and cluster 6 (vascular/wound/muscle)

Source of record: articles retrieved from PubMed (NCBI) via the PubMed MCP tools (get_article_metadata, get_full_text_article). DOIs are given as links where the files or the tool supplied them. Source files were read only, not edited.

Status key: VERIFIED = matches abstract/full text. CORRECTED = file wrong or over-stated; correct value given. UNVERIFIABLE = abstract (and any full text reached) does not contain the number. WRONG PMID = PMID resolves to a different paper.
"Calc" rows were recomputed independently (E = (r/2)dB/dt; sinusoid dB/dt_pk = 2 pi f B_pk; pulse dB/dt ~ B_pk/t_rise; probe V = N A dB/dt).

## 0. Headline results

- Bibliographic check (first author, year, journal, title): all PMIDs in both files resolved to the paper described (cluster 3: Section 5 list of 15 plus about 75 PMIDs in Section 1 tables; cluster 6: Section 3 list of 15 plus about 70 PMIDs in Section 1 tables). WRONG PMID: 0 of about 145.
- 30 priority quantitative claims (15 per file): 6 CORRECTED (5 substantive, 1 minor wording), 1 UNVERIFIABLE, 23 VERIFIED.
- Arithmetic: about 45 computed dB/dt and E values recomputed; 2 errors (Tsai E_rms is a method/arithmetic inconsistency; Prucha ">= 12 T/s" should be 11.8 T/s). All others correct to the stated rounding.
- Additional non-priority items: 3 UNVERIFIABLE (Jenis "not blinded for DC", Ko "twice weekly", and Wang 2019 30 G, counted above), 1 source typo (Mooney).

## 1. Cluster 3 (bone, cartilage, connective tissue): 15 priority quantitative claims

| PMID | Claim in file | Status | Correction / notes |
|---|---|---|---|
| 12929162 | Chang 2003: induced E 4.8, 8.7, 12.2 uV/cm rms; osteoclast-like cell formation enhanced about 50% or suppressed about 27% depending on E; 0.5, 2, 8 h/day for 7 days | VERIFIED | Matches abstract. [DOI](https://doi.org/10.1002/bem.10118) |
| 7639117 | Fitzsimmons 1995: E_max 1e-5 V/m at 15.3 Hz, 30 min, IGF-II receptor up, frequency-dependent | VERIFIED | Calc: B_ac = 2E/(r 2 pi f) = 13.9 uT at r = 1.5 cm; file's "about 14 uT" correct (geometry assumed by file). [DOI](https://doi.org/10.1002/jbmr.5650100519) |
| 10228567 | Pilla 1999: re-tuned PRF equal effect at 10x lower peak amplitude, about 800x lower average amplitude, about 10^6 lower average power | VERIFIED | [DOI](https://doi.org/10.1016/s0302-4598(98)00148-2) |
| 25661534 | Yan 2015: 0.6-3.6 mT in 0.6 mT steps, 50 Hz, 90 min/day; maximum proliferation at 0.6 mT; abolished by IFT88 siRNA | VERIFIED | Calc 2 pi 50 0.6e-3 = 0.188 T/s (file 0.19) correct. [DOI](https://doi.org/10.1016/j.mce.2015.01.031) |
| 26891468 | Zhai 2016: 0.5/1/2 mT, 15.38 Hz burst, 0.5/1/2/6 h/day, 3 days; best 2 mT at 2 h/day; Wnt1, Lrp6, b-catenin up | VERIFIED | [DOI](https://doi.org/10.1002/bem.21961) |
| 28741320 | Wang P 2017: RAW264.7+RANKL, 15 Hz, 2 h/day, 0.5/1/2/3 mT, 7 days; 0.5 mT decreases, 3 mT increases resorption via apoptosis | VERIFIED | Abstract uses the phrase "intensity window". [DOI](https://doi.org/10.1002/bem.22070) |
| 30422320 | Wang P 2019: 5 G (0.5 mT) reduced apoptosis genes and RANKL/OPG; 30 G (3 mT) did not | UNVERIFIABLE (30 G arm) | 5 G effect and cilia (polaris) dependence confirmed; the abstract does not state the 30 G outcome, so "3 mT did not" (also repeated in Section 2.4) is inference. |
| 17516509 | Tsai 2007: 0.13/0.24/0.32 mT rms, 7.5 Hz, 300 us quasi-rectangular pulses, 2 or 8 h/day, 18 days; 0.13 mT proliferation up; 0.32 mT proliferation inhibited, ALP up | VERIFIED (field/schedule/result) | See CORRECTED item in Section 3: computed E_rms. [DOI](https://doi.org/10.1002/bem.20336) |
| 17516509 | "Computed by me: E_rms about 1.5-7.6 uV/cm for r = 1.5-3 cm" (dB/dt >= 0.43, 0.8, 1.07 T/s) | CORRECTED | dB/dt values correct (0.13/0.24/0.32 mT over 300 us = 0.43/0.80/1.07 T/s). But with the file's stated formula E = (r/2) dB/dt, E = 32 uV/cm (0.43 T/s, r = 1.5 cm) to 160 uV/cm (1.07 T/s, r = 3 cm), i.e. 20-100x larger than stated. The stated 1.5-7.6 uV/cm only reproduces if the peak E is multiplied by an unstated sqrt(duty) = sqrt(300 us x 7.5 Hz) = 0.0474. That is not the stated method, and it mixes a B_rms-based pulse-width dB/dt with a duty rms factor. The file's conclusion that this "falls in Chang's range (3-12 uV/cm rms)" is therefore not supported by the stated calculation (it depends on the duty-cycle assumption and on B being rms vs pulse peak, neither of which is in the abstract). |
| 12111759 | Diniz 2002: 7 mT peak, 15 Hz burst; stimulatory at proliferation/differentiation stages, inhibitory at mineralisation stage | VERIFIED | [DOI](https://doi.org/10.1002/bem.10032) |
| 36377077 (and 36854553) | Xu 2022/2023: at fixed 1 mT, "75 Hz > 45 Hz > 15 Hz"; 75 Hz exosomes reduced OARSI score in ACLT rat; both PMIDs treated as one study | CORRECTED | Frequency set 15/45/75 Hz at 1 mT is confirmed and 75 Hz is the best. The abstracts do not support a graded 45 > 15 ordering (only that 75 Hz was most effective). The ACLT OA in vivo model and OARSI result belong to 36377077 only; 36854553 (a separate Sheng Wu Yi Xue Gong Cheng Xue Za Zhi paper) is a different study and should not be merged. Section 3 table ("75 > 45 > 15") and Section 2.5 inherit the unsupported ordering. [DOI](https://doi.org/10.1177/19476035221137726) |
| 2218718 | Mooney 1990: 195 patients, double-blind sham, fusion 92% vs 65%, p < 0.005 | VERIFIED | Numbers and design match. Note: the abstract prints "P greater than 0.005" (source typo for less than); the file's p < 0.005 is the intended reading. [DOI](https://doi.org/10.1097/00007632-199007000-00016) |
| 21915570 | Adie 2011: 259 randomised, 218 analysed; 10 h/day, 12 weeks; surgery 16/106 vs 15/112, RR 1.02 (0.95-1.14) | VERIFIED | [DOI](https://doi.org/10.2106/JBJS.J.00869) |
| 21491410 | Griffin 2011 Cochrane: 4 RCTs, 125 adults, union RR 1.96 (0.86-4.48), I2 58% | VERIFIED | [DOI](https://doi.org/10.1002/14651858.CD008471.pub2) |
| 25047554 | Jing 2014: rotating field 0.60 to 0.38 T, 7 Hz, 2 h/day, 4 weeks, null; calc dB/dt_pk about 17-26 T/s, E 0.17-0.26 V/m at r = 2 cm | VERIFIED (study); calc correct under file's stated assumption | Recompute: 2 pi 7 x 0.38 = 16.7, x 0.60 = 26.4 T/s; E = 0.167-0.264 V/m. The file itself flags geometry as a guess (a rotating permanent-magnet field is not a sinusoid in a fixed loop); treat as order of magnitude. [DOI](https://doi.org/10.1371/journal.pone.0102956) |
| 30552258 | Wu 2018 meta-analysis: sessions <= 30 min better than > 30 min; file labels this "non-monotonic dose-duration finding" | CORRECTED | Subgroup comparison of session length (<= 30 vs > 30 min) is a two-bin contrast, which cannot show non-monotonicity. Also, Wu 2018 reported knee and hand benefit but not cervical (file correct). Replace "non-monotonic" with "shorter sessions associated with larger effects (two-group subgroup)". |

## 2. Cluster 6 (vascular, wound, muscle): 15 priority quantitative claims

| PMID | Claim in file | Status | Correction / notes |
|---|---|---|---|
| 31915323 | Peng 2020: 1.5 mT/15 Hz vs 3.0 mT/30 Hz, 45 min/day x 2 wk; both raise capillary density, VEGF, VEGFR2; only 30 Hz/3.0 mT improved cardiac function | VERIFIED | Calc 0.141 vs 0.565 T/s (file 0.14 vs 0.57), ratio 4.0. [DOI](https://doi.org/10.1253/circj.CJ-19-0758) |
| 18176216 | Callaghan 2008: 1.2 mT, 4.5 ms pulses, 15 Hz, 8 h/day x 14 d (via review); wound closure 11 vs 15 d (WT), 16 vs 24 d (diabetic) | VERIFIED (abstract; parameters via Mayrovitz 2022 full text PMC9184174) | Calc >= 1.2 mT/4.5 ms = 0.27 T/s correct. [DOI](https://doi.org/10.1097/01.prs.0000293761.27219.84) |
| 24244477 | Delle Monache 2013: 2 mT, 50 Hz sinusoid reduces HUVEC/MS-1 proliferation, migration, tubulation, VEGFR2 | VERIFIED | Calc 0.628 T/s (file 0.63). [DOI](https://doi.org/10.1371/journal.pone.0079309) |
| 33126773 | Vincenzi 2020: 1.5 +/- 0.2 mT, 2.0 +/- 0.5 mV in 50-turn 0.5 cm probe, 1.3 ms, 75 Hz; VEGF 3.2x at 24 h (288 to 922 pg/mL); HIF-1a independent | VERIFIED | Full text PMC7663527 read. Calc dB/dt = V/(N A) = 2.0e-3/(50 x 1.963e-5) = 2.04 T/s; E = (0.01/2) x 2.04 = 10.2 mV/m at r = 1 cm (file "about 2 T/s", "about 10 mV/m") correct. [DOI](https://doi.org/10.3390/ijms21218053) |
| 25343187 | Bragin 2014: E 6 +/- 1 V/m, SAR 40 mW/kg, 27.12 MHz, 3 ms bursts at 5 Hz, 30 min; arterioles 26.4 to 29.1 um (p<0.01); RBC velocity +5.5%; NADH to 94.7%; L-NAME abolishes; effect "lasted about 3 h" | CORRECTED (minor) | All numbers verified in full text PMC6320690 (arterioles +10.2%, NADH -5.3%). Duration: the full text shows the effect no longer significant at the 3 h time point, so "lasted about 3 h" over-states slightly; say "present during the first hours, not significant by 3 h". [DOI](https://doi.org/10.3171/2014.8.JNS132083) |
| 16320175 | Schuhfried 2005: 100 uT/30 Hz vs 8.4 mT/10 Hz, n = 12, null; 84-fold B, 28-fold dB/dt | VERIFIED | Calc 0.0188 vs 0.528 T/s, ratio 28.0; 8.4 mT/0.1 mT = 84. [DOI](https://doi.org/10.1055/s-2005-837451) |
| 27227568 | Sun 2016: 0.5 mT, 12 Hz, 30 min, 22 diabetic + 21 healthy; smallest-vein velocity up vs sham; flux/diameter no difference | VERIFIED | Calc 0.038 T/s. [DOI](https://doi.org/10.1002/bem.21983) |
| 3377866 | Cleary 1988: J time-avg 7 mA/m2 (peak 7 A/m2) max, +32% proliferation; 3.5 effective; 1.8 none; > 10 inhibitory; 1 ms, 1 Hz unipolar | VERIFIED (numbers) | Peak/average consistent (7 A/m2 x 1 ms x 1 Hz = 7 mA/m2). The file's gloss "inverted U about 4-fold wide" (Section 2.4) is the file's own interpretation: effective bracket 3.5-7 is 2-fold, bracket from "none" (1.8) to "inhibitory" (10) is about 5.6-fold. CORRECTED (interpretive): remove or restate as "effective between 1.8 and 10 mA/m2". [DOI](https://doi.org/10.1002/bem.2250090210) |
| 24395219 | Cheing 2014: STZ rats, 5 mT, 25 Hz, 1 h/day; closure and re-epithelialisation up on d10 and closure d14, no difference later | VERIFIED | Calc 0.785 T/s. [DOI](https://doi.org/10.1002/bem.21832) |
| 35814025 | Terrie 2022: 2 +/- 0.2 mT, 5 +/- 1 mV, 75 +/- 2 Hz, 1.3 ms; 2 h/day vs 22 h/day; day-8 start best (fusion index 66% vs 51% vs 28%) | VERIFIED | Full text PMC9256958 read. Note for the file's reader: the abstract's 2D fusion-index statement differs from the full-text 2D data (about 77 vs 69%, a slight difference); the dossier does not rely on that figure. [DOI](https://doi.org/10.3389/fbioe.2022.892287) |
| 31177802 | Prucha 2019: 4 mT rectangular, 340 us, 72 Hz; dB/dt ">= 12 T/s"; 5 kHz AM sinusoid mode no change | CORRECTED | 4 mT / 340 us = 11.76 T/s, so ">= 11.8 T/s" (not 12). Waveform findings match abstract. [DOI](https://doi.org/10.33549/physiolres.933998) |
| 42652114 | Leyva Martinez 2026: 28 studies, 1060 patients; EMTT > 60 kT/s effective in structural disease; < 5 mT often placebo-like; one 80 mT/3 Hz trial null in myofascial pain | VERIFIED | Abstract/full text (PMC13509872): 28 studies, 1060 participants; "EMTT > 60 kT/s"; "<5 mT ... indistinguishable from placebo or active controls"; the 80 mT, 3 Hz, 20 min x 8 pilot (Yau et al., chronic myofascial pain) found no significant difference from sham. "Patients" vs "participants" is trivial. [DOI](https://doi.org/10.3390/biomedicines14081731) |
| 17952798 | Brix 2008: static threshold about 500 mT; 587 mT gave -40% capillary RBC velocity; reversible | VERIFIED | [DOI](https://doi.org/10.1080/10739680701410850) |
| 25882659 | Kwan 2015: 13 DFU patients, 12 G = 1.2 mT, 12 Hz, 60 min x 14 sessions; wound size -18% vs -10%; capillary velocity +28%, diameter +14% | VERIFIED | Calc 0.09 T/s. Pulse width 40 ms from review (secondary). [DOI](https://doi.org/10.1097/01.ASW.0000462012.58911.53) |
| 26045885 | Li 2015: 5 mT, 30 +/- 3 Hz, 4 x 8 min/day, 14 d; neovascularisation up, PI3K/eNOS inhibitors block | VERIFIED | Calc 0.94 T/s (sinusoid assumption flagged by file). Same protocol as Hao 2014 (24936220), correctly flagged as non-independent. DOI not returned by PubMed. |

## 3. Recomputed dB/dt and E values (all "computed by me" entries)

Cluster 3

| PMID | File value | Recompute | Status |
|---|---|---|---|
| 17516509 Tsai | dB/dt >= 0.43, 0.8, 1.07 T/s | 0.43, 0.80, 1.07 | VERIFIED |
| 17516509 Tsai | E_rms 1.5-7.6 uV/cm (r = 1.5-3 cm) | 32-160 uV/cm peak by stated formula; 1.5-7.6 only with unstated sqrt(duty) = 0.0474 | CORRECTED |
| 25661534 Yan; 41152178 An | 0.19 T/s (0.6 mT, 50 Hz) | 0.188 | VERIFIED |
| 29658660 Zhu | 0.57 T/s (1.8 mT, 50 Hz) | 0.565 | VERIFIED |
| 7639117 Fitzsimmons | B_ac about 14 uT | 13.9 uT | VERIFIED |
| 12483712 Torricelli | 1.8 T/s; E_pk 13 mV/m at r = 1.5 cm | 1.77 T/s; 13.3 mV/m | VERIFIED |
| 11913771 De Mattei | about 1.8 T/s | 1.77 | VERIFIED |
| 25047554 Jing 2014 | 17-26 T/s; 0.17-0.26 V/m at r = 2 cm | 16.7-26.4 T/s; 0.167-0.264 V/m | VERIFIED (geometry guess flagged by file) |
| 10758655 Satter | 0.33 and 0.03 T/s | 0.333 and 0.033 | VERIFIED |
| 41152178 An | 0.19 T/s | 0.188 | VERIFIED |

Cluster 6

| PMID | File value | Recompute | Status |
|---|---|---|---|
| 18176216 Callaghan | >= 0.27 T/s | 0.267 | VERIFIED |
| 26045885 Li; 24936220 Hao | 0.94 T/s | 0.942 | VERIFIED |
| 31915323 Peng | 0.14 vs 0.57 T/s; "4x" | 0.141 vs 0.565; 4.0x | VERIFIED |
| 24244477 Delle Monache | 0.63 T/s | 0.628 | VERIFIED |
| 31177802 Prucha | >= 12 T/s | 11.76 T/s | CORRECTED (>= 11.8) |
| 28990042 Cheng | 0.71 T/s | 0.707 | VERIFIED |
| 33126773 Vincenzi | about 2 T/s; about 10 mV/m at r = 1 cm | 2.04 T/s; 10.2 mV/m | VERIFIED |
| 27227568 Sun | 0.038 T/s | 0.0377 | VERIFIED |
| 25882659 Kwan | 0.09 T/s | 0.0905 | VERIFIED |
| 16320175 Schuhfried | 0.019 and 0.53 T/s; 28-fold; 84-fold | 0.0188, 0.528; 28.0; 84.0 | VERIFIED |
| 20496180 McNamee | 0.075 T/s | 0.0754 | VERIFIED |
| 41897249 Alghadier | 0.19-1.57 T/s | 0.188-1.571 | VERIFIED |
| 24395219 Cheing | 0.79 T/s | 0.785 | VERIFIED |
| 18410412 Vianale | 0.31 T/s | 0.314 | VERIFIED |
| 41280646 Yang 2025 | 0.36 T/s | 0.360 | VERIFIED |
| 35616355 He 2022 | 0.19 T/s | 0.188 | VERIFIED |
| 31408675 Demirkazik | 1.57 T/s | 1.571 | VERIFIED |
| Section 2.4 | IGEA induced E about 0.01 V/m at r = 1 cm | 0.0102 V/m | VERIFIED |
| Section 2.10 | sinusoid-equivalent range about 0.04 to 0.94 T/s | 0.038 to 0.942 | VERIFIED |
| Section 4 | E = 0.005 x r[cm] x dB/dt | (r/2) dB/dt with r in m: 0.005 x r[cm] | VERIFIED |

## 4. Other discrepancies and unverifiable items (non-priority)

| PMID | Claim | Status | Notes |
|---|---|---|---|
| 10941887 Jenis 2000 | "not blinded for DC" arm | UNVERIFIABLE | Abstract gives three arms (PEMF 22, DC 17, control 22) and null at 1 year; blinding detail not in abstract. |
| 39534390 Ko 2024 | 10 min "twice weekly" for 8 weeks | UNVERIFIABLE | Abstract gives p = .527 and null result; dosing frequency wording not confirmed. |
| 36377077 / 36854553 | Combined as "Xu 2022/2023" | CORRECTED | See Section 1; two separate papers. |
| 30996361 Ren 2019; 35355482 He 2022 | 0.6 mT, 50 Hz; PI3K peak at 0.5 h; polycystin-2 required | VERIFIED | Re-fetched. Ren: PI3K highest at 0.5 h then falls; AKT higher at 0.5 and 1.5 h; He: AMI and RNAi abolish effect. DOIs 10.19723/j.issn.1671-167X.2019.02.008 and 10.13345/j.cjb.210356 correct. Exposure duration for He 2022 is not in the abstract (file says so). |
| 33261301 Marmotti | 1.5 mT, 75 Hz, 8 h/day up to 21 d (cluster 3) vs 7-21 d (cluster 6) | VERIFIED (minor inconsistency) | The two files give slightly different durations ("up to 21 days" vs "7-21 d"); abstract supports up to 21 days. |
| 22993248, 22668623, 23481041, 9096843, 25683910 | direct E-field / electrode studies | VERIFIED | File correctly labels them as not magnetic-induction thresholds. |

## 5. Error rate

- PMID/bibliographic: 0 WRONG PMID of about 145 checked.
- Priority quantitative/interpretive claims (30): 6 CORRECTED (Tsai E_rms, Xu ordering/merge, Wu 2018 "non-monotonic", Prucha 11.8 T/s, Cleary "4-fold", Bragin 3 h duration), 1 UNVERIFIABLE (Wang 2019 30 G) = 20% corrected, 3% unverifiable.
- Computed values (about 45): 2 incorrect (Tsai E_rms; Prucha >=12 rounding) = about 4%.
- Direction of errors: mostly over-interpretation of abstracts rather than wrong numbers; only Tsai E_rms is a real calculation inconsistency, and it supports a conclusion in cluster 3 Section 2.1 (that Tsai's active E overlaps Chang's 3-12 uV/cm), which should be marked low-confidence.
