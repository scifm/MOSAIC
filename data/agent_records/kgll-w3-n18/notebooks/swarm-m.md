# swarm-m notebook

Started 2026-10-15T04:13:34+00:00.

## 2026-10-15 04:35 — wakeup 1: survey, role choice, first controls

**Board state.** Families: swarm-a w3-atlas (separable), swarm-b w3-joint (joint (G,R) classes),
swarm-c w2-atlas, swarm-e w3-bigamp, swarm-f w3-fsfloor (s21 floor via chiral mirror pairs),
swarm-g w3-chiral-phase, swarm-h w3-phase, swarm-i perp-matched, swarm-j w3-perp.
Leader: swarm-b f06f = S1×T1 class G⟂R, α=0.05 (pair-star rep): s21 1.105, r46 1.088, r56 1.092 PASS
(claim "suggestive"; now in converge stage). The ±30° classes lose both signs.

**Physics I worked out (and then found swarm-i/j had already posted it):** the G⟂R class with |R| = ℓ²|G| is
the "co-moving" term, e^{iG·r}e^{-ik·R_G} ∝ e^{iG·η} (cyclotron coordinate only), i.e. LL-mixing-like.
The chart is even in r AND even in k (O_s, F_p are cos sums), so cos·cos = ½(co-moving + counter-moving);
the sin·sin sector can't be represented (swarm-j asked the human).
Matched pairs in solver labels: S1↔T1, S2(|G|²=3)↔T2(|R|²=3), S3(|G|²=4)↔T3(|R|²=4), R_G=(n,−m).

**Decision:** three agents are already on the matched-⟂ classes, so I took the unclaimed role: mechanism controls (family `w3-mech`).
Hypothesis 20261015T043510.046Z_swarm-m_hypothesis_5426.
- Control A: static ρ̄ = <ρ_k>_BZ (ρ_k = |h_k|²/<|h_k|²>_uc, broker convention), projected on 8 shells. `work/control.py CAND OUT bzavg`.
- Control B (M2-scaled parent shape) is INADMISSIBLE on w3: its density goes negative (min ρ −0.006 at λ=1.011).
- Control C: same deformation on uniform LL0 (W_G=δ), compare with the `lll` parent's Δ.
- Fact: S3⊥ is M2-neutral (M2^(k)/M2 = 1.0017 at c=0.15), compared with 1.164 for S1⊥ and 1.138 for S2⊥ at the same c.

**Submitted:** e112 (A on f06f; s21,r46,r56), 5efe (C +0.05; s21,r46,r56), f33f (C −0.05; s21). 7 evals charged.
I built but did not submit the stage-A matched-⟂ inputs in work/inputs/A (they duplicate swarm-i/j); I keep them in case they're needed.
Tools: work/build.py (joint-class builder), work/showdef.py (show any request's deformation and results), work/m2check.py.

**Next:** read the control results. Mail the request-id authors with controls for large-α candidates once they reach r56.
Decide on the remaining ~430 budget: candidate gaps are w2 matched-⟂ optimisation, and a global multi-class search that includes the ⟂ classes.

## 2026-10-15 04:52 — wakeup 2: M1 results; leaving the control herd
- e112 (control A, BZ-avg ρ̄ static of f06f): R=1.0010 on s21/r46/r56, so the gain is not density. 5efe/f33f (uniform LL0 + S1⊥ ±0.05):
  Δ/Δ_lll = 0.978/0.968/0.971 (+0.05; s21/r46/r56), 0.962 (−0.05; s21). The gain needs the w3 harmonics (interference).
  Posted as result 20261015T045240.091Z_swarm-m_result_6629.
- Board: f06f is robust_positive (claim 1) with conv46 1.088. New leaders around 1.37–1.39 (swarm-h e9e8 on an S1⊥ α0.2 base, swarm-b 065b).
  w2: the gain is in the oblique 30/150 S1×T1 classes at α<0 (swarm-c/g, ~1.11 s21).
- Herding: 8 agents run controls (a,d,l,n,o,p,q,r,m). I stop running controls unprompted.
- The sign rule (swarm-c/p): gain where α·w_parent(G±G_R)>0. Counterexample: S1×T2 G∥R on w3 has G±G_R both on |G|²=4 but is even (swarm-b 2e34/1cfb). I mailed c and p.
- Now: work/harvest.py caches every visible request (work/store_cache.json); work/rule.py tabulates single-class probes, comparing the predicted G' overlap with the observed odd part.

## 2026-10-15 05:08 — wakeup 2b: rule table; new family w2-resonance
- Harvested 484 requests (work/harvest.py → work/store_cache.json, refresh takes ~10 min). work/rule.py prints the single-class odd-slope table.
- Finding: on T1 classes the G±G_R sign rule has 0 misses (w3 S1⊥ +2.72, S2∥ +2.61; w2 S1±30 −1.3; w2 S4T1⊥ gain); all failures are T2/T3.
  Posted as note 20261015T050608.269Z_swarm-m_note_5d24 and mailed o and r.
- Already taken by others: w3 outer T1 resonance (o, l), S2∥ + S1⊥ (r), recentred atlas at B (d), CMA-ES 14-D (a), chiral β at B (h, q), nematic (e, abandoned).
- The leader 7d04 (S1⊥ α=0.2): s21 1.369, r46 1.386, r56 1.306, conv46 1.386 = strong. Kernel converged (conv46 ≈ r46).
- NEW family w2-resonance (hypothesis 20261015T050719.905Z_swarm-m_hypothesis_8ca8): 12 w2 outer T1 classes × α=±0.1 (24 evals, work/inputs/W).
  Predictions: S7+10.89 (+), S7+70.89 (−), S13+43.9 (+), S16⊥ (+); weak: S7+49.11 (−), S13+16.1 (−); the rest ≈0.
  To analyse: odd slope = (R+ − R−)/0.2 per class.
- Budget: 7 + 24 = 31 charged.

## 2026-10-15 05:31 — wakeup 3: w2-resonance results; quasistatic probe
- w2-resonance A done (24 evals, all PASS, all <1 at ±0.1). Odd slopes: S7+10.89 +1.29, S7+70.89 +0.80, S7+49.11 −1.37,
  S13+43.9 −1.06, S13+16.1 +0.41, S16⊥ −1.94; controls S9 ±0.44 (class-blind), S12 0.03/−0.17, S13 76 −0.56, S16 30 −0.16.
  Activity partly predicted (~1.5× margin); sign 2/6. Even parts −0.15…−0.34 → single-class gain ≲3%.
  Result 20261015T052930.260Z_swarm-m_result_b212 (with coverage). Slopes mailed to swarm-e, who runs the w2 stacking CMA. I am NOT doing w2 stage B.
- Board: w3 leader swarm-p xcombo fe3d (S2∥ 0.25 + chiral β on S7) s21 1.695, r46 1.687. w2 leader swarm-c df59 strong (1.16–1.21).
  swarm-n: static sharpening of w3 reaches R 1.45 at M2=8 (controls). The k-GLL wins at matched M2.
- New mini-family w3-quasistatic (hypothesis 20261015T053117.910Z_swarm-m_hypothesis_a642): ⟨γ⟩_BZ=0 for every chart point, so static sharpening
  is only reachable via a Fejér F=1−K on the S4 shell. 3 diagnostics: aea0 (c+0.07), 7055 (c+0.141), fb69 (c−0.07). Expect <1.
- Budget: 31+3 = 34 charged.
- Ideas still open for me: (none strong). Consider the verifier role: the MT-partner control for β-containing leaders (fe3d has chiral β on S7).

## 2026-10-15 05:53 — wakeup 4
- quasistatic: aea0 0.355 FAIL, 7055 0.028 FAIL, fb69 0.369 FAIL. Closed; posted with coverage.
- Board: w3 leaders 2.4–2.9 (chiral β on resonant S7/S13/S19 classes + S1⊥/S2∥ α 0.25). c89a (j) s21 2.451 / r46 2.824. 02f7 (b) s21 2.38 / r46 2.59 / r56 2.53.
  w2 leader ≈1.19–1.23 (c's chiphase). Exploiters on stacking: a (CMA 10-D), j, h, b, f (phase stack), p, o, l, d, e (w2-stack), c, p (w2).
- Me: verification. Convergence replicates (n_mesh 96, g_cutoff 14; r46+r56, --control): e30e (c89a), 4df0 (02f7). Compare with leader r46/r56 and conv46.
- Budget: 34+4 = 38.

## 2026-10-15 06:15 — wakeup 5: convergence replicates
- e30e (c89a @96/14): r46 2.824272, r56 2.773773 vs leader 2.824281/2.773751 → kernel converged 1e-5; conv46 −0.107% = qmax effect.
- 4df0 (02f7 @96/14): r46 2.582795 (−0.104%), r56 2.525906 (−0.176%) — g_cutoff 7 slightly under-converged.
- Posted result (w3-verify-conv). b474 = cc13 replicate (swarm-a CMA top, s21 3.60 / r46 3.91, shells to |G|²=21 at g_cutoff 9) in flight.
- Board: leaders now 3.1–3.6 on s21 (a's w3-stack CMA, o's w3-radial). d and i finished early to avoid duplication.
- Budget: 38+2 = 40. Plan: report cc13; then probably `swarm done` (the board is saturated with exploiters, and my remaining niche is verification on request).

## 2026-10-15 06:37 — DONE
- b474 (cc13 @96/14): r46 3.909390, r56 3.775488 vs leader 3.909413 / 3.775404 → converged; conv46 −0.35% = qmax effect. Note 20261015T063625.297Z_swarm-m_note_37ce.
- Ran `swarm done` with a summary (40/500 charged). Stopping: the board is saturated with exploiters, and more budget would duplicate their work.
