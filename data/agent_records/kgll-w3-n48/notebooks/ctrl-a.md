# ctrl-a notebook

Started 2026-10-08T04:37:41+00:00.

## 2026-10-08 05:00 — wakeup 1
- Read brief, docs 40/46, key-facts, ADR-0040, kdep_envelope. Lessons: 024 pilot gain
  (+0.5 % at 4x6) flipped sign at 5x6; precision check saw w3 alpha[S1,T1]=+0.05 -> +1.85 % at Nk=21.
- Parent gaps: w3 s21 4.5714e-4, r46 4.3823e-4; w2 s21 3.2272e-4, r46 3.0955e-4.
- Tools: work/gen.py (stars S[|G|^2], T[|R|^2]; build(parent, terms, g_cutoff)).
  Stars: S keys 1,3,4,7,9,12,13,16,19,21; T keys 1,3,4 (T[4] is the brief's "T3").
- Posted hypothesis w3-axis-screen; submitted 70 axis probes (work/inputs/screen1:
  a_* alpha=+-0.05, b_* beta=+-0.03, g_cutoff 7). `swarm show` 'source' maps req -> file.
- Next: collect slopes/curvatures; then CMA-ES/line search in positive subspace, prefer T1.

## 05:22 — wakeup 2
- Screen1 done (70). Only alpha[S1,T1]+0.05 (s21 1.0223, r46 1.0262, c749) and alpha[S3,T1]+0.05
  (s21 1.0207, r46 1.0286, e75a) positive; r56 pending. All else <1; beta even; big quadratic penalty.
- Diagonal quadratic fit (T1 row): b,c per axis; S1 b=1.07 c=12.5; S3 b=.94 c=10.6; others tiny gain.
- Posted result+coverage for screen1. Hypothesis w3-T1-refine; submitted b2 (32): joint classes j0/j1/j2
  for S1,S3,S4,S9 x T1 (a=+-0.015 per pair term), S1xS3 grid, diag optimum 0.7/1/1.3.
- Geometry: S1 G0 vs T1 R0 relative 30deg (j0,j2 mirror pair; j1 = 90deg); S3 relative 0deg (j1,j2 mirror pair).
- work/collect.py [filter] prints table (slow first time, caches finished).

## 05:40 — wakeup 3
- b2 results: joint classes NOT mirror-symmetric (Chern band breaks mirror). Linear gain in S1 class j2
  (a=+.015: s21 1.0312, df68; -.015: .9470) and S3 class j0 (+.015: 1.0297, 7c84; -: .9518). Other classes flat/neg.
  S4 classes all ~0.9966 (flat), S9 classes slightly neg.
- diag_T1row x0.7/1.0/1.3: s21 1.0366/1.0455/1.0506, r46 1.0446/1.0630/1.0802 (3c9b) — still rising.
- S1xS3 full-star grid: (0.06,0.06) s21 1.0341 r46 1.0576; opposite signs lose.
- Submitted b3 (62, family w3-chiral-joint): A line S1j2+S3j0, B beta classes, C T2/T3 classes, D S7/S12 classes.
- Budget after: 164/500. Next: CMA-ES over linear classes; watch r56 of promoted ones.

## 06:06 — wakeup 4
- b3: base = S1 class j2 + S3 class j0 (T1) linear: a=.02/.03/.04/.05 -> s21 1.080/1.122/1.165/1.210,
  r46 1.069/1.104/1.141/1.178 (1802 best). Single class: kink at 0 (steeper loss for a<0).
  beta classes all <=1; T2/T3 classes flat; S7 o0j1 / o1j2 small linear (+0.5-0.7% @.015); S12 flat.
- M2^(k) boundary: base a=0.24 -> ratio 2.73, a=0.28 -> 3.23 (rejected). Max a ~0.25.
- Submitted b4 (53, w3-chiral-push): line to 0.24, S1:S3 ratio, +S7, local slopes S13/S16/S19/S21 classes at base(.05);
  b4w2 (3, w2-chiral-transfer). Budget -> 220/500.
- r56 pending for everything including parents (broker queue). Wait.
- TODO: request matched-density static control for winner (alpha!=0). Gen helpers: orbits(q) in batch4.py.

## 06:30 — wakeup 5
- b4: base line peak a=0.10: s21 1.3862 r46 1.3921 (63f3); 0.14 1.335; 0.20 1.011; 0.24 FAIL (EG .2). EG drops with a.
- extra linear classes at base(.05): S13 o0j0,o1j0 (+); S19 o0j2,o1j1 (-, lowers M2k!); S21 o0j1,o1j2 (-). S16 flat.
- w2: base hurts w2 (0.98/0.96/0.87). Parent-dependent; w2 would need own class screen.
- Submitted b5 (16, w3-chiral-combo). Posted request for matched-density control on 63f3.
- work/lib.py: DIRS + vec(**coef) helper. Budget -> 236/500.
- Next: CMA-ES in 10-class subspace (write work/cma loop, ask-tell via files).

## 06:47 — wakeup 6
- b5: X_b10_all (S1j2 .1, S3j0 .1, S13 .03, S19 -.04, S21 -.02): s21 1.7774 r46 1.7547 (c751). S19 -.06 on base: 1.6785/1.6384,
  M2k only 1.158. S13 cluster-sensitive (r46 << s21). grad line s21 ~1.37-1.39 but r46 1.52-1.59.
- Started CMA-ES A (work/cma_es.py; 6 dims S1j2,S3j0,S19pair,S21pair,S13pair,S7pair; obj min(s21,r46); lam 8, sig .025).
  Gen0 submitted (map in work/inputs/cma_A_g0/map.tsv). Loop: `cma_es.py tell A` then `ask A`, submit-batch > map.tsv.
- b6 (5): S19 line on base to -0.15, S19 alone. Posted request about r56 stuck (all pending ~2h).
- Budget -> 249/500.

## 07:00 — wakeup 7
- b6: S19 alone harmful (-0.05: 0.81; -0.10 FAIL). On base(.10): -0.09 1.22, -0.12/-0.15 FAIL. S19 optimum ~-0.05, non-additive.
- CMA gen0 s21 best 1.8765 (5b5b), r46 queued (r46 lane slow now). tell A not ready yet.
- Submitted w2-chiral-screen (24). Budget -> 273/500.

## 07:21 — wakeup 8
- CMA A gen0 f(min s21,r46): best 1.6752 < X_b10_all's 1.7547 (c751). Rugged landscape. Gen1 submitted (8).
- w2 screen: S1 j0,j1 negative a linear (+1.4% @ -.015; 1a5f, c8c0); S3/S9/S12 flat. Submitted w2-chiral-push (22).
- Budget -> 303/500. r56 still pending broker-wide; no human reply yet.

## 07:45 — wakeup 9
- CMA A gen1 best 1.8279 (x4 = [S1j2 .093, S3j0 .115, S19 -.023, S21 -.040, S13 .061, S7 -.011], req 552a). Very rugged
  (neighbours 1.15). Gen2 submitted.
- w2 line S1 j0+j1: -0.03/-0.05/-0.08/-0.12 -> s21 1.054/1.082/1.107/1.108, r46 1.055/1.088/1.130/1.149.
  local at base(-.05): S4 o0j2 + gives 1.1038/1.1227 (a643). S19 classes mixed (r46 up, s21 flat).
- b9w2 (4): base(-.08)+S4j2. Budget -> 315/500.
- 08:06 wakeup 10: queue slower (12 in flight); CMA gen2 and b9w2 not ready. Waiting.

## 08:35 — wakeup 11
- Queue stalled: 122 of my reqs waiting at r56. Withdrew 109 (work/withdraw.txt); kept c749 1802 63f3 c751 259a 3ef3 552a ed2e 5b5b 6a53, w2 7bb5 b1b5 a643.
  In future: withdraw marginal promotions promptly (only keep top few per family).
- CMA gen2 + b9w2 still unscored.

## 09:15 — wakeup 12
- CMA gen2 best 1.7568 (9d62); no gain over 552a (1.8279). Withdrew 7 weaker gen2. Gen3 submitted. Budget -> 323.
- w2 b9: base(-.08)+S4j2 .03: 1.1445/1.1850; +S19: 1.1480/1.2193 (5f07); S4j2 .06: 1.1473/1.2245 (2359). Withdrew 9522,1197.
- r56 still pending everywhere. Plan: reserve ~100 evals for post-r56 reaction; CMA up to gen5.

## 09:45 — wakeup 13
- CMA gen3 best 1.7934; plateau. Withdrew weak gen3. Stopped CMA after gen3 (32 evals total).
- Submitted w3-local-552a (56): local slopes around 552a for remaining T1 classes, T2/T3 classes of S1/S3, beta on S1j2/S3j0/S19.
  map: work/inputs/b10/map.tsv. Budget -> 379/500. Reserve ~120 for post-r56.

## 10:10 — wakeup 14
- b10 local slopes at 552a: r46 pinned ~1.827 for nearly all directions (binding). r46 movers: S9j2T1 - (s21 1.803, r46 1.882, 0ac2),
  S3j2T3 - (1.886/1.838, eb1d), S1j1T3 - (1.831/1.840), beta S1j2 -/S3j0 - (~+.005 r46). s21 boosters with flat r46:
  S1j0T1+, S1j1T1+, S3j2T1+, S3j1T1+, S12j0+ (~+0.02-0.03 s21). Phase now linear (chirality+amplitude bg).
- b11 (8): combos C1..C8 around 552a (u=0.015). Withdrew all 56 b10 promotions. Budget -> 387.

## 10:30 — wakeup 15
- b11: C4 (S9 -1u, S3j2T3 -1u on 552a) s21 1.8321 r46 1.8929 (e22e) = new best min. C5 (x2): 1.7616/1.9254. s21<->r46 tradeoff.
- Paused optimization (overfitting risk to 2 small clusters). Posted interim result + coverage (result_23b6). Withdrew b11 except C4,C5.
- Budget 387/500; 113 reserve for post-r56. Keep r56 queue: c749 1802 63f3 c751 259a 3ef3 552a ed2e 5b5b 6a53 9d62? e22e 8515, w2 7bb5 b1b5 a643 2359 5f07.
- 11:02 wakeup 16: no r56 yet. Submitted 3 diagnostics (w3-numerics): 552a/63f3/e22e at n_mesh 64, g_cutoff 10 on s21 (map b12diag). Budget 390.
- 11:23 wakeup 17: conv diagnostics: 63f3 exact, 552a -0.5%, e22e -0.75% at g10/n64. Posted result. Still no r56.
- 11:54 wakeup 18: no r56 (7 h). Holding.
- 12:25 wakeup 19: no r56. Holding.
- 13:29 wakeup 20: no r56 (8.5 h). Holding.
- 14:30 wakeup 21: no r56 (9.5h). Submitted w2-local-5f07 (30, map b13w2). Budget 420. Withdraw b13 promotions after scoring.
- 14:52 wakeup 22: w2 local slopes: s21 boosters S3(j0+,j1-,j2-), S12(j0-,j1+,j2+), S9j2+ (~+1.5% each); S7 o0j1-/o1j2- raise r46 only (1.24). Withdrew b13. Submitted b14w2 (6 combos). Budget 426.
- 15:13 wakeup 23: w2 combos: C_all_x1 (S3 trio+S12 trio+S9j2+S7 pair at 1u on 5f07) 1.1767/1.2586 (dfc2) = w2 best. x1.5/x2 lose s21. Withdrew others. Budget 426. Next: hold for r56 (hourly).
- 16:14 wakeup 24: no r56 (11 h). Holding.
- 17:15 wakeup 25: no r56 (12 h). Holding.
- 17:47 wakeup 26: no r56. Holding.
- 18:48 wakeup 27: no r56 (14 h). Holding.
- 19:49 wakeup 28: no r56 (15 h). Holding.
- 20:50 wakeup 29: no r56 (16 h). Holding; plan: swarm done ~6 h before deadline if r56 never arrives.
- 22:04 wakeup 30: no r56 (17 h). Holding.
- 23:05 wakeup 31: no r56 (18 h). Holding.
- 00:06 (10-09) wakeup 32: no r56 (19 h). Holding.
- 01:07 wakeup 33: no r56 (20 h). Holding.
- 02:21 wakeup 34: no r56 (21 h). Holding.
- 03:22 wakeup 35: no r56 (22 h). Holding.
- 04:23 wakeup 36: no r56 (23 h). Holding; 24 h to deadline.
- 05:25 wakeup 37: r56 LANE RAN. All promoted w3/w2 candidates confirm on r56+conv46, all PASS, no sign flips. Broker claim 'strong': e22e (min 1.8265), 552a, 8515, c751, 1802, 63f3, 2f47; w2 dfc2 (min 1.1767), 2359. c749 suggestive. Posted claim_b4c9. Submitted b15 (8): 2f47/9d62 + D(S9,S3T3) combos. Budget 434.
- 05:53 wakeup 38: b15: 2f47+D(2,2) (0896) s21 2.121 r46 1.943 r56 2.030 = new best min 1.943 (conv pending). Withdrew 5 weak. b16 (6): 2f47+D33/D44/D32/D23, mid+D22/D33. Budget 440.
- 06:20 wakeup 39: b16: 2f47+D44 (060b) 2.040/2.038/2.064 (min 2.038, conv pending); D33 (d6e7) 2.161/1.997/2.048; D32 (8d83). 0896 conv46 1.915 (min 1.915). b17 (3): D55, D43, D54. Budget 443.
- 06:38 wakeup 40: 060b complete: 2.0404/2.0383/2.0638/conv 2.0073 (min 2.0073) = best. D54/D55 worse s21; withdrew. Waiting 44f0 (D43) r56/conv then final report + done.
- 07:00 wakeup 41: 44f0 min 2.0064 (plateau). Posted FINAL result_de1a, ran swarm done. Loop stopped.
