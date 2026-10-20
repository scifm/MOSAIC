# swarm-g notebook

Started 2026-10-14T10:24:10+00:00.

## Wakeup 1 — 2026-10-14 ~11:18Z
- Board: swarm-a (axis-map) and swarm-b (linmap) BOTH claim the 60-axis separable ±map (S1-S10×T1-T3, α=±0.05, β=±0.03). I don't duplicate.
- Geometry (work/geom.py): solver G basis 120°, direct R basis 60°; ẑ×G(m,n) = (−n,m) maps S(|G|²=1,3,4) → T1,T2,T3 exactly (one flux/cell). rotG(m,n)=(−n,m−n), rotR(p,q)=(−p−q,p).
- Block limit: stars must be inversion-closed → γ spans cos(Gr)cos(kR) only; sin·sin (and comoving cos(Gr−k·ẑ×G)) unreachable. Posted note _note_7dca and request _request_9c9e.
- Family `joint-orbit` (hypothesis _hypothesis_70a9): C3-invariant matchings D_c = Σ_i P_i Q_σc(i) of the 3 G-pairs to 3 R-pairs. Separable = (1/3)(D0+D1+D2) in pair units. Steps per-pair α=±0.0289, β=±0.0173 (rms-matched to axis maps).
- Generator work/gen_joint.py OUT combos(|G|²x|R|²) [kinds]. File tags use |G|² (S3 = |G|²=3 shell); "P" marks the perpendicular (R=ẑ×G) channel.
- Submitted 30: S1T1 (12), S3T3 (12), S4T4 α (6). Pending: work/b1_later = S4T4 β (6).
- Next: read results, compute slope/curvature per channel, compare Σ_c slope with separable slopes from a/b; then off-diagonal combos.

## Wakeup 2 — 2026-10-14 ~11:45Z
- Board exploded: ~45 agents; joint-orbit space heavily herded (c jorb maps S1×T1,S1×T2,S2×T1; f chiral-odd β all 54; j/q/r ⊥ lines; e orbmap2 S2×T2..S3×T3; 3 CMA on min-over-clusters z/ag/n; am phase CMA; 4 surrogates; ao/av/aj kprof; ad/al/ah nematic; w/v/h outer α; a/ac/ap outer χ-odd β; k/s mechanism; p/u/y verify/audit).
- My batch 1 (30 evals, all PASS) posted as result _result_d1d4 with coverage. Key: S1×T1 at 0.0289/entry: ⊥α− 1.1017 (63eb), +30β+ 1.0966 (79d4, r46 1.0914), −30β− 1.0923. S2×T2 / S3×T3 channels weak ≤ +3%. ⊥ channel not special beyond S1. Did NOT submit work/b1_later (S3×T3 β).
- Leaders: f S3(|G|²=4)×T1 chiral-odd β 0.0167/entry → s21 1.558 (e5d5); c S2×T1 +60 β0.03 → s21 1.249 r46 1.404 (d698); c ⊥α−0.05 (7133) s21 1.171 r46 1.170 r56 1.160 → conv46 (suggestive already).
- Mechanism notes: MT symmetry (f): TL-linear directions = α mirror-even, β chiral-odd. s: ⊥ channel half static LL mixing (Q=0).
- Mailed j,q,r: I'm not scanning ⊥ further.
- Decision: space saturated; hold budget (30/500 used). Role → critic/verifier; look for a real hole. Candidate later task: phase-only (beyond-M2-clean) refinement near any α-containing winner; neighbourhood checks.
- Next: check r46/r56 of f's steep S3×T1 leader; critique (rule 11).

## Wakeup 3 — 2026-10-14 ~12:20Z
- Leaders now: j/q/r S1×T1 ⊥ α −0.45 (ea28): s21 1.64, r46 2.63, r56 2.44, conv46 2.63 (STRONG label on leaderboard; ak flags s21 branch change; s flags half static LL mixing Q=0). f claim 728b STRONG phase-only S3×T1 χ-odd b=0.05: 1.558/1.641/1.560. c claim 893d STRONG phase-only S2×T1 +60 β0.03: 1.249/1.404/1.347. h: outer S4×T1 α ~1.57/1.72/1.61. x combos s21 1.92.
- My 935d (S2×T2 ch2 β−) reached suggestive: 1.0218/1.0102/1.0374.
- Did 0-eval independent check of f's claim (work/claimcheck.py REQ: orbit δ, MT self-map on γ, S00 ratio, band distance). Posted note _note_7d9a. Key numbers: phase leaders band distance ~3e-4 mean (<1e-3 max) for +40–56% gain; ea28 2.9e-2 mean / 0.2 max, S00 ratio 0.41–3.15. Gain per band distance depends strongly on direction.
- Found: no many-body gauge-covariance test (gate 3 solver half) in julia/test; posted request _request_137b to human. Mailed f.
- Budget 30/500. Still holding; role = verifier. Next: watch for human answers (cos·cos request 9c9e, gate-3 137b); check further claims; consider band-distance-normalised ascent if nobody does it.

## Wakeup 4 — 2026-10-14 ~12:52Z
- New leaders: surrogate steps t 8c01 (s21 4.82, r46 5.19) and h c662 (4.76/5.23/4.67), multi-orbit α+β, band distance ~7e-3, abs gap ~1.1e-3 W0 (parent 2.26e-4, Δ_LLL 1.83e-4). j posted STRONG claim 3d0f (ea28). x: super-additive orbit combos 1.92/2.15/1.99.
- p is running a broker-side proxy for my gate-3 request (C6 rotation test: p_req_180c/57ac/3130).
- Posted critique _refutation_9d4e: V=V0 tanh(qd)/q, d=0.1 → parent gap ∝ d³ (ideal band, near zero mode); non-vortexable admixture ε gives ~ε² d → R−1 ~ 100 ε². R_gap not transferable; report absolute Δ. Key-facts: LL-mixed static optima gap ~0.03 W0 vs leaders ~1e-3.
- Posted request _request_530e: d_sc ∈ {0.1,0.3,1.0} control on parent + e5d5, ea28, 8c01 (s21 + 4×6). Mailed j,f,c,t,h.
- Budget 30/500 still.

## Wakeup 5 — 2026-10-14 ~13:24Z
- p (refutation d376) and u (two-body test 4869) refuted my 9d4e 1/d² argument: contact is inert for a single-component band (antisymmetry), so breaking vortexability only reaches the q² (d³) term; no scale separation. c: Δ/Δ_LLL parent 1.24, d698 1.54. RETRACTED in note _note_adae; mailed p,u,c,j,f,t,h. LESSON: in the scalar pure-LL0 k-GLL, the multicomponent contact channel does not exist; check the single- vs multi-component contraction before scale arguments.
- Records: h c662 STRONG claim 0069 (4.76/5.23/4.67, conv46 5.23); t 8c01 STRONG claim 4fb4 (4.82/5.19/4.55); o 8f9d s21 5.33. Density controls (k) exclude density for α claims. ap lllref: the leaders' γ on uniform LL0 does nothing or hurts → gain needs γ×ρ* cooperation. av: records follow the angular rule α∝cos2δ, β∝sin2δ on S1/S2×T1.
- Budget still 30/500.

## Wakeup 6 — 2026-10-14 ~13:55Z — DONE
- Records now R≈6–8 (o f5f1 strong 6.28/8.33/8.12/8.33; s 9a30 s21 7.35; x d2de 7.22). p's rotation test passes (5aad). Many agents finished.
- Decided to stop: no unowned sector; 30/500 spent. Posted final summary via `swarm done`.
