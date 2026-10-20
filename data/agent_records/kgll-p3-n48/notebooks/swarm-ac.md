# swarm-ac notebook

Started 2026-10-14T10:25:29+00:00.

## Wakeup 1 — 2026-10-14 ~11:25–11:40 UTC
- Read board (33 posts). Board is saturated on S1–S3 orbits, surrogates (h,o,u,t,x,z), finite size (q,y,ae), mechanism (k,s), high-shell α orbits (h S4–S6, w & v S7–S10), C3-breaking (ad), random survey (af).
- Leader: swarm-c d698 = phase-only β=0.03 on ONE ±60° orbit of |G|²=3×T1: s21 1.2494, r46 1.4041 (r56 pending). Phase-only chiral leaders dominate.
- swarm-a file labels: S{|G|²}_T{|R|²}_{a|b}{p|m}; e.g. S09_T4 α: 0.53–0.60, S12_T4 α: 0.38–0.44 (high shells very sensitive, negative).
- Tools written: work/geom.py (pair stars, joint C3 orbits, delta = angR − angG mod 180; rotation maps G:(m,n)->(m−n,m), R:(R1,R2)->(−R2,R1+R2); verified Cartesian), work/proxy.py (no-ED gauge-invariant form-factor sensitivity Q=λ_G^{kk'}λ_0^{k'k}); proxy table in work/proxy_rows.json: high shells as sensitive as low.
- Chose family `hs-odd`: 45 chiral-odd β directions on |G|²=7..21 × T1–T3 (per entry ±b on orbit ±δ). Posted hypothesis 20261014T113736.879Z_swarm-ac_hypothesis_aef8; mailed swarm-f (who planned all 54, low shells first).
- Inputs: work/b1/ (90 files, b=0.03/entry), split into b1a (|G|²=7,9,12), b1b (13,16), b1c (19,21). work/mk_hsodd.py builds them.
- Next: submit b1a (30), then b1b, b1c as slots free. Then lines along top odd directions; combine with leader.
- Submitted b1a (30 req) at 11:39; ids in work/b1a_ids.txt. b1b/b1c pending (32 in-flight cap).

## Wakeup 2 — 12:05 UTC
- 7 agents claimed outer chiral-odd β (a already charged at ±0.002). swarm-a: outer shells collapse at rms 0.03–0.05 → my ±0.03/entry (rms 0.073) is way non-perturbative. Withdrew all 30 b1a (charged ~25–30). Posted abandon 20261014T121221.922Z_swarm-ac_abandon_d131 with coverage.
- Board state: STRONG claim by swarm-c d698 (S2×T1 +60 β 0.03): 1.249/1.404/1.347; ⊥ α −0.45 leader 1.64/2.63/2.44 (past a manifold FAIL at −0.35, ak critique); f S3×T1 chiral-odd β +0.05: 1.558/1.641/1.560.
- New role `hfdisp` (0 evals): does the HF interaction-induced dispersion predict R_gap? work/hf.py (λ via solver formula; V_Coulomb d_l=0, D_l=0.1; contact part V(0) subtracted exactly, Hartree−Fock cancellation identity), work/collect.py (leaderboard ids → swarm show → ed_input block → work/board.json), work/feat.py (features on s21 and r46 meshes → work/feat.json).
- Parent HF: s21 ptp 2.82e-2 (H 4.69e-2, F 1.87e-2) in my units (no 1/A factor).

## Wakeup 3 — 12:25 UTC
- Collected 354 board requests → work/board.json; HF features → work/feat.json (352).
- RESULT (posted 20261014T122614.325Z_swarm-ac_result_5402): HF dispersion does not rank directions (first-order maps ρ ≈ −0.2…+0.2); line correlations are trivial. ⊥ α −0.45 flattens HF std to 0.23 (ptp 0.13); phase-only leaders <1% change; S2×T1 ∥ α +0.05 widens (+6%) yet R +22–33%.
- Causal test running: work/flat.py minimizes HF std over 24 non-⊥ α orbits (S1–S3×T1–T3) at rms(Reγ)=0.05/0.1/0.2 (Powell). Logs work/flat_*.log, outputs work/flat_r*_s1.json. Then submit 3–6 flattest to s21 (family hfdisp, ≤10 evals).
- 12:44 HF-flattening optimizer (non-⊥ α, 24 orbits S1–S3×T1–T3): std 0.62 @rms0.05, 0.43 @0.1, 0.26 @0.2 (Σ|α|>2.5, rescaled to 2.4 → rms 0.166, std 0.34). Flattest direction dominated by S1×T1 ±30 α<0 and S1×T2/T3 α<0 (note: c found S1×T1 ±30 α−0.05 → R 0.93!). Prediction: flattening alone won't help.
- Submitted 4 (work/hf1_ids.txt): flat_r05 620d, flat_r10 08c7, flat_r20s 9788, wide_r05 d906 (control, HF std 1.37).

## Wakeup 4 — 13:15 UTC
- Records now R≈5: c662 (h union α+β) 4.76/5.23/4.67 STRONG; 8c01 (t) 4.82/5.19/4.55. Density controls ≈1 (k). g critique: d_sc=0.1 parent near zero mode (Δ∝d³) → R amplified; p rebuts the contact part.
- HF features of records: c662 std 1.155 (WIDER), 9462 1.131 (wider), 8c01 0.866. Confirms HF dispersion is not the mechanism.
- My 4 hfdisp evals still pending (broker slow; swarm-o reports stuck lane). 16 hs-odd withdrawn still pending.

## Wakeup 5 — 13:46 UTC
- 14 of withdrawn hs-odd landed: mostly FAIL (splitting), as expected at rms 0.073; best PASS 0.83; one FAIL 1.27 (6f96 g9 r1 +30 bp). hfdisp 4 still pending.
- Board record f5f1 (o): 6.28/8.33/8.12, Σ|β| 1.88 near cap. Phase-only s21 ceiling ~1.72 (f). g retracted 1/d² critique.


## Wakeup 6 — 14:17 UTC (final)
- hfdisp causal test landed: flat_r05 0.733 PASS, flat_r10 0.302 FAIL, flat_r20s 0 FAIL, wide control 0.770 PASS → HF flattening not causal. Posted 20261014T141746.088Z_swarm-ac_result_d8aa with coverage. hfdisp closed.
- Board: records ~6–10× at s21 (av cos2d 10.39 s21; o f5f1 6.28/8.33/8.12 STRONG), cap-limited. Many agents finishing.
- Ran `swarm done` (34/500 charged). Loop stopped.
