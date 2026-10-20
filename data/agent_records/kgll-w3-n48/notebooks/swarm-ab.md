# swarm-ab notebook

Started 2026-10-08T04:36:15+00:00.

## 2026-10-08 05:12 — wakeup 1: scope chosen = mechanism controls (mdctl-w3)
- Board: ~15 hypotheses (atlases b/c/f/g, joint orbits e/i, hessian d, sobol o, z2 h, chiral j, c3break r, ps/nem k, w2: a,m).
- Lead signal: S1xT1 *perpendicular* joint orbit (G ⟂ R pairs: G(1,0)-R(0,1), G(0,1)-R(1,0), G(1,1)-R(-1,1)), alpha only.
  swarm-i fa76 (alpha 0.0866/pair) s21 R=1.1885 (M2k 3.812); swarm-e 56da (0.05/pair) s21 1.105 -> r46 pending.
- Nobody doing claim-2 controls -> I took it. Script work/mdcontrol.py: builds avg (BZ-avg diag density) and
  pow (rho*^p, M2-matched) static controls from any ed_input. Plain rescale 1+t(rho-1) is negative (w3 touches 0).
- fa76: rho_bar M2 = 3.644 (≈ parent), M2k = 3.812 -> the M2 increase is k-to-k fluctuation, not average.
- Submitted controls (s21): 69e8 avg-fa76, ca1f pow-fa76 (M2 3.81), 7791/79fb/71b4 calib M2 3.70/3.95/4.20.
- Hypothesis post 99fd; mailed swarm-e, swarm-i.
- Next: read control results; when a perpendicular-orbit candidate reaches r46/r56, run avg+pow controls there
  (--control --clusters r46,r56). Consider a search niche later (outer stars S4-S10 joint orbits unclaimed).

## 05:28 — wakeup 2
- s21 controls: avg(fa76) M2 3.644 -> 1.0030; pow M2 3.70 -> 1.0143; 3.812 -> 1.0365; 3.95 -> 1.0635; 4.20 -> 1.1108.
  Static slope ≈ 0.19 per unit M2 (dlnΔ/dlnM2 ≈ 0.70). fa76 1.1885 vs 1.0365 matched -> ~15 % beyond M2 at s21.
- swarm-p posted same control role 2 min after me (m2-control, ρ+ρ² mixing shape, runs s21/r46/r56 per candidate).
  Split proposed by mail: p = per-candidate controls; me = calibration curve Δ_static(M2) on s21/r46/r56.
- New leaders swarm-e R 1.33-1.50 at M2^(k) 4.1-6.1: linear extrapolation of static curve gives ~1.44 at 5.9 -> may be mostly M2!
- Submitted pow controls M2 4.40..6.50 on s21,r46,r56 (3baa ad2f 6422 4257 816c c775), low ones + fa76 avg on r46,r56
  (730c 174e b439 f01f 13bc). mdcontrol.py now has --n_mesh, --gmax 20, --eps floor (0.003) for positivity at high p.
- Posted result 0cc7.
- Next: complete calibration table per cluster; compare leaders' R vs R_static(M2^(k)) per cluster; post.

## 05:50 — wakeup 3
- Calibration (sharpened w3 ρ^p), s21 / r46: 3.70 1.0143/1.0144; 3.812 1.0365/1.0366; 3.95 1.0635/1.0636; 4.20 1.1108/1.1110;
  4.40 1.1473/1.1475; 4.70 1.1998/1.2000; 5.00 1.2484/1.2487; 5.50 1.3261/1.3269; 6.00 1.3981/1.4017; 6.50 1.4629/1.4764.
  Cluster-independent (≤0.1% to 5.5), sublinear. avg(fa76) 1.0030 both. r56 pending.
- swarm-p agreed split (p: per-candidate A/B; me: calibration). p's ρ+ρ² at 3.812 = 1.0336 (shape spread 0.3%).
- work/excess.py: R / R_static(M2k) from leaderboard. Leaders keep 1.2-1.46x over equal-M2 static. Top excess: swarm-au nocomov
  (a61f s21 1.569 @M2 4.02), swarm-am chiral β dressing (r46 ≫ s21, finite-size flag).
- Posted result a400. swarm-e asked for 7722/c3f0 controls: submitted 7722 avg (b914) + pow (4fc8) on s21,r46,r56; c3f0 is p's.
- Started mdctl-w2: w2 calibration ρ^p M2 2.60..4.20 on s21,r46,r56 (31f0 58df 6788 b6b2 9adf 201e; eps 0.003, 0.01 for 2.75/3.00).
- Next: r56 calibration column; w2 table + excess for w2 leaders; update excess table when r56 lands.

## 06:17 — wakeup 4
- r56 stage stalled board-wide (swarm-c request 8cff to human). Budget charged 57/500 (board total? digest line).
- 7722: avg (M2 3.756) 1.0232 both clusters; exact-M2 pow (4.637) 1.1879/1.1881 vs table interp 1.1888 -> table valid to ~0.2%.
- w2 calib s21/r46: 2.60 1.0248/1.0249; 2.75 1.0606/1.0611; 3.00 1.1182/1.1209; 3.30 1.1827/1.1909; 3.70 1.2549/1.2772; 4.20 1.3230/1.3751.
  w2 static is cluster-dependent above M2~3 (r46 +4% at 4.2); same at leaders' M2.
- w2 leaders' huge s21->r46 jumps (chiral β 1.026->1.276) not explained by static -> critique posted (2e28), mailed an/av/aq/ah.
- Next: when r56 lands -> add r56 columns to both calibrations, update excess tables, final coverage post.

## 06:48 — wakeup 5
- r56 still stalled board-wide. Many agents now in reserve/verifier.
- swarm-p result 2e62: static curve shape-independent to ~1% (ρ+ρ² vs ρ^p, to M2 6.5).
- Mail: swarm-v (w2 Z3 odd-artefact argument), swarm-aq (measured: w2 s21->r46 split is even, 2nd-order). Consistent with my static-no-split finding.
- Answered swarm-aj request 0b97: avg control of ef7f (M2 3.587) on s21,r46,r56 = b939. Mailed aj, p.
- Next: r56 columns + updated excess tables (w3, w2) when r56 lands; then coverage post + done.

## 07:19 — wakeup 6
- r56 still stalled. ef7f avg control b939: 0.9911 s21 & r46 (consistent with calib at M2 3.587).
- Herding: as, av, a, l all offered to extend calibration >6.5 (swarm-e note 7556; frontier M2k 6.2-7.4).
  swarm-l already submitted (hyp b9d5) -> mailed all 5: l owns it, others stand down; sent construction recipe.
- swarm-aj bbfb avg control submitted (302c, M2 3.570, s21/r46/r56).
- swarm-p: took swarm-t 6107/b863 A control; 6107 r46 3.709 vs R_static ~1.43.
- Next: r56 columns + final w3/w2 excess tables + coverage post, then done.

## 08:00 — wakeup 7
- bbfb avg 302c: 0.9874 both. Static >6.5 done by as (b1bb) + l (4733): saturates ~1.67/1.73 by M2 10.
- Frontier: ap 4547 s21 5.20 / r46 5.41 (M2k/M2 1.61 -> M2k 5.84 -> R_static ≈1.375, NOT 1.45 as written in e48d; fix in next post).
- Posted coverage result e48d (26 control requests, 63 charged evals, s21+r46 done; r56 queued).
- Remaining: r56 column only. Long cadence; if r56 never runs before deadline, post final + done.

## 09:26 — wakeup 8
- r56 still zero results (~4h); swarm-t request 61ea asks human for priority list. Most agents done.
- Posted correction note (4547 R_static 1.375, excess ~3.8-3.9x).
- Plan: hourly check; when r56 lands, post r56 column; otherwise near deadline post final + done.

## 10:27 — wakeup 9
- r56 still stalled. New w3 leader ap 0328 s21 6.655 / r46 7.107 (M2k 5.782). ap request 6a50 -> submitted avg (M2 3.417!) + exact-M2 pow controls on s21,r46,r56. Mailed ap.
- 10:48: 0328 controls: A 2761 0.9614/0.9810; B 5513 1.3673/1.3694 (as predicted). Posted result; mailed ap. ap 28b8 now s21 8.86/r46 9.39 @M2k≈4.32 (R_static≈1.13).
- 11:49: ap asked for 28b8 controls -> A (M2 3.286) + B (M2 4.333) submitted s21,r46,r56. ap will mail final path point id.
- 12:10: 28b8 A 1fe9 0.9385/0.9415, B 1a6f 1.1343/1.1346 -> excess 7.81x/8.27x. ap final point 077d (11.269/10.535, M2k 4.320): A 81b3 (M2 3.303) + B 70e8 submitted. Post both when 077d lands.
- 12:31: 077d A 81b3 0.9425/0.9445, B 70e8 1.1321/1.1323. Posted result (28b8+077d). Mailed ap. Remaining: r56 only.
- 13:42: quiet; r56 still stalled; no requests.
- 14:43: swarm done posted (81 evals, all controls). Loop stopped.
