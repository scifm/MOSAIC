# ctrl-b notebook

Started 2026-10-08T04:37:46+00:00.

## 2026-10-08 ~04:58 — wakeup 1 (start)
- Read brief, docs 40, 46, notes §5.6–5.7, §12. Key prior: doc 46 Nk21 w3 alpha[S1,T1]=+0.05 -> +1.85 %, -0.05 -> -9.0 %, beta[S1,T1]=+0.05 -> -4.4 %, alpha[S3,T1]=+0.05 -> -3.75 %. LL0 response is strong and strongly curved (quadratic vertex ~+0.04, ~+2 %).
- Parents: w3 s21 Δ=4.5714e-4, r46 4.3823e-4; w2 s21 3.2272e-4.
- Built work/build.py (stars in solver 120° basis: S1..S10 spatial, T1..T3 momentum allowed).
- Posted hypothesis w3-sep (20261008T045751.625Z_ctrl-b_hypothesis_f04a): box |a|<=0.15, |b|<=0.10, budget ~150.
- Submitted batch b1 (30): ±0.03 central differences along a[S1..S8,T1], b[S1..S4,T1], a[S1,T2], a[S1,T3], b[S1,T2]. ids in work/b1_ids.txt.
- Next: fit gradient + diagonal curvature, Newton step in combined direction, then CMA-ES.

## 05:15 — wakeup 2
- ALL 30 of b1 failed: "transient failures exhausted" (~2 min after accept). 30 evals charged. Infra, not input (admissible, no reason given). Parents' r56 still pending.
- Posted request 20261008T051528.599Z_ctrl-b_request_f527 to human. Resubmitted one probe (a_S1T1p) -> 20261008T051519.572Z_ctrl-b_req_b203; budget still 30 after resubmit (maybe charged on accept?). Holding other submissions until probe returns.

## 05:23 — wakeup 3
- Probe b203 also failed (transient exhausted); budget not re-charged (still 30). Posted follow-up request. HOLDING all submissions until human answers / digest shows fix.

## 05:49 — wakeup 4
- No human reply; no new results. Still holding.

## 06:20 — wakeup 6
- Still no human reply. Submitted 1 diagnostic: zero deformation block (20261008T062015.989Z_ctrl-b_req_ac59) to tell 'lanes down' from 'deformation inputs fail'.

## 06:31 — wakeup 7
- Zero-block probe ac59 is SUBMITTED/pending after 11 min (not failing fast like b1). Waiting.

## 06:47 — wakeup 8
- Zero-block probe ac59 FAILED too (transient exhausted, after ~25 min). Not my inputs: lanes down or deformation path broken. Posted request. Holding; 31/500 charged.

## 07:18 — wakeup 9
- No human reply; no change. Holding.

## 07:59 — wakeup 10
- No change, no human reply. Holding.

## 08:45 — wakeup 11
- No reply. Re-probe lanes with the same zero block (free so far): 20261008T084511.402Z_ctrl-b_req_5c2e.

## 09:13 — wakeup 12
- Re-probe 5c2e failed again (transient exhausted). Lanes still broken; no human reply. Plan: free re-probe ~hourly, otherwise hold.

## 10:14 — wakeup 13
- No reply/no change. Hourly re-probe submitted.

## 11:15 — wakeup 14
- LESSON: resubmitting an identical input reuses the cached (failed) evaluation in seconds (charged 0) — re-probes 5c2e, 9449, b203 were NOT real tests. Only ac59 (new hash) actually ran and failed (06:20-06:32).
- Submitted a fresh-hash probe alpha[S1,T1]=+0.01 (non-diagnostic, so it promotes if it works). Each real probe costs 1 eval.

## 11:36 — wakeup 15
- Fresh-hash probe 1265 FAILED. Lanes broken ~6.5 h. Posted status request. Next real probe ~13:40 (1 eval each).

## 12:37 — wakeup 16
- No reply. Holding; real probe next wakeup.

## 13:30 — wakeup 17
- No reply. Fresh-hash probe alpha[S1,T1]=+0.02 submitted.

## 13:50 — wakeup 18
- Probe 19b2 FAILED (transient). 33/500 charged, 0 results. Next real probe ~16:00.

## 14:51 — wakeup 19
- No reply, no change. Holding; probe next wakeup.

## 15:52 — wakeup 20
- No reply. Fresh-hash probe alpha[S1,T1]=+0.04 submitted.

## 16:13 — wakeup 21
- Probe 20c1 FAILED. 34/500 charged, 0 results, lanes down ~11 h. Stretching real probes to ~every 3 h.

## 17:14 — wakeup 22
- No change. Holding; next probe ~19:15.

## 17:48 — wakeup 23
- No change. Holding.

## 18:49 — wakeup 24
- No reply. Fresh-hash probe alpha[S1,T1]=+0.05 submitted.

## 19:10 — wakeup 25
- Probe 69ce FAILED. 35/500 charged; lanes down ~14 h. Next probe ~22:00.

## 20:11 — wakeup 26
- No change. Holding.

## 21:12 — wakeup 27
- No change. Holding; probe next wakeup (~22:12).

## 22:05 — wakeup 28
- No reply. Fresh-hash probe alpha[S1,T1]=+0.035 submitted.

## 22:25 — wakeup 29
- Probe 9bca FAILED. 36/500 charged; lanes down ~17.5 h. Next probe ~01:30.

## 23:26 — wakeup 30
- No change. Holding.

## 00:27 (10-09) — wakeup 31
- No change. Holding; probe next wakeup.

## 01:28 — wakeup 32
- No reply. Fresh-hash probe alpha[S1,T1]=+0.045 submitted.

## 01:49 — wakeup 33
- Probe dcb6 FAILED. 37/500 charged; lanes down ~21 h. Posted interim result w/ coverage (0 completed). Next probe ~04:50.

## 02:21 — wakeup 34
- No change (only my own post). Holding.

## 03:22 — wakeup 35
- No change. Holding; probe next wakeup.

## 04:23 — wakeup 36
- No reply. Fresh-hash probe alpha[S1,T1]=+0.025 submitted.

## 04:44 — wakeup 37
- Probe f1ae (a=+0.025) FAILED at 04:30. BUT parents' r56 now landed: w3 r56 Δ=4.5515e-4, w2 r56 Δ=3.2164e-4 (were pending since start). So lanes run something (5x6 parent, no deformation). Either lanes recovered after 04:30 or only deformation/s21 jobs fail.
- Submitted another probe immediately: 20261009T044415.426Z_ctrl-b_req_2b80 (a=+0.015).

## 04:59 — wakeup 38
- Probe 2b80 FAILED (04:44->04:49) right after parents' r56 completed. => lanes alive; deformation-block inputs fail at s21 (zero block too). Posted narrowed request to human. No julia on PATH for local diag (diag script needs manifest/julia env) — not pursuing.
- 39/500 charged.

## 06:00 — wakeup 39
- No reply. Hypothesis: my blocks omit g_cutoff (broker shows null); doc 46 set g_cutoff=4. Probe a76c with explicit g_cutoff=4, a[S1,T1]=+0.05.

## 06:16 — wakeup 40 — ROOT CAUSE FOUND
- a76c (alpha[S1,T1]=+0.05, explicit g_cutoff=4) -> s21 R_gap 1.0185 PASS, eg 8.97. All earlier failures = g_cutoff null in deformation block. build.py now defaults g_cutoff=4.
- Posted note 20261009T061708.695Z_ctrl-b_note_bfcb.
- Resubmitted gradient screen as b1g (30, same specs as b1 with g_cutoff=4); ids work/b1g_ids.txt. work/collect.py tabulates.
- Budget after: 70/500.

## 06:38 — wakeup 41 — b1g screen results (all PASS, s21, h=0.03)
R(+h)/R(-h): aS1T1 1.0150/0.9446 (g=+1.17, H~-45) | aS2T1 1.0131/0.9530 (g=+1.00,H~-38) | aS3T1 .9846/.9928 | aS4T1 .9750/.9505 (g=+.41,H~-83) | aS5T1 .9591/.9686 | aS6T1 .9541/.9690 | aS7T1 .9454/.9249 (g=+.34,H~-144) | aS8T1 .9400/.9582 | aS1T2 .9915/.9850 | aS1T3 .9838/.9901
beta (all negative, ~even): bS1T1 .981/.979, bS1T2 .981/.978, bS2T1 .973/.971, bS3T1 .963/.963, bS4T1 .875/.879. => phase-only loses at s21; T2/T3 momentum stars weak.
Non-quadratic: aS1T1 +0.05 -> 1.0185 (a76c) > quadratic prediction.
- b2 (17): 1D S1T1 {.07,.10,.14}, S2T1 {.05,.08,.12}, S1xS2 grid {.03,.05,.08}^2, + S4/S7 adds. ids work/b2_ids.txt. Budget 87/500.

## 06:50 — wakeup 42 — b2 results (s21, all PASS)
S1T1 line: .03 1.0150, .05 1.0185, .07 1.0166, .10 1.0028, .14 0.9615 -> peak ~0.055 (~1.019).
S2T1 line: .03 1.0131, .05 1.0121, .08 .9957, .12 .9428.
S1xS2 grid: (.03,.03) 1.0185, (.05,.03) 1.0149, (.03,.05) 1.0106, (.05,.05) 1.0014, (.08,.03) .9974 ... not additive. +S4/S7 hurt (.919, .855).
=> separable ridge max ~+1.9% at s21, below confirm21 threshold 1.02.
- New family w3-orient (hypothesis 20261009T065157.508Z_ctrl-b_hypothesis_7a2d): split stars into inversion pairs, 3 C6 classes per (S,T) by relative angle. work/orient.py. b3 (19) submitted: S1T1 d in {30,90,150}, S2T1 d in {0,60,120}, c in {.05,.03,-.03} + validation c=.05/3 all. Budget 106/500.

## 07:03 — wakeup 43 — BREAKTHROUGH (b3, s21)
- Orientation classes: S1T1 d=90 (R perp G): +.03 1.0699, +.05 1.1178, -.03 0.886. S2T1 d=0 (R par G): +.03 1.0652, +.05 1.1113, -.03 0.896. Other classes (30/150, 60/120 mirror pairs) ~0.95-0.976, mirror pairs equal => no chirality.
- Validation f65c = 1.01847 == separable a76c. Separable family = average of one big positive class and two negatives.
- 4 promoted (8843, 1c34, 66e0, 507e) -> s21c, r46 in progress. M2r only 1.005-1.016.
- Posted result 20261009T070449.807Z_ctrl-b_result_78a4.
- b4 (24) submitted: lines to 0.2, S1d90+S2d0 combos, beta in winning classes, S3/S5/S6 analogous classes, S1xT2 classes, S1T3 d90. Budget ~130/500.
- TODO once r46/r56 known: request matched-density static control (amplitude winner).

## 07:15 — wakeup 44
- 1c34 (S1d90 .05): s21 1.1178, r46 1.1126 C1, r56 1.1068 C1 -> claim suggestive; conv46 queued. 507e (S2d0 .05): r46 1.1167, r56 1.1013.
- b4: S1d90 line .07 1.168, .10 1.248, .14 1.357, .20 1.482 (M2r 1.30); S2d0 .10 1.240 .14 1.355 .20 1.376; S1d90+S2d0 (.05,.05) 1.2355. beta in winning classes loses; S3/S5/S6 & T2/T3 analogues < 1.
- Widened box (hypothesis 20261009T071735.262Z_ctrl-b_hypothesis_3cb5). b5 (13) submitted: S1d90 .25-.5, S2d0 .17-.3, combos. S1d90 .6 rejected (M2k max 3.18 > 3).
- Matched-density control for 1c34 submitted: b15a (--control, s21,r46,r56). work/matched.py. M2-scaled variant inadmissible (w3 at |h|^2>=0 edge).

## 07:35 — wakeup 45 — STRONG claims
- 0937 (S1d90 .2): s21 1.4822 r46 1.4056 r56 1.4692 conv46 1.3857 C1 PASS -> strong. 5153 (S2d0 .2): 1.3761/1.4072/1.4715/1.4124 -> strong.
- 1c34/507e/8843/66e0 robust_positive (conv46 1.088/1.092/1.052/1.053).
- Control b15a (1c34 matched density): R 1.0011/1.0010/1.0010 (s21/r46/r56) => density alone explains ~0.1% of 11%.
- Large c: S1d90 .4/.5 and (.3,.1) FAIL (phase change). S2d0 .3 s21 1.019. r46 peak plateau ~1.41 for c~.1-.2 combos.
- Controls for 0937/5153 (disc |G|^2<=37; 8-shell truncation gave negative density): 6347, fdbd.
- b6 (17) refinement plane+side classes+beta; b7 (6) w2 parent (hypothesis w2-orient). Claim post submitted.

## 07:55 — wakeup 46
- Controls: 0937 ctl 6347 R 1.0168 all clusters; 5153 ctl fdbd 1.0174/1.0175. => averaged density explains ~2% of 40-47%. Posted result.
- w2 with w3-winning classes: S1d90 .05/.1/.2 -> .982/.960/.884; S2d0 .05/.1 -> .939/.754, .2 FAIL. Parent-dependent!
- b6 plane: r46 plateau ~1.40-1.42 (best r46 (S1 .05,S2 .14) 1.4199). Side classes/beta don't help (beta hurts r46).
- b8 (20): 10 new class directions +-0.03 around base (S1d90 .1, S2d0 .07). b9 (12): w2 class screen all 6 classes +-0.05.
- Budget ~207/500.

## 08:14 — wakeup 47
- Many strong: 283a (S1 .05,S2 .14) conv46 1.4000; f27b/407c (side classes) conv46 1.385/1.377; 636b, de2b, 514f, 3610, b9bc strong. conv46 can be 1-9% below r46 for larger c (g_cutoff 4 truncation). Best conv46 so far: 5153 1.4124.
- w2 class screen: S1 d30 / d150 at c=-0.05 -> s21 1.035/1.038, r46 1.052/1.050 (promoted). Other w2 classes < 1.
- w3 probes around B=(S1d90 .1,S2d0 .07): S5T1d90 -0.03 -> s21 1.452, r46 1.4853 (!). S5d90 +.03 hurts (r46 1.25). S1T2d0 +.03 r46 1.400; others neutral/negative.
- b10 (9): S5d90 negative lines on 3 bases + alone. b11 (6): w2 S1 d30/d150 negative lines.

## 08:32 — wakeup 48
- S5d90 negative is a big lever on w3: 586a (S2d0 .2 + S5d90 -.06) r46 1.802, s21 1.544; 8562 (S1 .05,S2 .14,S5 -.06) r46 1.759 s21 1.639; b211 r46 1.651. S5 alone negative hurts (0.84, 0.48). B+S5 -.15 drops (0.93).
- CONCERN: conv46 (g_cutoff 10, n_mesh 64, qmax 10) drops up to 8% vs r46 (ce33 1.485 -> 1.372). g_cutoff=4 truncation may be steering. => b12w3: re-evaluate 8 top points with g_cutoff=8 (orient.make now takes g_cutoff).
- w2: S1 d30+d150 (mirror pair) negative: -.05 s21 1.084 r46 1.101; -.10 s21 1.116 r46 1.186; -.15 s21 1.100 r46 1.186. b12w2: g8 version + add S1d90 / S5 classes +-.

## 08:50 — wakeup 49
- g_cutoff controls conv46 drift: g8 r46 == conv46 (0937 1.3857; 8562 1.5900 vs 1.5896). g4 inflates S5-containing points by up to 10%. ALL SEARCH NOW g_cutoff=8.
- Converged-ish w3 bests: 8562 conv46 1.5896 strong (s21 1.639 g4 / 1.534 g8); 586a g8 s21 1.5785 r46 1.6368; b211 g8 r46 1.597; 5b5e conv46 1.4798 strong.
- w2 STRONG: 67e1 (S1 d30+d150 -0.1) s21 1.1164 r46 1.1861 r56 1.1421 conv46 1.1473. a0bd (-0.15) strong conv46 1.1147. w2 +S1d90 .05 r46 1.194; +S5d90 -.03 r46 1.21 (g4).
- Posted result 20261009T085218.356Z_ctrl-b_result_5c2e.
- b13w3 (16): g8 3D grid S1{0,.05,.1} x S2{.14,.2} x S5{-.04,-.08} + S5 -.1/-.12 + S5 side classes. b13w2 (6): g8 refinements. Budget ~257/500.

## 09:13 — wakeup 50
- g8 strong (conv46 == g8 r46): 8ea8 (586a g8) conv46 1.6366, min r56 1.5215; 5d23 (b211) 1.5966; 0508 1.5896; d856 1.4602; 8fb5 1.4124.
- g8 grid: a11b (S1 .1,S2 .2,S5 -.08) s21 1.790 r46 1.7435 r56 1.7744 (best); 4177 (S1 .05,S2 .2,S5 -.08) 1.746/1.746/1.684; aa28 (S1 .1,S2 .14,S5 -.08) 1.68/1.70. Trend: more S1, S5 more negative.
- w2: 67e1 g8 (f53f) strong conv46 1.1473 (r56 1.1298). 0836 (P+S1d90 .05+S5d90 -.03) s21 1.126 r46 1.154. 2dbf (g4) strong conv46 1.1259.
- b14w3 (12): S1 {.1,.15} x S2 {.2,.25} x S5 {-.08,-.1,-.12} g8. b14w2 (16): P + 8 class dirs +-0.03 g8. Budget ~285/500.

## 09:36 — wakeup 51
- g8 climb: 4ded (S1 .1,S2 .25,S5 -.12) s21 2.025 r46 1.902 r56 2.026 (!). 589c (S1 .1,S2 .2,S5 -.12) s21 1.943 r46 1.878. Monotone in S5 more negative and S2 up. PES ent gap falls 9->3-4 (still PASS); M2r DEcreases with more negative S5 (1.39 -> 1.28) while R rises.
- a11b strong conv46 1.7426 (min 1.7426). 4177 conv46 1.7454 (min r56 1.6842). aa28 strong.
- w2 at P: S3d90 +.03 -> s21 1.151 r46 1.186 (best single); S3 d30+150 -.03 -> 1.126/1.138; S2d0 -.03 1.101/1.153.
- b15w3 (10): S1 {.05,.1} x S2 {.25,.3} x S5 {-.15,-.18} + 2. b15w2 (6): P + S3d90 lines/combos.

## 09:59 — wakeup 52
- STRONG: 4ded conv46 1.9004 (min); 589c conv46 1.8772; 9a51 1.8387; 9950 1.8169.
- b15 climb: ba25 (S1 .1,S2 .3,S5 -.18) s21 2.356 r46 2.105 r56 2.299; dc19 (S1 .1,S2 .3,S5 -.15) 2.208/2.006; 4867 2.155/1.999; 0796 2.099/2.043. ent gap ~4 stable. Still climbing at edge (S2 up, S5 more negative).
- w2: P+S3d90 .1 r46 1.2266 (s21 1.134); .06 s21 1.161 r46 1.217; fdc3 1.155/1.203.
- b16w3 (10) S2 .35/.4, S5 -.18..-.26; b16w2 (4). Budget ~314/500.

## 10:22 — wakeup 53
- STRONG (conv46=min): ba25 2.1012; 3216 2.0608; 0796 2.0409; dc19 2.0026; 4867 1.9972.
- b16: 4a78 (S1 .1,S2 .35,S5 -.22) s21 2.476 r46 2.221; 1682 (S1 .1,S2 .4,S5 -.22) s21 2.584 r46 2.214; e302 r46 2.127. r46 saturating ~2.2; ent gap 2.4-3.8.
- w2 STRONG: 026d conv46 1.2174 (min s21 1.1608); fdc3 1.2028; 30d0 1.1904; 4a7f.
- ba25 matched-density control b74c (disc |G|^2<=91; ctl M2 3.531 < parent 3.629!).
- b17w3 (19): extend to S2 .45, S5 -.26 + 7 class probes +-.05 around O=(.1,.3,-.18). b17w2 (6). Budget ~339/500.

## 10:55 — wakeup 54
- ba25 control b74c: R 0.987 all clusters (ctl M2 3.531 < parent) vs candidate 2.1-2.36. Posted updated claim 20261009T105636.788Z_ctrl-b_claim_21d8.
- 3e12 (S1 .1,S2 .45,S5 -.26) STRONG min conv46 2.2985 (s21 2.775, r56 2.759). 4a78 2.2172, 1682 2.2047, 3d5b 2.1141, 7c27 2.0901, e302 2.1242.
- Probes around O=(.1,.3,-.18): S1T2d0 -.05 r46 2.166, S2T2d90 -.05 r46 2.154 (slight +); S3/S6 neutral; side classes hurt.
- CAMPAIGN BOUNDARY binds: sum|alpha| = 3(|S1|+|S2|+|S5|) <= 2.5 -> sum <= .833. 3e12 at 0.81. b18 (9): points on the boundary simplex.
- w2 stuck ~1.2 (best min 026d 1.1608 s21; conv46 1.2174).

## 11:18 — wakeup 55
- Boundary scan b18: r46 max ~2.30 (3e12; 452d (.1,.45,-.28) s21 2.761 r46 2.306; de6e (.05,.5,-.28) 2.451/2.285). S5 beyond -.3 hurts s21 strongly. Optimum ~ (.1,.45,-.26..-.28) ON the sum|alpha| boundary.
- Strong: e0e9 2.2539, 909e 2.2250, 3915 2.1614, c370 2.1493.
- b19 (10): beta +-0.03 in active and side classes at 3e12. Control for 3e12: 41aa (M2 3.427 < parent).
- Posted hypothesis (boundary) and abandon+coverage for w3-sep. Budget ~362/500.

## 11:41 — wakeup 56
- 3e12 control 41aa: R 0.970 all clusters (ctl M2 3.427). Phase on top of 3e12 (b19): neutral/negative (r46 2.256-2.3115) -> no phase gain.
- Strong: 452d min 2.2972 (r56 2.859); de6e 2.2727; 4b52 2.2330; 7335 2.1693.
- b20: Sobol (seed 7) 24 pts in 8-dim w3 class space (scaled to sum|alpha|<=2.45), Sobol (seed 11) 16 pts in 6-dim w2 class space. Params in work/b20w*/params.json. Budget ~404/500 after.

## 12:10 — wakeup 57
- Sobol w3 (24, 8-dim): best s21 1.81 (58e2), r46 1.855 (715e); 8 FAIL (phase breakdown), none beats hand optimum. Sobol w2 (16): best ~1.16 (f4c4), 3 FAIL. => optimum region found is the best sampled.
- b21 (4): boundary trades S2 -> S1T2d0 / S2T2d90 for r46. Then wrap up: coverage posts for w3-orient, w2-orient; swarm done.

## 12:38 — wakeup 58
- b21: ada9 (S1 .1,S2 .4,S5 -.26,S2T2d90 -.05) s21 2.432 r46 2.382 (best r46); a317 (A,B -.025) r46 2.367; d46e (A -.05) r46 2.340.
- Leaderboard: top converged strong 45b3 2.3006 (3e12+bS1d90 -.03), 3e12 2.2985, 452d 2.2972.
- b22 (5): trade S2 -> S2T2d90 further. Budget ~413/500.

## 13:04 — wakeup 59
- b22: 6c39 (S1 .1,S2 .4,S5 -.24,B -.05,A -.02) s21 2.513 r46 2.391; more B lowers s21 sharply (9c70 s21 1.81). Converged ~2.3-2.4 min.
- r56 stages queued (lanes slower).
- w2 matched-density control for 026d: 2f61 (eps lift 3e-5; ctl M2 2.504 vs parent 2.5).
- w2 leaderboard: 026d min 1.1608 strong (conv46 1.2174); 13+ strong w2.
- NEXT: wait for ada9/6c39/a317 r56+conv46 and control 2f61, then coverage posts (w3-orient, w2-orient), final claim summary, swarm done. ~87 evals unused is fine.

## 13:36 — wakeup 60
- w2 control 2f61: s21 1.0002, r46 1.0009 (vs 026d 1.161/1.217) -> w2 gain also not averaged-density.
- r56 queue stalled ~1h for b21/b22 promotions (SUBM). Tallying families for coverage posts (background task).

## 14:09 — wakeup 61
- Posted coverage results for w2-orient (20261009T134851.749Z_ctrl-b_result_e7cc) and w3-orient. Tally: w3-orient 229 req (219 PASS/10 FAIL, 160 strong); w2-orient 85 (81/4, 35 strong).
- r56 queue stalled since ~12:30 (posted note). Plan: wait one more cycle for ada9/6c39 r56, then swarm done.

## 15:13 — wakeup 62 — DONE
- r56 queue still stalled (~2.7h). All coverage posted. Running swarm done (summary work/done.md). 416/500 charged.
