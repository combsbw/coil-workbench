#!/usr/bin/env python3
"""Build thr_bundle.js (the threshold section data) from research-notes/dataset/*.json + thr_5/thr_6.
Run:  python3 research-notes/build_thr.py   ->  research-notes/thr_bundle.js
The bundle is spliced into /home/claude/coilbench/app.html by splice_thr.py.
"""
import json, glob, re, os, ast
HERE = os.path.dirname(os.path.abspath(__file__))
SP = '/tmp/claude-0/-home-claude-coil-workbench/be52d8fd-6910-5673-a281-429468ab8431/scratchpad/'

def J(p): return json.load(open(os.path.join(HERE, p)))
DS = {}
for f in sorted(glob.glob(HERE + '/dataset/*.json')):
    for r in json.load(open(f)): DS[r['id']] = r
T5 = {t['id']: t for t in J('thr_5_adenosine_immune.json')['targets']}
T6 = {t['id']: t for t in J('thr_6_B_driven.json')['targets']}
EXT = {**T5, **T6}

# driver classes: E induced field (dB/dt), B amplitude/orientation, T timing/waveform/frequency, U unresolved, X not a driver question
GROUPS = [
 ('phys', 'Physical bounds and safety'),
 ('nerve', 'Nerve, pain and brain'),
 ('ca', 'Calcium, calmodulin and nitric oxide'),
 ('imm', 'Adenosine, inflammation and immune cells'),
 ('bone', 'Bone, cartilage and tendon'),
 ('vasc', 'Vascular, wound and muscle'),
 ('mito', 'Mitochondria, redox and spin chemistry'),
]
# card: (id, group, driver class, [dataset ids], [ext ids], rows)
# rows: list of (label, B_mT, dBdt_T_s, E_V_m, basis)  each range = [lo,hi] or None; basis 'rep' reported | 'calc' computed
CARDS = [
 ('thermal', 'phys', 'E', ['thermal_noise_bound', 'thermal_noise_limit'], ['plausibility_kT_and_standards_context'],
  [('Thermal-noise bound on direct E detection', None, None, [1e-4, 0.1], 'rep')]),
 ('lorentz', 'phys', 'B', [], ['lorentz_hall_mhd_negligible_at_pemf'], [('Lorentz / Hall / MHD become measurable', [1000, 7000], None, None, 'rep')]),
 ('safety', 'phys', 'X', [], ['safety_icnirp_epidemiology'],
  [('Epidemiology category field to ICNIRP public level', [3e-4, 0.2], None, [0.02, 0.02], 'rep')]),
 ('dosemetric', 'phys', 'X', ['dose_metric'], ['decision_tests_B_vs_dBdt_E'], []),
 ('axon', 'nerve', 'E', ['axon_excitation'], [], [('Peripheral nerve / TMS excitation', None, [15, 26], [1.1, 120], 'rep')]),
 ('phosphene', 'nerve', 'E', ['magnetophosphene'], [], [('Retinal magnetophosphenes (20-60 Hz)', [22, 32], [4, 9], [0.002, 1.33], 'rep')]),
 ('subthr', 'nerve', 'E', ['membrane_polarisation', 'subthreshold_mood'], [], [('Network timing in slice (Deans 2007)', None, None, [0.18, 0.35], 'rep'), ('Low-field mood stimulation', None, None, [0.7, 1.0], 'rep')]),
 ('gating', 'nerve', 'E', ['pain_gating_opioid', 'rpms_pain'], [], [('Suprathreshold afferent recruitment', None, None, [2, 2], 'rep')]),
 ('painpemf', 'nerve', 'U', ['pemf_pain_trials', 'analgesia_adenosine_no'], ['mouse_ambient_elf_detection_shielding_analgesia', 'cnp_specific_pulsed_waveform_analgesia'],
  [('Shielded-mouse B x f effect (Prato)', [2.5e-5, 5e-4], [6.3e-6, 6.3e-6], [3e-8, 3e-8], 'calc'), ('Rat 5 mT, 50 Hz', [5, 5], [1.57, 1.57], [0.0079, 0.0079], 'calc'), ('Low-intensity PEMF trials 2-10 mT', [2, 10], [0.63, 3.1], [0.03, 0.24], 'calc'), ('MAGCELL 105 mT, 4-12 Hz', [105, 105], [2.6, 7.9], [0.013, 0.04], 'calc')]),
 ('regen', 'nerve', 'E', ['nerve_regen_DC_E', 'nerve_regen_pemf'], [],
  [('Direct DC field, in vitro', None, None, [24, 100], 'rep'), ('Low-B PEMF, rodent', [0.05, 0.3], None, [1e-4, 1e-2], 'rep')]),
 ('caentry', 'ca', 'E', ['ca_entry'], ['immune_cell_ca_signalling', 'elf_bdose_ca_oscillations_jurkat'],
  [('Lymphocyte Ca2+, Lindstrom (unreplicated)', [0.04, 0.15], [0.013, 0.047], None, 'calc'), ('Thymocyte Ca2+, Liburdy (B vs E test)', [22, 22], [8.29, 8.29], [0.17, 0.17], 'rep'), ('Stem cell and myoblast TRPC1, 10 min', [1.5, 2.0], None, None, 'rep')]),
 ('cambind', 'ca', 'T', ['cam_binding', 'ion_binding_timing'], [], []),
 ('no', 'ca', 'U', ['enos_no_cgmp', 'no_enos_node', 'camp'], [], [('eNOS / NO (various)', [0.5, 5], [0.14, 0.94], None, 'calc'), ('cAMP (Luben upper bound)', [0.6, 2], None, [0.1, 0.1], 'rep')]),
 ('icr', 'ca', 'T', ['icr_resonance'], ['icr_ipr_ca_resonance', 'snail_mouse_opioid_resonance_like'],
  [('Yost-Liburdy 16 Hz, 42 uT on 23 uT DC', [0.0234, 0.0421], [0.0042, 0.0042], None, 'calc'), ('Snail opioid windows, 60 Hz', [0.14, 0.55], [0.05, 0.2], None, 'calc')]),
 ('vgcc', 'ca', 'U', ['vgcc_hypothesis'], [], []),
 ('a2a', 'imm', 'U', ['a2a_receptor', 'a3_receptor'], ['adenosine_A2A_A3_upregulation'],
  [('A2A / A3 up-regulation (Ferrara signal)', [1.5, 3.0], [2.0, 4.1], [0.005, 0.05], 'calc')]),
 ('nfkb', 'imm', 'T', ['nfkb_cytokines'], ['nfkb_cytokine_prostaglandin_axis'], [('Cytokine suppression, 0.8-4 mT pulses', [0.8, 4.0], [0.19, 2.04], [0.001, 0.05], 'calc')]),
 ('macro', 'imm', 'T', ['macrophage_polarisation'], ['macrophage_polarisation_amplitude_pattern', 'neutrophil_ros_mast_cell_microglia'], []),
 ('osteo', 'bone', 'T', ['osteoblast_prolif_diff', 'insitu_E_dishes'], [], [('Osteoblast proliferation and differentiation', [0.13, 7], [0.19, 1.8], [0.0005, 0.016], 'calc'), ('In-situ E in dishes (McLeod, Collazo)', [0.7, 1.8], None, [0.0005, 0.0009], 'rep')]),
 ('boneca', 'bone', 'U', ['ca_cam_adenosine_bone'], [], []),
 ('tgfb', 'bone', 'T', ['tgfb_bmp_wnt_igf_cilia'], ['cmf_combined_field_bone_cells'], [('BMP, cilia, Wnt', [0.6, 2.4], [0.19, 0.19], None, 'calc'), ('IGF-II receptor, combined field', None, None, [1e-5, 1e-5], 'rep')]),
 ('clast', 'bone', 'E', ['osteoclast_opg_rankl'], [], [('Osteoclast / RANKL window', [0.5, 3.8], None, [0.00048, 0.00122], 'rep')]),
 ('chondro', 'bone', 'T', ['chondrocyte_matrix_oa'], [], [('Chondrocyte matrix', [1.0, 3.8], [0.47, 1.8], None, 'calc')]),
 ('tendon', 'bone', 'U', ['tendon_fibroblast', 'fracture_nonunion_fusion'], [], [('Non-union (uncontrolled series)', [0.01, 0.1], [0.03, 0.33], None, 'calc')]),
 ('angio', 'vasc', 'T', ['angiogenesis_fgf_vegf', 'hif1a'], [], [('Angiogenesis protocols', [1.2, 5], [0.14, 2.04], [0.01, 0.01], 'calc')]),
 ('flow', 'vasc', 'U', ['microvascular_flow', 'lymph_oedema_oxygen_iron'], [], [('Skin / microvascular flow trials', [0.1, 8.4], [0.019, 1.57], None, 'calc')]),
 ('wound', 'vasc', 'E', ['wound_fibroblast', 'dosimetry_regime_split'], [], [('Wound and fibroblast protocols', [1, 5], [0.31, 0.79], None, 'calc')]),
 ('muscle', 'vasc', 'T', ['skeletal_muscle'], [], [('Myoblast 1.5-2 mT', [1.5, 2.0], None, None, 'rep'), ('Static field route, muscle cells', [0.06, 0.4], [0, 0], [0, 0], 'rep')]),
 ('trpc1', 'mito', 'U', ['trpc1_mitochondria'], ['trpc1_ca_pgc1a_mitochondria'], [('TRPC1 mitohormesis', [1.5, 3.0], [0.14, 0.47], [0.0007, 0.012], 'calc')]),
 ('ros', 'mito', 'B', ['ros_redox', 'nrf2_ho1', 'mito_respiration_atp'], ['mitochondria_ros_redox_other_labs', 'weak_static_field_redox_regeneration'],
  [('ROS in cells, 0.1-20 mT', [0.1, 20], [0.16, 6.3], [0.00016, 0.031], 'calc')]),
 ('radical', 'mito', 'B', ['radical_pair'], ['rp_flavin_ros_static_plus_rf', 'rp_mfe_mT_scale_flavin', 'cryptochrome_dependent_elf_pemf_responses', 'env_elf_melatonin_tamoxifen_mcf7', 'chick_embryo_pulse_shape_ut_fields'],
  [('Weak-field flavin ROS partitioning', [2e-5, 0.05], None, None, 'rep'), ('mT-scale flavin effect (HeLa)', [18, 25], None, None, 'rep'), ('Cryptochrome ELF effects, fly', [0.09, 1.0], [0, 0.094], None, 'calc')]),
 ('magnetite', 'mito', 'B', ['magnetite_mechano'], ['biogenic_magnetite_magnetosome_torque'], [('Magnetite torque above kT', [0.05, 5], None, None, 'calc')]),
 ('diamag', 'mito', 'B', ['diamagnetic_zeeman_icr'], ['smf_diamagnetic_anisotropy_gradient_pain'], [('Diamagnetic orientation of cells and proteins', [1000, 16000], None, None, 'rep')]),
]

# ---------- labels ----------
PML, TIT = {}, {}
def lab_from(first, year, journal=None):
    s = f'{first} {year}'.strip()
    return s
try:
    am = json.load(open(SP + 'allmeta.json'))
    for p, e in am.items():
        au = e.get('authors') or []
        if isinstance(au, str): au = ast.literal_eval(au)
        pdt = e.get('publication_date') or {}
        if isinstance(pdt, str): pdt = ast.literal_eval(pdt)
        jn = e.get('journal') or {}
        if isinstance(jn, str):
            try: jn = ast.literal_eval(jn)
            except Exception: jn = {}
        if au:
            ln = au[0].get('last_name', '')
            PML[p] = f"{ln}{' et al.' if len(au) > 1 else ''} {pdt.get('year', '')}".strip()
            TIT[p] = e.get('title', '')
except Exception as ex:
    print('allmeta skipped', ex)
for l in open(os.path.join(HERE, 'existing_refs.tsv')).read().splitlines()[1:]:
    c = l.split('\t')
    if len(c) >= 4: PML[c[1]] = c[2].replace(' CA', '').strip(); TIT[c[1]] = c[3]
for l in open(os.path.join(HERE, 'allrefs.tsv')).read().splitlines():
    c = l.split('\t')
    if len(c) >= 6 and c[0] not in PML:
        try: y = json.loads(c[3]).get('year', '')
        except Exception: y = ''
        PML[c[0]] = f'{c[2]} {y}'.strip(); TIT[c[0]] = c[5]
for t in (J('thr_5_adenosine_immune.json'), J('thr_6_B_driven.json')):
    for r in t['new_refs']:
        PML[str(r['pmid'])] = f"{r['first_author']}{' et al.' if ',' in r.get('authors_short', '') or 'et al' in r.get('authors_short', '') else ''} {r['year']}"
        TIT[str(r['pmid'])] = r.get('title', '')
md = ''.join(open(f).read() for f in glob.glob(HERE + '/loop/*.md'))
for m in re.finditer(r'\|\s*(\d{6,8})\b[^|]*\|\s*([A-Z][^|]{2,60}?\b(?:19|20)\d\d)[^|]*\|', md):
    p, lab = m.group(1), re.sub(r'[,\s]+((?:19|20)\d\d)$', r' \1', m.group(2).strip())
    if p not in PML: PML[p] = lab
# hand fixes for first-author corrections flagged by the verifiers
PML.update({'32998161': 'Colombini 2020', '28255202': 'Varani 2017', '1468568': 'Walleczek 1992', '16528477': 'Ghibelli 2006', '6812594': 'Blackman 1989 (RF)', '36854553': 'Xu 2023', '15911163': 'King 2005', '22948539': 'Zhou 2012', '35129008': 'Ye 2022', '40973130': 'Bouisset 2025', '42058983': 'Jongutchariya 2026'})

# ---------- confidence badge ----------
RK = [('speculative', 0), ('very low', 1), ('low-moderate', 3), ('low–moderate', 3), ('low', 2), ('moderate', 4), ('medium', 4), ('high', 5)]
def grade(txt):
    t = (txt or '').lower(); found = []
    for k, v in RK:
        for m in re.finditer(re.escape(k), t):
            found.append((m.start(), v, k))
    # a 'low' inside 'low-moderate' / 'very low' is not a separate mention
    found = [f for f in found if not (f[2] == 'low' and (t[max(0, f[0] - 5):f[0]] == 'very ' or t[f[0]:f[0] + 12] in ('low-moderate', 'low–moderate')))]
    return min(v for _, v, _ in found) if found else 2

def slim_rec(r):
    out = {'name': r['name'], 'level': r.get('level', ''), 'driver': r['driver'], 'note': r.get('driver_note', ''), 'win': r.get('windows'),
           'ev': r.get('evidence', ''), 'conf': r.get('confidence', ''), 'cav': r.get('caveat', ''), 'refs': [str(x) for x in r.get('refs', [])]}
    return out

def slim_ext(t):
    de = []
    for d in (t.get('discriminating_evidence') or [])[:4]:
        de.append({'p': d.get('pmid'), 'd': d.get('design_feature', ''), 'f': d.get('finding', '')})
    return {'name': t['name'], 'driver': t['driver'], 'expl': t.get('driver_explanation', ''), 'win': t.get('window_summary', ''), 'rep': t.get('replication_status', ''),
            'conf': t.get('confidence', ''), 'cav': t.get('caveats', ''), 'de': de}

cards = []
for cid, g, dc, ds, ex, rows in CARDS:
    recs = [slim_rec(DS[i]) for i in ds]
    exts = [slim_ext(EXT[i]) for i in ex]
    refs = []
    for r in recs: refs += r['refs']
    for e in exts:
        refs += [d['p'] for d in e['de'] if d['p']]
    refs = list(dict.fromkeys(str(x) for x in refs if x))
    confs = [r['conf'] for r in recs] or [e['conf'] for e in exts]
    gr = min(grade(c) for c in confs) if confs else 2
    title = (recs[0]['name'] if recs else exts[0]['name'])
    cards.append({'id': cid, 'g': g, 'dc': dc, 'title': title, 'gr': gr, 'recs': recs, 'ext': exts, 'refs': refs,
                  'rows': [{'l': a, 'B': b, 'D': d, 'E': e, 'k': k} for a, b, d, e, k in rows]})
used = {p for c in cards for p in c['refs']}
for c in cards:
    for e in c['ext']:
        for d in e['de']:
            if d['p']: used.add(str(d['p']))
bundle = {'groups': GROUPS, 'cards': cards, 'pml': {p: PML.get(p, '') for p in sorted(used)}, 'tit': {p: TIT.get(p, '') for p in sorted(used) if TIT.get(p)}}
missing = [p for p in used if not PML.get(p)]
print('cards', len(cards), 'refs', len(used), 'no label', len(missing), missing[:40])
unused = [i for i in list(DS) + list(EXT) if not any(i in (c0[3] + c0[4]) for c0 in CARDS)]
print('records not placed on any card:', unused)
js = '/*THR-BEGIN*/\nconst THR_DATA=' + json.dumps(bundle, ensure_ascii=False, separators=(',', ':')) + ';\n/*THR-END*/'
open(os.path.join(HERE, 'thr_bundle.js'), 'w').write(js)
print('bytes', len(js))
