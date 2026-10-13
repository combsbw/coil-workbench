# Threshold research: status log

Scopes (each writes research-notes/thr_<n>_*.json; progress is checkpointed here and in git).

| # | Scope | State |
|---|-------|-------|
| 1 | Neural / induced-E thresholds | not finished: no output yet |
| 2 | Pain / analgesia dose studies | partial: ref metadata only (salvage/gen/refs_meta.py, 68 refs), no target records |
| 3 | Ca2+/CaM/NO, vascular | not finished: no output yet |
| 4 | Bone / cartilage / tendon | partial: 83 verified refs (salvage/refs1-4.py), no target records |
| 5 | Adenosine / immune / TRPC1 | DONE: thr_5_adenosine_immune.json (8 targets, 63 refs) |
| 6 | B-amplitude-driven mechanisms | DONE: thr_6_B_driven.json (17 targets, 94 refs) |

2026-10-13: first run lost most notes to a rate limit because agents wrote output only at the end. Scopes 5 and 6 recovered from their builder scripts.

## Earlier run (2026-10-12 22:38, seven clusters + verifiers): files recovered

research-notes/loop/cluster1_ca_nos.md, cluster2_adenosine_inflammation.md, cluster3_bone_cartilage.md, cluster4_nerve_pain.md,
cluster5_mito_ros_radicalpair.md, cluster6_vascular_wound_muscle.md, cluster7_dosimetry_B_vs_dBdt.md, verify_1_2.md, verify_3_6.md.
These cover every scope, so the remaining work is synthesis plus checking, not new searching.

## Synthesis progress (2026-10-13, resumable)
Dataset records are written to research-notes/dataset/*.json right after each cluster is read. Order: 7 (dosimetry), 4 (nerve/pain), 1, 2, 3, 5, 6, then thr_5 and thr_6 JSON merge.
- [x] cluster7 read -> dataset/c7_dosimetry.json
- [x] cluster4 read -> dataset/c4_nerve.json
- [x] cluster1 (Ca/NOS) -> dataset/c1_ca_nos.json  - [ ] cluster2 (adenosine/inflammation)  - [ ] cluster3 (bone)  - [ ] cluster5 (mito/ROS/radical pair)  - [ ] cluster6 (vascular/wound/muscle)
Verifier corrections to apply: verify_1_2.md section A, verify_3_6.md sections 1-2 (Tsai E_rms, Xu 75>45>15 ordering, Wu 2018, Prucha 11.8 T/s, Bragin 3 h, Cleary, Farndale cAMP, Ghibelli not static, Lin 2011 not Ferrara).
