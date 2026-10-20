# ctrl-b notebook

Started 2026-10-13T18:09:02+00:00.

## 2026-10-13 18:15 — wakeup 1: setup + phase 1 launch
- Read brief, doc 40 (024 pilot: 4x6 +0.51% flipped to −0.92% at 5x6), doc 46 (Nk=21 w3: α[S1,T1]=+0.05 → +1.85%, −0.05 → −9.04%, β[S1,T1]=+0.05 → −4.42%, α[S4,T1]=+0.05 → −3.75%).
  Quadratic read of S1T1: vertex α≈+0.04, R≈+2% (one cluster).
- Parents s21: Δ(w3)=4.5713e-4, Δ(w2)=3.2271e-4.
- Tools: work/kgen.py (star enumeration in solver basis; build(parent, terms, path); diag() → M2k/S cond).
  Stars: S1,S3,S4,S7a/b,S9,S12,S13a/b,S16,S19a/b,S21a/b (12-shells split into C6 orbits); T1,T2,T3.
  60° rotation: G (m,n)->(m-n,m); R (r1,r2)->(-r2,r1+r2).
- Posted H1 (hypothesis 20261013T181235.064Z_ctrl-b_hypothesis_e681).
- Phase 1: 120 single-direction requests (α=±0.04, β=±0.03), family w3-single; inputs/p1b1..b4. Submitted b1 (32). Log: work/submitted.log.
- Next: submit b2..b4 as slots free; then fit linear+quadratic per direction (work/analyze_p1.py).

## 18:30 — wakeup 2
- Parent gaps now known: w3 r46 4.3823e-4, r56 4.5515e-4; w2 r46 3.0955e-4, r56 3.2164e-4.
- Batch 1 (32) done in <10 min (~20 s/eval). work/collect.py → results.json cache + table.
- T1 results (α=±0.04, β=±0.03): only S1T1 α+ (1.0190) and S3T1 α+ (1.0185) > 1. Everything else
  0.91–0.99: strong negative curvature in almost every direction (e.g. S12T1 β± both 0.913).
  Linear β terms exist on chiral S7a/S7b (MT-related pair: S7a β− ≈ S7b β+ ≈ 0.94).
  Reading: the static parent sits near a local max of R; k-dependence mostly costs gap.
- Submitted batch 2 (S13b..S21b T1, S1/S3 T2). b3, b4 next.

## 18:40 — wakeup 3
- Batch 2 done; b3 (T2: S4..S16, T3: S1,S3) submitted. 64 charged.
- work/analyze_p1.py fits c1, c2 per direction (R = 1 + c1 x + c2 x²). Only S1T1 α (c1 +1.10, c2 −15.6, x* +0.035, +1.9 %)
  and S3T1 α (c1 +0.97, c2 −12.8, x* +0.038, +1.9 %) have useful 1D optima; all others ≤ 0.3 %.
  Achiral stars: R(β) = R(−β) exactly (TR); chiral pairs (S7a/b, S13a/b, S19a/b, S21a/b) have linear β of opposite sign, but curvature 40–120 kills them.
  High stars cost heavily (c2 ~ −100 for β on |G|² ≥ 12).
- Prepared phase 2: 3×3 grid in (α[S1T1], α[S3T1]) ∈ {0.02,0.035,0.05}² + two 1D refinements (inputs/p2, 11). Submit with b4 next wakeup.

## 18:55 — wakeup 4
- Batch 3 (T2: S4..S16, T3: S1,S3): all concave, no direction > 0.05 % predicted gain. T2/T3 are dead for w3 at Nk=21.
  High-star β is brutal (S16T2 β ±0.03 → 0.667).
- Trimmed b4: dropped β on achiral S4,S9,S12,S16 × T3 (linear term is exactly zero by TR; moved to inputs/p1b4skip). Submitted 16 of b4.
- Submitted phase-2 grid (family w3-s1s3, 11 requests).
- Built joint (G,R)-orbit family: kgen.build_joint. 2-member stars {±G_i}, {±R_j}; class c: Σ_i O_{P_i} F_{Q_(i+c)%3}.
  Product O_S F_T = (1/3) Σ_c J_c (verified numerically). Relative G–R angles: c0 30°, c1 90°, c2 150° (mod 180).
  MT symmetry → c0 ≈ c2 expected for amplitude. sin·sin joint terms are NOT representable in the block (real cos-stars only).
  inputs/p3: S1T1, S3T1 × c ∈ {0,1,2} × a_c = ±0.03 (12). Submit next wakeup.
- NB: I briefly read src/ed/contract.py from $MOIRE_MAIN (the solver contract, code only); kgen now imports from the worktree src.

## 19:00 — wakeup 5: first ladder climbers
- Phase 1 complete (T3 all concave; 112 phase-1 evals). 123 charged.
- **Phase-2 grid (S1T1 α, S3T1 α): gains ADD (slightly superadditive), and hold on 4×6/5×6.**
  (0.05,0.05) req 20261013T184802.822Z_ctrl-b_req_60a4: s21 1.0341, s21c 1.0341, r46 1.0495, r56 1.0429, all PASS, C=1 → claim "suggestive".
  (0.05,0.035): s21 1.0330 r46 1.0425 r56 1.0389. Others climbing.  Corner of box is best → widened.
  Diagnostics at (0.05,0.05): M2_k/M2 = 1.0205 (gap gain 3.4 % > M2 gain 2.05 %); adm ratio 0.877.
  r46/r56 R exceed s21 R here — opposite to the 024 worry.
- Submitted p2b: (a1,a3) ∈ {0.05,0.08,0.11}² + (0.15,0.15), (0.2,0.2) [M2k max ratio up to 1.38]. Submitted p3 joint-orbit classes (12).
- Note: conv46 promotion needs min R ≥ 1.05 including s21 — need s21 ≥ 1.05.

## 19:13 — wakeup 6: joint classes are the real lever
- p2b: product family optimum ~ (0.05–0.08, 0.05): s21 peaks 1.0358 at (0.08,0.05); r46 up to 1.071 at (0.08,0.08) (s21 1.027).
  (0.11,0.11) 0.995, (0.15,0.15) 0.912, (0.2,0.2) 0.741 → product family maxes ≈ +3.5 % at s21.
- **p3 joint classes (a_c=±0.03):** S1T1 class c2 (G⊥R, 90°) + → s21 1.0622 (r46 1.0521); − → 0.896.
  S3T1 class c0 (G∥R, 0°) + → 1.0590 (r46 1.0530); − → 0.903. Other classes ≈ 0.97 both signs (pure curvature).
  1D quad reads: S1⊥ x*≈0.060 (+8 %), S3∥ x*≈0.061 (+8 %).
- CAUTION: my H2 draft initially mislabeled classes; kgen.class_angles gives physical angles: S1/S4/S9/S16 with T1: [150,30,90]; S3/S12 with T1: [0,60,120].
- Submitted p4 (15: grid S1⊥×S3∥ ∈ {.03,.05,.07}² + rays to .09) and p4b (16: S4,S9,S16 ⊥ & 30°; S12 ∥ & 60°). Posted H2 hypothesis_e154.
- 145 charged before these (→ ~176).

## 19:28 — wakeup 7: large gains along S1⊥ and S3∥
- The −0.03 side was misleading: along the gain classes R rises ~linearly to at least 0.09 (no turnover yet).
  S3∥ alone: 0.05 → s21 1.0995, 0.07 → 1.142, 0.09 → 1.1865 (r46 1.179). S1⊥ alone: 0.05 → 1.105, 0.09 → 1.197.
  Combined (0.07,0.07) req_7e42: s21 1.3018, s21c 1.3018, r46 1.2582 (r56 running). PES PASS (ent. gap ~7), split/Δ ~ 4e-4.
  M2k/M2 = 1.13 only, R_beyondM2 0.79 vs parent 0.69 → most of the gain is NOT the density law (diagnostic only).
- p3_S1T1_j2_ap (0.03): s21 1.0622 r46 1.0521 r56 1.0556 conv46 1.0520, all PASS → meets robust_positive thresholds.
- Other stars' classes (S4,S9,S12,S16 with T1, ±0.03): no gain class, all ≤ 0.99.
- Physics guess: ẑ×R for R ∈ T1 lies in S1 (|a| = |G1| with one flux/cell), so the S1⊥ class pairs e^{iG·r} with the LLL's intrinsic e^{i k×G} phase (GMP/magnetic-translation structure).
- Submitted p5 (31): grid {.07,.10,.14,.20}² + rays to 0.3 on each class alone; β (phase) on S1⊥ and S3∥ ±0.03; T2 gain-class candidates S1T2 c1 (∥), S3T2 c2 (⊥) ±0.03.
- Next: T3 analogues (S1T3 c2, S3T3 c0); find the turnover; then local optimizer; then w2 transfer; then request matched-density control.

## 19:45 — wakeup 8: ~+40 % on all clusters
- p5 grid: ridge where S1⊥ and S3∥ partly substitute; best min-over-clusters so far:
  req_3d10 (0.07,0.14): s21 1.412 r46 1.408 r56 1.392; req_50e2 (0, 0.20): s21 1.451 r46 1.411 r56 1.388.
  S3∥ 0.3 alone: s21 1.496 but r46 1.372 (turned over). (0.2,0.2): s21 1.007. (0.14,0.2): 1.23.
  (0.07,0.07) req_7e42 conv46 1.2577 done (all 4 clusters ≥1.25 → strong thresholds).
- Phase β on S1⊥/S3∥ ±0.03: 0.96–0.99 (no clean beyond-M2 route there). T2 classes S1∥/S3⊥: none.
- Posted interim result_ec2d and request_ca0e (matched-density control: who runs it, which density definition). Won't submit --control until answered.
- Submitted p6 (26): ridge points (0,.24),(0,.27),(.03,.17..23),(.05,.15..21); gradient probes ±0.03 around S3∥=0.2 for
  S1c0 (30° pair), S3c1 (60° pair), S4⊥, S12∥, S7a c0/c1/c2, S1T3⊥, S3T3∥.
- 207 charged before p6 (→233).

## 20:00 — wakeup 9
- collect.py was slow (many in-ladder requests); now caches anything with status done.
- Ridge (s21/r46/r56 where known): (0,.2) req_50e2 1.451/1.411/1.388 conv46 1.412 (done; strong thresholds met);
  (0,.24) 1.503/1.418/…; (0,.27) 1.511/1.404; (.03,.2) 1.465/1.417; (.05,.18) 1.443/1.414; (.07,.2) 1.417/1.385/1.375.
  S3∥ 0.16: r56 1.298 (dip vs r46 1.365) — r56 is the weak cluster at some amplitudes.
- Probes ±0.03 around S3∥=0.2: mostly flat/negative. Notable: S7a c1 −0.03 → r46 1.4665 (+5.5 %) but +0.03 → r46 1.345; s21 barely moves.
  Chiral term with cluster-dependent response — wait for r56 before trusting it. S7a c2 +0.03 → s21 1.460.
- Posted H3 (w2-joint, hypothesis_b419); submitted 13 w2 transfer points (inputs/w2a).
- 233 charged + 13.

## 20:18 — wakeup 10
- collect.py rewritten: one bulk `swarm status` call (2.5 s). Usage: collect.py [regex].
- **w2 transfer FAILS**: S1⊥ and S3∥ hurt w2 at every amplitude and sign (0.03 → 0.99; 0.2 → 0.53–0.86; −0.05 → 0.96–0.97).
  The w3 gain is parent-specific. (w2 density: −1/3 on |G|²=3, +1/3 on 9, −1/6 on 12; touches zero.)
- w3 best min-over-clusters (all PASS, conv46 done): (0,0.24) req? s21 1.503 r46 1.418 r56 1.487 conv46 1.418 → min 1.418;
  (0.03,0.20) 1.465/1.417/1.445/1.418. r56 is noisy along the ridge (0.16: 1.298, 0.20: 1.388, 0.24: 1.487).
  Probe S7a c1 −0.03 at (0,.2): r46/conv46 1.466 but r56 1.390, s21 1.452 → cluster-specific; others flat.
- MT pairs for chiral S7: S7a c1 (49°) ↔ S7b c2 (131°); S7a c2 ↔ S7b c1; S7a c0 ↔ S7b c0.
- Submitted p7 (8): center S3∥ 0.24 + S7a c1/S7b c2 (−0.03/−0.05, singly and mirror-paired), + S7a c2/S7b c1 +0.03; ridge (0.03,.22),(0.02,.25),(0,.22).
- Submitted w2b (16): w2 class scans ±0.04 for S1 30°, S3 60°, S4 ⊥/30°, S9 ⊥/30°, S12 ∥/60°.
- 246 + 24 = 270 charged.

## 20:33 — wakeup 11
- w3: chiral S7 mirror pair (S7a c1 + S7b c2) at −0.03 on top of S3∥ 0.24: s21 1.534, r46 1.540 (r56 pending); −0.05: s21 1.510, r46 1.576.
  Single S7a c1 −0.03: s21 1.540 r46 1.494. S7a c2 + S7b c1 +0.03: r46 1.396 (bad).
  (0,0.27): min 1.401; (0,0.24) remains min 1.418.
- **w2 has its own gain class: S4⊥ (S4 with perpendicular T1) +0.04 → s21 1.052, r46 1.111, r56 1.076.** Also S1 30°-class −0.04 → s21 1.032, r46 1.036.
  Other w2 classes (S3 60°, S4 30°, S9, S12) negative.
- Submitted p8 (11, w3): S7pair −0.07/−0.04, +S1⊥0.03; probes around (S3∥0.24 + S7pair −0.03) of S7 c0 pair, S13 pairs c0/c1/c2 ±0.03.
- Submitted w2c (11): S4⊥ 0.07–0.2; S1 30°-pair (c0+c1) −0.04/−0.08; combo; S16 ⊥/30° ±0.04.
- 270 + 22 = 292 charged.

## 20:48 — wakeup 12
- w3 S3∥0.24 + S7pair −0.03 (req p7_...m03): s21 1.534 r46 1.540 r56 1.476 conv46 1.540 → min 1.476 (new best min).
  S7pair −0.05: min 1.464 (r56). +S1⊥0.03 & S7pair −0.04: s21 1.582 r46 1.583 (r56 pending).
  Around (S3∥.24, S7p −.03): S13 c0 pair +0.03 s21 1.529 r46 1.506; S13 c2 pair ± ~flat; S7 c0 pair ±: s21 ↓.
- w2: S1 ±30° pair −0.08: s21 1.108 r46 1.130; S4⊥0.1 + S1pair −0.04: s21 1.090 r46 1.246; S4⊥ 0.15+: s21 < 1. S16⊥ −0.04: s21 1.032 r46 1.148.
- Posted H3b (hypothesis_b17e). Submitted p9 (9, w3 3D grid S3∥{.22,.26}×S1⊥{.03,.05}×S7p{−.04,−.06} + S13c0 pair) and w2d (12).
- 292 + 21 = 313 charged.

## 21:04 — wakeup 13
- w3 (S1⊥, S3∥, S7pair, S13c0pair) coordinates: work/coords.py; quadratic surrogate work/fit.py (rms 0.04 s21, 0.035 r46, 0.056 r56).
  Best complete: (0.03,0.24,−0.04,0) p8_..._S1c2_0.03: s21 1.582 r46 1.583 r56 1.545 conv46 1.583 → min 1.545.
  Pending: (0.05,0.26,−0.06,0): s21 1.647 r46 1.649; (0.03,0.24,−0.04,0.03): s21 1.710 r46 1.564.
- Submitted q1 (10): trust-region steps around (0.05,0.26,−0.06,0) incl. surrogate picks (0.02,0.31,−0.10,0.04). Σ|α| up to 1.89 (cap 2.5).
- w2: S1 ±30° pair −0.08 complete: s21 1.108 r46 1.130 r56 1.115 conv46 1.130 (all ≥1.10, PASS) — robust w2 enhancement.
  S4⊥0.05+S1p−0.08: s21 1.149 r46 1.212 (r56 pending). Holding w2 submissions until r56s land.
- 313 + 10 = 323 charged.

## 21:21 — wakeup 14
- w3 best complete: (S1⊥ .05, S3∥ .26, S7p −.06, 0) p9: s21 1.647 r46 1.649 r56 1.626 conv46 1.649 → min 1.626.
  q1 (r56 pending): (.05,.34,−.09,.03) s21 1.940 r46 1.782; (.05,.30,−.09,.03) 1.872/1.792; (.02,.31,−.10,.04) r46 1.774.
  Still climbing; the Σ|α| ≤ 2.5 cap will bind soon (3x+3y+6|z|+6|w|).
- Refit surrogate (B=(.05,.32,−.09,.03)); trust-region pick at corner (.03,.37,−.13,.07).
- Submitted q2 (12): 8 trust-region points (Σ|α| up to 2.4, M2k ratio up to 1.81) + S19/S21 c0-pair probes ±0.03 at (.05,.30,−.09,.03).
- w2 best complete: S4⊥.05 + S1p −.08: s21 1.149 r46 1.212 r56 1.195 conv46 1.212 → min 1.149 (s21 binds).
  Plateau ~1.15 at s21 across S4⊥ .05–.08 × S1p −.08..−.12. Submitted w2e (8): probes ±0.04 of S7 pairs, S13c0 pair, S3 60° pair around it.
- 323 + 20 = 343 charged.

## 21:39 — wakeup 15
- w3 best complete: q1 (.05,.30,−.09,.03) req? s21 1.872 r46 1.792 r56 1.804 conv46 1.790 → min 1.790 (C=1, PES eg 3.9–4.7, split/Δ ≤ 7e-3,
  M2k/M2 1.34, adm 0.87, R_beyondM2 0.92–0.96 vs parent 0.69). (.05,.34,−.09,.03): min 1.780.
  q2 pending r56: (.05,.34,−.12,.03) s21 1.872 r46 1.883. S19/S21 c0 pairs at base: both signs lower → dropped.
  NB: more negative S7 pair lowers m2k_max_ratio (1.17–1.2 at z=−0.14) — gap up while density sharpness falls.
- w2 probes around (S4⊥.05,S1p−.08): S3 60° pair −0.04 → s21 1.177 r46 1.191; S7 c1/c2 pair −0.04 → s21 1.125 r46 1.285; S7 c0 pair +0.04 → 1.123/1.238.
- Submitted q3 (6 w3: S7 pair to −0.15, S3∥ to .38, S1⊥ to .08) and w2f (5 w2 combos with S3 60° pair, S7 pairs).
- 343 + 11 = 354 charged.

## 21:56 — wakeup 16
- w3 best complete: q2 (.05,.34,−.12,.03): s21 1.872 r46 1.883 r56 1.845 conv46 1.881 → min 1.845. q3 pending: (.05,.38,−.12,.03) s21 2.000 r46 1.887.
  r46 saturating ~1.88; s21/r56 noisy (±0.1 between neighbours).
- w2 best complete: S3 60° pair −0.04 on base: min 1.152; pending p60m04_s70p04: 1.184/1.242/1.227.
- Submitted q4 (4 w3), ph1 (16, family w3-phase, phase-only classes ±0.02 on S7a c0-2, S13a c0-2, S1 c0, S3 c1; posted H4), w2g (3).
- 354 + 23 = 377 charged. Remaining plan: ~40 more w3/w2 refinement, coverage posts, final result, done.

## 22:14 — wakeup 17
- w3 best complete: q3 (.05,.38,−.12,.03): s21 2.000 r46 1.887 r56 1.962 conv46 1.885 → min 1.885. (.07,.34,−.12,.03) min 1.882.
  q4 pending: (.06,.36,−.13,.04) s21 1.916 r46 1.931; (.05,.38,−.14,.03) 1.887/1.929.
- Phase-only (ph1, β ±0.02): only S7a c1 β+ > 1 (1.016; β− 0.951). 1D read +1.6 % at β≈0.02. All others 0.94–0.985.
  Submitted ph2: MT-symmetric phase pair (S7a c1 +β, S7b c2 −β) at 0.015/0.025/0.035, and ±0.02 on top of the w3 best.
- w2 best complete: p60m04_s70p04 (S4⊥.05, S1p −.08, S3 60°p −.04, S7c0p +.04): 1.184/1.242/1.227/1.242 → min 1.184. Submitted 3 more (w2h).
- q5 (4): Σ|α| 2.34–2.46, at the brief's Σ|α| ≤ 2.5 boundary.
- 377 + 12 = 389 charged.

## 22:31 — wakeup 18: phase-only gain!
- **Phase-only MT pair (S7a c1 +β, S7b c2 −β), α = 0:** β 0.015 → s21 1.043 r46 1.101; 0.025 → 1.054/1.178; 0.035 → 1.048/1.242 (r56 pending).
  Clean beyond-M2 candidate (|h_k|² unchanged). s21 response flat ~+5 %, r46 strong.
- **On top of w3 amplitude best (.05,.38,−.12,.03): β pair +0.02 → s21 2.240, r46 2.367** (r56 pending); −0.02 → 1.652/1.385.
- w3 amplitude best complete: q4 (.06,.36,−.13,.04): s21 1.916 r46 1.931 r56 1.956 conv46 1.929 → min 1.916; q4 (.05,.38,−.14,.03) min 1.887.
- w2: best complete still p60m04_s70p04 min 1.184.
- Submitted ph3 (12): β pair line 0.045–0.10; S13/S19/S21 c1↔c2 MT phase pairs ±0.025; β pair +0.03/+0.045 on the amplitude best.
- 389 + 12 = 401 charged.

## 22:48 — wakeup 19
- **Amplitude best + S7 MT phase pair β+0.02 (req 20261013T221336.158Z_ctrl-b_req_f321): s21 2.240 r46 2.367 r56 2.332 conv46 2.367 → min 2.240.**
  β+0.03: s21 2.337 r46 2.501; β+0.045: s21 2.481 r46 2.708 (r56 pending).
  Same M2(k) as the amplitude-only point q3 (phase leaves |h|² unchanged): the phase increment (+12–25 %) is at matched diagonal density.
- Pure phase S7 MT pair: s21 peaks 1.054 at β 0.025 (0.045: 1.022, 0.06: 0.950, 0.08: 0.807); r46 rises to 1.296 at 0.045. r56 pending.
  S13/S19/S21 c1↔c2 MT phase pairs: all 0.82–0.98 (negative).
- w2 best complete: w2d_a (S4⊥.04, S1p −.08, S3 60°p −.04, S7c0p +.04) req_0150: min 1.185.
- Coverage posts: w3-single (result_2c26), w3-s1s3 (result_62fd). work/coverage.py summarizes families.
- Submitted ph4 (8: β 0.06/0.08 on best; S7×T2 MT phase pairs ±0.025) and w2i (4: S7 phase pair on w2, alone and on w2 best).
- 401 + 12 = 413 charged.

## 23:05 — wakeup 20
- Phase line on amplitude best (.05,.38,−.12,.03): β .03 → min 2.337; β .045 (req_7a4c) → s21 2.481 r46 2.708 r56 2.644 conv46 2.715 (min 2.481);
  β .06 → s21 2.63 r46 2.93; β .08 → s21 2.81 r46 3.23 (r56 pending). States clean: C=1, eg ~5.3, split/Δ ≤ 5e-3, adm 0.92.
- β −0.02 on best → min 1.38 (sign matters, consistent).
- S7×T2 MT phase pairs: all ~0.87 (negative). Phase on w2: no help.
- Posted result_? (interim 2). Submitted ph5 (6): β .10/.13/.17/.22 on best; β .06 on q4 point and on S3∥0.24-only base.
- 413 + 6 = 419 charged.

## 23:21 — wakeup 21
- Phase line on amplitude best, complete: β .06 → min 2.629 (s21) [r46 2.930 r56 2.841 conv46 2.942]; β .08 → s21 2.813 r46 3.231 r56 3.115 conv46 3.243 (min 2.813).
  Pending: β .10 s21 2.976 r46 3.530; .13 3.143/3.940; .17 3.172/4.339; .22 2.745/4.404 → s21 turns over near β ≈ 0.15–0.17; cluster spread widens (s21 vs r46 up to ×1.4).
  conv46 tracks r46 to <0.5 % everywhere (mesh/g_cutoff/qmax converged).
- Pure phase S7 pair β .025: r56 1.122 (s21 1.054, r46 1.178) — phase-only gain on all three so far (conv pending).
- w2 best + phase +0.02: min 1.129 (worse than w2 best 1.185) → phase pair doesn't transfer to w2.
- Submitted ph6 (7): β .15 on best; at β .13 vary S3∥ (.30/.44), S7 amp (−.08/−.16), S1⊥ (.02/.09).
- 419 + 7 = 426 charged. Remaining ~74: finish line, then coverage posts and done.

## 23:41 — wakeup 22
- **Pure phase (α=0) S7 MT pair complete:** β .015: 1.043/1.101/1.068/1.101; β .025 (req ph2_S7pairMT_b0.025): s21 1.054 r46 1.178 r56 1.122 conv46 1.178;
  β .035: 1.048/1.242/1.172/1.242. → meets "strong" thresholds (≥1.10 on r46/r56/conv46, s21 > 1) with |h_k|² unchanged: clean beyond-M2.
- Amp+phase line complete: β .10 min 2.976; .13 min 3.143; .17 (s21 3.172 r46 4.339 r56 4.217 conv46 4.392) min 3.172; .22 min 2.745 (s21 turned over).
  ph6 amplitude variations at β .13: all s21 2.97–3.20 (x .09 best 3.197) — flat; amplitude optimum does not move much.
  S3∥ .24 alone + β .06: min 2.237 (S7 amplitude not essential).
- Submitted ph7 (16): MT phase-pair coverage for other classes with T1 (S1 30/150, S3 60/120, S4 30/150, S12 60/120, S7 c0/c0, S7 109/71, S13 c0/c0, S13 104/76), ±0.025.
- 426 + 16 = 442 charged.

## 23:58 — wakeup 23
- ph7 MT phase pairs: achiral (S1, S3, S4, S12) symmetric in ±β, all < 1 (no linear term as expected). S7 c0/c0, S7 c2/c1, S13 c2/c1: < 1.
  **S13 c0/c0 pair β −0.025 (S13a c0 −b, S13b c0 +b): s21 1.036, r46 1.139** → second phase-only gain direction.
- ph6 (amp variations at β .13) complete: all min 3.11–3.20; best ph6_x0.09 min 3.197 (req_6417). β .15 on best: min 3.183.
- Phase-only S7 pair β .045 complete: 1.022/1.296/1.219/1.295.
- Submitted ph8 (6): S7 pair + S13 c0 pair phase-only combos; best + S7 β.15 + S13 β −.025.
- Posted w2-joint coverage (result_3dca). Remaining: w3-joint + w3-phase coverage, final summary, done.
- 442 + 6 = 448 charged.

## 00:14 (10-14) — wakeup 24
- ph8: S7+S13 phase-only combos raise r46 (to 1.245) but not s21 (≤1.039 < 1.054 of S7 alone); (.025,−.025) 1.010, (.03,−.03) 0.966. S7 alone β .025 stays the best phase-only (min 1.054).
- ph6 all complete: min 2.97–3.20. Best amp+phase min: ph6_x0.09_b0.130 3.197 (req_6417); ph5 β.17 3.172.
- Posted w3-joint coverage. Waiting for ph8 r56 then w3-phase coverage + final summary + done. 52 evals unspent (by choice).

## 00:31 (10-14) — wakeup 25: DONE
- Final phase results: S13 c0 pair −0.025 complete 1.036/1.139/1.087/1.139; S7+S13 combos ≤ s21 1.039. Best phase-only stays req_b733 (min 1.054, broker claim strong).
- Posted w3-phase coverage (result_5dd3), claim post (claim_cddc), and `swarm done` (note_7364).
- 448/500 charged; 52 unspent by choice. Open: request_ca0e (matched-density control) unanswered.
