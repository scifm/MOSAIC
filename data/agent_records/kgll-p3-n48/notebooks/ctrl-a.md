# ctrl-a notebook

Started 2026-10-14T10:26:46+00:00.

## 2026-10-14 ~11:15 — wakeup 1: setup + coordinate scan launched
- Read brief, theory §6.4, pilot 024 (doc 40), doc 46. Parent w1c: s21 Δ = 2.2586e-4, r56 Δ = 2.5901e-4 (PASS).
- Tools: work/gen.py (C6 orbits in solver basis; build(terms) -> input with deformation block),
  work/mk_scan.py. Stars: S1,S3,S4,S7a,S7b,S9,... (|G|²=7,13,19,21 split into two chiral orbits); T1,T3,T4 (|R|²=1,3,4).
- swarm check: m2k_max_ratio = M2^(k)/M2 (decreases with |alpha|: 0.95 at alpha=±0.6 S1T1). Not binding.
- Posted hypothesis coord-scan (20261014T111226.662Z_ctrl-a_hypothesis_f09f): 6 orbits x 3 T x {alpha ±0.10, beta ±0.05} = 72.
- Submitted inputs/scan1 (32 reqs: S1,S3,S4[T1,T3]). Next: submit scan2 (32) + scan3 (8) as slots free; read signs.

## 11:25 — wakeup 2: scan1 results (s21 R_gap; a=alpha±0.10, b=beta±0.05)
| block | a+ | a- | b+ | b- |
|---|---|---|---|---|
| S1T1 | 0.902 | 0.992 | 0.947 | 0.945 |
| S1T3 | 1.015 | 0.970 | 0.996 | 0.996 |
| S1T4 | 1.018 (f0ee) | 1.007 | 1.008 | 1.019 (4b22) |
| S3T1 | .397F | .711F | .588F | .586F |
| S3T3 | .571 | .470 | .517 | .519 |
| S3T4 | .752F | .601F | .693F | .664F |
| S4T1 | .138F | .551F | .367F | .364F |
| S4T3 | .125F | .000F | .041F | .045F |
(F = manifold splitting/Δ > 0.1.)
- Lesson: S3/S4 at 0.1 are catastrophic (outer stars hugely stiff on this sharp parent; beta response even in sign).
  S1T4 positive for BOTH signs of alpha and beta -> positive curvature, go larger.
- Dropped scan2/scan3 (0.1 steps on S4T4, S7, S9 would be same catastrophe). Replaced by r2 (32):
  S1T4 alpha ±0.2,±0.3, beta ±0.1,±0.15; S1T3 alpha +0.2,+0.3; S1T1 alpha -0.05,+0.03;
  S3,S4,S7a,S7b,S9 x T3,T4 x alpha ±0.02. ids in work/inputs/r2/ids.tsv.

## 11:38 — wakeup 3: r2 results (s21 R_gap)
- S1 larger steps all bad: S1T4 a±0.2 0.90/0.85, a±0.3 FAIL ~0.5; b±0.1 0.89/0.88, b±0.15 FAIL; S1T3 a+0.2 0.84, +0.3 FAIL.
  S1T1 a-0.05 1.008, a+0.03 0.983. => S1 optimum small (|a|<~0.1), ≤ +2%.
- Outer stars at alpha ±0.02:
  T3 (odd, + sign wins): S3 1.012/0.988, S4 1.013/0.986, S7 1.014/0.979, S9 1.012/0.975
  T4 (even, both +): S3 1.008/1.007, S4 1.013/1.011, S7 1.027/1.023, S9 1.031/1.019
- S7a and S7b give IDENTICAL R on Nk=21 (mirror partners) -> use S7a only from now (same for S13/S19/S21 halves).
- Auto-promoted to r46: S7a/S7bT4 ±0.02, S9T4 +0.02 (s21c agreed).
- r3 submitted (32): S9T4 +.04,+.06,-.04; S7aT4 ±.04; S4T4 ±.04; S3T4 +.04; T3 +.04 on S3,S4,S7a,S9;
  S12,S13a,S16,S19a,S21a x T3,T4 x ±0.02. Budget ~95/500.
- Caution: T4 even-positive everywhere could be an Nk=21 sampling artifact; r46/r56 will tell.

## 11:51 — wakeup 4: r3 results; first r46 numbers
- r46 (4x6): S7T4 a+0.02 = 1.0431 PASS, a-0.02 = 1.0192 PASS; S9T4 a+0.02 = 1.0506 PASS. r56 pending. (r2 ids)
- Outer T4 at ±0.02, s21: S12 1.027/1.015, S13a 1.026/1.015, S16 1.023/1.013, S19a 1.019/1.012, S21a 1.016/1.011 (pattern: + better than -, both >1).
- Outer T3 ±0.02: S12 1.006/0.971, S13 1.004/0.970, S16 0.999/0.968, S19 0.992/0.966, S21 0.988/0.966.
- Larger steps lose fast: S9T4 +.04 0.954, +.06 FAIL 0.62, -.04 0.910; S7T4 ±.04 0.971/0.949; S9T3 +.04 0.834; S7T3 +.04 0.913;
  S4T4 ±.04 1.009/0.990; S3T4 +.04 1.023 (promoted); S3T3 +.04 1.015.
- Response is NON-quadratic: both ±0.02 > 1 but ±0.04 < 1 -> kink-like near alpha=0 (|alpha| term), optimum ~0.01-0.03. 
  Suspect level structure (E3/E4 multiplets) rather than smooth physics; watch r56 sign.
- r4 submitted (32): fine steps S9T4/S7T4, S12/S13 T4 +.03, beta ±.01 on T4 (S4,S7,S9,S12), T1 ±.02 (S4,S7,S9,S12), 6 combos. Budget ~127/500.

## 12:05 — wakeup 5: 5x6 results arrive — null
- r56: S7T4 a+.02 1.0014 (r46 1.043), a-.02 0.983; S9T4 a+.02 1.0000 (r46 1.051). 5x6 kills the 4x6 gain (pilot-024 pattern).
  Pending r56: S12/S13a/S16 T4 a+.02 (r46 1.057/1.058/1.059), S3T4 a+.04 (r46 1.046).
- r4 s21: fine steps S9T4: +.01 1.010, +.015 1.020, +.02 1.031, +.025 1.018, +.03 1.000, -.01 1.008. S7T4 +.01 1.007, +.03 1.010, -.01 1.006.
  T1 outer all < 1 (0.92-0.995). beta T4 ±.01: S9 1.021/1.030, S7 1.025/1.024, S12 1.017/1.026, S4 1.012/1.011 (several promoted).
  combos: S7+S9 .01 1.030 (promoted), S9+S12 .01 1.030 (promoted), 4-star .01 0.974, S7+S9 .02 0.964.
- Promotion needs s21 >= 1.02, so anything must clear that first; no direct r56 path.
- r5 (36) submitted: beta T4 on more orbits/larger, beta T3, beta T1, alpha/beta mixes, combos. Budget ~163.
- Posted interim note.

## 12:20 — wakeup 6: product-T4 dead at 5x6; start joint-orbit family
- r56 for all alpha-T4 products: S7 1.0014, S9 1.0000, S12 0.9974, S13 0.9965, S16 0.9934, S3(+.04) 0.9958 (r46 were 1.043-1.059).
  => product-star alpha x T4 is a 5x6 null. beta-T4 r56 pending (S7 ±.01, S9 ±.01, S12 -.01; combos S7+S9, S9+S12).
- r5 partial: beta ±.02 on T4 bad (S12 0.90/0.88); beta T1 bad (0.93-0.95); S12T3 beta ±.01 0.989.
- Cluster sampling (work/fmom.py, f21.py): F_T4 aliases on 4x6 (mean-sq 1.333 vs 1); F_T3 is skewed on 21-site (min -0.41).
- New: joint (G,R) orbits via pair-stars (gen.py: pairs/joint_orbits/build_joint). Hypothesis 20261014T122230.725Z_ctrl-a_hypothesis_893d.
  j1 submitted (36): S1/S9/S12 x T1/T3/T4 x 2 inequivalent orbits x ±amp (0.1 S1, 0.03 outer).

## 12:39 — wakeup 7: JOINT ORBITS give large, odd (analytic) responses
- j1 s21: S12T1 j0 +.03 1.204 (r46 1.235!), j0 -.03 0.711; S12T1 j60 -.03 1.118; S9T1 j90 -.03 1.242, j30 +.03 1.081;
  S1T1 j90 -.1 1.195, j30 +.1 1.051; S1T4 j90 +.1 1.052; S1T3 j0 +.1 1.033; S9T3 j0 +.03 1.035. T3/T4 orbits weaker; T1 strongest.
  Product star = equal sum of 3 orbits -> their big linear responses cancel; that is why products looked flat.
- Product beta-T4 r56: all 0.988-0.993; combos 0.999-1.001; S9T4 a+.015 r56 1.0031. Product family = 5x6 null, closing it.
- r5 s21 rest: beta T3 ~1.000, beta T1 0.93-0.95, beta ±.02 on T4 0.88-0.97.
- j2 submitted (42): step extensions on the T1 winners, beta (phase) versions, T1 joint orbits of S3,S4,S16,S7a,S13a.

## 12:57 — wakeup 8: JOINT ORBITS CONFIRMED ON 5x6
- s21/r46/r56: S9T1 j90 a-.03 1.242/1.262/1.241; S12T1 j0 a+.03 1.204/1.235/1.208; S1T1 j90 a-.1 1.195/1.197/1.184;
  S12T1 j60 a-.03 1.118/1.163/1.141; S9T1 j30 a+.03 1.081/1.114/1.096. All PASS, C=1. Now in conv46.
- j2: phase-only joint orbits negative (0.96-0.99). Amplitude extensions: S1 j90 -.15 1.281, -.2 1.359 (s21); S9 j90 -.045 1.312,
  -.06 1.316 (saturating); S12 j0 +.045 s21 1.176 r46 1.356, +.06 FAIL (splitting). New orbits: S13a j103.9 -.03 1.206,
  j163.9 +.03 1.166; S16 j90 -.03 1.219; S4 j90 -.03 1.176; S7a j109 -.03 1.175, j169 +.03 1.179; S3 j0 +.03 1.122.
  Pattern: for each spatial orbit, one joint orbit (sign) gives +12..+24 % at 0.03.
- Rule mapping (ANG/SGN in work/mk_j3.py): S1 j90 -, S3 j0 +, S4 j90 -, S7a j169 +, S9 j90 -, S12 j0 +, S13a j104 -, S16 j90 -.
- j3 submitted (24): S1 j90 -0.25/-0.3/-0.4; 9 combos; S19a/S21a T1 orbits.
- Matched-density controls (work/mk_ctrl.py) submitted as --control s21,r46,r56 (inputs/ctrl/ids.txt). Density differs <=1.4%.
- Posted note 20261014T130012.352Z_ctrl-a_note_cfc6 and request 20261014T130013.162Z_ctrl-a_request_f63a.
- Budget ~263+3 ctrl.

## 13:16 — wakeup 9: STRONG claim; controls = 1.000; optimizing combos
- conv46 done. Broker claim=strong: S1T1 j90 a-.2 (req_efe8) s21 1.359 r46 1.399 r56 1.362 conv46 1.399;
  S9T1 j90 a-.03 (req_612b) 1.242/1.262/1.241/1.262; S12T1 j0 a+.03 (req_dcaf) 1.204/1.235/1.208/1.235;
  S13a j104 -.03 1.206/1.250/1.222/1.250; S12 j0 +.045 1.176/1.356/1.291/1.357; S1 j30 +.1 1.05/1.06/1.053 (robust-pos level).
  Also S9T3 j0 +.03: r56 1.058, S1T4 j90 +.1 r56 1.008.
- Controls (matched density): S12 ctrl 1.0000 all clusters, S1(-.1) ctrl 0.9990 all, S9 ctrl 1.0000 (r56 pending). => beyond M2.
  Control for efe8 submitted: req_aced (s21,r46,r56,conv46).
- Posted claim 20261014T131710.062Z_ctrl-a_claim_84d6.
- j3 s21: S1 j90 -.25 1.407, -.3 1.436, -.4 1.464 (saturating); S1+S9+S12 1.635; all.015+S1.05 1.620; S9+S12 1.498;
  S1+S12 1.441; S1+S9 1.361; S1.15+S9.045 1.364; S1+S4 1.342; S9+S13 1.263; S9+S16 1.248.
  S19a: j173 +.03 1.151, j113 -.03 1.119; S21a: j101 -.03 1.156, j161 +.03 1.104.
- j4 submitted (13): contrast directions, scaled S1S9S12 (x1.5,x2), 14-star vector incl chiral partners (x.5,1,1.5),
  S1 -0.5/-0.6, S1.3+S9+S12, S1.2+S9.045+S12.045, all.03+S1.1. Budget ~286.

## 13:35 — wakeup 10: combos explode on 4x6; s21 is the bottleneck
- Controls final: all 4 controls R = 0.996-1.000 on every cluster (incl. ctrl for efe8 at conv46 0.996). Beyond M2 settled.
- c_S1.1_S9.03_S12.03: s21 1.635 r46 1.862 r56 1.723 conv46 1.862 (min 1.635, converge done).
- c_all.015_S1.05: s21 1.620 r46 2.037 r56 1.875.  S9+S12: 1.498/1.597/1.513.
- j4 s21 (r46): contrast S1 .2 1.513 (1.580); contrast S12 1.402 (1.452); contrast S9 1.393 (1.416);
  S1S9S12 x1.5 1.723 (2.280), x2 1.658 (2.683); D_S1.2_S9.045_S12.045 1.7335 (2.393); D_S1.3 1.712 (2.311); S1 -0.5 1.467 (2.046);
  all14 x0.5 1.545 (2.262); all14 x1.0 FAIL(splitting 8.9), x1.5 FAIL; S1 -0.6 FAIL; all.03+S1.1 FAIL.
  -> s21 saturates ~1.73 while r46 keeps growing; manifold FAIL on s21 sets the amplitude ceiling.
- Contrast form (fav orbit a, other two -a/2) beats single orbit by +15-20 points.
- j5 submitted (23): contrast3 x.5..1.25, S1 contrast .3/.4, D + other stars, 6 random perturbations of D, D + T3/T4 orbit.
- Posted coord-scan coverage result (closed). Budget ~312.

## 13:54 — wakeup 11: T3 joint orbit added to D jumps s21 to 2.14
- j4 converged: B x1.5 (req_0f2b) s21 1.723 r46 2.280 r56 2.113 conv46 2.280 -> claim strong, min 1.7227 (current best confirmed).
  B x2 (req_85f5) 1.658/2.683/2.503/2.682 strong. D_S1.2_S9.045_S12.045 (req_d082) 1.7335/2.393/2.219/conv pending.
  C_all14 x0.5 1.545/2.262/2.105. S1 -0.5 1.467/2.046/1.885.
- j5 s21: D+S9T3j0.03 2.140 (req_6679)!!; D+S3.02 1.746; D+S4 1.691; D+S7ab 1.682; D+S1T4 1.582; perturbations P0-5 1.63-1.72;
  contrast3 x.5/.75/1 1.58/1.66/1.57, x1.25 FAIL; S1 contrast .3/.4 1.626/1.638; S9/S12 contrast .045 1.53/1.52.
  FAIL (splitting>0.1): D+S13ab, D+S16, D+S19ab, D+S21ab.
- s21 manifold splitting is the binding constraint; T3 orbit may relieve it (watch r46/r56 for 6679: T3 sampled oddly on 21-site).
- j6 submitted (23): D + S9T3 j0 scan, other T3 adds, B x1.5/x2 + T3, T3 orbit scans S3/S4/S16. Budget ~335.

## 14:12 — wakeup 12: T3 additions push s21 to 2.27
- j6 s21: D+S9T3j0 .015/.03/.045/.06 = 1.878/2.140/2.266/2.248; D+S9T3.03+S1T3j0.1 2.268; D+S9T3+S12T3j30 2.164;
  D+S3+S9T3 2.143; D+S12T3j30 2.119; D+S1T3j0.1 1.952; Bx1.5+S9T3 2.088; Bx2+S9T3 2.120; Dx0.75+S9T3 1.949.
  T3 single orbits: S4T3 j0 +.03 1.030, S16T3 j0 +.03 1.026, S3T3 j30 +.03 1.015; rest <1.
- D+S9T3j0.03 r46 2.657 (D alone 2.393) -> T3 helps on 4x6 too; r56 pending.
- r46 for j5: D+S7ab 2.597, D+S4 2.522, D+S3 2.482, S1contrast.4 2.153, contrast3 x1 2.437.
- j7 submitted (13): D + T3 set (S9T3 j0 .045 + S1T3 j0 .1) with variations/scales/contrast. Budget ~348.

## 14:34 — wakeup 13: confirmed min 2.164 (strong)
- Fully converged (conv46 done): D+S9T3j0.03+S12T3j30.03 (req_3450) s21 2.164 r46 2.679 r56 2.537 conv46 2.680 -> strong, best min.
  Bx2+S9T3j0.03 2.120/3.014/2.703/3.013; D+S3+S9T3 2.143/2.758/2.476/2.758.
- j7 s21 (r46): Bx2+T3 2.603 (3.134); Dx1.25+T3 2.564 (3.114); D+S3+T3 2.417 (2.769); D+T3 2.239 (2.490);
  FAIL: Dx1.5+T3(.06,.15) 2.76 (split .105), D+T3+S12T3j30, D+T3+S16T3j0, D+S9T3 contrast.
- Control for 3450 submitted: req_9d56 (density dev up to 0.12 abs, M2 9.94 vs 10.04).
- j8 (16): ray X = Bx2-like (S1 .2,S9 .06,S12 .06)+T3(S9T3 .045,S1T3 .1) scaled f 1.1-1.3, T3 scale, ratio tweaks, +S3/S4/S7ab. Budget ~364.
- Plan: after j8, ~1 more refinement round (~20), then coverage posts; keep ~40 reserve.

## 14:57 — wakeup 14: ray X scales cleanly; confirmed min 2.603
- Converged: Bx2+T3 (req_a22a) s21 2.603 r46 3.134 r56 2.806 conv46 3.134 -> best confirmed min 2.6027.
  Dx1.25+T3 2.564/3.114/2.869/3.114. D_S1contrast+S9T3 2.227 (STRONG). Control for 3450 (req_9d56): 0.996 all clusters.
- j8 s21: X f1.1/1.2/1.3 = 2.771/2.941/3.110 (r46 f1.2 3.677, f1.3 3.939); X+S3.02/.03 2.762/2.824; X+S7ab 2.890;
  X_S12.075 2.837; X_f1.1+S3 2.922; X+S12T3j30 2.379; t1.5 FAILs (T3 too big breaks s21 manifold).
- j9 (14): X f 1.45..2.5, T3 ratio at f1.6/2.0, Y = X(S12 .075)+S3+S7ab at f 1,1.3,1.6. Budget ~382.

## 16:29 — wakeup 15: ray X confirmed up to min 3.44; r56 manifold is the frontier
- Converged (all PASS, C=1): X f1.8 (req_ed91) s21 3.436 r46 4.716 r56 4.183 conv46 4.714 -> best min 3.4358 (r56 split/Δ 0.0993!);
  X f1.6 (73d8) 3.374/4.579/3.964; X f1.45 (c182) 3.322/4.320/3.740 (r56 split/Δ .083); X f1.3 3.110; f1.2 2.941; f1.1 2.771.
  X f1.3+S3.03 3.041; X f1.3+S7ab.02 2.773; X+S7ab.015 2.890; X_S12.075 2.837.
- FAIL on r56 manifold (split/Δ 0.11-0.15): X f2.0, f2.5, f1.6 t1.2, f2.0 t1.2. Y (X+S3+S7ab+S12.075) FAILs s21 at all f.
- Entanglement gap drops to ~2.1-2.3 at f>=1.45 (still PASS).
- Posted claim update 20261014T163134.236Z_ctrl-a_claim_5e1f. Control for ed91 submitted: req_8657.
- j10 (11): f 1.8-2.2 with T3 0.8-1.1, S12/S9 ratio at f1.8, small beta on S1 j90. Budget ~393.
- Remaining plan: read j10 -> maybe one last small round; then coverage post for joint-orbit, swarm done. Keep ~30 reserve.

## 16:52 — wakeup 16
- ed91 control (req_8657): 0.9877/0.9867/0.9862/0.9867 -> beyond M2 for the best candidate. Posted note.
- j10 s21: X f1.8 t1.1 3.833 (r46 4.673); f1.9 t1 3.474; f1.8+beta ±.02 on S1j90 3.425/3.433 (no help); S12/S9 ratio up hurts s21 (2.69/2.81);
  t0.9 variants ~3.01-3.04; f2.0 t0.8 2.585; f2.2 t0.8 FAIL. => s21 gain driven by T3 part; r56 manifold limits T3. r56 pending.

## 17:13 — wakeup 17: frontier mapped; ed91 still best (min 3.4358)
- j10 converged: f1.8 t0.9 3.013; f1.9 t0.9 3.020; f2.0 t0.9 3.038; f2.0 t0.8 2.585; f1.8 S12.075 2.694; f1.8 ±beta 3.425/3.433.
  r56 manifold FAIL: f1.8 t1.1 (0.111), f1.9 t1.0 (0.105). s21 rises with T3, r56 manifold caps T3*f.
- j11 (12): T3 composition at f1.8, f1.6-1.75 with t1.05-1.1, small extra T3 orbits, +S3. Budget ~409. Then coverage + done.

## 17:40 — wakeup 18: j11 s21 up to 3.89 (S3T3j30, S9T3 .055, S4T3, S16T3 adds); r56 manifold verdicts pending.

## 18:01 — wakeup 19: extra T3 always fails r56 manifold
- r56 FAIL (split/Δ 0.102-0.133): XT(.055,.1), XT(.06,.08), f1.75 t1.05, f1.7 t1.1, +S16T3, +S3T3j30, +S4T3.
- Pending r56: XT(.045,.12) s21 3.68, f1.6 t1.1 3.58, f1.7 t1.05 3.60, f1.8+S3 3.24.
- Counts: coord-scan 164 req (22 FAIL, 21 reached r56); joint-orbit 233 req incl 6 controls (36 FAIL, 145 reached r56, 121 conv46).
- Next: when those 4 finish, post joint-orbit coverage result and swarm done (budget 409/500 is enough; frontier mapped).

## 18:22 — wakeup 20: new best X(1.7,1.05) req_5418 min 3.598; coverage posted
- req_5418: s21 3.598 r46 4.634 r56 4.079 (split/Δ 0.0997) conv46 4.632, strong. XT(.045,.12) & f1.6 t1.1 FAIL r56 (0.106/0.100).
- Control for 5418 submitted: req_425a. Joint-orbit coverage result posted: 20261014T182255.876Z_ctrl-a_result_4c88.
- Next: when control lands, post note + swarm done; stop loop. Budget 409(+control)/500.

## 18:39 — wakeup 21: DONE
- Control for 5418 (req_425a): 0.9888/0.9880/0.9875/0.9879. Posted note. Posted swarm done (work/done.md). Loop stopped.
- Final: best min R_gap 3.598 (req_5418), strong, beyond M2. 413/500 charged.
