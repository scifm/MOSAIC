# swarm-a notebook

Started 2026-10-14T05:19:46+00:00.

## 2026-10-14 05:20–05:30 UTC — wakeup 1 (first agent on the board)
- Read: theory note, 024 pilot (progress/40: +0.51% at 4x6 flipped to -0.92% at 5x6), progress/46 (Nk21 search≈confirm to 2e-5; w3 α[S1,T1]=+0.05 gave +1.85% at Nk21), ADR-0040.
- Parent w1c: s21 Δ = 2.2586e-4; r46 = conv46 = 2.4101e-4.
- Block = product stars only: γ = Σ (α/2 + iβ) O_s(r) F_p(k), both real cosine star functions (the odd-odd sin·sin joint-orbit sector is not expressible).
- Tools: work/gen.py (stars, build()), work/feed.sh FAMILY (submits work/pending/FAMILY/* into free in-flight slots; ids in work/submitted/FAMILY/ids.tsv).
- NAMING: in filenames T1/T3/T4 = |R|^2 = 1/3/4 = stars T1/T2/T3.
- Posted hypothesis 2e52, family `linmap`: 10 shells x 3 momentum stars x {α ±0.1, β ±0.05}, 120 evals.
- Submitted wave 1 (32: S1, S3, S4xT1/T2). 88 pending in work/pending/linmap.
- Next: feed the remaining waves as slots free; then analyse the map (linear coefficient + curvature per direction), post the map result, and plan the gradient-combination / CMA follow-up.

## 05:38–05:45 — wakeup 2
- linmap wave 1 done (32): S1 gentle (0.90–1.02 PASS), S3/S4 product terms are cliffs (0.0–0.75, mostly manifold FAIL). Posted note ca24.
- The board moved fast: swarm-b/c (joint orbits), swarm-i (comove P_n = S_n×T_n, G⊥R), swarm-d (MT rule: product-star β is even; all ladder clusters chiral), swarm-e/f/h (large α). Leaders: swarm-c f721 (|G|²4 × T1 G⊥R, α −0.06 per pair) s21 1.368; c5b8 (P orbit S1×T1) s21 1.202, r46 1.204.
- Dropped the β half of linmap (44 files → work/dropped). Fed 30 of the 44 α outer-shell points; 14 remain pending.
- NEW family mdctl (hyp d963): matched-density static controls. ρ̄ = BZ-avg of ρ_k (work/control.py, output in work/controls). Submitted 28d5 (ctl c5b8) and 6ef6 (ctl f721) on s21, r46, r56. ρ̄ differs from the parent by only ~9e-4 → expect R≈1.
- Posted a request to the human: is the control definition right, and can the block be extended to sin·sin?
- Next: feed the remaining 14 linmap α points; read the control results; post an mdctl result; controls for new leaders. Consider a unique search direction once the board settles (avoid herding on joint orbits).

## 05:58–06:15 — wakeup 3
- Both mdctl controls done: R_control 0.9989 (28d5→c5b8), 0.9992 (6ef6→f721) on s21, r46, r56, all PASS. Posted result 924d. Handed controls to swarm-q (m2ctl) and swarm-l (mdens), who run the same protocol; mailed both.
- linmap closed (62 evals, best 1.019). Outer shells ≥ 7 give R ≈ 0 at α = 0.1; kernel truncation was checked and is small (work/trunc.py). Posted result 92d3 + abandon f7ef. Remaining pending points moved to work/dropped/.
- Board: leaders are swarm-r ac14 (s21 4.44, r46 4.93; small α on even T1 orbits + β on odd), swarm-n trgrad ~2.8, swarm-i P1 line (c=−0.5: s21 1.88, r46 2.65). Optimizers: n, p, r, i, c, b. Plenty already.
- Checked: the solver H is normal-ordered with flat E_i, so there is no hidden one-body term.
- NEW role (analysis, no ED): `qgeom` = single-particle quantum geometry vs R_gap. work/geom.py computes C, σ_F/⟨F⟩, T = ⟨tr g − |F|⟩ from the links λ_0^{kk'}. Validated: LLL uniform (T=0); parent ideal (T=0) but σ_F = 2.07; ac14 σ_F = 1.89, T = 0.063.
- Running work/collect.py + work/geom_all.py on ~336 visible requests (background). Next: correlate R_s21 with σ_F, T; post the result. If a proxy works, offer it to the optimizers.

## 06:19–06:25 — wakeup 4
- qgeom: 325 requests analysed (work/geom_results.json). PASS: Spearman(R, σ_F) = −0.52 (s21), −0.68 (r46); T correlates positively. The P1/trgrad family flattens curvature (σ_F 1.16, T 0.49); ac14 does not (σ_F 1.89, T 0.06) → a finite-q mechanism. R² of the fit is 0.29, so not a proxy. Posted result 4d08 and mailed swarm-g (geoflat).
- swarm-q handed ρ̄ controls back to me (crossed hand-offs). I own them now. Submitted a440 (ac14), 203e (41dd), f032 (9de1) on s21, r46, r56. For the P1 large-α points ρ̄ moves (max dw 0.07, M2 8.79) → informative.
- Board: f/c test whether w1c is a "soft static point" (static frontier); f's kconv shows the top 9 converged; l asked for low_energies and a 27-site rung; b phase-only u1+u2 1.73/2.28; d S5T1 X phase 1.61/2.22; n says P1 −0.5 is a level-crossing plateau.
- Next: read the controls; post an mdctl update. Possible idea: a finite-q proxy (interaction-weighted form factor), only if cheap.

## 06:36–06:45 — wakeup 5
- My controls a440/203e/f032 finished and duplicate swarm-l's D1 controls (agree to ≤ 5e-4). swarm-l owns ρ̄ controls; I've STOPPED them.
- Leaderboard: r b55a s21 10.9 / r46 11.4; h josobol 53df 8.75 / 9.42. Top 12 all PASS with PES EG 3–4 and small split/Δ.
- work/contact.py: Python rebuild of TrialBandH2 (V = tanh(0.1q)/q). Validated: LLL contact cancels to 1e-15; parent converged at qmax 8. b55a: rel. err 1.5e-3 at qmax 8, 5e-5 at qmax 10 → not an artifact. ⟨|A|⟩ of b55a is 9× the parent's (≈ R). Posted note 97da.
- Running work/ascale_all.py (background): two-body scale proxy A/A_parent over the whole dataset. If it predicts R well, post it and offer it to the optimizers as a free pre-screen.

## 06:53–07:05 — wakeup 6
- Two-body scale proxy over 543 requests: R² 0.13, so weak. My "9×" in 97da was a 6-quadruple artifact; the robust ratio is ~2.5×. Posted CORRECTION + negative result 8b1d.
- Board: r claimed STRONG for ac14 (4.44/4.93/4.43/4.93); b claimed strong phase-only (ec27). f escale: interaction scale falls for the leaders. j: finite-size transfer (r46 is the high outlier). n: gate audit fine. e: a non-Laughlin 3-fold trap borders the phase-only sector. k: ℓ=2 field unifies the orbit levers (log-slope ∝ cos 2θ_GR).
- Trying work/pair.py: the two-particle spectrum on the 4×6 mesh (a V1-like pseudopotential proxy). LLL: top pair energy uniform, 3.94e-3. Parent top 0.122 (31× LLL!) yet the gap is only 1.24× → the top pair energy is not the Laughlin-relevant one. Looking at the full per-sector top-4 for references and leaders (background).
- If this doesn't separate quickly: stop the analysis line. Then either take a modest optimizer niche or wind down with a summary (77/500 used).

## 07:00–07:10 — wakeup 7 (key result)
- MECHANISM: e2 = sector-mean of the 2nd-largest antisymmetrised 2-particle eigenvalue (4×6 mesh). It predicts R: r46 R² 0.969 (n=191), s21 0.88, r56 0.99 (n=20), conv46 0.99 (n=18); R_r46 ≈ 0.95·(e2/e2_p)^0.65. The parent splits the LLL V1 doublet (e1 27× up, e2 below LLL); winners restore e2. Posted result 27fc (family pairspec).
- Tools: work/e2fast.py (3 s/eval, matches pair.py to 1e-9), work/coords.py (18 MT-clean T1 coordinates; b55a projects exactly), work/proxy_cma.py (CMA on log e2 ratio, boundary + admissibility enforced).
- Hypothesis 1f2e (e2guide): CMA run0 seeded at b55a, σ 0.05, 40 gens, running in the background (nohup, log work/cma/run0.log). Then submit ~10–15 designs along the proxy frontier (≤ 30 ED evals).
- Budget: 77/500 used.

## 07:33–07:40 — wakeup 8
- CMA run0 done (40 gens): best log e2 ratio 4.77 (e2r ≈ 118, predicted R ≈ 24). The trajectory left b55a: the P1 sign flipped; it leans on S7/S9 odd β and presses Σ|α| ≈ 2.0–2.4 and Σ|β| ≈ 1.8–2.0.
- Out-of-sample e2 test on c's static controls and g's flatness controls: the ordering transfers; rms log err 0.12 with an e1 term (log R = 0.650 log e2r + 0.072 log e1r − 0.05). Over-predicts when e1 collapses; blind to gap closing (6cc8). Posted note 0662; mailed c and g.
- Kernel tail of the CMA designs is large at g_cutoff 8 (L1 6–14 %) → set g_cutoff 14 / n_mesh 64 in the block (tail L1 6e-3).
- Submitted e2guide g00..g39 (10 reqs: 08ee 6ada 01d0 46be 30d7 9304 57ea 3125 25e3 39d1), plus diagnostic f501 = g39 at the default 8/48.
- Board: h c954 full ladder min 11.25; k's chiral ℓ=2 3bd0 s21 13.58 (i flags truncation); r claimed strong b55a (11.4). 87/500 used.
- Next: read the e2guide results; compare against the prediction; post.

## 07:53–08:05 — wakeup 9
- e2guide: 10/10 FAIL (best 08ee s21 7.66, split/Δ 0.39; the rest collapse to R ~ 1e-3). The truncation diagnostic f501 fails the same way. Proxy maximisation exits the phase. Posted result 4458 + abandon 0308. 88/500 used.
- Running work/phase_feat.py (background): top-4 pair eigenvalues per sector for all ~550 s21 requests, including FAILs → is there a phase classifier in the pair spectrum?
- Board: n's chiral projection of b55a (E− removed) gives 12.94/12.37/12.18; r 0f3b 12.17/11.97; q: leader blocks don't transfer to w3/w2; g closed geoflat citing e2.

## 08:05 — phase classifier
- work/phase_feat.json: top-4 pair eigenvalues for 554 s21 requests. e3 (V3-like) separates PASS/FAIL: AUC 0.89 for le3 alone, 0.83 for log(e3/e2); logistic CV AUC 0.965. Rule le3 < 6 → precision 0.975. e2guide failures sit at r32 ≈ −0.9; b55a at −1.50. Posted result 4131.
- Constrained CMA run1 (work/proxy_cma2.py: objective le2 − 4·max(0, r32 + 1.9), seed b55a, σ 0.04, 30 gens) running in the background → then ~6 ED designs as a falsification test.

## 08:32–08:35 — wakeup 10
- swarm-g independently reproduced e2 (R² 0.967); they suggest the harmonic mean of e1, e2. Leaders: n 2fb9 min 14.27 (k's chiral ℓ=2 E+ field + l0 breathing); k 3bd0 13.1; k says all 40 strong claims are one chiral E+ field. Many agents have posted final summaries (c, e, f, i, j, m).
- Leaders' pair features: le2 3.2–3.5, r32 −1.5 … −1.9, le3 ≈ 8.1–8.3. 5a1c (r46 FAIL) has r32 −0.73, le3 9.45 → the classifier flags it.
- Constrained CMA run1 (penalty r32 > −1.9): best feasible le2 3.62 at r32 −1.92. Submitted 6 designs (family e2c): c3c4 8b24 471f f57d 456c d693, at le2 3.56–3.62 and r32 −1.92 to −2.21; g_cutoff 14.
- Falsification: if these PASS with R ≳ 11, the (e2, e3) picture is a usable design tool. If they FAIL, it's a separator only.

## 08:50–09:02 — wakeup 11
- e2c: 6/6 PASS (s21 9.1–12.4, r46 9.8–11.7; 8b24 best, 12.41/11.68), against 0/10 unconstrained. Posted result 4ad8. 94/500 used.
- Leaders sit at lower e2 (2fb9 le2 3.31, r32 −1.58) but higher R → e2 under-predicts near the top.
- work/coords10.py: 42 MT-clean coordinates (10 shells × T1); 2fb9 projects exactly. e2fast kernel-converged for 2fb9 at 48/10.
- Running (background): refresh dataset + pair features → refit log R on (le2, le1, r32) → CMA objective for the 42-D run seeded at 2fb9.

## 09:05–09:15 — wakeup 12
- Refit on 534 r46 PASS points: log R = 0.696 le2 + 0.295 le1 − 0.067 (CV R² 0.977); r32 adds nothing within PASS.
- New leader: n 8f40 min 15.62 (λ=0.018 chiral E+ + l0 breathing): le2 3.53, le1 0.92, r32 −1.45, predicted 14.3 → the −1.65 threshold was too conservative near the top.
- run2 (seed 2fb9) stopped at gen 14 (lesson: pkill -f killed my own shell; use ps/kill by pid). run3: proxy_cma4.py (42-D coords10, NM64/GC12, objective = predicted log R − 4·max(0, r32 + 1.45)), seed 8f40, σ 0.03, 40 gens, background.
- e2c designs waiting on r56. Many agents are done (c d e f g i j k m p q).

## 09:24 — wakeup 13
- run3 (seed 8f40) done: best predicted R 17.9 vs 14.3 for the seed (8f40 actual 15.6). Submitted 6 designs d0..d5 (predicted R 16.1–17.9; r32 −1.46 to −1.75; |x−x0| 0.33–0.39; tail L1 ≤ 3e-3 at gc 14).
- The e2c c-designs are still waiting on r56.

## 09:47 — wakeup 14
- run3 designs: 6/6 PASS, s21 15.2–18.0, r46 14.1–15.6; 6619 is #2 (r46 15.57). The proxy over-predicts ~10–20 % at the top. n's ED trust region and my proxy CMA converge on r46 ≈ 15.6. Sum bounds near-binding (Σ|α| 2.0–2.4, Σ|β| 1.7–1.9). Posted result.
- Waiting for r56/conv46. Then: post coverage, write final summary, swarm done (100/500 used; the frontier is saturated and most agents are done).

## 10:18 — wakeup 15
- e2c run3 designs completed the full ladder, all PASS: 61e6 16.81/15.40/15.67/15.68 (min 15.40); 6619 min 15.20; a741 14.55; 962d 14.52; 2b58 13.37; ca2f 13.00. All strong-tier. The 8f40 leader is min 15.62.
- Submitted ρ̄ controls 2dc1 (61e6) and 9dcf (6619) on s21, r46, r56 (ρ̄ M2 9.79 / 9.89; max dw 0.02). After they land: claim post + final coverage, then summary + done.
- The earlier e2c c-designs are still waiting on r56 (GPU queue).
- Many agents are done: b, c, d, e, f, g, i, j, k, l, m, n, o, p, q, r.

## 10:39 — final
- Controls 2dc1 (61e6) 1.005/1.005/1.003 and 9dcf (6619) 1.009/1.008/1.008. Posted claim strong 71f7 (61e6 min 15.40) and e2c coverage 0bf0. Wrote the final summary and ran `swarm done`. 106/500 used.
