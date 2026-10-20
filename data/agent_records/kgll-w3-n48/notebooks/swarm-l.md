# swarm-l notebook

Started 2026-10-08T04:35:12+00:00.

## Wakeup 1 — 2026-10-08 ~05:05Z
- Read brief, docs 40/46, theory §6.4. Board: b,c,f,g run single-term atlases on w3 (herding, d flagged it);
  d: 12-D even Hessian (S1-S3 x T1-T2); e,i: joint (G,R) orbits; a: w2 atlas.
- Early atlas data (c, s21): S1T1 alpha -0.1/-0.03/+0.03/+0.1/+0.3 -> 0.845/0.948/1.015/1.033/0.965;
  S2T1 alpha -> 0.860/0.955/1.015/1.018/0.725. Phase S1T1, S2T1 beta +-0.03/+-0.1 -> ~even, negative (0.985, 0.93/0.87).
  T2/T3 at |alpha|=0.1 catastrophic (R 0.11-0.29) except S1.
- Observation: R(alpha) has a KINK at 0 (slope ~+0.5 for alpha>0, ~+1.7 for alpha<0). Interpretation: gap = min over
  several excitation branches degenerate at the parent; deformations split them. Gap maximization is a minimax
  (nonsmooth) problem; Hessian/quadratic fits around the parent will mislead.
  Also: k-dependence breaks ideality (C=1 ideal bands are all static B(r) x LLL), so GS energy rises ~quadratically.
- Plan: family `minimax-w3`: active-set / minimax optimizer using sector-resolved spectra if available. Batch b1 (10):
  S1T1, S2T1 alpha line fills + positive-quadrant S1+S2 combos.
- Tools: work/gen.py (stars, input builder), work/scrape.py (leaderboard -> swarm show table, cache).
- Next: see if `swarm status REQ` exposes per-sector low energies; post hypothesis with budget.

## Wakeup 2 — ~05:21Z
- Board exploded (48 agents). Key result: half-translation-invariant joint orbits S1T1-perp and S2T1-par (e, h, i):
  s21 ~1.10 at pair c=0.05; i's fb45/fa76 (orbit amp 0.0866/0.05-ish) s21 1.18-1.19, r46 1.16-1.17.
  All non-invariant orbits = negative cone (half-translation selection rule, swarm-h).
- `swarm status REQ` gives no sector spectra -> minimax/active-set idea not feasible. minimax-w3 re-scoped (superseded).
- My b1 (separable): s21 1.02-1.034, r46 up to 1.072 (58f3: S1 .05+S2 .10). r46 > s21 for separable points.
- New role: verifier `numconv-w3` (posted hypothesis 20261008T052136.975Z_swarm-l_hypothesis_9125, <=60 evals).
  conv1 submitted: fb45, fa76, be47, 56da at n_mesh 64/g_cutoff 12 (work/conv.py RID nmesh gcut out).
- Next: compare conv1 vs originals; watch for large-amplitude leaders (M2k/M2>1.5) and convergence-check them;
  post minimax-w3 result+coverage after r56; write a critique post.

## Wakeup 3 — ~05:45Z
- conv1 result: 64/12 vs 48/8 identical to <=4e-7 on s21/s21c/r46 for fb45, fa76, be47, 56da. Posted result
  20261008T054351.170Z_swarm-l_result_e2b2 (also closes minimax-w3 with coverage block). Withdrew conv1 copies and
  minimax r56 promotions (free up r56 queue).
- Leaders now large-amp: e c3f0 (s21 1.452, r46 1.413), af c310 (1.518/1.409), af 4af3 (1.392, M2k/M2 1.75), af 72e1.
  conv2 queued: c3f0/c310/4af3/72e1 @96/16, c3f0/4af3 @64/12 (ids 93d0 952e b0cc 8fc0 aed3 2887). work/cmp.py compares.
- r56 parent gap still pending at 05:44 (118 requests waiting at r56). Not halted, just slow.
- swarm-ag covers high-shell (losers) convergence; I cover leaders.
- Next: compare conv2; withdraw copies after r46; critique post on finite-size drift vs amplitude once r56 lands.

## Wakeup 4 — ~06:13Z
- LESSON: `swarm digest` marks read; use `swarm digest --no-mark` first, then plain digest. (Lost one post list.)
- conv2: 64/12 == 96/16; vs 48/8 shift <= 1.1e-4 (4af3 r46, M2k/M2 1.75). Posted 20261008T061053.542Z_swarm-l_result_c9d5.
  Copies withdrawn.
- New leaders R_s21 ~2.0-2.5 (t 0e99 2.478, e 80c7 2.151, am 08b5 2.055/r46 2.063, j ba1f 2.031/r46 2.225):
  chiral-beta dressing + high shells up to |G|^2=21 at g_cutoff 8. ag says 1.2-5% kernel L1 outside box 8.
- conv3 submitted (96/16: 0e99 80c7 08b5 ba1f f7a7; 64/12: 0e99 ba1f) = 558e 1046 e716 fe14 f857 3641 69dd.
  ag overlaps on 0e99/80c7/ba1f with gc12/16 diagnostics; mailed split (ag: |G|^2>=12; me: low shells + r46).
- r56: zero results anywhere after ~95 min; swarm-c posted request to human.
- Next: compare conv3 (cmp.py), post; withdraw copies after r46. Consider own search family with remaining ~470 evals.

## Wakeup 5 — ~06:35Z
- conv3: R~2 leaders converged on s21 and r46; 48/8 bias <= 1.1e-3 (ba1f s21), r46 half that. 64/12 == 96/16.
  Posted 20261008T063452.037Z_swarm-l_result_9b81 with coverage (23 evals total in numconv). Copies withdrawn.
  numconv closed (ag, z, me all agree).
- Board: many agents now reserve/verifier (w, a, r). Frontier: e 80c7 r46 2.29, t 0e99 r46 2.49, j ba1f r46 2.23.
  w2 frontier b 8c39 s21 1.299 / r46 1.343. r56 still zero results.
- Me: reserve mode, ~470 evals. Take mail requests; re-evaluate once r56 lands (ordering audit; a also plans this).

## Wakeup 6 — ~07:18Z
- Board: many agents done/reserve. Frontier s21 R ~3.6 (t 4fee, M2k 7.44); r56 still zero results anywhere.
- swarm-e critique 7556: static M2 calibration (ab shape P rho^p, p shape B) stops at M2 6.5; frontier above it.
- Took it: family `m2hi-ctl`, static controls w3^p at M2 6.5/7/7.5/8/9/10 on s21,r46,r56
  (reqs de4e 5f91 872c c0d6 cf2f 81ac). work/m2ctl.py (floor 2e-4 needed: truncated series went negative).
  Hypothesis 20261008T071803.589Z_swarm-l_hypothesis_b9d5. Mailed ab.
- Check: overlap point 6.5 vs ab/p (1.4629 / 1.4586 s21).

## Wakeup 7 — ~07:40Z
- swarm-as ran the same M2 6.5-10 static controls at 07:09 (before my post). Mine = replicate; agree <= 8e-4.
  Posted 20261008T073930.956Z_swarm-l_result_4733 (coverage). Withdrew my r56 copies.
- Static curve saturates ~1.67 s21 / 1.73 r46; frontier ap 3a0e s21 4.388 / r46 4.390 at M2k 6.31 (~3x static).
  ap frontier near campaign box edge (sum|alpha| 2.39 of 2.5).
- Many agents done. r56 still zero results. Me: reserve, 461 evals left. Wake ~50 min; if r56 lands, audit ordering.

## Wakeup 8 — ~08:32Z — DONE
- Most agents finished; r56 still zero results. Nothing distinct left for me. Posted `swarm done` summary
  (39 charged: 33 search + 6 controls; families minimax-w3, numconv-w3, m2hi-ctl all closed with coverage).
