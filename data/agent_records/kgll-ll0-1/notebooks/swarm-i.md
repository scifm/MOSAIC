# swarm-i notebook

Started 2026-10-02T03:51:37+00:00.

## Wakeup 1 — 2026-10-02 ~04:05–04:20 UTC

**Board state.** a: w3 star atlas (96). c: w3-wide CMA (8-D α, 16-D α+β, S1–S4 × T1–T2). b and f: w2 star atlas, the same design twice (duplicated). e: w2-map. g and h: w3-orient joint orbits (U/X/C, U/A/B) on S1–S3 × T1–T2, α and β.

**Key insight (posted as note 20261002T041116.041Z_swarm-i_note_2234).** The symmetry is MT (mirror × time reversal), antiunitary, with α[o] → α[Mo] and β[o] → −β[Mo].
- MT-even (linear term allowed): α-U, α-X/A, α chiral-sum, β-chiral (o − Mo).
- MT-odd (Δ even in TD): β-U (all star-product phases), β-X/A, α-chiral.
- No ladder cluster is mirror-symmetric (checked against geometry.jl): s21 is C6 but chiral; 4×6 and 5×6 are C2 only. So MT-odd directions get spurious cluster-chirality linear terms.
- g and h predict R(+c) = R(−c) for C in both α and β. I think that is wrong for β. Mailed g, h (and a, b, c, e, f about β-U).

**My family: `chiral-phase`** (hypothesis 20261002T041355.973Z_swarm-i_hypothesis_a92f). β-chiral (MT-even), phase-only, so beyond-M2.
- Tools: `work/chiral.py` (orbits, directions, block) and `work/make.py PARENT OUTDIR NAME 'gn2,rn2,dir,kind,coef;...'`.
- Direction names: `chi{θ+}-{θ−}` = +orbit θ+ and −mirror orbit θ−, unit Frobenius norm.
- Verified that the decomposition reproduces star-product γ to 1e-17, and that a unit direction has mean |γ|² = 1.
- Batch 1: `work/b1_w3` (28 files) and `work/b1_w2` (16), ±0.03. Shells in the names are |G|² (S7 = |G|² 7, the 12-member shell), T1 = |R|² 1, T3 = |R|² 3, T4 = |R|² 4. (Caution: my file tags use |R|² numbers, not star indices: "T3" in a tag means |R|² = 3, i.e. star T2.)

**Next:** submit both batches once `swarm check` passes. Then fit slope and curvature per direction and pool them with g's and h's S1–S3 β-C.
- 04:17: submitted the w3 batch (28 requests; ids in `work/b1_w3.ids`). The w2 batch (16, `work/b1_w2`) is held for the 32-in-flight cap; submit it once some w3 requests finish.

## Wakeup 2 — 04:43 UTC

- Batch 1 (w3) is done: 28/28 PASS. Live modes (beta-chiral, T1):
  - |G|²=7 chi49.11-130.89: +0.03 → 1.0364 (req e356, identical to d 2400), r46 1.080.
  - |G|²=13 chi163.9-16.1: −0.03 → 1.0252 (req 877a), r46 1.057.
  - Both have even part ≈ −0.003. All other modes have |odd| ≤ 0.38 and even −0.02 to −0.045.
- Swarm herding is heavy on chiral-phase (d, l, j, k, o, me). d is running the |G|²=7 line search, j has w2 |G|² ≤ 4, o is running combinations.
- Dropped the w2 1/3/4/9/12 batch (`work/b1_w2_dropped`).
- Batch 2 submitted (g_cutoff 10, `work/make.py` takes the GCUT env var):
  - w3 |G|²=13 c1 line search, β = −0.03 … −0.20;
  - w3 13×T2 (3 modes ±0.03);
  - w2 7×T1 and 13×T1 (3 modes ±0.03 each).
  - Ids in `work/b2_*.ids`.
- Posted result 20261002T044506.630Z_swarm-i_result_0f68.
- Next: read the line search. If the curvature stays small, widen beyond 0.20. Candidate idea: chiral modes on higher 12-member shells (|G|² = 19, 21, 28, 31) × T1, possibly the next live ones. Also w2 transfer.

## Wakeup 3 — 05:11 UTC

- Batch 2:
  - w3 |G|²=13 c1 line, s21: −0.03 1.025, −0.06 1.036, −0.10 1.019, −0.15 0.938, −0.20 0.80. r46: −0.03 1.053, −0.06 **1.137**. Peaks near 0.06; curvature kicks in beyond that.
  - w3 13×T2 (3 modes): dead.
  - w2 7×T1 and 13×T1: big slopes. 13c3 +0.03: s21 1.0655, r46 1.152 (ffbc). 7c1 +0.03: s21 1.0475, r46 1.135 (2df9). 13c2 weakest.
- Board: the leaders are α S2T1∥ (c 776c, s21 1.52) and o's α+β combinations (968b: 1.61/1.71). r56 is pending for everyone. The human fixed the converge gate (r46/r56 only) and control clusters.
- **Selection rule (note f044).** A live T1 orbit needs a_{G+Gp} = ∓R for some parent shell Gp, or Gp = 0. Tool: `work/qstatic.py`.
  - Fits: w3 18/19 T1 classes (miss: |G|²=9 ⟂), w2 8/8 T1 shells.
  - Fails as a sufficient condition on T2.
  - Implication: the linear gains are static, LL-mixing-type content, not k-dependence. Mailed b, p, c, d, k, r, o. Handed the w2 line searches to l.
- Batch 3 (pre-registered test, 20 req, g10) on |G|²=19, 21 × T1, ids in `work/b3_*.ids`:
  - predicted live: w3 19 chi113.41-66.59, w3 21 chi40.89-139.11 (weak), w2 19 chi113.41-66.59;
  - all others predicted dead (w2 21 included).
- Next: score the test and post the outcome as a result (or a refutation of my own rule). If the rule holds, consider a signed first-order calculation to explain the T2 failure.

## Wakeup 4 — 05:44 UTC

- Pre-registered test scored (result ca2c): live/dead w3 6/6, w2 2/4 (the 19a and 19c modes are live although predicted dead). Size scaling fails (|G|²=21 slope 1.51 > 19's 1.22).
- Post-hoc two-harmonic rule (a_{G+Gp1−Gp2} = ∓R, `work/qstatic2.py`) explains the w2 misses and b's S8-30°, and leaves the w3 set unchanged. Conceded o's point: the leaders' gains are α∥×β cross terms (2nd order), outside the rule.
- Live new modes: w3 19b (−0.03 → 1.0276, r46 1.10) and w3 21c (+0.03 → 1.030, r46 1.13). o is adding C19 and C21 to the leader, so I don't.
- Board leaders: o bd1a s21 2.27 / r46 2.63 / r56 2.57 (on conv46); o 48bf r46 3.03; k 13f5 2.64/2.71.
- **New family `static-free`** (hyp fb7e): CMA-ES in the 10-D MT-even zero-static-content subspace on w3, box 0.3, σ0 0.1, λ 10. Driver `work/sf_cma.py` (propose / record IDS / update), state in `work/sf/state.json`. Gen0 submitted (`work/sf/gen0.ids`). Expected null.
- Each wakeup: `python work/sf_cma.py update`; if it updates, run `propose`, then `swarm submit-batch work/sf/genN`, then `record`.

## Wakeup 5 — 06:09 UTC

- static-free gen0 (σ0 0.1, radius 0.27–0.41): 5/10 FAIL (broken manifold, e.g. 6a06 R 0.076, split/Δ 0.73); PASS points 0.40–0.91 (best 174f 0.910). A strong loss in every direction at radius ~0.3.
- Restarted CMA at the origin with σ 0.05, recorded in `state['restarts']`. FAIL now scores 0.5·min(R, 1), graded. Gen1 submitted (radii 0.10–0.22).
- Claims on the board:
  - p cc86 STRONG, provisional: 2.40 / 2.47 / 2.46 / conv 2.47.
  - o bd1a STRONG, provisional: 2.27 / 2.63 / 2.57 / 2.63.
  - d 2400 robust_positive: 1.036 / 1.080 / 1.056 / 1.076. This is phase-only and identical to my e356. d's claim already carries my f044 caveat.
- e: the leaders' β patterns lose at α = 0 (β gain needs α). p is running its own static-free cc86 analogue (12 req), complementary to my CMA.
- c: PES entanglement gap drops from 21 to ~5 on the amplitude leaders.

## Wakeup 6 — 06:31 UTC

- static-free gen1 (σ 0.05, radius 0.10–0.22): best 0.956, mean 0.785. New mean |m| 0.073, σ 0.046. Gen2 submitted (`work/sf/gen2.ids`).
- p: static-free cc86 analogue is a null (best 0.746). k: blind T2 test of my rule passes 4/5.
- New: the static-free gradient at the leader cc86. `work/addon.py` merges pair-star terms. 10 directions × ±0.05 on top of cc86, plus the re-expressed base (γ identical to 9e-17) → `work/cc86_sf.ids` (21 req). Caveat: at cc86, "static-free relative to the parent" no longer rules out static content in combination with the base α∥ harmonics.
- Next: if gen2 has nothing above 1, finish the CMA (maybe 1 more gen) and post the static-free null with coverage, including the at-leader gradient.

## Wakeup 7 — 06:59 UTC

- CMA gen2 found **f8d6**: s21 1.0757, r46 1.1870, PASS, eg 6.3, in the first-order static-free subspace. An isolated point (neighbours 0.66–0.94).
- `work/qpair.py`: at second order, every pair of directions has static content (weights 0.9–4.4), so "static-free" is first-order only. f044's mechanism reading is withdrawn beyond first order.
- cc86 static-free gradient: all 20 below the base on s21; r46 within +0.003. A local max.
- Posted result f4eb (interim, coverage). Gen3 submitted, plus a ray t = 0.5–1.5 through f8d6 (`work/sf/ray_f8d6.ids`).
- Next: read gen3 and the ray, then update the CMA. If f8d6 holds at r56, ask a or n for a matched-density control (α-heavy).
- Board: the w3 top is k 435c (s21 3.47 / r46 3.84). Claims: c 776c strong (α-only), h d49b strong (small α), r e064 w2 phase-only strong, g w2 98ec/29a2 strong.

## Wakeup 8 — 07:24 UTC

- Ray through f8d6 (s21): t 0.5 → 0.999, 0.75 → 1.029, 1.0 → 1.076, 1.25 → 1.119, 1.5 → 1.138. A ridge, not an isolated point. f8d6 r56 still pending.
- CMA gen3: best **106b s21 1.190** (radius 0.22). Winners share α S2T1±60 strongly negative, α S3T1⟂ positive, α 7×1 10.9 negative, β13c3 negative.
- Gen4 submitted, plus rays f8d6 t = 2, 2.5, 3 and 106b t = 1.25, 1.5, 2 (`work/sf/ray2.ids`).
- static-free spend: ~71, beyond the ~70 planned. Announce the extension in the next result post.
- Board: l w2 9fcb phase-only strong (my 13c3 mode at β 0.04). e: all claimed points are exactly MT-invariant. p 9fc9 s21 3.51.

## Wakeup 9 — 07:48 UTC

- Rays (s21 / r46):
  - f8d6: t 0.75 1.029/1.125, 1.25 1.119/1.255, 1.5 1.138/1.326, 2.0 1.176, 2.5 1.223, 3.0 1.105 (turns over).
  - 106b: t 1.25 1.272, 1.5 1.368, 2.0 **1.404** (618c).
- 618c: M2(k) 4.89 vs 3.63, R_staticM2 0.968, eg 2.79. Mostly density. n's yardstick at M2 4.89 gives ≈ 1.24, so ~+0.16 beyond.
- Gen4 best 1.216. Gen5 is the final generation, plus the 106b ray at t 2.5 and 3.0 (clipped).
- Then close static-free with a final result and coverage: genuine first-order-static-free directions DO beat the parent at second order, mostly via density.
- Board: k 7966 s21 3.73 / r46 3.83 / r56 3.79. Claims by o (84e4 phase-only) and d (e25f/3ea2 phase-only strong). Agents finishing: c, f, m, o.

## Wakeup 10 — 08:07 UTC

- static-free w3 closed (result cd00): 618c s21 1.404 / r46 1.511 at an interior optimum; ~0.16 beyond n's M2 yardstick; eg 2.8. CMA bests by generation: 0.91 → 1.30. 92 requests in total. Asked n for a matched-density control on 618c.
- **New: `static-free-w2`** (hyp 3ae8). Driver `work/sf2_cma.py` (DIRS for w2, σ0 0.05, state `work/sf2/state.json`). Gen0 submitted.
- Board: e's audit says the top R > 3 tier has split/Δ of 4–9% (near the gate); the robust tier is cc86. h: the conv46 shift for the T2-β family is −1.2%.

## Wakeup 11 — 08:32 UTC

- w2 static-free gen0 (σ 0.05, radius 0.10–0.22): best 0.937, mean 0.57, 4/10 FAIL (radius ≥ 0.14). Much more fragile than w3. Gen1 submitted (σ 0.046). Note: the w2 gen0 seed equals the w3 gen1 seed (same z draws, different directions); harmless.
- n submitted an M2-matched control for 618c (req 4eaa, s21/r46/r56). n's estimate is ≈ 1.21 s21.
- Board: k 7966 strong 3.73/3.83/3.79/3.79; p 9fc9/8bc7 strong, but manifold margins are thin. Final summaries posted by m, c, f, o, j, q.

## Wakeup 12 — 08:55 UTC

- 618c control (n, req 4eaa, M2-matched static mix): s21 1.216 / r46 1.221, against 618c 1.404 / 1.511. So +0.19 / +0.29 is beyond density (static explains 54% / 43%). r56 is queued.
- w2 static-free gen1 best 0.939, mean 0.68. Gen2 submitted. Plan: gen3, then close as a (likely) null.
- Board: g w2 1909 s21 1.513 / r46 1.539. k refuted p's 9fc9 (manifold margin). Final summaries from p and e.

## Wakeup 13 — 09:18 UTC
- w2 static-free gen2 best 0.930 (mean 0.78). Gen3 (final) submitted. Then close static-free-w2 as a null, and post a combined static-free result (w3 positive vs w2 null) with the 618c control numbers.
- Board: h a965 s21 4.34; k 459c 4.11/4.60 (split 0.005). d closed (final summary).


## Wakeup 14 — 09:41 UTC

- static-free-w2 closed as a null (result e69c, abandon dc3e): 40 evals, best 0.939, 7 FAIL.
- Withdrew the 21 cc86 gradient probes and 40 intermediate static-free ray/CMA points from the ladder. Kept 618c and f858 (plus the chiral 6fac and 752a) for r56.
- Claim posted: w3 ee6c robust_positive, phase-only C13 (1.036 / 1.137 / 1.085 / 1.136). w2 ffbc and 2df9 are robust_positive replicates of l's modes.
- Remaining: wait for r56 of 618c, f858, 6fac, 752a. If 618c is ≥ 1.10 on r56 and conv46, post a strong claim with the matched-control numbers. Then the final summary and `swarm done`. Budget 204/500; no new family planned unless something new appears on the board.
- 10:14 UTC: r56 still pending for 618c, f858, 6fac, 752a. No action.

## Wakeup 16 — 11:00 UTC — FINAL
- r56 still pending for 618c, f858, 6fac, 752a (low per-parent priority). The broker will finish them; claims are computed automatically.
- Posted the final summary note and ran swarm done. All families closed with coverage. 204/500 charged.

