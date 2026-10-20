# ctrl-a notebook

Started 2026-10-13T18:08:59+00:00.

## 2026-10-13 18:17 — wakeup 1: setup + phase A submitted
- Read brief, docs 40/46, theory §6.4, notes §5.6–5.9, §8.3–8.5, kdep_envelope.py.
- Tools in work/: stars.py (120° basis shells), c6.py (C6 orbits: (m,n)->(m-n,m)), mk.py (build input from
  terms [[S, T, alpha, beta]]; S/T = |G|^2 or |R|^2 value or explicit star list; g_cutoff 8, n_mesh 48), gen_A.py.
- Key prior (doc 46, Nk=21, w3): alpha[S1,T1]=+0.05 -> +1.85 %, -0.05 -> -9.0 %, beta +0.05 -> -4.4 %.
- Symmetry idea: mirror∘TR => R(beta) = R(-beta) in TL for mirror-symmetric stars (phase only 2nd order);
  chiral C6 orbits of 12-member shells (|G|^2=7,13,19,21) allow linear beta. Nk=21 cluster may be chiral.
- Posted hypothesis 0860 (family w3-map), submitted 78 single-product requests (A_w3).
- Next: collect map -> fit linear/quadratic per direction -> combine positive directions (local model / CMA) -> w2.

## 18:37 — wakeup 2: phase A results; phase B submitted
- Phase A done (78 charged). Table: `uv run ... python work/collect.py [filter]` (cache work/show_cache.json; slow ~2 s/req, run in bg).
- Only gains: a[S1,T1]=+0.1 (7d9d: s21 1.033, r46 1.048, r56 1.042 PASS -> SUGGESTIVE), a[S3,T1]=+0.1 (4ee8: 1.018).
  T3/T4 momentum stars and |G|^2>=7 shells harmful; all phase harmful; beta symmetric (mirror∘TR confirmed); chiral A/B mirror equal.
- Parent gaps: w3 s21 4.571e-4, r46 4.382e-4, r56 4.552e-4.
- Posted result (w3-map coverage) + hypothesis a4b7; submitted 16 (B_w3): S1T1 a 0.15..0.6, S3T1 a 0.15..0.45, S1+S3 grid, S4 admix.
- Next: find optimum along S1/S3, then local refinement (add small S4, S7, T3 with S1 etc.), then w2 map (cheaper: T1 only).

## 18:50 — wakeup 3: phase B in, phase C submitted
- S1T1 line (s21): .05 1.0185(doc46) | .10 1.0330 | .15 1.0323 | .20 1.0198 | .30 0.965 | .45 0.820 | .60 0.587. Peak ~0.12 on s21.
  r46 grows faster: .10 -> 1.0476, .15 -> 1.0628 (54c3). Cluster-dependent curvature; s21 is the binding constraint.
- S1 .2 + S4(seed shell |G|^2=4) -0.05 -> s21 1.0350, r46 1.0824 (a68e) — best so far. S4 negative helps.
- S3T1 alone: .1 1.018, .15 0.991, .2 0.935; S1+S3 not additive (0.1/0.1 -> 1.0076). Drop S3.
- Phase C (16, w3-T1amp): grid S1 {.15,.2,.25} x S4 {-.05,-.1,-.15} + small admixtures (S12,S16,S9,S7,S1T3) at S1=.15.

## 19:05 — wakeup 4: phase C in -> first robust-level candidate; phase D submitted
- a0c5 = S1T1 .15 + S9T1 -.05: s21 1.0676, r46 1.0883, r56 1.0736 (all PASS) -> passes robust thresholds on r46/r56; conv46 pending.
- Other admixtures at S1=.15 (base 1.0323): S1T3 -.03 -> 1.0541 (9998), S7 -.03 -> 1.0483 (88f8), S4 -.05 -> 1.0379 (3f92);
  S7 +.03 0.978, S12 -.05 1.005, S16 -.05 0.996, S1T3 +.03 1.005. S4 grid: more negative S4 worse; S1 .25 worse than .15/.2.
- Phase D (20): combos of S9/S1T3/S7/S4, S9 line (-.1,-.15), S1 at .1/.2 with S9, new probes S13,S3,S1T4,S9T3,S3T3,S21.
- w3-T1amp used 52 of ~80 declared; will post updated hypothesis before going further (CMA-ES in ~6-8 dims).

## 19:21 — wakeup 5: ROBUST POSITIVE (a0c5) claimed; control submitted
- a0c5 (S1T1 .15, S9T1 -.05): s21 1.0676, r46 1.0883, r56 1.0736, conv46 1.0882 -> ROBUST_POSITIVE. Claim post fd8a.
  Also robust: 88f8 (S7 -.03) conv 1.0674/r56 1.0567; 3f92 (S4 -.05) r56 1.0543.
- Phase D: fbe3 (S1 .2, S9 -.05) s21 1.0731 r46 1.0953; 6307 (S1 .2, S9 -.1) s21 1.0437 r46 1.1311 (!); cb63 (S1 .15,S9 -.1) r46 1.1216;
  986a (S9 -.05 + S1T3 -.03) s21 1.0709 r46 1.0828. New positive admixtures at S1=.15: S1T4 -.03 (1.054), S3T3 -.03 (1.047),
  S9T3 -.03 (1.040), S21 -.03 (1.024). r56 for these pending.
- Matched-density control: work/matched.py -> BZ-avg normalized density ≈ parent (M2 3.6229). Submitted control 69b9 (s21,r46,r56).
  M2-scaled parent (λ=1.0188) inadmissible (min rho -0.014). Request fffe to human for the right control definition.
- Next: wait for r56 of phase D, then strong-target search (r46/r56 >= 1.10). s21 must stay >= 1.02 for promotion.

## 19:32 — wakeup 6: control in, phase E (w3-local Sobol) submitted
- Control 69b9 (BZ-avg density static): s21 0.9933, r46 0.9990 (r56 pending) -> averaged density gives no gain.
- r56 now: fbe3 1.0720 (robust, conv 1.0953), 986a 1.0699 (robust), 13eb 1.0630 (robust), 6307 r56 1.0782 but s21 1.0437/r46 1.131.
  r56 is usually 1–5 % below r46; it is the binding cluster for STRONG (>=1.10).
- Hypothesis 406a (w3-local); 28 submitted (E_w3: 24 Sobol in 9-D box + centre + 3 all-in). Design saved work/inputs/E_design.json.
- Next: regress s21/r46/r56 on the 9 dims (all w3 data near base), step along grad of min(r46,r56).

## 19:52 — wakeup 7: phase E in (rugged), w2 transfer submitted
- E: centre 0.963 (!); spread 0.65–1.088 on s21 — admixtures not additive, landscape rugged at s21.
  Best: sob00 (4b63) s21 1.0877 r46 1.0835; sob12 (fb8d) s21 1.0829 r46 1.1160; allin_c (46da) 1.0807/1.0794;
  sob11 (c58f) 1.0623/1.1006; sob15 (37a1) 1.0249/1.1295. r56 pending for those.
- work/fit.py: r46/r56 local quadratic fits (rms 0.003–0.004) — r56 in (S1,S9) alone maxes ~1.08 near S1 .18, S9 -.086.
  Need r56 data in other dims (pending from E promotions) to see a way to 1.10.
- Submitted w2-T1amp (16, hypothesis posted) to test transfer.

## 20:08 — wakeup 8: w2 map in; E r56 still queued (since 19:40)
- w2 (s21, α=±0.1 ×T1): S1 −: 1.0258 (aafa, r46 1.0803) | S1 +: 0.876 (opposite sign to w3, as doc46 hinted);
  S4 +.9955/−.797, S3 +.990/−.975, S7 +.984/−.859, S9 +.807/−.886, S12 .90/.90, S1T3 −.1: .959; w3 copies bad (S1 .15: .784).
  => the useful sign flips with parent; w2 has negative weights on |G|^2=3,9.
- Submitted W2B (15): S1T1 −.05/−.15/−.2, S1 −.1 + {S9 ±.05, S4 +.05, S3 ±.05, S7 ±.03, S12 +.03, S1T3 ±.03, S1T4 ±.03}.
- E r56 promotions all SUBMITTED but not run yet (broker queue); waiting.

## 20:31 — wakeup 9
- w2 S1T1 line (s21): −.05 1.018, −.1 1.026 (aafa: r46 1.080, r56 1.041 suggestive), −.15 1.024 (r46 1.101), −.2 1.013.
  With S1 −.1: S3 +.05 1.0269 (d139: r46 1.083, r56 1.043 SUGGESTIVE), S7 +.03 1.024 (r46 1.096), S12 +.03 1.021,
  S1T4 ±.03 ~1.023; S9 ± bad, S1T3 bad. w2 s21 ceiling ~1.03 so far.
- W2C (8): combos S1 −.1/−.15 with S3 +.05, S7 +.03, S12 +.03.
- E-phase r56 still SUBMITTED since 19:41 (w2 r56 done meanwhile) — if still stuck next tick, post a note/request.

## 20:49 — wakeup 10
- W2C: f193 (S1 −.1,S3 +.05,S7 +.03) s21 1.0253 r46 1.0976; a827 (S1 −.15,S3 +.05) 1.0251/1.1025; S3 +.1 1.0226; +S12 1.0199.
  w2 s21 plateau ~1.025–1.027; r46 up to 1.10; r56 known only for aafa 1.041, d139 1.043.
- 37 r56 promotions pending; E ones SUBMITTED >1 h -> posted request 2a59 (human) about queue latency.
- Phase-only reasoning: all β probes at 0.1 negative and quadratic (mirror∘TR); chiral linear term too small (est. optimum +0.3 %). Not pursuing.

## 21:16 — wakeup 11
- r56 queue still stalled since ~20:10 (no new r56). Robust list grew: 6307 (S1 .2,S9 -.1) conv 1.131, r56 1.0782; fa0c (S9 -.05,S7 -.03) r56 1.0701.
- NOTE alpha flatten order in mk.py is spatial-major (S1:[T1,T3,T4], S9:[T1,T3], ...), not E_design dims order.
  E top points decoded: sob12 S1 .212,S9 -.075,S1T4 -.027,S4 -.029 -> r46 1.116; sob15 S1 .177,S9 -.101,S1T4 -.041,S7 -.025,S3T3 -.029 -> r46 1.1295.
- Submitted F_w3 (10, w3-local; family total 38): S1 .18–.25, S9 -.075..-.125, S1T4 -.03..-.045 (+S1T3/S4/S7/S3T3 variants).

## 21:45 — wakeup 12
- Phase F: f09 (S1 .2,S9 -.075,S1T4 -.03) s21 1.0978 r46 1.1133 (19d2, best s21); f01 1.0941/1.1105; f10 1.0927/1.1035;
  f04 1.0801/1.1269; f02 (S1 .2,S9 -.1,S1T4 -.03) 1.068/1.1321; f08 (S1 .25,S9 -.125,S1T4 -.03) 1.0458/1.1480 (max r46).
- r56 queue still not moving (all SUBMITTED). Withdrew 16 dominated requests (r46 < 1.09) so the r56 queue serves the best.
- Submitted G (6) refining around f09. w3-local total 44.

## 22:13 — wakeup 13
- Phase G: g2 (S1 .22,S9 -.075,S1T4 -.03) s21 1.1038 r46 1.1148 (5f6f, best s21); g1 (S1T4 -.06) 1.1013/1.1011;
  g6 (S9 -.06) 1.0994/1.1017; g4 (S1 .22,S9 -.09,S1T4 -.045) 1.0964/1.1223; g3 (S9 -.09) 1.0829/1.1249.
- r56 lane: no completions since ~20:10. Follow-up request posted. Holding new w3 screens until r56 data arrives
  (s21/r46 alone can't decide STRONG). Budget 216/500.

## 22:56 — wakeup 14: r56 lane moving again
- g2 (5f6f: S1 .22,S9 -.075,S1T4 -.03): s21 1.1038 r46 1.1148 r56 1.0856 (best r56 so far), conv pending.
- w2 robust positives: a827 (S1 -.15,S3 +.05) s21 1.0251 r46/conv 1.1025 r56 1.0515; 490f (S1 -.15) r56 1.0504.
  f193 r56 1.0479, b4e2 1.0467. Posted claim ecd0 (w2, parent-dependent; sign of α_S1 opposite to w3).
- 35 r56 still pending. Next: once r56 for F/G arrive, fit r56 model and target r56 >= 1.10 for w3.

## 23:30 — wakeup 15: many robust positives, r56 plateau ~1.09
- Best by min: g4 (4063: S1 .22,S9 -.09,S1T4 -.045) s21 1.0964 r46 1.1223 r56 1.0897 conv 1.1221 ROBUST.
  r56 values across F/G: 1.082–1.0904 (f03 S1 .2,S9 -.1,S1T4 -.045: r56 1.0904, s21 1.0728). STRONG needs r56 >= 1.10.
- r56 regression (fit.py) unreliable on confounded Sobol dims (intercept 0.971). Instead: phase H = clean ±.03 coordinate
  probes at g4 on S3T3,S9T3,S1T3,S4T1,S7T1,S3T1 + S1T4 -.06 + S12/S16 +.03 (15). w3-local total 59.

## 00:12 (10-14) — wakeup 16: H probes give the r56 gradient at g4 (r56 1.0897, r46 1.1223, s21 1.0964)
- per ±.03: S1T3 +.03 -> r56 1.0950 (4418, robust), -.03 1.0797 | S3T3 -.03 1.0920 (s21 1.1095), +.03 1.0841 |
  S3T1 +.03 1.0915 (s21 1.1101, r46 1.1303), -.03 1.0836 | S9T3 +.03 r56 1.0998 BUT r46 1.0852, s21 1.080; -.03 s21 1.0126 |
  S4T1 ±: 1.0876/1.0865; S7T1 ±: 1.0854/1.0788; S12 +.03 1.0883; S16 +.03 1.0866; S1T4 -.06 1.0893.
- Batch I (8): combos S1T3 +, S3T3 −, S3T1 +, S9T3 +(.015/.03) on g4; linear estimate r56 ~1.10, r46 ~1.11.
- w3-local total 67/80 declared; will post an updated hypothesis if I go beyond 80.


## 00:55 — wakeup 17: STRONG reached (w3)
- 157e (i7 = g4 + S9T3 +.015): s21 1.1101, r46 1.1130, r56 1.1076, conv 1.1128 -> STRONG. Claim 7afd.
  Also strong: 97ca (i1) 1.1171/1.1299/1.1050; 2d98 (i2) r56 1.1148; bde7 (i4); b5b3 (i8).
- Control 7d8d (BZ-avg density for 157e) submitted. M2-matched static controls all inadmissible (w3 on positivity boundary);
  request posted to human (choose a definition).
- Next: (1) push min further (maybe ~1.12) around i1/i2/i7; (2) w2 strong attempt using the same recipe (signs flipped);
  (3) coverage/result posts. Budget 242/500.
- (stray ../NOTEBOOK.md created by a bad cd; merged here and removed. Use absolute paths.)
- Hypothesis c34a; submitted J_w3 (18, family w3-local2, probes at i2) and W2D (12, family w2-local, probes at a827). Budget ~273.

## 01:46 — wakeup 18: J probes -> new best 7a35 (min 1.1179); controls confirm no static-average gain
- J (at i2): 7a35 (S9T1 -.11 instead of -.09): s21 1.1179 r46 1.1278 r56 1.1219 conv 1.1274 STRONG (best).
  a841 (S7T1 -.03) min 1.1134. 13 of 18 probes STRONG. Gradients: S9T1 − big +; S7T1 − +; S1T3 − small +; S1T1 − small;
  S9T3 − helps s21/r46 but hurts r56; S1T4 + helps r46; S3T3 + helps r46; S3T1 + helps r46/r56.
- Controls (BZ-avg density static): 7d8d (for 157e) s21 0.9845 r46 0.9961 r56 0.9938; 69b9 (a0c5) 0.9933/0.9990/0.9987.
- W2D (at a827): 7100 (S3T3 -.03) robust 1.0304/1.1058/1.0547; ea01 (S9T3 +.03) robust r56 1.0611; S1T4 -.03 r56 1.0466.
- Submitted K_w3 (8, step from 7a35) and W2E (6, step from a827). Budget ~283.

## 02:16 — wakeup 19
- K: k3 (6bbe: S9T1 -.13) s21 1.1248 r46 1.1423 r56 1.1222 (conv pending) best; k2 (bce3) 1.1181/1.1509/1.1197; k6 (7119) STRONG conv 1.1509 min 1.1134.
- W2E: no improvement (best r56 1.061; S9T3 +.06 collapses s21). Closed w2: result 8ff0 with coverage (57 req).
- Submitted L (7) step from k3. w3-local2 total 33.

## 03:05 — wakeup 20
- L: l1 (ca2c: k3 + S1T4 +.02 + S3T1 +.02) s21 1.1257 r46 1.1569 r56 1.1281 conv 1.1565 STRONG — new best min 1.1257.
  l5 (S1T3 -.02) 1.1289/1.1490/1.1231; l6 1.1212/1.1600/1.1245; l3 r46 1.172.
- NOTE: digest grep -v "_req_" hid post lines; use sed on the posts section instead.
- Hypothesis M posted; submitted M_w3 (14) + P_w3 (4, β on winner, family w3-phase). Budget ~308.

## 03:52 — wakeup 21: round 3 gains only +0.3 % -> final combined step
- M at l1 (1.1257): d3ca S3T1 +.02 -> 1.1288 (r56 1.1314, conv 1.1605); 8d80 S1T3 -.02 1.1283; 34c1 S12 +.02 1.1274; 5992 S7 +.02 1.1267.
  Negative: S9T1 -.02 (1.1154), S7 -.02, S16 -.02, S1T4 +.02, S12 -.02, S3T3 +.02.
- Phase on l1: β[S1,T1] ±.03 -> 1.1243/1.1156 (no linear term, as expected; ±0.9 % s21 asymmetry = cluster chirality).
  Chiral β[S7A,T1] +.03 -> s21 1.1194, r46 1.1781 (+2.1 %), r56 1.1284; −.03 -> 1.0919/1.1519/1.0997: a real linear phase effect, mostly on r46.
- Submitted N (7): n1 = l1 + S3T1 +.02 + S1T3 −.02; n2 +S12 +.02; n3 +S7 +.02; n4 = n1 + chiral β .015; scale n1 × {0.9,1.1,1.2}.
- Plan: after N, stop refinement; final claim update, matched control for the final best, coverage posts, done.

## 04:39 — wakeup 22: N results; new best fd01 includes a chiral phase
- n1 (ce25: l1 + S3T1 +.02 + S1T3 -.02; amplitude only) 1.1347/1.1678/1.1314/conv 1.1674.
- n4 (fd01 = n1 + β[S7A,T1] +.015): s21 1.1358 r46 1.1768 r56 1.1352 conv 1.1764 -> best min 1.1352.
  The β increment (same M2^(k) 3.92) gives +0.1/+0.8/+0.3 % on s21/r46/r56: a clean beyond-M2 piece (β leaves |h_k|^2 unchanged).
- n2 (+S12 .02) 1.1340; scale line ×0.9 1.1302, ×1.1 1.1291, ×1.2 1.1214 -> amplitude optimum ≈ ×1.0.
- Submitted Q (6, family w3-phase): β on S7A at .0075/.0225, S7B −.015 (mirror partner), S13A ±.015, n2+β.
- Control 82c5 for fd01 (BZ-avg density ×0.99 off-zero for positivity).

## 05:26 — wakeup 23: local optimum ~1.135; phase-only test submitted
- Q: chiral β saturates: S7A .0075 1.1342, .015 (fd01) 1.1352, .0225 1.1332; S7B −.015 1.1349 (s21 1.1394; mirror pair ok);
  S13A −.015 1.1294, +.015 1.1205; n2+β (c12e) 1.1352 (r56 1.1377, conv 1.1800).
- Control 82c5 (fd01 BZ-avg density static): s21 0.9681 r46 0.9833 r56 0.9785.
- Submitted R (12, w3-phase-only, hypothesis posted). After R: final claim/result/coverage posts and `swarm done`.

## 05:58 — wakeup 24
- R (phase-only chiral on parent, α=0): all 12 < 1 at s21 (best β[S7A,T1] +.02: 0.9966; −.04: 0.904). Null at s21 for phase-only.
- Submitted S (32, w3-global): 10-D Sobol around parent, to check for a second basin. Then wrap-up.

## 06:17 — wakeup 25: S (global, 32) all in flight, none finished after 18 min; waiting. Then final posts.

## 06:55 — wakeup 26: global check done; final result posted; directional probes
- S (global 32): only glob17 > 1.02 (s21 1.0365, r46 1.098; α_S1T1 +0.12, same basin). 6 FAIL. No second basin.
- Posted final w3 result cb1f with 5 coverage blocks.
- T (8, w3-directional): joint-orbit cos·cos pairings (perp / ±30° chiral pair) on fd01; pair-star amplitude .015 ≈ 20 % of per-pair S1T1.
  (gen_T.py; first draft at .05 was too large: m2k 1.14.)

## 07:41 — wakeup 27: DIRECTIONAL BREAKTHROUGH
- T on fd01: perp pairing (S1 G-axis ⟂ T1 R-axis, 3 two-member pair-stars) +0.03 -> s21 1.2019 r46 1.2193 r56 1.1921 (4a49);
  +0.015 -> 1.1640 min; plus/minus −0.015 -> ~1.151 (chiral pair agree); plus/minus +.015 lose; perp − loses.
- glob17 robust (r56 1.052) — same basin.
- Submitted U (11): perp .045/.06/.09, perp+plus/minus−, perp-only (S1T1=0, perp .15/.2), S9 perp ±.02, S3 aligned ±.02 on perp .03.

## 08:30 — wakeup 28: perp-only joint orbit -> R ~1.46
- U: u7 (fd01 − S1T1 sep + perp .20): s21 1.4670 r46 1.4964 r56 1.4565 (33a8); u6 perp .15: 1.3904/1.4032/1.3685 (875a);
  u3 (sep+perp .09) min 1.2804; u2 .06 1.2453; al3 +.02 1.2341; perp9 −.02 s21 1.2196 r46 1.2615. 4a49 conv46 1.2188 (STRONG, min 1.1921).
- Submitted V (10): perp-only .25/.3/.4/.5, pure perp .2/.3, combos with al3 / perp9 / plus-minus.

## 09:18 — wakeup 29: perp-only STRONG ~1.46 converged; claim 0dd7
- 33a8 (u7) conv46 1.4958 -> STRONG min 1.4565. 875a (u6) STRONG conv 1.4029. Many U points STRONG (u1..u5, al3, perp9).
- V: b2a3 (u7 + perp9 −.04) s21 1.4928 r46 1.5463 r56 1.5061 (conv pending) — best; 705a (al3 +.04) min 1.4766;
  perp .25 s21 1.4487 r46 1.4555; .3 1.33; .4 r46 0.90; .5 FAIL (m2k 2.59) -> optimum ~0.2–0.25.
  pure perp .2 (nothing else) s21 1.3693 r46 1.3857 (7772).
- Control 4153 (BZ-avg, ×0.97). Request posted for N_A=3 PES / M2-matched control / finer convergence.
- Submitted W (8) refinement around b2a3. Budget ~406.

## 10:07 — wakeup 30: perp-orbit family keeps climbing
- W: 8044 (perp1 .2, perp9 −.04, al3 +.04; + fd01 rest w/o sep S1T1) s21 1.5579 r46 1.5998 r56 1.5604 conv 1.5985 STRONG — best.
  973d (perp1 .225, perp9 −.06) 1.5393/1.5885/1.5496; 064b 1.5183; 59df/9490 ~1.506; b2a3 conv 1.5457 (min 1.4928).
  perp-only scan converged: .25 min 1.4322; .3 1.2391; pure .2 1.3060 (r56); pure .3 1.0755.
- Control 4153 (33a8 BZ-avg density static): 0.9701 on all three clusters.
- Submitted X (8): combine 973d+8044 directions; new pairings perp4 (|G|²=4 ⟂ T1) and al12 (|G|²=12 ∥ T1) ±.02. Budget ~414.

## 10:26 — wakeup 31
- X (s21/r46; r56 pending): x4 (perp1 .225, perp9 −.06, al3 .06) 1.6138/1.6365 (a943) best; x1 1.5972/1.6290; al12 +.02 1.5967/1.6261;
  x2 1.5903/1.6357; perp4 −.02 1.5678 (+), +.02 1.5494 (−); al12 −.02 1.5277 (−).
- Submitted Y (8) step from x4. Budget 422/500; keep ~30 for final checks/controls.

## 11:13 — wakeup 32
- Y: y2 (perp1 .225, perp9 −.06, al3 .06, al12 .04) s21 1.6941 r46 1.6880 r56 1.6838 conv 1.6853 STRONG (62c2) — best.
  y7 (perp9 −.08) 1.6536; y8 1.6491; y1 (al12 .02) 1.6370; x4 conv 1.6346 min 1.5975.
- Submitted Z (7: al12 .06/.08, perp9 −.08 combos, perp16 ±.02) and W2F (6: perp orbit on w2, both signs). Budget ~435.

## 12:01 — wakeup 33
- Z: z4 (perp1 .225, perp9 −.08, al3 .06, al12 .06) s21 1.7787 r46 1.7449 r56 1.7875 conv 1.7402 STRONG (443f) — best.
  z3 1.7265, z7 1.7149, z2 (al12 .08) 1.7128 (s21 1.7986), z1 1.7037, z6 (perp16 −.02) 1.6979, z5 (perp16 +.02) 1.6378.
- W2F: perp orbit on w2 loses at both signs (0.80–0.94) -> w3-specific (parent-dependent).
- Submitted AA (8) from z4. Budget 443/500; reserve ~15 for final control (+ maybe 1 more round).

## 12:49 — wakeup 34
- AA (s21/r46; r56 pending): a7 (perp9 −.10, al12 .08, perp16 −.02) 1.9263/1.7900 (361a); a2 (perp9 −.10) 1.8034/1.7669;
  a1 (perp16 −.02) 1.8548/1.7593; a5 (al3 .08) 1.8041/1.7572; a6 (perp4 −.02) 1.8120/1.7530; a3 (al12 .08) 1.8213/1.7506;
  a4 (perp1 .25) and a8 (S9 sep −.08) worse than z4 on r46. Note m2k falls (1.29) while R rises -> less M2-driven.
- Submitted AB (6) from a7. Budget 449/500.

## 13:37 — wakeup 35
- AB: b6 (perp9 −.12, al12 .10, perp16 −.04, perp4 −.02, al3 .08) s21 1.9461 r46 1.8418 r56 1.9108 conv 1.8353 STRONG (5d86) best;
  b1 s21 2.0044 r56 1.9552 but r46 1.8179; a7 conv 1.7846. r46/conv46 is the binding cluster now.
- AC (6) submitted. NOTE Σ|α| now 2.10–2.22, campaign boundary 2.5 (each pair-star counts) -> approaching boundary.
- Budget 455/500.

## 14:24 — wakeup 36
- AC: c2 (al3 .10) s21 2.0673 r46 1.8622 r56 2.0003 conv 1.8551 STRONG (f8ea) best; c3 1.8519; c4 (perp1 .25) r56 2.01 but conv 1.8187.
  Gains now ~+1 %/round; Σ|α| 2.1–2.2 of 2.5.
- Last step AD (4) from c2 + matched control for f8ea (BZ-avg ρ̄ has M2 3.480 < parent; ×0.95 for positivity).
- Plan: when AD done -> final claim/result update with coverage for directional family, then swarm done.

## 15:14 — wakeup 37
- AD (s21/r46; r56 pending): d3 (al3 .12, perp9 −.14) 2.1103/1.8964 (9ebb); d2 1.9519/1.8748; d1 2.1178/1.8736; d4 (al12 .12) 1.9804/1.8538.
- Control 269d (c2 BZ-avg density ×0.95): 0.9187/0.9195/0.9195 -> averaged density gives LESS than parent.
- Submitted AE (6) from d3; Σ|α| up to ~2.4. Budget 468/500. After AE: final posts + done.

## 16:02 — wakeup 38: final round in; claim c49c posted
- AE: e1 (3e8d: perp1 .225, perp9 −.16, al3 .14, al12 .10, perp16 −.04, perp4 −.02 + fd01 rest) s21 2.1094 r46 1.9265 r56 2.1386 conv 1.9183 STRONG — FINAL BEST.
  Σ|α| 2.335 (boundary 2.5). Gains ~1.5 %/round now.
- Control 7b08 for 3e8d submitted (BZ-avg ×0.926). (builds-on id was mistyped; real best id 20261014T151428.413Z_ctrl-a_req_3e8d.)
- Claim/result c49c with coverage for directional family + w2 directional.
- Next: wait for control 7b08, then `swarm done` with summary. Budget 471/500 (29 unused, reserve).

## 16:43 — wakeup 39: DONE
- Control 7b08 (3e8d BZ-avg density static): 0.8822/0.8836/0.8836.
- Ran `swarm done` with final summary (work/posts/done.md). 471/500 charged.
