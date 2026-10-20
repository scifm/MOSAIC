# swarm-c notebook

Started 2026-10-14T10:23:56+00:00.

## 2026-10-14 11:15 — wakeup 1
- Read brief, docs 40/46, ADR-0040, kdep_envelope. Parent w1c: Δ s21 = 2.2586e-4, r56 = 2.590e-4.
- Board: swarm-a (axis-map) and swarm-b (linmap) both doing the 60 full-star ± map (same steps). Mailed both re duplication.
- My family `jorb` (hyp post 20261014T111331.227Z_swarm-c_hypothesis_ecea): joint (G,R) C6 orbits.
  Pair stars {±G},{±R}; 3x3 pair matrix splits into 3 joint-rotation orbits (⊥/∥ and chiral ±θ).
  Tools: work/joint.py (orbits, block builder), work/mk.py, work/gen_s1.py. Naming gXrY = |G|²=X, |R|²=Y (g3 = S2, r3 = T2).
- Submitted stage 1: 36 reqs (work/s1/), g1r1 {90,±30}, g1r3 {0,±60}, g3r1 {0,±60} × α±0.05, β±0.03 (per orbit entry).
- Caveat to check: Nk=21 cluster is chiral → ±θ split partly a cluster effect; rectangular rungs test it.
- Next: collect, compute slopes per orbit, chiral asymmetry; compare with a/b full-star map (full slope = mean of orbit slopes × ... at equal per-entry coef, full α_f ↔ pair α_f/3 on all 9).

## 2026-10-14 11:35 — wakeup 2
- Stage 1 done (36): huge linear responses. Leaders s21: S2×T1 +60 β+ 1.2494 (d698), −60 β− 1.2403, S2×T1 ∥ α+ 1.2166, S2±60 α− 1.178/1.168, S1⊥ α− 1.171 (r46 1.170), S1+30 β+ 1.160 (r46 1.159).
  MT symmetry confirmed: (θ,α)≡(−θ,α), (θ,β)≡(−θ,−β) to <0.9%. Full stars cancel (∥ vs ±60 opposite α slopes). s21≈r46 within 0.6%.
- ~20 agents piled onto my channels (j,q,r,ae,s line scans; x,z,e combos/CMA; h,o,t,u surrogates; g orbits). Dropped my stage-3 CMA.
- Posted result bc24 (with coverage), herding note, mailed j,q,r,x,u,ae,z,g.
- Box/mesh convergence non-issue (work/conv.py): kernel weight outside g_cutoff 8 ≤4e-5 at small steps; only qmax matters.
- Submitted 8 within-orbit α·β corners (work/s2/): g3r1 +60 and g1r1 +30.
- Next: fit per-orbit quadratic in (α,β) incl cross term; then maybe T2/T3 copies of S2 α orbits (thin spot 4), or mechanism help.

## 2026-10-14 11:56 — wakeup 3
- d698 (S2×T1 +60 β+0.03, phase-only) → STRONG: s21 1.249, r46 1.404, r56 1.347, conv46 1.404 (=r46: conv rung not independent for LL0, per swarm-l). Posted claim 893d.
- 37dc (S2×T1 ∥0 α+0.05) STRONG 1.217/1.327/1.276 — α, mailed swarm-k for matched-density control.
- ad6b, 884a, dbab SUGGESTIVE (conv46 pending).
- Board leader now ⊥ α line (j/q/r ea28): s21 1.639, r46 2.63.
- My thin spot 4 got 6 takers, outer chiral β 7 takers → herding note 2 (5564).
- 8 within-orbit α·β corners still pending.
- Plan: analyze corners; consider role as verifier/critic; keep budget (~456 left).

## 2026-10-14 12:17 — wakeup 4
- ad6b, 884a, dbab now STRONG too (all α except dbab β). swarm-u independently verified claim 893d (S00 identical to parent pointwise). swarm-k queued density controls for 37dc/ad6b/884a.
- Board: ⊥ α −0.45 (j/q/r) STRONG 1.64/2.63/2.44 — density controls lower gap (k). f claims S3×T1 chiral-odd β 1.558/1.641/1.560 STRONG. x combos s21 1.92.
- Herding note 2 worked: a owns outer β map; ar owns inner T2/T3 α map; i/ac/as/ap/aq deduped.
- 8 corners still queued (45 min). Waiting.

## 2026-10-14 12:44 — wakeup 5
- Leaders now R ~4.8 (s21) / 5.2 (r46) via multi-orbit α+β combos (t 8c01, h c662). α·β superadditive (h).
- Key insight posted (note 88b2): R_beyondM2 parent 0.12 (s21)/0.137 (r46); leaders 0.60/0.72 ≈ smooth static w3/w2 level (~0.7, doc 46).
  → k-dep "repairs" w1c up to the M2 law. Test: does anything exceed R_beyondM2 ≈ 0.7?
- e critique: PES ent gap drops 13.4 → 3–5 in leaders (gates pass).
- Corners: g1r1+30 ambp 1.0965, apbp 1.1987 (≈ additive: ap 1.046 + bp 1.160 → 1.206). g3r1 corners pending.

## 2026-10-14 13:11 — wakeup 6
- Corners done → result 770f: within-orbit α·β additive (H_xy≈0); superadditivity is cross-orbit. a396 (S2×T1+60 α−,β+) s21 1.324 r46 1.632.
- Replied to g's 9d4e critique (parent Δ/Δ_LLL 1.24/1.38, same order as uniform LL0; no special amplification).
- Board records: c662 (h) STRONG 4.76/5.23/4.67; 8c01 (t). Density controls all ≈1 (k). av: records follow α∝cos2δ, β∝sin2δ rule.
- i running static M2 scan (M2 2..8) to calibrate my 88b2 note.
- Role now: verifier/critic; budget 452 unspent. Only spend on gaps nobody covers.

## 2026-10-14 13:42 — wakeup 7
- New record o f5f1: R 6.28/8.33/8.12, R_beyondM2 0.78/1.15/1.16 → first past M2 law on rectangles. Σβ=1.88 near 2.0 cap. Posted note (follow-up to 88b2).
- g retracted 1/d² critique after my reply. ap: leaders' γ on uniform LL0 lower gap → gain is γ×ρ* cooperation.
- Stuck-lane reports from o, j, m (ops). My 3 r56 promotions still pending.

## 2026-10-14 14:13 — wakeup 8
- i's static calibration (365e) falsified my 88b2 framing: w1c is the static optimum of its shape family; Δ/(M2 Δ_LLL) is shape-dependent. Posted correction.
- s21 leaders now ~R 10 (av e0a8 cos2δ rule, s c325 noQ0). o f5f1 STRONG claim 2208 on the Σβ boundary. t asks human about representation-dependent Σ caps (789e).
- p: rotation test of k≠k' handling passes (1.6e-6). y: kernel exact at n_mesh 48.
- Many agents finishing (d, ak, g, p, q, aj, au done). My 3 r56 promotions still pending.

## 2026-10-14 14:44 — wakeup 9 (final)
- Records ~R 10 STRONG (av e0a8, s c325), cap-limited. My family is complete; posted final coverage result. Running swarm done (44/500 charged).
- r56 promotions 08d7, c07d, a396 still queued (free, will land in store).
