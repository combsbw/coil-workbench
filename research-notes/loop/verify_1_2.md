# Independent verification of cluster 1 (Ca/NOS) and cluster 2 (adenosine/inflammation) dossiers

Method: every PMID in the key-reference lists, in the study tables and in the synthesis sections was pulled with PubMed get_article_metadata and checked for first author, year, journal and title. Numbers were checked against the abstract, or against PMC full text where I could fetch it (PMC4568470 Petecchia: full text read; PMC1762120 Varani 2002: full text returned empty). All "computed by me" values were recomputed in Python (E = r/2 * dB/dt; dB/dt_pk = 2*pi*f*B_pk; f_c = qB/(2*pi*m) with m = 40.078 u).

Status key: VERIFIED / CORRECTED / UNVERIFIABLE (abstract lacks the number) / WRONG PMID. No PMID in either file points to the wrong paper (0 WRONG PMID). Three citation-metadata errors and several wording/interpretation errors are listed under CORRECTED.

## A. Everything flagged CORRECTED or UNVERIFIABLE (read this first)

| PMID | File | Claim in file | Status | Correction / notes |
|---|---|---|---|---|
| 32998161 | C2 | "Vinhas 2020, PLoS One" (tendon cells, A2A) | CORRECTED (citation) | First author is Colombini (Colombini A et al.), PLoS One 2020, "A2A adenosine receptors are involved in the reparative response of tendon cells to PEMFs". Vinhas is first author of the different paper 32751697 (Int J Mol Sci). PMID, journal, year are right. |
| 28255202 | C2 | "Varani 2017, Biomed Res Int" | CORRECTED (citation) | Journal is Mediators Inflamm 2017 (DOI 10.1155/2017/2740963). |
| 24352823 | C2 | "Paolo 2013 (TKA)" | CORRECTED (citation) | "Paolo" is the given name; first author surname is Adravanti (Int Orthop 2013). |
| 36377077 | C2 | "75 Hz > 45 Hz > 15 Hz" (table, 2.3, section 3) | CORRECTED | Abstract only says the 75 Hz PEMF-exposed exosomes had a more significant inhibitive effect than 15 Hz and 45 Hz. No ordering of 45 vs 15 Hz is given. Safe wording: "75 Hz best of 15/45/75 Hz at 1 mT". PEMF was applied to donor AMSCs, not to the chondrocytes. |
| 34821733 | C2 | "differing only in send-pause pulse grouping"; "blinded screen of 22 found only two with diverging effects" | CORRECTED | Abstract: fields A and B have "similar fundamental frequencies (51.8 and 52.3 Hz) but are emitted in different groups of pulses or send-pause intervals". "Only" is an inference (52.3 vs 51.8 Hz also differ). The abstract says two fields were "further characterized as they diversely affected macrophage function", not that only two diverged. |
| 21448989 | C2 | Section 0: "1.5 mT peak (2.5 mT for osteoblasts)"; section 2.3 and table call the Lin 2011 signal "the Ferrara signal" | CORRECTED | Lin 2011 exposed 7F2 osteoblasts at 1.5 mT (75 Hz, 1.3 ms, induced voltage 2.5 mV, 9 h). It is not a Ferrara-group paper (affiliation not in the record; only the parameter set matches). The "2.5 mT for osteoblasts" statement is not supported by this abstract and is UNVERIFIABLE for Vincenzi 2013 (23741498; abstract gives no B). |
| 2988718 | C1 | Farndale 1985: "cAMP lowered" (table 1E) and synthesis 2.4 "lowered cAMP in marrow fibroblasts" | CORRECTED | cAMP was not measured. The abstract says collagen production rose, cell proliferation was unchanged, temperature rise < 0.1 C, and "We propose ... PEMFs act by reducing cAMP levels" (hypothesis based on dibutyryl-cAMP and PGE2 add-back). |
| 16528477 | C1 | Ghibelli 2006 used as a "static field (dB/dt = 0)" example in 2.1(a) and section 3 item 3 ("Ghibelli 1 T") | CORRECTED | Abstract: NMR apparatuses "use combinations of microwaves over a homogeneous strong (1 Tesla) static magnetic field". The exposure is NMR (static plus RF), so dB/dt is not zero. The table row (1 T static plus RF) is right; the synthesis use is not. Fanelli 1999 (9872934) is the genuine static example. |
| 37408527 | C1 | "kV/m, ns" pulses | CORRECTED (minor) | Abstract: 30,000 pulses, 237 kV/m, 280 ps rise time, 500 ps duration (title says "nanosecond"). Conclusion (mostly no effect on transcripts; APX-1/6 up) matches. |
| 1468568 | C1 | Synthesis 2.1: thymocyte 45Ca influx "positive ... at 3 Hz pulsed 6.5 mT" | CORRECTED (wording) | Walleczek 6.5 mT reduced ConA-induced 45Ca uptake by 45% (inhibition). "Positive" can only mean "effect present". Table row is correct. |
| 6812594 | C1 | Adey 1982 "p = 0.96 confidence" (2.6) | CORRECTED (wording) | 0.96 is the confidence level of the binomial analysis (about p = 0.04), not a p value. |
| 11976268 | C2 | Varani 2002: lowest amplitudes smaller/n.s., "apparent threshold ~0.5-1 mT", "plateau ~1.5-3.5 mT", derived "0.7-1.4 T/s" threshold dB/dt | UNVERIFIABLE | Abstract says only "intensity, time and temperature dependent". PMC full text fetched but empty. File itself flags "not verified against the table". The 0.7-1.4 T/s figure is arithmetic on an unverified 0.5-1 mT. |
| 21448989 / 26364969 | C2 | IGEA induced voltage "2.0+/-0.5 mV in a 50-turn, 0.5 cm-ID probe" giving 2.04 T/s | UNVERIFIABLE (inputs) | Arithmetic is right (see section D) but the probe geometry and 2.0 mV come from "earlier reading", not from any record I could check. Lin 2011 reports 2.5 mV with no geometry; Petecchia 2015 reports 5+/-1 mV at 2 mT with a different set-up. 5 mV at 2 mT vs 2-2.5 mV at 1.5 mT is not a consistent scaling, so cross-paper "induced voltage" values cannot be treated as the same probe. |
| 23802593 | C1 | Pall 2013 table "has no exposure values" | UNVERIFIABLE | Abstract confirms 23 studies and the VGCC-blocker claim; table content not checked. |
| 26705327 | C2 | Bagnato: 27.12 MHz, 1000 Hz pulse rate, 100 us burst, ~0.0098 W peak (from file's own full-text read) | UNVERIFIABLE | Not in abstract; no PMC record returned. Year: PubMed record dated 2015 (epub), journal volume 2016; file's "2016" is the print year. |
| 20527063 | C2 | Rohde 2010: pain "~3-fold lower at 5 h" | VERIFIED with caveat | Abstract says "a 300 percent decrease at 5 hours", which is not arithmetically a decrease; "about 3-fold lower" is an interpretation. |
| 15 PMIDs | both | "group standard" parameters (1.3 ms, 75 Hz, 1.5/2.5 mT) attributed to Varani 2002, Vincenzi 2013, Merighi 2019, Ongaro 2012 etc. | UNVERIFIABLE | Abstracts do not give parameters; the file marks these "not stated in abstract". Merighi 2024 (39684558) and Ouyang 2020 do state 1.3 ms/75 Hz and 1.5 mT/75 Hz/10% duty (VERIFIED). |
| not in synthesis | C2 | Section 3 item 4: Physio-Stim "~10 T/s" | UNVERIFIABLE | File says "from my earlier reading, not recomputed". |

## B. The 15 most important quantitative claims per file

### Cluster 1

| PMID | Claim | Status | Notes |
|---|---|---|---|
| 1333413 | 22 mT, 60 Hz, E induced 1.7 mV/cm, 37 C, 60 min; response follows induced E at constant B; pure E field gives similar change | VERIFIED | Abstract matches. |
| 1333413 | (computed) dB/dt = 8.29 T/s; E = 1.7 mV/cm implies ring radius 4.1 cm | VERIFIED | 2*pi*60*0.022 = 8.294 T/s; r = 2*0.17/8.294 = 4.10 cm. Assumes 22 mT is peak (abstract does not say). |
| 1468568 | 3 Hz monopolar quasi-rectangular pulses, Bpeak 6.5 mT, Emax 0.69 mV/cm, Jmax 2.6 uA/cm2, ConA-induced 45Ca uptake -45%, B series 0/1.6/6.5/28 mT, 30 min | VERIFIED | Computed E 0.17 and 3.0 mV/cm at 1.6 and 28 mT by proportional scaling: 0.69*1.6/6.5 = 0.170; 0.69*28/6.5 = 2.97. Arithmetic right; proportionality is the file's stated assumption. |
| 7748202 | Jurkat; no effect below 0.04 mT, plateau 0.15 mT at 50 Hz; 5-100 Hz tested at 0.15 mT; broad peak 50 Hz | VERIFIED | (computed) 0.0126 and 0.0471 T/s; E = 0.24 mV/m for 1 cm radius (r/2 = 0.5 cm * 0.0471 T/s = 0.236 mV/m). All correct if peak sine. |
| 10656853 | 1.5 G, 50 Hz, 8 min; transients 16.5% MF, 14.6% sham, 14.2% none; Lindstrom 92% response | VERIFIED | |
| 9261541 | 0.15 mT rms, 60 Hz, 78.2 uT DC, Jurkat E6-1, Fluo-3 flow cytometry, null | VERIFIED | (computed) 0.08 T/s: 2*pi*60*0.2121e-3 = 0.0800. |
| 1733766 | 16 Hz, 42.1 uT AC + 23.4 uT DC (ratio 1.8), 60 min, 37 C; neither alone effective; resting cells do not respond | VERIFIED | (computed) f_c(Ca2+) = 0.766 Hz/uT -> 17.93 Hz at 23.4 uT, 38.3 Hz at 50 uT. Correct. |
| 2540755 | Enhanced efflux at 1.75, 3.85, 5.57, 6.82, 7.65, 7.77, 8.82 mW/cm2; none at 0.75, 2.30, 4.50, 5.85, 7.08, 8.19, 8.66, 10.6, 14.7; SAR <= 0.005 W/kg; 50 MHz AM 16 Hz, 20 min | VERIFIED | 7 enhanced and 9 null counts in 2.5 are correct. |
| 9915588 | 2.97 uT DC, 45 Hz = H+ resonance, 42.5/47.5 near, 40/50 off, +/-10% bandwidth, repeated 3 times | VERIFIED | |
| 1064869 | 1, 6, 16, 32, 75 Hz; 5/10/56/100 V/m in air; 20 min; efflux -12 to 15% max at 6 and 16 Hz; thresholds ~10 (chick), 56 V/m (cat); tissue gradient ~0.1 uV/cm | VERIFIED | Ratio to 0.69 mV/cm is about 7000x, "orders of magnitude" holds. |
| 26364969 | 2+/-0.2 mT, 5+/-1 mV, 75+/-2 Hz, 1.3 ms, 10 min/day up to 27 days; [Ca]i +30% at day 9; L-type cells 40% -> 100%; Ca current 199 vs 70 pA at day 9 | VERIFIED (full text) | Also: file says mineral deposition "reduced by PEMF": full text says fewer deposits in ODM+/PEMF+, but the abstract says extracellular deposition was "unaffected" (internal inconsistency in the paper, file follows the full text). Computed 1.5 T/s = 2 mT/1.3 ms = 1.54 (crude, correct). |
| 31915323 | 15 Hz/1.5 mT vs 30 Hz/3.0 mT, 45 min/day, 2 weeks; both raise p-eNOS S1177; only 30 Hz/3.0 mT improves function | VERIFIED | Computed 2x (fixed pulse width) vs 4x (waveform scales with period) dB/dt ratios: correct. |
| 25343187 | Arteriole 26.4 -> 29.1 um (p<0.01); RBC velocity +5.5%; NADH 94.7%; L-NAME 10 mg/kg blocks; n = 11/7/5 | VERIFIED | +10.2% in synthesis is correct (29.1/26.4). |
| 2988718 | Farndale 1985: "cAMP lowered" | CORRECTED | See section A. |
| 16528477 | Ghibelli 2006: 1.8-2.5-fold apoptosis; "static 1 T" | CORRECTED | 1.8-2.5-fold is right; static classification is wrong, see section A. |

### Cluster 2

| PMID | Claim | Status | Notes |
|---|---|---|---|
| 11976268 | A2A Bmax 126+/-10 -> 215+/-15 fmol/mg (P<0.01), Kd 1.05 vs 1.08 nM, HE-NECA cAMP EC50 43 -> 10 nM, O2- EC50 3.6 -> 1.6 nM, 1 h | VERIFIED | |
| 11976268 | Intensity threshold ~0.5-1 mT, plateau 1.5-3.5 mT | UNVERIFIABLE | Full text empty. |
| 22012856 | 1.5 mT: 2.0-fold at 4 h, 1.4-fold at 6 h (tissue); 3 mT: 2.0-fold at 2 h, 1.6-fold at 4 h; membranes 1.9 and 2.2-fold at 2 h; A1/A2A mRNA unchanged | VERIFIED | Abstract gives cortex and neurons as paired values (e.g. 6 h: 1.4 and 1.8; 3 mT 2 h: 2.0 and 2.2); file reports the tissue value. |
| 32596310 | Mouse DMM/air pouch, 1.5 mT, 75 Hz, 10% duty | VERIFIED | (computed) ~2 T/s is the file's IGEA-shape assumption. |
| 34994274 | 3.82 mT, 8 Hz, 40 min/day, 5 d/wk, 12 wk, n = 6/group; computed 0.19 T/s, E 0.96 mV/m at r = 1 cm | VERIFIED | 2*pi*8*3.82e-3 = 0.192; 0.005*0.192 = 0.96 mV/m. |
| 28370033 | 60 Hz, 0.8 mT RAW 264.7: NO, TNF-a, IL-1b, IL-6, NF-kB, NFAT2, Ca influx up; computed 0.30 T/s, 1.5 mV/m | VERIFIED | 0.3016; 1.51 mV/m. |
| 36377077 | 1 mT; 15/45/75 Hz; computed 0.47 T/s (75 Hz) and 0.094 T/s (15 Hz) | CORRECTED | Numbers correct; "75 > 45 > 15" ordering not supported. |
| 34821733 | Fundamentals 51.8 and 52.3 Hz; blinded screen of 22 | CORRECTED | See section A (frequencies and 22 are right). |
| 28741320 | 15 Hz, 2 h/day, 7 d, 0.5/1/2/3 mT; 0.5 mT inhibits resorption, 3 mT enhances through apoptosis | VERIFIED | |
| 31408675 | 72 rats; 50 Hz 5 mT; 4 x 30 min with 15 min gaps; 15 days; peak day 7; L-NAME no difference; computed 1.57 T/s, 7.9 mV/m | VERIFIED | 1.5708 T/s; 7.85 mV/m. |
| 21381048 | 25-500 nT peak, 10-240 Hz, 1 h daily, ~100x shielding, threshold at or below 1000 nT-Hz; computed 6.3 uT/s and 3e-8 V/m | VERIFIED | 2*pi*1e-6 = 6.28e-6 T/s; 0.005 m * that = 3.14e-8 V/m. |
| 25199571 | Q4 20 min/4 h, Q2 15 min/2 h, 5/20; 24 h VAS 43% and 35% of 1 h; 5/20 87% vs 74% Q4 sham, P = 0.451; narcotic 2-fold higher | VERIFIED | Abstract also says 5/20 increases NO 4-fold faster than Q4 (not in file; supports its hypothesis statement). |
| 20527063 | n = 24; -57% at 1 h; narcotic 2.2-fold; IL-1b 275% lower; TNF-a, VEGF, FGF-2 n.s. | VERIFIED | 5 h wording see section A. |
| 29950893 | 36 subjects; 42 us vs 38 us; low back -40.2/-18.6/-25.6%; leg -45.0/-17.0/-24.5%; 2x daily 60 d; between-group P > 0.05 | VERIFIED | |
| 21448989 | 1.5 mT, 2.5 mV, 75 Hz, 1.3 ms, 9 h; NO 65 vs 17 uM day 7; proliferation +23%, COL I 3.4-fold | VERIFIED (numbers) | Attribution/osteoblast-2.5-mT problem: see section A. |

### Other numeric claims checked (not in the top 15)

| PMID | Claim | Status |
|---|---|---|
| 26562074 | Wuschech: MAGCELL 4-12 Hz sine, 105 mT at 1 cm, n = 57, 2 x 5 min, 18 d; computed 2.6-7.9 T/s, 13-40 mV/m | VERIFIED (2.639, 7.917 T/s; 13.2, 39.6 mV/m) |
| 36514244 | Xiang protocol: 15 Hz, 30 mT, 40 min/day, 5 d/wk, 6 wk, n = 428; computed 2.8 T/s | VERIFIED (2.827 T/s) |
| 24338431 | Cochrane: 9 RCTs, 636; pain MD 15.10 (9.08-21.13); function MD 4.55 (-2.23 to 11.32) n.s.; QoL SMD 0.09 n.s. | VERIFIED ("low-moderate certainty" not in abstract) |
| 15979009, 20473540, 11900312 | n = 83 / 40 / 75 (69 analysed); nulls between groups; p = 0.906/0.855/0.809 | VERIFIED |
| 25919263 | n = 32; pain 2-fold (5 h), 4-fold (72 h); IL-1b 5-fold (24 h); narcotic 2-fold | VERIFIED |
| 18506512 | n = 42, 80 breasts; ~3-fold faster VAS fall by POD 3, p < 0.001 | VERIFIED |
| 16770449 | RA n = 13, FM n = 18; <= 400 uT peak, < 3 kHz, 30 min; effect size 0.32 (RA, power 0.54), 0.52 (FM) | VERIFIED |
| 42652114 | 28 studies, 1060 participants; <5 mT; EMTT > 60 kT/s | VERIFIED |
| 28842627 | 2 mT, 6 ms bursts, 15 Hz, 10 min once | VERIFIED |
| 28173722 | 0.5-3.0 A/m, 2 Hz (field strength, not B) | VERIFIED |
| 36048344 | PEMF 4 h after ICH, 4 h/day x 7 d | VERIFIED |
| 31518158, 33644848 | 1.5 mT 10 min (Yap); 2 mT 10 min (Madanagopal); TRPC1; aminoglycosides block | VERIFIED |
| 16838272, 30312357, 29784011 | 2 mT/50 Hz; 0.4 mT/50 Hz; 1 mT at 7.5/15/30/50/70 Hz. Computed 0.63, 0.13, 0.047-0.44 T/s | VERIFIED (0.628, 0.126, 0.0471-0.4398; 9.3-fold span) |
| 35616355, 30350869, 30837038, 36680558 | 0.6 mT/50 Hz (0.19 T/s computed, verified 0.188); 50% duty 90 min/day; 3/6/9 d ALP; 20 G (= 2 mT)/15 Hz/6 wk | VERIFIED |
| 10453066 | Zhadin: 50 vs 500 uT DC, proportional AC; computed ~100x dB/dt | VERIFIED (2*pi*f*B scales with f*B = 10*10) |
| 9872934 | Fanelli: 6 G (0.6 mT) onset, plateau 6 mT | VERIFIED |
| 22005645, 10228567 | 10x lower peak amplitude, ~800x lower average amplitude, ~10^6x lower average power | VERIFIED |
| 22940137 | ~3-fold NO (MN9D, within seconds of LPS); ~2-fold in fibroblasts, 15 min, blocked by W-7 | VERIFIED |
| 6287472 | induced extracellular E <= 1 mV/cm; 15 Hz bursts, 72 Hz train | VERIFIED |

## C. Bibliographic check: every PMID (first author, year, journal, title)

Result: all PMIDs resolve to the paper the file describes. Citation-metadata errors: 32998161 (author), 28255202 (journal), 24352823 (author name format). Cosmetic year differences (epub vs print): 22451021 Nelson (2012 epub / 2013 print; C1 says 2013, C2 says 2012, both defensible), 26705327 Bagnato (2015 epub / 2016 print).

### Cluster 1 (all VERIFIED unless noted)
1333413 Liburdy 1992 FEBS Lett; 8243637 Liburdy 1993 FEBS Lett; 1468568 Walleczek 1992 FEBS Lett; 7748202 Lindstrom 1995 Bioelectromagnetics; 10656853 Wey 2000 Environ Health Perspect; 9261541 Lyle 1997 Bioelectromagnetics; 1733766 Yost 1992 FEBS Lett; 8451278 Coulton 1993 Phys Med Biol; 10723019 Coulton 2000 Bioelectromagnetics; 12483663 Liboff 2003 Bioelectromagnetics; 1064869 Bawin 1976 PNAS; 282648 Bawin 1978 PNAS; 6812594 Adey 1982 Bioelectromagnetics; 2540755 Blackman 1989 Bioelectromagnetics; 9915588 Blackman 1999 Bioelectromagnetics; 10453066 Zhadin 1999 Bioelectromagnetics; 10797457 Prato 2000 Bioelectromagnetics; 9795129 Kavaliers 1998 Brain Res; 30793837 Kavand 2019 J Tissue Eng Regen Med; 18288680 Vincze 2008 Bioelectromagnetics; 19437458 Muehsam 2009 Bioelectromagnetics; 22005645 Pilla 2011 BBA; 22940137 Pilla 2012 BBRC; 10228567 Pilla 1999 Bioelectrochem Bioenerg; 23675615 Pilla 2013 Electromagn Biol Med; 18240331 Fitzsimmons 2008 J Orthop Res; 16677936 Li 2006 Ultrasound Med Biol; 18506512 Heden 2008 Aesthetic Plast Surg; 20527063 Rohde 2010 Plast Reconstr Surg; 22451021 Nelson 2013 Rheumatol Int; 25199571 Taylor 2014 J Surg Res; 25343187 Bragin 2014 J Neurosurg; 31915323 Peng 2020 Circ J; 26045885 Li 2015 Am J Transl Res; 27780890 Ma 2016 Biosci Rep; 19799606 Patruno 2009 Br J Dermatol; 15208265 Tepper 2004 FASEB J; 17427956 Schnoke 2007 J Orthop Res; 16222888 Morimoto 2005 J Int Med Res; 20119972 Martino 2010 Bioelectromagnetics; 27430265 Nakayama 2016 Int J Radiat Biol; 35616355 He 2022 FASEB J; 30350869 Li 2018 Bioelectromagnetics; 30837038 Wang 2019 Zhongguo Yi Xue Ke Xue Yuan Xue Bao; 36680558 Hao 2023 J Bone Miner Res; 26364969 Petecchia 2015 Sci Rep; 31518158 Yap 2019 FASEB J; 33644848 Madanagopal 2021 Eur Cell Mater; 27856256 Zhang 2016 BBRC; 9699506 Shankar 1998 J Cell Physiol; 6287472 Luben 1982 PNAS; 2988718 Farndale 1985 Calcif Tissue Int; 30920672 Yang 2019 Bioelectromagnetics; 35129008 Ye 2022 Electromagn Biol Med; 16838272 Lisi 2006 Bioelectromagnetics; 30312357 Wu 2018 PLoS One; 29784011 Zhang 2018 Stem Cell Res Ther; 9872934 Fanelli 1999 FASEB J; 16528477 Ghibelli 2006 Apoptosis; 8045284 Karabakhtsian 1994 FEBS Lett; 8986359 Eichwald 1996 Bioelectromagnetics; 23802593 Pall 2013 J Cell Mol Med; 40713855 Chen 2025 Stem Cell Res Ther; 37408527 Porcher 2023 Bioelectromagnetics. Section 1G: 25879308 Pall 2015, 29573716 Pall 2018, 35114921 Pall 2022, 34043892 Pall 2021, 26300312 Pall 2015, 20707644 Liboff 2010, 19811395 Liboff 2009, 18097820 Liboff 2007, 31032646 Liboff 2019, 23323834 Foletti 2013, 19337897 Foletti 2009: all VERIFIED; the file's characterisation ("hundreds of studies", "non-monotone", ICR/0.05 uT/commercial device 7 Hz) matches the abstracts. Key-reference list items 1-18 and all 18 DOIs match.

### Cluster 2
11976268 Varani 2002 Br J Pharmacol; 22012856 Varani 2011 Bioelectromagnetics; 21830213 Ongaro 2012 J Cell Physiol; 23741498 Vincenzi 2013 PLoS One; 22761760 Vincenzi 2012 PLoS One; 27639248 Vincenzi 2016 J Cell Physiol; 32998161 CORRECTED (Colombini, not Vinhas); 28255202 CORRECTED (Mediators Inflamm); 37373237 Moretti 2023 Int J Mol Sci; 32596310 Ouyang 2020 Biomed Res Int; 39953605 Zhou 2025 Arthritis Res Ther; 34994274 Liu 2022 Electromagn Biol Med; 28173722 Zou 2017 J Int Med Res; 28370033 Kim 2017 Bioelectromagnetics; 21448989 Lin 2011 Bioelectromagnetics; 34821733 Chen 2021 Bioengineering; 32751697 Vinhas 2020 Int J Mol Sci; 31400640 Merighi 2019 Cytokine; 39684558 Merighi 2024 Int J Mol Sci; 36048344 Yang 2022 J Mol Neurosci; 36377077 Xu 2022 Cartilage; 28741320 Wang 2017 Bioelectromagnetics; 28842627 Parate 2017 Sci Rep; 40391205 Guarnaccia 2025 JOR Spine; 42549352 Sukumar 2026 Smart Med; 31408675 Demirkazik 2019 Nitric Oxide; 28836499 Ozdemir 2017 Gen Physiol Biophys; 21381048 Prato 2011 Bioelectromagnetics; 22940137 Pilla 2012 BBRC; 21968643 Shiiba 2011 Cell Mol Neurobiol; 24338431 Li 2013 Cochrane; 42075549 Chang 2026 Medicina; 30552258 Wu 2018 BMJ Open; 35586276 Tong 2022 Pain Res Manag; 42652114 Leyva Martinez 2026 Biomedicines; 15979009 Thamsborg 2005 Osteoarthritis Cartilage; 20473540 Ozguclu 2010 Clin Rheumatol; 11900312 Pipitone 2001 Curr Med Res Opin; 26705327 Bagnato 2015 (epub)/2016 Rheumatology; 26562074 Wuschech 2015 Bioelectromagnetics; 41588476 Lau 2026 J Cachexia Sarcopenia Muscle; 36514244 Xiang 2022 BMJ Open (protocol, correctly labelled); 20527063 Rohde 2010; 25919263 Rohde 2015 Plast Reconstr Surg; 18506512 Heden 2008; 25199571 Taylor 2014; 29950893 Sorrell 2018 J Pain Res; 16770449 Shupak 2006 Pain Res Manag; 34872332 Li 2021 Bone Joint Res; 35834942 Wang 2022 Am J Sports Med. "Not extracted but retrieved": 26957530 Svaerdborg 2016 (abstract not available, confirmed), 24352823 (Adravanti), 30868475 Lisi 2019, 30177406 Elshiwi 2018, 31575112 Alzayed 2019, 41745713 Lara-Reyes 2026, 38102884 Dana 2023, 39985539 Ilfeld 2025, 36239249 Figueroa 2022, 22451021 Nelson: all resolve correctly. All 15 key-reference DOIs and all "also cited" DOIs match the records.

## D. Recomputation of every "computed by me" dB/dt and E value

All arithmetic was recomputed; no arithmetic errors found in either file. Items below are the arithmetic status only (assumptions about waveform/peak and geometry are flagged in section A where they matter).

| Source | Quantity | File | Recomputed | Status |
|---|---|---|---|---|
| Liburdy 22 mT, 60 Hz | dB/dt | 8.29 T/s | 8.294 | OK |
| Liburdy E 1.7 mV/cm | loop radius | 4.1 cm | 4.10 cm | OK |
| Lindstrom 0.04/0.15 mT, 50 Hz | dB/dt | 0.013/0.047 T/s | 0.0126/0.0471 | OK |
| Lindstrom 0.15 mT | E | ~0.24 mV/m per cm of radius (1 cm loop) | 0.236 mV/m at r = 1 cm | OK |
| Lyle 0.15 mT rms 60 Hz | dB/dt peak | ~0.08 T/s | 0.0800 | OK |
| Walleczek E scaling | 1.6 and 28 mT | 0.17 and 3.0 mV/cm | 0.170 and 2.97 | OK (assumes proportionality) |
| Ca2+ f_c | per uT; at 23.4 uT; at 50 uT | 0.766; 17.9; 38 Hz | 0.7663; 17.93; 38.3 | OK |
| Petecchia crude | 2 mT / 1.3 ms | ~1.5 T/s | 1.54 | OK (crude, as labelled) |
| Lisi / Wu / He | 2 / 0.4 / 0.6 mT at 50 Hz | 0.63 / 0.13 / 0.19 T/s | 0.628 / 0.126 / 0.188 | OK |
| Zhang 2018 | 1 mT, 7.5-70 Hz | 0.047-0.44 T/s, 9-fold | 0.0471-0.4398; 9.33 | OK |
| Zhadin | f and B both x10 | ~100x dB/dt | 100 | OK |
| Peng 2020 | 15 Hz/1.5 mT vs 30 Hz/3 mT | 2x or 4x | 2x (fixed width), 4x (period-scaled) | OK |
| Lindstrom vs Liburdy | ratio | "two to three orders" | 176x to 640x | OK |
| IGEA probe | 2.0 mV / (50 turns * pi*(0.25 cm)^2) | 2.04 T/s; 1.5-2.5 T/s for 1.5-2.5 mV | 2.037; 1.53-2.55 | OK arithmetic; inputs UNVERIFIABLE |
| IGEA rise time | 1.5 mT / 2.04 T/s | 0.74 ms | 0.736 ms | OK |
| IGEA E at r = 0.5/1/2/3.5/5 cm | (r/2)*2.04 | 5.1/10.2/20.4/35.7/51 mV/m | 5.09/10.19/20.37/35.65/50.93 | OK |
| IGEA scaled | 0.5/3/2.5 mT | 0.7/4.1/3.4 T/s | 0.68/4.07/3.40 | OK |
| Section 2.1 threshold | 0.5-1 mT | 0.7-1.4 T/s | 0.68-1.36 | OK arithmetic |
| Liu 2022 | 3.82 mT, 8 Hz | 0.19 T/s, 0.96 mV/m | 0.192; 0.960 | OK |
| Kim 2017 | 0.8 mT, 60 Hz | 0.30 T/s, 1.5 mV/m | 0.302; 1.51 | OK |
| Demirkazik | 5 mT, 50 Hz | 1.57 T/s, 7.9 mV/m | 1.571; 7.85 | OK |
| Prato 2011 | 1000 nT-Hz | 6.3 uT/s, 3e-8 V/m | 6.28e-6; 3.14e-8 | OK |
| Xu 2022 | 1 mT, 75 and 15 Hz | 0.47 and 0.094 T/s | 0.471 and 0.0942 | OK |
| Wuschech | 105 mT, 4 and 12 Hz; E at 1 cm | 2.6/7.9 T/s; 13-40 mV/m | 2.639/7.917; 13.2-39.6 | OK |
| Xiang | 30 mT, 15 Hz | 2.8 T/s | 2.827 | OK |
| Ouyang | ~2 T/s | assumption (IGEA shape) | not recomputable | assumption flagged by file |
| IGEA duty | 1.3 ms * 75 Hz | ~10% | 9.75% | OK |

## E. Error rate

- PMIDs/records checked: about 150 (C1 about 84 including section 1G; C2 about 66 including the "not extracted" list). Wrong PMID: 0. Citation-metadata errors: 3 (about 2%).
- Quantitative/interpretive claims audited: about 70 (30 designated top-15 per file plus extras). CORRECTED: 7 (Xu ordering, Chen "only", Lin 2.5 mT/attribution, Farndale cAMP, Ghibelli static, Porcher ps/ns, Walleczek wording) plus one wording slip (Adey 0.96). UNVERIFIABLE: 5 distinct items (Varani 2002 thresholds, IGEA probe inputs, Pall table, Bagnato RF parameters, Physio-Stim 10 T/s). Arithmetic errors: 0.
- Overall: roughly 11 corrections in about 220 checks (about 5%), none of which changes a headline conclusion; the highest-impact fixes are the Xu 2022 frequency ordering (used as evidence for frequency dependence in C2 sections 2.3 and 3), the Farndale cAMP claim, and the Ghibelli "static" classification (used to argue a non-induction route in C1).
