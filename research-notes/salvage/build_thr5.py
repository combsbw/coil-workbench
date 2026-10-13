import json, sys
S = '/tmp/claude-0/-home-claude-coil-workbench/be52d8fd-6910-5673-a281-429468ab8431/scratchpad/'
OUT = '/tmp/claude-0/thr/thr_5_adenosine_immune.json'
db = json.load(open(S + 'db.json'))
existing = {}
for line in open('/tmp/claude-0/thr/existing_refs.tsv', encoding='utf-8').read().splitlines()[1:]:
    p = line.split('\t')
    existing[p[1]] = p[0]


def T(role, endpoint, prep, ev, pmid, refkey, depth, B=None, Bnote='', f=None, wf='', pw=None, burst='',
      exp='', sched='', dbdt=None, dbasis=None, E=None, Ebasis=None, Egeom='', B0=None, note=''):
    return dict(role=role, endpoint=endpoint, preparation=prep, evidence_type=ev, B_pk_mT=B, B_note=Bnote,
                freq_Hz=f, waveform=wf, pulse_width_ms=pw, burst=burst, exposure=exp, schedule=sched,
                dBdt_T_s=dbdt, dBdt_basis=dbasis, E_V_m=E, E_basis=Ebasis, E_geometry=Egeom,
                static_B0_uT=B0, pmid=pmid, refkey=refkey, source_depth=depth, note=note)


def D(pmid, refkey, feat, finding):
    return dict(pmid=pmid, refkey=refkey, design_feature=feat, finding=finding)


FER = 'Ferrara/IGEA exposure system: 14 x 23 cm coils, 1400 turns, 1.3 ms pulse at 75 Hz (~10% duty)'
# computed values (shown in notes):  dB/dt = V/(N*A) = 2.0e-3/(50*pi*(2.5e-3)^2) = 2.04 T/s (probe coil 50 turns, 0.5 cm ID)
DBDT_FER = 2.04
# E dish-scale: (r/2)*dB/dt with r=0.043 m (half of 8.6 cm mean flask side) -> 0.0439 V/m
E_FER = 0.044

targets = []

# ---------------------------------------------------------------- 1
targets.append(dict(
    id='adenosine_A2A_A3_upregulation',
    name='Adenosine A2A / A3 receptor up-regulation (Bmax, cAMP, anti-inflammatory signalling)',
    level='biochemical',
    modalities=['wound/inflammation resolution', 'bone & cartilage repair', 'pain relief', 'neuro-modulation/neuroprotection'],
    driver='unresolved',
    driver_explanation=(
        'Within the Ferrara/IGEA work the receptor-density effect is dose-like in amplitude and exposure time: in human neutrophils 0.2 and 0.5 mT were '
        'insufficient, 1 mT gave a significant A2A increase and 1.5-3.5 mT was a plateau (secondary source: Varani 2017 review of Varani 2002/2003), and in rat cortex '
        '1.5 mT needed about 4 h whereas 3 mT gave the same ~2-fold rise after 2 h (Varani 2012 abstract). Amplitude was varied at fixed 75 Hz and 1.3 ms pulse, so '
        'B and dB/dt (and E) co-vary and the studies cannot separate them; frequency, pulse width and waveform were never varied. '
        'Receptor involvement itself does not seem waveform-specific: an independent group using a PhysioStim-like waveform (3.85 kHz pulses, 10 T/s slew, 4 h/day) found that CRISPR loss of A2A/A3 blunted '
        'PEMF-driven osteoblast differentiation (Kar 2021), but receptor density was not measured there. The A2A/A3 up-regulation literature is essentially one consortium; one independent tendon-cell study '
        'did not reach significance (Colombini 2020).'),
    discriminating_evidence=[
        D('11976268', 'varani2002', 'Amplitude, time and temperature varied at fixed 75 Hz / 1.3 ms; human neutrophils (abstract only; amplitude series via Varani 2017 review)',
          'A2A Bmax 126+-10 -> 215+-15 fmol/mg after 1 h; effect intensity-, time- and temperature-dependent; Kd unchanged. Review: no effect at 0.2-0.5 mT, effect from 1 mT, plateau 1.5-3.5 mT, rise between 30 and 120 min, stable to 240 min.'),
        D('22012856', 'varani2012', 'Amplitude x exposure-time matrix (1.5 vs 3 mT; 2/4/6 h) in rat cortex and cortical neurons (abstract only)',
          'Cortical A2A about doubled at both amplitudes, but 1.5 mT needed 4 h and 3 mT needed 2 h; effect transient in intact organ, constant in isolated membranes (1.9- and 2.2-fold after 2 h). A1 and A2A mRNA unchanged. Verifies the "doubling at 1.5-3 mT" statement (2.0-fold) and shows an amplitude-time trade-off.'),
        D('23741498', 'vincenzi2013', 'Single amplitude (1.5 mT chondrocytes, 2.5 mT osteoblasts), single 24 h duration; probe-coil measurement of induced voltage (full text)',
          'A2A and A3 mRNA/protein/Bmax about 2.1-2.3x, Kd, A1 and A2B unchanged; functional gain in cAMP responses and PGE2/IL-6/IL-8/NF-kB suppression. No amplitude or frequency comparison; but full methods allow dB/dt to be computed.'),
        D('33630907', None, 'Independent group, different waveform (PhysioStim-like, 3.85 kHz, 10 T/s slew, 4 h/day for up to 16 days); CRISPR knock-out/knock-in of Adora2A and Adora3 in MC3T3-E1 (full text)',
          'Adora3 disruption markedly blunted PEMF-induced alkaline phosphatase and several osteoblast genes; Adora2A disruption delayed it and blunted cFos/Pthr1; Adora3 knock-in restored the response. Shows A2A/A3 dependence for a waveform with ~5x the Ferrara dB/dt, but did not measure receptor density; no B value given.'),
        D('32998161', 'colombini2020', 'Independent group, same nominal 1.5 mT / 75 Hz / 10% duty, 48 h, human tendon cells (full text)',
          'A2A Bmax rose 28.7 -> 53.3 fmol/mg (84.4 -> 135.8 with IL-1b) but not significantly; ADORA2A mRNA fell with IL-1b + PEMF (feedback); PGE2 and IL-6 fell only slightly. Partial null or cell-type/duration dependence.'),
        D('42737802', None, 'Independent Korean group, different device (Corefacial), UVB fibroblasts, abstract only',
          'PEMF restored A2AAR/PKA/cAMP and reduced IL-1b/NF-kB/MMP; authors state the data are consistent with but do not prove A2AAR involvement. PEMF parameters not in the abstract.'),
    ],
    thresholds=[
        T('no_effect_below', 'A2A receptor density (Bmax) in human neutrophils', 'Human neutrophils (Varani 2002/2003 as summarised in Varani 2017 review)', 'invitro', '28255202', None, 'fulltext',
          B=0.5, Bnote='Highest amplitude with no significant effect (0.2 and 0.5 mT tested), per review text; peak vs average not specified', f=75, wf='quasi-rectangular pulses (Ferrara/IGEA)', pw=1.3,
          burst='~10% duty', exp='1 h', note='Secondary source (review); primary methods of Varani 2002 not read (abstract only; PMC retrieval blocked). Frequency and pulse width are the Ferrara standard, not verified from the primary paper.'),
        T('lowest_effective', 'A2A receptor density in human neutrophils', 'Human neutrophils', 'invitro', '28255202', 'varani2002', 'fulltext',
          B=1.0, Bnote='Reported amplitude per review; peak vs mean not specified', f=75, wf='quasi-rectangular pulses (Ferrara/IGEA)', pw=1.3, burst='~10% duty', exp='30-120 min (rise); elevated by 90 min, stable to 240 min',
          dbdt=1.36, dbasis='computed', Egeom='not computed (neutrophil suspension geometry unknown)',
          note='dB/dt computed ONLY by linear scaling of the measured 2.04 T/s at 1.5 mT (same coil/waveform assumed): 1.0/1.5 x 2.04 = 1.36 T/s. Primary-paper dose-response data not read.'),
        T('plateau', 'A2A receptor density in human neutrophils', 'Human neutrophils', 'invitro', '28255202', 'varani2002', 'fulltext',
          B=1.5, Bnote='Lower edge of the 1.5-3.5 mT plateau (upper edge 3.5 mT), per review text', f=75, wf='quasi-rectangular pulses (Ferrara/IGEA)', pw=1.3, burst='~10% duty', exp='1-4 h',
          dbdt=2.04, dbasis='computed', note='Computed from the 1.5 mT Vincenzi 2013 probe-coil measurement (2.04 T/s); 3.5 mT would scale to ~4.8 T/s if the waveform is unchanged (computed, not reported). Two-fold receptor density went with ~4-fold agonist potency gain and enhanced superoxide inhibition (review).'),
        T('lowest_effective', 'A2A Bmax ~2-fold in intact rat cerebral cortex', 'Rat cortex (intact tissue) and cortical neurons', 'animal', '22012856', 'varani2012', 'abstract_only',
          B=1.5, Bnote='Amplitude as stated in abstract; peak vs mean not specified', f=None, wf='pulsed (Ferrara system; frequency/pulse width not stated in the abstract)', exp='4 h (2.0-fold in intact cortex); 6 h 1.4- to 1.8-fold',
          note='At 1.5 mT the effect needed ~4 h. Effect was transient in the whole organ. Isolated membranes: 1.9-fold after 2 h at 1.5 mT, constant thereafter.'),
        T('plateau', 'A2A Bmax in rat cortex/cortical neurons', 'Rat cortex and cortical neurons', 'animal', '22012856', 'varani2012', 'abstract_only',
          B=3.0, Bnote='Amplitude as stated in abstract', f=None, wf='pulsed (Ferrara system; frequency/pulse width not stated in the abstract)', exp='2 h (2.0- and 2.2-fold); 4 h 1.6- and 1.9-fold',
          note='Same ~2-fold ceiling reached in half the time at 2x the amplitude; effect declines with longer exposure in whole organ (1.6- to 1.9-fold at 4 h).'),
        T('optimal', 'A2A and A3 Bmax ~2.1-2.3x, cAMP and PGE2/IL-6/IL-8 modulation', 'T/C-28a2 human chondrocytes', 'invitro', '23741498', 'vincenzi2013', 'fulltext',
          B=1.5, Bnote='1.5 +- 0.1 mT, measured in air with a Hall probe (+-1% uniformity); peak', f=75, wf='quasi-rectangular / near-triangular pulse (edge ~0.74 ms implied)', pw=1.3, burst='duty ~10%',
          exp='24 h', dbdt=DBDT_FER, dbasis='computed',
          E=E_FER, Ebasis='computed', Egeom='Dish/flask-scale peak E at the edge: (r/2)*dB/dt with r = 0.043 m (flask 9.2 x 8.2 cm, Merighi 2024), field assumed normal to the monolayer; NOT cell-scale',
          note='Operating point, not a determined optimum: only one amplitude/duration was tested. Computed dB/dt = V/(N*A) = 2.0e-3 V /(50 x pi x (2.5e-3 m)^2) = 2.04 T/s from the reported induced voltage 2.0+-0.5 mV in a 50-turn, 0.5 cm ID probe coil. 1.5 mT / 2.04 T/s implies an edge time ~0.74 ms.'),
        T('optimal', 'A2A and A3 Bmax ~2.2-2.4x', 'hFOB 1.19 human osteoblasts', 'invitro', '23741498', 'vincenzi2013', 'fulltext',
          B=2.5, Bnote='2.5 +- 0.2 mT, Hall probe in air; peak', f=75, wf='quasi-rectangular pulses', pw=1.3, burst='duty ~10%', exp='24 h',
          dbdt=3.4, dbasis='computed', note='dB/dt scaled linearly from the 1.5 mT measurement (2.5/1.5 x 2.04 = 3.4 T/s) because the induced voltage was reported for the 2.0 mV set-up only; the exact coil setting for the osteoblast voltage is not separately stated. Only one amplitude tested.'),
        T('lowest_effective', 'A2A Bmax and IL-1b-potentiated A2A (664-708 fmol/mg) with cAMP, PGE2, IL-6, IL-8 modulation', 'Chondrocytes and osteoblasts +- IL-1b 1 ng/ml (48 h)', 'invitro', '23741498', 'vincenzi2013', 'fulltext',
          B=1.5, f=75, wf='pulsed', pw=1.3, exp='24 h', note='PEMF plus IL-1b raised A2A Bmax to 664+-56 (chondrocytes) and 708+-62 (osteoblasts) fmol/mg: potentiation of the inflammatory-induced receptor expression.'),
        T('loss_above', 'A2A receptor density (not significant) and mRNA (down-regulated with IL-1b)', 'Human tendon cells +- IL-1b', 'invitro', '32998161', 'colombini2020', 'fulltext',
          B=1.5, Bnote='Nominal; not independently confirmed by me', f=75, wf='pulsed, 10% duty (coils 1000 turns)', exp='48 h',
          note='Not a threshold: the only non-significant Bmax change at the nominal Ferrara dose. Possible duration (48 h, feedback down-regulation of ADORA2A mRNA) or tendon-cell dependence. The paper cites 8-12 h as dose-dependent exposures in tendon cells.'),
        T('lowest_effective', 'Neuroprotection / ROS reduction via A2A-linked pathways', 'N9 microglia, SH-SY5Y, PC12', 'invitro', '39684558', 'merighi2024', 'fulltext',
          B=1.5, Bnote='1.5 +- 0.2 mT; peak', f=75, wf='pulsed', pw=1.3, burst='duty 0.1', exp='4-72 h; N9 microglia 24 h reduced ROS by 33-39%; 90 min preserved mitochondrial membrane potential',
          note='Protection of SH-SY5Y viability appeared only 6 h after a 24 h exposure.'),
    ],
    window_summary=('Receptor up-regulation: threshold ~1 mT (neutrophils; 0.2-0.5 mT ineffective), plateau 1.5-3.5 mT at 75 Hz / 1.3 ms; exposure must be at least 30-120 min in neutrophils and 2-4 h in rat cortex; common operating point 1.5-2.5 mT, 24 h. '
                    'Computed dB/dt at 1.5 mT ~2.0 T/s (from a measured 2.0 mV probe voltage); dish-scale E ~0.04 V/m (computed). No frequency, pulse-width or dB/dt comparison exists.'),
    replication_status='Essentially a single consortium (Ferrara/Borea/Varani/Vincenzi/Gessi/Merighi with IGEA co-authors); independent support partial (Colombini 2020 not significant; Kar 2021 functional dependence only; Byun 2026 abstract-level). No independent null of Bmax found in PubMed searches.',
    confidence='medium',
    caveats=('Varani 2002 and Yap 2019 primary methods could not be read (Europe PMC rate-limited). Neutrophil dose-response numbers are from a review. Rat cortex frequency/pulse width not in abstract. '
             'Peak vs mean B not specified in the abstracts. Computed dB/dt relies on one probe-coil voltage and an assumed uniform scaling; E is dish-scale only and orientation of the coil to the monolayer is ambiguous.')))

# ---------------------------------------------------------------- 2
targets.append(dict(
    id='nfkb_cytokine_prostaglandin_axis',
    name='NF-kB / TNF-a / IL-1b / IL-6 / PGE2 / COX-2 anti-inflammatory axis',
    level='cellular',
    modalities=['wound/inflammation resolution', 'pain relief', 'bone & cartilage repair'],
    driver='unresolved',
    driver_explanation=(
        'Anti-inflammatory effects are reported over a very wide range: 4 uT at 5 Hz (Selvam), 1 mT at 50 Hz (Vianale), 1.5 mT at 75 Hz pulses (Ferrara) and ~4 mT square wave at 5-8 Hz (Ross), '
        'while the same readouts go the other way at 0.8-1 mT sine 50-60 Hz in macrophages (Kim 2017, Frahm 2006). The only within-study frequency comparison (Ross 2013, ~4 mT, 5-30 Hz) found effect at 5.1-7.8 Hz and none at 10.8 Hz and above at fixed amplitude, i.e. a frequency window that does not scale with dB/dt (dB/dt rises with f). '
        'No study varied B and dB/dt independently in these readouts. The best candidates for the discriminating variable are frequency/pulse pattern (Ross; Chen 2021) and amplitude windows (Wang 2017; Sukumar 2026), but each rests on single groups.'),
    discriminating_evidence=[
        D('23576877', 'ross2013', 'Frequency series 5.1-30 Hz at fixed ~4 mT, 50% duty square wave, 1 h, LPS-challenged RAW264.7 (full text)',
          '5.1 and 7.8 Hz: TNF-a about -37%; 5.1 Hz: NF-kB about -60%; 10.8, 15.6, 20.8, 23.4 and 30 Hz: no effect. Effect does not increase with dB/dt: window at lowest frequencies. Edge time not reported so dB/dt not computable.'),
        D('26151161', None, '5 Hz vs 13 Hz comparison in CHO mu-opioid cells (abstract only)',
          '5 Hz stimulated a cAMP reduction larger than morphine (+23%), 13 Hz behaved like control. Supports narrow low-frequency window; same group.'),
        D('17537462', 'selvam2007', 'In vivo adjuvant arthritis, 4 uT at 5 Hz, 90 min (abstract only)',
          'Lymphocyte PMCA activity and intracellular Ca2+ restored and PGE2 reduced at microtesla amplitude; indicates effects far below the mT regime (dB/dt computed ~1.3e-4 T/s).'),
        D('18410412', 'vianale2008', '1 mT, 50 Hz sine in HaCaT, 1 h and 72 h (abstract only)',
          'NF-kB p65 nearly undetectable after 1 h; RANTES/MCP-1/MIP-1a/IL-8 down after 72 h; cell growth up at 48 h.'),
        D('28370033', None, '0.8 mT, 60 Hz in RAW264.7 (abstract only)',
          'Opposite polarity: NO, TNF-a, IL-1b, IL-6 up, NF-kB nuclear translocation, NFAT2 and Ca2+ influx up; antioxidant treatment worsened it. Inverse effect at B similar to Vianale.'),
        D('16598759', None, '50 Hz, 1.0 mT; 0.05-1.0 mT for free radicals (abstract only)',
          'IL-1b 12.3-fold at 24 h, phagocytosis 1.6-fold at 45 min; free-radical formation significant at all tested flux densities 0.05-1.0 mT (45 min).'),
        D('25199571', 'taylor2015', 'Human post-operative dosing comparison (abstract only)',
          'Q4 (20 min per 4 h) and Q2 (15 min per 2 h) schedules worked, a 5 min per 20 min schedule did not: schedule matters, more frequent short exposures lost the effect. Device parameters not given in abstract.'),
        D('18640059', None, '75 Hz, 1.5 mT, 24 h, bovine synovial fibroblasts +- adenosine deaminase (abstract)',
          'EMF lowered TNF-a/LPS-stimulated PGE2 and COX-2; the EMF effect was lost when endogenous adenosine was removed with adenosine deaminase -> adenosine-dependent.'),
    ],
    thresholds=[
        T('lowest_effective', 'TNF-a (-37%) and NF-kB (-60% at 5.1 Hz)', 'RAW264.7 + LPS, Helmholtz coils 14 cm diameter, 2400 turns', 'invitro', '23576877', 'ross2013', 'fulltext',
          B=4.0, Bnote='Reported "about 40 G" = 4 mT; waveform amplitude (square wave), peak assumed', f=5.1, wf='square wave, 50% duty', exp='1 h', sched='single exposure, cells challenged with LPS (3 h pre-challenge)',
          dbdt=None, dbasis=None, note='Edge time not reported, so dB/dt and E left null. 7.8 Hz also effective for TNF-a.'),
        T('loss_above', 'TNF-a / NF-kB suppression disappears', 'RAW264.7 + LPS', 'invitro', '23576877', 'ross2013', 'fulltext',
          B=4.0, f=10.8, wf='square wave, 50% duty', exp='1 h', note='No effect at 10.8, 15.6, 20.8, 23.4 or 30 Hz at the same amplitude (frequency window, not an amplitude window).'),
        T('lowest_effective', 'PMCA activity, lymphocyte Ca2+, PGE2 in adjuvant arthritis', 'Rats with adjuvant arthritis', 'animal', '17537462', 'selvam2007', 'abstract_only',
          B=0.004, Bnote='4 uT as given in abstract; peak vs rms not stated', f=5, wf='not stated', exp='90 min',
          dbdt=1.26e-4, dbasis='computed', note='Computed assuming a sine wave with 4 uT as peak: dB/dt = 2*pi*5*4e-6 = 1.26e-4 T/s. If 4 uT is rms multiply by 1.41. Waveform unknown, so treat as a lower bound only.'),
        T('optimal', 'NF-kB p65 down (1 h), chemokines down (72 h), growth up (48 h)', 'HaCaT keratinocytes', 'invitro', '18410412', 'vianale2008', 'abstract_only',
          B=1.0, Bnote='1 mT as stated; peak vs rms not stated', f=50, wf='sinusoidal (50 Hz ELF)', exp='1 h to 72 h',
          dbdt=0.314, dbasis='computed', note='Computed assuming 1 mT is sine peak: 2*pi*50*1e-3 = 0.314 T/s. Operating point; no amplitude comparison.'),
        T('optimal', 'PGE2 and COX-2 inhibition (TNF-a/LPS stimulated)', 'Bovine synovial fibroblasts', 'invitro', '18640059', None, 'abstract_only',
          B=1.5, f=75, wf='pulsed (Ferrara system)', exp='24 h', dbdt=2.04, dbasis='computed',
          note='dB/dt borrowed from the 1.5 mT measurement in Vincenzi 2013 (same group/coil design), not measured in this paper.'),
        T('lowest_effective', 'PGE2, IL-6, IL-8 down, IL-10 up', 'Human OA synovial fibroblasts + IL-1b', 'invitro', '21830213', None, 'abstract_only',
          note='Amplitude, frequency and duration not stated in the abstract; Ferrara system.'),
        T('lowest_effective', 'IL-1b in CSF (up to 10-fold lower at 6 h)', 'Rat traumatic brain injury', 'animal', '22503903', 'rasouli2012', 'abstract_only',
          note='B and frequency not given in the abstract.'),
        T('loss_above', 'Post-operative pain/narcotic benefit lost with 5 min per 20 min schedule', 'Human post-operative patients', 'human_rct', '25199571', 'taylor2015', 'abstract_only',
          exp='5 min every 20 min failed; 20 min per 4 h and 15 min per 2 h worked', sched='VAS at 24 h 87% (failed) vs 74% of the 1 h value (effective)',
          note='Schedule-dependence (too-frequent short exposure lost the effect); B and frequency not given in the abstract.'),
        T('adverse', 'Pro-inflammatory activation: NO, TNF-a, IL-1b, IL-6, NF-kB nuclear translocation, NFAT2, Ca2+ influx', 'RAW264.7 macrophages', 'invitro', '28370033', None, 'abstract_only',
          B=0.8, Bnote='0.8 mT as stated; peak vs rms not stated', f=60, wf='sinusoidal ELF', dbdt=0.302, dbasis='computed', note='Computed assuming sine peak: 2*pi*60*0.8e-3 = 0.302 T/s.'),
        T('adverse', 'IL-1b release 12.3-fold (24 h), phagocytosis 1.6-fold (45 min), free radicals (0.05-1.0 mT, 45 min)', 'Mouse macrophages', 'invitro', '16598759', None, 'abstract_only',
          B=1.0, Bnote='1.0 mT as stated; free radical rise also at 0.05 mT', f=50, wf='sinusoidal ELF', exp='45 min to 24 h', dbdt=0.314, dbasis='computed',
          note='Computed assuming sine peak 1.0 mT. Apparently no genotoxicity (micronuclei unchanged at 12-48 h).'),
    ],
    window_summary=('Anti-inflammatory window is frequency/pattern-specific rather than a clear B or dB/dt window: effective at 5-8 Hz (~4 mT square wave), 50 Hz sine (1 mT), 75 Hz pulses (1.5 mT) and 5 Hz at 4 uT, but pro-inflammatory with 50-60 Hz sine at 0.8-1 mT in macrophages. '
                    'Computed sine dB/dt of the effective and adverse cases overlaps (0.3 T/s), so dB/dt alone does not separate them.'),
    replication_status='Mixed: several groups report suppression (Ross, Vianale, Ferrara, Selvam) with different devices, but each parameter set is single-lab; contradictory pro-inflammatory results from independent labs (Kim 2017, Frahm 2006).',
    confidence='low',
    caveats=('Most records abstract-only. Rohde 2015 (exudate IL-1b 5-fold higher in sham at 24 h; pain 2x at 5 h and 4x at 72 h) and Taylor 2015 do not give device parameters in the abstracts; device type not verified. '
             'Peak vs rms of ELF sine amplitudes not specified in several abstracts.')))

# ---------------------------------------------------------------- 3
targets.append(dict(
    id='macrophage_polarisation_amplitude_pattern',
    name='Macrophage M1/M2 polarisation (including inverse, pro-inflammatory effects)',
    level='cellular',
    modalities=['wound/inflammation resolution', 'bone & cartilage repair', 'muscle/tendon recovery'],
    driver='waveform_spectral',
    driver_explanation=(
        'Chen 2021 compared 22 blinded fields at near-identical fundamental frequency (51.8 vs 52.3 Hz) and amplitude (6-282 uT at 6 mm) and found that the send/pause pulse-burst pattern flipped M1 vs M2 outcomes, '
        'which cannot be explained by B or by dB/dt computed from the fundamental alone. Amplitude windows are additionally suggested: Sukumar 2026 (pulse barrage, 0-3 mT) found maximal M1 activation at 3 mT after one 10-min exposure whereas earlier work at uT-1.5 mT was anti-inflammatory; '
        'Wang 2017 (15 Hz, 0.5-3 mT) found opposite effects on osteoclast-lineage RAW264.7 cells at 0.5 and 3 mT. Each is a single lab, and none separates B from dB/dt.'),
    discriminating_evidence=[
        D('34821733', None, '22 blinded fields (Somagen), B 6-282 uT, fundamental 3.3-90.6 Hz, 7 or 30 min, PBMC-derived macrophages (full text)',
          'Field A (51.8 Hz) M1-like (pSTAT1 x2.9, CD86 x2.0, ROS x1.4); field B (52.3 Hz) M2-like (arginase x2.6); differ in send-pause burst pattern, not in fundamental or amplitude. Extending 7 to 30 min did not raise marker effects, but cytokine secretion did.'),
        D('42549352', 'sukumar2026', 'Amplitude series 0, 0.5-3 mT drive, 15 Hz pulse barrage, single 10 min, 24 h read-out; TRPC1 and aminoglycoside/SKF-96365/2-APB blockers (full text)',
          '3 mT (vs 0 and 2 mT) gave strongest M1 markers (iNOS, CD86 up; PPAR-gamma, arginase down) in RAW264.7 and BMDM and repolarised IL-4 M2 cells; blocked by TRPC1 inhibitors. In vivo 4T1 tumours: 3 mT, 30 min twice weekly, 3 of 4 mice tumour free at 2 weeks (n=4).'),
        D('28741320', None, 'Intensity series 0.5/1/2/3 mT at 15 Hz, 2 h/day for 7 days, RAW264.7 + RANKL (abstract)',
          '0.5 mT inhibits osteoclast formation and resorption, 3 mT enhances resorption via apoptosis (BAX up): an explicit intensity window with opposite sign.'),
        D('32596310', None, 'In vivo synovitis mice (DMM, air pouch), 1.5 mT, 75 Hz, 10% duty (abstract)',
          'Reduced IL-1b/TNF-a, fewer neutrophils, more macrophages; enhanced efferocytosis with p38 phosphorylation inhibited.'),
        D('32751697', None, 'Co-culture human tendon cells (IL-1b primed) and macrophages, parameters from earlier work (abstract only)',
          'PEMF favoured a pro-regenerative macrophage phenotype and anti-inflammatory mediators, possibly via FAK signalling.'),
    ],
    thresholds=[
        T('lowest_effective', 'M1-like activation (CD86 x2.0, pSTAT1 x2.9, ROS x1.4)', 'PBMC-derived human macrophages', 'invitro', '34821733', None, 'fulltext',
          B=0.282, Bnote='Up to 282 uT as the maximum of the 22-field set at 6 mm; per-field amplitude for field A not separately recorded by me', f=51.8, wf='burst/pulse pattern with fundamental 51.8 Hz (not sinusoidal)', burst='send-pause pattern (details in paper)', exp='7 or 30 min',
          dbdt=0.092, dbasis='computed', note='Computed upper bound as a sine-equivalent: 2*pi*52*282e-6 = 0.092 T/s; the actual waveform is non-sinusoidal so true dB/dt can be higher. Field B at 52.3 Hz gave an M2-like profile.'),
        T('optimal', 'Maximal M1 markers (iNOS, CD86), repolarisation of IL-4 M2 cells', 'RAW264.7 and BMDM', 'invitro', '42549352', 'sukumar2026', 'fulltext',
          B=3.0, Bnote='3 mT drive amplitude; 2 mT and 0 mT comparators', f=15, wf='pulse barrage: 20 x 150 us on/off pulses repeated for 6 ms, ~50 us rise to maximum', pw=0.15, burst='20 pulses per 6 ms barrage at 15 Hz', exp='single 10 min', sched='read-out at 24 h; NF-kB biphasic at 0.5 and 4 h',
          dbdt=17, dbasis='reported', note='Reported "~17 T/s" for 0.5-3 mT drive amplitudes; but 3 mT/50 us = 60 T/s and 1.5 mT/50 us = 30 T/s (computed), so the reported value is inconsistent with the stated rise time; flagged. E not reported.'),
        T('lowest_effective', 'Anti-inflammatory vs pro-inflammatory crossover', 'RAW264.7 macrophages (cross-study)', 'invitro', '42549352', 'sukumar2026', 'fulltext',
          B=1.5, Bnote='Paper states prior macrophage work in uT to 1.5 mT range was anti-inflammatory (narrative); not a measured crossover in one study', f=15, exp='10 min',
          note='Placeholder for the amplitude polarity inversion; not independently measured. 2 mT was weaker than 3 mT.'),
        T('lowest_effective', 'Osteoclast formation and resorption inhibition', 'RAW264.7 + RANKL', 'invitro', '28741320', None, 'abstract_only',
          B=0.5, f=15, wf='pulsed', exp='2 h/day for 7 days', dbdt=None, dbasis=None, note='Waveform and edge time not given in the abstract.'),
        T('adverse', 'Osteoclast apoptosis (BAX up), enhanced resorption at high amplitude', 'RAW264.7 + RANKL', 'invitro', '28741320', None, 'abstract_only',
          B=3.0, f=15, wf='pulsed', exp='2 h/day for 7 days', note='Opposite sign from 0.5 mT; 1 and 2 mT not detailed in the abstract.'),
        T('optimal', 'Efferocytosis up, IL-1b/TNF-a down, synovitis score down', 'C57BL/6 mice DMM synovitis and air pouch', 'animal', '32596310', None, 'abstract_only',
          B=1.5, f=75, wf='pulse waveform', burst='10% duty', dbdt=2.04, dbasis='computed',
          note='dB/dt borrowed from the Ferrara 1.5 mT measurement; waveform shape per abstract only "pulse waveform".'),
    ],
    window_summary='Polarity depends on pulse pattern and amplitude: M2/anti-inflammatory with uT-1.5 mT and 5-75 Hz stimuli, M1 with a 3 mT, 15 Hz pulse barrage (reported ~17 T/s, computed 30-60 T/s) and with certain 52 Hz burst patterns at <=282 uT. Not a B or dB/dt window.',
    replication_status='Single groups for each pattern (Chen/Somagen; Sukumar/NUS; Wang/China); contradictory polarity between labs is the norm.',
    confidence='low',
    caveats='Inverse (pro-inflammatory) effects are context dependent (tumour/infection vs injury). The Sukumar 4T1 result has n=4. Phase 1 cancer-patient safety statement is from the paper, not independently verified.'))

# ---------------------------------------------------------------- 4
targets.append(dict(
    id='trpc1_ca_pgc1a_mitochondria',
    name='TRPC1-Ca2+-(calcineurin/NFAT, PCAF)-PGC-1a mitochondrial biogenesis (magnetic mitohormesis)',
    level='membrane/ion channel',
    modalities=['muscle/tendon recovery', 'bone & cartilage repair', 'wound/inflammation resolution'],
    driver='combined',
    driver_explanation=(
        'The response is brief and low-dose (single 10 min, 1-1.5 mT pulses at 15 Hz in Franco-Obregon group studies) and is blocked by TRPC1 knock-down or aminoglycosides. Evidence against a purely induction-driven mechanism comes from the same group: '
        'downward-directed fields outperform upward-directed ones (Wong 2022), and the response is lost with growth in the dark, magnetic shielding or upward fields (Iversen 2025, CRY2-TRPC1 axis). Both point to a vector/orientation and light-linked (radical-pair-type) component. '
        'The authors also say pulses are chosen for clinically tolerable repeated delivery; the rationale for pulses is stated as "unclear" in the harmonisation review, with rise time, symmetry and direction seldom reported. '
        'The device reports are internally inconsistent about 1 vs 1.5 mT. B vs dB/dt was never separated by varying frequency at fixed B.'),
    discriminating_evidence=[
        D('31518158', 'yap2019', 'Single 10 min exposure, 1.5 mT amplitude; CRISPR TRPC1 knock-down, TRPM7 siRNA, aminoglycoside block, ambient-field deprivation (abstract only)',
          'TRPC1-mediated Ca2+ entry, NFAT, PCAF and PGC-1a up; mitochondrial respiration up; TRPC1 knock-down abolished it, TRPM7 siRNA did not; removing ambient field lowered TRPC1 expression.'),
        D('35841726', None, 'Directionally specific field (downward vs upward), 1.5 mT, 10 min (abstract)',
          'Downward-directed field produced a greater secretome/EV response and TRPC upregulation than upward-directed; streptomycin blocked; direct exposure caused mild oxidative stress.'),
        D('39937022', None, 'Dark growth, magnetic shielding, field direction and CRY2 (abstract)',
          'Sensitivity depends on light and CRY2, and is lost with shielding or upward-directed field: vector and radical-pair-type involvement, not dB/dt alone.'),
        D('32875708', None, 'Cell-derived vesicles with and without TRPC1 knock-down (abstract)',
          'Vesicles carrying TRPC1 respond to PEMF with TRPC1-mediated Ca2+ entry; knock-down vesicles do not and can transfer responsiveness to recipient cells.'),
        D('39061719', None, 'Concurrent optical and magnetic stimulation (abstract)',
          'Magnetic plus light: supra-additive proliferation, lower ROS, higher ATP; aminoglycosides block.'),
        D('36262374', 'stephenson2022', 'Randomised pilot ACLR (n=10 vs 10), 1 mT peak, 10 min weekly for 16 weeks (full text)',
          '31P-MRS Pi/PCr, (Pi+PCr)/ATP, PDE/ATP improved and ceramides fell; discussion acknowledges magnetically induced oxidative stress could be harmful in inflamed, surgically injured tissue and a small developmental depression under direct exposure.'),
        D('37892906', None, 'Narrative review of efficacy windows (full text)',
          'States that low oxidative stress (lower amplitude, frequency or duration) gives the beneficial response and higher doses the opposite; 1.5 mT/10 min for myogenesis vs 3 mT/60 min for cancer-cell killing; potency lower if exposure is applied after log-phase expansion.'),
    ],
    thresholds=[
        T('lowest_effective', 'TRPC1-Ca2+-PGC-1a activation, mitochondriogenesis, respiration', 'C2C12 myoblasts', 'invitro', '31518158', 'yap2019', 'abstract_only',
          B=1.5, Bnote='Amplitude stated as 1.5 mT; the device is described elsewhere as "1 mT @ 15 Hz", so amplitude is uncertain', f=15, wf='pulse barrage per Sukumar 2026 device description: 20 x 150 us on/off pulses repeated for 6 ms, ~50 us rise', pw=0.15,
          exp='single 10 min', dbdt=30, dbasis='computed',
          note='Computed 1.5 mT/50 us = 30 T/s only if the device waveform is the one described in Sukumar 2026 (assumption, not shown for Yap 2019). Full text not read.'),
        T('optimal', 'Myogenesis / mitochondria / PGC-1a', 'Mouse in vivo', 'animal', '32627872', None, 'abstract_only',
          B=1.5, Bnote='1.5 mT as stated', f=15, wf='per group device', exp='10 min', sched='weekly; 6 weeks (with exercise) to >4 months',
          note='Pgc-1a up after 2 months alone; oxidative muscle and fatty-acid oxidation after >4 months. Exercise alone did not raise Pgc-1a in 6 weeks.'),
        T('optimal', 'Human mitochondrial energetics (31P-MRS), ceramides', 'ACL reconstruction patients (pilot RCT)', 'human_rct', '36262374', 'stephenson2022', 'fulltext',
          B=1.0, Bnote='1 mT peak', f=15, wf='per Franco-Obregon device', exp='10 min', sched='weekly x 16 weeks',
          note='n=10 per arm; no dB/dt reported.'),
        T('loss_above', 'Myogenic potency reduced / oxidative stress emerges', 'Myoblasts', 'invitro', '37892906', None, 'fulltext',
          note='Review states that higher amplitude, frequency or duration shifts the response toward oxidative stress; and that 3 mT/60 min kills cancer cells. No numeric dose-response within one study; potency is lost when exposure is applied after log-phase expansion.'),
        T('adverse', 'Mild oxidative stress with direct exposure', 'Myoblasts', 'invitro', '35841726', None, 'abstract_only',
          B=1.5, f=15, exp='10 min', note='Directly exposed cells show mild oxidative stress while conditioned medium does not.'),
        T('lowest_effective', 'Metabolic benefit in humans', 'Type 2 diabetes patients (40 adults)', 'human_other', '41010617', None, 'abstract_only',
          exp='10 min per visit, alternate legs, 12 weekly sessions', note='No overall HbA1c/glucose/HOMA-IR change; subgroup with central obesity improved (HbA1c 7.5 -> 7.1%). B not given in the abstract. Well tolerated, no adverse events.'),
    ],
    window_summary='Brief (10 min) exposures at ~1-1.5 mT, 15 Hz pulses, weekly; direction-, light- and TRPC1-dependent. More exposure (3 mT/60 min) or later-phase exposure reverses the benefit in the same literature (review-level). Computed dB/dt of the device is 30-60 T/s if the 50 us rise applies; not independently verified.',
    replication_status='Single group (Franco-Obregon, NUS; Iversen/Yap/Sukumar/Wong), with external TRPC/CRY-related biophysics unproven; small human pilots; the T2DM study was mostly null overall.',
    confidence='low',
    caveats='Yap 2019 full text not read (blocked); the 1.0 vs 1.5 mT inconsistency; rise time is borrowed from Sukumar 2026. Stephenson 2022 is a pilot with n=10 per arm.'))

# ---------------------------------------------------------------- 5
targets.append(dict(
    id='mitochondria_ros_redox_other_labs',
    name='Mitochondrial function, ROS and antioxidant (MnSOD) adaptation: other labs',
    level='cellular',
    modalities=['neuro-modulation/neuroprotection', 'wound/inflammation resolution'],
    driver='unresolved',
    driver_explanation=(
        'Independent labs report adaptive antioxidant (MnSOD) induction and reduced ROS after repeated short PEMF exposures (Osera 2015, Falone 2016), reduced ROS with maintained mitochondrial membrane potential (Merighi 2024) '
        'and dose-dependent mitochondrial effects with exposure time (Ivanov 2026). A 30 kHz sine-burst device showed ATP-synthesis-linked respiration stimulation but failed to rescue NO-inhibited respiration (Zavadskis 2026). Another group found a shift from mitochondrial respiration to glycolysis at 4 mT and 80 Hz (Liao 2025). '
        'There is no B vs dB/dt discrimination; the data are of the exposure-time (dose) type.'),
    discriminating_evidence=[
        D('42078208', None, 'Exposure time series, 1 vs 5 min/h for 10 nights, broadband pulsed device (abstract)', 'Antioxidant potential +8% (n.s.) at minimum exposure vs +20.6% at maximum; thymocyte mitochondrial fluorescence +29% at the maximum only: dose-dependent.'),
        D('41618092', None, 'Cultures, homogenates and isolated mitochondria; 1 ms, 30 kHz sine burst (abstract)', 'ATP-synthesis-linked respiration selectively stimulated; no rescue of NO-inhibited respiration; blue light did rescue.'),
        D('39939866', None, 'L929 fibroblasts, 4 mT, 80 Hz (abstract)', 'Migration/viability up, shift to glycolysis, low ROS; vesicular transport up.'),
        D('26940444', None, '2 mT, 75 Hz, 15 min x 3 over 5 days, SK-N-BE(2) (abstract)', 'MnSOD-based protection up and ROS down after H2O2 challenge.'),
        D('25708841', None, '10 min x 4 per week (40 min total), SH-SY5Y (abstract)', 'MnSOD activity up and ROS down after 30 min H2O2; B not stated in the abstract.'),
        D('40575091', None, '10 uT oscillating field at 12-33 Hz on a 45 uT static field, HT-1080 cells (abstract)', 'Proliferation accelerated or inhibited depending on frequency near 16.5 Hz and a 0.5 Hz or 250 nT shift: radical-pair-type sensitivity; weak-field regime.'),
    ],
    thresholds=[
        T('lowest_effective', 'MnSOD activity up, ROS down after H2O2', 'SH-SY5Y human neuroblastoma', 'invitro', '25708841', None, 'abstract_only',
          exp='4 x 10 min per week (40 min total)', note='Amplitude and frequency not in the abstract.'),
        T('optimal', 'MnSOD-based protection up, ROS down', 'SK-N-BE(2) drug-resistant neuroblastoma', 'invitro', '26940444', None, 'abstract_only',
          B=2.0, Bnote='2 mT as stated; peak vs average not stated', f=75, wf='pulsed', exp='15 min', sched='3 sessions over 5 days',
          dbdt=None, dbasis=None, note='Waveform and pulse width not in abstract.'),
        T('optimal', 'Wound-model energy metabolism shift, migration, low ROS', 'L929 fibroblasts', 'invitro', '39939866', None, 'abstract_only',
          B=4.0, Bnote='4 mT as stated', f=80, wf='pulsed', note='"Specific parameter" 4 mT, 80 Hz; exposure time not in abstract.'),
        T('lowest_effective', 'Thymocyte mitochondrial fluorescence (+29%), plasma antioxidant potential (+20.6%)', 'BALB/c mice (60 animals, 5 groups)', 'animal', '42078208', None, 'abstract_only',
          exp='5 min/h for 10 nights (maximum); 1 min/h gave +8% (n.s.)', note='Broadband weak pulsed device (TOR); B not in abstract.'),
        T('plateau', 'ATP-synthesis-linked respiration up; no rescue of NO-inhibited respiration', 'Cells, homogenates, isolated mitochondria', 'invitro', '41618092', None, 'abstract_only',
          f=30000, wf='1 ms, 30 kHz sine wave per pulse', pw=1.0, note='Independent mitochondria study with a very different waveform; B not in abstract.'),
        T('lowest_effective', 'Growth modulation by 10 uT oscillating field', 'HT-1080 fibrosarcoma cells', 'invitro', '40575091', None, 'abstract_only',
          B=0.01, Bnote='10 uT (as stated)', f=16.5, wf='oscillating magnetic field on 45 uT static field', B0=45,
          dbdt=1.04e-3, dbasis='computed', note='Computed 2*pi*16.5*10e-6 = 1.04e-3 T/s assuming a sine of 10 uT peak. Frequency shifts of 0.5 Hz or field change of 250 nT altered the sign of the effect.'),
    ],
    window_summary='Repeated short exposures (10-15 min) at 2 mT/75 Hz and brief weekly 1-1.5 mT/15 Hz exposures both give antioxidant adaptation; time-dependence (Ivanov) and weak-field frequency sensitivity (Bajtos) are the only discriminating hints.',
    replication_status='Independent labs exist (Osera/Falone, Liao, Zavadskis, Ivanov) but with non-matching parameters; no direct replication. Searches for Calabro, Gualdi and Kuhn mitochondrial PEMF papers returned no PubMed hits and were not included.',
    confidence='low',
    caveats='All abstract-only. Zavadskis 2026 and Ivanov 2026 are recent single reports.'))

# ---------------------------------------------------------------- 6
targets.append(dict(
    id='immune_cell_ca_signalling',
    name='Immune-cell Ca2+ signalling (lymphocytes/Jurkat, thymocytes; calcineurin/NFAT)',
    level='membrane/ion channel',
    modalities=['wound/inflammation resolution'],
    driver='dBdt_E',
    driver_explanation=(
        'Liburdy 1992 is the cleanest B vs E discrimination in this scope: using a multi-ring annular culture plate based on Faraday induction, thymocyte Ca2+ influx (plateau phase of mitogen signalling) depended on the induced E at constant B, '
        'and a pure 60 Hz E-field matched a magnetically induced E-field of the same strength. Independent replication of 50 Hz Jurkat Ca2+ oscillations (Lindstrom 1993 at 0.1 mT) is mixed: Mattsson 2001 found a weaker response in Jurkat cells from three sources, '
        'and a blinded multi-laboratory repeat at 0.15 mT (Wey 2000) found no difference between field, sham and no-field. McCreary 2002 found effects only after correcting for cell-cycle and anti-CD3 covariates. A 4.75 T static + 0.7 mT pulsed NMR exposure raised Ca2+ in normal lymphocytes and lowered it in Jurkat cells without pro-inflammatory output (Aldinucci 2003).'),
    discriminating_evidence=[
        D('1333413', None, 'Multi-ring annular culture plate: E varied at constant B; pure E-field vs magnetically induced E (abstract)', 'Ca2+ influx increased in the plateau phase of mitogen signalling at 22 mT, 60 Hz, E = 1.7 mV/cm; scaled with induced E; pure E matched; Ca2+ channel implicated.'),
        D('8344993', None, '50 Hz, 0.1 mT sinusoidal, single-cell fura-2 imaging, Jurkat (abstract)', 'Acute Ca2+ oscillations that stopped when the field was off; comparable to anti-CD3 effect.'),
        D('10656853', None, 'Blinded RAPID programme repeat, 1.5 G (0.15 mT) 50 Hz, 8 min; MF vs sham vs no field (abstract)', 'Transient incidence 16.5 / 14.6 / 14.2% (MF / sham / no field), no significant difference: null replication of Lindstrom.'),
        D('11518497', None, 'Replication with 50 Hz, 0.15 mT in Jurkat E6-1 cells from three sources (abstract)', 'Responses were seen but at lower percentage than the original.'),
        D('11948612', None, '60 Hz 100 uT peak, 78 uT static, combined; covariate analysis (abstract)', 'Effects only appeared after cell-cycle and anti-CD3 correction.'),
        D('12929155', None, '4.75 T static + 0.7 mT pulsed NMR, 1 h, human lymphocytes and Jurkat (abstract)', 'Ca2+ up in normal lymphocytes, down in Jurkat; no pro-inflammatory cytokines.'),
        D('8986359', None, 'Model paper: activation-dependent and biphasic responses (abstract)', 'Proposes that effects depend on cell activation state and may be biphasic, explaining irreproducibility.'),
    ],
    thresholds=[
        T('lowest_effective', 'Ca2+ influx in mitogen-activated thymocyte plateau phase', 'Rat thymic lymphocytes, 37 C', 'invitro', '1333413', None, 'abstract_only',
          B=22.0, Bnote='22 mT as stated in abstract (peak vs rms not stated)', f=60, wf='sinusoidal', exp='60 min',
          dbdt=8.29, dbasis='computed', E=0.17, Ebasis='reported', Egeom='Abstract reports E induced = 1.7 mV/cm (x0.1 = 0.17 V/m); position in the annular plate not specified',
          note='Computed dB/dt = 2*pi*60*22e-3 = 8.29 T/s (assuming sine peak). The abstract reports the effect scaled with induced E at constant B.'),
        T('lowest_effective', 'Ca2+ oscillations in Jurkat', 'Jurkat T cells', 'invitro', '8344993', None, 'abstract_only',
          B=0.1, Bnote='0.1 mT as stated (assumed peak)', f=50, wf='sinusoidal', dbdt=0.0314, dbasis='computed', note='Computed 2*pi*50*0.1e-3 = 0.0314 T/s.'),
        T('no_effect_below', 'Ca2+ transients (blinded multi-lab repeat)', 'Jurkat cells', 'invitro', '10656853', None, 'abstract_only',
          B=0.15, Bnote='1.5 G = 0.15 mT as stated', f=50, wf='sinusoidal (bifilar coil)', exp='8 min', dbdt=0.0471, dbasis='computed', note='Null at the Lindstrom conditions: computed 2*pi*50*0.15e-3 = 0.0471 T/s.'),
        T('lowest_effective', 'In vivo lymphocyte Ca2+/PMCA restoration', 'Arthritic rats', 'animal', '17537462', 'selvam2007', 'abstract_only',
          B=0.004, Bnote='4 uT as stated', f=5, exp='90 min', dbdt=1.26e-4, dbasis='computed', note='Computed assuming sine peak.'),
        T('lowest_effective', 'Calcineurin up, NFATc1 nuclear translocation down, Ca2+ oscillations suppressed', 'RAW264.7 + RANKL', 'invitro', '27856256', None, 'abstract_only',
          note='B and frequency not in the abstract; the opposite sign (NFAT2 up) was seen at 0.8 mT 60 Hz in macrophages (Kim 2017).'),
    ],
    window_summary='Effects reported from 0.1 mT at 50-60 Hz (computed dB/dt 0.03-0.05 T/s) up to 22 mT (reported E 0.17 V/m); independent replications at 0.1-0.15 mT were null or weak. The E-metric experiment is the only one that tests the driver directly.',
    replication_status='Contested: single-lab positives (Lindstrom, Liburdy) with weak or null independent replications (Wey blinded repeat, Mattsson, McCreary).',
    confidence='medium',
    caveats='Abstract-only; Liburdy dose in B (22 mT) is high relative to therapeutic or environmental 50 Hz exposures; E magnitude 0.17 V/m is the reported value.'))

# ---------------------------------------------------------------- 7
targets.append(dict(
    id='neutrophil_ros_mast_cell_microglia',
    name='Innate immune cells: neutrophil ROS, mast-cell degranulation, microglia',
    level='cellular',
    modalities=['wound/inflammation resolution', 'neuro-modulation/neuroprotection'],
    driver='unresolved',
    driver_explanation=(
        'Neutrophil superoxide inhibition is tied to A2A density and shows intensity, time and temperature dependence (Varani 2002), while ELF fields at 0.1 mT enhanced the PMA burst by 12.4% in rat neutrophils (Roy 1995), '
        'so polarity depends on the stimulus and the field. Mast cells showed no response at 5 mT, 60 Hz for 0.5-2 h (Price 1998, null). Microglia (N9) show reduced TNF-a/IL-1b via JNK (Merighi 2020) and reduced ROS (Merighi 2024) with the Ferrara 1.5 mT, 75 Hz protocol. '
        'No design separated B from dB/dt.'),
    discriminating_evidence=[
        D('11976268', 'varani2002', 'Neutrophils (abstract only)', 'Receptor density and agonist potency increased; superoxide inhibition by A2A agonists enhanced; intensity-, time- and temperature-dependent.'),
        D('7498533', None, '0.1 mT, 60 Hz, primed rat peritoneal neutrophils, PMA, DCFH real time (abstract)', 'PMA-induced burst fluorescence +12.4% under field (n=5, P<0.02).'),
        D('9554697', None, '5 mT, 60 Hz solenoid, rat peritoneal mast cells, 30 min to 2 h, 37 C (abstract)', 'No degranulation and no change in 48/80 sensitivity: null.'),
        D('31400640', 'merighi2020', 'N9 microglia (existing library)', 'TNF-a and IL-1b reduced via a JNK-dependent pathway.'),
        D('39684558', 'merighi2024', 'N9 microglia, SH-SY5Y; time series 4-72 h (full text)', 'ROS reduced 33-39% after 24 h in N9; 90 min preserved membrane potential.'),
    ],
    thresholds=[
        T('lowest_effective', 'PMA-induced oxidative burst +12.4%', 'Rat peritoneal neutrophils', 'invitro', '7498533', None, 'abstract_only',
          B=0.1, Bnote='0.1 mT as stated', f=60, wf='sinusoidal ELF', dbdt=0.0377, dbasis='computed', note='Computed 2*pi*60*0.1e-3 = 0.0377 T/s (assuming peak). Direction is pro-oxidant.'),
        T('no_effect_below', 'Histamine release / sensitivity to 48/80', 'Rat peritoneal mast cells', 'invitro', '9554697', None, 'abstract_only',
          B=5.0, Bnote='5 mT as stated', f=60, wf='sinusoidal solenoid', exp='30 min to 2 h', dbdt=1.885, dbasis='computed', note='Null at 5 mT: computed 2*pi*60*5e-3 = 1.885 T/s.'),
        T('lowest_effective', 'ROS reduction 33-39% (24 h) in microglia', 'N9 microglia', 'invitro', '39684558', 'merighi2024', 'fulltext',
          B=1.5, f=75, wf='pulsed', pw=1.3, burst='duty 0.1', exp='4-72 h', dbdt=2.04, dbasis='computed', note='dB/dt from the 1.5 mT probe measurement (Vincenzi 2013).'),
        T('lowest_effective', 'A2A agonist-mediated superoxide inhibition', 'Human neutrophils', 'invitro', '11976268', 'varani2002', 'abstract_only',
          B=1.0, Bnote='From Varani 2017 review', f=75, wf='pulsed', pw=1.3, exp='>=1 h'),
    ],
    window_summary='Ferrara protocol (1.5 mT, 75 Hz, 1.3 ms) reduces ROS/cytokines in neutrophils and microglia; 60 Hz sine fields at 0.1 mT increase neutrophil burst, and 5 mT does not affect mast cells.',
    replication_status='Single group for the protective effects; ELF pro-oxidant and null results from separate labs.',
    confidence='low',
    caveats='Abstract-only for most records.'))

# ---------------------------------------------------------------- 8
targets.append(dict(
    id='safety_icnirp_epidemiology',
    name='Safety side: ICNIRP/IARC limits and the 0.3-0.4 uT childhood-leukaemia association',
    level='tissue-neural',
    modalities=['wound/inflammation resolution'],
    driver='unresolved',
    driver_explanation=(
        'ICNIRP 2010 limits are expressed as induced E in the CNS (basic restriction) and B (reference level), i.e. they are induction-based. The childhood-leukaemia association is for 24 h average residential magnetic field categories of 0.3-0.4 uT and above (about three orders of magnitude below therapeutic mT levels); '
        'it is an epidemiological association, not shown to be causal, and the mechanism (B, dB/dt, E, contact currents, or confounding) is unknown. IARC 2002 classified ELF magnetic fields as possibly carcinogenic (2B) on this basis.'),
    discriminating_evidence=[
        D('10944614', None, 'Pooled analysis of 9 studies (abstract)', 'For <0.4 uT (99.2% of children) estimates were near the null; for >=0.4 uT (44 cases, 62 controls) RR 2.00 (1.27-3.13); selection bias may explain part.'),
        D('11055621', None, 'Pooled analysis of 12 studies (abstract)', '>0.3 uT vs 0-0.1 uT OR 1.7 (1.2-2.3); 0.1-0.2 and 0.2-0.3 uT showed little or no association; US population-attributable fraction 3% (-2% to 8%).'),
        D('20877339', None, 'Seven post-2000 studies, 10,865 cases (abstract)', 'ORs vs <0.1 uT: 1.07 (0.81-1.41) for 0.1-0.2; 1.16 (0.69-1.93) for 0.2-0.3; 1.44 (0.88-2.36) for >=0.3 uT.'),
        D('29808013', None, 'Power-line proximity pooled analysis (abstract)', 'OR 1.33 (0.92-1.93) for <50 m from 200+ kV lines; no association with calculated magnetic field.'),
        D('34481821', None, 'Pooled analysis of four recent studies (abstract)', 'OR 1.01 for >=0.4 uT vs <0.1 uT; the meta-analysis of the three pooled analyses gave 1.45 (0.95-2.20).'),
    ],
    thresholds=[
        T('adverse', 'Childhood leukaemia (association, 24 h average residential field)', 'Children, case-control pooled analysis', 'human_other', '10944614', None, 'abstract_only',
          B=0.0004, Bnote='0.4 uT category cut-point of the 24 h average residential field (time-weighted mean, NOT a peak; if sinusoidal the peak would be ~1.41x an rms value)', f=50,
          wf='residential 50/60 Hz', dbdt=1.26e-4, dbasis='computed', E=6.3e-6, Ebasis='computed', Egeom='(r/2)*dB/dt with r = 0.1 m (rough head/torso scale, assumed)',
          note='Computed 2*pi*50*0.4e-6 = 1.26e-4 T/s assuming 0.4 uT is sine amplitude. Association only; RR 2.00 (1.27-3.13) for >=0.4 uT (44 cases, 62 controls). 99.2% of children were below 0.4 uT.'),
        T('adverse', 'Childhood leukaemia (association)', 'Children, 12-study pooled analysis', 'human_other', '11055621', None, 'abstract_only',
          B=0.0003, Bnote='0.3 uT category cut-point (time-weighted mean field)', f=50, dbdt=9.4e-5, dbasis='computed',
          note='Computed 2*pi*50*0.3e-6 = 9.4e-5 T/s. OR 1.7 (1.2-2.3) vs 0-0.1 uT; no clear association below 0.3 uT.'),
        T('adverse', 'Childhood leukaemia (association)', 'Children, post-2000 studies', 'human_other', '20877339', None, 'abstract_only',
          B=0.0003, Bnote='>=0.3 uT category', f=50, note='OR 1.44 (0.88-2.36); weaker in recent studies, imprecise.'),
        T('safety_limit', 'ICNIRP 2010 general-public reference level for B', 'Standard', 'standard', '21068601', 'icnirp2010', 'abstract_only',
          B=0.283, Bnote='200 uT rms at 50 Hz = 0.283 mT peak (converted); occupational 1000 uT rms. Values from a garbled PDF extraction: to be re-verified against the original', f=50, wf='sinusoidal rms',
          dbdt=0.0889, dbasis='computed', note='Computed from the peak: 2*pi*50*0.283e-3 = 0.0889 T/s. At 10 Hz the public reference is 500 uT rms. Pulsed therapy at 1.5 mT peak and 75 Hz is numerically ~5x the public peak value but pulse shape and duty cycle must be assessed with the induced-E restriction, not B alone.'),
        T('safety_limit', 'ICNIRP 2010 CNS basic restriction (induced E, rms)', 'Standard', 'standard', '21068601', 'icnirp2010', 'abstract_only',
          f=50, E=0.02, Ebasis='reported', Egeom='General public 0.02 V/m rms at 50 Hz; occupational 0.1 V/m; 10-25 Hz public 0.01 V/m, occupational 0.05 V/m (from a garbled PDF extraction; verify)',
          note='Computed dish-scale E for the Ferrara 1.5 mT pulses (~0.044 V/m) is the same order as this restriction; the cell dish is not tissue and the comparison is only a magnitude check.'),
        T('safety_limit', 'IARC 2002 classification', 'Standard', 'standard', '12071196', None, 'abstract_only',
          note='ELF magnetic fields classed as 2B (possibly carcinogenic) based on the childhood-leukaemia association (stated in Zaryabova 2013 abstract; the IARC monograph abstract itself was not available). WHO EHC 238 (2007) and NTP 1998 were not retrievable from PubMed and are not verified.'),
    ],
    window_summary='Epidemiological association appears at 24 h mean residential fields of about 0.3-0.4 uT and above (OR 1.4-2.0, imprecise, weaker in recent studies); ICNIRP public reference 200 uT rms at 50 Hz and CNS induced-E restriction 0.02 V/m rms. Therapeutic pulsed mT fields are 3-4 orders of magnitude above the epidemiological category field.',
    replication_status='Pooled analyses consistently show elevated but imprecise ORs at >=0.3-0.4 uT; recent pooled data show attenuation (OR 1.01 for >=0.4 uT in four recent studies); causality is not established.',
    confidence='medium',
    caveats=('Association, not causation; selection bias and confounding (e.g. traffic, wire code) are discussed in the primary papers. A typical residential 50/60 Hz field magnitude is not quoted from a verified abstract here (Ahlbom reports 99.2% of children below 0.4 uT); ICNIRP numbers need re-verification. '
             'The IARC monograph abstract was not accessible.')))

# ---------------------------------------------------------------- refs
A = {}  # pmid: (type, systems, mechs, direction, summary)
A['28255202'] = ('review', ['immune'], ['adenosine'], '+', 'Review of the A2A/A3 adenosine receptor route for PEMF anti-inflammatory action; the neutrophil data it summarises give no effect at 0.2-0.5 mT, effect from 1 mT, plateau 1.5-3.5 mT and a rise over 30-120 min, with two-fold receptor density giving ~4-fold agonist potency.')
A['21830213'] = ('invitro', ['immune'], ['adenosine'], '+', 'Human OA synovial fibroblasts exposed to EMF showed selective A2A/A3 up-regulation with cAMP changes, lower PGE2, IL-6 and IL-8 and higher IL-10, mediated by the receptors; no effect on matrix-degrading enzymes. Exposure parameters not in the abstract.')
A['18640059'] = ('invitro', ['immune'], ['adenosine'], '+', 'Bovine synovial fibroblasts exposed to 75 Hz, 1.5 mT for 24 h had lower TNF-a/LPS-stimulated PGE2 and COX-2; the EMF effect was lost when endogenous adenosine was removed with adenosine deaminase, supporting A2A up-regulation as the mediator.')
A['14599547'] = ('invitro', ['immune'], ['adenosine'], '+', 'Human neutrophils exposed to PEMF showed unchanged A3 affinity (KD 2.36 vs 2.45 nM) but higher receptor density (Bmax 451 to 736 fmol/mg protein); abstract gives no B value.')
A['33126773'] = ('invitro', ['nervous'], ['adenosine'], '+', 'PEMF induced a time-dependent, HIF-1a-independent VEGF release in human astrocytes whose conditioned medium protected SH-SY5Y cells after oxygen-glucose deprivation; exposure parameters not in the abstract.')
A['30656694'] = ('invitro', ['nervous'], ['adenosine'], '+', 'In hypoxic PC12 cells PEMF reduced death through rapid p38 activation (30 min), HSP70, CREB phosphorylation (24 h) and later BDNF/Bcl-2 changes (48 h).')
A['27639248'] = ('invitro', ['nervous', 'immune'], ['adenosine'], '+', 'PEMF reduced hypoxia-induced cell death, apoptosis, HIF-1a and ROS in SH-SY5Y, PC12 and N9 microglia (24-48 h) and lowered TNF-a, IL-1b, IL-6 and IL-8 release from LPS-stimulated N9 cells.')
A['40650273'] = ('invitro', ['nervous'], ['adenosine'], '+', 'PEMF restored mitochondrial and CREB/BDNF signalling in oxidatively stressed PC12 cells (Ferrara group).')
A['26151161'] = ('invitro', ['immune'], ['effectors'], '+', 'In CHO cells with human mu-opioid receptors a 5 Hz EMF reduced stimulated cAMP more than morphine (about 23% more), whereas 13 Hz behaved like control; supports a narrow low-frequency window. B not in abstract.')
A['27228272'] = ('review', ['immune'], ['effectors'], '+', 'Review of electromagnetic-field devices in nociception and peripheral inflammation (Ross).')
A['34471827'] = ('review', ['immune'], ['effectors'], '+', 'Review of PEMF modulation of inflammation and tissue repair (Ross and collaborators), including frequency-specific work.')
A['34821733'] = ('invitro', ['immune'], ['effectors'], '±', 'Twenty-two blinded Somagen fields (6-282 uT, fundamental 3.3-90.6 Hz, 7 or 30 min) acted on PBMC-derived macrophages; fields of 51.8 Hz and 52.3 Hz with different send-pause burst patterns drove M1-like and M2-like profiles respectively, showing waveform dependence at matched frequency and amplitude.')
A['28741320'] = ('invitro', ['immune'], ['effectors'], '±', 'RAW264.7 cells with RANKL exposed to 15 Hz PEMF at 0.5, 1, 2 and 3 mT (2 h/day for 7 days): 0.5 mT suppressed osteoclast formation and bone resorption, 3 mT enhanced resorption through apoptosis and higher BAX, defining an intensity window.')
A['28370033'] = ('invitro', ['immune'], ['radical'], '+', 'A 60 Hz, 0.8 mT field increased NO, TNF-a, IL-1b and IL-6, NF-kB nuclear translocation, NFAT2 and Ca2+ influx in RAW264.7 macrophages and reduced antioxidant effectiveness: a pro-inflammatory ELF result.')
A['16598759'] = ('invitro', ['immune'], ['radical'], '+', 'A 50 Hz, 1.0 mT field raised mouse macrophage phagocytosis 1.6-fold at 45 min and IL-1b release up to 12.3-fold at 24 h; free-radical formation rose at every flux density tested (0.05-1.0 mT, 45 min) without micronucleus change.')
A['30942408'] = ('invitro', ['immune'], ['effectors'], '-', 'Low-frequency PEMF inhibited RANKL-induced osteoclastic differentiation in RAW264.7 cells via ROS scavenging.')
A['29749519'] = ('invitro', ['immune'], ['effectors'], '-', 'PEMF inhibited osteoclast differentiation in RAW264.7 cells through the Akt/mTOR pathway.')
A['27856256'] = ('invitro', ['immune'], ['vgcc'], '-', 'PEMF suppressed RANKL-dependent osteoclast formation in RAW264.7 cells by damping Ca2+ oscillations, raising calcineurin activity and blocking NFATc1 nuclear translocation.')
A['32596310'] = ('animal', ['immune'], ['adenosine'], '+', 'In mouse DMM and air-pouch synovitis, PEMF (pulse waveform, 1.5 mT, 75 Hz, 10% duty) lowered IL-1b and TNF-a, reduced neutrophils, increased macrophages and efferocytosis, with p38 phosphorylation inhibited.')
A['32751697'] = ('invitro', ['immune'], ['effectors'], '+', 'In co-cultures of IL-1b-primed human tendon cells and macrophages, PEMF favoured a pro-regenerative macrophage phenotype and anti-inflammatory mediators, possibly through FAK signalling.')
A['15352165'] = ('review', ['immune'], ['radical'], 'th', 'Review framing ELF fields as effectors of free-radical-mediated cellular activation in immune cells.')
A['42737802'] = ('invitro', ['immune'], ['adenosine'], '+', 'Independent Korean study: PEMF restored A2AAR, PKA and cAMP in UVB-injured fibroblasts and reduced IL-1b/NF-kB/MMP markers and collagen loss in vitro and in vivo; the authors say the data are consistent with but do not prove A2AAR involvement; parameters not in the abstract.')
A['42304062'] = ('theory', ['immune'], ['adenosine'], 'th', 'Atomistic simulations of magnetic-field modulation of the A2A adenosine receptor (Sapienza and IGEA authors); theoretical support only.')
A['33630907'] = ('invitro', ['muscular'], ['adenosine'], '+', 'In MC3T3-E1 cells exposed to a PhysioStim-like waveform (3.85 kHz pulses, 10 T/s slew, 4 h/day for up to 16 days), CRISPR disruption of Adora3 blunted PEMF-driven alkaline phosphatase and osteoblast genes, Adora2A disruption delayed and partly blunted them, and Adora3 knock-in rescued; independent evidence that both receptors are needed.')
A['39937022'] = ('invitro', ['muscular'], ['trpc1', 'radical'], '+', 'A CRY2-TRPC1 photosensitive axis underlies magnetic myogenesis; sensitivity was lost by growth in the dark, magnetic shielding or upward-directed fields.')
A['35841726'] = ('invitro', ['muscular'], ['trpc1'], '+', 'A single 10 min exposure at 1.5 mT produced a myogenic secretome; downward-directed fields outperformed upward-directed fields, TRPC upregulation was seen, direct exposure gave mild oxidative stress and streptomycin blocked the effect.')
A['32875708'] = ('invitro', ['muscular'], ['trpc1'], '+', 'Cell-derived vesicles from C2C12 myoblasts carry TRPC1 and respond to PEMF with TRPC1-mediated Ca2+ entry; TRPC1 knock-down vesicles do not, and wild-type vesicles restore PEMF-induced respiration and proliferation in knock-down cells.')
A['32627872'] = ('animal', ['muscular'], ['trpc1'], '+', 'Mice given 1.5 mT, 10 min weekly PEMF (with or without exercise) showed higher muscle and adipose Pgc-1a after 6 weeks with exercise and after 2 months alone, with oxidative muscle and fatty-acid oxidation after >4 months.')
A['37892906'] = ('review', ['muscular'], ['trpc1'], 'th', 'Review of magnetic mitohormesis stating efficacy windows (1.5 mT/10 min for myogenesis vs 3 mT/60 min for cancer-cell killing), that waveform symmetry, rise time and direction are rarely reported, and that exposure after log-phase expansion reduces myogenic potency.')
A['39061719'] = ('invitro', ['muscular'], ['trpc1'], '+', 'Combined optical and magnetic stimulation gave supra-additive proliferation and ATP, lower ROS and higher TRPC1 protein; aminoglycosides blocked.')
A['39120305'] = ('review', ['muscular'], ['trpc1'], 'th', 'Commentary on aminoglycoside antibiotics as TRP-channel antagonists that block magnetic mitohormetic signalling.')
A['42737597'] = ('review', ['muscular'], ['trpc1'], 'th', 'Perspective on magnetic mitohormesis as a therapy for X-linked muscle disease (Iversen); source of the 15 Hz, 1 vs 1.5 mT device description.')
A['25708841'] = ('invitro', ['nervous'], ['radical'], '+', 'SH-SY5Y cells pre-exposed to short repeated PEMF (4 x 10 min per week, 40 min total) had higher MnSOD activity and lower ROS after H2O2; B not stated in the abstract.')
A['26940444'] = ('invitro', ['nervous'], ['radical'], '+', 'Drug-resistant SK-N-BE(2) cells exposed to 2 mT, 75 Hz (15 min x 3 over 5 days) had higher MnSOD protection and lower ROS after H2O2.')
A['40575091'] = ('invitro', ['general'], ['icr', 'radical'], '±', 'HT-1080 cells in a 45 uT static field with a 10 uT oscillating field at 12-33 Hz showed growth acceleration or inhibition near 16.5 Hz, sensitive to a 0.5 Hz shift or 250 nT field change.')
A['39849096'] = ('theory', ['general'], ['radical'], 'th', 'Model of a Complex III radical-pair amplification mechanism for weak ELF magnetic field effects in cancer cells.')
A['1333413'] = ('invitro', ['immune'], ['induction', 'vgcc'], '+', 'Rat thymocyte Ca2+ influx in the plateau phase of mitogen signalling rose at 22 mT, 60 Hz (induced E 1.7 mV/cm); an annular plate showed dependence on induced E at constant B and a pure E-field matched, pointing to an electric-field metric and a Ca2+ channel site.')
A['8344993'] = ('invitro', ['immune'], ['vgcc'], '+', 'Jurkat T cells exposed to 50 Hz, 0.1 mT showed Ca2+ oscillations that stopped when the field was off, comparable in size to anti-CD3 stimulation.')
A['11518497'] = ('invitro', ['immune'], ['vgcc'], '0', 'Replication at 50 Hz, 0.15 mT in Jurkat E6-1 cells from three sources found a lower fraction of responding cells than the original report.')
A['10656853'] = ('invitro', ['immune'], ['vgcc'], '0', 'Blinded multi-laboratory repeat of Lindstrom (1.5 G, 50 Hz, 8 min) found transient incidence 16.5, 14.6 and 14.2% for field, sham and no-field, not significantly different.')
A['11948612'] = ('invitro', ['immune'], ['vgcc'], '0', 'Jurkat Ca2+ responses to 60 Hz 100 uT with 78 uT static fields appeared only after correction for cell-cycle and anti-CD3 covariates.')
A['1397839'] = ('review', ['immune'], ['vgcc'], 'th', 'Review of field effects on immune cells with calcium signalling as the proposed route.')
A['8986359'] = ('theory', ['immune'], ['vgcc'], 'th', 'Model of activation-dependent and biphasic field effects on Ca2+ signalling in immune cells.')
A['12929155'] = ('invitro', ['immune'], ['vgcc'], '±', 'One hour in a 4.75 T static plus 0.7 mT pulsed NMR field raised Ca2+ in normal lymphocytes and lowered it (with lower proliferation) in Jurkat cells, without pro-inflammatory cytokine changes.')
A['7498533'] = ('invitro', ['immune'], ['radical'], '+', 'A 60 Hz, 0.1 mT field increased the PMA-induced oxidative burst of rat neutrophils by 12.4% (n=5).')
A['9554697'] = ('invitro', ['immune'], ['effectors'], '0', 'Rat peritoneal mast cells exposed to 5 mT, 60 Hz for 30 min-2 h showed no degranulation and no change in compound 48/80 sensitivity.')
A['10944614'] = ('meta', ['immune'], ['effectors'], 'th', 'Pooled analysis of nine studies: for fields below 0.4 uT (99.2% of children) estimates were near null, for 0.4 uT and above RR 2.00 (1.27-3.13) from 44 cases and 62 controls, with selection bias a possible explanation.')
A['11055621'] = ('meta', ['immune'], ['effectors'], 'th', 'Pooled analysis of twelve studies: >0.3 uT vs 0-0.1 uT OR 1.7 (1.2-2.3), little or no association for 0.1-0.3 uT, US population-attributable fraction 3% (-2% to 8%).')
A['20877339'] = ('meta', ['immune'], ['effectors'], 'th', 'Pooled analysis of seven post-2000 studies (10,865 cases): ORs vs <0.1 uT 1.07, 1.16 and 1.44 (0.88-2.36) for 0.1-0.2, 0.2-0.3 and >=0.3 uT; weaker than earlier pooled analyses and imprecise.')
A['29808013'] = ('meta', ['immune'], ['effectors'], 'th', 'Pooled analysis of power-line proximity: OR 1.33 (0.92-1.93) within 50 m of 200+ kV lines with no association for calculated magnetic field.')
A['34481821'] = ('meta', ['immune'], ['effectors'], '0', 'Pooled analysis of four recent studies (24,994 cases): OR 1.01 for >=0.4 uT vs <0.1 uT; the meta-analysis of the three pooled analyses gave 1.45 (0.95-2.20).')
A['29574256'] = ('human', ['immune'], ['effectors'], 'th', 'Residential-mobility analysis: calculated fields >=0.4 uT gave OR 1.71 (0.65-4.52) in non-movers and about 1.98 after propensity adjustment, illustrating exposure-misclassification issues.')
A['28900736'] = ('human', ['immune'], ['effectors'], '0', 'California population-based study: the highest exposure group had OR 1.50 (0.70-3.23).')
A['17485729'] = ('human', ['immune'], ['effectors'], 'th', 'Nighttime-exposure analysis: >=0.4 uT OR 1.93 (1.11-3.35).')
A['12071196'] = ('standard', ['immune'], ['effectors'], 'th', 'IARC Monograph evaluation of static and ELF electric and magnetic fields (Part 1); classification as possibly carcinogenic (2B) is reported by secondary sources; abstract not available here.')
A['23675624'] = ('human', ['measurement'], ['effectors'], 'th', 'Measurement study of ELF magnetic fields near transformers; its abstract states that IARC 2002 classed ELF magnetic fields as 2B and that WHO EHC 238 (2007) confirmed this.')
A['16023006'] = ('animal', ['immune'], ['adenosine'], '+', 'Aged Dunkin-Hartley guinea pigs with osteoarthritis given PEMF 6 h/day for 3 months had reduced chondropathy progression and thicker cartilage, linked to chondrocyte metabolism and adenosine A2a activity.')
A['33970582'] = ('review', ['general'], ['adenosine'], '+', 'Review of PEMF stimulation of bone healing and joint preservation, including the adenosine receptor mechanism and the clinical record.')
A['40428093'] = ('review', ['immune'], ['adenosine'], '+', 'Review of PEMF regulation of inflammation (NF-kB, MAPK, adenosine A2A) in soft tissue, cartilage and joint healing with clinical examples.')
A['41618092'] = ('invitro', ['general'], ['effectors'], '±', 'A single low-energy 1 ms, 30 kHz sine-burst device selectively stimulated ATP-synthesis-linked respiration in cells, homogenates and isolated mitochondria but did not rescue NO-inhibited respiration (blue light did).')
A['39939866'] = ('invitro', ['general'], ['effectors'], '+', 'PEMF at 4 mT and 80 Hz promoted L929 migration and viability, shifted metabolism from mitochondrial respiration to glycolysis, kept ROS low and increased vesicular transport.')
A['41010617'] = ('human', ['muscular'], ['trpc1'], '0', 'Exploratory 12-session weekly 10 min PEMF (magnetic mitohormesis) in 40 adults with type 2 diabetes showed no overall HbA1c, glucose or HOMA-IR change; HbA1c fell 7.5 to 7.1% in the central-obesity subgroup; no adverse events.')
A['42078208'] = ('animal', ['immune'], ['effectors'], '+', 'Mice exposed to a weak broadband pulsed device for 10 nights showed a dose-dependent rise in plasma antioxidant potential (+8% n.s. at 1 min/h, +20.6% at 5 min/h) and thymocyte mitochondrial fluorescence (+29% at the highest exposure).')

refs = []
for pmid, (typ, sysm, mech, dirn, summ) in A.items():
    if pmid in existing:
        print('SKIP existing', pmid, existing[pmid], file=sys.stderr)
        continue
    a = db[pmid]
    au = a.get('authors') or []
    if au and au[0].get('last_name'):
        first = au[0]['last_name']
        names = ['%s %s' % (x.get('last_name', ''), x.get('initials', '')) for x in au[:3]]
        short = ', '.join(names) + (', et al.' if len(au) > 3 else '')
    else:
        first = 'IARC Working Group'
        short = 'IARC Working Group'
    c = a.get('citation') or {}
    cit = ''
    if c.get('volume'):
        cit = c['volume'] + ('(%s)' % c['issue'] if c.get('issue') else '') + (':' + c['pages'] if c.get('pages') else '')
    elif c.get('pages'):
        cit = c['pages']
    refs.append(dict(pmid=pmid, first_author=first, authors_short=short, year=int(a['publication_date']['year']),
                     title=a['title'], journal=a['journal']['title'], citation=cit, doi=a['identifiers'].get('doi') or a.get('doi'),
                     pmcid=a['identifiers'].get('pmc'), type=typ, systems=sysm, mechs=mech, direction=dirn, summary=summ))

# validation
used = set()
for t in targets:
    for e in t['discriminating_evidence']:
        used.add(e['pmid'])
    for th in t['thresholds']:
        used.add(th['pmid'])
refpm = {r['pmid'] for r in refs}
unknown = [p for p in used if p not in refpm and p not in existing]
print('cited but neither new nor existing:', unknown)
print('new refs not cited:', [p for p in refpm if p not in used])
print('targets', len(targets), 'refs', len(refs))

cross = (
    'Dose variable by group: Ferrara/IGEA uses 1.3 ms pulses at 75 Hz (computed ~2 T/s at 1.5 mT from a measured 2.0 mV probe voltage; dish-scale E ~0.04 V/m); Ross uses 5-30 Hz square waves at ~4 mT; Franco-Obregon/NUS uses 15 Hz pulse barrages '
    '(rise ~50 us; reported ~17 T/s inconsistent with 3 mT/50 us = 60 T/s); Kar 2021 used 3.85 kHz pulses at 10 T/s slew. A2A/A3 involvement appears across these very different dB/dt values (2 to 60 T/s), which argues against dB/dt as the sole trigger, '
    'but B and dB/dt were never decoupled. The only direct E-vs-B experiment in scope is Liburdy 1992 (thymocyte Ca2+, E reported 0.17 V/m at 22 mT, 60 Hz). Mast-cell and Jurkat Ca2+ nulls were found; independent nulls of A2A Bmax were not found. '
    'Not found in PubMed with simple searches: Calabro, Gualdi, Kuhn mitochondrial PEMF papers. Methods of Varani 2002 and Yap 2019 were not read (Europe PMC HTTP 429); Byun 2026 has a PMC full text (PMC13566763) that was not read. '
    'Epidemiology is reported strictly as association; a typical residential field value is not supplied because no verified abstract states one. '
    'Sub-note: the Sukumar 2026 statement that prior macrophage work at uT-1.5 mT was anti-inflammatory is a narrative statement, not a measured crossover. Li 2019 (high-voltage E-field pulses) and Piredda 2026 (>2 T multifrequency pulses) were screened out as not therapeutic magnetic-field studies.')

out = dict(scope='Adenosine A2A/A3 receptors, inflammation/immune signalling (NF-kB, cytokines, macrophages, lymphocytes, neutrophils, mast cells, microglia), TRPC1-mitochondrial targets and ELF safety side',
           targets=targets, new_refs=refs, cross_cutting_notes=cross)
json.dump(out, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('written', OUT)
