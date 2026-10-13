import math
def g3(x):
    return float(f"{x:.3g}")
def TH(role, endpoint, prep, etype, pmid, refkey=None, depth="abstract_only", B=None, Bnote="", f=None, wave="", pw=None,
       burst="", exposure="", schedule="", sine=False, dbdt=None, dbdt_basis=None, E=None, E_basis=None, Egeo="", B0=None, note=""):
    d = dict(role=role, endpoint=endpoint, preparation=prep, evidence_type=etype, B_pk_mT=B, B_note=Bnote, freq_Hz=f,
             waveform=wave, pulse_width_ms=pw, burst=burst, exposure=exposure, schedule=schedule,
             dBdt_T_s=dbdt, dBdt_basis=dbdt_basis, E_V_m=E, E_basis=E_basis, E_geometry=Egeo, static_B0_uT=B0,
             pmid=pmid, refkey=refkey, source_depth=depth, note=note)
    if sine and B is not None and f is not None:
        x = 2*math.pi*f*B*1e-3
        d["dBdt_T_s"] = g3(x); d["dBdt_basis"] = "computed"
        e1, e3 = 0.005*x, 0.015*x
        d["E_V_m"] = g3(e1); d["E_basis"] = "computed"
        d["E_geometry"] = (f"computed macroscopic E=(r/2)*dB/dt with dB/dt=2*pi*f*B_pk={g3(x)} T/s (sine-equivalent at stated f); "
                           f"r=1 cm -> {g3(e1)} V/m (value given), r=3 cm -> {g3(e3)} V/m; assumed loop radii, not tissue/dish-specific")
    else:
        if d["dBdt_basis"] is None: d["dBdt_basis"] = "null"
        if d["E_basis"] is None: d["E_basis"] = "null"
    return d
def ES(pmid, refkey, feature, finding):
    return dict(pmid=pmid, refkey=refkey, design_feature=feature, finding=finding)
