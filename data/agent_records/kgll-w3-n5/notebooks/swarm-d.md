# swarm-d notebook

Started 2026-10-13T18:08:51+00:00.

## 2026-10-13 18:20 — wakeup 1
- Read the brief, doc 40 (024 pilot: +0.51% at 4x6 → −0.92% at 5x6), doc 46 (Nk=21: w3 α[S1,T1]=+0.05 → +1.85%, −0.05 → −9%, β+0.05 → −4.4%), and notes §5.6/8.4/12.
- Parent gaps: w3 s21 4.5714e-4, r46 4.3823e-4; w2 s21 3.2271e-4.
- The deformation block only allows star products O_s(r)F_p(k) with inversion-symmetric (cos) stars. True joint (G,R) orbits (cos(Gr+kR) separated from cos(Gr−kR)) are NOT representable. Worth a board note.
- Tools: work/kgen.py (stars in the 120° basis, C6 orbits; make/diag/check), work/cma18.py (CMA-ES with init/ask/submit/tell/show, state in work/<family>/state.json).
- swarm-a took `w3-map` (single-term map, |α|≤0.1, |β|≤0.05). I took `w3-cma18`: 18-dim α+β on S1,S2,S3 (|G|²=1,3,4) × T1,T2,T3, box |α|≤0.3, |β|≤0.15, λ=12, σ0=0.04 (β scaled ×0.5), g_cutoff 6. Hypothesis 20261013T181550.649Z_swarm-d_hypothesis_f018. Budget ≈180.
- Gen 0 submitted (12 reqs, 20261013T1816/1717..).
- Next: `python cma18.py tell` when gen0 is done, then ask + submit. Later: a w2 counterpart, plus verification/critique of others' leads.

## 2026-10-13 18:33 — wakeup 2
- CMA gen0 (w3-cma18): all 12 < 1 (0.42–0.94). σ0 too large for the whole-star bowl. Then saw swarm-c's orientation-channel α leads on w3: 68f6 (S2T1 0°, c=0.08) s21 1.092 / r46 1.084 / r56 1.082 SUGGESTIVE, conv46 running; 3182 (S1T1 90°) s21 1.097 / r46 1.081.
- Abandoned w3-cma18 (post 20261013T183157.770Z_swarm-d_abandon_0d96), since whole-star products dilute the channel.
- New family `w2-orient` (hypothesis 20261013T183158.583Z_swarm-d_hypothesis_bfa2), on swarm-b's invitation to take the w2 joint sector. kgen.py now has pairs/channels/channel_block. Keys: g<|G|²> r<|R|²> d<angle>. Channel angles: g1,g4 × r1,r4 → 30/90/150; g3 × r1,r4 → 0/60/120; g1,g4 × r3 → 0/60/120; g3 × r3 → 30/90/150.
- Batch b1 (30 reqs) submitted: w2o/b1_submitted.txt maps files to req ids.
- Others: swarm-a w3 whole-star map (S1T1 α+0.08 → s21 1.030 / r46 1.040 / r56 1.037); swarm-b w2 whole-star α map (best s21 ~1.014); swarm-e w3 orientation (overlaps swarm-c).
- Mailed swarm-b (taking w2 joint) and swarm-c (matched-density control; amplitude line).
- Next: read b1, then β on the best channels, amplitude lines, combinations.

## 2026-10-13 18:52 — wakeup 3
- w2-orient b1 results: the w3 winners (g1r1-D90, g3r1-D0 +0.08) LOSE on w2 (0.976, 0.975). w2 winner g4r1-D90 +0.08 (ef27): s21 1.057, r46 1.129, r56 1.086, suggestive, conv46 queued. g1r1-D30/D150 at −0.08: 1.033/1.036, r46 1.041. g3 is inert on w2 (all 0.975–0.977). T2/T3 all lose at +0.08.
- Hypothesis: the winning channel is tied to the parent's own density harmonics (w3: density g4 → winners g1, g3; w2: density g3 → winners g4, g1).
- swarm-c's w3 line: c=0.40 g3-D0 (3faf) R 1.50/1.42/1.47; but R_beyondM2 peaks at c≈0.32 (8617: 0.80) and falls at 0.40; d025 (g1-D90 c=0.40) R_beyondM2 0.66 < parent 0.69. Posted critique note 20261013T185113.363Z_swarm-d_note_6ebe (it mislabels d025 as a combo; corrected by mail to swarm-c).
- Posted w2 interim result 20261013T18515x. Submitted b2 (26): w2o/b2_submitted.txt. Builder: work/w2o_batch.py (edit DESIGN per batch).
- Budget: 42 + 26 = 68 charged.
- Next: read b2; then a CMA/line search over the best w2 channels (g4-D90, g1-D30+150, plus g9/g12 if they win) at larger c; watch R_beyondM2 vs parent (w2 parent Δ/(M2 Δ_LLL) = 3.2271e-4/(2.5×1.8272e-4) ≈ 0.706).

## 2026-10-13 19:13 — wakeup 4
- b2 results: g4r1-D90 line on s21 peaks at c≈0.08–0.16 (1.057/1.055) and falls fast (0.24: 0.99, 0.5: 0.53), but r46 for c=0.16 is 1.204, so the cluster spread is large. g1 D30+150 achiral −0.16 (f07b) 1.111/1.143/1.125. Combo g4+0.16 & g1achiral−0.08 (9445) 1.103/1.245/1.198 (M2k 2.657), at converge. β on g4-D90 ±0.04 → 0.978/0.976 (even, M·T OK). g4×T2/T3, g9 channels all lose.
- **ef27 (20261013T183218.010Z!) = robust_positive on w2**: 1.057/1.129/1.086/conv 1.129, M2k +0.7%. The deformed gaps are cluster-stable (3.41/3.50/3.49e-4); the parent's dip on r46 drives the R spread. Claim 20261013T191026.165Z_swarm-d_claim_c997. NB: my result post 0644 mis-cites ef27 as 183208; corrected in the claim.
- Human request for the w2 control: 20261013T191040.807Z_swarm-d_request_719d. Controls submitted myself (work/controls.py, ε=2e-4 floor, box 12): w2o/ctl_submitted.txt (7 × 3 clusters = 21 evals).
- b3 (30) submitted: 2-D grid g4-D90 {0.04,0.08,0.12} × g1achiral {−0.08..−0.20}, plus g7a/g7b/g16 × r1 channels ±0.08 (w2o/b3_submitted.txt).
- Helper: work/tab.sh <submitted.txt> tabulates results.
- Budget ≈ 68+30+21 = 119.
- Others: w3 claims STRONG (swarm-c g3-D0 c=0.32/0.40). swarm-b and swarm-e are running w3 controls.

## 2026-10-13 19:37 — wakeup 5
- b3 grid: STRONG on w2 for several (c_g4D90, c_g1(D30+150)) points: 5061 (0.12,−0.20) 1.161/1.200/1.180/1.200 (best R_min); 3cde (0.08,−0.16) 1.158/1.206/1.191; ea53 (0.12,−0.16) 1.154/1.230/1.210. s21 binds everywhere. 9445, f07b, efff and 36a1 are also strong.
- Controls (s21/r46): every static control is ≤1.006 (frozen-max of 9445, M2 2.926: 0.920/1.002); parent sanity fc36 0.9998. So the gain isn't static density. r56 controls are pending.
- Outer shells on w2: g7 chiral halves obey the M·T mirror pairing to ≤0.007. Best singles: g7b d10 + 1.025 (r46 1.078), g7a d169 + 1.018, g7b d130 − 1.017, g7a d49 − 1.013; g16 d90 − 1.004; everything else loses.
- Claim STRONG posted: 20261013T193600.534Z_swarm-d_claim_ba8a.
- b4 (21) submitted: ridge extension, third ingredients on B=(0.10,−0.18), T2/T3 at negative c (w2o/b4_submitted.txt).
- Budget ≈ 140.
- w3 status (others): swarm-c g3-D0 optimum c≈0.40–0.44 (r46 1.42), flat; swarm-a: a −3G harmonic on g1-D90 helps while M2k falls; swarm-b: w3 static controls all ≤1.024 against 1.495.
- Next: read b4 and the r56 controls. Then perhaps a small CMA over the 4–6 achiral w2 channels with objective min(s21, r46) to lift s21; then a coverage post.

## 2026-10-13 20:00 — wakeup 6
- b4: B=(0.10,−0.18) afaf 1.165/1.213/1.191 strong; B+g1d90+0.06 (20261013T193518.346Z_swarm-d_req_510b) 1.178/1.208/1.194/1.208 strong = best w2 R_min. Third ingredients (g7B −, g16 −, g4 D30+150 −) raise r46 to 1.25–1.30 but cost s21. Ridge closes past c_B −0.24. T2/T3 at −0.08 lose.
- Controls on s21/r46 all ≤1.006 (r56 still pending).
- w3 elsewhere: swarm-a square-wave g1-D90 (fundamental + −3G) up to r46 1.80 with g3; swarm-c CMA ece3 R_min 1.653; swarm-b k-reassign kills the gain (the gain lives in the k-assignment).
- Started `w2-cma` (work/cma_ch.py, state work/w2-cma/state.json): 8 achiral channels, x0=510b, σ 0.04, λ=10, objective min(s21,r46). Hypothesis 20261013T195938.292Z_swarm-d_hypothesis_2ab2 (its ref to 510b has a WRONG timestamp; correct one above, noted to swarm-e). Gen0 submitted.
- LESSON: always grep the request IDs from *_submitted.txt before citing them.
- Budget ≈ 171.

## 2026-10-13 20:25 — wakeup 7
- CMA gen0 (w2-cma): best 437e min(s21,r46)=1.177 (s21 1.177, r46 1.244); no gain over 510b. Mean barely moved (g16 −0.02, g9 small). Gen1 submitted.
- r56 legs of the controls are still SUBMITTED after 70 min (queue).
- Board: swarm-a STRONG w3 0208 R_min 1.80 (square wave g1-D90 + 3G + g3-D0); swarm-b mechanism: k-reassign destroys every winner (5061 1.161 → 0.569); static controls ≤1.02.
- Critique in prep: the entanglement gap falls as R rises (parent ~20; 68f6 9.5; 0208 4.5; s21c N_A=3 3.8). Script work/entgap.py → eg.json.
- Posted critique 20261013T202850.168Z_swarm-d_note_5a4a: the PES ent. gap falls with R (w3 r=−0.59; medians 8.3 at R<1 → 4.4 at R≥1.8; min on board 1.66; bfbd N_A=3 2.57). Mailed swarm-a. Suggested N_A=3 on r46 for the finals.

## 2026-10-13 20:43 — wakeup 8
- w2-cma gen1: best 1ebf (s21 1.1915, r46 1.2097; r56 pending; zc=[A .082, B −.172, g1D90 .063, g9D30150 .029, g9D90 .018, g7B −.032, g16 .012, g4D30150 .007]) and 5b88 (1.1903/1.2403). New w2 best min(s21,r46) ≈ 1.19. Gen2 submitted, σ 0.030.
- swarm-e's w2-profile 891b R_min 1.202 is the current w2 leader (s21 1.202, r46 1.238).
- w3: swarm-c 38fd R_min 1.986 (g3-D0 0.54 + g9-D90 −0.23). swarm-b: phase-only gain along chiral S4 combos (r46 1.27).

## 2026-10-13 21:05 — wakeup 9
- gen2: 13bd s21 1.2249 / r46 1.1992 (r56 queued); 6813 1.192/1.282; c478 1.195/1.199. 1ebf strong: 1.1915/1.2097/1.1845/1.2088 (R_min 1.1845).
- The mean drifts to more g7B (−0.05), g9D90 (+0.04), B −0.20, A 0.10. Gen3 submitted (σ 0.029).
- The r56 queue is slow; swarm-b asked the operator about r56 controls stuck in SUBMITTED (mine too, since 19:12).

## 2026-10-13 21:28 — wakeup 10
- gen3: ffc2 min(s21,r46) 1.226 (s21 1.230, r46 1.226; zc A .093 B −.163 g1D90 .015 g9D30150 .048 g9D90 .072 g7B −.071 g16 .019 g4D30150 −.048). bc42 1.202, fe93 1.205.
- 25ff FAIL: manifold splitting/Δ = 0.167 (PES matched, ent. gap 2.24). Large g9D90 .087 + g7B −.09 + A .14, so a manifold-splitting boundary sits nearby.
- swarm-e 044c (5061 base + g1D90 +0.16, g16 −0.12, A 0.08): 1.220/1.291/1.298. Injected a 044c-like point into gen4 (#9) on top of my mean, with the CMA injection Mahalanobis cap in tell.
- w3 is at R_min 2.145 (swarm-c 0fea), Σ|α| 2.19 near the box.

## 2026-10-13 21:49 — wakeup 11
- gen4: 9d4f s21 1.245 / r46 1.274 (r56 pending); injected 044c-like f404 1.196/1.351; aab3 1.207/1.252.
- r56 bites: ffc2 strong but r56 1.159 → R_min 1.159; 13bd strong R_min 1.192 (1.225/1.199/1.206/1.192). The objective min(s21,r46) doesn't see r56. Final candidates need all clusters.
- Mean: A .11, B −.17, g1D90 .05, g9D90 .07, g7B −.04, g4D30150 −.035. Gen5 submitted.
- Plan: gens 5–7 (~30 evals), then pick a final w2 candidate by R_min over all clusters + ent gap; coverage posts for w2-orient and w2-cma; done near ~250 evals unless new ideas.

## 2026-10-13 22:17 — wakeup 12 (after a session interruption)
- The session died mid-call. CMA state had gen=6 with no pending gen (ask had written files but not saved state), and the budget showed nothing submitted. Re-ran ask+submit for gen6 (10).
- gen5 best: 1017 (zc in state history) STRONG: 1.264/1.344/1.293/conv 1.339 → **best w2 R_min 1.264**. 9d4f STRONG 1.245/1.274/1.250/1.271.
- Board: swarm-a's chiral phase (|G|²=7 C49−C131, β) on top of w3 0fea: R up to s21 3.43 / r46 3.89 at β=0.2, still rising; the human is asked for a sanity/gauge check. swarm-e (w2-phasemap on f6be) and swarm-b (w2 amp+phase) cover w2 phase, so I'll wait for their map and then put the best chiral phase on 1017 as the final step.
- Plan: gen6 (and maybe gen7), then a w2-cma result + coverage post.

## 2026-10-13 22:40 — wakeup 13
- gen6: 86af (20261013T221541.186Z) s21 1.2646 / r46 1.2852; 8e6c 1.240/1.257; 0fe2 1.241/1.253; d174 0.89. The CMA plateaus at min(s21,r46) ≈ 1.26 (mean A .14, B −.15, g9D90 .07). Paused after gen6 (gen7 not asked).
- swarm-b: w2 044c + S7 chiral phase β −0.04 → s21 1.267, r46 1.405. Critique: expose low_energies to separate a gap gain from energy-scale inflation.
- b5 (6): swarm-b's S7 chiral phase (copied from 22d7, β −0.02/−0.04/−0.06) on 1017 and 86af (w2o/b5_submitted.txt). Mailed swarm-b.
- Next: read b5. Choose the final w2 candidate (R_min over all clusters, ent gap). Then post the w2-cma result + coverage and the w2-orient coverage. Likely `done` around 230–260 evals.

## 2026-10-13 23:03 — wakeup 14
- b5: swarm-b's |G|²=7 chiral phase 10.9−169.1 (my files are labelled "S7chiral" = |G|²=7, swarm-b's S4) on 86af: β −0.04 → s21 1.327 / r46 1.339 (3a58); −0.06 → 1.318/1.362; on 1017 it hurts (1.263→1.243 at −0.04). Base-dependent, as swarm-b warned.
- Verified my chiral-combo builder reproduces swarm-b's 22d7 phase block exactly: combo(θ) = β(C_θ − C_{180−θ})/√2, entries β/√6.
- b6 (13) submitted: the 5 other chiral combos (|G|²=7: 49−131, 71−109; |G|²=13: 16−164, 44−136, 76−104) ±0.04 + 10.9−169.1 at +0.04 on 86af; g13 44−136 ±0.04 on 1017.
- Board: swarm-b STRONG w2 R_min 1.350 (f6be + |G|²=13 44−136 phase); swarm-e 7818 s21 1.312 / r46 1.565; w3 R_min 4.18 (swarm-c 4462).

## 2026-10-13 23:24 — wakeup 15
- b5 full ladder: 86af + |G|²=7 10.9−169.1 phase: β −0.04 (20261013T223836.285Z_swarm-d_req_3a58) strong 1.327/1.339/1.316/1.324 → R_min 1.316; β −0.06 (…223838.674Z_swarm-d_req_7b9c) strong 1.318/1.362/1.339/1.345 → R_min 1.318 = my best w2.
- b6 on 86af: best single combos |G|²=13 44−136 +0.04 (5a3e) 1.355/1.334; |G|²=13 16−164 −0.04 1.244/1.371; |G|²=7 71−109 −0.04 1.222/1.340; |G|²=7 49−131 ±: 1.28/1.27, 1.22/1.29. Opposite signs mostly lose (M·T-allowed chiral response is odd). 1017 + |G|²=13 44−136 +0.04 (ab13) 1.336/1.443.
- b7 (6): 86af + 7(10−169)− + 13(44−136)+ combos; 1017 + 13(44−136) +0.06/+0.08.
- swarm-a: large-phase conv46 vs r46 grows (+1.9% on 4462), probably qmax applied to the candidate only.

## 2026-10-13 23:46 — wakeup 16
- b7: 86af + 7(10−169) −0.04 + 13(44−136) +0.04 (ddc9) s21 1.350 / r46 1.355 (r56 pending); 1017 + 13(44−136) +0.06 (bef5) 1.346/1.466; +0.08 1.333/1.452. ab13 r56 1.368 → suggestive (min 1.336 so far); 5a3e r56 1.292.
- The w2 gains saturate at s21 ≈ 1.35 on my bases; swarm-b's phase-CMA on f6be is at s21 1.453. Wrap up: wait for r56/conv46 on ddc9, bef5, ab13, then post the w2-cma result + coverage (and w2-orient coverage) and `done`.
- w3: swarm-c R_min 4.823 at the Σ|α| boundary (9d3e).

## 2026-10-14 00:19 — final
- Final ladder: bef5 STRONG R_min 1.346 (1.346/1.466/1.378/1.407), ab13 1.336, 7b9c 1.318, ddc9 1.316, 5a3e 1.292.
- Withdrew the stuck r56 control legs (s21 + r46 stand).
- Coverage posts: w2-orient 20261014T001734.077Z_swarm-d_result_67ea, w2-cma 20261014T001758.849Z_swarm-d_result_6b16. Mailed swarm-e the seeds.
- `swarm done` posted. 235/500 charged. Stopped: the remaining directions are covered by swarm-b, swarm-c and swarm-e.
