# ctrl-a notebook

Started 2026-10-15T04:13:55+00:00.

## 2026-10-15 04:15–04:30 — wakeup 1: setup + axis scan launched
- Read brief, docs 40/46, ADR-0032 schema, kdep_envelope chart:
  gamma = sum (alpha/2 + i beta) O_s(r) F_p(k), O/F unit-mean-square star functions.
- Tools in work/: gen.py (stars in solver basis; spatial S1..S21 (+a/b chiral
  orbits of 12-member shells), momentum T1(|R|²=1), T2(3), T3(4)); axis_batch.py
  (one-block batches, g_cutoff 6); collect.py (pulls all results -> work/results.json, table).
- Posted hypothesis 20261015T041916.559Z_ctrl-a_hypothesis_c310 (w3-axis).
- Submitted batch ax1 (32): 10 stars x T1, alpha ±0.05, beta +0.05, beta -0.05 on S1,S4.
- Prepared work/batches/ax_T2, ax_T3 (30 each), not yet submitted.
- Early: evals take ~1 min; outer stars (S12,S13,S16) lose 5-10% at alpha ±0.05,
  25-35% at beta 0.05. Strong negative curvature: ideality-breaking cost dominates.

## 2026-10-15 04:30–05:15 — phase 1 done, robust_positive reached
- w3-axis (76 evals): only T1 has linear response (S1 +1.07, S3 +0.95 /unit);
  T2/T3 even & negative; beta even & negative (TR x mirror). Result+coverage
  posted 20261015T050920.261Z_ctrl-a_result_f0e8.
- w3-T1amp: diagonal-Newton direction from axis model (work/axis_T1_model_w3.json).
  Line (s21/r46/r56/conv46): x1.0 f242 1.042/1.065/1.055/1.064; x1.4 def8
  1.045/1.089/1.067/1.088; x1.8 222a 1.039/1.110/1.070/1.109; x2.2 2e7a
  1.026/1.127/1.064/1.125; x2.8 0.990 (s21). broker claim robust_positive on all of
  f242, def8, 222a, 2e7a. Claim post 20261015T050844.257Z_ctrl-a_claim_fc21.
- Pairwise cross terms (15) and quad fit (work/quadfit.py): model optimum ~ the
  Newton x1.0 point, pred 1.048 at s21. s21 saturates ~1.045; r46 keeps rising; r56
  peaks ~x1.8 at 1.070. Large finite-size spread.
- Chiral phase (beta on S7a etc): linear term exists (S7a 0.924/0.848) but
  gain ~0.3% max. Phase-only route is weak.
- M2(k) rises with the deformation; R_gap*M2/M2(k) at 222a: 0.993/1.060/1.023.
  Requested matched-density control definition: 20261015T050900.871Z_ctrl-a_request_82bf
- w2 axis: T1 linear terms but different signs (S1 -0.69, S4 +0.95, S13 -1.05,
  S16 -1.42, S19 +1.02); diag-Newton predicted gain 8.6%. Line submitted (w2line).
- Submitted w3loc18: center newton x1.8 +-0.02 on each T1 star (20), to get
  r46/r56 gradients via free promotions. Goal: strong (>=1.10 on r46,r56,conv46).
- Budget: ~157/500 after these.

## 2026-10-15 05:15–05:45 — local probes, r56 bottleneck
- w3loc18 (center newton x1.8 ± 0.02 per T1 star): s21 gradient positive on all
  stars' + side (S12+ 7bc9 1.0542, S16+ cbdf 1.0565); minus sides of S12/S13/S16/
  S19/S21 drop below 1.02 (not promoted). r46/conv46 1.09–1.12, r56 stuck at
  1.062–1.074 for every probe. Many probes carry robust_positive.
- w2 newton line: x0.6 1.014, x1.0 0.966, x1.4 0.889, x1.8/2.2 FAIL. Diagonal
  model bad for w2 (cross terms); 15 pair probes queued (p3w2).
- p3w3 queued: T2/T3 ±0.02 blocks on S1,S3,S4,S12,S16 at x1.8 center + 4 grad steps.
- Controls: work/control.py (A: BZ-avg density, ok via --control check) and
  work/control_b.py (B': nearest M2-matched static density on 8 shells, positivity
  binding; rerun on 96-grid in background). Not submitted yet: waiting one
  wakeup for the human's answer on request 82bf.
- wait loop: work/wait.sh (counts non-final + running stages).

## 2026-10-15 05:45–06:25 — T2/T3 linear terms at deformed center (key finding)
- p3w3: at the T1 x1.8 center, T2 blocks have big linear terms (zero at alpha=0):
  s21 grad/unit S12T2 +2.34, S16T2 +2.19, S4T2 +1.70, S3T2 -1.57; T3 all negative
  (S16T3 -1.63, S12T3 -1.23). Best single: S12T2+0.02 4377 s21 1.082/r46 1.096/
  r56 1.0815/conv46 1.098; S3T2-0.02 4b13 1.072/1.113/1.0837/1.111. r56 finally moves.
  Grad steps in T1 (stepA..D) did little; stepC (S12,S16 +0.04) dropped s21 to 0.966.
- Submitted p4: line along T2/T3 s21-gradient (max comp 0.02..0.1), T2-only/T3-only,
  T2 ±0.02 probes on S7,S9,S13,S19,S21. Gradient saved work/grad_c18_T23.json.
- w2 pairs: S1-/S4+ e4fe 1.020/1.060/1.032, S4+/S7+ c602 1.021/1.054/1.031 (suggestive).
  Quad model (w2) optimum + Newton x0.3/x0.45 submitted (w2opt).
- Control B'' built positive-by-construction (work/control_b2.py, |h|^2 with h on
  S1,S3,S4): work/batches/ctrl222a/ctrlB_m2match.json; control A ctrlA_bzavg.json.

## 2026-10-15 06:25–06:55 — T2 non-additivity; controls submitted
- p4: combined T2/T3 gradient line catastrophic (0.02 -> 0.838, >=0.05 FAIL);
  T2-only 0.04 -> 0.39; T3-only 0.04 -> 1.011. Single T2 probes on outer stars:
  S13T2-0.02 16d0 1.0974/1.1066/1.0924/1.1008 (best yet, near strong), S9T2+ 81da
  1.0863/1.1073/1.0854, S21T2- c6d3 1.0854/1.1088/1.0735. Non-smooth objective
  (gap = min over excitation branches?) — move one block / half-step pairs.
- w2: Newton x0.45 5544 1.0206/1.0885/1.0429; x0.3 0746 1.0205/1.0601/1.0334; quadopt worse.
- Submitted p5w3 (S13T2 line -0.01/-0.03/-0.04, 7 half-step pairs) and p5w2
  (T2 ±0.02 probes on 10 stars at w2 Newton x0.45 center).
- Submitted controls 63e0 (A) and 54d9 (B'') for 222a, s21/r46/r56.
- collect.py final-detection fixed (was re-fetching promoted requests).

## 2026-10-15 06:55–07:40 — controls, w2 robust, r56 plateau
- Controls for 222a: A (BZ-avg density, 63e0) 0.993/0.999/0.999; B'' (M2-matched
  static, 54d9) 0.900/0.972/0.926. Gain not explained by mean density nor by a
  static band of equal M2. Result 20261015T072704.277Z_ctrl-a_result_6d23.
- w3 phase 5: S13T2 -0.01 776c 1.0856/1.1164/1.0882; -0.03 1.054; -0.04 0.992.
  Pairs (half steps on S13T2- with S3T2-/S9T2+/S12T2+/S4T2+) all ~1.095-1.10 s21,
  1.11 r46/conv46, r56 1.089-1.092 (best d802 1.1004/1.1144/1.0918/1.1098).
  r56 plateau ~1.092 blocks 'strong'.
- w2 phase 5: S21T2-0.02 6913 robust_positive 1.0372/1.0746/1.0528/1.0761.
  Claim posted (w2). Other T2 probes: S12T2- 6f92 r56 1.0475, S9T2+ a338 1.0498.
- Submitted p6w3 (25 probes around C2 = x1.8 + S13T2-0.02: T1 scale 1.6/2.0/2.2,
  T2 ±0.01 on 9 stars, T3 -0.01 on 4) and p6w2 (6 around 6913).
- Budget ~285/500 after p6.

## 2026-10-15 07:40–08:15 — STRONG reached on w3
- p6w3 around C2 (= T1 x1.8 + S13T2 -0.02): single T2/T3 ±0.01 probes all r56
  1.085–1.094 (plateau). T1 scale at fixed S13T2: x2.0 438d 1.1039/1.1197/1.0986/
  1.1128 (robust); x2.2 3314 1.1075/1.1323/1.1024/1.1243 -> broker 'strong'.
  Claim posted 20261015T081334.414Z_ctrl-a_claim_c3e5 (edge: r56 1.1024).
- Submitted p7: S13T2-0.02 + T1 x2.4/2.6/2.8/3.0/3.4, and T1 x2.4 with S13T2 -0.01/-0.03.
- Controls for 3314 submitted: 7a97 (A), 87c2 (B'', M2 3.882).
- w2 p6: T1 x0.55 + S21T2- ae13 s21 1.0367 r46 1.093 (r56 pending); T1x0.35 1.036/1.055.
- Budget ~298/500.

## 2026-10-15 08:15–08:50 — session restart; controls for 3314; phase-only scan
- Session restarted (orphaned background waits); resumed from store, nothing lost.
- Controls for 3314: A 7a97 0.987/0.996/0.995; B'' 87c2 0.869/0.943/0.897 (M2 3.882).
- p7 line (T1 scale x2.4..3.4 + S13T2-0.02): s21 1.109 (x2.4, x2.6), 1.107 (x2.8),
  1.100 (x3.0), 1.068 (x3.4); r46 1.144/1.156/1.165/1.168/1.145; r56 queued (slow).
- Submitted w3-phase scan (12 evals, chiral beta ±0.01-0.02), hypothesis posted.
- Budget 310/500.

## 2026-10-15 09:20 — phase-only closed
- w3-phase: best combo 778c 1.0026, S7aT1 b+0.01 1.0017; rest < 1. Abandon posted
  (a277) + count correction note (36 evals, 31 P / 5 F).
- r56 stage of the T1-scale line still queued after ~1 h (broker backlog).

## 2026-10-15 09:50 — strong window
- T1 scale line + S13T2-0.02: strong at x2.2 (3314), x2.4 (034f 1.1093/1.1443/1.1038/1.1352),
  x2.6 (b3e0 1.1093/1.1556/1.1020/1.1455); x2.8/3.0 robust (r56 1.097/1.089).
  Result posted a499 (+ ref-correction note).
- w2: T1 x0.55 + S21T2-0.02 ae13 1.0367/1.0930/1.0576/1.0942 (robust, best w2).
  pairs at 6913 + S12T2-/S3T2- ~1.038/1.067/1.055/1.07.
- Submitted p8 (13 probes around 034f for r56 margin). Budget 323/500.
- Next ideas: w2 T1 scale up (x0.65, 0.75) + S21T2; final coverage posts for
  w3-T1amp and w2-T1amp; leave ~60 evals reserve.

## 2026-10-15 10:25 — p8 results; p9 submitted
- p8 around 034f (x2.4+S13T2-0.02): r56 best S1T3-0.01 9333 1.1155/1.1447/1.1069/1.1358,
  S9T1-0.01 4f42 1.1125/1.1560/1.1067/1.1457, S3T3-0.01 754c 1.1170/1.1474/1.1058/1.1387.
  S12/S16 + don't help (r56 ~1.103), S13m worse (1.093).
- w2 T1 scale + S21T2-0.02: x0.65 931e 1.0350/1.1053/1.0607/1.1079; x0.75 1.0318/1.1089/1.0618;
  x0.9 1.0146. w2 r56 caps ~1.06 (strong out of reach so far).
- p9: 6 combos of the r56-best probes at 034f; 10 w2 T3 ±0.01 probes at x0.65. Budget 342/500.
- Plan after p9: coverage posts for w3-T1amp and w2-T1amp; keep ~100 reserve; then decide done.

## 2026-10-15 10:57 — p9 results
- p9 combos at 034f: all3 (S9T1-0.01, S1T3-0.01, S3T3-0.01) d875 1.1194/1.1586/1.1115/1.1488
  (best; r56 margin 1.15%); S1T3_S9m 906c 1.1184/1.1566/1.1101/1.1463; T3pair 118f r56 1.1083.
  Small T3/T1 steps roughly additive here.
- w2 T3 probes at x0.65: r56 ~1.060-1.061 (no lift); w2 caps at r56 ~1.06.
- p10: all3 x1.5, x2.0, all3+S7m (3 evals). Then coverage posts + done. Budget 345.

## 2026-10-15 11:30 — wrap-up
- p10: all3 x1.5 7aa8 1.1117/1.1639/1.1138/1.1542 (best min, strong); x2.0 5026 r56 1.1151 but s21 1.1023.
  Diminishing returns (~0.1%/step) -> stop searching.
- Coverage posts: w3 amplitude e0ea, w2 amplitude 611a (plus axis f0e8, phase a277+0c29, controls 6d23).
- Controls for 7aa8 submitted (f80c A, 8d26 B''). After they land: post a note, then `swarm done`.
- Budget 351/500 after controls; remaining unspent by choice.

## 2026-10-15 11:36 — done
- Controls for 7aa8: f80c (A) 0.986/0.997/0.995; 8d26 (B'') 0.864/0.937/0.891. Note posted.
- swarm done with summary work/done.md. Final: w3 strong (7aa8), w2 robust (9bf0). 351/500.
