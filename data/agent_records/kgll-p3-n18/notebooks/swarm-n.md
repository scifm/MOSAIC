# swarm-n notebook

Started 2026-10-14T05:20:30+00:00.

## 2026-10-14 05:35–05:52 — wakeup 1: survey, scope, trgrad iteration 1a

**Board state.** Families taken: linmap (a), jorbit (b), jointorb (c), chiphase (d), sharpen/bigamp/bigstep (e,f,h),
comove P_n (i), phasequad (j), outerjo/outerorb S4-S10xT1 (k,m — duplicate), nematic C3-breaking (o),
matched-density controls (a mdctl, q m2ctl, l), pooled-surrogate BO (p), cross-family integration (l).
I first built an outer-shell joint-orbit map (work/orbits.py, gen_stage1.py, s1/) but swarm-k posted the identical
plan 3 min earlier -> not submitted.

**Key numbers (s21 unless noted).** P1 = S1xT1 self-mirror (G perp R) alpha/entry: -0.06 1.20 (r46 1.204), -0.25 1.47,
-0.35 1.48 FAIL (splitting/D 0.108 only), -0.5 1.882 PASS (r46 2.650 PASS; M2k 9.34, flatter than parent) = swarm-i req_9de1.
d's S5T1 mirror-odd beta 0.0204/entry: 1.614 (r46 2.218). c's S3T1 P -0.06: 1.368. Matched-density controls of c5b8/f721: 0.999.
s21->r46 consistent in sign for every promoted point so far (often r46 larger).
Outer-shell orbits at small amplitude are cliffs (R~2 but FAIL).

**Check I did (no evals).** work/trunc.py: kernel weight outside the g_cutoff=8 box is <=1e-6 for all PASS leaders;
2-7 % only for f's S10xT1 alpha=0.3 product (FAIL anyway). Not worth a post on its own.

**My family `trgrad`** (hypothesis 20261014T055102.608Z_swarm-n_hypothesis_a5b4): central-difference gradient AT the incumbent
(P1 alpha=-0.5) in 30 MT-allowed directions (tr.py: P_a, M_a = A+B alpha, O_b = A-B beta on S1-S3xT1-T3; O_b on S5/S6/S8xT1).
Steps 0.04 alpha, 0.015 beta (0.01 outer). it1a (30 evals) submitted 05:51; it1b (30) waiting in work/it1b for in-flight room.
Mailed swarm-i, swarm-p.

**Next.** Submit it1b when in-flight < 2. Fit gradient (R(+)-R(-))/2step and curvature; trust-region step + line search;
objective min over s21/r46/r56.

## 06:08–06:14 — wakeup 2: it1a results, it2 submitted
- it1a (30 evals, table in result post 20261014T061325.361Z_swarm-n_result_08fc): at P1 -0.5 the response is a level-crossing
  plateau, s21 ~2.75 / r46 ~3.5 in 6 directions. Mirror-odd beta: one sign gives the plateau with sp<=0.005, the other FAILs on
  splitting (sp 0.10-0.12). Best of mine: S3T1 A+B alpha +0.04 (41dd) 2.880/3.092; S3T1 A-B beta -0.015 (1757) 2.781/3.569.
- The board leader is swarm-r ac14 (small combined cross-family steps: S1T1P -0.06, S3T1P -0.06, S2T1P +0.06, S2T1 X beta, S5T1 X beta 0.0204)
  at 4.443/4.935. Herd around ac14: r (xsector), h (josobol Sobol), p (poolbo), l. I stay in the large-P1 basin as a diverse basin.
- Many families have been abandoned: product stars at large amplitude all FAIL (e,f,h,j,a); outer joint orbits xT1 FAIL (k,m).
- it1b shelved. it2 (16 evals; gen_it2.py) submitted 06:13: combos of the alpha winners {S2T1 P, S2T1 A+B, S3T1 A+B} and the
  beta winners {S1,S2,S3,S5 T1 A-B} at t=0.5/1/1.5, plus pairs and 2x singles.
- Tools: mine.py (my requests by dir), pool.py (slow; all requests -> coords).
Next: read it2. If the combos stay capped at ~2.75, the large-P1 basin is inferior; abandon it with coverage, and consider
verifying/critiquing ac14-type leaders (MT partner, r56) or re-centring on the best leader.

## 06:29–06:32 — wakeup 3: it2 breaks the plateau; it3 line search
- it2 (s21): AB_t0.5 4.223, AB_t1 5.632, AB_t1.5 5.669 (all PASS, sp<=0.004); B (phase-only beyond P1) t0.5/1/1.5 = 3.26/4.57/5.35;
  A alone t0.5 2.665, t1 2.12, t1.5 FAIL. Pairs: S3M+S3O 3.95, S3M+S2O 3.75, S2P+S3O 3.54. So the plateau was a crossing; combos are
  ~multiplicative (matches r's X1 finding: log R additive, split/D is the binding gate).
- Board: r b55a s21 10.91, h 53df 8.75 (josobol). Values >> 1.1. a's qgeom: the P1 family = Berry-curvature flattening;
  ac14 is not (finite-q mechanism). f's kconv: the top 9 are kernel-converged. Controls (l, a, q): averaged density explains none of the gain.
- Constraint: Sigma|alpha| <= 2.5 binds in my basin (P1 -0.5 uses 1.5; A adds 0.6 per unit t). it3 (9 evals): B t=2,3,4; A1+B2/3;
  reduced P1 (-0.4/-0.3/-0.2) with A,B at t=2-3.
Next: read it3; keep climbing where it rises. Consider verifier work on the top leaders (r56, PES N_A=3, sign checks).

## 06:47–06:52 — wakeup 4: it3 results; audit; stacking on b55a
- it3: A1_B2 (P1 -0.5, A t=1, B t=2) f5ad s21 6.758 / r46 7.345 PASS = my best (#6 on the board). A1_B3 5.81/6.91. B t2 5.32, t3 3.35, t4 FAIL.
  Reduced P1 (-0.4/-0.3/-0.2 with larger A, B) all FAIL (splitting). The P1 basin caps at ~6.8 (s21).
- Board: r b55a = 3x ac14 (P entries 0.18, beta 0.061), s21 10.91 / r46 11.39 / r56 11.16 PASS. Claims so far: b strong (phase-only
  ec27, 1.15), r strong (ac14, 4.4-4.9). Leaders: r and h (josobol).
- Posted audit note f97a (top-25 gate margins: min EG 2.10 at N_A=3, max sp 0.048; no trap) + correction d34e (23/25, not 21/25;
  ALWAYS compute derived stats before posting).
- st1 (11 evals): stack my levers (S1T1/S3T1 A-B beta, S2/S3 A+B alpha, extra P1) on b55a, plus a replica of b55a through my mapping
  (expect 10.912). Mailed swarm-r.
Budget: 75/500 after st1 (64 + 11).

## 07:07–07:11 — wakeup 5: stacking null; chiral E+ test
- st1 (11): b55a is a local max along every P1-basin lever (best bf4e P1 -0.05: s21 10.981 / r46 11.379; others lower).
  Replica 8559 = b55a exactly (pair map validated). S3 A-B beta x2 cancels the s21 splitting (0.000) at -3 %.
  Result post f223 with coverage.
- Board: r's line along ac14 saturates (t=4 11.07 F split). h c954 s21 11.33 (confirm pending). k: gain is ONE chiral l=2 field
  E+ = e^{+2i theta_GR} (signed G->R angle); E- is inert but adds splitting. a: e2 pair-channel proxy predicts R (R2 0.97).
- chiral.py: per-block l0/E+/E- fit (exact on 6x6 blocks). b55a: E+ positive real on S1,S2,S3,S5 (0.060, 0.131, 0.060, 0.071).
  A single P orbit = l0+E++E- equally.
- chi1 (5 evals): b55a E+ only x1 (e949), x1.25 (9770); b55a minus E- (6c29); uniform E+ lambda 0.08 (fecb) / 0.10 (5eab).
  Sigma|alpha| binds at ~1.3x E+ (the full field fills 9 cells/block). Mailed k.
Budget after chi1: 82/500.
Next: if E+-only beats b55a or lowers the splitting at equal R -> scale within the boundary, maybe trade alpha for beta
(rotate the E+ prefactor phase? untested and physically distinct, not an equivalence). Otherwise close trgrad with coverage.

## 07:26–07:31 — wakeup 6: E- removal works
- chi1 (s21, screen): b55a minus E- (6c29) 12.940 (b55a 10.912); uniform inner E+ 0.10 (5eab) 12.381, 0.08 (fecb) 11.748;
  bEp x1.25 (9770) 12.283; bEp x1 (e949) pending. Confirms k's E+ picture at large inner lambda.
- Board leader: k 3bd0 = pure outer E+ (S4-S10 x T1, z-lambda 0.016, Sigma|alpha| 1.0): s21 13.58 / r46 13.11.
  r 0f3b inner+outer 12.17. bf4e (mine, b55a + P1 -0.05) reached conv46 11.408 PASS; r56 11.039.
- l0 is expensive in Sigma|alpha| (real on all 9 cells). chi2 (6): noEm x1.15 (b880), noEm l0x0.5 (d3ce), noEm+outer 0.004
  (f5f3), inner 0.06+outer 0.008 (c092), same + b55a l0 (3f5f), inner 0.04+outer 0.012. Mailed k, r.
- Gotcha: gen_chi2 runs at import -> regenerated a rejected file; the batch rejected it (no charge). Guard module code next time.
Budget: ~93/500 after chi2.

## 07:46–07:51 — wakeup 7: chiral results; l0 ablation
- b55a-E- (6c29) 12.940 / 12.373 / 12.180 PASS. l0 x1 / x0.5 / x0 at fixed E+: 12.94 / 12.48 / 11.64 (l0 also lowers the s21 splitting).
- 3f5f (b55a l0 + inner E+ 0.06 + outer E+ 0.008) s21 14.699 = top screen value; f5f3 14.362; b880 13.774; 1727 13.766; c092 13.485.
- Board: k's pure outer E+ line is linear in lambda (3bd0 0.016 z-units -> 13.58/13.11). h c954 full ladder min 11.25. q: leader blocks don't
  transfer to w3/w2. g: Berry flattening is a marker, not the mechanism. i: truncation critique for the outer field at large lambda
  (f/p checking 96/14). h+k asked the human whether Sigma|alpha| is representation-dependent (pair stars 3x product). Don't exploit until answered.
- Posted result 3e2c. My niche now: the l0 component. l0a (5): 3bd0 + 0.8 l0 {as b55a, all-neg, S2 only, S1S3 only} (0667, 7ed9, 5961, 2fb9)
  + l0 + in0.05 + out0.010 (a3c2).
- mine.py now refreshes only the named dirs (fast).

## 08:06–08:09 — wakeup 8: l0 ablation -> S1/S3 negative breathing
- l0a on 3bd0 (s21 13.582): S1S3 only -0.048 (2fb9) 15.466, sp 0.004 (BEST s21 on board); b55a pattern (0667) 14.233; all neg (7ed9) 13.714;
  S2 + only (5961) 12.373. S2 l0 hurts either sign. a3c2 (b55a l0 + in0.05 + out0.010) 14.799.
- Ladder: 6c29 conv46 12.390 (min 12.18 r56), 3f5f r46 13.949, f5f3 r46 13.359, 1727 r46 13.431.
- Board: k claim STRONG 3bd0 13.58/13.11/13.10/13.30 (D1 control 1.007). p kconv2: large-lambda outer fields lose 12-30 % on r46
  (5a1c FAIL) -> watch r46 of my outer+l0 points. Many agents done (m, i, e). Split agreed: n=l0 (+E- removal), r=per-shell E+, k=12-member sub-star.
- l0b (7): S1S3 l0 at -0.03/-0.065/-0.08; S1 only; S3 only; +-S5 l0 0.016 — all on 3bd0's outer field.
Note: l0 on a 6x6 block = product star (alpha_prod = 3z), charged 9|z| as pair stars. Not exploiting.

## 08:24–08:27 — wakeup 9: STRONG claim 2fb9
- 2fb9 (3bd0 outer E+ 0.016 + l0 -0.048 on S1,S3 x T1): 15.466/14.587/14.268/14.704 all PASS, C=1, EG>=3.17, broker claim=strong.
  Claim post f783. min 14.27 > 3bd0 min 13.10 and > k's pure-field r46 saturation (~13.7).
- l0 scan: S3 only (ef19) 15.59/14.66; S1 only 13.85/13.68; S1S3 at -0.03/-0.048/-0.065/-0.08 -> 14.95/15.47/14.30/11.32;
  +S5 -0.016 (6c70) 15.72/14.47; S5 +0.016 14.58/14.24. Other ladder: 3f5f conv46 14.14 (min 13.56 r56); a3c2 min 13.72; 1727 min 13.43.
- k: pure chiral field saturates at r46 ~13.7 (lam 0.009); s21 overshoots beyond that -> optimize min, not s21.
  k posted a relabelling critique (40 strong claims = one E+ field); replied in f783 and by mail. Asked l for a D1 control of 2fb9.
- l0c (6) in flight: S3 -0.036/-0.06, S3+S5, S3+S1+S5, and on the lam 0.018 (k's 0.009) field: S1S3, S3+S5.

## 08:45–08:48 — wakeup 10: 8f40 leads; scanning around it
- D1 control of 2fb9 (l's 8c71): 0.994/0.994/0.993 -> beyond M2. f's kconv: 2fb9 holds at 96/14 (|dR/R| <= 8e-4).
- l0c: 8f40 (outer 0.018 + S3 -0.048 + S5 -0.016) s21 17.435 / r46 15.620 = board #1; d130 (outer 0.016, same l0) 16.73/14.92;
  0d51 S3 -0.06 16.20/14.88; b537 (outer 0.018 + S1S3) 16.11/14.95; 2bd5 16.39/14.78; 5175 S3 -0.036 14.99/14.34.
  l0b ladder: 6c70 min 14.47 (conv46 14.52), ef19 r56 14.61, 4a99 min 14.20.
- With breathing present, a stronger outer field helps r46 (pure field turns over at k-lam 0.009 = my 0.018).
- l0d (7): outer 0.020/0.022; S3 -0.06; S5 -0.03; +S6/S8 l0 -0.01; outer 0.020 + S3 -0.06 + S5 -0.024. Judge by min R.

## 09:06–09:08 — wakeup 11: 8f40 strong, family at optimum
- 8f40 17.435/15.620/16.021/15.978 all PASS, C=1, broker strong. Claim post 5a11 (with coverage), correction 7b8a
  (102 evals charged; 89 P / 0 A / 13 F — ALWAYS recount before posting coverage).
- l0d: every variant raises s21 (to 18.2) but r46 sits at 15.4-15.55; lam 0.022 drops (13.90). min R plateau ~15.6 -> family optimum.
- Board: most agents have posted final summaries (c, d, e, f, g, i, j, k, m, p). p's kconv2: 8f40/d130/2bd5 kernel-converged.
Next: one more wakeup to collect the l0d r56 values and swarm-l's D1 for 8f40; then final summary + swarm done.

## 09:37 — wakeup 12: wrap-up
- l0d ladder complete: mins 15.10-15.55 (de6d 13.90); 8f40 min 15.62 stays best. D1 control for 8f40 (l's c34b) = 1.005 on s21/r46/r56.
- swarm-r takes the pooled GP over the chiral profile (agreed by mail). h claimed b2b4 min 13.16.
- Posted final summary; calling swarm done. 102/500 evals charged. Claims: 8f40 (min 15.62), 2fb9 (min 14.27), both strong, D1 ~1.
