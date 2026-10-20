# swarm-ap notebook

Started 2026-10-08T04:37:13+00:00.

## 2026-10-08 05:21 wakeup 1 (first)
- Read board: ~30 agents on low-shell w3 joint orbits / atlases; 4 on z3-w2. Leaders: swarm-i fa76 S1T1⟂ x=0.15 (s21 1.189, r46 1.156), fb45 S2T1∥ x=0.15 (s21 1.179, r46 1.171).
- Selection rules posted: swarm-h Z2xZ2 (pair (m,n)x(R1,R2) TL-allowed iff m≡R2, n≡R1 mod 2); swarm-j M·T (α on achiral, β on chiral).
- My niche: `tl-grad-w3` = gradient at the frontier in the 31 TL-allowed directions (20 achiral α + 11 chiral β), S1–S10×T1–T3. Tools: work/orbits.py (classifier, 31/126 invariant orbits, matches h/w), work/build.py (directions(), combine(), make_input()), work/showdef.py (print a req's deformation).
- Normalization: x = orbit unit-mean-square amp; per-product entry x/√nprod (3 or 6).
- Posted hypothesis 20261008T052059.608Z_swarm-ap_hypothesis_264f. Mailed swarm-i.
- Submitted b0: diagonal S1T1⟂=S2T1∥=x, x∈{.15,.20,.25,.30,.35}: d640, 0cfe, ca30, 4012, 1547. M2 ratio 1.21→2.27 (x=0.5 is outside the box).
- NOTE: early on I read swarm-i's worktree JSON by mistake (same campaign). From now on I use only `swarm show`.
- Next: pick the best center → 62-eval central-diff gradient (±0.04 x) on all 31 directions.

## 2026-10-08 05:46 wakeup 2
- b0 diagonal (x S1T1⟂ = x S2T1∥) s21: .15→1.364 (r46 1.329), .20→1.385 (r46 1.393), .25→1.321 (r46 1.313), .30→1.186 (r46 1.143), .35→0.997. Peak at x≈0.2; consistent with swarm-e's ridge (entry c⊥+c∥≈0.2).
- The frontier moved: swarm-au (nocomov-w3) base S2T1∥ x=0.3 (5059, s21 1.3905). Their ±0.1 gradient on 16 achiral non-co-moving orbits: a61f (+S9T1 mirror-sum x=−0.1) s21 1.569!, 771f (+S5T1⟂ x=−0.1) 1.497. So higher-shell slopes switch on at the frontier (my thesis), but au is measuring them.
- Pivot: complementary gradient at au's base: 3 co-moving α (±0.1) + 11 chiral β (±0.05) = 28 evals, batch work/g1, ids in work/g1_ids.txt. Mailed au with a split: au steps in its 17-D subspace, I take the full 31-D step.
- Board facts: chiral β ±0.1/term destroys (j); doubly-allowed chiral β small gains S4/S7/S9/S10×T1 (w, j); r46≫s21 for chiral β is suspect (k). LL0 control: the ⟂ gain needs w3's S3 harmonic (ao, as). numconv: small-amplitude leaders converged (l).
- Next: when g1 lands, combine it with au's 16 slopes → full gradient at B0 → full-space step + line search (~8 evals).

## 2026-10-08 06:10 wakeup 3
- g1 landed (28, all PASS). At B0 = S2T1∥ x=0.3 (1.3905), chiral β×T1 slopes per 0.05: S10 +.266, S9 +.205, S4 +.192, S7 +.131 (H≈0/+). T2/T3 β flat/concave. Co-moving: only S1T1⟂ +.097/0.1. Posted result 20261008T060938.624Z_swarm-ap_result_3caa.
- au's slopes (per 0.1) at B0: S9T1 α −.259 (H −.16), S10T1 α −.187, S5T1 α −.132; S9T2 +.169 (H −.59), S8T3 +.161, S5T2 +.117 ...
- Board leaders now ~2.0–2.5 s21: t 0e99 2.478 (S2T1∥ .33 + S1T1⟂ .13 + β S4 .089, S7 .034 + small α), am 08b5 (S2T1∥ .45 + β S4 .1) r46 2.06, j ba1f (S2T1∥ .346 + β all four .037) r46 2.23.
- Tool: work/decomp.py RID… projects any request onto the 31 directions. work/tab.py IDS BASE tabulates ± pairs.
- s1 submitted (10): β̂ step along the gradient (S10 .65, S9 .50, S4 .47, S7 .32), r∈{.08,.12,.16,.22}, ± the α step (S1T1⟂ +.1, S9T1 −.1, S5T1 −.1, S10T1 −.05), plus S2T1∥=0.4 variants. ids work/s1_ids.txt.
- Spent 43/500.

## 2026-10-08 06:30 wakeup 4
- s1 results (s21 / r46): ab4 r.12 (2848) 2.921/3.721; ab4 r.16 (7a96) 2.807/4.072; ab r.08 2.499/2.937; ab r.12 2.612/3.450; ab r.16 2.435/3.724; ab r.22 1.527/3.564; b r.08 1.866/2.204; b r.12 1.619/2.422; b r.16 1.178/2.383; b r.22 FAIL 0.69. All others PASS.
  → The α step (⟂+, S5/S9/S10 α −) makes the β tolerable; ∥ 0.4 > 0.3. The r46−s21 split grows with β (as j/k found). r56 is stalled board-wide (human asked by swarm-c).
- t 4a76 (∥ .53, ⟂ .215, S4β .142, S7β .054, dressing) s21 3.325 / r46 3.087 = best min-over-clusters.
- g2: 63-eval central-diff gradient at 4a76 (α ±.05, β ±.03), all 31 directions. Promotion gives r46 slopes too → a cluster-robust gradient. Mailed t.
- g2 submitted 06:43–06:48 (63 reqs, ids work/g2_ids.txt). A swarm check hung >10 min under node load 61; I killed it and submitted directly (the broker checks on submit).

## 2026-10-08 07:00 wakeup 5
- g2 s21 landed (r46 pending). Base a02f reproduces 4a76 s21 3.3252 (M2k 6.23 = 1.72×). Best probes: b_S9T1+ 3.467, b_S10T2+ 3.457, a_S9T2+ 3.450, b_S4T2+/b_S7T2+ 3.438. All 31 have H<0 now (local max-like curvature). NEW: chiral β×T2 slopes switch on here (S10T2 +.255, S4T2 +.18, S7T2 +.16, S9T2 +.13 per 0.03); they were flat at B0. Tables: work/g2_tab_s21.txt.
- The diagonal-Newton step (work/newton.py; predicts +1.47, which is over-optimistic) from s21: s2 submitted λ=.2,.4 + α-only/β-only at λ=.5 (0850, 2182, c5f8, 3a0e). λ≥.6 is rejected: Σ|α| > 2.5. **The frontier sits near the Σ|α| = 2.5 campaign boundary.**
- Mail: t keeps S9/S10 β off to protect min-over-clusters; y critique: t 4a76 Berry curvature goes negative in part of the BZ (C=1 still).
- Next: when the g2 r46 data land, post a result with both gradients; make the Newton step on min(s21, r46).

## 2026-10-08 07:30 wakeup 6
- s2: Newton λ=.4 **3a0e s21 4.388 / r46 4.390** (leader); β-only λ=.5 2182 4.177/4.170; λ=.2 c5f8 3.888/3.776; α-only 0850 3.784/3.699. 3a0e: Σ|α| 2.386 (box 2.5), Σ|β| .82, M2k/M2 1.74.
- g2 r46 gradient: all 11 chiral β positive on both clusters; α sign-consistent sets: + {S9T2, S10T2, S7T1, S5T2, S6T3∥, S8T3_30}, − {S1T1⟂, S2T2⟂, S4T1, S5T1, S9T1, S7T2, S1T2, S4T2, S3T3⟂, S8T3⟂}; disagree: S2T1∥, S10T1α. work/g2_tab.txt.
- s3 (7): B2 (=3a0e coefs, work/B2.json) β-only continuation λβ .6/.8/1.0 (dced, fd95, b967); B2 S1T1⟂ −.05/−.10 (a4f6, 84b0); robust Newton (newton2.py; avg s21/r46, sign-disagreeing dropped) α .25 β .6/1.0 (4547, 3b4d).
- Posted result f5be. Mailed z for a numconv check of 3a0e. TODO: after r56, post a `request` for a matched-density static control of the leader (α≠0).

## 2026-10-08 07:58 wakeup 7
- s3: robust step **4547 s21 5.203 / r46 5.414** (M2k/M2 1.61, Σ|α| 2.36, Σ|β| 1.19, split/Δ .0016/.013). 3b4d (β 1.0) FAIL: splitting/Δ .105. β-only continuation of 3a0e: fd95 4.665/4.799, dced 4.601/4.681, b967 4.504/4.690. S1T1⟂ −.05/−.10: 4.347/4.598, 4.274/4.627.
- z: 3a0e converged (48/8 +0.03%). as: 3a0e = 3.0× its equal-M2 static band. c critique: the Σ|α| L1 cap is chart-dependent, and it binds → report this frontier as a box-edge result.
- Posted result 78ff. g3: 62-eval gradient at B3 (= 4547 coefs, work/B3.json), ids work/g3_ids.txt.

## 2026-10-08 08:35 wakeup 8
- g3 landed (gradient at 4547; table work/g3_tab.txt). Best probes: e2f1 S1T2∥+ 5.430/5.565; many α slopes positive, but the Σ|α| cap binds (B3 2.363).
- KEY: α directions are disjoint in products → Σ|α| = Σ_d √n_d |x_d|. work/l1step.py solves the separable L1-constrained step (avg model, sign-disagree g=0, H floored at −.05); predicts +1.26 at cap 2.48 (diag model, so optimistic).
- s4 (7): β-only .5/1.0 (c882, 62e7); cap 2.40 s1 b.5 (f2f9); cap 2.48 s.5 b0/.5 (77fd, 4337), s1 b0/.5 (7877, 0328). The .coef files in work/s4 store the orbit coefficients.
- swarm-s runs a CMA around 4547 (mailed them the cap tip). Most agents have done `swarm done`; the active ones: me, s, t (paused), q (w2), z/others in reserve.
- Spent 186/500.

## 2026-10-08 09:33 wakeup 9 (after a session restart)
- s4: **0328 (cap 2.48, β .5) s21 6.655 / r46 7.107**; f2f9 (cap 2.40) 6.625/7.076; 4337 6.305/6.765; 7877 (no β) 6.027/6.347; 77fd 5.877/6.036; β-only c882 5.218/6.037, 62e7 4.860/6.525. 0328 split/Δ .0005/.007; M2k/M2 1.59.
- Posted result 558a, plus a request (matched-density control for 0328, r56 stall, Σ|α| cap reading).
- g4: gradient at B4 = f2f9 coefs (work/B4.json), α ±.04 (keeps every probe ≤ 2.5), β ±.03; ids work/g4_ids.txt (submitting in the background).
- NOTE: newton2.py/l1step.py hard-code α h = 0.05 → use 0.04 for g4!

## 2026-10-08 10:10 wakeup 10
- g4 (gradient at f2f9) landed; best probes 8946 (b_S10T2+) 7.227/7.272, 77af 7.141/7.229. All β slopes + on both clusters; many α slopes − on both (S1T1⟂, S2T1∥, S5T1, S9T1 ...). Table: work/g4_tab.txt.
- **Σ|β| ≤ 2.0 cap now binds too** (5 of 6 first-try steps rejected). l1step.py generalized: KIND=b HB=.03. HA=.04 for g4.
- s5: α-only L1 (c270); s5b α×{.5,1} β-L1×{.5,1} plus β-only .5/1 (2c01, 4414, 5287, a2e9, 28b8, bc16).
- au's critique (min(s21,r46) steps fit the split; r56 is the held-out test) accepted in note. Plan: stop climbing after s5; read the path on r56 when it lands; keep ~240 evals in reserve.
- Path for the r56 read: 3a0e → 4547 → 0328/f2f9 → 8946/77af → s5.

## 2026-10-08 10:42 wakeup 11
- s5: **28b8 (α L1 ×1, β L1 ×.5) s21 8.862 / r46 9.388**, M2k/M2 1.19 (!), split/Δ .016/.021, PES 4.21/4.45. c270 (α only) 7.879/8.511; 5287 7.759/8.456; bc16 7.620/8.418; 2c01 (β only) 7.477/7.559; a2e9 6.024/7.416; 4414 5.311/6.141.
- The α step shrank S1T1⟂ (.20→.08) and S2T1∥ (.53→.41) and grew S5T1⟂/S9T1 negative → M2k fell to 4.33 while R rose. R_beyondM2 5.1/5.4.
- ab submitted type-A (ρ̄, M2 3.417) and type-B (sharpened M2 5.782) controls for 0328 on s21/r46/r56.
- One more gradient (g5) at B5 = 28b8 (work/B5.json), α ±.04, β ±.03. Then stop; keep the reserve for r56.
- Posted result for round 5.

## 2026-10-08 11:18 wakeup 12
- g5 (gradient at 28b8) landed; best probes 8589 9.421/9.604, eabf 9.377/9.598, 37bc 9.352/9.541. Table: work/g5_tab.txt.
- ab's controls for 0328: type A (ρ̄ static, M2 3.417) 0.961/0.981; type B (static at M2 5.782) 1.367/1.369 → leader ≈5× beyond M2 (s21/r46). ab offered controls for 28b8 → asked yes; will send the final-path id.
- s6 (final climb step from 28b8, both caps 2.40/1.90): 7af1 (β .5), 077d (.5/.5), 7b04 (.5/1), 6c7b (α 1), 43a7 (1/.5), 1519 (1/1).
- After s6: STOP climbing. Reserve ~177 evals for r56 follow-up (r56 still stalled campaign-wide).

## 2026-10-08 11:50 wakeup 13 — SEARCH CLOSED
- s6: **077d (α .5, β .5) s21 11.269 / r46 10.535**; 43a7 11.041/9.799; 6c7b 10.238/9.452; 7af1 9.497/10.434; 1519 7.911/6.600; 7b04 FAIL (2.71, splitting). The s21−r46 sign flips (α favours s21, β favours r46). The PES gap is trending down (s21c N_A3 3.18).
- Posted the closing result with coverage (81dc): 323 evals, 320 PASS / 0 AMB / 3 FAIL. Asked ab for A/B controls on 077d and 28b8.
- f: qmax=8 truncation ≤ 0.4% at 8589 (null).
- Now WAITING for r56 (stalled ~6 h). Reserve 177. When r56 lands: read the path (5059, 4a76, 3a0e, 4547, 0328/f2f9, 8946, 28b8, 077d) on r56; post the held-out result; if robust, request conv46 / controls; then `swarm done`.
- 12:51: ab controls posted (7e11): 077d A .9425/.9445, B 1.1321/1.1323; 28b8 A .9385/.9415, B 1.1343/1.1346 → ~8–10× beyond M2 on s21/r46. r56 still stalled. Waiting.
- 13:50: r56 still stalled; q's conditioning audit: worst min/max S over top-26 w3 = 0.73 (null). Waiting.
- 14:50: r56 still stalled (~9 h). q and ab are done. Waiting.
- 15:51: no change; r56 still stalled.
- 16:52: no change; r56 still stalled.
- 18:08: no change; r56 still stalled (~12 h).
- 19:09: no change; r56 still stalled (~13 h). Plan: if r56 has not moved by ~2026-10-09 06:00 UTC, run swarm done with the summary (the r56 results land in the store regardless).
- 20:10: no change; r56 still stalled.
- 21:11: no change; s is done; r56 still stalled.
- 22:25: no change; r56 still stalled.
- 23:26: no change; r56 still stalled.
- 00:27 (10-09): no change; r56 still stalled.
- 01:28: no change; r56 still stalled.
- 02:41: no change; r56 still stalled.
- 03:42: no change; r56 still stalled.

## 2026-10-09 04:43 wakeup — r56 LANDED
- **077d STRONG**: s21 11.269, s21c 11.270, r46 10.535, r56 11.778 (held out), conv46 10.789; all PASS, C=1; split/Δ ≤ .014; PES ≥ 3.18. 43a7 and 7af1 are also STRONG (min 9.80, 9.50). 8589: r56 9.98, conv46 9.44.
- Posted the claim: 20261009T044421.885Z_swarm-ap_claim_4c7a. The r56 legs of ab's controls are still pending.
- Transfer test: the 077d and 28b8 deformation blocks applied to parent w2 (family w3path-on-w2, 2 evals): ids in work/w2x_ids.txt.
- TODO: read the r56 of the rest of the path when it lands; update the claim with the r56 controls; post the w2 transfer result; then swarm done.
- 05:16: w2 transfer FAIL (cf6f 0.0002, 9a11 0.137) → posted result. Path r56: only 8589 and 077d done so far; waiting for the rest and for the controls' r56 legs.

## 2026-10-09 06:17 — DONE
- af verified 077d: broad smooth max, all 10 probes PASS, 3 STRONG, boundary-limited. f r56 audit: no sign flips. 28b8 r56 9.64 / conv46 9.13.
- Ran `swarm done` with the summary (325 charged, 175 unspent). Loop stopped.
