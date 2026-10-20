# swarm-n notebook

Started 2026-10-14T10:24:34+00:00.

## 2026-10-14 wakeup 1 (11:16–11:40 UTC)
- Read brief, docs 40/46, theory §2/§5/§6.4/§8, board (a,b axis maps; c jorb; e bigamp; d,f chiral phase; g joint-orbit;
  h,o,u pooled surrogates; x combos; q,y finite size; j,r perp amp; k,s mechanism; v,w high-shell α; ad nematic; af survey).
- Key board facts: joint (G,R) orbits carry big linear slopes at s21 (c): G1R1 +30° β+0.03 → 1.1595 (ce1f), r46 1.1586;
  G3R1 (S2×T1) +60° β+0.03 → 1.2494 (d698); ∥ α+0.05 → 1.2166 (37dc); ⊥ G1R1 α−0.05 → 1.1709 (7133), r46 1.1699.
  MT symmetry (mirror×TR) holds on s21 to <1 %: R(+θ,β)=R(−θ,−β), R(+θ,α)=R(−θ,α). r46 tracks s21 to <0.6 % at small steps.
  Outer separable stars (|G|²=9,12) at α=±0.05 → R≈0.4–0.6: strong negative curvature, no first-order value.
- My family `minmax` (hypothesis 20261014T113214.052Z_swarm-n_hypothesis_3e62): CMA-ES with fitness = min R over
  clusters reached (promotions free), in 27-D TL-active orbit coords (work/tlcoords.py: per channel G{1,3,4}×R{1,3,4}:
  a_self, a_pair, b_odd per pair entry). Lanes: `joint` (27-D, λ=10, σ0=.015) and `beta` (9-D b_odd, λ=8).
  Representation verified: G1R1:b_odd=.03 ≡ ce1f+c75e blocks (|Δγ|=6e-17, work/check_equiv.py).
- Driver: `python3 work/minmax.py step joint|beta` (run from work/); state work/minmax/<lane>/state.json; idempotent:
  waits until every request in the generation has result.status == done.
- Submitted: probe 6b28 (G1R1 b_odd +0.03, additivity of MT-partner orbits), joint gen0 (10), beta gen0 (8). Charged 19.
- Next: step both lanes when gen0 ladders finish; watch r56 of c's leaders; post critique if s21/r56 diverge.

## 2026-10-14 wakeup 2 (11:57 UTC)
- My 19 requests not yet run (broker backlog). Board moved fast: c CLAIM strong phase-only S2×T1 +60° β=.03 (d698):
  1.249/1.404/1.347 (s21/r46/r56). f: chiral-odd β per-entry ≈ b_sep/3; G4R1 (|G|²=4×T1) b_sep=+.05 → s21 1.558, r46 1.641
  (e5d5); G3R1 +.05 → 1.483; G1R1 +.10 → 1.381 (5098). T2/T3 weak/negative. u audit: |G|²=3 leaders use 30–50 % of the
  s21 splitting gate (split/Δ 0.03–0.05), r46 cleaner → s21 gate will bind before R peaks. e: full stars break the
  manifold at |α|≈0.1–0.2, |β|≈0.12. k: matched-density control for α⊥ explains none of the gain.
- Agreed with ag (mail): stop my β-only lane after gen0 (ag's fsmin 24-D β covers it). Keep 27-D joint lane.
- Plan for gen1: if gen0 shows many gate FAILs, restart CMA from the board's best combined point with smaller σ
  (~0.006 per entry) — per-entry slopes are ~30/unit on G3R1/G4R1 b_odd, so σ .015 is a big step there.

## 2026-10-14 wakeup 3 (12:23 UTC)
- Broker backlog: 893 SUBMITTED vs 20 RUNNING, ~10 evals/min swarm-wide → my gen0 (11:34) still unrun. Expect ~1.5 h/generation.
- Board: STRONG claims: α⊥ G1R1 a_self −0.45 (e99d/ea28/c027): 1.639/2.632/2.445 (s21/r46/r56), matched-density control
  (k) explains none; f e5d5 G4R1 b_odd .0167: 1.558/1.641/1.560 phase-only; c d698. x d524 (G1R1 a_self −.05, b_odd .015,
  G3R1 a_self .05, a_pair −.025 + MT-odd residual) s21 1.923, r46 2.149.
  s21 manifold splitting is THE binding gate (q, u): s21 sp/Δ grows 8–30× faster than r46's; min-over-clusters = s21.
- Wrote work/project.py: projects any request onto my 27 coords (+ residual, + split/Δ per cluster).
- Started lane `joint2` (warm mean: G1R1 a_self −.15, b_odd .015; G3R1 a_self .04, a_pair −.02, b_odd .005; G4R1 b_odd .01;
  σ .008, G1R1 a_self scaled 3×). gen0 submitted (10). Old `joint` lane: let gen0 finish as data, then stop it.
- Mail: z (rcma 18-D T1 α+β, agreed split), q (s21 split gate binds; use sp/Δ as constraint).

## 2026-10-14 wakeup 4 (12:56 UTC)
- Records now ~4.7–5.2: h c662 STRONG (4.760/5.226/4.674/5.226), t 8c01 (4.816/5.186/r56 ~4.55). Response in TL-active
  orbit space is strongly SUPERadditive (h: α·β), not concave; s21 split gate still the binding constraint.
- My first results (old joint gen0): e3da (c09, random sample) s21 3.916 PASS sp/Δ .004; 36b6 2.798; eef2 2.712 FAIL
  (sp/Δ .182); beta-lane 3386 1.687. A random 27-D sample at σ .015 hitting 3.9 → gain is generic in the TL-active space.
- Added to minmax.py: board_elites() (leaderboard top, projected, residual/norm) + maybe_restart(): after each tell,
  if a board elite with residual <10 % beats the lane best by >5 %, restart the lane mean there (island model).
  Currently c662 (resid 3 %) would be the restart target.
- beta lane: stopped (ag covers β-only); its gen0 is data only.

## 2026-10-14 wakeup 5 (13:28 UTC)
- joint gen0 told: fits [2.448, 1.535F, .031F, 2.195, 2.798, .339F, .760F, 1.660, 1.356F, 3.553]; e3da (random c09)
  completed full ladder 3.916/3.571/3.553/3.571 → STRONG-eligible (min 3.553). 5/10 FAIL (manifold split) at σ .015.
  beta lane gen0: 6/8 FAIL (am also: random phase-only directions FAIL) → lane stays dead.
- Fixes: status "failed" counts as done; converge-stage with r56 present counts as done (conv46 ≡ r46 for S1–S3).
- joint gen1: restarted at board elite o f5f1 (s21 6.28, ladder partial). 10 submitted. joint2 gen0 still unrun.
- Board: claims STRONG c662 (h), 8c01 (t); k: density controls exclude density for α records; ap: leaders' γ on uniform
  LL0 LOWER the gap → gain is γ×ρ* cooperation; av: records follow α∝cos2δ, β∝sin2δ angular rule.

## 2026-10-14 wakeup 6 (14:01 UTC)
- Records s21 8.71 (t 6506), 8.08, 7.35 (s 9a30 noQ0, linear to t=4, no turnover), 7.22 (x d2de); f5f1 (o) s21 6.28 /
  r46 8.33 / r56 8.12. No turnover along the record rays; the binding constraint is becoming the Σ|α|/Σ|β| caps
  (representation-dependent: t request 789e). Phase-only s21 ceiling ≈1.72 (f, gate-limited).
- My lanes: joint gen1 (restart at f5f1) and joint2 gen0 both still queued. Nothing to tell yet.
- Decision: keep CMA running (cheap; independent boundary optimizer on min-over-clusters), avoid adding more
  ray-pushing families. Look for a critique target next wakeup (rule 11; 0 critiques so far).

## 2026-10-14 wakeup 7 (14:32 UTC)
- Records ~10: av e0a8 (cos2δ+i sin2δ rule) 10.39/9.87/10.50 (s21/r46/r56); s c325 9.87/10.15/9.53; at Σ|α| cap.
  u: qmax-8 projected pair interaction non-PSD for R≈10 records (fixed at qmax 10) → conv46 (qmax 10) is the real check.
- joint2 gen0 all PASS (2.0–4.2 s21); told with r46-based estimate (new: if r46 in and r56 pending, add 0.96·r46 to
  the min instead of waiting — y: r56 ≈ 0.96 r46). Best 8def 3.92. Restarted joint2 at av e0a8 (9.87); gen1 submitted.
- joint gen1 (restart at f5f1) still unrun at s21 since 13:29 (queue).
- Both lanes now explore the cap boundary around the records; repair rescales to Σ|α| ≤ 2.4, Σ|β| ≤ 1.9 (my pair-star rep).

## 2026-10-14 wakeup 8 (15:05 UTC)
- Records s21 13.9 (w 407a), 12.5 (av 55f9/7b3e), 11.8 (x). u f0fa: qmax-8 pair spectra non-PSD at R≈13–14.
- Posted audit note 2e92 (critique #1): conv46/r46−1 ≤ 0.03 % for R<8.5, +0.06…+0.88 % at R≈9–10.5 (positive);
  R≈12–14 points need conv46 before quoting. Mailed u.
- joint gen1 (f5f1 restart): 5/10 FAIL, PASS ones s21 3.4–6.4 (f0a2 6.33/r46 8.34; 5b42 6.39/7.94). σ too big near cap.
- joint2 gen1 (e0a8 restart): 10/10 PASS s21 9.49–10.70; 70c4 10.70/11.16, d769 10.55/11.49, c359 10.57/11.11.
  Waiting r46 for the rest.
- NB: my "near_done" shortcut treats conv46 ≡ r46; at R≳9 conv46 differs by up to ~1 % — acceptable for CMA ranking.

## 2026-10-14 wakeup 9 (16:35 UTC)
- Board: STRONG records min 13.26 (w 407a, includes outer S7–S10 cos2δ α), 12.51 (av 55f9), 12.44 (al a8c1, lowsym);
  inner-shell-only STRONG h 5063 11.65/12.30/11.97/12.29. an: above s21≈12 the r46 manifold gate binds.
  Many agents posting final summaries.
- joint gen1 told (best 5b42 6.39); restarted at h 5063 (11.65) → gen2 submitted.
- joint2 gen1 told: fits 9.35–10.70, all PASS (best 70c4 10.70); restarted at e b7a3 (11.68) → gen2 submitted.
- Plan: 2–3 more generations in the inner-shell (S1–S3) 27-D space to locate its capped maximum, then post
  result with coverage and stop. My space excludes S4–S10, so it cannot reach the outer-shell records.

## 2026-10-14 wakeup 10 (17:09 UTC)
- joint2 gen2 (restart at e b7a3): all PASS, best c9e2 s21 13.04 / r46 12.39 (r56 pending; est min 11.89) — purely
  inner-shell (27-D, residual 0) → above h's inner-shell STRONG 5063 (min 11.65) if r56 holds.
- joint gen2 (restart at h 5063): best 9284 11.50/12.03/11.55 (r56 in) → STRONG-eligible min 11.50.
- Both lanes restarted at w 39cd (12.73) for gen3 → redundant islands now. y/u: above R≈9 qmax-8 rungs are
  unconverged (conv46 shifts up to +20 %), so s21 chasing at R≈13 is partly numerics.
- Decision: gen3 is the last generation. Then post result + coverage, and `swarm done`. ~99 evals total.

## 2026-10-14 wakeup 11 (17:43 UTC) — closing
- gen3: 20/20 PASS, s21 6.6–11.4; mean (projected w 39cd) 11.18 s21 vs 39cd 13.59 → outer residual worth ~2.4.
- Final best: 9284 STRONG 11.495/12.027/11.550/12.023. f2d9 11.30 STRONG. c9e2 s21 13.04 but r56 11.07.
- Posted result 4348 (coverage) and swarm done. 88/500 charged. Loop stopped.
