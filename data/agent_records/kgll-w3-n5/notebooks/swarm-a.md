# swarm-a notebook

Started 2026-10-13T18:08:40+00:00.

## 2026-10-13 18:16 — wakeup 1 (orientation + first batch)
- Read brief, docs 40/46, theory §5–8, notes §7.5 (ideality defect = <Var_r(∂+γ)>, grows ∝ |α/2+iβ|²|R|²) and §12 (contact vanishes for scalar bands; M2(k) not a complete descriptor).
- Prior lead (doc 46, not in store): w3 α[S1,T1]=+0.05 → +1.85 %, −0.05 → −9.0 %, β +0.05 → −4.4 %, α[S3,T1]=+0.05 → −3.75 %.
- Parents in store: w3 s21 4.5714e-4, r46 4.3823e-4; w2 s21 3.2271e-4, r46 3.0955e-4.
- Tools: work/kgll.py (stars S1..S10 [+a/b 6-orbits for 12-member shells], T1..T3; build(parent, terms, path); diag → M2k ratio, Smin/Smax).
- Posted hypothesis 20261013T181434.416Z_swarm-a_hypothesis_6c8e (family w3-map, ~75 evals).
- Submitted b1 (32 reqs): S1T1 α line {.02,.03,.04,.06,.08}, β {±.02,−.05}; S2..S7×T1 α,β ±0.05. Pending b1b (15): S8..S10×T1 + S1T1 ±0.05 refs. Then S1..S3×T2,T3.
- Observation: M2^(k)/M2 barely moves (≤1.4 %) even at α=0.3 on S3 — amplitude doesn't sharpen much at these steps.
- MISTAKE: ran submit-batch b1 twice → 32 duplicate requests (ids 181607–181618); withdrew all 32. Verify they are not charged (budget showed 23/500 right after). Never re-run submit-batch on the same dir; move submitted dirs to work/batches/done/.

## 2026-10-13 18:30 — wakeup 2
- b1 results (all PASS): α S1T1 monotone 0.02→1.0107 … 0.08→1.0301; ladder: 0.08 (5777) r46 1.0397 r56 1.0368 SUGGESTIVE; 0.06 (112e) r46 1.031 r56 1.030; α S2T1 +0.05 (2e00) 1.021/1.029/1.026. All β lose, β-even; loss grows with |G|. S3–S7 α lose both signs.
- Duplicates were free (budget 32 after b1).
- Board: swarm-b w2 map+CMA, swarm-c w3-joint (pair-star orientations; best s21 ~1.09–1.10, r46 1.084!), swarm-d w3-cma18 (S1–S3×T1–T3 joint CMA), swarm-e w3-orient. swarm-b M·T rule: β-odd vanishes in TL for whole stars; clusters are chiral/only-inversion.
- Posted interim result 20261013T183004.199Z_swarm-a_result_9d85; mailed swarm-d.
- Submitted b2 (30): S1T1 α to 0.40, S2T1 to 0.20, combos, S1–S3×T2/T3, S8–S10×T1 (ids work/batches/b2_ids.txt).
- Tool: work/collect.py [filter] prints my table.
- Next: find turnover of S1T1 α; if large α keeps winning, push to box edge (0.6) and request matched-density control.

## 2026-10-13 18:50 — wakeup 3
- b2 done. α S1T1 peaks s21 1.0341 @0.12; r46 1.0628 / r56 1.0452 @0.15 (5373, best R_min 1.0452 suggestive); turns over by 0.25 (0.997), 0.40 0.877. S2T1 peaks ~0.08. Combos b5e2 1.0352/1.0531/1.0451. All T2/T3 and S8–S10 lose.
- swarm-c single orientation channels (g1Δ90, g3Δ0) dominate: c=0.40 → s21 1.495, r46 1.419 (3faf); robust_positive claim on c=0.08 ones. Herding: b,c,d,e all on orientation channels.
- Closed w3-map: abandon post 20261013T184608.831Z_swarm-a_abandon_b6dd with coverage (typo'd 5373 id; corrected in note).
- Critique note 20261013T185001.599Z_swarm-a_note_67c3: gc6 truncation 7e-4 at c=0.4; BZ-avg density M2 3.77 vs M2k 4.92 (+36%) vs R +42-50%. Mailed swarm-c.
- NEW ROLE: surrogate. work/harvest.py (all leaderboard rows → work/data/rows.json, cache work/data/show), work/features.py (M2k, M2bar, Dvar ideality-defect proxy). Plan: fit log R ~ f(M2k, Dvar), then optimize over multi-channel space within box, submit top proposals.

## 2026-10-13 18:58 — wakeup 4
- Surrogate log R ~ log(M2k/M2) + Dvar: poor (corr .68 w3, .52 w2), underpredicts channel winners 10–25 %. Dropped: swarm-e owns the proxy study. Mentioned in hyp post.
- Board: 3faf STRONG (r46 1.419, r56 1.467, conv46 1.420). swarm-d critique: R_beyondM2 peaks near c≈0.3, above that the gain tracks M2k. swarm-b runs frozen-k static controls. On w2 the w3 channels lose; g4-D90 wins (swarm-d). swarm-c b3: g3 line to c=0.88 at gc8, plus a 2D grid of the two channels.
- New family w3-profile (hyp 20261013T185833.687Z_swarm-a_hypothesis_1a25): fundamental channel c=0.24 (g1 = 875a, g3 = e07f, free refs) + collinear add-on (2G, 3G, 2R, 2G2R) at c2 ±0.06/±0.12. b3 = 30 files (ids work/batches/b3_ids.txt). Tool: work/chan.py (pair-star channel builder; G1CH/G3CH pairings).

## 2026-10-13 19:18 — wakeup 5
- b3 results: **g1Δ90 c=0.24 + 3G (|G|²=9, same R pairing) c2=−0.12 → s21 1.3765, r46 1.3972 (1e08), M2k ratio 1.050 (base 1.138, 1.3105/1.2596)**. Square-wave shaping along G. 2G flat, 2R loses, g3 add-ons inconsistent.
- Board: swarm-c g3Δ0 optimum c≈0.40–0.48 (6f32 STRONG r46 1.4197, r56 1.456); PES FAIL past c≈0.7; second channel hurts near optimum. swarm-b static controls (ρ̄, frozen-K/Γ) all ≤1.024 vs 1.495 → gain needs k-dependence. swarm-d w2 g4-D90 robust_positive (ef27).
- Posted result 20261013T191826.588Z_swarm-a_result_5771 (the ref id I passed for 1e08 was guessed; see below for the real id).
- Submitted b4 (19, gc8): g1 square-wave grid c 0.16–0.48 × c3/c −1/3…−5/4; gc8 repeat of 1e08; g3+g1sq combos; ids in work/batches/b4_ids.txt.
- real ids: 1e08 = 20261013T185845.691Z_swarm-a_req_1e08, 842b = 20261013T185845.002Z_swarm-a_req_842b, bdee = 20261013T185846.223Z_swarm-a_req_bdee

## 2026-10-13 19:39 — wakeup 6
- b4: square-wave g1Δ90 (3G at c3/c≈−0.6) is the top w3 direction: 7b81 (c .48, c3 −.32) s21 1.783, r46 1.655, r56 1.660, conv pending; 76f8 (.40,−.27) 1.663/1.632; 849e (.32,−.22) 1.532/1.570. M2k falls as |c3| grows while R rises. gc6→8 at 1e08: −1.2 % on r46.
- Board: swarm-c now CMA (w3-cma) over 15 pairs incl. my 3G (ece3 s21 1.696). swarm-d STRONG on w2 (R_min 1.161). swarm-e nematic.
- Posted 20261013T193853.631Z_swarm-a_result_7305 (it gives the correct 1e08 id); mailed swarm-c (split: I do lines, they do CMA) and swarm-d (try 3G shaping on w2 g1 channel).
- b5 (19, gc8): c 0.56–0.80 × ratio −0.5/−0.6/−0.7; 0.48 × −0.75/−0.85; g1sq + g3 combos. ids work/batches/b5_ids.txt.
- Tool: work/collect2.py [filter] (fast, from leaderboard).

## 2026-10-13 19:57 — wakeup 7
- b5: pure g1sq saturates r46 ~1.65 (4ee8 STRONG: 1.708/1.651/1.699/conv 1.650; 7b81 R_min 1.6535). Past c≈0.5, s21 rises but r46 falls (c .80: 1.76 vs 1.24). Combos g1sq+g3: 0208 (.40,−.27,+.16) s21 1.901 r46 1.802; a76c (.48,−.32,+.16) 1.955/1.787; r56 pending.
- Board: swarm-b k-reassignment h_{k+M} kills the gain (6f32 1.50→0.60), so the gain lives in the k-assignment; swarm-b runs controls on a76c from its own budget. swarm-c CMA: ece3 = g3 .475 + |G|²=9 Δ90 −.10, R_min 1.653.
- Posted result 20261013T195628.449Z_swarm-a_result_1efb; mailed swarm-c seeds + overshoot warning.
- b6 (8): g3-coordinate grid around 0208. Afterwards the 3D optimum is left to swarm-c's CMA.
- Next idea candidates: (a) w2 square-wave on swarm-d's g1(Δ30+Δ150) if swarm-d declines; (b) robustness of the top points (finer mesh / gc) beyond conv46; (c) coverage post for w3-profile.

## 2026-10-13 20:20 — wakeup 8
- b6: the ridge around 0208 is flat on r46 at 1.80–1.82: b30d (.40,−.27,g3 .24) s21 1.931 r46 1.820; 31f7 (.32,−.22,.24) 1.873/1.812; 7463 1.878/1.806. I hold the w3 top 5.
- 0208 full ladder: s21 1.901, s21c 1.901, r46 1.802, r56 1.905, conv46 1.8005, C=1 → STRONG. R_beyondM2 ≈ 0.96–1.01 (parent 0.69).
- Posted claim 20261013T201754.559Z_swarm-a_claim_bf6f; mailed swarm-c (recenter on b30d/0208; I stop 3D lines).
- swarm-e on w2-profile (square-wave transfer); swarm-d added 3G to the w2 CMA; swarm-b on chiral phase.
- b7 (9, gc10): base 0208 at gc10 (truncation check) + 4G (|G|²=16) ±.05/±.10, 2G ±.08, g3-2G ±.06 add-ons. 4G is not in swarm-c's CMA coordinate set.
- Physical picture (speculative): g1Δ90 ≈ f(G·r)·cos(G·X_k), with X_k = guiding centre (ẑ×R_j ∥ G_j), i.e. each orbital is sharpened at its own centre — an effective l_B reduction. swarm-b's k+M reassignment (gain → loss) fits this. g3Δ0 doesn't fit as simply.

## 2026-10-13 20:45 — wakeup 9
- b7: harmonic add-ons (2G, 4G, g3-2G) at 0208 are null/negative; gc10 base (df0f) = gc8 to 1e-4. 3G is the only useful harmonic.
- swarm-c CMA 38fd (g3 .537, g9 −.229, g1 .07, g4Δ90 .10) STRONG R_min 1.986 (s21 2.072, r46 1.988, r56 2.065, conv 1.986); now the w3 top. ρ̄ M2 3.587 < parent.
- swarm-d: entanglement-gap margin shrinking (0208: 4.5–4.7 at N_A=2, 3.81 at N_A=3). Suggests N_A=3 on r46 for the final candidate.
- Posted note (b7 null + 38fd check). b8 bridge line b30d → 38fd t=.2,.4,.5,.6,.8,1.2 (6), at swarm-c's request.
- Budget 145 + 6. Next: decide a new direction. Candidates: w3 T1-only space seems saturated by the CMA. Maybe: (i) final-candidate robustness package (request N_A=3 r46 from the human); (ii) the coverage post for w3-profile.

## 2026-10-13 21:05 — wakeup 10
- b8 bridge b30d→38fd: r46 monotone 1.820→1.979 (t .8) → 1.988 (38fd) → 1.962 (t 1.2), so one ridge. s21 peaks at t .8 (028c, 2.141). M2k falls along it. Posted result.
- swarm-c CMA gen4: s21 2.22 (0fea), pending ladder. swarm-b: phase-only chiral S4×T1 49–131 combo r46 1.27 (clean beyond-M2 path); swarm-e w2-profile STRONG 1.20.
- New family w3-offT1: b9 = 24 add-ons (S1/S2/S5 × T2/T3 achiral combos, ±0.08) on 38fd + rebuilt 38fd ref (25). Tools: work/orient.py (joint-C6 orientation channels, any shell × T).

## 2026-10-13 21:30 — wakeup 11
- b9 off-T1 on 38fd: mostly null/negative on r46; S2T2 th90 −0.08 +1 % on both clusters; T2/T3 cause big s21/r46 splits. Rebuilt 38fd (9368) reproduces exactly → my term-merging builder is validated.
- swarm-c 0fea STRONG R_min 2.145 (Σ|α| 2.185 near the 2.5 box). swarm-b chiral S4×T1 phase-only: linear part robust, +5–6 %/0.04.
- Posted result (off-T1). b10 (8): 0fea + chiral-S4 phase β ±, 38fd + 0.04, S2T2θ90 follow-ups, 0fea rebuilt. Mailed swarm-b.
- Data blocks cached in work/data/blk_*.json; batch10.py has the terms()/merge() helpers (canonical pair keys).

## 2026-10-13 21:50 — wakeup 12
- b10: **0fea + chiral S4×T1 phase (swarm-b 49−131 antisym, +β) β=.06 → s21 2.740, r46 2.843 (b5d1)**; .04 2.637/2.653; .02 2.433/2.404; −.04 1.788/1.617. 38fd + .04 → 2.340/2.427. Huge α·β cross term (odd part ~8× phase alone). 0fea rebuilt f8cb exact. S2T2θ90 on 0fea −.08: 2.161/2.231 (r46 +3.8 %, s21 −2.8 %); on 38fd −.16: null.
- Posted result; mailed swarm-b (credit) and swarm-c (add β to the CMA).
- b11 (7): β .08–.20 on 0fea + symmetric-combo control ±.04 (artefact test).

## 2026-10-13 22:10 — wakeup 13
- b11: phase line on 0fea rises roughly linearly: β .20 (69c3) s21 3.43, r46 3.89, r56 3.77. Symmetric-combo control odd part −0.008/−0.013 vs antisym +0.43/+0.52, so physical in the M·T sense. b5d1 (β .06) full ladder STRONG R_min 2.740, ent gap 4.8 (base 3.9).
- Posted result 20261013T220913.435Z_swarm-a_result_51de, plus a request to the human for a physics sanity check (gauge covariance, plausibility of 8.5×Δ_LLL). No claim above b5d1 until the human answers.
- b12 (16): β .25–.70 on 0fea; other chiral combos (S4 11−169, 71−109; S7 16−164, 44−136, 76−104) ±.04 on 0fea+β.20. Builder: work/batch12.py chiral().
- swarm-b runs the w2 amp+phase add-on (mirroring mine).
- 22:12: 69c3 full ladder s21 3.43 / r46 3.89 / r56 3.77 / conv46 3.90 (strong-level, but held from claim pending human check). swarm-c started w3-cma2 (joint α + chiral β; β on my |G|²=7 combo and |G|²=13). b12 in flight.

## 2026-10-13 22:35 — wakeup 15
- b12: β line on 0fea peaks at s21 β≈0.40 (d48b 3.919 / r46 5.013 / r56 4.882); r46 peak 0.50 (5.162); 0.70 s21 2.03. Other chiral combos: only S7 16−164 +0.04 adds (+1.9 % s21, +4.5 % r46).
- Posted result; mailed swarm-c (β optimum ≈ 0.40, not their x0 0.06). Handing the joint α/β optimum to w3-cma2.
- No human reply yet to request 3420. No claim above b5d1 until then.
- Budget 205/500. Next: since the w3 joint optimum is swarm-c's and w2 is d/e/b's, consider (a) coverage/abandon posts for w3-profile and w3-offT1, (b) a cheap independent consistency test of the phase result (e.g. same β on 4ee8 / 0208 bases: does the α·β cross term scale with the amplitude?), (c) waiting for the human.
- b13 (5): S4 phase β=.20 on amplitude bases 68f6 (g3 .08), 8617 (.32), 6f32 (.40), 0208, 4ee8, to see how the α·β cross term scales with amplitude. Bare-parent reference from swarm-b: s21 0.789 at .20.

## 2026-10-13 22:58 — wakeup 16
- b13: the phase is an α·β synergy. At β=.20 the s21 ratio is ×1.44–1.55 on strong bases, ×1.02 on 68f6, ×0.79 on the bare parent. d48b full ladder: s21 3.919, r46 5.013, r56 4.882, conv46 5.078.
- swarm-c cma2 leader 4462: s21 4.182, r46 5.462, r56 5.344.
- Posted result ab62 + abandon/coverage posts for w3-profile (6653) and w3-offT1 (575d).
- Convergence worry: the conv46/r46 difference grows with β (b5d1 −0.07 %, 69c3 +0.23 %, d48b +1.3 %). The phase changes only off-diagonal kernels, which my trunc.py doesn't see. b14 (4, --diagnostic, family w3-convcheck): d48b and 4462 at s21 with gc10/nm64 and gc12/nm72.

## 2026-10-13 23:17 — wakeup 17
- b14 diagnostics: s21 converged (4462 4.1823 → 4.1773 at gc10/nm64 and gc12/nm72; d48b 3.9192 → 3.9135). conv46 − r46: 4462 +1.87 %, d48b +1.31 %, so probably qmax applied to the candidate only. Posted note + mailed swarm-c.
- Board: swarm-c cma2 s21 up to 4.82 (9d3e), r46 5.71. w2: swarm-b phase-cma s21 1.45.
- My active families are all closed. Remaining role: critic/verifier and answering the human. Budget 214/500.

## 2026-10-13 23:48 — wakeup 18 (final)
- No human reply. swarm-c 9d3e STRONG R_min 4.823 (boundary); d and e are wrapping up. Nothing high-value left for me. Running `swarm done` with the summary in work/done.md.
