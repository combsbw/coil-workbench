# -*- coding: utf-8 -*-
import json, math, sys, csv
sys.path.insert(0, "/tmp/claude-0/-home-claude-coil-workbench/be52d8fd-6910-5673-a281-429468ab8431/scratchpad")
from refs_data import REFS

PI2 = 2 * math.pi

def sd(f, b_T):            # sine dB/dt peak, T/s
    return float("%.3g" % (PI2 * f * b_T))

def ee(r_m, dbdt):         # E ~ (r/2) dB/dt, V/m
    return float("%.3g" % (r_m / 2.0 * dbdt))

def T(role, endpoint, prep, et, pmid, src="abstract_only", B=None, Bnote="", f=None, wf="", pw=None,
      burst="", exp="", sched="", dbdt=None, dbasis=None, E=None, Ebasis=None, Egeo="", B0=None,
      refkey=None, note=""):
    return {"role": role, "endpoint": endpoint, "preparation": prep, "evidence_type": et,
            "B_pk_mT": B, "B_note": Bnote, "freq_Hz": f, "waveform": wf, "pulse_width_ms": pw,
            "burst": burst, "exposure": exp, "schedule": sched,
            "dBdt_T_s": dbdt, "dBdt_basis": dbasis, "E_V_m": E, "E_basis": Ebasis, "E_geometry": Egeo,
            "static_B0_uT": B0, "pmid": pmid, "refkey": refkey, "source_depth": src, "note": note}

def D(pmid, design, finding, refkey=None):
    return {"pmid": pmid, "refkey": refkey, "design_feature": design, "finding": finding}

def G(id_, name, level, modalities, driver, expl, ev, th, window, rep, conf, cav):
    return {"id": id_, "name": name, "level": level, "modalities": modalities, "driver": driver,
            "driver_explanation": expl, "discriminating_evidence": ev, "thresholds": th,
            "window_summary": window, "replication_status": rep, "confidence": conf, "caveats": cav}

SQ2 = math.sqrt(2.0)
targets = []

# ---------------------------------------------------------------- 1
b1 = 10e-6 * SQ2
d1a = sd(7e6, b1); d1b = sd(10e6, b1)
targets.append(G(
 "rp_flavin_ros_static_plus_rf",
 "Radical-pair (flavin/superoxide) ROS partitioning by weak static field plus RF/Zeeman-resonant field",
 "biochemical",
 ["wound/inflammation resolution", "vascular/angiogenesis"],
 "B_AC_over_B0",
 "In the NIST/Nevada/Montana line of work the response needs a static field of about 45 uT AND an oscillating field of about 10 uT rms at 5-10 MHz oriented perpendicular to it; the response depends on orientation and on the RF being near the Zeeman/hyperfine condition, i.e. on the ratio and geometry of B_AC to B0, not on RF induction. For scale, the RF dB/dt is very large (computed 6e2-9e2 T/s peak) yet the cell-scale induced E is only mV/m (computed, r=10 um assumed), so induction is not a plausible driver in these designs, and therapeutic PEMF (kHz-range, mT) does not match the RF/Zeeman conditions. Theory papers (Kattnig 2016; Brocklehurst 1996) argue spin relaxation and radical lifetime limit such effects, and the extension to broadband pulsed fields is speculative.",
 [
  D("24681944", "Static 45 uT plus 7 MHz RF at 10 uT rms vs static-only control (rat PASMC)", "Superoxide fell and H2O2 rose only with the combined static+RF exposure; sham used only for DC (abstract + partial full text)."),
  D("25251337", "Static 45 uT vertical, RF 5 or 10 MHz at 10 uT rms perpendicular to static, vs static-only controls (HT1080)", "10 MHz plus static cut cell number up to 30% (day 2) and raised H2O2 55% at 8 h versus static-only controls; 5 MHz also tested."),
  D("27995996", "RF at Zeeman resonance, varied field orientation (HUVEC)", "ROS partitioning and bioenergetics changed with oscillating-field orientation, as expected for coherent singlet-triplet mixing and not for induced currents."),
  D("15141211", "7 MHz field applied at 0, 24 and 48 degrees to the geomagnetic field (robins)", "Orientation was normal when the RF was parallel to the geomagnetic field and lost at 24 and 48 degrees, so the effect depends on angle between B_AC and B0 (resonance-like), not on RF amplitude alone."),
  D("27020113", "Spin-relaxation simulation, Arabidopsis cryptochrome-1", "Radical-pair lifetimes near microseconds are optimal and relaxation is too fast for the long coherence needed to explain RF disruption; counter-evidence from theory."),
  D("8601753", "Radical-pair theory of environmental-strength fields", "Low-field effects depend on radical lifetime and chemistry; freely diffusing radical pairs unlikely to give significant biological effects."),
 ],
 [
  T("lowest_effective", "Lower superoxide / higher H2O2 (ROS partitioning)", "Rat pulmonary arterial smooth muscle cells, in vitro", "invitro", "24681944",
    B=round(b1 * 1e3, 5), Bnote="Reported 10 uT rms; peak = rms x sqrt(2), computed.", f=7e6, wf="sine RF, perpendicular to static field",
    exp="not stated in abstract", dbdt=d1a, dbasis="computed", E=ee(10e-6, d1a), Ebasis="computed",
    Egeo="Single-cell scale, assumed r = 10 um (my assumption, not from paper); dish-scale E not computed", B0=45,
    note="dB/dt = 2*pi*7e6*1.414e-5. Only one RF amplitude (10 uT rms) reported in the abstract, so no dose-response and no lowest-effective level can be inferred."),
  T("lowest_effective", "Reduced proliferation (up to 30% fewer cells) and +55% H2O2", "HT1080 fibrosarcoma cells, in vitro", "invitro", "25251337",
    B=round(b1 * 1e3, 5), Bnote="Reported 10 uT rms; peak computed.", f=1e7, wf="sine RF perpendicular to 45 uT static",
    exp="8 h for H2O2 (+55%); cell number measured through day 2", dbdt=d1b, dbasis="computed", E=ee(10e-6, d1b), Ebasis="computed",
    Egeo="Single-cell scale, assumed r = 10 um (my assumption)", B0=45,
    note="5 MHz was also tested; the abstract quotes the 30% reduction for 10 MHz only."),
  T("optimal", "Zeeman (Larmor) frequency of a free electron spin, g = 2", "Theory / my calculation", "theory", "",
    src="fulltext", Bnote="", f=float("%.3g" % (28.02e6 * 0.045 / 1e-3 * 1e-3)), wf="n/a", B0=45,
    note="Computed: gamma_e/2pi = 28.02 MHz per mT, so 1.26 MHz at 45 uT; 7 MHz corresponds to B0 = 0.25 mT, i.e. the 7 MHz RF in Usselman 2014 and Ritz 2004 is about 5x the free-electron Larmor frequency of the ~45 uT static field (hyperfine couplings, not the Larmor frequency alone, set the resonance in a radical pair). The brief's '~1.4 MHz/mT' appears to be a unit slip: it is about 1.4 MHz at 50 uT."),
 ],
 "Reported effective RF: about 10 uT rms (about 14 uT peak), 5-10 MHz, on a 45 uT static field, perpendicular geometry. Computed dB/dt about 4e2-9e2 T/s peak but cell-scale E only about mV/m. Requires B0; no amplitude dose-response available.",
 "single group (Martino/Usselman lineage); concept supported independently only in birds (Ritz 2004); unresolved physical objections",
 "low",
 "Only one RF amplitude in the abstracts; exposure durations not in abstract; plausibility is contested; none of this uses therapeutic PEMF waveforms. Existing library refs hore2016, barnes2015 and wang2017 cover RPM theory but were not re-read in this pass."));

# ---------------------------------------------------------------- 2
targets.append(G(
 "rp_mfe_mT_scale_flavin",
 "Radical-pair magnetic field effect at mT amplitudes (flavin photochemistry, cryptochrome)",
 "biochemical",
 ["neuro-modulation/neuroprotection"],
 "B_amplitude",
 "In vitro flavin/cell photochemistry shows a magnetic-field effect whose size depends on the instantaneous field amplitude B and saturates at a few mT to tens of mT (B1/2 = 18.0 mT in HeLa autofluorescence; effects at 100 mT in Drosophila neurons); the effect is a property of static or slowly varying B, not of dB/dt. Because radical-pair lifetimes are microseconds (Kattnig 2016) while PEMF pulse widths are hundreds of microseconds to ms, a PEMF peak field in the 1-50 mT range would act on a light-activated radical pair as a quasi-static field during each pulse (my inference, not tested for pulses in these papers). All these systems need photoexcitation, so relevance to non-illuminated deep tissue is uncertain.",
 [
  D("33397812", "Field sweep up to 25 mT, single-cell fluorescence kinetics (HeLa)", "Autofluorescence changed with static field, half-saturation 18.0 mT, saturation 3.7%; consistent with triplet-born radical pair."),
  D("29724094", "FAD photochemistry vs pH 2.3-8.0 in water", "Magnetic field effects persist at physiological pH at about 25% of the pH 2.3 sensitivity."),
  D("27798129", "100 mT applied with blue light, motoneuron electrophysiology with ectopic cryptochrome", "Depolarisation, input-resistance rise and firing were potentiated by the field only in combination with blue-light cryptochrome activation; single field strength tested."),
  D("18449197", "Model carotenoid-porphyrin-fullerene triad, 50 uT or less", "Radical-pair lifetime changed at geomagnetic-strength fields with anisotropy; proof of principle, not a biological readout."),
 ],
 [
  T("plateau", "Change in autofluorescence (flavin radical-pair magnetic field effect)", "HeLa cells, single-cell imaging", "invitro", "33397812",
    B=25, Bnote="Maximum field tested ('25 mT and less'); static field.", f=0, wf="static", exp="not stated in abstract",
    dbdt=0, dbasis="computed", note="B1/2 = 18.0 mT and saturation amplitude 3.7% reported (so the response is near saturation at 25 mT). dB/dt = 0 for a static field by definition."),
  T("optimal", "Potentiation of blue-light cryptochrome-dependent firing", "Drosophila larval motoneurons with ectopic cryptochrome", "animal", "27798129",
    B=100, Bnote="Single field strength tested ('100 mT'), so this is not a threshold.", f=0, wf="static", dbdt=0, dbasis="computed",
    note="Light is required."),
 ],
 "B-driven, saturating around 18-25 mT in HeLa flavin photochemistry (B1/2 = 18.0 mT); dB/dt = 0 in these static designs. Requires light for the radical pair; no data on pulsed mT fields here.",
 "independent groups (Tokyo, Manchester, Oxford model) but different systems; no tests with PEMF waveforms",
 "medium",
 "In vitro/illuminated systems; extrapolation to PEMF therapy is inferential. Giachello tested one field only."));

# ---------------------------------------------------------------- 3
fe_dbdt_50 = sd(50, 3e-4); fe_dbdt_3 = sd(3, 3e-4); fe_dbdt_3_90 = sd(3, 9e-5); fe_dbdt_3_1000 = sd(3, 1e-3)
targets.append(G(
 "cryptochrome_dependent_elf_pemf_responses",
 "Cryptochrome-dependent responses to ELF/pulsed fields (ROS, circadian, behaviour, plant growth)",
 "cellular",
 ["neuro-modulation/neuroprotection", "wound/inflammation resolution"],
 "B_amplitude",
 "The best discriminating design is Fedele 2014: in a shielded apparatus a 300 uT static field, 3 Hz and 50 Hz fields all produced the same circadian-period shortening in Drosophila, and 3 Hz was effective from 90 to 1000 uT; a static field has dB/dt = 0 (and 50 Hz at 300 uT would have about 17-fold larger dB/dt than 3 Hz, computed), so B amplitude, not dB/dt or induced E, is the operative variable there. Plant data (500 uT static) are likewise B-driven. Sherrard 2018 used a 10 Hz pulsed device of about 2 mT peak, cryptochrome knock-out and a mu-metal control; those controls prove field-dependence and cryptochrome-dependence but do not discriminate B from dB/dt, because shielding or an antiparallel coil removes both B and the induced E together. Lohof 2022 reports that low-intensity rTMS repair depends on the stimulation pattern and on cryptochrome (abstract only).",
 [
  D("25473952", "Static 300 uT vs 3 Hz vs 50 Hz in a shielded Schuderer apparatus with sham; 90, 300, 1000 uT at 3 Hz; CRY mutants; blue vs 500 nm light", "Static, 3 Hz and 50 Hz gave the same period effect (dB/dt differs from 0 to computed 0.094 T/s), so B, not dB/dt; effect is CRY- and blue-light-dependent; hyperactivity not significant at 1 mT; 500 nm light reversed the sign; mouse SCN slices showed no effect at 50-500 uT, 50 Hz."),
  D("30278045", "Cry1/2 knock-out/knock-down, DmCry expression, mu-metal (1 mm, field reduced about 85%), antiparallel-wound coil with same current", "ROS rose within 15 min in Cry-expressing cells and cells lacking Cry did not respond; mu-metal and antiparallel coil abolished it. Shielding and antiparallel coil remove B and induced E together, so B vs dB/dt/E is not resolved."),
  D("35023064", "LI-rTMS pattern comparison in cerebellum, Cry dependence", "Repair depended on stimulation pattern and Cry, not on induced-current excitation (abstract only)."),
  D("16955271", "Static 33-44 uT vs 500 uT, blue vs red light, cry mutants (Arabidopsis)", "500 uT enhanced blue-light, cryptochrome-dependent hypocotyl inhibition; no effect in the dark, under red light or in cry mutants."),
  D("30194534", "500 uT given only in dark intervals vs continuous", "Effect arises during flavin reoxidation in the dark."),
  D("32065192", "500 uT only during 5 min light vs only during 10 min dark", "Field applied only during light had no effect; dark-interval exposure was effective."),
  D("30278038", "Commentary", "Frames the Sherrard result as potentially linking animal magnetoreception, therapeutic PEMF and environmental-EMF concerns; calls for caution given field history."),
 ],
 [
  T("optimal", "Cry-dependent ROS rise, slowed growth, gene expression changes, larval avoidance", "HEK293 / Sf21-DmCry / MEF cells and Drosophila larvae, PEMF device GEM EC10701", "invitro", "30278045", src="fulltext",
    B=2.0, Bnote="Reported peak about 1.8-2 mT (coil 9 x 5.5 cm, 200 turns, dish 1 cm above coil); single amplitude, no dose-response.", f=10, wf="pulsed (device waveform; pulse about 0.5 ms)", pw=0.5,
    exp="ROS after 15 min; gene expression after 3 h; growth after 48 h", dbdt=4.0, dbasis="computed",
    note="dB/dt computed as B_pk/pulse width = 2 mT / 0.5 ms = 4 T/s, a LOWER bound because actual edges may be shorter. Authors state the device is not a therapeutic one. E not computed (coil/dish geometry not fully specified)."),
  T("lowest_effective", "Circadian period shortening (3 Hz)", "Drosophila melanogaster, shielded apparatus", "animal", "25473952", src="fulltext",
    B=0.09, Bnote="Reported 90 uT; amplitude not stated as rms or peak; treated here as nominal peak.", f=3, wf="sine", exp="circadian recording (days)",
    dbdt=sd(3, 9e-5), dbasis="computed", note="dB/dt = 2*pi*3*9e-5."),
  T("optimal", "Circadian period shortening and hyperactivity", "Drosophila melanogaster", "animal", "25473952", src="fulltext",
    B=0.3, Bnote="Reported 300 uT; rms/peak not stated; same effect for static, 3 Hz and 50 Hz.", f=0, wf="static (and 3 Hz, 50 Hz sine)", dbdt=0, dbasis="computed",
    note="For the static field dB/dt = 0 yet the effect is the same as 3 Hz (computed dB/dt %.3g T/s) and 50 Hz (computed %.3g T/s) at 300 uT: decisive for B over dB/dt in this assay." % (fe_dbdt_3, fe_dbdt_50)),
  T("loss_above", "Hyperactivity phenotype (not significant at 1 mT, 3 Hz)", "Drosophila melanogaster", "animal", "25473952", src="fulltext",
    B=1.0, Bnote="Reported 1000 uT, 3 Hz; period effect still seen.", f=3, wf="sine", dbdt=fe_dbdt_3_1000, dbasis="computed",
    note="Only the hyperactivity endpoint lost significance at 1 mT."),
  T("lowest_effective", "Enhanced cryptochrome-dependent hypocotyl inhibition, CRY2 degradation", "Arabidopsis seedlings", "invitro", "16955271",
    B=0.5, Bnote="Reported 500 uT vs ambient 33-44 uT; only this contrast tested, so not a true threshold.", f=0, wf="static", dbdt=0, dbasis="computed",
    note="Needs blue light; absent in cry mutants."),
 ],
 "Cryptochrome-dependent effects in Drosophila appear at 90-1000 uT regardless of frequency (0, 3 or 50 Hz), i.e. B-amplitude-driven (computed dB/dt from 0 to about 0.094 T/s). Pulsed ~2 mT peak fields (computed dB/dt >= 4 T/s) also act via Cry but B vs dB/dt was not separated.",
 "multiple independent groups (Leicester/Cambridge; Paris/Florida; Manchester) but each system single-lab; no independent replication of the Sherrard mammalian-cell ROS result found in this search (search not exhaustive)",
 "medium",
 "Light required (blue). Fedele reports the effect as hCRY2-, not Trp-triad-dependent, which complicates a classical RPM reading; mouse SCN slices were null. Amplitude rms/peak not given in Fedele. Mu-metal and antiparallel-coil controls do not discriminate B from E."));

# ---------------------------------------------------------------- 4 ICR / IPR
bl_lo = 7.7e-6 * SQ2; bl_hi = 46.8e-6 * SQ2
targets.append(G(
 "icr_ipr_ca_resonance",
 "Ion cyclotron / ion parametric resonance (Ca2+ and other ions) in combined static + AC fields",
 "membrane/ion channel",
 ["bone & cartilage repair", "neuro-modulation/neuroprotection", "pain relief"],
 "B_AC_over_B0",
 "The ICR/IPR hypothesis says the response depends on the AC frequency relative to f_c = qB0/(2*pi*m) and on the ratio B_AC/B0 (Lednev 1991; Blanchard & Blackman 1994), not on dB/dt or induced E. Supporting designs vary B0, f and B_AC independently and test orientation: PC-12 neurite outgrowth followed IPR predictions at 45 Hz/36.6 uT and 25 Hz/20.3 uT with an off-resonance control (Blackman 1994); chick brain Ca2+ efflux required B_dc perpendicular to B_ac at constant E (Blackman 1990); rat behaviour followed proportional DC and AC scaling at 50 and 500 uT (Zhadin 1999). Against it, several well-designed attempts found nothing (Parkinson 1989; Coulton 1993), one diatom study was irreproducible (Reese 1991), and physics critiques show classical cyclotron orbits cannot survive collisions (Sandweiss 1990: gyration radius about 50 m, damping time below 1e-10 s; Halle 1988; Adair 1992). Machlup 2007 and Engstrom 1996 try to rescue the theory.",
 [
  D("8074739", "Independent control of B_ac (7.7-46.8 uT rms), B_dc (36.6 uT or 2 uT off-resonance), f (45 vs 25 Hz) in a multi-coil system", "All PC-12 neurite outgrowth responses matched IPR predictions, including the off-resonance condition."),
  D("2242051", "Parallel vs perpendicular B_dc/B_ac at fixed 315 Hz, 61 nT rms, 15 V/m rms (in air)", "Ca2+ efflux from chick brain only when perpendicular; orientation matters while E magnitude is the same."),
  D("1854354", "Sample temperature varied during 16 Hz exposure", "Outcome was enhancement, reduction or null depending on temperature history, which may explain poor reproducibility."),
  D("12929158", "Cell-free plasma-membrane vesicles, 27-37 uT static x 7-72 Hz, 13-114 uT AC", "Ca-45 efflux confirmed the Blanchard IPR model quantitatively in a purified membrane system."),
  D("9453705", "Cell-free glutamic acid solution, 1-10 Hz sweep, B_ac 0.02-0.08 uT", "Current peak (20-30%) at the cyclotron frequency, proportional to B0 and only at very low B_ac (higher amplitudes abolished it)."),
  D("10453066", "Rats, DC 50 vs 500 uT with proportional AC frequency/amplitude", "Ca2+ frequency lowered and Mg2+ frequency raised open-field activity at both DC levels."),
  D("3663247", "Diatom motility, frequency and B_ac dose-response", "Sharp resonance at predicted Ca2+ frequency, dose-response in B_ac, odd harmonics also effective."),
  D("2012618", "16 Hz, 20.9 uT AC with 20.9 uT horizontal DC, diatoms", "Field-associated increase seen at 0.25 mM Ca2+ but too irreproducible to test frequency dependence."),
  D("2712845", "Fura-2 imaging in four cell lines, resonant and non-resonant fields", "No change in cytosolic Ca2+ (null)."),
  D("8451278", "Mouse lymphocytes, 16 and 50 Hz, DC shifted up to 25% either side, 60 min, ConA positive control", "No change in intracellular Ca2+ (null)."),
  D("1590822", "Theory critique", "Four independent reasons why a Lednev-type mechanism cannot operate.", None),
  D("1700714", "Theory critique", "Gyration radius about 50 m at Earth-field cyclotron frequency; damping time below 1e-10 s versus about 1e-2 s needed."),
  D("2461205", "Theory critique", "Model violates classical mechanics; friction precludes effect."),
  D("9905119", "Existing library ref (Adair 1991, constraints on weak ELF effects)", "Listed for completeness; contents not re-read in this pass.", refkey="adair1991"),
 ],
 [
  T("optimal", "Inhibition of NGF-stimulated neurite outgrowth following IPR-predicted pattern", "PC-12 cells, in vitro", "invitro", "8074739",
    B=round(bl_lo * 1e3, 4), Bnote="Reported B_ac 77-468 mG rms (7.7-46.8 uT rms) at 45 Hz; peak = rms x sqrt(2), computed; value given is the low end, high end 0.0662 mT peak.", f=45, wf="sine AC parallel to DC",
    dbdt=sd(45, bl_lo), dbasis="computed", B0=36.6,
    note="dB/dt computed at the low end; at the high end 2*pi*45*6.62e-5 = %.3g T/s. Off-resonance test used B_dc 2 uT with B_ac 0.79-2.1 uT rms; 25 Hz test used B_dc 20.3 uT with B_ac 7.8-18.1 uT rms. Exposure durations not in abstract." % sd(45, bl_hi)),
  T("lowest_effective", "Ca2+ efflux enhancement (resonance-like) from chick brain tissue", "Chick forebrain tissue, in vitro", "invitro", "2242051",
    B=round(61e-9 * SQ2 * 1e3, 6), Bnote="Reported 61 nT rms; peak computed.", f=315, wf="sine, B_ac perpendicular to B_dc",
    dbdt=sd(315, 61e-9 * SQ2), dbasis="computed", E=15, Ebasis="reported", Egeo="15 V/m rms electric field in air (not tissue E); tissue field much lower",
    note="B_dc not stated in the abstract. The effect appears with B_ac perpendicular to B_dc and not when parallel."),
  T("lowest_effective", "Enhanced diatom motion at 0.25 mM Ca2+ (poorly reproducible)", "Amphora coffeaeformis on agar", "invitro", "2012618",
    B=0.0209, Bnote="Reported AC amplitude 20.9 uT (rms/peak not stated; treated as nominal peak).", f=16, wf="sine parallel to DC",
    dbdt=sd(16, 20.9e-6), dbasis="computed", B0=20.9, note="Authors report poor reproducibility."),
  T("lowest_effective", "Cyclotron-resonance current peak (20-30% of DC)", "Cell-free aqueous glutamic acid", "invitro", "9453705",
    B=2e-5, Bnote="Reported B_ac 0.02 uT (low end); rms/peak not stated.", f=None, wf="sine AC swept 1-10 Hz, parallel to DC",
    note="Peak frequency proportional to static field; B_dc not in abstract."),
  T("loss_above", "Cyclotron-resonance current peak vanishes at larger AC amplitude", "Cell-free aqueous glutamic acid", "invitro", "9453705",
    B=8e-5, Bnote="Effect arises only for B_ac of 0.02-0.08 uT; above 0.08 uT it is absent.", f=None, wf="sine AC swept 1-10 Hz",
    note="Inverted-U / window in AC amplitude as IPR predicts through Bessel-type dependence."),
  T("optimal", "Ca-45 efflux modulation", "Purified plasma-membrane vesicles, 30 min, 32 C", "invitro", "12929158",
    B=0.114, Bnote="Upper end of tested peak AC range (13-114 uT peak); effective combinations not itemised in abstract.", f=72, wf="sine AC (7-72 Hz) with 27-37 uT static",
    exp="30 min", dbdt=sd(72, 114e-6), dbasis="computed", B0=32, note="dB/dt computed for the extreme combination 72 Hz x 114 uT only (upper bound); static range 27-37 uT (midpoint 32 uT shown)."),
  T("optimal", "Reduced locomotor/exploratory activity (Ca2+ frequency)", "Rats, open field", "animal", "10453066",
    B=None, Bnote="Amplitudes not given in abstract; AC scaled proportionally to DC.", f=None, wf="parallel DC + AC at ion cyclotron frequency", B0=50,
    note="Qualitatively the same at DC 50 uT and 500 uT (second DC level not representable in this field)."),
 ],
 "Effects, where seen, occur at AC amplitudes of 0.02 uT to about 66 uT peak with B0 of 20-50 uT (Earth-like) and are not monotonic in B_ac (window). Computed dB/dt is only 1e-6 to 2e-2 T/s. Activator is B_ac relative to B0 and frequency, not dB/dt.",
 "contested: positive claims from a few groups (Blackman/EPA, Zhadin, Fitzsimmons, Baureus Koch) vs multiple null replications (Parkinson, Coulton, Reese) and strong theoretical objections",
 "low",
 "Many positive studies are small and from the same labs; theory objections have not been resolved experimentally. Zhadin glutamic-acid result is in a cell-free solution, which is unusual. Liboff 2009/2010 (existing refs) argue for ICR-like geomagnetic regulation but were not re-read."));

# ---------------------------------------------------------------- 5 CMF bone
targets.append(G(
 "cmf_combined_field_bone_cells",
 "Combined static + low-frequency AC magnetic field (CMF) signalling in bone cells (Ca2+ flux, IGF-II)",
 "cellular",
 ["bone & cartilage repair"],
 "combined",
 "Fitzsimmons and colleagues report that a combined AC/DC field at about 15 Hz, with a calculated induced potential gradient of only 1e-5 V/m in medium, increases Ca2+ flux, IGF-II receptor number and IGF-II release in osteoblast-like cells, with a narrow frequency peak (15.3-16.3 Hz, bandwidth about 1 Hz). The 1e-5 V/m E is far below usual cellular E thresholds, so the authors argue for resonance-type dynamics, cell shape and signal averaging rather than simple induction. This is an ICR/IPR-type B_AC/B0 dependence, but B_ac and B_dc values were not in the abstracts and the work is from a single lab.",
 [
  D("7866919", "Frequency scan of CMF; calculated induced potential gradient 1e-5 V/m (abstract only)", "Net Ca2+ flux peaked at 15.3-16.3 Hz with about 1 Hz bandwidth, i.e. resonance-like narrow window."),
  D("7639117", "15.3 Hz CMF, 30 min, frequency-dependent", "IGF-II receptor number rose, IGF-I receptors unchanged (abstract only)."),
  D("7789337", "CMF 10 min, anti-IGF-II antibody control, cell-density variation", "IGF-II release and 24 h DNA synthesis rose; anti-IGF-II blocked proliferation; effect larger at low cell density."),
 ],
 [
  T("lowest_effective", "Increased net Ca2+ flux", "Human osteoblast-like (osteosarcoma) cells", "invitro", "7866919",
    f=15.3, wf="combined AC + static", E=1e-5, Ebasis="reported", Egeo="Calculated maximum potential gradient in culture medium (as reported in abstract)",
    note="Frequency window 15.3-16.3 Hz. B_ac and B_dc not available from the abstract (full text not retrieved). Back-estimate of B_ac (my computation, assumes 35 mm dish r = 17.5 mm and f = 15.3 Hz: B = 2E/(r*2*pi*f)) is about 1.2e-5 T (12 uT) pk, which is an assumption-laden estimate only."),
  T("optimal", "Increased IGF-II receptor number", "TE-85 osteosarcoma cells", "invitro", "7639117",
    f=15.3, wf="combined AC + static", exp="30 min", E=1e-5, Ebasis="reported", Egeo="Calculated maximum potential in culture medium"),
  T("optimal", "Increased IGF-II release and DNA synthesis", "TE-85 osteosarcoma cells", "invitro", "7789337",
    wf="combined AC + static", exp="10 min exposure; effects measured 1 h and 24 h later",
    note="Field amplitudes not in abstract."),
 ],
 "Reported E about 1e-5 V/m at 15.3-16.3 Hz (about 1 Hz bandwidth); B_ac/B_dc not retrieved. Not a dB/dt-scaling effect (E is tiny); narrow frequency window.",
 "single group (Loma Linda); no independent replication found in this search",
 "low",
 "Abstract-only data; amplitudes unknown; osteosarcoma lines; E value is a calculation by the authors and not a measurement."));

# ---------------------------------------------------------------- 6 Prato snail
targets.append(G(
 "snail_mouse_opioid_resonance_like",
 "Land-snail / mouse opioid-analgesia inhibition by ELF fields (resonance-like, light-dependent, Ca2+/NO)",
 "tissue-neural",
 ["pain relief"],
 "B_AC_over_B0",
 "The Prato/Kavaliers snail work reports amplitude windows (nonlinear in B_ac over 0-547 uT at 60 Hz), frequency windows at fixed 141 uT (30-35, 60-90, 120-240 Hz), dependence on the parallel static field, and angle dependence between AC (299 uT peak) and DC (78 uT) fields. The authors argue this excludes induced current (it would be constant with angle at fixed B_ac) and excludes magnetite torque (maximum would be at 90 degrees), and favour a Lednev-type parametric resonance with Ca2+ or K+ settings, a light requirement and NO involvement. A parallel line in rodents used rotating 0.5 Hz fields (0.15-0.8 mT; computed dB/dt up to 2.5e-3 T/s) and Ca2+-channel drugs.",
 [
  D("7601344", "Varied B_ac (0-547 uT peak), frequency (10-240 Hz at 141 uT), and static field at constant AC (snails)", "Nonlinear amplitude dependence, three frequency windows, effect depends on static field; concluded direct detection, not induced current."),
  D("8860729", "Angle between B_dc (78 uT) and B_ac (299 uT peak, 60 Hz) varied 0-90 degrees", "Inhibition about 20% at 0 and 90 degrees and up to 50% at 50-70 degrees: not explained by constant induced current or by magnetite."),
  D("10797457", "PRM-predicted parameter sets for Ca2+ and K+ ions, 141-414 uT peak, light vs dark, glibenclamide", "Analgesia was decreased, unchanged or increased as predicted; K+ setting effect blocked by glibenclamide; abolished in the dark."),
  D("10501522", "Light vs dark, NO precursor", "Light-dependent potentiation of arginine's inhibitory effect."),
  D("9795129", "NOS inhibitor L-NAME and NO donor SNAP with 15 min, 60 Hz, 141 uT peak", "L-NAME reduced and SNAP enhanced the magnetic inhibition: NO/NOS involved."),
  D("2452251", "0.5 Hz rotating field 1.5-8.0 G, Ca2+-channel agonists/antagonists (snail)", "Field reduced opioid/stress analgesia; DHP and non-DHP drugs modulated it."),
  D("2446152", "0.5 Hz rotating field, 60 min, mice, Ca2+-channel drugs", "Field reduced morphine analgesia; Ca2+-channel drugs modulated the inhibition."),
  D("12111760", "Not included", "Liboff 2002 published a comment on Prato 2000 (no abstract in PubMed).") if False else D("25962809", "Author's review", "Prato (2015) describes the field as not a balanced review and notes remaining work.")
 ],
 [
  T("optimal", "Reduced opioid-mediated analgesia (nonlinear in B_ac)", "Land snail Cepaea nemoralis", "animal", "7601344",
    B=0.141, Bnote="Reported peak 141 uT (frequency scan) within a 0-547 uT amplitude scan at 60 Hz.", f=60, wf="sine AC plus parallel static field",
    exp="15 min typical in this line of work (not in the 1995 abstract)", dbdt=sd(60, 141e-6), dbasis="computed",
    note="dB/dt at 547 uT, 60 Hz = %.3g T/s. Frequency windows at 141 uT: 30-35, 60-90, 120-240 Hz." % sd(60, 547e-6)),
  T("optimal", "Analgesia reduction maximal at 50-70 degrees between AC and DC", "Land snail", "animal", "8860729",
    B=0.299, Bnote="Reported 299 uT peak, 60 Hz, with B_dc 78 uT.", f=60, wf="sine AC; angle to DC varied", dbdt=sd(60, 299e-6), dbasis="computed", B0=78,
    note="About 20% inhibition at 0 and 90 degrees, up to 50% at 50-70 degrees; with fixed B_ac, dB/dt is constant across angles."),
  T("optimal", "Increase/decrease/no effect on analgesia per PRM prediction", "Land snail", "animal", "10797457",
    B=0.414, Bnote="Tested 141-414 uT peak; value shown is the upper end.", f=None, wf="sine AC plus static set per PRM for Ca2+ or K+",
    note="Frequencies and B_dc not in abstract."),
  T("optimal", "Inhibition of enkephalinase-induced antinociception (NO dependent)", "Land snail", "animal", "9795129",
    B=0.141, Bnote="Reported 141 uT peak.", f=60, wf="sine", exp="15 min", dbdt=sd(60, 141e-6), dbasis="computed"),
  T("optimal", "Reduced opioid analgesia (rotating field)", "Land snail", "animal", "2452251",
    B=0.8, Bnote="Rotating field magnitude 1.5-8.0 G = 0.15-0.8 mT; value is the upper end.", f=0.5, wf="rotating field (constant magnitude), 0.5 Hz",
    exp="15-30 min", dbdt=sd(0.5, 0.8e-3), dbasis="computed",
    note="Computed dB/dt = 2*pi*0.5*B magnitude: %.3g T/s at 0.8 mT and %.3g T/s at 0.15 mT." % (sd(0.5, 0.8e-3), sd(0.5, 0.15e-3))),
 ],
 "Snail effects at 0.14-0.55 mT peak, 60 Hz (computed dB/dt 0.05-0.2 T/s) with windows in B_ac, frequency, B_dc and angle; the angle test argues against a pure induced-current driver. Rodent rotating-field effects at 0.15-0.8 mT (computed 5e-4 to 2.5e-3 T/s).",
 "single research group (London, Ontario); contested - a published comment disputes the PRM reading (Liboff 2002) and the group's own 2015 account is not a balanced review",
 "low",
 "Light, species and circadian state modulate outcomes; B_dc values and frequencies are missing from several abstracts; mechanism (PRM vs other) unresolved."));

# ---------------------------------------------------------------- 7 mouse shielding
Er = 0.015
targets.append(G(
 "mouse_ambient_elf_detection_shielding_analgesia",
 "Mouse detection of ambient ELF magnetic field removal (mu-metal shielding analgesia) and B x f threshold",
 "tissue-neural",
 ["pain relief"],
 "dBdt_E",
 "This is the clearest quantitative B-vs-dB/dt test in the scope. Mu-metal shielding for 1 h/day induces naloxone-reversible analgesia in mice, and reintroducing 30 or 120 Hz fields of 25-500 nT peak attenuates it. At a constant B_pk x f product of 6000 nT-Hz (12.5-100 Hz) the attenuation was constant, so the detector responds to the B x f product, i.e. dB/dt (or induced current), not to B amplitude; the threshold is at or below 1000 nT-Hz (computed dB/dt_pk about 6.3e-6 T/s). Independent replication (Choleris 2002, Pisa and London) shows that nulling only the static component (Helmholtz coils) or screening only E does not reproduce shielding, implying the very weak time-varying magnetic component matters. Blue/UV light is required, so a photoreceptor-based mechanism is proposed.",
 [
  D("21381048", "Reintroduced 30 and 120 Hz fields (25-500 nT pk) and constant 6000 nT-Hz at 12.5, 25, 50, 100 Hz in a shielded box", "Attenuation scaled with amplitude at fixed frequency and was constant at fixed B x f: dependence on nT-Hz (a dB/dt-like metric); threshold at or below 1000 nT-Hz."),
  D("11798436", "Mu-metal shielding vs Helmholtz nulling of static B vs copper screening of E; replication in Pisa and London", "Only mu-metal shielding reduced stress-induced analgesia; nulling static B or screening E did not, pointing to the weak time-varying component."),
  D("18583276", "Red, blue, UV light during shielding", "Red light had no effect; blue (465 nm) and UV (405 nm) abolished the shielding analgesia; blue threshold about 5e16 photons/s/m2."),
  D("15672364", "1 h/day for 10 days, naloxone", "Analgesia peaked on days 4-6 and was blocked by naloxone; comparable to 5 mg/kg morphine."),
 ],
 [
  T("lowest_effective", "Attenuation of shielding analgesia (30 Hz)", "Male CD-1 mice, hot-plate, 1 h/day shielded exposure", "animal", "21381048",
    B=5e-5, Bnote="Reported 50 nT peak at 30 Hz (25 nT did not attenuate at 30 Hz).", f=30, wf="sine", exp="1 h per day", sched="repeated daily", dbdt=sd(30, 50e-9), dbasis="computed",
    E=ee(Er, sd(30, 50e-9)), Ebasis="computed", Egeo="Body-scale, assumed r = 15 mm mouse half-width (my assumption)", note="Product 50 nT x 30 Hz = 1500 nT-Hz."),
  T("lowest_effective", "Attenuation of shielding analgesia (120 Hz)", "Male CD-1 mice", "animal", "21381048",
    B=2.5e-5, Bnote="Reported 25 nT peak; significant at all tested amplitudes at 120 Hz.", f=120, wf="sine", exp="1 h per day", dbdt=sd(120, 25e-9), dbasis="computed",
    E=ee(Er, sd(120, 25e-9)), Ebasis="computed", Egeo="Body-scale, assumed r = 15 mm (my assumption)", note="Product 25 nT x 120 Hz = 3000 nT-Hz."),
  T("lowest_effective", "Detection threshold in B_pk x f", "Mice", "animal", "21381048",
    Bnote="Product, not an amplitude: at or below 1000 nT-Hz (1e-3 mT-Hz).", wf="sine", dbdt=float("%.3g" % (PI2 * 1e-6)), dbasis="computed",
    E=ee(Er, PI2 * 1e-6), Ebasis="computed", Egeo="Body-scale, assumed r = 15 mm (my assumption)", note="dB/dt_pk = 2*pi*(B_pk x f) = 2*pi*1e-6 T/s."),
  T("plateau", "Constant attenuation at constant B x f", "Mice", "animal", "21381048",
    Bnote="6000 nT-Hz at 12.5, 25, 50 and 100 Hz.", wf="sine", dbdt=float("%.3g" % (PI2 * 6e-6)), dbasis="computed",
    note="Decisive: same dB/dt, four different B amplitudes (480, 240, 120, 60 nT peak) -> same effect."),
  T("loss_above", "No exposure abolished the effect (except perhaps 120 Hz, 500 nT)", "Mice", "animal", "21381048",
    B=5e-4, Bnote="500 nT peak at 120 Hz.", f=120, wf="sine", dbdt=sd(120, 500e-9), dbasis="computed",
    note="Effect attenuated but not fully abolished at tested amplitudes."),
 ],
 "Threshold in this assay is at or below B_pk x f = 1000 nT-Hz, computed dB/dt_pk about 6.3e-6 T/s (computed body-scale E about 5e-8 V/m with assumed r = 15 mm), from ambient 25-500 nT, 12.5-240 Hz fields. Driver is B x f (dB/dt-like), not B.",
 "phenomenon replicated independently (Pisa + London, Choleris 2002, though both include Prato group); the B x f scaling is single-group",
 "medium",
 "These are removal-of-ambient-field experiments, an unusual regime; computed E uses an assumed geometry; mechanism unresolved (light/photoreceptor suggested). Existing library ref weaver1990 gives thermal-noise-limit context, not re-read here."));

# ---------------------------------------------------------------- 8 Cnp pain
targets.append(G(
 "cnp_specific_pulsed_waveform_analgesia",
 "Specific pulsed ELF waveform (Cnp) analgesia: snails, mice, healthy humans, RA/fibromyalgia",
 "tissue-neural",
 ["pain relief"],
 "waveform_spectral",
 "The group reports that analgesia depends on the specific waveform: in snails two other pulsed designs failed to induce analgesia while Cnp (about 100 uT peak, frequency modulated, 15 min) did, with partial opioid (delta, some mu) mediation. In mice, 100 uT Cnp was equivalent to roughly 5 mg/kg morphine. In humans, 30 min exposures raised experimental pain thresholds (double-blind, n=39 and 31) and reduced McGill pain ratings in 13 RA and 18 FM patients (up to 400 uT peak, below 3 kHz). The data point to waveform spectral content (not B amplitude or a single dB/dt) as the determinant, but the waveform is proprietary in the abstracts and dB/dt was not reported. The related Thomas 2007 RCT is an existing library ref.",
 [
  D("9111740", "Cnp vs two other pulsed waveforms (snail)", "Only Cnp produced analgesia; two other designs failed: waveform specificity."),
  D("9213364", "Opioid receptor-selective antagonists/agonists", "Reduced by naloxone, mu and delta antagonists, not kappa."),
  D("14698475", "Cnp 100 uT, hot-plate, morphine co-treatment (mice)", "Latency prolongation equivalent to about 5 mg/kg morphine; offset morphine hyperactivity."),
  D("15172106", "Double-blind, sham, 30 min, heat-pain thresholds", "Pain thresholds rose after active but not sham exposure; sensory thresholds unchanged; sex interaction."),
  D("16770449", "Double-blind placebo-controlled, 30 min, RA n=13 and FM n=18", "Significant pre-post x condition effect on McGill pain index in both groups; small trial."),
  D("18080043", "Existing library ref (Thomas 2007 RCT)", "Contents not re-read in this pass.", refkey="thomas2007"),
 ],
 [
  T("optimal", "Antinociception ('analgesia')", "Land snail", "animal", "9111740",
    B=0.1, Bnote="Reported about 100 uT peak.", wf="pulsed, frequency modulated ELF (Cnp)", exp="15 min", note="dB/dt not reported (waveform proprietary)."),
  T("optimal", "Hot-plate latency increase (about 5 mg/kg morphine equivalent)", "Male CF-1 mice", "animal", "14698475",
    B=0.1, Bnote="Reported 100 uT.", wf="pulsed ELF (Cnp)", note="Exposure time not in abstract."),
  T("optimal", "Reduced McGill pain index", "RA (n=13) and FM (n=18) patients, double-blind RCT", "human_rct", "16770449",
    B=0.4, Bnote="Reported 'up to 400 uT peak; below 3 kHz'.", wf="pulsed low-frequency", exp="30 min, single session",
    note="dB/dt not reported; sine upper bound at 3 kHz x 0.4 mT would be 7.5 T/s but the waveform is not a pure sine, so no dB/dt is assigned."),
  T("optimal", "Increased heat-pain threshold", "Healthy volunteers, double-blind", "human_rct", "15172106", wf="specific pulsed MF", exp="30 min", note="Field amplitude not in abstract."),
 ],
 "Effective peak fields about 0.1 mT (snail, mouse) and up to 0.4 mT (human), 30 min in humans; dB/dt and E not reported. Waveform-specific.",
 "single group (Lawson/Western); small trials; partial overlap with existing thomas2007 RCT",
 "low",
 "Waveform proprietary; sample sizes small; placebo not excluded (authors discuss). Positive-only evidence from one lab."));

# ---------------------------------------------------------------- 9 Jurkat Ca B-dose
targets.append(G(
 "elf_bdose_ca_oscillations_jurkat",
 "50 Hz B dose-response of Ca2+ oscillations in T cells (Lindstrom vs Wey)",
 "membrane/ion channel",
 ["wound/inflammation resolution"],
 "B_amplitude",
 "Lindstrom 1995 gave a dose-response in flux density at 50 Hz (threshold 0.04 mT, plateau 0.15 mT) and a frequency scan at 0.15 mT (5-100 Hz, peak 50 Hz), without a tuned DC field. B and f were varied but the paper does not separate B from f x B (dB/dt). A blinded repeat at 1.5 G (0.15 mT), 50 Hz (Wey 2000) found no effect (16.5% field, 14.6% sham, 14.2% no field), though the authors note they sampled cells differently (all cells, not pre-selected responders).",
 [
  D("7748202", "Flux density scan at 50 Hz; frequency scan at 0.15 mT; fura-2 microfluorometry in single preselected cells", "Threshold 0.04 mT, plateau 0.15 mT; broad frequency peak at 50 Hz."),
  D("10656853", "Blinded, randomised, field/sham/no-field; positive control anti-CD3", "Field 16.5% vs sham 14.6% vs no field 14.2%: no significant effect; cannot exclude responsive subpopulation."),
 ],
 [
  T("lowest_effective", "Onset of [Ca2+]i oscillations", "Jurkat T-cell line", "invitro", "7748202",
    B=0.04, Bnote="Reported 0.04 mT; rms/peak not stated; treated as nominal peak.", f=50, wf="sine", dbdt=sd(50, 4e-5), dbasis="computed", E=None, note="Threshold response: no effect below 0.04 mT."),
  T("plateau", "[Ca2+]i oscillations", "Jurkat T-cell line", "invitro", "7748202",
    B=0.15, Bnote="Reported 0.15 mT; rms/peak not stated.", f=50, wf="sine", dbdt=sd(50, 1.5e-4), dbasis="computed", note="Plateau at 0.15 mT; broad frequency peak at 50 Hz."),
 ],
 "Single-lab claim of a 50 Hz threshold near 0.04 mT with plateau at 0.15 mT (computed dB/dt 1.3e-2 to 4.7e-2 T/s if values are peak); not replicated by a blinded attempt at 0.15 mT.",
 "failed independent replication (Wey 2000, NIOSH) at the plateau amplitude",
 "low",
 "Cell pre-selection in the original; null in the repeat may reflect methodology rather than absence of effect."));

# ---------------------------------------------------------------- 10 MCF-7
mc = 1.2e-6 * SQ2
targets.append(G(
 "env_elf_melatonin_tamoxifen_mcf7",
 "Environmental-level 50/60 Hz microtesla fields blocking melatonin/tamoxifen action in MCF-7 cells",
 "cellular",
 [],
 "B_amplitude",
 "Liburdy 1993 reported a threshold between about 2 and 12 mG (0.2-1.2 uT) for 60 Hz. Harland & Liburdy 1997 used a Faraday's-law design to separate B from induced E and associated the effect with the magnetic component, not the induced E. Ishido 2001 found 1.2 uT and 100 uT identical at 50 Hz (83-fold B and dB/dt difference, same effect), indicating saturation in B instead of scaling with dB/dt; Girgert 2005 saw maximal response at 1.2 uT (non-monotonic). Independent confirmation exists (Blackman 2001, EPA; Ishido, Girgert), but 1.2 uT is below the 2 uT level that Valberg 1997 regards as implausible for a physical effect, and the original lab's earlier 1992 FEBS paper has a published erratum.",
 [
  D("9383244", "Faraday's-law design: B and induced E varied independently", "Block of melatonin/tamoxifen action tracked the magnetic field, not the induced electric field."),
  D("11180258", "Independent lab, blinded counts, 1.2 uT rms, 60 Hz, chambers with/without field", "Replicated: melatonin 16.7% inhibition lost; tamoxifen 18.6/25% became 8.7/13.1%."),
  D("11408347", "50 Hz at 1.2 uT vs 100 uT, 3-7 days", "Same uncoupling of melatonin MT1a to adenylyl cyclase at both amplitudes."),
  D("16168388", "Intensity-dependent tamoxifen dose-response shift, 50 Hz", "Maximal response at 1.2 uT (non-monotonic)."),
  D("19882681", "50 Hz, 1.2 uT, 48 h; transfected MT1 cells", "Melatonin-induced CREB/BRCA-1 binding and gene expression disrupted."),
  D("8320637", "60 Hz at about 2.4-2.5 mG vs about 12 mG", "Block only at about 12 mG; threshold between 2 and 12 mG."),
  D("11255213", "2 Hz, 0.3 mT PEMF with melatonin", "No effect of the PEMF on melatonin action or invasion: PEMF in the therapeutic range is null in this assay."),
  D("9216613", "Physics review", "Effects of ELF fields at or below 2 uT considered implausible; above 10 uT only with time averaging plus a magnetic-moment transducer."),
 ],
 [
  T("no_effect_below", "Melatonin growth inhibition preserved", "MCF-7 cells", "invitro", "8320637",
    B=round(2.4e-7 * SQ2 * 1e3, 6), Bnote="Reported about 2.4 mG (0.24 uT) 'average'; assumed rms, peak computed (x sqrt(2)).", f=60, wf="sine", dbdt=sd(60, 2.4e-7 * SQ2), dbasis="computed",
    note="Melatonin inhibition (18-27%) was intact at about 2.4-2.5 mG; threshold lies between 2 and 12 mG."),
  T("lowest_effective", "Block of melatonin oncostatic action", "MCF-7 cells", "invitro", "8320637",
    B=round(mc * 1e3, 5), Bnote="Reported about 12 mG = 1.2 uT; assumed rms, peak computed.", f=60, wf="sine", dbdt=sd(60, mc), dbasis="computed",
    note="Continuous exposure; duration of experiments about 7 days (per companion papers)."),
  T("optimal", "Block of melatonin and tamoxifen growth inhibition (independent replication)", "MCF-7 cells", "invitro", "11180258",
    B=round(mc * 1e3, 5), Bnote="Reported 1.2 uT rms; peak computed.", f=60, wf="sine", exp="continuous to 7 days", dbdt=sd(60, mc), dbasis="computed"),
  T("plateau", "Uncoupling of melatonin 1a receptor from adenylyl cyclase; same as at 1.2 uT", "MCF-7 cells", "invitro", "11408347",
    B=round(100e-6 * SQ2 * 1e3, 4), Bnote="Reported 100 uT; assumed rms, peak computed.", f=50, wf="sine", exp="3, 5 and 7 days", dbdt=sd(50, 100e-6 * SQ2), dbasis="computed",
    note="83-fold larger B (and dB/dt) than 1.2 uT gives the same effect: B-saturating, not dB/dt-scaling. 1.2 uT, 50 Hz computed dB/dt = %.3g T/s." % sd(50, mc)),
  T("optimal", "Maximal tamoxifen dose-response shift", "MCF-7 clones", "invitro", "16168388",
    B=round(mc * 1e3, 5), Bnote="Reported 1.2 uT; assumed rms, peak computed.", f=50, wf="sine", dbdt=sd(50, mc), dbasis="computed",
    note="Authors describe a maximal response at 1.2 uT with intensity dependence below and above."),
 ],
 "Reported effective 50/60 Hz field is 1.2 uT rms (1.7 uT peak, computed dB/dt about 5-6e-4 T/s), with a threshold between about 0.2 and 1.2 uT and the same effect at 100 uT. B-component associated by Faraday design; plateau/saturation suggests B or a B-dependent molecular transducer, not dB/dt.",
 "replicated by 3 independent labs (EPA Blackman 2001, NIES Ishido 2001, Gottingen Girgert) vs a physics objection (Valberg 1997) and a null with a different, therapeutic-type PEMF (Leman 2001)",
 "medium",
 "No therapeutic modality - included as the credibility benchmark for micro-tesla ELF effects. Original 1992 FEBS paper from the Liburdy lab (PMID 1333413) has an erratum (PMID 10930587, FEBS Lett 478:304, 2000; content not seen), so the Liburdy-lab data warrant caution; the 1997 Harland paper is also from that lab."));

# ---------------------------------------------------------------- 11 chick embryo
targets.append(G(
 "chick_embryo_pulse_shape_ut_fields",
 "Chick embryo teratogenic effects of microtesla pulsed fields (rise time / pulse shape)",
 "tissue-neural",
 [],
 "waveform_spectral",
 "Ubeda 1983 exposed chick embryos to 100 Hz pulses at 0.4-104 uT: abnormalities appeared only at 1.0 and 13.9 uT with 100 us rise time (window), and shorter rise times (2 and 42 us) at 0.4 and 1.0 uT gave bigger effects, strongest at 1.0 uT/42 us. Computed dB/dt for 1.0 uT is 0.01 T/s (100 us), 0.024 T/s (42 us) and 0.5 T/s (2 us); the non-monotonic result (42 us > 2 us) shows pulse shape/spectral content matters beyond peak dB/dt. A six-laboratory replication (Berman 1990, 1 uT, 2 us edges, 100 pps) found a small pooled excess (about 25% vs 19%) but only 2 of 6 labs were individually significant.",
 [
  D("6654743", "Same repetition rate, intensities 0.4-104 uT and rise times 100, 42, 2 us", "Window in amplitude at 100 us rise; stronger effects with faster edges, maximal at 42 us."),
  D("2242052", "Six independent labs, identical equipment, blinded scoring", "Pooled anomalies about 25% vs 19% (highly significant) but only two labs significant and unexplained inter-lab variation."),
 ],
 [
  T("lowest_effective", "Teratogenic changes (truncal nervous system)", "Chick embryo, first 48 h", "animal", "6654743",
    B=0.001, Bnote="Reported 1.0 uT; pulse amplitude basis (peak) assumed.", f=100, wf="pulsed, rise time 100 us", exp="48 h", dbdt=float("%.3g" % (1e-6 / 100e-6)), dbasis="computed",
    note="dB/dt computed as B/t_rise = 1e-6 T / 1e-4 s. At 42 us rise: 0.0238 T/s (strongest effect)."),
  T("optimal", "Teratogenic changes (strongest)", "Chick embryo", "animal", "6654743",
    B=0.001, Bnote="Reported 1.0 uT, rise time 42 us.", f=100, wf="pulsed, rise time 42 us", exp="48 h", dbdt=float("%.3g" % (1e-6 / 42e-6)), dbasis="computed"),
  T("optimal", "Circulatory/foregut abnormalities", "Chick embryo", "animal", "6654743",
    B=0.0139, Bnote="Reported 13.9 uT, 100 us rise.", f=100, wf="pulsed, rise time 100 us", exp="48 h", dbdt=float("%.3g" % (13.9e-6 / 100e-6)), dbasis="computed"),
  T("no_effect_below", "No teratogenic change at 100 us rise time", "Chick embryo", "animal", "6654743",
    B=0.0004, Bnote="Lowest tested intensity 0.4 uT (and intensities other than 1.0 and 13.9 uT up to 104 uT were not effective at 100 us).", f=100, wf="pulsed, rise time 100 us",
    dbdt=float("%.3g" % (0.4e-6 / 100e-6)), dbasis="computed", note="Intermediate intensities tested are not itemised in the abstract."),
  T("optimal", "Increased anomalies, multi-lab", "Chick embryo, six labs", "animal", "2242052",
    B=0.001, Bnote="Reported 1 uT peak.", f=100, wf="unipolar pulse, 500 us width, 2 us rise/fall", pw=0.5, burst="100 pulses/s", exp="48 h",
    dbdt=float("%.3g" % (1e-6 / 2e-6)), dbasis="computed", note="dB/dt computed as B_pk/t_edge = 1e-6/2e-6 = 0.5 T/s. 25% vs 19% pooled."),
 ],
 "Teratogenic window around 1-14 uT peak (100 Hz) with computed dB/dt of 0.01-0.5 T/s; effect depends on edge speed in a non-monotonic way (42 us > 2 us > 100 us at 1 uT). Replication across six labs was only partial.",
 "multi-laboratory replication with marginal/variable outcome",
 "low",
 "Hazard-oriented, not a therapeutic readout; dB/dt values are computed by me from the stated rise times and amplitudes."));

# ---------------------------------------------------------------- 12 static weak field redox
targets.append(G(
 "weak_static_field_redox_regeneration",
 "Weak/static and hypomagnetic field effects via ROS and redox (planarian regeneration, metabolic mice, flavoenzymes)",
 "cellular",
 ["wound/inflammation resolution"],
 "B_amplitude",
 "Static fields have dB/dt = 0 by definition, so any effect is B-driven (or driven by a coincident static E). Van Huizen 2019 saw planarian regeneration go up or down with static field strength below 1 mT through ROS and Hsp70; Carter 2020 reported that a combined static magnetic (about 3 mT) plus static electric (about 7 kV/m) exposure improved glucose tolerance in mice, with 3.0 mT effective and 0.5 mT ineffective in hepatoma cells and mitochondrial SOD2 abolishing the effect; Austvold 2024 found ROS partitioning in a flavoenzyme differs between 20 nT and 50 uT. Binhi & Prato 2017 conclude that hypomagnetic effects show no consistent correlation with field magnitude, duration or type, arguing against a single common target.",
 [
  D("30729158", "Static fields below 1 mT, RNAi of Hsp70, ROS measurement (planarian)", "Regeneration increased or decreased depending on field strength; mediated by ROS and Hsp70."),
  D("33027675", "Static B plus static E in mice (30 days), cell dose-response 0.5-5 mT, SOD2 rescue", "3.0 mT lowered superoxide and raised H2O2 in Hepa1-6, 0.5 mT did not; SOD2 abolished the in vivo effect (full text grepped; E was co-applied so B vs E is not separated)."),
  D("38370016", "Purified ETF flavoenzyme, 20 nT vs 50 uT static", "13% less H2O2 and 10% more superoxide at 50 uT relative to 20 nT; matches RPM calculation."),
  D("28654641", "Review of hypomagnetic experiments", "No statistical correlation of the effect with field magnitude, inhomogeneity, exposure type or duration."),
 ],
 [
  T("lowest_effective", "Lower mitochondrial superoxide, higher H2O2", "Hepa1-6 cells, in vitro", "invitro", "33027675", src="fulltext",
    B=3.0, Bnote="Reported 3.0 mT static (0.5 mT ineffective); 5-10 kV/m static E co-applied in the full study.", f=0, wf="static", dbdt=0, dbasis="computed",
    note="Mouse study used about 3 mT plus about 7 kV/m vertical static E for 30 days."),
  T("no_effect_below", "No change in superoxide/H2O2", "Hepa1-6 cells", "invitro", "33027675", src="fulltext", B=0.5, Bnote="Reported 0.5 mT.", f=0, wf="static", dbdt=0, dbasis="computed"),
  T("optimal", "ROS partitioning shift (H2O2 -13%, O2 +10%)", "Recombinant human ETF flavoenzyme", "invitro", "38370016",
    B=0.05, Bnote="Reported 50 uT vs 20 nT; effect is the difference between the two.", f=0, wf="static", dbdt=0, dbasis="computed", B0=50),
 ],
 "Static-field effects reported from 20 nT-50 uT (flavoenzyme) through <1 mT (planarian) to about 3 mT (hepatoma cells, with coincident static E); dB/dt = 0 so the driver is B (or coincident E). Sign and size vary with field strength.",
 "single groups; independent confirmation lacking",
 "low",
 "Heterogeneous endpoints; Carter combined B and static E; planarian amplitudes not in abstract; reviewers report no consistent hypomagnetic dose-response."));

# ---------------------------------------------------------------- 13 magnetite
ms = 4.8e5
V50 = (50e-9) ** 3
m50 = ms * V50
kT = 1.380649e-23 * 310
targets.append(G(
 "biogenic_magnetite_magnetosome_torque",
 "Biogenic magnetite / magnetosome and ferritin magnetomechanical transduction",
 "cellular",
 ["neuro-modulation/neuroprotection"],
 "B_amplitude",
 "For magnetite-based transducers the interaction energy is mB (torque on a permanent moment) and scales with B amplitude; it does not depend on dB/dt except through viscous-lag filtering. A single-domain 50 nm magnetite cube (assumed M_s = 4.8e5 A/m, my assumption) has m = 6e-17 A m2, giving mB about 14 kT at 1 mT and 0.7 kT at 50 uT (computed at 310 K), so mT-level pulses could in principle align such particles whereas geomagnetic-strength fields cannot beat thermal noise unless chains or clusters are involved. Meister 2016 shows ferritin/MagR actuation claims are physically impossible (5-10 log units) and that only permanent-moment particles of about 30 nm and larger (magnetosomes) are plausible. Magnetite exists in human brain (kirschvink1992 in library; Gilder 2018 maps it to cerebellum and brain stem), and a strong pulse shifts bird headings via upper-beak magnetite (Wiltschko 2009).",
 [
  D("27529126", "Physical analysis of ferritin/MagR claims (full text read)", "Reported effects are 5-10 log units too large; ferritin torque 4 log units below kT at about 50 mT; permanent-moment (magnetosome-like) particles could work."),
  D("31373554", "Alternative mechanisms proposed", "Magneto-mechanical and magneto-thermal routes suggested for ferritin spin configurations (theory)."),
  D("26569474", "Protein complex alignment assay", "Reports spontaneous alignment of a MagR/Cry complex in fields; challenged by Meister."),
  D("19324756", "Strong magnetic pulse, upper-beak anaesthesia (silvereye)", "Pulse shifted headings by about 90 degrees; local anaesthesia of upper-beak skin prevented it."),
  D("15863473", "Physical model of superparamagnetic clusters", "Chains of SP clusters self-assemble in fields and are disrupted by strong oblique pulses; supports a pulse-effect mechanism."),
  D("30054530", "Remanence mapping in 7 human brains", "Magnetite concentrated in cerebellum and brain stem."),
  D("1502184", "Existing library ref (Kirschvink 1992, magnetite in human brain)", "Contents not re-read.", refkey="kirschvink1992"),
  D("8096090", "placeholder", "placeholder") if False else D("8601753", "Radical-pair theory context", "Distinguishes spin chemistry from magnetite as separate transduction routes.")
 ],
 [
  T("lowest_effective", "Interaction energy mB of a single-domain 50 nm magnetite cube vs kT (310 K)", "Theory / my calculation (assumed M_s = 4.8e5 A/m, not verified in the library)", "theory", "",
    src="fulltext", B=1.0, Bnote="Computed: m = M_s*V = %.2g A m2; mB = %.2g J = %.0f kT at 1 mT (about %.1f kT at 50 uT)." % (m50, m50 * 1e-3, m50 * 1e-3 / kT, m50 * 50e-6 / kT), f=0, wf="static or quasi-static",
    dbdt=0, dbasis="computed", note="Assumptions: 50 nm cube, bulk magnetite M_s, 310 K; permanent-moment single-domain particles only (superparamagnetic particles need larger fields)."),
  T("no_effect_below", "Ferritin torque / force far below kT", "Theory", "theory", "27529126", src="fulltext",
    B=50, Bnote="At about 50 mT ferritin anisotropy torque is about 4 log units below kT; a 100-fold larger field could give torque comparable to kT; reported ferritin experiments used 0.05 T and 6.6 T/m.", f=0, wf="static", dbdt=0, dbasis="computed",
    note="Even at 5 T the dipole-dipole force is about 4 log units too small."),
 ],
 "Magnetite torque is a B-amplitude (not dB/dt) mechanism: mB about 14 kT at 1 mT and 0.7 kT at 50 uT for a 50 nm single-domain particle (computed); ferritin-based mechanisms are ruled out by Meister at mT-T levels.",
 "single groups; physical plausibility strongly contested (Meister 2016) for ferritin/MagR, open for magnetosomes",
 "medium",
 "No direct PEMF-therapy experiment tests magnetite. M_s and particle size are my assumptions. Bird pulse experiments use much stronger/shorter pulses than therapeutic PEMF."));

# ---------------------------------------------------------------- 14 SMF
targets.append(G(
 "smf_diamagnetic_anisotropy_gradient_pain",
 "Static magnetic field (SMF): membrane diamagnetic anisotropy, gradient forces, and SMF pain trials",
 "membrane/ion channel",
 ["pain relief", "bone & cartilage repair"],
 "B_amplitude",
 "SMF effects have dB/dt = 0 except by motion, so they are B (or B x gradient) driven. Rosen 2003 argues moderate SMF (mT to hundreds of mT) reorient diamagnetically anisotropic membrane phospholipids and deform Ca2+ and Na+ channels; Zablotskii 2016 theory suggests about 1 T with gradient up to 1 GT/m could shift membrane potential (far from permanent-magnet therapy). Strong SMF (8 T) aligns osteoblasts and orients new bone (Kotani 2002). Clinical SMF pain trials are mixed: positive 450 G insoles in 375 DPN patients (Weintraub 2003) and 300-500 G in post-polio (Vallbona 1997), a modest bracelet effect of uncertain specificity (Harlow 2004), and a meta-analysis of nine VAS trials showing no effect (Pittler 2007). Colbert 2008/2009 show most trials lack adequate dosimetry (61%).",
 [
  D("14515021", "Mechanistic review with patch clamp and temperature dependence", "SMF effects on Ca2+/Na+ channels via phospholipid anisotropy with thermotropic phase-transition dependence."),
  D("12736891", "Double-blind sham, 4 months, 375 DPN patients", "Burning -12% vs -3%, numbness -10% vs +1% in months 3-4."),
  D("9365349", "Double-blind, 45 min, n=50", "Pain score fell 4.4 vs 1.1; 76% vs 19% exceeded placebo effect."),
  D("15604181", "Three-arm RCT, 12 weeks, n=194", "WOMAC A mean difference 1.3 (95% CI 0.05 to 2.55) standard vs dummy; uncertain specificity."),
  D("17893349", "Meta-analysis of nine placebo-controlled VAS trials", "WMD 2.1 mm (95% CI -1.8 to 5.9) - no significant pain reduction."),
  D("18955243", "Review of 56 SMF human studies", "34 (61%) lacked enough SMF dosimetry to replicate."),
  D("18532897", "Dosimetry argument", "Negative trials uninterpretable without target-tissue field; defines ten dosing parameters."),
  D("12369785", "8 T SMF, 60 h, MC3T3-E1 and mouse ectopic bone", "Cells aligned parallel to field, ALP and matrix up, proliferation unchanged; bone oriented parallel to field."),
  D("27857227", "Theory", "About 1 T with gradient up to 1 GT/m could change membrane potential."),
 ],
 [
  T("optimal", "Reduced burning/numbness/foot pain (months 3-4)", "375 DPN patients, shoe insoles", "human_rct", "12736891",
    B=45, Bnote="Reported 450 G multipolar insoles; surface field (target-tissue field not stated in abstract).", f=0, wf="static", exp="constant wear", sched="4 months", dbdt=0, dbasis="computed"),
  T("optimal", "Reduced McGill pain score", "50 postpolio patients, trigger-point magnets", "human_rct", "9365349",
    B=50, Bnote="Reported 300-500 G (30-50 mT); value is upper end.", f=0, wf="static", exp="45 min", dbdt=0, dbasis="computed"),
  T("optimal", "Osteoblast alignment, ALP and mineralisation increase", "MC3T3-E1 cells and mouse BMP-2 pellets", "invitro", "12369785",
    B=8000, Bnote="Reported 8 T.", f=0, wf="static", exp="60 h", dbdt=0, dbasis="computed", note="Proliferation unchanged."),
  T("optimal", "Theoretical membrane-potential change", "Theory", "theory", "27857227",
    B=1000, Bnote="About 1 T with gradient up to 1 GT/m.", f=0, wf="static", dbdt=0, dbasis="computed"),
 ],
 "SMF therapy trials use 30-50 mT surface fields (computed dB/dt = 0) with conflicting outcomes; strong-field cellular effects require roughly 1-8 T and/or very high gradients.",
 "contested - RCTs mixed; meta-analysis null; cellular effects rely on single groups",
 "low",
 "Surface vs target-tissue field not known; sham designs and blinding vary. Weintraub 2003 (this SMF trial, PMID 12736891) must not be confused with the existing weintraub2009 PEMF ref (PMID 19577022)."));

# ---------------------------------------------------------------- 15 Lorentz
v_t = 0.5
targets.append(G(
 "lorentz_hall_mhd_negligible_at_pemf",
 "Lorentz force, Hall and magnetohydrodynamic effects (blood flow, vestibular)",
 "tissue-neural",
 ["vascular/angiogenesis"],
 "B_amplitude",
 "Lorentz/MHD effects scale with B x velocity (induced field v x B) or J x B body force, not with dB/dt, and become significant only at tesla levels: Roberts 2011 found nystagmus proportional to static field in 3 T and 7 T scanners (little or none near 0.7 T) explained by Lorentz force on endolymph; Tenforde 2005 reports no hemodynamic effects at 1.5 T and SA-node current density above 100 mA/m2 only above 5 T; aortic flow reduction 1.3% (5 T), 4.9% (10 T), 10.4% (15 T); Kinouchi 1996 finds MHD flow reduction only above about 10 T. ICNIRP 2009 sets 2 T (head/trunk occupational), 8 T (limbs) and 400 mT (public). At PEMF mT levels my computed values are tiny: v x B with v = 0.5 m/s and B = 2 mT gives 1 mV/m, and a J x B body force with J = 0.5 A/m2 (E = 1 V/m, sigma = 0.5 S/m) at 2 mT is about 1e-3 N/m3, i.e. 1e-7 of gravity body force (rho*g = 1e4 N/m3).",
 [
  D("21945276", "Static field 3 T vs 7 T, speed of table varied, polarity reversed, search coil EMI recording, labyrinthine-deficient controls (full text read)", "Nystagmus scaled with static B, not with motion-induced voltage, reversed with polarity, absent without labyrinth; calculated Lorentz pressure 0.002-0.02 Pa at 7 T vs threshold 0.0001 Pa."),
  D("15556666", "Review of animal and modelling data to 15 T", "No hemodynamic changes at <=1.5 T; SA-node current density >100 mA/m2 above 5 T; flow reduction 1.3/4.9/10.4% at 5/10/15 T."),
  D("8742752", "Finite-element Navier-Stokes of aortic flow", "MHD flow reduction only above about 10 T."),
  D("19276710", "ICNIRP static-field guidelines (document text fetched from icnirp.org)", "2 T head/trunk occupational, 8 T limbs, 400 mT general public; vertigo ~1 T/s motion-induced; flow potentials >~0.1 T near heart; estimated induced E about 2 V/m for 0.5 m/s into 4 T."),
  D("8938025", "Existing library ref (Gabriel 1996 tissue conductivity)", "Tissue conductivity of order 0.1-1 S/m used as an order-of-magnitude assumption.", refkey="gabriel1996"),
 ],
 [
  T("no_effect_below", "No hemodynamic changes", "Monkeys and dogs", "animal", "15556666", src="abstract_only",
    B=1500, Bnote="Reported static fields up to 1.5 T.", f=0, wf="static", dbdt=0, dbasis="computed"),
  T("adverse", "SA-node induced current density >100 mA/m2 predicted", "Human model", "theory", "15556666", src="abstract_only",
    B=5000, Bnote="Above 5 T.", f=0, wf="static", dbdt=0, dbasis="computed", note="Aortic flow reduction 1.3% (5 T), 4.9% (10 T), 10.4% (15 T)."),
  T("lowest_effective", "Horizontal nystagmus (magnetic vestibular stimulation)", "Healthy humans in 3 T and 7 T MRI", "human_other", "21945276", src="fulltext",
    B=3000, Bnote="Reported 3 T and 7 T; proportional to B; outside bore (~0.7 T) little or no nystagmus.", f=0, wf="static", dbdt=0, dbasis="computed",
    note="Linear-scaling inference (my computation, not in paper): 0.0001 Pa threshold vs 0.002-0.02 Pa at 7 T would imply a threshold of order 0.035-0.35 T; treat as an extrapolation only."),
  T("safety_limit", "Occupational head/trunk", "Standard", "standard", "19276710", src="fulltext", B=2000, Bnote="2 T (spatial peak); up to 8 T for controlled work.", f=0, wf="static", dbdt=0, dbasis="computed",
    note="Source: ICNIRP document text via icnirp.org (PubMed record has no abstract)."),
  T("safety_limit", "Occupational limbs", "Standard", "standard", "19276710", src="fulltext", B=8000, Bnote="Up to 8 T for limbs.", f=0, wf="static", dbdt=0, dbasis="computed"),
  T("safety_limit", "General public, any part of the body", "Standard", "standard", "19276710", src="fulltext", B=400, Bnote="400 mT (factor of 5 below 2 T).", f=0, wf="static", dbdt=0, dbasis="computed"),
  T("adverse", "Induced field from Lorentz motion, computed", "Theory / my calculation", "theory", "", src="fulltext",
    B=2.0, Bnote="B = 2 mT, v = 0.5 m/s (blood or body motion, assumption).", f=0, wf="static or slow", E=float("%.3g" % (v_t * 2e-3)), Ebasis="computed",
    Egeo="E = v x B = 0.5 m/s x 2e-3 T = 1e-3 V/m; for 5 mT 2.5 mV/m; at 1 T 0.5 V/m", dbdt=0, dbasis="computed",
    note="Compare ICNIRP's quoted ~2 V/m for walking into a 4 T magnet. Body force: J x B = 0.5 A/m2 x 2e-3 T = 1e-3 N/m3 vs rho*g = 1e4 N/m3 (ratio 1e-7); sigma = 0.5 S/m assumed."),
 ],
 "Lorentz/Hall/MHD effects are negligible at PEMF peak fields of 1-50 mT (computed v x B about 1-25 mV/m, force ~1e-7 of gravity) and become measurable only at about 1-7 T (vestibular, proportional to B) and relevant to cardiovascular function above about 5 T.",
 "multiple independent sources (clinical, animal, modelling, standards)",
 "high",
 "Computed estimates rely on assumed v = 0.5 m/s, sigma = 0.5 S/m and a J = 0.5 A/m2 at E = 1 V/m; Roberts 2011 threshold extrapolation is a linear guess. ICNIRP numbers come from a fetched summary of the guideline text and should be checked against the PDF if used in a calculator."));

# ---------------------------------------------------------------- 16 decision tests
targets.append(G(
 "decision_tests_B_vs_dBdt_E",
 "Decision-test record: experiments that discriminate B-driven from dB/dt/E-driven effects",
 "cellular",
 [],
 "unresolved",
 "Discriminating designs in the library: (1) constant B with variable induced E using multi-ring Faraday geometry (Liburdy 1992: E at constant B governed Ca2+ influx; a pure E field gave the same effect), versus the same trick applied to MCF-7 growth (Harland & Liburdy 1997: B, not E, associated). (2) Static vs ELF equivalence (Fedele 2014: 0, 3, 50 Hz same effect, so B). (3) Constant B x f at different B and f (Prato 2011: constant effect, so dB/dt-like). (4) Selective removal of components (Choleris 2002: static nulling did not reproduce shielding; E screening did not either). (5) Orientation/angle tests at fixed amplitude (Prato 1996; Blackman 1990; Ritz 2004). (6) Dose-response saturation (Ishido 2001: 1.2 vs 100 uT same). Different endpoints therefore give different answers: the same lab line produced an E metric in one system and a B metric in another, so no single driver applies across targets.",
 [
  D("1333413", "Multi-ring annular plate: induced E varied at constant 22 mT, 60 Hz, vs pure E exposure", "Ca2+ influx tracked induced E (1.7 mV/cm = 0.17 V/m reported) and a pure E field of equal strength matched it (erratum exists)."),
  D("9383244", "Faraday-law design for B vs induced E", "Melatonin/tamoxifen block tracked B, not induced E."),
  D("25473952", "Static vs 3 Hz vs 50 Hz at 300 uT", "Same effect: B-driven (dB/dt from 0 to 0.094 T/s computed)."),
  D("21381048", "Constant B x f at 4 frequencies", "Constant attenuation: dB/dt-like."),
  D("11798436", "Static nulling vs mu-metal vs E screening", "Only shielding worked: time-varying B component."),
  D("8860729", "Angle between AC and DC at fixed AC", "Effect varies with angle, not with constant induced current."),
  D("11408347", "1.2 vs 100 uT", "Same effect at 83-fold different B and dB/dt: saturation."),
 ],
 [
  T("lowest_effective", "Increase in Ca2+ influx in mitogen-activated thymocytes (induced E metric)", "Rat thymic lymphocytes, 37 C, 60 min", "invitro", "1333413",
    B=round(22.0 * SQ2 * 0 + 22.0, 3), Bnote="Reported 22 mT, 60 Hz; rms/peak not stated; treated as nominal peak.", f=60, wf="sine", exp="60 min", dbdt=sd(60, 22e-3), dbasis="computed",
    E=0.17, Ebasis="reported", Egeo="Reported induced E 1.7 mV/cm (= 0.17 V/m) in the annular culture plate (dish scale)",
    note="Erratum exists (PMID 10930587). Computed back-radius r = 2E/(dB/dt) = %.3g m (plate-scale consistency check, my computation)." % (2 * 0.17 / sd(60, 22e-3))),
 ],
 "No universal driver: Ca2+ influx in lymphocytes followed induced E (0.17 V/m at 22 mT, 60 Hz; computed dB/dt 8.3 T/s), fly circadian and MCF-7 data follow B, mouse shielding analgesia follows B x f (dB/dt-like).",
 "mixed - several individual decision tests, mostly single-lab",
 "medium",
 "Liburdy-lab studies (1992, 1993, 1997) share an author with a published erratum on the 1992 paper. Not every claimed mechanism has had a B-vs-E test."));

# ---------------------------------------------------------------- 17 plausibility
targets.append(G(
 "plausibility_kT_and_standards_context",
 "Physical plausibility (kT, ELF theory) and exposure-standard context for B-driven mechanisms",
 "biochemical",
 [],
 "unresolved",
 "Valberg 1997 concludes residential-level ELF effects (<=2 uT) are implausible and that effects above 10 uT would be plausible only through temporal averaging plus a magnetic-moment transducer; resonance mechanisms conflict with accepted physics. Binhi & Rubin 2007 counter that the 'kT paradox' rests on assumptions that may not hold for magnetic nanoparticles, long-lived rotational states or radical-pair spins. Brocklehurst & McLauchlan 1996 and Kattnig 2016 bound radical-pair mechanisms by lifetimes and relaxation. The ICNIRP 2010 guideline (existing ref icnirp2010) treats induced E as the basic restriction (CNS 10-25 Hz: 0.05 V/m occupational, 0.01 V/m public rms) with reference B of 1 mT occupational and 0.2 mT general public (50/60 Hz, rms), i.e. standards operate on E, not on B. WHO EHC 238 (2007) and the SCENIHR 2015 opinion (not in PubMed; read via fetched summaries) state that no accepted biophysical mechanism explains low-level ELF health effects; WHO states established acute effects occur at well above 100 uT through induced E and currents.",
 [
  D("9216613", "Physics review of mechanisms", "<=2 uT implausible; >10 uT only with averaging plus magnetic-moment transducer (abstract only)."),
  D("17454082", "Critique of the kT argument", "Specific loopholes (nanoparticles, rotational states, radical pairs, proton moments) can in principle evade kT."),
  D("21068601", "Existing library ref ICNIRP 2010 (guideline numbers from fetched icnirp.org text)", "Basic restrictions on internal E (CNS 0.01 V/m public at 10-25 Hz) and reference B 0.2 mT public, 1 mT occupational at 50/60 Hz.", refkey="icnirp2010"),
  D("9905119", "Existing library ref (Adair 1991)", "Contents not re-read in this pass.", refkey="adair1991"),
  D("8601753", "Radical-pair theory", "Lifetime and chemistry limit freely diffusing pairs."),
  D("27020113", "Relaxation simulations", "Microsecond lifetimes optimal; long coherence unlikely."),
 ],
 [
  T("safety_limit", "ICNIRP reference level, general public (rms)", "Standard", "standard", "21068601", src="fulltext", refkey="icnirp2010",
    B=round(0.2 * SQ2, 3), Bnote="Reference level 0.2 mT rms at 50/60 Hz; peak = rms x sqrt(2), computed.", f=50, wf="sine", dbdt=sd(50, 0.2e-3 * SQ2), dbasis="computed",
    note="Fetched from icnirp.org guideline text. At 60 Hz the same 0.2 mT rms."),
  T("safety_limit", "ICNIRP reference level, occupational (rms)", "Standard", "standard", "21068601", src="fulltext", refkey="icnirp2010",
    B=round(1.0 * SQ2, 3), Bnote="Reference level 1 mT rms at 50/60 Hz; peak computed.", f=50, wf="sine", dbdt=sd(50, 1e-3 * SQ2), dbasis="computed"),
  T("safety_limit", "ICNIRP basic restriction, CNS tissue of the head, 10-25 Hz, general public", "Standard", "standard", "21068601", src="fulltext", refkey="icnirp2010",
    f=None, wf="sine", E=0.01, Ebasis="reported", Egeo="Internal E, rms, CNS tissue (10-25 Hz); occupational 0.05 V/m", note="All tissues 1 Hz-3 kHz: 0.4 V/m public, 0.8 V/m occupational; magnetophosphene threshold ~5 mT at 20 Hz (retinal E ~50-100 mV/m); PNS ~4-6 V/m."),
  T("lowest_effective", "Plausibility floor for ELF magnetic effects (physics review)", "Theory", "theory", "9216613",
    B=0.0, Bnote="Effects at <=2 uT judged implausible; >10 uT (0.01 mT) possibly plausible via averaging + moment transducer (not a measured threshold).", wf="ELF", note="Used only as a benchmark for credibility, not a dose-response."),
 ],
 "Credibility benchmark: physics reviews put the plausibility boundary between about 2 and 10 uT; ICNIRP 2010 reference B is 0.2 mT (public) / 1 mT (occupational) rms at 50/60 Hz, derived from induced-E basic restrictions (0.01-0.05 V/m CNS at 10-25 Hz).",
 "consensus bodies (WHO, SCENIHR) vs individual positive studies",
 "medium",
 "WHO EHC 238 and SCENIHR 2015 are not PubMed-indexed and were read through fetched summaries only; not added as refs. ICNIRP numbers came from a fetched summary of the PDF."));

# fix the placeholder in target 6 (list comprehension guard)
for tg in targets:
    tg["discriminating_evidence"] = [e for e in tg["discriminating_evidence"] if e["finding"] != "placeholder"]

# ---------------------------------------------------------------- refs
ACC = {"Engstrom": "Engström", "Lindstrom": "Lindström", "Baureus Koch": "Bauréus Koch"}
new_refs = []
for r in REFS:
    (pmid, fa, auth, yr, title, jr, cit, doi, pmc, typ, sysl, mech, dirn, summ) = r
    fa = ACC.get(fa, fa)
    auth = auth.replace("Engstrom", "Engström").replace("Lindstrom", "Lindström").replace("Baureus Koch", "Bauréus Koch").replace("Kavaliers M, Prato", "Kavaliers M, Prato")
    new_refs.append({"pmid": pmid, "first_author": fa, "authors_short": auth, "year": yr, "title": title, "journal": jr,
                     "citation": cit, "doi": doi, "pmcid": pmc, "type": typ, "systems": sysl, "mechs": mech,
                     "direction": dirn, "summary": summ})

existing = {}
with open("/tmp/claude-0/thr/existing_refs.tsv", encoding="utf-8") as fh:
    for row in csv.DictReader(fh, delimiter="\t"):
        existing[row["pmid"]] = row["key"]

dupe = [r["pmid"] for r in new_refs if r["pmid"] in existing]
newset = {r["pmid"] for r in new_refs}
assert not dupe, dupe
assert len(newset) == len(new_refs), "duplicate pmid in new_refs"

missing = set()
for tg in targets:
    for e in tg["discriminating_evidence"]:
        if e["pmid"] and e["pmid"] not in newset and e["pmid"] not in existing:
            missing.add(("evidence", tg["id"], e["pmid"]))
        if e["refkey"] and existing.get(e["pmid"]) != e["refkey"]:
            missing.add(("refkey-mismatch", tg["id"], e["pmid"], e["refkey"]))
    for t in tg["thresholds"]:
        if t["pmid"] and t["pmid"] not in newset and t["pmid"] not in existing:
            missing.add(("threshold", tg["id"], t["pmid"]))
        if t["refkey"] and existing.get(t["pmid"]) != t["refkey"]:
            missing.add(("refkey-mismatch", tg["id"], t["pmid"], t["refkey"]))
print("missing/mismatch:", missing)

out = {"scope": "thr_6_B_driven: mechanisms where field amplitude B or B-direction (or B relative to a static B0), rather than dB/dt or induced E, is the putative driver: radical pair / cryptochrome / flavin; ion cyclotron and ion parametric resonance incl. combined fields and Prato snail/mouse work; biogenic magnetite; static-field (SMF) diamagnetic/gradient effects and SMF pain trials; Lorentz/Hall/MHD; B-dependent dose-response, static-bias effects and credibility of microtesla ELF effects; plus a decision-test record contrasting B-driven and E-driven designs.",
       "targets": targets, "new_refs": new_refs,
       "cross_cutting_notes": ""}

out["cross_cutting_notes"] = (
 "1) Decision tests. Designs that discriminate B from dB/dt/E and were run: Liburdy 1992 (Faraday multi-ring plate: Ca2+ influx followed induced E, 1.7 mV/cm = 0.17 V/m at 22 mT 60 Hz; erratum exists); Harland & Liburdy 1997 (MCF-7: B, not E); Fedele 2014 (static = 3 Hz = 50 Hz at 300 uT: B); Prato 2011 (constant B x f: dB/dt-like); Choleris 2002 (static nulling and E screening do not reproduce shielding); Prato 1996 and Blackman 1990 (angle/orientation dependence at fixed amplitude); Ishido 2001 (1.2 uT = 100 uT: saturation, so not dB/dt-scaling). Sherrard 2018's mu-metal and antiparallel-coil controls do NOT discriminate B from E because both remove B and induced E together. "
 "2) Larmor frequency: the brief's '~1.4 MHz/mT' is a unit slip; free-electron Larmor is 28.0 MHz/mT, about 1.26 MHz at 45 uT and 1.4 MHz at 50 uT; 7 MHz RF (Usselman, Ritz) is about 5x the Larmor frequency of the ~45 uT static field. "
 "3) Therapeutic relevance: B-driven mechanisms in this scope operate at much lower B (0.02 uT to 0.5 mT) than typical PEMF peaks (1-50 mT) or need static B0 plus orientation; the radical-pair mT-scale effects (B1/2 = 18 mT) are the one place where PEMF peak fields overlap, but they need light-activated flavin and have not been tested with pulses. "
 "4) Credibility context (not added as refs because not in PubMed; read via fetched summaries): WHO EHC 238 (2007) restates IARC 2B for >0.3-0.4 uT childhood leukaemia and says no accepted mechanism and established acute effects only well above 100 uT via induced E and currents; SCENIHR 2015 (final opinion page) says no mechanisms identified and no experimental support for the leukaemia association. ICNIRP 2010 (existing ref icnirp2010) numbers were taken from a fetched summary of the guideline text. "
 "5) Gaps: Fitzsimmons CMF B_ac/B_dc not retrieved (abstracts only); Hore 2012 comment, Lednev 1995 comment, Liboff 2002 comment and a Russian-language Deriugina 1996 precursor were seen but not added (no abstracts or duplicates of added refs); Dobson 2008 and Kirschvink 1996 (microwave magnetite) were judged out of scope; existing refs hore2016, barnes2015, wang2017, kirschvink1992, adair1991, liboff2009, liboff2010, pall2013, pall2022, weaver1990, gabriel1996, thomas2007 were cited but not re-read in this pass. "
 "6) weintraub2009 (existing, PMID 19577022) is the PEMF diabetic-neuropathy study; the SMF insole RCT added here is Weintraub 2003 (PMID 12736891). "
 "7) Liburdy-lab caution: the 1992 FEBS paper (PMID 1333413) carries an erratum (PMID 10930587, FEBS Lett 478(3):304, 2000), content not seen; the 1993 and 1997 MCF-7 papers share the senior author but were independently supported by Blackman 2001, Ishido 2001 and Girgert 2005/2010.")

with open("/tmp/claude-0/thr/thr_6_B_driven.json", "w", encoding="utf-8") as fh:
    json.dump(out, fh, ensure_ascii=False, indent=1)
print("targets", len(targets), "new_refs", len(new_refs))
