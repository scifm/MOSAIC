# swarm-o notebook

Started 2026-10-08T04:35:24+00:00.

## 2026-10-08 05:04 — wakeup 1: scope chosen
- Board: b,c,f,g (w3 ±δ atlases), a (w2 atlas), e,i (joint orbits). Herding on local maps.
  Best so far: swarm-c S1xT1 α=+0.1 → s21 R=1.033 PASS (M2k/M2 = 1.022).
- My family: `global-sobol-w3` (hypothesis 20261008T050333.448Z_swarm-o_hypothesis_0c07).
  S1-S3 x T1-T2 separable stars, n_mesh 48, g_cutoff 8. Tools: work/mk.py (builder), work/sobol1.py.
- Submitted phase 1a: 32 α-only Sobol (seed 7, |α|≤0.4); ids in work/p1a_ids.txt, params in work/gen/p1_params.json.
- Pending: phase 1b β-only (work/gen/p1b, 16 files) once in-flight < 32 allows.
- Note: |α|≤0.4 in 6 terms moves M2k/M2 0.98–1.88 per swarm check; M2 bound 3x not binding yet.
- Next: collect, fit R vs M2k/M2, quadratic surrogate; then CMA-ES.

## 2026-10-08 05:32 — wakeup 2
- Phase 1a result: 3/32 PASS (best 0.842 req_24f5), 28 collapsed; req_8a50 R=1.18 but manifold split. Posted result 20261008T053118.469Z_swarm-o_result_78da with coverage. Dropped 1b (β separable).
- Board learned (h, i, e, ad, ap): Z2xZ2 half-translation rule → only invariant orbits have TL slopes; S1T1⊥ (gc-lock) and S2T1∥ are the only linear ones.
  Leader: ad S1T1⊥ x=0.3 → s21 1.36 (req_d746); x=0.6 → 1.108; i fb45 S2T1∥ x=0.15 r46 1.17.
- New tools: work/orbits.py (orbit enumeration, verified vs swarm-i fa76), work/orbmk.py (6 achiral invariant directions), work/sobol2.py.
- Phase 1c submitted: 32 Sobol (seed 23) in 6-D invariant box; ids work/p1c_ids.txt, params work/gen/p1c_params.json. Hypothesis 20261008T053138.467Z_swarm-o_hypothesis_9d0d.
- Budget: 64/500 charged after this.
- Next: collect p1c, fit quadratic surrogate (R vs x), CMA-ES; owe a critique post (rule 11).

## 2026-10-08 06:22 — wakeup 3
- Phase 1c: 28/32 PASS, 17 ≥1.05, best s21 1.398 (req_cc8b, x3=0.38). Results: work/p1c_ids.txt.res.json. Posted 20261008T062110.045Z_swarm-o_result_5ff7.
- Harvest (work/harvest.py, set OMP_NUM_THREADS=1! swarm show otherwise burns 7 CPU-s): 121 public points in my 6-D subspace → work/harvest.json.
  S2T1∥ axis: s21 peaks ~1.52 at x3 .45 (af c310), 1.575 at (-.1,0,.6) (af bea6); r46 peaks 1.420 at x3≈0.40 (af c380, e d888), drops at 0.6 (1.376).
- Quadratic fit (work/fit.py): rms .045 / LOO .066; all directions concave; off-plane grads negative at ridge. Not trusted (cones).
- Phase 2a submitted: ±0.06 in x2,x4,x5,x6 at center (0,0,0.4,0,0,0)=af c380. ids work/p2r_ids.txt. Budget 72/500.
- Next: if all lower → close low-star subspace (coverage). Then consider: r56 status of leaders; a critique post (owed); maybe beta-chiral dressing at the ridge if aa doesn't cover it.

## 2026-10-08 06:45 — wakeup 4: family closed
- 2a ridge cross-curvature (center af c380 s21 1.500 / r46 1.4197): max gain +0.008 s21 (S2T2−), +0.004 r46 → local max. Odd slopes flip s21↔r46 (S2T2 −0.64 vs +0.19; S3T3 flat on s21, +0.26/+0.29 on r46).
- Posted closing result + coverage 20261008T064346.035Z_swarm-o_result_48ca; mailed swarm-y (critique).
- Board frontier: S2T1∥ + chiral β (S4/S7/S9/S10×T1) + negative high-shell α: t/ap s21 2.8–3.3, r46 up to 4.07 (ap 7a96). r56 stalled for everyone (c request 8cff). y: leaders strongly non-ideal (F<0 patches).
- Many agents now reserve/verifier (at, x, u, w, a, r, k). Budget: 72/500 used.
- Next options: (i) perturbation-robustness cloud around a top leader (landscape width vs cluster spread); (ii) reserve. Decide after r56 starts moving.

## 2026-10-08 07:20 — done
- No uncovered direction worth budget; frontier (chiral β + dressing) saturated by ≥10 agents, reserve pool large. Ran `swarm done` (72/500 used).
