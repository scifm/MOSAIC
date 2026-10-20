# ctrl-b notebook

Started 2026-10-14T05:20:51+00:00.

## 2026-10-14 05:25 — wakeup 1: setup + stage A launched
- Read brief, docs 40/46, theory §6.4. Parent w1c Δ_s21 = 2.2586e-4 (PASS).
- Tools: `work/gen.py OUTDIR name 'a:S1:T1=0.1;b:S2:T1=-0.05' ...` builds inputs
  (stars S1..S10 by |G|², whole 12-member shells; T1..T3). n_mesh 48, g_cutoff 8.
- Note: alpha on S1xT1 *lowers* M2^(k)/M2 (0.998 at 0.1, 0.946 at 0.6).
- Hypothesis posted (family `starmap`): stage A = one-coefficient ±steps
  (α ±0.10, β ±0.05) over S1–S6 × T1–T3 (72 evals); B line searches; C CMA-ES.
- Submitted 32 (all α blocks S1–S5 + a61): ids in work/A1_ids.txt.
  Remaining 40 in work/A (α S6 rest + all β) — submit when slots free.

## 05:40 — wakeup 2: stage A1 results (32 evals, α ±0.10 on S1–S5 × T1–T3 + a61)
- Parent refs: Δ_s21 2.2586e-4, Δ_LLL(uniform) 1.83e-4 → parent only 1.24× uniform although M2=10
  (R_staticM2 ≈ 0.125: M2 law badly broken here). r46 2.41e-4, r56 2.59e-4.
- **Laughlin state is fragile to k-dependence on outer stars**: every S2..S6 block at α=±0.1
  fails or collapses (S2: R 0.4–0.75; S3: 0–0.55; S4–S6: R≈0, PES gone). Only S1 survives.
- S1 at α=±0.1 (R): T1 +0.902/−0.992 ; T2 +1.0151/−0.970 ; T3 +1.0180/−1.0068.
  → S1×T3 positive on both signs (positive curvature); S1×T2 linear (+); S1×T1 hurts.
- Admissibility ratio min/max S00 ~0.13 at α=0.1 S1T3 (parent S(k) itself varies).
- Tool: `work/collect.py [filter]` tabulates (cache in work/cache).
- A2 submitted (28): S1 β ±0.05 T1–T3; S1 α 0.2 (T2,T3), −0.2 (T3,T1); S2/S3 α ±0.02 all T;
  S2 β ±0.01. Unsubmitted stage-A files moved to work/A_unsubmitted (outer stars too large).
- Next: line search along +α(S1T2), ±α(S1T3) jointly; small-step outer stars only if linear
  terms look useful.

## 05:55 — wakeup 3: A2 results (28), B1 submitted (30)
- S1 at |α|=0.2 drops to R 0.84–0.90 (all PASS): response is narrow/strongly nonquadratic.
- Small outer-star steps (α ±0.02, β ±0.01) are fine (PASS, eg 7–8.5). R at +/−:
  S2T1 α .973/1.000; S2T2 α 1.0115/.988; S2T3 α 1.0083/1.0065; S3T1 α .964/.995;
  S3T2 α 1.0134/.986; S3T3 α 1.0128/1.0105; β S2T1 .988/.986, S2T2 ~1.000, S2T3 1.008/1.007.
- S1 β ±0.05: T1 .947/.945; T2 .996/.996; T3 1.0081(+)/1.0191(−).
- Pattern: **T2 blocks linear in sign (+α good, all spatial stars)**; **T3 blocks even (both
  signs gain)**; T1 always hurts. Suspicion: T2 linear term and T3 evenness may be Nk=21
  sampling artefacts → want promotions (R≥1.02) to see r46/r56 for free.
- Budget display said 35 charged after 60 requests (counter lag? check).
- B1: line points on S1T2/S1T3 α, S1T3 β, S2/S3 bigger steps, S3 β ±0.01, combos c1–c10.

## 06:10 — wakeup 4: B1 results (30), B2 submitted (26)
- **Combos are strongly sub-additive**: c3 (S1T2 .1+S2T2 .02+S3T2 .02) 0.78; c2 0.91; c6 FAIL 0.50;
  c1 (S1T2+S1T3 α .1) 0.97; c7 (c6 halved) 0.97. Landscape narrow; nonideality damage grows fast.
- Line points: S1T2 α .05→1.011, .15→.976; S1T3 α .05→1.006, .14→.982; S1T3 β −.03→1.009,
  −.08→.964, +.08→.944; S2T2 α .04→1.015; S3T2 α .04→1.0045, .06→.88; S3T3 α ±.04→1.009/.990;
  S2T3 β .02→1.011; S3 β ±.01: T1 .98, T2 1.00, T3 1.011/1.012.
- **Promoted:** c5 (β S1T3 −.05 + α S1T2 .1): s21 1.026, s21c 1.026, r46 1.033, r56 pending.
  l23a04 (α S2T3 .04): s21 1.023, r46 1.046, **r56 0.9958** → sign flip at 5×6 (024-like).
- collect.py fixed (cache only non-promotable results).
- B2: scalings/variants of c5, S2T3 line, S4–S6 × T2/T3 α ±0.01.

## 06:30 — wakeup 5: B2 results (26), B3 submitted (9)
- S4/S5/S6 at α ±0.01 follow the same pattern: T2 linear (+ good ≈ +1%), T3 even (+1% both).
  The T2-linear / T3-even pattern is star-independent → property of the momentum factor on
  Nk=21, not of the spatial star. (Checked analytically: F_T1..T3 first and second moments over
  every cluster's k-points equal the BZ values, so not a crude sampling-moment artefact.)
- c5 neighbourhood: c5v2 (β S1T3 −.05, α S1T2 .05) s21 1.031 r46 1.038; c5v3 (−.07,.1) 1.032/1.027;
  c5s075 1.024/1.027; c5s125 1.009; c5v1 (−.03,.07) 1.020 (not promoted, <1.02); c12 1.018; c11 .944.
  l23bm02 (β S2T3 −.02) 1.022/1.035. S2T3 α: .03→1.0175, .04→1.023, .06→.982, −.04→1.008.
- Waiting on r56 for c5, c5s075, c5v2, c5v3, l23bm02 (5×6 queue is slow).
- B3: c5v2 neighbourhood + phase-only combos on T3.

## 06:50 — wakeup 6: first full ladder; B4 submitted (23)
- **c5 (β S1T3 −.05 + α S1T2 +.10; req 7897): s21 1.026, r46 1.033, r56 1.040, all PASS**
  → "suggestive" tier (R>1 everywhere, <1.05). First survivor across clusters.
- l23a04 flipped at r56 (0.996): S2T3-amplitude is cluster-fragile; c5 family is not (so far).
- B3: d2 (β −.06, α .05) s21 1.0385 r46 1.041 (r56 pending); d3 (β −.05, α .03) 1.029/1.037.
  **Super-additive** in this plane: α S1T2 .05 alone 1.011, β S1T3 −.06 alone 1.004, together 1.0385.
  Phase-only on T3 stacks badly (p1 .89, p3 FAIL); adding β S2T3 to c5v2 hurts (d4 .946).
- Converge stage needs min R ≥ 1.05 *including s21* → need s21 ≥ 1.05.
- B4: grid β S1T3 ∈ −{.06..0.10} × α S1T2 ∈ {.03,.05,.07}; sign flips e1/e2; swapped roles e3;
  small add-ons e4–e8.

## 07:12 — wakeup 7: B4 results, B5 submitted (14)
- r56 landed: c5s075 1.028 (s21 1.024, r46 1.027) — suggestive; c5v2 1.006; c5v3 1.018.
  So far every c5-family point with r56 is >1 but r56 values scatter 1.006–1.040.
- B4 grid (β S1T3, α S1T2): optimum near β −.06..−.07, α .05...07 (s21 ≤1.044); β ≤ −.08 falls
  fast; g_b08_a07 s21 1.044 but r46 0.996, g_b09_a07 r46 0.946 → larger |β13| is cluster-fragile.
- **e7 = β S1T3 −.06, α S1T2 .05, β S1T2 +.02: s21 1.047, r46 1.063** (r56 pending). New axis β12.
  e1 (β13 sign flipped +.06) 1.0245/1.035; e2 (α12 −.05) 1.020; e3 (roles swapped) .990.
- Quadratic surrogate over S1-only coords (work/fit.py) fits poorly (rms 1.9%): landscape not quadratic.
- B5: local scan around e7 along β12, α12, β13 and combos.

## 07:35 — wakeup 8: B5 results, B6 submitted (10)
- **e7: s21 1.047, r46 1.063, r56 1.026** (all PASS) — best min so far (suggestive tier).
- r56 is the bottleneck and prefers larger α S1T2 / smaller |β S1T3|:
  (β13,α12,β12)→r56: c5(−.05,.10,0) 1.040; c5s075 1.028; c5v3(−.07,.10) 1.018; c5v2(−.05,.05) 1.006;
  d2(−.06,.05) 0.997; g_b06_a07(−.06,.07) 1.010; e7(−.06,.05,.02) 1.026; e5 (d2+αS3T2 .01) 1.021; e4 1.000.
- B5 (s21/r46): f_b07 (β13 −.07) 1.051/1.055; f_a03 1.048/1.062; f_p03 1.040/1.071; f_p04 1.021/1.077;
  β12 ≥ .06 or ≤ −.02 collapses (.93/.97); β13 sign flip with β12 present: .949. r56 all pending.
- B6: α12 .10–.12 with β12 and αS3T2 add-ons, aiming at r56.

## 08:00 — wakeup 9: B6 results, B7 submitted (10)
- r56 keeps lagging: f_a03 1.016, f_a13 1.023, f_b07 1.017, e8 1.011, d3 0.995. Best min still
  e7 (1.026) and c5 (1.026, r56 1.040).
- α S1T2 ≥ .10 with β13 kills s21 promotion (h2 1.009, h4 1.001, h8 1.014, h9 1.010) — the s21≥1.02
  gate blocks the r56-rich corner around c5.
- Add-ons that moved r56 up relative to d2 (0.997): αS3T2 +.01 → 1.021 (e5); αS1T1 −.02 → 1.011 (e8).
- B7: e7 (and f_b07-like base) + those add-ons, + αS4T2/S5T2 .01, βS1T1 .01.

## 08:30 — wakeup 10: r56 batch, B8 submitted (8)
- **f_a07 (β S1T3 −.06, α S1T2 .07, β S1T2 .02; req 6869): s21 1.041, r46 1.062, r56 1.037** → best min.
  f_b05 (β13 −.05, α .05, β12 .02): 1.041/1.058/1.030. f_77p2 1.043/1.054/1.026. f_p01 r56 1.011.
- B7 screens: k10 (e7 + β S1T1 .01) s21 1.054 (best s21); k5 (αS4T2) .009, k9 (αS3T2 .02) .009 — drop.
- r56 queue ~20 deep; keep screens small.
- B8: around f_a07 (α12 .07–.09, β13 −.05/−.06, β12 .015–.025, βS1T1 .01/.02).

## 09:00 — wakeup 11: r56 results; B9 submitted (15)
- New mins: f_p03 (β13 −.06, α12 .05, β12 .03) 1.040/1.071/1.042 → **min 1.040 (best, req 9896)**;
  k1 (e7+αS1T1 −.02) 1.044/1.070/1.038; k2 (αS1T1 −.04) 1.036/1.072/1.048; h7=k3 (e7+αS3T2 .01)
  1.036/1.063/1.045; k6 1.037/1.055/1.034; k7 1.048/1.062/1.030; k10 (βS1T1 .01) 1.054/1.063/1.014.
- **s21 and r56 trade off** along every S1 direction tried (finite differences at e7):
  αS1T1 −.02: Δs21 −.003, Δr56 +.013 (best ratio); αS3T2 +.01: −.011/+.019; β12 .03: −.007/+.016;
  α12 .07: −.006/+.012; β13 −.07: +.004/−.009; βS1T1 +.01: +.007/−.012. r46 ≈ 1.06–1.07 throughout.
  Linear extrapolation needs huge steps for min ≥ 1.05 → not reachable with these directions alone.
- B9: 15 one-step probes on new directions (S2/S3/S4 × T1–T3 α/β) at base k1 to find any direction
  that raises s21 and r56 together.

## 09:27 — wakeup 12: waiting on B9 r56
- B8 r56: m1 (α12 .09) 1.030/1.060/1.046; m6 1.035/1.060/1.045; m5 (β12 .025) 1.037/1.067/1.043;
  m2 1.037/1.058/1.042; m8 1.043/1.057/1.030; m4/m7 (βS1T1 on) r56 1.027/1.010. Best min still f_p03 1.040.
- B9 screens vs base k1 (s21 1.0437, r46 1.0695): αS2T1 +.01 → s21 1.0507 (n01);
  βS2T1 +.005 → 1.0509 (n06); αS3T1 +.01 → 1.0519 but r56 1.023 (n15); βS2T3 −.01 → s21 1.051 but
  r46 1.015 (n08); βS2T2 .01 → 1.002 (n07); βS3T3 .01 → r46 1.039 (n14). r56 for n01..n14 pending.
- No submissions this tick (r56 queue ~20 deep, the decisive data).

## 10:05 — wakeup 13: B9 r56 back; new family jointorb (J1, 10 submitted)
- B9 confirms universal trade-off: n01 (αS2T1) +.007 s21 / −.013 r56; n06 +.007/−.015; n15 +.008/−.015;
  n12 (βS1T1 −.01) −.011/+.006; n05 (αS2T3 −.01) 1.044/1.071/1.040; n11 (αS1T3 −.02) 1.043/1.072/1.040.
  (s21 + r56) ≈ 2.08 everywhere on the ridge → product-star subspace saturates at min ≈ 1.04.
- New family **jointorb** (hypothesis 3761): S1 split into inversion pairs, couplings restricted to
  C6 joint-orbit classes by R-vs-G line angle (T2: 0/±60; T1,T3: 90/±30). Tool work/gen2.py
  (terms 'a|b:S1:T<p>:<cls>=v'; 'all' = product star, verified identical γ to 2e-16).
- J1: j_all (encoding sanity, should equal f_p03), + each f_p03 term concentrated in one class.

## 10:25 — wakeup 14: J1 results — joint-orbit classes are the key; J2 submitted (16)
- j_all reproduces f_p03 exactly (s21 1.0396, r46 1.0707) → pair encoding verified in the solver.
- Concentrating each f_p03 term into one class (equal Σ|coef|), s21 / r46:
  β S1T3: **+30 → 1.146 / 1.089**; −30 → .885; 90 → .869  (strongly chiral!)
  α S1T2: **0 (parallel) → 1.076 / 1.107**; −60 → 1.027/1.048; +60 → .989
  β S1T2: **+60 → 1.073 / 1.095**; 0 → 1.044/1.072; −60 → .963
- Side note: h10 (starmap) got r56 1.053 and is pending converge.
- J2: best classes combined (q_best3), pairwise, scalings of β13(+30) from −.04 to −.14, sign flip,
  α12(0) .08/.12, β12(+60) .05/.08, singles, and ×2 of best3.

## 10:48 — wakeup 15: robust positives; J3 submitted (19); result post 971a
- I had misread the claim rule: s21 only needs R>1; ≥1.05 needed on r46, r56, conv46. converge ran
  for several starmap points (h1, h10, k4, k8, m3, n03 — r56 1.052–1.060, conv46 = r46 to 4 digits).
- **jointorb robust_positive:** 618a (α S1T2 parallel) 1.076/1.107/1.068/1.107; f61c (β S1T2 +60)
  1.073/1.095/1.061/1.095. conv46 reproduces r46 → numerically converged.
- J2 screens (s21 / r46, r56 pending): q_b12c60_05 1.276/1.196; q_a12c0_08 1.231/1.184;
  q_best3 1.226/1.173; q_b13c30_04 1.181/1.179; q_b13c30_b12c60 1.200/1.157; q_b13c30_a12c0 1.182/1.144;
  q_b13c30_08 1.247/1.088; q_b13c30_10 r46 0.92; −0.14 FAIL; sign flip +.06 FAIL .71; ×2 FAIL .14;
  b12c60 .08 FAIL(1.16 but gate); b13c30 alone .974; a12c0 alone 1.030; b12c60 alone 1.019.
- J3: phase-only (β13 c30 + β12 c60) for a clean beyond-M2 candidate; combos pushing α12c0 .08 &
  β12c60 .05; add-on classes on S1T1/S1T3.

## 11:18 — wakeup 16: STRONG claim (c3e6); J4 submitted (15); control requested
- **c3e6 (q_b13c30_04: β S1T3 c+30 −.04, α S1T2 c0 .05, β S1T2 c+60 .03): 1.181/1.179/1.100/1.179
  all PASS, C=1 → broker claim "strong"** (r56 right at 1.10). Claim post 754b; request 1e94 for
  matched-density static control (has α≠0).
- Other J2 converge: 2750 (α12c0 .08) 1.231/1.184/1.087/1.184; 6631 (β12c60 .05) 1.276/1.196/1.083;
  7248 best3 1.226/1.173/1.077; 5f79 1.060 r56; 2ae0 1.053 r56; ce2e (β13 −.08) r56 0.997.
  → r56 lags r46 by 8–11 %; larger β13 hurts r56. r56 favours small β13 (−.04).
- J3 screens: phase-only pB3 (β13c30 −.04, β12c60 .05) 1.185/1.205 (r56 pending) ← clean beyond-M2 hope;
  pB4 (β13 −.08) 1.287/1.062; x6 (best3 + α S1T1 c90 −.03) **1.322/1.307**; x3 (α S1T1 c+30 .03)
  1.276/1.214; r3 1.233/1.208; r4 1.275/1.199; x4/x5 (β S1T1 c±30) bad; r7 (no β13) r46 .86.
- J4: α S1T1 c90 scan (y1–y8), phase-only line around pB3 (z1–z7).

## 11:48 — wakeup 17: more STRONG; phase-only robust_positive; J5 submitted (16)
- x6 (best3 + α S1T1 c90 −.03; req 58c3): **1.322/1.307/1.189/1.307 strong**; x3 (α S1T1 c+30 .03; 0521)
  1.276/1.214/1.109/1.214 strong; r3 1.233/1.208/1.0985; r5 1.217/1.189/1.093; r4 1.275/1.199/1.064.
- **Phase-only pB3 (β S1T3 c+30 −.04, β S1T2 c+60 .05; req 0438): 1.185/1.205/1.083/1.205
  robust_positive — clean beyond-M2 (|h_k|² unchanged).** pB6 1.193/1.183/1.072; pB2 r56 1.064.
- J4 screens: **α S1T1 c90 is a big lever**: y1 (−.05) 1.380/1.397; **y2 (−.08) 1.457/1.515**;
  y7 1.406/1.333; y3 1.382/1.350. Phase-only z-line: z5 1.217/1.197, z6 1.166/1.200, z4 1.201/1.170.
- New tool work/gen3.py: general pair-basis builder for any S_s, T_p (verified vs gen2, 6e-17).
  Classes: S1/S3 × T1/T3 {90,±30}, × T2 {0,±60}; S2 × T1/T3 {0,±60}, × T2 {90,±30}.
- J5: α S1T1 c90 −.12…−.25, alone, sign flip, with pB3; phase-only S2/S3 class add-ons on pB3.

## 12:20 — wakeup 18: R_gap ≈ 2; matched-density control submitted; J6 (13)
- **u25 (best3 + α S1T1 c90 −.25; req 72d8): 1.736/2.071/1.974/2.071 all PASS (strong).** Monotone in
  |α|: u12 1.544/1.659, u16 1.615/1.796/1.663, u20 1.674/1.924/1.805. M2(k) 9.81 (< parent 10.035).
  u08only (term alone, −.08) 1.262/1.274; u08pb3 1.461/1.486; u08x3 1.533/1.563; u08p (+.08) .865.
- J4 r56: y2 1.457/1.515/1.374; y1 1.380/1.397/1.263; y3 1.229 r56; y8 1.214; y6 1.200; y7 1.190.
- Phase-only: z5 1.217/1.197/1.077 robust; z1 r56 1.048. **v21c60 (pB3 + β S2T1 c+60 .02):
  s21 1.497, r46 1.366** (phase-only lever, r56 pending); v21c0 1.236/1.111; v21c−60 .845; S2T2 classes
  FAIL/loss; v33 (β S3T3 c30) r46 .82; v32 .99.
- **Control**: work/mkctrl.py builds static W_G of ρ̄ = <|h_k|²/<|h_k|²>_uc>_BZ; for u25: M2(ρ̄) 9.70,
  ρ̄_min .056; submitted --control on s21,r46,r56 (req 5657). Hypothesis update ae40.
- J6: α S1T1 c90 −.30…−.60 (boundary), alone −.25/−.40; β S2T1 c60 .03–.08 on pB3, alone, sign, mixed.

## 12:50 — wakeup 19: control says beyond-M2; u50 R≈2.1–2.7; J7 (16) around u50
- **Control 5657 (matched density of u25): R 0.981/0.980/0.979** vs u25 1.736/2.071/1.974 → gain is
  momentum-dependent, not density. Result post 0879.
- α S1T1 c90 axis on best3: u40 1.919/2.464/2.485; **u50 2.070/2.499/2.686** (conv pending); u60 drops
  1.620/1.912. Term alone: u25only 1.466/1.895; u40only FAIL (s21 splitting 0.102Δ, R 1.52).
- Phase-only v21c60 (pB3+β S2T1 c60 .02; ec26) 1.497/1.366/1.176/1.366 strong. Bigger S2T1 phase
  steps all FAIL the s21 splitting gate (0.10–0.5Δ), non-monotone (w08 R 2.08 FAIL).
- J7: around u50 — t45/t55, B3 scale ×1.5/×0.5/×0, individual B3 terms, + S2T1 phase, + other S1T1
  classes, + α S1T3 c90 ±.1, α S1T2 c±60.

## 13:18 — wakeup 20: u50 converged min 2.07; J7 screens; J8 (13) combos
- u50 (8203): **2.070/2.499/2.686/2.499**; u40 1.919/2.464/2.485/2.464; u30 1.793/2.212/2.146; u60
  1.620/1.912/2.276; u25only 1.466/1.895/1.765 (term alone carries most).
- J7 screens (s21/r46): t50v (+β S2T1 c60 .02) **2.627/3.042**; t50xp (+α S1T1 c−30 .05) 2.293/2.760;
  t50b12 (β12 .06) 2.348/2.480; t50x3 2.221/2.674; t50s0 (U alone) 1.882/2.650; t50s15 2.093/2.328;
  t50a13± FAIL; t50xm (α c−30 −.05) 1.735. s21 is now the min cluster.
- J8: combinations of the add-ons on u50, S2T1 phase step sizes, U ∈ {−.4, −.6} with add-ons.

## 13:32 — wakeup 21: t50v min 2.63 converged; J9 (13) around k02
- t50v (u50 + β S2T1 c60 .02; c1a1): **2.627/3.042/3.143/3.042**. t50b12 2.348/2.480/2.747; t50xp
  2.293/2.760/2.893. r56 now ≥ r46 > s21 → s21 is the limiting cluster.
- J8 screens: k02 (u50+V+XP+β12 .06) **3.063/3.375**; k03 (k01+X3) 2.899/3.521; k01 2.850/3.338;
  k04 (V .03) 2.849/3.298; k06 (U+V, no B3) 2.330/3.133. r56 pending.
- J9: single moves from k02 (V .03/.04, XP .10, β13 −.04, α12 .08, U −.45/−.55, β12 .08, β S1T1 c90 ±.05,
  α S2T1 c60 ±.05, +X3).

## 14:02 — wakeup 22: m02 min 3.48 converged; J10 (10) cumulative; control for m02 (37c5)
- k02 (f505) 3.063/3.375/3.427/3.375. **m02 (k02 + X3 + V .03; 8ac8): 3.476/3.882/3.654/3.882**.
  m01 3.214/3.559/3.533; m09 (β12 .08) 3.236/3.350/3.458.
- J9 screens vs k02 (3.063/3.375): V .04 (m03) 3.535/3.967; XP .10+X3 (m04) 3.366/3.770;
  β S1T1 c90 −.05 (m11) 3.186; α S2T1 c60 +.05 (m12) 3.220; U −.55 3.096, −.45 2.965; β13 −.04 3.031;
  α12 .08 3.019; β S1T1 c90 +.05 2.899; α S2T1 c60 −.05 2.709.
- J10: cumulative combos (n01–n10). Σ|α| now ~2.2 (boundary 2.5).
- Control for m02: M2(ρ̄) 8.92, ρ̄ trunc err 2e-3; submitted 37c5 (note: --builds-on given a bogus id).

## 14:30 — wakeup 23: n04 min 4.12; m02 control 0.94; J11 (16) single moves from n04
- **n04 (a179): 4.188/4.433/4.123/4.433** = b13c30 −.06, a12c0 .05, b12c60 .08, U(a11c90) −.50,
  V(b21c60) .04, XP(a11c−30) .10, X3(a11c30) .03, b11c90 −.05. n05 (+a21c60 .05) 4.173/4.210/3.872;
  n07 4.006/4.105/3.674; m03 3.535/3.967/3.640. r56/conv all PASS.
- Control for m02 (37c5): s21 0.938, r46 0.937 (r56 pending) → still beyond M2 (M2(ρ̄) 8.92).
- Tool: work/n04.sh `spec key=val ...` (verified reproduces n04 block exactly).
- J11: one-at-a-time moves on 8 terms + new S2T1 c0 β, S2T3 c60 β, S2T1 c0 α, S3T1 c90 β/α.
- Budget 310/500 + 16. Plan: ~2 more ascent rounds, then coverage probes of untouched structure,
  then final control on the best + coverage/result posts.

## 15:00 — wakeup 24: J11 screens; J12 (11) cumulative incl. new lever α S2T1 c0
- J10 converged: n04 best (min 4.123). n03 4.003/4.311/3.854; n10 3.916/4.424/3.793; n02 3.858/4.201/3.838.
- J11 vs n04 (s21 4.188 / r46 4.433): **o14 α S2T1 c0 +.05 → 4.873/5.019/4.645(r56)**; o02 V .06 →
  4.645/4.746/4.181; o01 V .05 4.437; o15 β S3T1 c90 −.03 4.426; o04 β12 .10 4.348; o05 XP .15 4.312;
  o06 X3 .06 4.289; o03 β11c90 −.08 4.280; o07 β13 −.08 4.224; o12 β S2T1 c0 .02 4.225; o09 4.19;
  o08 β13 −.04 4.138; o13 4.102; o10 U −.45 4.065; o11 U −.40 3.936; o16 α S3T1 c90 −.1 3.815/4.725.
- J12: cumulative (p01–p05, p10), α S2T1 c0 .08/.10 (p06–p08), α S2T3 c0 (p09), sign check p11.
  Σ|α| up to 2.43 (boundary 2.5).

## 15:31 — wakeup 25: o14 converged min 4.64; J12 screens ~5.2–6.0; J13 (12)
- o14 (c172): 4.873/5.019/4.645/5.019. o15 4.426/4.359/4.310; o02 4.645/4.746/4.181.
- J12 screens (s21/r46[/r56]): **p08 (n04 + α S2T1 c0 .10 + V .06 + β S3T1 c90 −.03) 5.981/5.883/5.465**;
  p10 5.970/5.664/5.302; p05 5.879/5.596; p04 5.833/5.620; p03 5.792/5.572; p02 5.618/5.557;
  p07 5.604/5.513; p01 5.360/5.294; p06 (α S2T1 c0 .10 alone on n04) 5.237/5.353; p09 4.302; p11 (sign −) 3.114.
- J13 from p08 (Σ|α| near 2.5 limit): α S2T1 c0 .15/.20, p05/p04 add-ons, α S2T2 classes ±, V .08,
  β S3T1 c90 −.06, α S2T1 c±60.

## 16:02 — wakeup 26: p08 conv min 5.46; q09 min 5.70; J14 (10)
- p08 (1ca8) 5.981/5.883/5.465/5.883; p10 5.970/5.664/5.302; p04 5.833/5.620/5.237; p05 5.879/5.596/5.231.
- **q09 (p08 with V .08; 900d): 6.431/6.110/5.702/6.110**; q08 (α S2T2 c−30 .05; a149) 6.275/6.117/5.694.
  q04 6.255/5.929/5.609; q10 (β S3T1 −.06) 6.034/5.946/5.576; screens q03 6.328/5.914, q07 6.306/5.921.
  α S2T1 c0 .15 (q01) 5.854/5.957; .20 (q02, XP .05) 5.325. α S2T2 c90 ± ~neutral at s21, r46 down for +.
- Per-step gains now ~3–5 %; r56 is the limiting cluster again. Σ|α| capped ~2.5.
- J14 from q09: q03 add-ons, α S2T2 c±30, V .10, β S3T1 −.06, trade U→−.45 for α S2T1 c0 .15.
- Budget 349 + 10. Plan: J15 last ascent round (~10), then ~25 coverage probes (S4–S6 joint
  orbits, T2/T3 for S2, β-only structure) and the final control.

## 16:33 — wakeup 27: q09 confirmed min 5.70; r08 screens 7.47/6.97/6.62(r56); J15 (10)
- J13 converged: q09 best (5.702); q08 5.694; q04 5.609; q03 6.328/5.914/5.586; q10 5.576.
- J14 screens: **r08 (q09+q03 adds + α S2T2 c−30 .05 + β S3T1 c90 −.06 + V .10; d210):
  7.465/6.973/6.624** (conv pending); r06 (V .10) 7.052/6.444; r03 (α S2T2 c30) 6.971/6.312;
  r02 (α S2T2 c−30) 6.928/6.503; r07 6.894/6.406; r01 6.683/6.275; r10 6.638; r05 6.587; r09 6.504; r04 6.219.
- J15: phase-only moves from r08 (α Σ = 2.49 saturated): V .12/.15, β S3T1 c90 −.09, β12 .12,
  β11c90 −.11, β on S3T2 c60 / S3T1 c±30 / S2T3 c60 / S3T3 c30.
- m02 control r56 still pending (5×6 queue).

## 17:03 — wakeup 28: m02 control done (0.94/0.94/0.93); J14 r56 in; C1 coverage (13)
- m02 control (37c5): 0.938/0.937/0.933 → beyond-M2 again (two controls now: u25, m02).
- J14 r56: r08 6.624 (min); r02 6.129; r06 6.083; r07 6.024; r03 6.009; conv pending for all.
- J15 screens still queued behind converge runs.
- C1 coverage at q09 base: outer stars S4 (classes ±11°), S5 (like S1: c90), S6 (like S2: c0/c60),
  S5T2, S6T2 at per-pair ±0.02. Class lists: S4T1/T3 {±11,±49,±71}, S4T2 {±19,±41,±79}.

## 17:34 — wakeup 29: s07 min 7.29 converged; C1 coverage screens; J16 (8)
- r08 conv: 7.465/6.973/6.624/6.973. **s07 (r08 + β S3T1 c+30 .03; a722): 8.354/7.670/7.294/7.670**;
  s02 (V .15) 8.396/7.663/6.961/7.663; s01 (V .12) 8.022/7.354/6.975; s05 7.449/6.978/6.628;
  s09 (β S2T3 c60) 7.412/7.383/6.875; screens s03 7.417/6.614, s04 7.343/6.859, s06 (β S3T2 c60) 6.750/5.464,
  s08 (β S3T1 c−30) 6.528/6.112, s10 (β S3T3 c30) 6.460/5.374.
- C1 coverage at q09 (6.431/6.110), per-pair 0.02: α S5T1 c90 − 6.823/6.615; α S5T2 c0 6.763/6.523;
  β S5T2 c60 6.766/5.874; β S5T1 c90 − 6.653/6.441; α S6T2 c−30 6.587/6.423; α S6T1 c0 6.577/6.302;
  α S4T1 c±11 + 6.53–6.55/6.234, − 6.16–6.17/5.90; β S4T1 c11 6.017; β S4T1 c−11 5.086/5.349;
  β S6T1 c60 6.197/6.381. Outer stars: modest (≤ +6 %) and mirror the S1/S2 pattern.
- J16 from s07: V .15/.18, β S3T1 c30 .05/.06, + β S5T1 c90, β S2T3 c60, α trade to S5.
- Budget 382 + 8 = 390. Remaining ~110: J17 last round (≤10), final control on best (1), then
  coverage/result/claim posts and `swarm done`. Keep ~30 spare.

## 18:10 — wakeup 30: t07 min 8.18; C1 coverage converged; J17 (8)
- **t07 (s07 + V .15 + β S3T1 c30 .05 + β S5T1 c90 −.02 + β S2T3 c60 .03; e3dc): 8.840/9.080/8.180/9.081**;
  t06 (V .15 + α trade XP .06→S5T1 c90 −.02, S5T2 c0 .02; db7c) 9.374/8.664/8.074; t04 (V .15 + β S5T1 c90 −.02)
  9.073/8.529/8.022; t05 8.216/8.055/7.091; t01 8.438/7.914/6.955; t03 8.605/7.986/7.515; t08 (V .18) 6.047 ↓.
- C1 coverage converged (q09 base 6.431/6.110/5.702/6.110): best add-ons α S5T1 c90 −.02 6.823/6.615/6.178;
  α S5T2 c0 6.763/6.523/5.967; β S5T1 c90 6.653/6.441/5.974; S6 ~neutral; S4 ± sign-dependent (−4 % … +2 %);
  β S4T1 c−11 −21 %. All 13 PASS.
- J17 from t07: β S5T1 c90 −.04/−.06, α trade to S5, β S3T1 c30 .03, V .12, combos.

## 18:46 — wakeup 31: u02 min 9.19 converged; J18 (8)
- **u02 (t07 + α trade XP .10→.06, α S5T1 c90 −.02, α S5T2 c0 .02; 5e06): 9.188/9.722/9.210/9.724**.
  u03 (+β S5T1 c90 −.04) 8.666/9.673/9.250; u04 8.835/8.796/8.035; t07 conv 9.081. s21 and r56 now ~equal.
- J18 from u02: β S3T1 c30 .04, drop β S2T3, deeper α trade into S5 (c90/T2 c0), β S5T1 −.03,
  β S5T2 c60, α S6T2 c−30, β S2T1 c0.
- Budget 398 + 8 = 406. ~94 left.

## 19:23 — wakeup 32: plateau ~9.1–9.2; J19 (7) incl. decomposition; control for u02
- J17 conv: u07 8.314/9.737/9.315; u01 8.354/9.457/8.777; u06 7.738/9.267/8.764. u02 still best min 9.19.
- J18: v06 (β S5T2 c60 .02) **s21 10.019**/9.522/9.049; v01 9.228/9.566/9.080; v02 9.195/9.132/8.900;
  screens v05 8.964/9.834, v08 8.684/9.701, v04 9.073/9.372, v07 9.093/9.184, v03 8.645/8.985.
  → s21↔r56 trade-off again; gains per step ≲1–2 %. Plateau of this coordinate search ~9.2.
- J19: w01–w05 last trade-off tries; **decomposition** d1 = u02 phases only (α=0, beyond-M2 by
  construction), d2 = u02 amplitudes only (β=0).
- Control for u02 (mkctrl) submitted.
- u02 control v1 5a7f (|G|²≤49, trunc err 2.6e-2); v2 with |G|²≤121 (err 1e-4) submitted too. mkctrl now uses |G|²≤121.

## 19:58 — wakeup 33: u02 control 0.94; decomposition; J20 (3) scaled phase-only
- **u02 matched-density control: 0.944/0.942/0.939 (5a7f, |G|²≤49) and 0.944/0.942/0.939 (fafb, |G|²≤121)**
  → truncation irrelevant; u02's ×9.2 gain is beyond M2 (three controls: u25 0.98, m02 0.93–0.94, u02 0.94).
- Decomposition of u02 at s21: phases only (d1, α=0) R 6.00 but FAIL (splitting 0.106Δ, PES eg 0.28);
  amplitudes only (d2, β=0) R 3.21 FAIL (splitting 0.104Δ). Both parts needed for a clean Laughlin manifold.
- J18 conv: v05 8.964/9.834/9.286; v08 8.684/9.701/9.097; v06 10.019/9.522/9.049; v01 9.228/9.566/9.080.
  None beats u02 min 9.188. J19: w04 (β S5T2 c60 .04) FAIL splitting .107; w01–w03, w05 r56 pending.
- J20: u02's phase part scaled ×0.5/0.7/0.85 to find the largest clean phase-only point.
- Budget 419 + 3 = 422.

## 20:35 — wakeup 34: plateau confirmed; phase-only scaling fails; R1 random local check (8)
- J19 conv: w05 9.914/9.592/8.981; w02 9.891/9.305/8.857; w03 9.906/9.138/8.712; w01 9.566/9.009/8.761.
  None beats u02 (min 9.188).
- J20 phase-only part of u02 scaled: ×0.5 R 0.47 FAIL, ×0.7 1.54 FAIL, ×0.85 3.59 FAIL (×1.0: 6.00 FAIL).
  The phase-only sub-structure of u02 is not a clean Laughlin state on its own at any scale tried;
  best clean phase-only remains v21c60 (ec26) 1.497/1.366/1.176/1.366 and pB3 (0438) 1.185/1.205/1.083.
- R1: 8 random perturbations of u02 (rel 15 %, per pair, C6-breaking; seed 7; work/perturb.py).
- Then: final posts (coverage for starmap + jointorb, claim for u02, result for controls), swarm done.

## 21:18 — wakeup 35: R1 local check → u02 is a local optimum; final posts; J21 (8) α re-allocation
- R1 (8 random ±15 % C6-breaking perturbations of u02): all PASS, s21 8.64–9.14, r46 9.25–9.63 — all below u02.
- Posted: claim aff4 (u02 strong + beyond-M2, control fafb), starmap coverage f9e9, jointorb coverage 4197.
- Last idea: Σ|α| is the binding constraint (2.49/2.5) → J21 moves the weak α terms (S1T1 ±30° classes,
  0.27 of Σ) or 0.05 of U into the strong levers (S2T1 ∥, S2T2 −30°, S5T1 ⊥, S5T2 ∥).
- After J21: update claim if improved, then `swarm done` (budget 430 + 8 = 438).

## 22:02 — wakeup 36: J21 → **y8 min 10.15**; J22 (6) transfer U → S5T1 ⊥
- R1 r56 done: all 8 below u02 (min 8.64–9.12) → u02 locally optimal against random C6-breaking noise.
- J21 (α re-allocation): **y8 (U −.45, α S5T1 ⊥ −.07; 47ad): 10.296/10.761/10.151/10.760** — new best.
  y7 (U −.45, α S2T1 ∥ .15) 9.837/9.960/9.065; y1 (weak ±30° terms → S2T1 ∥ .19) 8.239/9.138/8.682;
  y6 7.968/8.654/8.157; y4 (→ S5T1 ⊥ −.11) 6.234/6.651/6.242; y3/y5/y9 FAIL. The S1T1 ±30° terms matter;
  U ↔ S5T1 ⊥ is the profitable trade.
- J22: scan of the transfer (U −.40/−.35/−.30 with S5T1 ⊥ −.12/−.17/−.22), + α S2T1 ∥, + β S5T1 ⊥.

## 22:38 — wakeup 37: z1 min 10.52; J23 (5) final refinement
- J22: **z1 (U −.40, α S5T1 ⊥ −.12; 7fe4): 10.753/11.439/10.523/11.421**; z6 (z1 + β S5T1 ⊥ −.04)
  10.414/11.731/10.977; z2 (U −.35, −.17) 10.513/11.340/10.474; z4 (U −.40, S5 −.07, α S2T1 ∥ .15)
  11.072/10.827/10.103; z5 9.841/10.904/10.341; z3 (U −.30, −.22) r56 FAIL. conv46 within 0.2 % of r46.
- J23: combine z1 with α S2T1 ∥ .15, finer transfer point, β S5T1 ⊥ −.03, β S5T2 c60 .02.
- Then: matched-density control on the final best, update claim, swarm done. Budget 444 + 5 = 449.

## 23:14 — wakeup 38: e5 min 11.38; J24 (5)
- J23: **e5 (U −.35, α S5T1 ⊥ −.12, α S2T1 ∥ .15, β S5T1 ⊥ −.03; 772a): 11.563/11.999/11.384/11.983**;
  e1 (same without β change) 11.711/11.397/10.764; e3 10.631/11.619/10.938; e2 10.717/11.439/10.549;
  e4 (β S5T2 c60) 11.375/10.753/10.270.
- J24 around e5: β S5T1 −.04, β S5T2 c60 .02, U −.30 + α S2T1 ∥ .20, U −.325 + S5 −.145, β S3T1 c30 .04.
- Budget 449 + 5 = 454; then control (3) + claim + done.

## 23:50 — wakeup 39: f4 min 11.52 (final best); e5 control 0.97; f4 control submitted
- J24: **f4 (U −.325, α S5T1 ⊥ −.145, α S2T1 ∥ .15, β S5T1 ⊥ −.03; 0590): 11.652/12.154/11.518/12.129**;
  f1 (β S5T1 −.04) 11.335/12.397/11.633; f3 11.799/11.569/11.157; f5 11.352/11.985/11.295;
  f2 12.138/11.213/10.970. Gains now ~1 % per round → stopping the ascent.
- e5 control (918e): 0.976/0.973/0.972 → beyond-M2. f4 control submitted; then final claim + done.

## 00:26 (Oct 15) — wakeup 40: FINAL
- f4 control (b2ea): 0.979/0.976/0.976 → beyond-M2. Final claim 6519 (f4 0590: 11.652/12.154/11.518/12.129).
- Coverage addendum 1d7d. `swarm done` with summary work/done.md. Budget 460/500 used.
