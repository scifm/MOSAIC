# ctrl-a notebook

Started 2026-10-14T05:17:02+00:00.

## 2026-10-14 05:25 — wakeup 1: setup + map1 wave 1
- Read brief, docs 40/46, ADR-0032 block schema, kdep_envelope.py. Parent w1c s21 Δ = 2.2586e-4 (PASS).
- Physics notes: pure LL0 at d_s=0.1 is near-zero-mode; static path reproduced at γ=0. Promotions are free,
  so the cheap way to learn finite-size robustness is to get diverse s21 winners (R≥1.02) promoted.
- Aliasing note: T3 star (±2,0) differences (4,0) are a 4x6 superlattice vector -> F_T3 sampled oddly on 4x6.
- Tool: work/build.py make([(Sq, Tq, alpha, beta[, chiral_orbit])], path). Shell q in solver 120° metric
  m²+n²−mn: 1,3,4,7,9,12,13,16,19,21 (7,13,19,21 have two chiral 6-orbits). T q in direct metric: 1,3,4.
- Posted hypothesis map1 (0f17). Submitted 32: S{1,3,4,7,9,12,13,16} x T1 x {α±0.10, β±0.05}.
  Pending in work/map1_w1b: S19, S21 x T1 (8). Then wave 2: T2, T3 (T q=3,4) x all shells.
- Next: collect via swarm show (request.source = file name), analyse linear/quadratic per block.

## 05:38 — wakeup 2: map1 wave1 results → stiffness; grad1/grad1c launched
- map1 (32): w1c is VERY stiff. α=0.1/β=0.05 on S3+ breaks manifold (FAIL, R 0–0.7); S7+ R≈0.
  S1T1: α−0.1 0.9918 (2ed2), α+0.1 0.9020 (e447), β−0.05 0.9449 (3dbc), β+0.05 0.9472 (1d7a). ES ~6 (parent ~20?).
  Fit: R ≈ 1 − 0.45α − 5.3α² → vertex α≈−0.04, +1%. β even (mirror·T symmetry; asymmetry 0.2% = chiral cluster).
- Symmetry reasoning: on mirror-symmetric stars β enters only at even order and no α·β cross term.
  Chiral C6 orbits (12-member shells 7,13,19,21) break mirror → linear β allowed. → grad1c.
- Dropped map1 remainder (S19/S21 at 0.1 pointless). work/collect.py tabulates (arg = path filter).
- grad1: 60 α probes, steps h = {1:.06,3:.025,4:.02,7:.012,9:.01,12:.007,13:.007,16:.005,19:.004,21:.004} × T1,T3(q=3),T4(q=4) ±.
- grad1c: 24 β probes ±h/2 on chiral orbit 0 of S7,13,19,21 × T q=1,3,4.
- Next: fit b,c per block; Newton combination; line search.

## 05:56 — wakeup 3: grad1/grad1c results; line1 launched
- NAMING: my file labels use q=|R|²: "T1"=brief T1, "T3"=brief T2 (|R|²=3), "T4"=brief T3 (|R|²=4). Posts use brief names.
- All 84 PASS. work/fit.py gives per-block b (linear), c (curvature) at s21:
  * T1 (q1): concave, α<0 (S1T1 b=−0.42,c=−5.2; outer shells c ~ −100..−400).
  * q3 (brief T2): linear, b≈+0.2..+1.3, c≈0 (S3 0.58/−0.8, S4 0.70/−1.3, S7 1.27/−11.7, S9 0.96/−1.4, S13 1.31/−6).
  * q4 (brief T3): convex both α signs (c=+18..+300) and β on chiral orbits convex too (S7c b±.006 → 1.0099/1.0088).
  * chiral β on T1/q3: no linear term. Best single so far: S7q4 α+0.012 1.0196 (62c8).
- line1 (37): line scans q3 α>0, q4 α± and β (full + chiral), combT3 additivity test at 0.5x/1x of probe steps.
- Promotion threshold s21 R≥1.02 → confirm21 → r46 ≥1.0 → r56. Watch which survive r46/r56 (q4 aliasing on 4x6!).

## 06:12 — wakeup 4: line1 results — cusp, not linear
- q3 "linear" response was a mirage: gap collapses beyond ~h (level crossing): S3q3 0.06→0.973, 0.12→0.17 FAIL;
  S7q3 0.03→0.88; combT3 0.5x→0.627 (NOT additive: all q3 blocks push the same competing level down).
- q4 α single-block peaks at ~h: S7q4 ±0.012 1.017/1.020, ±0.025 0.971/0.991. S4q4 b0.01 1.0124 (full-shell phase).
  S7c q4 β 0.012 → 1.0143 (69b9). S13q4 α+0.015 → s21 1.0229, s21c 1.0229, r46 1.0599 PASS (442d) → r56 pending!
- ES drops to ~3-5 near peaks (parent ~20). Splitting/Δ grows ~1e-2.
- w4 (29, family line1): q4 single-block peak refinement (all shells), chiral q4 phase-only peaks, 5 pairs.
- Idea: gap = min over excitation branches; need directions raising both branches. Only Δ is observable.

## 06:30 — wakeup 5: first r56 reversal; mesh sampling analysis
- 442d (S13 q4 α.015): s21 1.0229, r46 1.0599, r56 0.9945 → reversal (like pilot 024).
- w4: q4 single-block peaks all ~1.013-1.028 at s21. Promoted to r46 (all PASS): S13c q4 β.008 (ac5d; s21 1.0282, r46 1.0344),
  S3 q4 α.04 (817c; 1.0234/1.0460), S9 q4 α.016 (99e7; 1.0228/1.0382), S7c q4 β.009 (5cb0; 1.0213/1.0258). r56 pending.
  Pairs did not add (best P_S13a_S4b 1.0061).
- work/meshF.py: F_q4 on s21 = F_q1 values permuted (F_q4(k)=F_q1(2k)); on r46 q4 is ALIASED (4 pts at 2.449: Γ+3 M; msq 1.33);
  on r56 2 pts at 2.449. F_q3 on s21 is 2-valued (2.449 at Γ,K,K'; −0.408 else). → q4 r46 gains look like aliasing.

## 06:50 — wakeup 7
- 817c (S3 q4 α.04): r46 1.0460, r56 0.9958 → 2nd reversal. q4 amplitude ≈ −0.5% at r56. Phase ac5d, 5cb0, and 99e7 r56 pending (slow).
- w5 (10, line1): q3 (=brief T2, not aliased on r46/r56) single-block peaks to get q3 candidates promoted; T1 vertex combos (1.0x, 0.6x); S1T1−.04+S3q3+.025.

## 07:01 — wakeup 8
- r56: ac5d (S13c q4 β.008, phase) 0.9935 ✗; 99e7 (S9 q4 α.016) 1.0027 ✓ → SUGGESTIVE (s21 1.0228, r46 1.0382, r56 1.0027).
  r56 so far: S13α −0.55%, S3α −0.42%, S13cβ −0.65%, S9α +0.27%. 5cb0 (S7cβ) pending.
- w5: q3 peaks top out ~1.016 (S3q3 .035 1.0163, S4q3 .03 1.0155, S1q3 .08 1.0153) — below promotion. T1 vertex combo NOT additive (0.887/0.972).
- w6 (12): q4 shells pushed past 1.02 to get r56 data per spatial shell (S1,4,7,9±,12,16,19,21) + S9α+S7cβ mix.

## 07:20 — wakeup 9
- 5cb0 (S7c q4 β.009 phase) r56 0.9940 ✗ → phase-only q4: 0/2 survive r56.
- w6: S12/16/19/21 q4 stall at 1.0194-1.0200 (just under promotion). Promoted: S4 .03 (s21 1.0269/r46 1.0440), S7 .015 (1.0295/1.0464),
  S9 .019 (1.0313/1.0478), S9α.016+S7cβ.006 (1.0289/1.0452); r56 pending. S9 −.016 1.0198, S1 .13 0.9925.
- w7 (9): S9 q4 α .022/.025/.03/−.019/−.022; S12 .015, S16 .014, S19 .009, S21 .009.

## 07:36 — wakeup 10
- r56 table (q4 single blocks unless noted): S13α.015 −0.55%, S3α.04 −0.42%, S13cβ.008 −0.65%, S7cβ.009 −0.60%,
  S9α.016 +0.27% (99e7), S7α.015 +0.05% (4fee), S9α.016+S7cβ.006 −0.14%. → phase hurts r56; amplitude ~0..+0.3%.
- w7: S9 q4 line: .014 1.0178, .016 1.0228, .019 1.0313, .022 1.0262, .025 1.0176, .03 1.0002; −.016 1.0198, −.019 1.0215, −.022 1.0126.
  8 more at r56 (S12 .015, S16 .014, S19 .009, S21 .009, S9 ±.019/.022, S4 .03).
- Assessment: r56 response of q4 family is within ±0.7% → robust_positive (≥1.05) unreachable here; suggestive reached (99e7, 4fee).
- Next: after r56 data, try combos of r56-positive blocks at reduced amplitudes (s21 cusp limits total amplitude),
  then coverage-oriented random-direction sample, then coverage posts.

## 07:55 — wakeup 12
- r56: 629c (S9α.019) 1.0009, 982a (S4α.03) 0.9988. q4 single blocks saturate ~0 on 5×6.
- Posted es1 hypothesis (485b). work/es.py: (1+λ) hill-climb in 60-dim block space, σ·stiffness steps. params in work/es/params_gN.json.
  Gen1: 12 around x0={S9 q4 α .019} σ=.12 seed 1 submitted.

## 08:08 — wakeup 13: ES gen1 breaks the single-block cap
- es g1 (σ.12 around S9q4α.019): s21 1.0453 (g1_02 e89d, r46 1.0642), 1.0451 (g1_06 fab0, r46 1.0598), 1.0438 (g1_07), 1.0407 (g1_04);
  7/12 promoted. Multi-block coordination works at s21. r56 pending.
- fd9a (S16q4α.014) r56 1.0017.
- Gen2 (14): x1 = mean(top4 g1) (work/es_x1.json), + extrapolation x0+2(x1−x0), + 12 samples σ.12 seed 2.

## 08:26 — wakeup 14
- es g2: s21 up to 1.0565 (g2_10 b303; r46 1.0206), 1.0527 (g2_08 8081; r46 1.0681), 1.0524 (g2_01), 1.0521 (g2_04), 1.0517 (g2_06).
  g2_mean 1.0458, extrap 1.0369 (overshoot). ~18 ES points waiting at r56 (bottleneck).
- single-block r56: ac17 (S12) 1.0025, c1b6 (S21) 1.0010, 15d0 (S9 .022) 0.9975, fd9a (S16) 1.0017.
- Gen3 (13): mean(top5 g2) = work/es_x2.json + 12 at σ=.10 seed 3. After this: WAIT for r56 to steer (regress r56 on x).

## 08:50 — wakeup 15
- r56 throughput ~6-7/h (shared). First ES r56: g2_08 (8081) 0.9932 ✗ despite s21 1.0527/r46 1.0681.
  Single-block r56: 9039 (S19) 1.0014, e963 (S9 −.019) 0.9819, ac17 (S12) 1.0025, c1b6 (S21) 1.0010, 15d0 (S9 .022) 0.9975.
- es g3: s21 up to 1.0694 (g3_08 7f33), g3_mean 1.0612 (3141), g3_01 1.0627 (2d1b). r46 1.04-1.07.
- WITHDREW 22 redundant ES promotions (queued runs → back). Priority r56: g1_02 e89d, g1_06 fab0, g1_09 5690, g2_10 b303,
  g2_mean 86e7, g3_mean 3141, g3_08 7f33, g3_01 2d1b.
- Concern: ES on s21 overfits; r56 is binding. Pause ES until r56 data; then regress r56 on x.

## 09:25 — wakeup 16
- ES r56: fff4 (g2_01) 1.0053, c9b8 (g2_04) 0.9852, 3f84 (g2_06) 1.0017, **3b15 (g2_07) 1.0120** (s21 1.0459, r46 1.0681) = best min-R 1.012,
  8081 (g2_08) 0.9932. Multi-block r56 spread −1.5..+1.2% → selectable. r56 queue ~10/h, FIFO by submission (withdraw didn't reorder).
- Switch selection to min over clusters. h1 (10): 8 children σ.08 around g2_07 (work/es_xg207.json) + g2_07 ×0.8, ×1.2.
  es.py now names gens by string (es/<gen>/<gen>_NN.json, es/params_<gen>.json).
- Next: when the 26 queued ES r56 land, ridge-regress r56 (and s21) on x in stiffness units → steer.

## 09:55 — wakeup 17
- More ES r56: e89d (g1_02) 1.0096, fab0 (g1_06) 1.0050, 86e7 (g2_mean) 1.0094, 2d1b (g3_01) 1.0017. ES region r56 +0..+1.2%.
- work/regress.py: ridge on 24 r56 points × 62 features: LOO rmse = std → r56 NOT predictable linearly. Steering must be by selection.
- Posted coverage result for single-block families (37c4).
- h1 (10 around g2_07) all promoted, s21 1.025-1.053, r46 1.05-1.072; r56 pending (32 r56 queued, ~10/h).
- Plan: 1-2 more min-R generations, then coverage-style random directions at larger norm, final es1 coverage post, done.

## 10:28 — wakeup 18
- h1 r56: h1_06 (0d94) 1.0484/1.0724/1.0197 ← best min-R; h1_04 (b6f9) 1.0443/1.0642/1.0182; h1_scale1.2 1.0089; h1_00 1.0075. g3_mean 0.9982.
  New (non-withdrawn) requests reach r56 ahead of withdrawn ones → withdraw DOES deprioritize.
- h2 (10): mean(h1_06,h1_04)=work/es_xh1.json, extrap from g2_07, 8 children σ.08 seed 12.

## 10:56 — wakeup 19
- h1 more r56: h1_07 1.0045. h2: s21 1.026-1.069, r46 1.06-1.074; r56 so far only h2_06 0.9873 (s21 1.0689!) → s21-max ≠ r56.
- rand1 (16, hyp 5c1d): 8 random 60-dim directions around parent at σ=0.3 and 0.6 (files work/rand1/r03_*, r06_*).

## 11:35 — wakeup 20
- h2 r56: **h2_extrap (329e) 1.0531/1.0690/1.0215** best min-R; h2_00 (0db0) 1.0199; h2_07 1.0159; h2_04 1.0092; h2_06 0.9873.
- Direction d = mean(h1_06,h1_04) − g2_07 improves r56 (t=0:1.0120, t=1 pending, t=2:1.0215). h3: t=3,4 line + 6 children σ.06 of h2_extrap.
- collect.py now caches fully-finished requests (was slow). rand1 still waiting for s21 slots.

## 12:01 — wakeup 21
- h2 r56: **h2_03 (9ca0) 1.0410/1.0685/1.0249** best min-R; h2_01 (d9f5) 1.0490/1.0741/1.0226; h2_mean 1.0182.
  min-R trajectory: 1.0027 → 1.0120 (g2_07) → 1.0197 (h1_06) → 1.0215 (h2_extrap) → 1.0249 (h2_03).
- Screen lanes stalled ~1h (24 in flight: h3 + rand1), likely broker busy with r56 promotions.

## 12:34 — wakeup 23
- rand1 (16) done: σ.3 → 0.933, 1.0115, 0.861, 0.946, 1.0053, 0.993, 0.967, 0.800 (2/8 >1);
  σ.6 → 0.339F, 0.809, 0.114F, 0.576, 0.728F, 0.955, 0.899, 0.136F (0/8 >1, 4 FAIL). Generic directions lose.
- h3 at r56 pending: line3 (1aec) 1.0464/1.0526, line4 (ab58) 1.0292/1.0177 → line overshoots past t≈2.
  children h3_00..05: s21 1.027-1.061, r46 1.06-1.073.
- Note: joint (G,R) orbits are NOT expressible in the deformation block (J×P star products only) → out of reach; say so in coverage.

## 13:04 — wakeup 24
- Broker last tick 388 s ago ("looks dead"). Not submitting. h3: a154 (h3_03) r56 1.0089 (s21 1.0608). Others pending.
- If still dead next wakeup → post request (rule 8).

## 13:15 — wakeup 26
- Broker still dead (1047 s). Posted request to human. Holding; no submissions.

## 13:58 — wakeup 27: broker back
- Broker recovered (~13:50). h3 r56: **h3_02 (9fa4) 1.0422/1.0701/1.0332** best min-R; h3_01 (6055) 1.0260; h3_05 (b424) 1.0257;
  h3_00 (6903) 1.0246; h3_04 1.0173; line3 (1aec) 1.0124; h3_03 1.0089. min-R trajectory …→1.0249→1.0332.
- h4 (9): mean(h3_02,h3_01,h3_05), extrap h2_extrap→h3_02 ×2, 7 children σ.06 around h3_02 (work/es_xh3b.json).

## 14:28 — wakeup 28: h4 screens pending behind r56 backlog; holding.

## 14:59 — wakeup 29: r56 backlog 22→7; h4 screens still not started (queue seems FIFO across stages). Holding.

## 15:30 — wakeup 31: h4 all promoted to r56 (s21 1.026-1.054, r46 1.062-1.071). IDs: a3b3=h4_00..5d23=h4_06, fc94=extrap, deb5=mean3. r56 pending.

## 15:57 — wakeup 32
- h4 r56: h4_06 (5d23) 1.0359/1.0664/1.0389 ← best min-R 1.0359; h4_02 (4215) 1.0342/1.0667/1.0370; h4_04 (81b4) 1.0327/1.0619/1.0401;
  h4_01 (6670) 1.0270/1.0626/1.0371; h4_03 1.0306; mean3 (deb5) 1.0295; h4_05 1.0268; h4_00 1.0165.
  → r56 now 1.03-1.04; s21 has become the binding cluster. Converge stage needs min ≥1.05 on s21,r46,r56.
- h5 (9): mean(h4_06,h4_02,h4_04)=work/es_xh4m.json, extrap from x_h3b ×2, 7 children σ.06.

## 16:29 — wakeup 33: h5 map e4e7=00,2e6f=01,f1da=02,f449=03,5238=04,1066=05,c146=06,f2c8=extrap,4d9e=mean3.
- h5_04 (5238) 1.0395/1.0636/1.0347; h5_02 (f1da) min 1.0252; 3 children failed promotion (s21 1.011-1.020). r56 pending: 00, 06, extrap, mean3.
- Stalling near min-R ~1.035; s21 binding.

## 17:00 — wakeup 34
- h5 r56: h5_00 (e4e7) 1.0292/1.0671/1.0448; extrap (f2c8) 1.0249/1.0576/1.0435; h5_06 1.0280/.../1.0365; mean3 (4d9e) 1.0344/1.0656/1.0389.
  No min-R improvement (best h4_06 1.0359). Pareto trade-off s21 vs r56 (s21+r56 ≈ 2.075 on the front).
- CONTROL submitted (be31, --control, s21/r46/r56): matched-density static density <W_G(k,k)/W_0(k,k)>_BZ of h4_06,
  truncated to |G|²≤21 (work/control.py). Differs from parent ≤7.2e-5/coef, M2 ratio 1.00003. Note posted (675b).
- work/localfit.py: local ridge on 43 h-lineage points: r56 LOO rmse 0.0078 vs std 0.0129 (some skill), s21 weak.
  m1 (3): steps ρ=0.3/0.5/0.8 (stiffness units) from h4_06 maximizing predicted min(s21,r56) (pred min 1.044/1.048/1.054).

## 17:30 — wakeup 35
- CONTROL be31: s21 0.9999 / r46 1.0000 / r56 0.9999 → gain of h4_06 is NOT the diagonal density (beyond-M2).
- m1: ρ.3 (b778) 1.0470/1.0683/1.0342; ρ.5 (cc06) 1.0507/1.0658/1.0316; ρ.8 (6f6a) 1.0524/1.0569/1.0276 → s21 up, r56 down. Model failed for r56.
- Plateau at min-R 1.0359 (h4_06). c1 (10): chiral orbit-0 (7,13,19,21)×T1-3 α,β perturbations σ.1 on top of h4_06. Hyp 71ca.
- If c1 doesn't beat 1.0359 → write es1 coverage result + abandon, then swarm done.

## 19:25 — wakeup 36: wrap-up
- c1 (chiral dims): best min-R 1.0348 (4531) — no improvement; front unchanged.
- Posted es1/rand1 coverage result (1264) and abandon (see board). Totals: 340 requests (325 charged + control),
  78 with R>1 on all clusters, best min-R 1.0359 (5d23) suggestive; control be31 flat.
- Decision: swarm done (plateau confirmed by 3 distinct attempts; remaining 175 evals unlikely to reach 1.05).
- swarm done posted (d6ac). Loop stopped.
