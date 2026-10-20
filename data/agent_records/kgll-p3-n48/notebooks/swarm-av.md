# swarm-av notebook

Started 2026-10-14T10:26:42+00:00.

## 2026-10-14 11:38 — wakeup 1: orientation, family `kprof`
- Board: ~30 families, ~20 agents herded on S1/S2×T1 joint orbits; 4 pooled surrogates (h,o,t,u); CMA on min-over-clusters (z,n,ag,am); nematic x3 (ad,ah,al).
- Leader: c `…req_d698` S2×T1 +60 β+0.03/entry phase-only: s21 1.249, r46 1.404 (r56 pending). e: full-star breakdown at |α|≈0.1–0.2, |β|≈0.12.
- My choice: c's thin spot 4 → `kprof` (hypothesis `…av_hypothesis_1724`): T2/T3 copies of S1–S3 α orbits (stage 1, 24 evals submitted 11:38), then T1+T3 profile shaping on the four T1 leaders (stage 2).
- Tools: work/gen.py (orbit(s,p,delta), write(path, entries)) — pairings verified against c's. work/stage1.py. Files work/s1/g{s}r{p}_o{δ}_a{p|m}.json.
- Caveat: r46 samples T3 pair ±(2,0) with mean square 2 (h) — T3 gains bigger on r46 are suspect.
- Mailed c, g about overlap.
- Next: read stage-1 results; design stage 2 (T1 best + T3 ±0.025/±0.05) on S2∥ α+, S2+60 α−, S1⊥ α−, S1+30 α+.

## 12:01 — wakeup 2
- 6 agents on the inner T2/T3 orbit map (e, ao, av, aj, ar, i). Withdrew my S3×T3 four (e has ±0.03). Dropped stage 2 (shaping: ao/aj/au).
- New role (note `…av_note_777c`): merged, deduplicated table of the inner S1–S3×T2/T3 map from all six agents; flag T3 r46 aliasing (±(2,0) ms 2 on r46).
- First results: S2×T2 ⊥90 α− 0.9891 (b619), α+ 0.8215 (01bf). Weak, as g found.
- Board: c STRONG claim d698 (1.249/1.404/1.347). f e5d5 S3×T1 chiral-odd β +0.05: 1.558/1.641. ⊥ α −0.45: 1.64 s21 / 2.63 r46 (branch change suspected, ak). u: S2 leaders use 30–50% of s21 split gate.
- Tool: work/mystatus.py (my requests with file, R, split/Δ).
- Next: when stage 1 lands, collect others' T2/T3 data (swarm show by id from their result posts) → merged table + coverage post. Then look for a non-crowded direction for the remaining ~480 evals.

## 12:31 — wakeup 3: new family `cos2d`
- Queue slow: kprof stage 1 still pending after ~50 min (24 charged incl. the 4 withdrawn S3×T3; withdraw ≠ cancel).
- ar claims the full inner T2/T3 α map; i withdrew α. My merged-table role stands (i's β points: S1×T3 +30, S2×T2 +30, S2×T3 +60 ±0.03, ids in i's note).
- Observation: all T1 α gains obey α·cos2δ>0 (δ=∠R−∠G): S1 ⊥−/±30+, S2 ∥+/±60−, S5/S6/S4 c0+ (h). h misread S2 sign; mailed h. Exception: h S4 c1−.
- Hypothesis `…av_hypothesis_0649`; stage 1 = 13 evals in work/c1 (A: S1–S3 α μ .01–.045 & −.02; B: all shells g=w_s/w1; C/D: complex with β=μ/2, μ·sin2δ/sin60). Generator work/cos2d.py (block(shell_w, tstars, mu_a, mu_b)).
- Note: cos2δ on S1–S3 lowers M2^(k) (ratio 0.998 at μ .045).
- Mailed b, ab, h.
- Next: read c1 + kprof results; stage 2 = shell profile & mix ratio & turnover.

## 13:07 — wakeup 4
- Board: records at R~5 (h c662 STRONG 4.76/5.23/4.67/5.23; t 8c01 4.82/5.19/4.55). Superadditive α+β union steps. Density controls (k) all ≈1 or <1.
- v confirms cos2δ on S7–S10×T1, slope ≈4×projection uniform in |G| (mail; my stage B weights are too weak outer).
- 0-eval result `…av_result_ddbc`: records are 78–98% cos2δ in α on S1/S2×T1 (+T2), β has the sin2δ sign; no S3, T3 or outer. work/project.py does the projection (reads the ed_input path from swarm show).
- kprof data: S1×T3 is ANTI-rule (⊥ α+ 1.0459 c400, α− 0.939); S2×T2 follows the rule weakly (+30 α+ 1.012). T3 sign flips (f's S1×T3 odd b− also gains).
- Stage 2 submitted (12, work/c2): E1 S1–S3 T1 μ .06–.13; E2 S1–S2 control; E3 +T2 half; E4 S1–10 outer .25; E5 +T3 −0.5. β/α=0.7 per entry. L1 bound binds near μ 0.1 with T2/outer.
- Next: read stage 1/2; if E1 > record, push μ/ρ; coverage posts for kprof + merged table.

## 13:38 — wakeup 5
- kprof data in: S3×T1 ⊥ α− 1.368 (af3d, split 0.04), ⊥ α+ FAIL; +30 α+ 1.016 (split 0.077). S2×T3 anti-rule, narrow window (∥α+ FAIL, +60 α− FAIL). S1×T3 ⊥ α+ 1.046/r46 1.062 (anti-rule). S3×T2 ∥ α+ 1.034, α− 0.690.
- e: S3 is ~3× steeper than S1 → weight S3 ≈0.35 in the next stage. f: phase-only s21 ceiling ≈1.72. Records ~4.8 (α+β). aj: T1+T3 shaping does not help. Stuck-lane reports (o, j) — my stage-1 cos2d is still pending after 1 h.
- Next: write the kprof coverage/merged table once S3×T3 lands; read cos2d stage 1/2; stage 3 = complex rule with S3 at 0.35, maybe outer uniform on top of the best.

## 14:13 — wakeup 6: BIG — E1 line
- cos2d E1 (S1–S3×T1, α=μcos2δ, β=0.7μ sin2δ/sin60): s21 7.07 (5c15, μ.06), 8.94 (b7f3, .08), 9.67 (0d8f, .10), 10.39 (e0a8, .13), all PASS, split ≤0.065, eg N_A=3 ≥1.6, S00 0.13, M2k falls. Board's previous s21 record 6.28 (o f5f1). Σ|α| 2.34 at μ .13 (cap 2.5 → μ≤0.139).
- α-only saturates ~1.69 (μ .03); complex removes the ceiling (C/D: 2.5–3.3 at μ .02–.03).
- B (all shells at w_s) FAILs at μ ≥ .03 (splitting).
- kprof: S3×T3 mostly FAIL; S3×T2 ∥ α+ 1.034 but r46 0.775 (sign flip!).
- Posted `…av_result_19a6`. Stage 3 (work/c3): ρ frontier, S3 half (μ to .165), S1–S6. F5 no-S1⊥ ablation `…_141f`. Mailed k for density controls.
- Next: watch r46/r56 for E1; if they hold → claim. Then kprof coverage post. Consider the human request on the cap reading (t asked already).

## 14:42 — wakeup 7
- e0a8 full ladder: 10.39/9.87/10.50/conv46 9.96 all PASS → CLAIM `…av_claim_8f85` (STRONG). 0d8f: 9.67/10.49/10.35, conv46 pending.
- E4 (S1–10, outer .25, μ .04): s21 12.51 PASS (55f9; split .067); μ .06/.07 FAIL. E3 (+T2) FAIL; E5 (+T3 −.5) 1.91; E2 (no S3) 4.97/6.78.
- Stage 4 (work/c4, 7) around E4: outer weight .10/.15/.25, μ, ρ=1, S3 half, S7–10 only.
- kprof closed with coverage (`…kprof closed`).
- Others: x/a add outer α/β to e0a8; z runs CMA around e0a8; u: qmax-8 non-PSD (conv46 resolves, +0.9%).
- Next: watch the F/G stages and the E4 ladder; density control from k; F5 ablation (no S1⊥).

## 16:56 — wakeup 8
- 55f9 STRONG: 12.51/12.71/12.79/conv46 13.00, M2k 10.497 (+4.6%), half the caps → CLAIM `…av_claim_f629`. Asked k for its density control.
- e0a8 density ctrl (k 0a3b) 0.993/0.989/0.990. No-S1⊥ ablation 141f (μ .10): 8.60/9.85/9.67/9.87 vs 0d8f 9.67/10.49/10.35/10.51 → 89–94% kept.
- Gate map: above min ~12.5, r46 splitting binds. β/α ≥0.85 breaks r46. S4–6 at .4 too much. 7b3e min 12.17, e6c4 11.49 (r46), aaeb 11.30.
- Board: w builds on 55f9 + outer S7–S10 (407a min 13.26, qmax caveat); x, z, t, s, h, o all ~11–12. Many agents finished (done).
- Stage 5 (work/c5, 8): β/α 0.5–0.6 to buy amplitude under the r46 gate; outer weight .2/.25/.35; S4–6 at .1.
- Next: read c5; if H-points beat 55f9 on min → claim; then think about ending (coverage post for cos2d).

## 17:30 — wakeup 9
- Stage 5: lower β/α helps r46. 023e (μ .05 ρ .5): s21 13.69 / r46 13.46; b594 (μ .055 ρ .5) 13.85/13.16; 92c7 (out .35 μ .035 ρ .6) 13.26/13.30; 6143 13.11/13.22; b85d 13.05/13.12; 5ea4 13.21/13.21. r56 pending. s21 split ~0.06–0.07 now binds.
- k: 55f9 density ctrl 1.005 → beyond-M2 by the brief. u: 55f9 is qmax class B (qmax 8 understates).
- z rcma2 centred on 023e. Many agents done.
- Stage 6 (work/c6, 6): ρ .35–.5, μ .05–.065, outer .2/.25/.3, S3 .8.
- Next: claim the best H/I point once the ladder lands; cos2d coverage post; then decide whether to stop.

## 18:03 — wakeup 10
- 023e full ladder 13.69/13.46/13.61/13.77 → CLAIM `…av_claim_b517`. Plateau: 9 neighbours at min 13.1–13.4; μ>0.055 trades r46 for s21.
- Density control for 023e submitted myself (`…av_req_72f5`, work/control.py, k's recipe; truncation negativity → harmonics ×0.970, M2_ctrl 9.29). The script reproduces the broker M2^(k) exactly.
- Board: w a8eb min 14.56, z e327 14.23 (built on the rule). Most agents done; k closed.
- Plan: next wakeup → stage-6 ladders + control → cos2d coverage post → swarm done (family saturated; remaining directions owned by w/z).

## 18:38 — wakeup 11
- Stage 6 ladders: 1125 min 13.41, db2e 13.37, d43c 13.22, 2475 13.36, 7fec 13.11, 0765 11.86 (r46). Plateau confirmed; 023e (13.46) is the family best.
- 023e density control 72f5: s21 0.978 (r46/r56 control rungs `…_cd1f` queued).
- cos2d coverage posted (`…av_result_a28c`).
- Add-on (hypothesis `…av_hypothesis_3c9d`): residual cos4δ⊥{1,cos2δ} α on 12-member shells at 023e, 6 evals (work/c7).
- Frontier on board: w a8eb 14.56, z e327 14.23 (rule + per-shell freedom).
- Next: read c7 + control → final note → swarm done, stop the loop.

## 19:12 — wakeup 12
- Add-on c7: −ε residual (cos4δ⊥{1,cos2δ}) on 12-member shells GAINS (opposite to prediction): fd2d ε −.025: 15.48/14.58/14.16 (min 14.16; conv46 pending); 866f −.0125: 15.03/14.14/14.16; S4-only − : 13.60. +ε loses.
- Cap binds (fd2d Σ|α| 2.39). Not using star regrouping. Cap-neutral trades (c8, 6): outer .15/.2/.25, μ .045/.05, ε −.03…−.04, all four shells or S7–10 only.
- 023e control: s21 0.978, r46 0.976 (r56 pending).
- Posted the interim result.

## 19:45 — wakeup 13
- fd2d full ladder 15.48/14.58/14.16/conv46 14.81 → CLAIM `…av_claim_a9e8`. The residual saturates on r56; cap-neutral trades lose (r56 ~12.7). fd2d is the family optimum in the box.
- fd2d density control submitted (a8b4 s21, fa30 r46/r56; positivity shrink 0.943, M2_ctrl 8.76).
- Board leader: w 256c min 15.09.
- Next: read the controls → final note → swarm done → stop the loop.

## 20:10 — final
- fd2d density control: s21 0.952, r46 0.949. 023e: 0.978 / 0.976. r56 rungs still queued.
- w 256c (min 15.09) is at Σ|α| 2.42, so my residual can't be added without a cap trade.
- swarm done posted. Loop stopped.
