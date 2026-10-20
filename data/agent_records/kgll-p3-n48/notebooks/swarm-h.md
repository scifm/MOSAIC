# swarm-h notebook

Started 2026-10-14T10:24:13+00:00.

## 2026-10-14 ~11:25 — wakeup 1: orientation, scope, batch 1
- Read brief, docs 40/46, theory §6.4, notes §5.4–5.8, §12. Parent w1c: s21 Δ 2.2586e-4, r46 2.4101e-4, r56 2.5901e-4.
- Derived the M·T (mirror x conj) argument: in TL separable β and chiral α have no linear term; TL-active = 72 mirror-even α + 54 chiral β
  (C6-invariant pair-product space, S1–S10 × T1–T3). Verified numerically (work/check_mt.py). Ladder clusters have no mirror
  (s21 C6 chiral, r46/r56 C2 only: work/geom.py). r46 aliases T3 pair ±(2,0) (ms 2): work/alias.py.
- HERDING: c, d, f, g all independently took joint orbit / chiral phase (same argument). Dropped my chiral-β batch (work/batches/chb1, NOT submitted).
- Chose role: `union` integrator — merge all maps into a quadratic model in the pair-product basis, trust-region steps.
  Hypothesis 20261014T112401.142Z_swarm-h_hypothesis_e593.
- Batch 1 submitted (24): mirror-even α orbit contrasts S4,S5,S6 × T1–T3 at ±0.05 (work/even_alpha.py, work/batches/eva1).
- Tools: work/chiral.py (pairs, orbits, block builder), work/even_alpha.py, work/gen_chiral.py.
- Next: when maps land, build work/union.py: pull each request's block via `swarm show`, project onto pair-product basis, fit gradient.

## 11:33 — wakeup 1 cont.
- Throughput is fast (minutes). Leaders: c's jorb chiral β S2T1 (|G|²=3) orbit 0.052 → s21 1.249, r46 1.404 (d698). α S2T1 orbits 1.18–1.22, r46 1.25–1.33.
- Data confirm M·T (34 image pairs, |ΔR| ≤ 2.4% on s21) — posted note 20261014T113200.342Z_swarm-h_note_4bf9 (+ Σ|α| bound is representation dependent).
- Response is very nonlinear: rms 0.05 moves R 0.42..1.25 on one line.
- Built work/union.py (pull+project, cache in work/cache), work/lines.py, work/model.py (per-line quadratic), work/mtpairs.py, work/gen_union.py.
- un1 submitted (12): additive Newton step over orthogonal measured lines, tracks a / b / ab, scales 0.25..1.0 (t clipped 0.1). Additive pred R ~2–3 at s=1 (surely optimistic).
- Herding again: o, u, t, x also pooled-model integrators; w & v duplicate S7–S10 even α (mailed both).
- Next: read un1; if additivity fails, pivot to something less crowded (T2/T3 profile of leaders? critique of PES/entanglement drop 20→4?).

## 11:47 — wakeup 2
- Queue congested; all 36 of mine still pending. 48 agents; heavy herding (c's note 05eb, p's note 6c59).
- e: manifold breaks at |α|≈0.1–0.2, |β|≈0.12 for full-star; a: outer shells at 0.05 FAIL; u: response kinked (min of branches).
- Decided: step back from pooled surrogate (o, t keep it). Posted note. After un1/eva1 land: post result+coverage, then choose verifier/critic or uncrowded niche.

## 12:14 — wakeup 3: eva1 hit
- eva1: S4T1 c0+ (353f) s21 1.572 / r46 1.720 / r56 1.614 PASS, C=1, in converge. S5T1 c0+ (8a8a) 1.498 / r46 1.594; S6T1 c0+ (99f8) 1.498 / r46 1.655;
  S4T1 c1− (631f) 1.259 / r46 1.259. T2/T3 copies flat or bad, several T3 FAIL. Minus signs lose ~50%.
- Board leader: perp-amp α_⊥ S1T1 (j/q/r ea28) s21 1.639, r46 2.632, r56 2.445, conv46 2.632 → "strong" claim already.
- Submitted eva2 (20): line scans t=0.025/0.075/0.10/0.15 for S4c0+, S4c1−, S5c0+, S6c0+ and combos c3/c4 at 0.025, 0.05. (work/gen_eva2.py)
- Posted result 20261014T121423.198Z_swarm-h_result_282d; mailed k for matched-density control of 353f.
- Idea: combine my outer T1 contrasts with the ⊥ S1 leader (and β chiral leader) — next after eva2.
- Charged so far: 36 + 20 = 56.

## 12:40 — wakeup 4: un1 hit
- un1 α+β: s21 1.909/2.817/3.766/4.760 PASS (1a1c/f821/9462/c662) at s=0.25..1. α-only 1.346/1.594/1.683/1.660F. β-only pending.
  353f conv46 1.7198 P (claim-eligible: robust/strong? check).
- t's orbsurr 8c01: 4.816 — same direction independently.
- Submitted un2 (11): (sa,sb) grid (work/gen_un2.py) up to (1.6,2.5).
- Posted result 20261014T...union step (res2).
- LESSON: digest output got truncated by head and marked everything read → lost 4 mails + 14 posts. ALWAYS `swarm digest > work/digest_<time>.txt` then read the file.

## 13:00 — wakeup 5: STRONG claim
- c662: s21 4.760 / r46 5.226 / r56 4.674 / conv46 5.226 all PASS C=1 → posted claim 20261014T130043.431Z_swarm-h_claim_0069.
  f821 (s=0.5) also STRONG 2.82/2.96/2.72. 353f STRONG 1.57/1.72/1.61, 8a8a 1.50/1.59/1.51, 99f8 1.50/1.66/1.55.
- Filed request 20261014T130044.195Z_swarm-h_request_ef0a for matched-density controls (c662, 353f).
- Others on c662: r (⊥ ablation), as (width), x (record + my outer T1 α), aa (add S3T1 chiral β). g critique: near-zero-mode amplification; p rebutted.
- Queue slow: eva2 (20), un2 (11), un1_b (4) pending. Charged 67.
- Digest now saved to work/digest_HHMM.txt.

## 13:27 — wakeup 6
- k's density controls: c662 0.995, 353f 1.000 → density excluded. 353f = clean beyond-M2 (no Q=0) STRONG. Posted note.
- un1 β-only: 1.446/1.711 (r46 1.467/2.027), FAIL at s≥0.75. So α+β > both alone (c's: superadditivity is cross-orbit).
- av: records are cos2δ (α) / sin2δ (β) angular rule on S1/S2×T1.
- eva2/un2 still SUBMITTED since 12:14/12:38 (broker stall, o reported).

## 14:00 — wakeup 7
- un2 s21: (1.25,2.0) 194b 6.593 best; (1.0,1.5) 5.415; (1.0,2.0) 5.433; (1.25,1.25) 5.797; (1.0,2.5) FAIL; (0.5,2.0) FAIL. Pending (1.5,1.5),(1.5,2.0),(1.6,2.5).
- eva2: outer lines peak ~1.55–1.66 at t≈0.075; combos FAIL at 0.05 — outer don't add at parent. S4c1− still rising at 0.15 → eva3 (t=.2,.25,.3) submitted.
- Board: o f5f1 6.28/8.33/8.12 record; s noQ0 line to 7.35; aa S3T1 β on records; Σ caps bind (t's request 789e). Several agents done (d, ak, p, g).
- Posted res3. Charged ~70.

## 14:28 — wakeup 8
- un2 full s21/r46: (1.5,1.5) 6.88/7.37; (1.5,2.0) 7.58/8.40; (1.6,2.5) 017f 8.28/9.08 (Σ|α| 2.43 cap). r56 pending.
- eva2 r46: outer lines grow on r46 (S4c0 t=0.1: 1.59→2.40; S5c0 2.20; S6c0 2.27; c4 2.13).
- Board: av cos2δ+i sin2δ rule s21 10.39 at cap; x outer at c662 7.22/8.20; r ablation: no-⊥ keeps 83–93% of c662; records cap-limited (ae); u: qmax 8 non-PSD at R~10.
- Submitted un3 (4): drop low-yield α blocks (separables S2T2/S2T3/S3T*), reinvest Σ|α| into S1T1/S2T1/S1T2 (A,B,E) or S1T1/S2T1 only (C), β to Σ 1.98.
- Charged ~77. Plan: after un3, post coverage result; consider `done` (frontier crowded: av, o, x, z, w...).

## 14:56 — wakeup 9
- un2 corner 017f STRONG 8.28/9.08/8.54/conv 9.09. 194b 6.59/8.03/7.06; 454b 7.58/8.40/7.54.
- un3 (cap reallocation, drop separable T2/T3 α): B 1c8a s21 11.07 (board s21 high; av e0a8 10.39/9.87/10.50), A 10.71, C 10.84, E 9.15.
- My step follows angular rule (cos 0.94/1.00): work/rule.py.
- eva3 S4c1: t=0.2 1.58, 0.25/0.3 FAIL → S4c1 line peaks ~1.58–1.59 at t≈0.15–0.2.
- Submitted un4 (4): reallocate 15–30% cap onto S3T1 rule (work/gen_un4.py). Posted res4. Charged ~84.
- Next: un3/un4 ladder; then coverage post; consider done.

## 16:34 — wakeup 10
- un3 ladder: B 1c8a 11.07/10.24/9.63/10.24; A 10.71/9.98/9.23; C 10.84/10.66/9.67.
- un4: 5063 (S3T1 15/15) 11.65/12.30/11.97/conv 12.29 STRONG (#9 board); 8594 (30/30) 11.61/12.24/12.38/12.28; cad3 (β20) 10.16/11.64/11.34; e096 (α20) 12.14/10.97/10.37.
- Board frontier min ≈ 12.2–13.3 (w 407a outer, av 55f9, al a8c1 lowsym). u: qmax truncation at R>11 (asked u to prescreen 5063/8594).
- Posted claim 20261014T163405.971Z_swarm-h_claim_406b. Charged ~88.
- Plan: low-activity mode; respond to human answer on Σ caps / u's prescreen; write coverage post; done when nothing distinct left.

## 17:07 — wakeup 11: closing
- u: 5063 is the cleanest R>11 point (qmax-clean). k asked for 5063 density control.
- Board converged on the angular rule; frontier is cap-limited, crowded (av, w, x, t, o, s, z). Many agents done.
- Posted coverage result 20261014T170641.380Z_swarm-h_result_a37a. 78/500 charged; 61 PASS / 17 FAIL at s21.
- Calling `swarm done`.
