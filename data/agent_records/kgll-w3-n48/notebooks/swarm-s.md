# swarm-s notebook

Started 2026-10-08T04:35:39+00:00.

## 2026-10-08 05:12 UTC — wakeup 1: scope chosen, gen 0 submitted
- Read brief, docs 40/46, notes §7.5/8.4/12, board. Board: single-term atlases (b,c,f,g), w2 atlas (a),
  even Hessian (d), joint orbits (e,i), chiral beta (j), half-cell symmetry (h), parent-shaped (k),
  global Sobol (o). All optimise the s21 screen value.
- Early data: e's S1xT1 90-deg orbit c=0.05 -> s21 1.105; S2xT1 0-deg orbit -> 1.099; separable
  alpha[S1,T1]=0.10 (c req_6492) -> s21 1.033, r46 1.048 PASS (transfers at 4x6!). beta even-negative.
- My family `robust-cma-w3` (hyp 20261008T050950.337Z_swarm-s_hypothesis_471b): CMA-ES, fitness =
  broker R_gap_min over all ladder clusters reached (free promotions), FAIL -> 0. 18-D alpha in
  C6 joint orbits S1-S3 x T1-T2 x d (per-entry alpha c). lam 12, mu 6, sigma0 0.02 (post said 0.03;
  lowered before submitting since 18-D sum would be large), seed 20261008, box |c|<=0.3, 3*sum|c|<=2.4.
- Tools: work/kgll.py (stars, pairs, orbit block, check), work/cma_driver.py (step --submit; state
  work/cma_state.json), work/collect.py + work/table.py (board dataset).
- Mailed e and i about overlap.
- Next: wait for gen 0 ladders, `python work/cma_driver.py step --submit`.

## 05:31 — wakeup 2: re-scoped
- Board exploded (~45 agents). Key facts: swarm-h Z2xZ2 half-cell magnetic-translation rule -> only
  invariant orbits (pair rule m≡R2, n≡R1 mod 2) can have TL first-order slope. Invariant (my labels):
  S1T1 d1(90°), S2T1 d0(0°), S1T2 d0, S2T2 d2, S3T3 d0/d1/d2, S5T1 d1, S5T2 d0. Verified with my code.
- e: S2T1∥ c=0.3 -> s21 1.505 (M2k ratio 1.63); i: A=0.15 orbits s21 1.19 r46 1.16. Everyone herding on
  the S1T1⊥/S2T1∥ plane (e, i, af, h, ap, b, ac, ad).
- iso18 gen 0: s21 0.79–1.04; 3 promoted (10f6, 8cc5, 1b7a) pending r46. Run stopped (state work/cma_state.json,
  CMA_RUN=iso18). af's critique accepted (note 20261008T053014.992Z_swarm-s_note_1573).
- Run 2 `inv9`: 9 invariant orbits, mean (0.1,0.1,0...), sigma 0.04, lam 10, box 0.4; state work/cma_inv9.json.
  gen 0 submitted (10 req). Budget used: 22.
- Next: tell inv9 gen0 when ladders done; report iso18 transfers.

## 05:50 — wakeup 3: waiting on inv9 gen 0 ladders
- iso18 transfers (s21 → r46): 10f6 1.025→1.030, 8cc5 1.043→1.0435, 1b7a 1.039→1.024; r56 pending.
- inv9 gen0 s21: 0.63(FAIL, manifold split; S5T1⊥ c=0.138) … 1.47 (9519: S1T1⊥ .116, S2T1∥ .133). 8/10 ≥1.02.
- Board: leaders e/af plane r46 ~1.41; au nocomov s21 1.57; chiral β hi-shell (w, am) r46≫s21 — r56 decides.
  ao: S1T1⊥ gain needs w3's S3 harmonic (offset rule, g/b). ab: fa76 beats M2-matched static by ~15% (s21).
- Queue slower now (confirm21 pending ~15 min).

## 06:12 — wakeup 5: inv9 gen0 told, inv13 launched
- Board: chiral-β (S4/S7/S9/S10×T1, Z2-invariant, swarm-w/j convention) dressing of S2T1∥ → s21 2.03, r46 2.23
  (j ba1f); t's GP s21 2.48. r56 still pending for EVERYTHING incl. parent → broker r56 bottleneck.
- inv9 gen0 told (fitness min over ladder at r46): best 9519 1.474/1.485. inv9 paused (gen1 inputs written, NOT submitted).
- Driver now tells at r46 (WAIT_FOR), fitness = min(s21,s21c,r46[,r56]), FAIL anywhere → 0.
- inv13: 9 α orbits + chi7/13/19/21 (pattern work/chiral_T1_ba1f.json from j ba1f; β = 0.25 x).
  M0 (0.05,0.18,0..,0.048×4), σ 0.03, λ 11. gen0 submitted (11). Budget used 33.
- Posted result 20261008T061216.093Z_swarm-s_result_ef44. Replied d re chiral α in 9519 (S3T3 d0≠d2, small).
- TODO: post r56 of 9519 etc when in; ablation of 9519 chiral α if r56 survives.

## 06:35 — wakeup 6: inv13 gen0 told (best 0d42 s21 2.380 / r46 2.369), gen1 submitted
- gen0 fits: 2.369 (0d42), 2.346 (6357: s21 2.346 r46 2.705), 2.10 (d4c0), 1.91, 1.73, ... min 1.34.
  Pattern: r46 > s21 when χβ large (e0a2 χ7=0.15: s21 1.59, r46 2.38) — CMA objective penalizes that.
- σ 0.028; mean S1T1⊥ .068, S2T1∥ .178, χ ≈ .067/.072/.069/.048 (β ≈ .017).
- Board: t's GP 4a76 s21 3.33/r46 3.09; ap 2848 s21 2.92/r46 3.72. Ingredients I lack: negative achiral α
  dressing on S9/S10×T1 (12-member) and S5T1⊥/S3T3⊥/S2T2⊥ (au, t). r56 still stalled (c's request to human).
- Budget 44 used.
- Idea next: run 4 adding S9/S10 achiral invariant α twins if inv13 plateaus below the board.

## 06:58 — wakeup 7: inv13 gen1 told (best 3864: s21 2.988 / r46 3.342), gen2 submitted
- Mean moving: S2T1∥ .22 (up), S2T2⊥ −.054, S5T1⊥ −.051 (negative dressing, as au/t found), χS9 .122 largest.
- All 11 gen1 points have r46 ≥ s21 (r46 excess grows with χβ) — even part per ae/an/aq refutations.
- r56 still stalled board-wide; many agents moved to reserve. Budget 55 used.

## 07:20 — wakeup 8: inv13 gen2 told (best d4e0 s21 3.262 / r46 3.356), gen3 submitted
- Mean: S2T1∥ .229, S5T1⊥ −.076, χS9 .134. σ 0.0315. Many agents done/reserve; r56 still stalled.
- e critique: frontier M2k up to 7.4 above static calibration; l extending static M2 controls to 7–10. Budget 66 used.

## 07:43 — wakeup 9: inv13 gen3 told (best 3.17, median 2.73), gen4 submitted
- Board frontier: ap 3a0e s21 4.388 / r46 4.390 (31-dir s21+r46 gradient + Newton, Σ|α| 2.39); t 4020 3.52/3.92.
- Static M2 saturates ≈1.67–1.73 by M2 7–10 (as, l) → frontier ~3× beyond static M2 (amplitude needs ctl anyway).
- My CMA lags (best 3.26). Plan: continue a few gens; if stalled < frontier, re-seed at frontier or switch to
  verifier on r56 when it lands. Budget 77 used.

## 08:06 — wakeup 10: inv13 gen4 told (best 386a s21 3.638 / r46 4.086), gen5 submitted
- Mean: S2T1∥ .277, S5T1⊥ −.097, S1T2∥ .055, S2T2⊥ −.065, χS9 .131, χS10 .078.
- Board: ap 4547 s21 5.20 / r46 5.41 on Σ|α| edge; c critique: pair chart inflates Σ|α| by ~3.9x.
- r56 stalled ~3 h. Budget 88 used.

## 08:35 — wakeup 11: inv13 stopped (6 gens, best 386a 3.638/4.086); run 4 front13 launched
- inv13 corroborates frontier shape (S2T1∥ .28, S5T1⊥ −.10, χS9 largest) but plateaus ~3.6 (lacks S9/S10 achiral dressing).
- ap 4547 s21 5.203 / r46 5.414 (robust two-cluster Newton, Σ|α| 2.36/2.5). ap now does robust objective too.
- front13: base = ap 4547 block (work/base_ap4547.json, reproduces boundary numbers exactly), CMA deltas in
  the 13 inv13 coords, σ 0.02, λ 11; Σ|α|>2.5 draws rejected by check → reallocation. Mailed ap. Note posted.
- Most agents done; r56 still stalled (~3.5 h).

## 09:25 — wakeup 12 (after session interruption): front13 gen0 told, gen1 submitted
- Interrupted call had NOT saved state; removed stray gen01 inputs, re-ran step (deterministic RNG).
- front13 gen0 best 2e2e s21 5.573 / r46 5.678 (> base ap 4547 5.203/5.414); median ~4.9; 3 Σ|α| rejects.
- ap moved on: 0328 s21 6.655 / r46 7.107 (M2k 5.78). Plan: after gen1, rebase CMA onto the best robust point
  (ap 0328 or mine), keep C and σ, reset mean to 0. Budget 110 used.

## 09:48 — wakeup 13: search CLOSED; waiting for r56 (verifier mode)
- front13 gen1 told: best 83cd s21 5.597 / r46 5.835. ap at ~6.7 (L1-constrained robust steps).
- au critique (min(s21,r46) can fit the cluster split; r56 is held-out) accepted. Posted closing result with
  coverage: 20261008T094743.876Z_swarm-s_result_22e7. 110 evals, 109 PASS / 1 FAIL.
- front13 gen2 inputs written but NOT submitted (don't submit).
- Plan: long wakeups; when r56 lands, post transfer table s21→r46→r56 for my promoted points; 9519 chiral-α
  ablation if it survives r56. ~390 evals reserve for others' requests.
- 10:28 wakeup 14: no r56 yet; ap, t, q also closed searches awaiting r56. Waiting.
- 11:30 wakeup 15: no r56 yet. ap 28b8 s21 8.86 / r46 9.39 (M2k/M2 1.19; gap 4.05e-3, split/Δ 1.6%, PES gap 4.2). ab: 0328 ~5x beyond equal-M2 static. Waiting.
- 12:30 wakeup 16: r56 still stalled (~6h; c, t, af requests to human). ap closed: 077d s21 11.27 / r46 10.54. Waiting.
- 13:38 wakeup 17: r56 still stalled (~7.5h). ab: R~9-11 frontier ~8-10x beyond equal-M2 static; q: conditioning fine (min S/max S ≥0.67). Waiting.
- 14:39 wakeup 18: r56 still stalled (~8.5h). Waiting.
- 15:40 wakeup 19: r56 still stalled (~9.5h). Waiting.
- 16:41 wakeup 20: board quiet, r56 still stalled (~10.5h). Waiting.
- 17:57 wakeup 21: board quiet, r56 still stalled (~12h). Waiting.
- 18:57 wakeup 22: quiet, r56 still stalled (~13h). Waiting (promised transfer table).
- 19:58 wakeup 23: quiet, r56 still stalled (~14h). Waiting.
- 21:00 wakeup 24: r56 stalled >15h; ran swarm done (summary work/done.md). Loop stopped.
