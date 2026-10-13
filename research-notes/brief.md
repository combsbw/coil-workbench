# Shared brief: activation thresholds for PEMF mechanistic targets

GOAL. For each biochemical/biophysical mechanistic target of pulsed/low-frequency magnetic-field therapy in your scope, establish from the primary literature:
 (1) the target and the therapeutic modality(ies) it serves (pain relief/analgesia, bone & cartilage repair, wound/inflammation resolution, vascular/angiogenesis, neuro-modulation/neuroprotection, muscle/tendon recovery);
 (2) the ACTIVATING VARIABLE: is the response driven by the field amplitude B itself (static or AC), by dB/dt (i.e. the induced electric field E = -dΦ/dt/loop, E ≈ (r/2)·dB/dt), by the induced current density/membrane polarisation, by frequency/pulse-width/waveform spectral content, by the ratio of AC to static field, or unresolved? Cite the *experimental design feature that discriminates* (e.g. effect scales with f at fixed B → dB/dt/E; effect same at different f but same B → B; effect depends on a static field B0 → resonance/radical-pair; dose-response in E at fixed geometry; sham-coil vs. conductive-medium controls; blockers);
 (3) THRESHOLDS: lowest reported effective level, optimal/plateau level, level where effect disappears (window or inverted-U), and any adverse/safety level. For each, record the numbers actually reported and their conditions.

UNITS / CONVERSION RULES (important, this feeds a calculator):
 - Report B as peak mT (state if the paper gives rms or peak-to-peak and convert; say so). 
 - Report dB/dt in T/s. If not reported, you may compute: sine dB/dt_pk = 2π f B_pk; trapezoid/pulse dB/dt ≈ B_pk / t_edge; mark as "computed" and show the formula and inputs.
 - Report induced E in V/m. If the paper reports it (e.g. mV/cm → ×0.1 = V/m... careful: 1 mV/cm = 0.1 V/m), quote it as "reported". Otherwise you may compute macroscopic E ≈ (r/2)·dB/dt for a stated loop radius r (state r; use the tissue/culture-dish geometry in the paper when given; for cultures say whether it is the dish-scale E, not cell-scale). Mark "computed".
 - Always keep reported vs computed separate. NEVER invent numbers. If a number is not in the paper, put null.
 - Also record frequency (Hz), waveform (sine, quasi-rectangular pulse, burst, monophasic/biphasic), pulse width (ms), duty/burst structure, exposure time per session, session schedule, static background field if known, and the biological preparation (cell type / species / human condition).

CITATION RULES. Use the PubMed MCP tools (search_articles, get_article_metadata, lookup_article_by_citation) — load them with ToolSearch (query "select:mcp__PubMed__search_articles,mcp__PubMed__get_article_metadata,mcp__PubMed__lookup_article_by_citation,mcp__PubMed__get_full_text_article,mcp__PubMed__find_related_articles"). Every reference you rely on MUST be verified against PubMed (PMID, first author, year, title, journal, volume/pages, DOI). Use get_full_text_article (PMC) when you need exact numbers from methods. If you can only see an abstract, say so in the record ("abstract only") and only use numbers stated in the abstract. WebSearch/WebFetch may be used to locate papers but verify the PMID in PubMed. Papers already in the workbench library are listed in /tmp/claude-0/thr/existing_refs.tsv (key, PMID) — reuse their keys when you cite them (put the key in "refkey"), and do not re-add them as new refs; but DO read them for threshold numbers if relevant (full text if PMC). Prefer quantitative dose-response studies, replications, null/negative studies and independent replication over narrative reviews. Report negative and null findings.

SEARCH STRATEGY. Run many searches (target name × "pulsed electromagnetic field" × "dose-response" / "amplitude" / "frequency window" / "induced electric field" / "dB/dt" / "threshold"; also look for sham/null replications). Aim for roughly 25–45 verified, relevant papers in your scope (not padding). Quality > count.

OUTPUT. Write ONE JSON file to the path given in your assignment (valid JSON, UTF-8), with this schema, then reply with a SHORT summary (<= 250 words: how many targets, how many new refs, the 3–5 most important quantitative findings, and any uncertainties). Do not paste the JSON in your reply.
{
 "scope": "...",
 "targets": [
  {
   "id": "short_snake_case",
   "name": "Mechanistic target, e.g. 'Ca2+/calmodulin–eNOS–NO/cGMP'",
   "level": "biochemical|membrane/ion channel|cellular|tissue-neural",
   "modalities": ["pain relief", "..."],
   "driver": "dBdt_E | B_amplitude | B_AC_over_B0 | waveform_spectral | frequency_window | combined | unresolved",
   "driver_explanation": "2–5 sentences: what actually activates it and how the literature distinguishes B from dB/dt/E, including counter-evidence",
   "discriminating_evidence": [ {"pmid":"","refkey":null,"design_feature":"...","finding":"..."} ],
   "thresholds": [
     {"role":"lowest_effective|optimal|plateau|no_effect_below|loss_above|adverse|safety_limit",
      "endpoint":"...","preparation":"...","evidence_type":"invitro|animal|human_rct|human_other|theory|standard",
      "B_pk_mT":null,"B_note":"","freq_Hz":null,"waveform":"","pulse_width_ms":null,"burst":"","exposure":"","schedule":"",
      "dBdt_T_s":null,"dBdt_basis":"reported|computed|null","E_V_m":null,"E_basis":"reported|computed|null","E_geometry":"",
      "static_B0_uT":null,"pmid":"","refkey":null,"source_depth":"fulltext|abstract_only","note":""}
   ],
   "window_summary": "1–3 sentences giving the target window in B, dB/dt (T/s), E (V/m), frequency, with honest ranges",
   "replication_status": "independent replication / single group / contested",
   "confidence": "high|medium|low",
   "caveats": "..."
  }
 ],
 "new_refs": [
  {"pmid":"","first_author":"","authors_short":"Smith J, Doe A, et al.","year":0,"title":"","journal":"","citation":"vol(issue):pages","doi":"","pmcid":null,"type":"invitro|animal|rct|human|review|meta|theory|standard","systems":["nervous|vascular|immune|muscular|measurement|general|plant"],"mechs":["induction|camno|vgcc|adenosine|trpc1|radical|icr|magnetite|effectors|endogenous"],"direction":"+|0|±|th","summary":"1–3 sentences, PARAPHRASED (never copy abstract text), include the key numbers"}
 ],
 "cross_cutting_notes": "anything relevant outside the strict scope"
}
