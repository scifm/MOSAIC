# ctrl-a notebook

Started 2026-10-02T03:52:23+00:00.

## 2026-10-02 04:00 — wakeup 1: setup + stage A1

- Read docs 40, 46, notes §5, theory §5/§8, kdep_envelope. Block = star products only:
  gamma = sum (a/2 + i b) O_S(r) F_T(k); O,F are cosine sums (even in r and in k separately),
  so true joint (G,R) C6 orbits with sin*sin parts are NOT expressible. Stars may be any
  inversion-symmetric set (chiral halves S4a/S4b, single pairs) -> less-symmetric choices possible.
- w3 density lives on the 2x sublattice (shells 3,6,8 = 2*S1, 2*S2, 4*S1). S1/S2 deformations
  create odd-lattice harmonics.
- Doc 46 (g_cut 4): w3 a[S1,T1]=+.05 -> +1.85%, -.05 -> -9.0%, b +.05 -> -4.4%, a[S3,T1] +.05 -> -3.75%;
  w2 a[S1T1]+.05 -5.05%, b -3.0%.
- Tools: work/gen.py (parent + terms -> input JSON, g_cutoff 6, n_mesh 48), work/submissions.tsv (label->req).
- Hypothesis post 20261002T035540.088Z_ctrl-a_hypothesis_0022 (family coord-w3).
- Submitted A1: 32 one-coordinate probes (8 spatial stars x T1 x {a,b} x +-0.04). Pending.
- Next: submit A2 (T2 x S1,S2,S3,S6 at +-0.04, plus S1T1 a=+0.05, +0.02 calibration; files ready in
  work/inputs/A2) once slots free; then fit per-coordinate quadratics, joint search in uphill subspace.
- 04:11 wakeup 2: 1/32 done (S1T1 a-0.04: R 0.931 PASS, consistent w/ doc46). Broker slow (~12 min/first). Wrote work/collect.py. A2 not yet submitted (31 in flight).

## 04:32 wakeup 3: A1 results (32/32 PASS at s21; R_gap, +-0.04)
amp a+/a-: S1 1.0188/0.9312  S2 1.0185/0.9406  S3 .981/.990  S4a .982/.965  S4b .981/.965
           S5 .954/.979  S6 .950/.969  S8 .937/.961
phase b+/b-: S1 .977/.981 S2 .977/.972 S3 .959/.959 S4a .955/.897 S4b .894/.951 S5 .901/.901 S6 .845/.845 S8 .807/.808
- Phase: concave, ~symmetric, worse for higher stars (S8 -19%): phase-only around w3 is downhill on every T1 star.
- Amplitude uphill only on S1,S2 (the odd-lattice harmonics w3 lacks). Per-coord quadratic:
  S1 l=1.10 q=-15.6 -> vertex a~0.035, +1.9%;  S2 l=0.97 q=-12.9 -> vertex ~0.038, +1.8%.
  Parent-own stars (S3,S6,S8) downhill both ways.
- PES entanglement gap shrinks with deformation (11 -> 5) but all PASS.
- Submitted B1 (25): S1T1xS2T1 amplitude 2D (7 pts) + A2 (T2 probes x S1,S2,S3,S6, S1T1 a .05/.02 calib).

## 04:59 wakeup 4: B1 results
- S1T1 amp alone: a .02 1.0108, .035 1.0170, .04 1.0188, .05 1.0223 -> MONOTONE, the A1 quadratic vertex (0.035)
  was wrong (response asymmetric: a- side falls much faster). Doc 46 g_cut4 a+.05 = 1.0185 vs my g_cut6 1.0223:
  ~0.4% box sensitivity at a=.05 -> keep g_cutoff 6.
- S1+S2 T1 amp plane (s21 / r46): (.02,.02) 1.0201/1.0215, (.03,.015) 1.0219/1.0238, (.015,.03) 1.0216/1.0244,
  (.03,.03) 1.0268/1.0314, (.04,.04) 1.0316/1.0408 [req ef31], (.05,0) 1.0223/1.0262. r56 pending for all 6.
  r46 > s21 so far (good sign for finite size).
- T2 x {S1,S2,S3,S6} amp & phase: all downhill (S6T2 phase -52%!). T2 dead around w3.
- Submitted C1 (17): S1 axis .07-.15, S2 axis .05-.15, diagonal .05-.15, off-diag ratios 2:1.
- Budget 74/500.

## 05:26 wakeup 5: C1 results (s21 / r46; r56 pending everywhere, even parent's r56)
- S1 axis: .05 1.022/1.026, .07 1.028/1.035, .10 1.033/1.048, .15 1.032/1.063
- S2 axis: .05 1.021/1.029, .07 1.023/1.040, .10 1.019/-, .15 0.992/-
- diag: .04 1.032/1.041, .05 1.034/1.050, .06 1.034/1.058, .08 1.027/1.071, .10 1.009, .12 .979, .15 .912
- off: (.08,.04) 1.0367/1.056 [best s21], (.10,.05) 1.034/1.065, (.04,.08) 1.029/1.061, (.05,.10) 1.021/1.072
- s21 peaks ~1.037 near (.08,.04); r46 keeps rising with |alpha| -> strong cluster dependence. 5x6 decides.
- M2_k rises with alpha (3.63 -> 3.83 at (.08,.08), +5.6%) -> amplitude winners need matched-density control.
- Submitted D1 (18, w3): third-direction probes at base (.06,.06): S3/S4/S5/S6/S8 T1 amp +-.03, S1/S2 T2 amp +-.03,
  S1/S2 T1 phase +-.02.  W2A (18, w2): coord map, hypothesis post 20261002T052739.956Z_ctrl-a_hypothesis_0f52.
- Budget 110/500.

## 05:59 wakeup 6: D1 + W2A results. r56 STILL pending for all (parents' r56 too) — broker bottleneck.
D1 (w3, base (S1,S2)T1 = (.06,.06): s21 1.0343 / r46 1.0575), one extra coordinate:
  a- side (-.03) s21/r46: S3 1.042/1.064, S4 1.052/1.061, S5 1.0575/1.0774 (M2k DOWN to 3.699), S6 1.033/1.073,
  S8 1.029/1.076, S1T2 1.045/1.051, S2T2 1.056/1.046.  a+ side all downhill. Phase S1/S2 +-.02 ~neutral.
  -> odd-lattice outer stars S4,S5 want negative amp opposite to S1,S2. T2 helps s21 but hurts r46 (finite-size flag).
W2A (w2, +-.04): uphill S1 a- 1.0155, S3 a+ 1.0152, S4 a+ 1.008, S8 a- 1.001; rest downhill; phase downhill.
  M2k barely moves (2.500-2.504) -> w2 gains would be close to beyond-M2.
Submitted E1 (15 w3 joint steps: combos of S3..S8 a-, T2, S1/S2 re-balance with S5 -.03, 1.5x scaled step)
and W2B (11 w2: S1- x S3+ plane, + S4, S8).  Budget ~136/500.

## 06:32 wakeup 7: E1 + W2B results; r56 still stalled (posted request 20261002T063259.468Z_ctrl-a_request_07fc)
w3 (s21/r46): e_n S1 .10,S2 .06,S5 -.03 = 1.0659/1.0874 [best s21]; e_k (.08,.06,S5-.03) 1.0628/1.0829;
  e_l (.06,.08,S5-.03) 1.0585/1.0872; e_m (.08,.04,S5-.03) 1.0598/1.0737; e_h base+S5 -.05 1.0524/1.0929 [best r46];
  e_d base+S5-.03,S6/S8 -.015 1.0366/1.0871. Strongly NON-additive: all-five (e_e) 0.983, 1.5x (e_o) 0.856,
  S5+S4 (e_a) 1.046 < S5 alone 1.0575, S5 -.06+S4 (e_i) 1.0015.
w2: (S1,S3) (-.10,0) 1.0258/1.0803; (-.08,.04) 1.0215/1.0961; (-.04,.04) 1.021/1.079; S3 alone .07 1.012.
  S1-,S3+,S4+ 1.0195; M2k <= 2.517 (+0.7%) — w2 gains ~ not M2.
Pattern on both parents: r46 R > s21 R (like the pilot). r56 is the decider.
Submitted F1 (9, w3 refine around e_n) + W2C (13, w2 third-direction probes at (-.08,.04) + S1 axis -.12/-.15).
Budget ~158/500. Plan: hold further big batches until r56 numbers exist.

## 07:14 wakeup 8: human note — r56 was waiting for a GPU (queue full), nothing broken.
F1 (w3, s21/r46): f9 (.12,.08,S5 -.04) 1.0710/1.1055 [best r46]; f3 (.10,.06,-.04) 1.0697/1.0953; f7 (+S2T2 -.02)
  1.0868/1.0841 [best s21; T2 again helps s21 not r46]; f1 (.12,.06,-.03) 1.067/1.091; f2 (.10,.08) 1.064/1.095.
W2C (w2): S1 axis -.12 1.0263/1.094, -.15 1.0242/1.1008; (-.12,S3 .03) 1.020/1.101; base(-.08,.04)+S4 +.03
  1.0235/1.1033, +S2 +.03 1.0233/1.0978; other third directions <= base.
Posted phase-only result w/ coverage. Submitted G1 (6 w3 ray extensions to 1.6x of (.10,.06,-.03), +T2 variants)
and W2D (3 w2: S1 -.12/-.15 + S4/S2). Budget 167/500. Waiting for r56.

## 07:56 wakeup 9: still no r56 anywhere.
G1 (w3, s21/r46/M2k): g1 1.071/1.114/3.94, g2 (1.6x) 1.068/1.120/4.03, g3 (f9+S2T2 -.02) 1.1005/1.104/3.85,
  g4 (g1+S2T2 -.02) 1.1043/1.1131/3.93 [best min so far], g5 1.075/1.114, g6 1.070/1.107.
W2D: h1 (S1 -.12,S4 .03) 1.023/1.100; h2 (+S2 .03) 1.024/1.1015; h3 (-.15,S4 .04) 1.014.
Mechanism note (my arithmetic, diagnostic only): w3 g4 M2k +8.3% vs gap +10%; R_beyondM2 ratio vs parent ~1.02
  at s21 -> w3 winners mostly track M2^(k); needs matched-density static control. w2 S1- family: M2k +0.2%,
  r46 +10% -> the cleaner beyond-M2 lead (but s21 only +2.4%).
Holding submissions (167/500) until r56 lands — no point refining on s21/r46 alone given the pilot's history.
- 08:47 wakeup 10: parents' r56 done (w3 4.5515e-4, w2 3.2164e-4); mine still queued.
- 09:08 wakeup 11: still 0 own r56. collect.py parallelised.

## 09:41 wakeup 12: r56 FLOWING. First robust_positive.
- w3 g4 req_20fc: s21 1.1043, r46 1.1131, r56 1.0852, conv46 1.1101, all PASS, C=1 -> broker claim robust_positive.
  g3 3ced r56 1.0852 conv 1.1015; g5 a173 r56 1.0808 conv 1.1116; f7 eaea r56 1.0757 conv 1.0824;
  f9 fbfc r56 1.0755; g1 1ece r56 1.0724.
- w2: S1 -.10 (fe03) r56 1.0412; S1 -.12 (a91e) r56 1.0457 (r46 1.094, s21 1.026). M2k ~flat -> beyond-M2 lead.
- M2 caveat: g4 r56 gain 1.085 ~= M2k ratio 1.083. Posted claim 20261002T094147.495Z_ctrl-a_claim_85ee and
  control request 20261002T094148.284Z_ctrl-a_request_98d8 (asked which static density: BZ-avg vs M2-matched).
- Next: wait for remaining ~45 r56 results; fit what drives r56 (vs s21/r46) -> target strong (r56>=1.10) on w3,
  and r56>=1.05 on w2 (S1- with S3+/S4+/S2+ partners).

## 10:13 wakeup 13: w2 robust_positive x2 (5fcc: S1 -.08,S3 .04,S4 .03 r56 1.0522 conv 1.1033; 7a7c: S1 -.15 r56 1.0504)
 M2k +0.2-0.3%. Posted w2 claim. w3 r56 table: g3/g4 1.0852 > g5 1.0808 > f3/f7/f9 ~1.0755 > g1 1.0724 > g6 1.0713
 > e_n 1.0705 = f1 > g2 (1.6x) 1.0645 -> r56 peaks around g3/g4 scale; T2(S2)<0 and S5 more negative raise r56.
 w2 r56: S1 -.07 1.033, -.10 1.041, -.12 1.046, -.15 1.050; (-.08,S3 .04) 1.046; +S4 .03 1.052; (-.12,S3 .03) 1.050.
 Stage-C hypothesis 20261002T101511.316Z_ctrl-a_hypothesis_3bef. Submitted H1 (14 w3) + W2E (12 w2). ~193/500.
 Lesson: gen.py args must be valid JSON (0.12 not .12) -> use work/batch_*.py scripts now.

## 10:56 wakeup 14
- H1 (w3) s21/r46: all ~1.08-1.108 / 1.08-1.124. h12 (S1 .14,S2 .10,S5 -.05,S2T2 -.03) 1.1083/1.1196; h04 (S5 -.06)
  1.0995/1.1240; h03 (S5 -.05) 1.1042/1.1139. h13 (S2T2 -.06) worse 1.080. r56 pending.
- W2E (w2): ALL s21 < 1.02 (best k04 S1 -.18 1.0185, k11 1.0178) -> none promoted. w2 is s21-gated: s21 tops out
  ~1.026 (S1 -.12) and every partner/scale-up lowers s21 while r46 rises. w2 r56 frontier (1.052) is effectively
  capped by the 1.02 confirm21 threshold. Deprioritise w2 refinement.
- Older r56 (lower amplitude): D1 S5- 1.0646, S4- 1.0549, S3- 1.0531; E1 e_h 1.0709, e_n 1.0705, e_l 1.0686, e_k 1.0685.
- No human reply on control request yet.
- 11:38 wakeup 15: H1 r56 all pending; no new posts. Holding.

## 12:24 wakeup 16: H1 all 14 robust_positive (r56 1.083-1.096). Best: h04 (S5 -.06) s21 1.0995 r46 1.1240 r56 1.0958
 conv 1.1198 [0.4% short of strong]; h05 (S5 -.05,S2T2 -.04) r56 1.0955; h12 r56 1.0926; h14 1.0924; h03 1.0913.
 r56 increments vs g3 (1.0852): S5 -.01 +0.6%, -.02 +1.06%; S2T2 -.04 +0.3%, -.06 -0.2%; S3 -.02 +0.4%;
 S4 -.015 +0.4%; S6/S8 -.01 +0.2%; S1T2 -.02 -0.2%; S1/S2 rebalance ~0. ~additive (h05).
 Submitted I1 (12): S5 -.07..-.10, S2T2 -.035, + S3/S4/S6/S8 combos. Target r56 >= 1.10 (strong). ~204/500.
- 13:16 wakeup 17: I1 screens done, all at r56 queue. s21/r46: i09 (S5 -.10) 1.039/1.1535 [M2k 3.744, lower];
  i10 1.114/1.142; i11 (S3 -.03) 1.116/1.126; i04 1.115/1.124; i07 1.085/1.140. s21 falls with very negative S5,
  r46 rises, M2k falls (3.74-3.81) -> the large-S5 points are LESS M2-tracking. Waiting r56.

## 14:02 wakeup 18: STRONG x8 on w3 (I1). i03 req_3ce9 (S1 .12,S2 .08,S5 -.07,S2T2 -.035): s21 1.1067 r46 1.1331
 r56 1.1046 conv 1.1272, M2 ratio 1.045. i07 req_3649 (+S3 -.02,S4 -.015): r56 1.1035, M2 ratio 1.0345 (least
 M2-tracking). i09 (S5 -.10) r56 1.0906 overshoot. Posted claim 20261002T140256.522Z_ctrl-a_claim_37af + correction
 note (56 robust+ not 31 — always count before quoting!).
 Tally over 148 w3 requests: strong 8, robust 48, suggestive 24.
 Submitted J1 (10): ridge probe + lower-M2 variants (S4 -.03, smaller S1/S2). ~214/500.
- 14:55 wakeup 19: J1 at r56 (s21 1.03-1.115, r46 1.11-1.149; lower-M2 variants j04-j06 M2k 3.66-3.68 have r46
  1.11-1.13). Posted w2 coverage result (57 req, 4 robust, 7 suggestive, all PASS). w2 closed.

## 15:41 wakeup 20: J1 r56 plateau ~1.106 (j08 S2T2 -.045, j09 S1 .13/S2 .09, j10) -> strong family saturated at r56.
 Lower-M2 variants: j04 r56 1.088 (M2 ratio 1.015), j05 1.085 (1.014), j06 1.0785 (1.008; s21 1.030, r46 1.114, conv 1.110).
 M2-matched construction (work/m2match.py, local m2_k == broker): exact M2^(k)=M2* unreachable in this shape (M2 convex;
 still +0.2% at 30% amplitude).
 Controls (work/ctrl_density.py): BZ-averaged per-k envelope density -> static W_G. M2(rho_bar) ~ M2* (3.616-3.630) !
 i07/g4 truncations go slightly negative (w3 nearly touches 0) -> skipped. Submitted --control family ctrl-density:
 i03 (12 shells) req_c9f2, j06 req_82ea. Note post 20261002T154348.551Z_ctrl-a_note_d450.
 Control (b) (static M2 = M2^(k)) inadmissible by rescaling w3 (negative) — left to human.
 Budget ~216/500. Next: control results; then coverage post for coord-w3; maybe a final new family (phase-on-top
 of strong point, chiral S4a/S4b, T3) for coverage.

## 16:15 wakeup 21: controls: static rho_bar(i03) s21 0.9916, rho_bar(j06) 0.9954 vs k-dep 1.1067/1.0300 -> average
 density doesn't explain gain. Posted result 20261002T161522.395Z_ctrl-a_result_7b9e. Posted w3 coverage
 20261002T161622.193Z_ctrl-a_result_e69c (158 req; 12 strong, 54 robust, 24 suggestive; best min 1.1063 j08 req_be9e).
 Submitted X1 (16, family ext-w3): phase on top of j08, T3, S4a/S4b. Skipped C2-only stars (symcluster validity unknown).
- 16:58 wakeup 22: X1 screens done (base j08 s21 1.1149 / r46 1.1304): phase +-.02 on S1T1/S2T1/S1T2 ~neutral
  (s21 1.110-1.114, r46 1.129-1.131); S5T1 phase: s21 -2.8% but r46 +0.6% (1.1365); S1T3 -.03 s21 1.1189 (+0.4);
  S4a/S4b exactly mirror-symmetric (a- = b-: 1.0973/1.0971). All at r56.

## 17:49 wakeup 23: X1 r56 (base j08 1.1063): S1T3 -.03 -> 1.1092 [NEW BEST min 1.1092: s21 1.1189 r46 1.1274 conv 1.1199];
 S2T3 -.03 1.1071; T3 + signs worse (1.094/1.101). Phase on top: r56 1.104-1.105 (S1,S2,S1T2), S5 phase 1.0993 ->
 phase neutral-to-negative even jointly with amplitude. S4a/b -.02 1.105 (mirror-symmetric).
 Submitted X2 (8): S1T3 -.05/-.07, S2T3 combos, S5T3 +-, +S4. ~240/500.

## 18:40 wakeup 24: X2: T3 saturates. y06 (S1T3 -.03, S5T3 +.02) r56 1.1103 but s21 1.1044; y07 (+S4 -.02) r56 1.1086;
 S1T3 -.05 1.1071, -.07 1.1021; S2T3 combos <= 1.105. Best min-over-clusters still x_aS1T3_m 1.1092
 (s21 1.1189 r46 1.1274 r56 1.1092 conv 1.1199). r56 ceiling ~1.11 in this family.
 Submitted SB1 Sobol n=32 (8-D amp box +-0.12, seed 20261002; points in work/sobol_points.json) to test other basins.

## 19:28 wakeup 25: Sobol SB1 (32, 8-D +-0.12): 1/32 above 1 (sb00 req_408c: S1 .116, S2 .098, S5 +.065, S4 -.115,
 S6 .084 ... s21 1.030, r56 1.043, in the S1+,S2+ quadrant = known ridge). 21 PASS below 1 (0.42-0.96);
 10 FAIL (ground manifold not clean, splitting/Delta up to 28; R 0.01-0.56) -> no large-gap other phases.
 Single basin in this box. Waiting sb00 ladder, then post result+coverage.
 Idea next: diagonal-quadratic surrogate on the ~70 ridge points with r56 to propose a few r56-optimal points.
 Surrogate (work/fit.py): linear + quadratic(5 main) + diag(others) on 99 r56 points, fit rms .0048, 5-fold cv .0064.
 Proposes moving ALL coords outward (S5 more -, S2T2 more -, S3/S4/S6/S8 small -, S2T3 +): predicted r56 1.113-1.141
 at trust radius .005-.03 — risky given e_e non-additivity; submitted Q1 (5 steps) to test. ~277/500.

## 20:21 wakeup 26: Q1 surrogate: q05 r56 1.1138 (best r56) r46 1.154 conv 1.145 but s21 1.0907; q10 r56 1.110 s21 1.06;
 q15/q20/q30 s21 1.01/0.93/0.69(FAIL). Spread grows with size; best min-over-clusters stays req_c4a4 1.1092.
 sb00 ladder: r46 1.066 r56 1.043. Posted Sobol result 20261002T202131.616Z_ctrl-a_result_43ab and ext-w3 result
 20261002T202147.258Z_ctrl-a_result_faab (both with coverage).
 Reopened w2 briefly: W2F 6 (T3 x S1/S3/S4 +-.03 on S1 -.12, S4 .03) — T3 lifted s21 on w3, w2 is s21-gated. ~283/500.
 Plan: after W2F, post final summary; keep loop alive slowly for the human's control-(b) answer, then swarm done.
- 21:03 wakeup 27: W2F: S1T3 -.03 s21 1.0275 (best w2 s21; base h1 1.0229) r46 1.092; S4T3 +.03 s21 1.0232 r46 1.086; rest <1.02. r56 pending. No human reply on control (b).

## 21:54 wakeup 28: FINAL. W2F r56: S1T3 1.0458, S4T3 1.0434 (< 1.0522) -> w2 closed (addendum note posted).
 Final summary 20261002T215432.791Z_ctrl-a_result_f0ee + count correction (219 w3 req: 33 strong, 59 robust, 25 sugg.).
 Best: req_c4a4 min 1.1092. Calling swarm done. 283/500 charged.
