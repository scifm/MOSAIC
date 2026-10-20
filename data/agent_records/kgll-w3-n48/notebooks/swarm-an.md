# swarm-an notebook

Started 2026-10-08T04:37:04+00:00.

## 2026-10-08 05:41 — wakeup 1: scope chosen
- Read board (~90 posts). w3 heavily covered (~40 agents): leaders are S1xT1-perp + S2xT1-par amplitude orbits (s21 up to 1.52, r46 1.41).
  High-shell invariant orbits are herded (w, ah, ai, al, y, ap) -> I dropped my first idea (high-shell inv orbits).
- swarm-w found phase-only chiral beta on S4xT1 / S7xT1 gains on w3 (r46 1.21): beyond-M2 by construction.
- My family: `chiphase-w2` = the same chiral-beta phase-only sector on parent w2 (nobody has it; swarm-ar plans S4xT1 beta later; mailed).
  Z3 rule on w2: monomial phase w^{(m+n)+(R2-R1)}; T1 x G-pair half-invariant iff m+n != 0 mod 3 -> stars S1,S3,S4,S7,S8,S9.
- Tools: work/orbits.py (joint orbits, mirror, Z2 rule, block builder), work/gen_w2chi.py (chiral beta per-entry b).
  g_cutoff 10, n_mesh 48.
- Submitted phase 1: 24 reqs (12 dirs x b=+-0.03), ids 20261008T0541xx_swarm-an_req_* (see swarm status).
- Hypothesis post: 20261008T054101.404Z_swarm-an_hypothesis_ef57. Budget <=80.
- Next: read results; odd/even parts per direction; phase 2 line scans to b<=0.12 + additivity; then cross with swarm-m ba45 (S3xT1 perp).

## 2026-10-08 05:58 — wakeup 2
- Phase 1 landed 22/24. w2 chiral-beta curvature ~5x w3. Only S7xT1 44deg acute+ at 0.03 gains (aa67 s21 1.0264, promoting).
  odd>even also for S4(11deg) acute- and S3(30deg) acute-. NOTE sign map: my orbit-a is obtuse for S1,S3,S4c1,S7c1,S8,S9c1
  (so acute+ = my "bm"); acute for S4c2,S4c3,S7c2,S7c3,S9c2,S9c3.
- Herding: ah, aq, av opened the same w2 chiral-beta family within 3 min. Posted result 20261008T055824.814Z_swarm-an_result_37b5 with split
  proposal (me: line scans/additivity; aq/av: cross with amplitude leaders). Mailed ah/aq/av/ak.
- Phase 2 submitted (6): S7c1 bm 0.010/0.015/0.020, S4c2 bm 0.015, S3c1 bp 0.015, S7c1m015+S4c2m015. Gen: work/gen_w2chi_p2.py.
- Budget: 30/500.

## 2026-10-08 06:20 — wakeup 3
- Split agreed: me = w2 phase-only line scans/additivity; b = chidress-w2 (amp x chi-beta cross); q = cma-w2; aq/av = Z3 null controls. ah/aq/av closed screens.
- S7(44)+ line s21: .010 1.0589, .015 1.0702, .020 1.0687, .030 1.0264. r46: 1.123, 1.176, 1.216, 1.276 (monotone!). S4(11)- .015: s21 1.048 r46 1.150.
  S3(30)- .015 1.018. S7+S4 .015 each: 1.052 (subadditive). S9 c2/c3 all < 0.76.
- r56 stalled for everyone (swarm-c request to human).
- Submitted 3 parity CONTROLS (r46,r56) at S7(44) acute- b=.010/.015/.030: 205e, b39a, 7c6d. Tells if r46 excess is even in b (artifact).
- Posted result_2 (phase 2). Budget ~33/500.
- Next: read parity controls; if r46 even -> post critique/null; if odd and r56 confirms, line is a phase-only w2 candidate. Then maybe close family with coverage.

## 2026-10-08 06:47 — wakeup 4
- Parity controls r46 (acute-): .010 0.9270, .015 0.9082, .030 0.7641. r46 odd 0.098/0.134/0.256 (slope ~9/unit b) = s21 odd 0.249@0.03.
  Even: r46 +0.02..+0.04 vs s21 -0.22 @0.03. => split is curvature, cluster-dependent (agrees with aq c7cf; contradicts v f84d). Posted; mailed v.
- Most agents now in reserve/verifier mode. r56 still stalled swarm-wide.
- Next: wait r56 for 84d6/aa67/controls; then close chiphase-w2 with coverage block. Consider a reserve/verifier role after.

## 2026-10-08 07:20 — wakeup 5
- r56 still stalled. Closed chiphase-w2 for search with coverage post. Best 84d6 s21 1.0702 / r46 1.1762.
- Board: w3 frontier R~4.4 (ap 3a0e, M2k/M2 1.74, alpha_sum 2.39/2.5 near boundary). Many agents done / reserve.
- Plan: reserve/verifier; post r56 addendum for 84d6/aa67 + controls when r56 lands; then swarm done.

## 2026-10-08 07:58 — wakeup 6
- r56 still stalled swarm-wide. Nothing new for my family. aq (result_3308): w2 r46 parent on a soft level, small deformations lift r46 ~+5% even -> consistent with my r46 even part +0.02..+0.04.
- Holding in reserve; will post r56 addendum then swarm done.

## 2026-10-08 09:35 — final
- r56 still stalled (~4h). Family closed with coverage (result_5393). Nothing left in scope. Ran `swarm done` with summary work/posts/done.md.
