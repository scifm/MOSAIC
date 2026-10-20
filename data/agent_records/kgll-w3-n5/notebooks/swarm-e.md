# swarm-e notebook

Started 2026-10-13T18:08:55+00:00.

## 2026-10-13 wakeup 1 (18:10–18:20 UTC)
- Read brief, docs 40/46, theory §6.4/§7.5 (ideality defect = Var_r(∂₊γ), so k-dependence costs ideality at 2nd order), ADR-0040.
- Facts: parents w3 lives on |G|²=4,12,16 (half-period density), w2 on 3,9,12 (√3 cell). Nk21 s21 Δ: w3 4.5714e-4, w2 3.2271e-4.
  Solver default ed_mode = full_ed, so non-C6 deformations are safe. Doc 46: w3 α[S1,T1]=+0.05 → +1.85 % at Nk21; −0.05 → −9 %.
- swarm-a claimed `w3-map` (single full-star terms S1..S10×T1..T3 at ±0.05, plus an S1T1 line).
- I claimed `w3-orient` (hypothesis 20261013T181805.275Z_swarm-e_hypothesis_e72d): orientation-resolved joint (G,R) orbits
  in the block format via inversion-pair "stars" and circulant α/β matrices. Tools: work/orient.py, work/build_orient.py
  (spec g2:r2:sub:m:kind:c), work/mk.py. Verified: the sum of 3 orientations at c equals the full star at 3c (1e-17).
  Relative angles: S1×T1 m0/1/2 = 30/90/150°; S2×T1 = 0/60/120°; S3×T1 = 30/90/150°.
- Submitted batch1: S1,S2 × T1 × m0..2 × {α±0.04, β±0.025} = 24 reqs (ids in swarm status). Pending: batch1b (S3, 12 files) in work/batch1b.
- Next: collect, compare Σ_m orientation response vs swarm-a full-star response (first-order sum rule), submit batch1b.

## wakeup 2 (18:36)
- batch1 (24 reqs, S1/S2×T1 channels): ALL FAILED_TRANSIENT_TERMINAL, charged 24. They're the only transient failures in the store.
  Only difference from swarm-c's identical-format requests: no g_cutoff (null). mk.py now defaults to g_cutoff=6.
- Board: swarm-c posted w3-joint (same channel family, S1–S3×T1) 2 min before me. Its S2T1 0° α c=0.08 (68f6) is ROBUST_POSITIVE:
  s21 1.0916, r46 1.0843, r56 1.0818, conv46 1.0843. S1T1 90° (3182): r56 1.0849. swarm-a: whole-star α S1T1 0.08 → r46 1.040, r56 1.037.
  swarm-d moved to w2-orient; swarm-b on w2 map + an M·T selection rule (β-odd vanishes in TL for whole stars).
  All β (phase) single terms negative so far.
- Pivot: I don't re-run T1 (it would duplicate swarm-c). New scope: the same channels at T2/T3 on w3, then cross-T combos with the T1 winners.
  Mailed swarm-c the split + the M2 point (68f6 M2k/M2 = 1.011 vs gain 8 %).
- Test: 2 reqs with g_cutoff 6: 7910 (S1T2 0° α .0462), 931a (S2T3 0° α .0462). Batch1b (S3T1, no g_cutoff) NOT submitted, superseded.
- Angles: S1×T2 = 0/60/120 (m0/1/2), S1×T3 = 30/90/150, S2×T2 = 150/30/90, S2×T3 = 0/60/120, S3×T2 = 0/60/120, S3×T3 = 30/90/150.

## wakeup 3 (18:45)
- g_cutoff fix confirmed: 7910 (S1T2 0° α .0462) s21 0.9678, 931a (S2T3 0° α .0462) s21 0.9451, both PASS.
- Board: swarm-c b1 table (S1–S3×T1 channels): only achiral g1Δ90 and g3Δ0 +α win (s21 1.097/1.092); all β < 1. swarm-c then
  went to large amplitude: 3faf s21 1.495, r46 1.419, r56 1.467, M2k 4.92 (1.36× the parent). swarm-b claimed outer shells S4–S10×T1.
  swarm-d on w2 (ef27 r46 1.129). swarm-c proposed I take the 12-member chiral shells + β, but swarm-b took those shells.
- β is dead at T1: the M·T-even phase direction β(C_θ − C_{180−θ}) has slope ~0.1 and curvature ~−16, so the max gain is ~0.02 %.
- New role: mechanism/verification. work/geom.py computes the LL0 k-GLL quantum geometry from K(k,k') (verified: uniform LL0 gives
  F = tr g = 1; static w3 has defect 0, F std 0.015). work/collect.py fetches every leaderboard request → geom_cache.json
  (Fstd, defect, Sratio, Σ|α|, Σ|β|, M2k). Running in the background.
- Next: correlation table (R vs M2k, defect, Fstd), post as a result/note; design ED tests of the proxy's predictions.

## wakeup 4 (18:50–19:00)
- Geometry proxy done for 230 requests (work/geom_cache.json). On w3: log R ≈ 3.25 log(M2k/M2) − 1.67 defect, R² 0.49; Fstd useless.
  swarm-c's lines: R/(M2k ratio) ≈ 1.08–1.17. 3faf: R 1.495, M2 ratio 1.356, defect 0.37 → ideality isn't limiting.
  The BZ-mean density of 3faf has M2 3.77 only; the w3 parent min is 0.005, so λ-scaling goes negative.
- Built static matched-M2 controls (work/control.py): ρ_w3·exp(t O_S2), |G|²≤112, C6-symmetrized, t tuned so M2 = M2^(k).
  Submitted as --control (family m2-control), clusters s21,r46,r56: 3faf ± (3c29/dbdf), 8617 ± (9a52/03a9), 68f6 ± (3d69/1bbb). 18 evals.
- Posted result 20261013T185904.086Z_swarm-e_result_10cb.
- Next: read the control results; if R_control ≈ R_kdep, the gain is density. Then maybe a static M2-ladder (t scan) to map Δ(M2) for
  the w3+O_S2 family, which is the static baseline any amplitude winner must beat. Budget used ≈ 44 + 18.

## wakeup 5 (19:15)
- My m2-control results so far (static ρ_w3·e^{tO_S2}, M2 matched): 3faf+ s21 0.787 / r46 0.849; 3faf− 0.985 / 1.068;
  8617+ 0.833 / 0.908; 8617− 0.937 / 1.013; 68f6± 0.964 / 1.000, 0.954 / 1.002. All far below the k-dep (1.42–1.50). r56 pending.
  Oddity: tiny-t 68f6 controls show s21 −4 % but r46 0 %. Submitted the t=0 sanity control 3e25 (421-harmonic parent, s21/r46/r56).
  swarm-b had the same (096b, 441-box parent → R = 1.0000).
- Board consensus: static controls (swarm-b ρ̄, frozen-K, frozen-Γ; mine) all lose, so the gain needs k-dependence. swarm-c b3 critiques
  my M2 fit (collinearity along lines; above M2k≈5, R falls as M2k grows). Fair; to acknowledge in the next post.
  swarm-c strong claim (g3Δ0 c=0.40, R_min 1.419, conv46 1.4195); PES FAIL past c≈0.7. swarm-d w2 robust_positive (ef27).
- New family `w3-nematic` (hyp 20261013T191648.873Z_swarm-e_hypothesis_b781): C2 single/two-pair versions of g3Δ0, 10 reqs in work/nem1/ids.txt.
  s21 for j=0,1,2 must coincide (Nk21 is C6); the r46/r56 j-spread = cluster anisotropy.

## wakeup 6 (19:33)
- t=0 sanity control 3e25: s21 1.0000, r46 1.0000, so the control path is exact and the m2-controls' losses are real.
- nematic b1 (g3Δ0 pairs, entry e): s21 is identical across j (construction ✓).
  one pair e=.2309: s21 1.0206; r46 j0/j1/j2 = 1.0406/1.0903/1.0974 (5.7 % orientation spread on 4×6!).
  one pair e=.40: 0.8854; e=.60: 0.6539. Two pairs e=.2309: s21 1.2569; r46 1.3224/1.3291/1.3130.
  C6 (3 pairs, e=.2309 = swarm-c c 0.40): s21 1.500, r46 1.420. → strongly SUPERADDITIVE (+2 %, +26 %, +50 %): the gain needs crossing stripes.
- nem2 submitted (work/nem2/ids.txt): weights (1,1,.5), (1,1,1.5), (1.15,1.15,.7), (.85,.85,1.3) at e0; two-pair at e=.30, .36.
- Board: swarm-a: a −3G harmonic on g1Δ90 raises R while M2k falls. swarm-c: g3Δ0 optimum flat (r46 1.420); w3-cma over 8 achiral channels.
- TODO: once r56 lands, post nematic + control result incl. acknowledging swarm-c's M2-collinearity critique.

## wakeup 7 (19:54)
- nem2: (1,1,.5) s21 1.4092 / r46 1.3756; (1.15,1.15,.7) 1.4687 / 1.3800; (.85,.85,1.3) 1.4651 / 1.4129; (1,1,1.5) 1.4634 / 1.4026;
  two-pair e .30: 1.3272 / 1.2892; e .36: 1.3353 / 1.2167. Every C2 variant is below C6 (1.500 / 1.420), so C6 is a local optimum.
- Posted result 20261013T195448.770Z_swarm-e_result_b78f (controls + nematic, incl. the correction to my M2 fit). r56 legs still queued.
- Board: swarm-a square wave g1Δ90 (c, c3) = (0.48, −0.32): s21 1.783, r46 1.655, r56 1.660 (best w3). swarm-d w2 strong: 5061
  (A = |G|²=4 Δ90 0.12, B = |G|²=1 Δ30+Δ150 −0.20) R_min 1.161. swarm-b: k-reassignment kills the gain.
- New family w2-profile (hyp 20261013T195638.141Z_swarm-e_hypothesis_2915): Δ90 collinear harmonics nG (|G|²=1,4,9,16 are n=1..4 of the
  S1 directions, same Δ90 mask) on top of 5061. Tool: work/addharm.py base_req parent out gcut n:c ... Batch w2p1 (7) ids in work/w2p1/ids.txt.
- Budget: 63 charged before w2p1, so ~70 now.

## wakeup 8 (20:17)
- w2p1 (base 5061 at gc8; s21 / r46): base 1.1614 / 1.2001; n1+.08 1.1671 / 1.1839; n1− 1.1086 / 1.1830; n3+ 1.1648 / 1.1703; n3− 1.0618 / 1.1819;
  n4+ 1.1411 / 1.1539; n4− 1.1387 / 1.2306. → profile shaping on w2 ≤ +0.5 % on min(s21, r46), no square-wave analogue. Near-null transfer.
  swarm-d mail: B + g1Δ90 +0.06 = 510b (best w2, R_min 1.178); swarm-d's w2-cma includes these coordinates jointly.
- w2p2 submitted (c417 n1+.16, f3ce n3+.16, 31b3 n1+n3, 891b n1+ n4−) to finish the 1D scan; then close w2-profile with coverage.
- Board: swarm-a g1sq + g3Δ0 (0208) s21 1.901 / r46 1.802; pure g1sq 4ee8 strong R_min 1.650. s21 overestimates past c≈0.5.
  swarm-c CMA ece3 R_min 1.653. swarm-b: k-reassignment collapses every winner on both parents.
- Refreshing the geometry proxy over 584 board requests (collect.py in background → collect2.log) to look for a single-particle
  quantity that tracks R on the new ridge.
- My r56 legs (controls, nematic, w2-profile) have been queued > 1 h.

## wakeup 9 (20:39)
- **891b** (5061 + n1 +0.08 + n4 −0.06): s21 1.2022, r46 1.2376, r56 1.2276, conv46 1.2377 → R_min 1.2022, STRONG, #1 on w2 (prev 510b 1.178).
  Superadditive: n1+ alone (2dc8) s21 1.167 (R_min 1.167, strong); n4− alone (cd9c) s21 1.139.
  w2p2: c417 n1+.16 1.1607 / 1.1456; f3ce n3+.16 1.0567 / 1.1113; 31b3 n1+n3 1.1692 / 1.1542.
- w2p3 submitted (8, work/w2p3/ids.txt): (c1, c4) ∈ {(.12, −.06), (.08, −.10), (.12, −.10), (.16, −.12)}; (.08, −.06) + n3 ±.06; + n2 ±.04.
  Note: submit-batch has no --builds-on.
- Proxy refresh (501 reqs): within R>1.1 on r46, |corr| ≤ 0.26 for logM2k, defect, Fstd, Sratio. Single-particle geometry is NOT predictive at the top.
- Board: swarm-c CMA 38fd strong R_min 1.986 (g3Δ0 0.54 + g9Δ90 −0.23). swarm-a 0208 R_min 1.80. swarm-d: the PES ent-gap shrinks with R (20 → 3.4–4.7).

## wakeup 10 (21:01)
- w2p3 (s21 / r46): n2−.04 (5085) 1.2104 / 1.2487 (best s21); n2+.04 1.1804 / 1.2188; n3−.06 1.1393 / 1.2316; n3+.06 1.1930 / 1.2256;
  (.08, −.10) 1.1609 / 1.2564; (.12, −.06) 1.2027 / 1.2222; (.12, −.10) 1.1942 / 1.2578; (.16, −.12) 1.2002 / 1.2640. Flat ridge at ~1.20, s21 binding.
- w2p4 submitted (5): A lowered (n2 −.04/−.08) combined with the (c1, c4) ridge, + n3 +.04. Ids in work/w2p4/ids.txt. After this, close w2-profile (coverage post).
- r56 queue: my control/nematic r56 legs have been stuck since ~19:15; swarm-b asked the operator (12f0) about the same.
- Board: swarm-b phase-only chiral S4 combo: s21 1.054, r46 1.27 (big spread; checking artefacts).

## wakeup 11 (21:22)
- w2p4 (s21 / r46 / r56): f4b7 (.08, −.06, n2 −.08) 1.2034 / 1.2523; a1ce (.12, −.06, n2 −.04) 1.2090 / 1.2377; a6f4 (.12, −.10, n2 −.04) 1.2127 / 1.2790;
  265c (+n3 .04) 1.1989 / 1.2410; **044c (.16, −.12, n2 −.04) 1.2202 / 1.2907 / 1.2976** (new w2 best). 5085 STRONG done: conv46 1.2488.
- Posted interim result 20261013T212255.861Z_swarm-e_result_e9d5; mailed swarm-d 044c as a CMA seed.
- w2p5 submitted (5): (.20, −.15, n2 −.04), (.16, −.12, n2 −.08), (.24, −.18, n2 −.06), (.20, −.15, n2 −.08), (.16, −.16, n2 −.04).

## wakeup 12 (21:44)
- 044c STRONG done: conv46 1.2899, R_min 1.2202. a6f4 R_min 1.2127 (strong).
- w2p5 (s21 / r46): f6be (.16, −.12, n2 −.08) **1.2311** / 1.3093; fae5 (.20, −.15, n2 −.08) 1.2237 / 1.3308; 2198 (.20, −.15, n2 −.04) 1.2096 / 1.3052;
  e7c8 (.16, −.16, n2 −.04) 1.1621 / 1.3132; 8d3b (.24, −.18, n2 −.06) 1.2002 / 1.3314. Lower A helps s21; larger |c4| hurts s21.
- addharm.py now takes 'b:c' (adds to the B channel = |G|²=1 Δ30+Δ150). w2p6 (5): n2 −.12/−.16 at (.16, −.12), n2 −.12 at (.20, −.15), B ±.04 at f6be.
- Board: swarm-c CMA 0fea R_min 2.145 (w3), Σ|α| 2.19 near the box.

## wakeup 13 (22:06)
- f6be STRONG: s21 1.2311, r46 1.3093, r56 1.3019, conv46 1.3087 → R_min 1.2311 (w2 best). fae5 R_min 1.2237, 2198 1.2096, 8d3b 1.2002.
- w2p6 (s21 / r46): e353 (B −.04) 1.2320 / 1.2705; 1d8a (B +.04) 1.2266 / 1.3335; 91aa (A=−.04) 1.2318 / 1.3105; 66ad (A=−.08) 1.2202 / 1.2903;
  a180 1.2277 / 1.3314. s21 plateaus at ~1.232, so w2-profile is converged. Coverage post due once the promotions land.
- New family w2-phasemap (hyp posted): chiral M·T-allowed phase combos β(C_θ − C_{180−θ})/√2 for |G|² = 1, 3, 4, 9, 12 × T1 on f6be, β ±0.04.
  Tool work/phaseadd.py. Ids in work/ph1/ids.txt. Mailed swarm-b (they own S4 / 12-member shells and phase on 044c).
- Board: swarm-a α×β cross term on w3 (0fea + S4 chiral β 0.06 → s21 2.740, r46 2.843).

## wakeup 14 (22:15)
- e353 STRONG R_min 1.2320 (conv46 1.2707); 91aa R_min 1.2318 (r56 1.2814).
- ph1 s21 (base f6be 1.2311), β ±0.04 per chiral combo: g1 1.2622 / 1.1613; g3 1.1550 / 1.2671; g4 1.1339 / 1.2637; g9 1.2299 / 1.1867;
  g12 1.2361 / 1.1326. Odd parts ≈ +5.0, −5.6, −6.5, +2.2, +5.2 % per 0.04, so a large first-order α×β cross term on w2 too.
- ph2: gradient line (unit gradient u = g1 .442, g3 −.491, g4 −.568, g9 .189, g12 .453) at t = .04, .08, .12, .16. Ids in work/ph2/ids.txt.
- Board: swarm-a w3 phase line still rising at β=0.20 (s21 3.43, r46 3.89); a human sanity request (3420). swarm-c w3-cma closed (0fea R_min 2.145).

## wakeup 15 (22:37)
- ph1 r46 (base f6be r46 1.3093): g1+ 1.3442 (r56 1.3340); g1− 1.2323; g3+ 1.2864; g3− (547f) 1.3340 (STRONG R_min 1.2671);
  g4+ 1.1586; g4− (d7dd) 1.4093 (STRONG R_min 1.2637, conv46 1.4079); g9+ 1.3247; g9− 1.3231; g12+ 1.3664; g12− 1.2924.
- ph2 gradient line, s21 / r46: t.04 (44a6) 1.3044 / 1.4378; t.08 (7818) 1.3122 / 1.5650; t.12 1.2122 / 1.6691; t.16 1.0087.
  s21 peaks at t≈.06–.08 while r46 keeps rising, so the s21/r46 split grows with β (same pattern as on w3).
- ph3 (5): grad t=.06; t=.06 with α ×1.2 / ×0.8; t=.04 with α ×1.2; equal-magnitude sign pattern .035. phaseadd.py now takes ASCALE env.
- Board: swarm-a w3 phase optimum β≈0.40 on 0fea: d48b s21 3.919, r46 5.013, r56 4.882. swarm-b: the w2 S4 phase on 044c gives s21 1.267, r46 1.405.

## wakeup 16 (22:59)
- 7818 STRONG R_min 1.3122 (s21 1.3122, r46 1.5650, r56 1.4612, conv46 1.5634). 44a6 strong R_min 1.3044.
- ph3 s21 / r46: d445 grad t.06 1.3166 / 1.5046; 93af (α×.8) 1.3026 / 1.4851; 187c (α×1.2) 1.3096 / 1.4828; ec0e (t.04, α×1.2) 1.2973 / 1.4093;
  02d6 sign-.035 1.3131 / 1.5426. α rescaling is neutral, and the 6-shell phase saturates at s21 ≈ 1.32.
- swarm-b claims w2 strong: f6be + chiral S7×T1 phase, b87e R_min 1.350 (6fc7 s21 1.397 / r46 1.620 / r56 1.563).
- ph4 (4): my gradient at t = .03, .05 on top of b87e and 6fc7. Mailed swarm-b.
- Board (w3): swarm-c CMA2 4462 R_min 4.182 (r46 5.46); swarm-a: the α·β synergy multiplies R ≈ 1.5 at β = 0.2.

## wakeup 17 (23:21)
- ph3 strong: d445 R_min 1.3166 (r56 1.4301, conv46 1.5035), 02d6 1.3131, 187c 1.3096.
- ph4 on swarm-b's S7 points (s21 / r46): 868e (6fc7 + t.03) 1.4285 / 1.7172; 5e61 (6fc7 + t.05) 1.4290 / 1.7779; 4c33 (b87e + t.03) 1.3992 / 1.5640;
  796f (b87e + t.05) 1.4121 / 1.6286. → the 6-shell gradient ADDS to the S7 phase (+2.3 % s21 over 6fc7's 1.397).
- swarm-b runs phase-cma on f6be over S4/S7/S9 combos. Mailed: include my 6-shell combos; I stop adding w2 points.
- New: w3-phasemap: the 6-shell chiral combos ±0.04 on swarm-a's d48b (10 reqs, work/ph5/ids.txt). Hypothesis posted; mailed swarm-c.

## wakeup 18 (23:44)
- w3-phasemap on d48b: near-null (best 5745 g9 −.04 s21 3.966, r46 ≤ base). Phase directions are parent-specific.
- 868e / 5e61 STRONG on w2 (R_min 1.4285 / 1.4290). w2 leader: swarm-b phase-cma 83f6 R_min 1.453. w3 leader: swarm-c 9d3e R_min 4.823.
- Posted coverage: w2 (20261013T234507.580Z_swarm-e_result_7499) and w3 (posted next).
- Remaining budget ~370. Ideas left: none distinctive that others aren't covering (swarm-b owns the w2 phase CMA, swarm-c the w3 CMA2).
- Posted the w3 coverage (20261013T234530.625Z_swarm-e_result_ed79).
- New: w2-jcma (work/jcma.py; state in work/jcma/state.json). Joint α+β ES on 83f6 (swarm-b's w2 best, R_min 1.453), 7 coords, λ=8, μ=4.
  Each wakeup: run `uv run ... python work/jcma.py` from work/ (it collects the generation if complete, else prints "waiting").
  gen0 submitted (p0 = x=0 = 83f6 copy). Hypothesis posted; mailed swarm-b and swarm-d.

## wakeup 19 (00:09, 10-14)
- jcma gen0 so far min(s21, r46): p0 1.4527 (= 83f6, free), p1 1.4012, p2 1.4580, p3 1.3866, p4 1.2250, p5 1.3604, p6 pending, p7 1.4634.
- swarm-b added my gradient u to its phase CMA (w2ph2; gen0 best s21 1.487). It stops after 2 more generations and suggests I reseed
  from its best. Plan: when its best lands, switch jcma BASE to it (offsets x on top), reset the mean to 0, and keep sigma.
- swarm-a posted its final summary. swarm-c w3-cma2 at 5.345 (bb15), extending to 100 evals.

## wakeup 20 (00:25)
- jcma gen0 complete: f = [1.4527, 1.4012, 1.4580 (0e0c strong, r46 1.878), 1.3866, 1.2250, 1.3604, 1.0064 (no promotion), 1.4634 (6438 strong)].
  Fixed result(): s21 < 1.02 is final (no r46). gen1 submitted (mean ≈ s13 −0.16, s7 +0.17, others ~0).
- swarm-b phase-cma best dd54 R_min 1.4870 (r46 1.834). swarm-d closed (best 1.346, bef5); it suggests re-optimizing α with phase on.
- Plan: after swarm-b's last 2 generations, rebase jcma on its best (BASE := that req, mean := 0).

## wakeup 21 (00:47)
- jcma gen1 f = [1.3528, 1.0466, 1.3842, 1.4418, 1.4251, 1.0409, **1.4713** (b64c), 1.4550]; success 1/8, so sigma shrinks. gen2 submitted.
- swarm-b closed phase-cma: dd54 STRONG R_min 1.487 (f6be + 7-coord chiral phase incl. my u).
- jcma.py now reads the base from state['base']. Plan after gen2: set state['base'] = dd54 (20261013T234457.189Z_swarm-b_req_dd54), mean = 0, keep sigma.

## wakeup 22 (01:09)
- jcma gen2 f = [1.3943, 1.3912, 1.4569, 1.2031, 1.3758, **1.4727** (1413-ish p5), 1.4531, 1.3328]. Plateau ~1.47 around 83f6, below dd54 1.487.
- REBASED: state['base'] = dd54, mean = 0, sigma = 0.7·SIG0, gen3 submitted (p0 = x=0 = dd54 copy).
- Board: swarm-c w3 6bcd R_min 5.643; swarm-b k-reassignment kills dd54 (→0.211) and bb15 (→0.083); swarm-b w3 phase-only CMA (α=0).

## wakeup 23 (01:31)
- jcma gen3 (dd54 base) f = [1.4870 (= dd54), 1.4141, 1.4665, 1.4447, 1.4868, **1.5251 (1413)**, 1.4745, 1.3753]. New w2 best on min(s21, r46); r56 pending.
  gen4 submitted (mean: s7 +0.14, others ≈ 0).

## wakeup 24 (01:53)
- **1413 STRONG**: s21 1.5251, r46 1.8256, r56 1.7528, conv46 1.8232 → R_min 1.5251, the w2 record. Claim posted (20261014T015432.208Z_swarm-e_claim_e87c).
  x = (dA −.026, dn1 −.015, dn4 −.035, dB +.004, s13 −.033, s7 +.194, t −.016) on dd54.
- jcma gen4 f = [1.4361, 1.4903, 1.4593, 1.3421, 1.4479, 1.4712, 1.4706, 1.4039], 0 successes. gen5 submitted.
  Switched to ELITIST centering (mean := best x since the rebase) from the gen5 collection on.
- Board: swarm-c w3 97ac R_min 6.316, extending to 150 evals. swarm-b closed the w3 phase-only line (a05b 1.054 s21; Nk21 caps phase-only near +5 %).

## wakeup 25 (02:15)
- jcma gen5 f = [1.5115, 1.4358, 1.4275, 1.4835, 1.4678, 1.3847, **1.5295** (d882), 1.4771]; elitist mean → s7 +0.60 (|G|²7/19 phase ×1.6).
  gen6 submitted. Gains now ~0.3 %/gen; plan: ≤ 2 more gens, then close w2-jcma with coverage.
- swarm-b: static controls for swarm-c's 6bcd all below the parent (ρ̄ 0.91, frozen-K 0.90/0.97, frozen-Γ 0.74/0.80).

## wakeup 26 (02:40)
- d882 STRONG R_min 1.5295 (r46 1.7767, r56 1.7183, conv46 1.7754).
- jcma gen6 f = [1.3449, 1.4715, 1.5176, 1.5074, 1.4896, 1.5092, **1.5401** (3e70), 1.4400]. gen7 submitted (planned last unless still climbing).

## wakeup 27 (03:02)
- jcma gen7: no improvement (best 1.5286). **3e70 STRONG R_min 1.5401** (r46 1.8812, r56 1.7889, conv46 1.8769), the w2 record.
  Closed w2-jcma with coverage (20261014T030305.141Z_swarm-e_result_6c0b): 64 evals, all PASS.
- swarm-c closed w3-cma2: 3231 R_min 7.019 (boundary: Σ|α| 2.45, Σ|β| 1.83).
- New w2-cma2 (work/jcma2.py, state work/cma2/state.json): 11-coord CMA-ES (λ=10) on 3e70, σ0 .08; hypothesis posted; gen0 submitted.
  Each wakeup: `cd work && uv run ... python jcma2.py`.

## wakeup 28 (03:26)
- cma2 gen0 f = [1.5401 (base), 0.997, 1.265, FAIL, FAIL, 1.017, 0.802, FAIL, 1.424, 0.641]. Steps of σ 0.08 are too big; the w2 basin is narrow.
  All 3 FAILs = "ground manifold not clean" (splitting/Δ 0.11–0.18), all with s13 ≥ +0.26 (|G|²13 phase ×1.3).
  → the |G|²13 chiral phase on w2 can't grow without splitting the Laughlin manifold. gen1 submitted (σ 0.0695).
- swarm-c final: e688 R_min 7.060 (boundary). swarm-c is done (304 evals).

## wakeup 29 (03:48)
- cma2 gen1 f = [FAIL, 1.2543, 1.1468, 1.4046, 1.2880, 1.2164, 1.3849, 1.3679, 1.2714, FAIL]; σ 0.064, mean drifting off 3e70.
  The w2 optimum is sharply peaked (0.1 in α costs 10–30 %). gen2 submitted; if no improvement → close w2-cma2 as a negative (~30 evals).

## wakeup 30 (04:10) — DONE
- cma2 gen2: fec6 s21 1.5511 / r46 2.077 but r56 FAIL (splitting 0.101). 7/30 FAILs, all manifold splitting. Closed w2-cma2 (20261014T041146.983Z_swarm-e_result_6eee).
- Final summary posted; ran `swarm done`. 223/500 charged. The w2 record stays 3e70 (R_min 1.5401, strong).
