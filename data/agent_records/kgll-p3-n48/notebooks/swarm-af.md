# swarm-af notebook

Started 2026-10-14T10:25:40+00:00.

## 2026-10-14 ~11:30 — wakeup 1: orientation, family `rsurvey`
- Read brief, docs 40/46, kdep_envelope.py (γ = Σ(α/2 + iβ) O_s F_p; pair stars allowed → joint orbits).
- Board: ~14 agents on structured directions (axis maps a/b, S1–S3 orbits c/g/j/r/q/f/l/m, S4–S10 orbit contrasts h/v/w, pooled models h/o/x, mech k, nematic ad, fsmatch y). Leader: jorb chiral β orbit S2×T1 (+60°), β=0.03/entry → s21 1.2494 (req d698). c75e (S1×T1 +30° β) holds r46 1.1586.
- w1c facts: Δ(s21) 2.2586e-4, uniform LLL 1.827e-4 → only 1.24×; deep M2 saturation.
- My niche: random-direction survey over the full 126-orbit C6 space (inner S1–S3 = 27 orbits, outer S4–S10 = 99), α and β separately, ± pairs at rms 0.05 of Re/Im γ. Generator `work/rsurvey.py` (orbit basis verified: 126 orbits × 3 entries, swarm-c leader is one orbit). Direction vectors in `work/dirs_s1*_*.json`.
- Hypothesis posted: 20261014T112925.722Z_swarm-af_hypothesis_4570 (budget ≤200).
- Submitted stage 1 β half: 32 reqs (work/s1b, seeds 101 inner, 102 outer). α half (work/s1a, seeds 103 inner, 104 outer) waits for in-flight slots.
- Next: submit s1a when slots free; analyse ± pairs → directional slopes/curvatures; gradient-norm per cell.

## 2026-10-14 ~12:05 — wakeup 2
- None of my 64 stage-1 evals finished yet (32 pending in broker, 32 queued). Broker heavily loaded.
- Board news: swarm-c STRONG claim (phase-only S2×T1 +60° β=0.03: 1.249/1.404/1.347 s21/r46/r56). ⊥ α=−0.45 S1×T1: s21 1.64, r46 2.63 (swarm-ak critique: past a manifold-gate FAIL, possible branch change). swarm-k: matched-density control for α⊥=−0.05 gives R_ctrl≈0.999 → density explains none. swarm-a note: outer shells (|G|²≥7) at full-star 0.05 break the Laughlin manifold → my outer cells at rms 0.05 may FAIL (still informative for genericity; consider rms 0.01–0.02 for outer in stage 2). swarm-f: S3×T1 chiral-odd β +0.05 → s21 1.558, r46 1.641.
- Heavy herding on inner orbits and outer chiral-odd β (5–7 agents). My random survey remains unique.

## 2026-10-14 ~12:30 — wakeup 3
- First 10 results (inner β random, rms 0.05, seed 101 d00–d04): s21 R = 0.976/0.681, 0.897/0.929, 0.521F/0.417F, 0.807/1.007, 0.620/0.821 (−/+). Generic inner phase directions LOSE at the leader's band displacement; best +0.65 %. Early sign the +25 % leaders are channel-specific (even part strongly negative, ≈ −15…−50 %).
- Board: STRONG claims c (S2×T1 +60 β 0.03: 1.249/1.404/1.347) and f (S3×T1 chiral-odd β 0.05: 1.558/1.641/1.560). h: S4×T1 α orbit contrast c0+ 1.572/1.720/1.614. j: α⊥ −0.45 1.64/2.63/2.44 (k: density control lowers gap → not density). e: PES entanglement gap drops 13.4 → 4–5 for leaders. at: g_cutoff 8 truncation matters for S9/S10 → judge outer on conv46.
- Throughput: 40 charged in ~1 h for me. Waiting for rest of stage 1.

## 2026-10-14 ~13:05 — wakeup 4
- Inner β random (rms 0.05, 8 dirs ±, seed 101) complete: 16 pts, R s21 median ≈0.80; >1: d05m 1.1325 (r46 1.0934), d06p 1.064 (r46 0.9845), d07p 1.019, d03p 1.0065. 2 FAIL (d02 both sides). Generic inner phase loses; ~1 in 8 directions has a +6–13 % side.
- Outer β random (rms 0.05, seed 102): 13/14 landed are FAIL (R 0–0.67) — outer window ≪ 0.05 rms, consistent with swarm-a note. Submitted same directions at rms 0.01 (outer β seed 102, outer α seed 104; work/s1o, 32 reqs) for linear-regime slopes.
- Board: records now s21 4.76 (h union α+β), 4.82/5.19 s21/r46 (t orbsurr, 8c01); j STRONG α⊥ −0.45 1.64/2.63/2.45/2.63; ae S2×T1 MT-odd β 0.03: 1.687/1.989. Strong superadditivity (x, h, t). Mechanism: density controls < 1 (k), projected interaction moments flat (u), c: leaders restore static-M2 law (R_beyondM2 0.12→0.72).
- Next: when α cells land, compute directional slope/curvature per cell, gradient norms, fraction R>1; post result + coverage.

## 2026-10-14 ~13:40 — wakeup 5
- Inner β (seed 101) complete. `work/angular.py`: odd part (R+−R−)/2 vs projection on board's angular rule (β ∝ sin2δ, T3 sign −): corr +0.69, n=8, sign agrees 6/7 PASS pairs (d04 disagrees; d02 FAIL both). Even part mean −0.174 (all 8 negative), rms odd 0.118. → gain is directional; random directions pay a large TL-even penalty.
- swarm-am abandon 5b1e: 12/12 random phase directions over 18 orbits at larger rms (~0.2) all FAIL. Consistent.
- Board: STRONG claims h c662 4.76/5.23/4.67, t 8c01 4.82/5.19/4.55, v S7×T1 α 1.56/1.93/1.79, s noQ0 phase-only 1.73/2.32/2.14; f: phase-only s21 ceiling ≈1.72. av: records = complex angular rule cos2δ + i c sin2δ on S1/S2×T1(+T2).
- α cells (32) + outer rms .01 (32) still pending/queued. Plan: post result when α inner lands (incl. angular-rule test for α with cos2δ).

## 2026-10-14 ~14:20 — wakeup 6
- Stage 1 (rms 0.05) complete; posted result 20261014T141425.862Z_swarm-af_result_6d30 with coverage. Per cell PASS/R>1: βin 14/4, αin 16/4, βout 1/1, αout 0/0. corr(odd, rule proj) +0.69/+0.78/+0.60/+0.60. Winners = largest rule-aligned projection: 425f αin 1.5277 (proj +1.45), f749 βout 1.5272 s21 / 1.6059 r46 (proj +0.81), 6da6 βin 1.1325/1.0934.
- Submitted stage 2a: same inner directions at rms 0.02 (work/s2i, 32 reqs) → odd/even scaling (linear vs quadratic), gradient-norm & Hutchinson curvature estimates per cell. Outer rms 0.01 (work/s1o) still pending.
- Board: records now av cos2d S1–S3×T1 complex rule s21 up to 10.39 (Σ|α| cap); o f5f1 6.28/8.33/8.12 STRONG. Density controls all ≈1 (k: R_ctrl−1 ≈ 0.06 ΔM2). Space well covered; my remaining value = coverage + scaling. Plan to wrap up after 2a + outer .01 (~130 evals total) unless something new appears.

## 2026-10-14 ~14:50 — wakeup 7
- Outer rms 0.01 (same dirs as s102/s104) landed at s21: all 32 PASS. Linear regime: corr(odd, rule) β +0.83, α +0.95 (α sign 8/8). mean even −0.030 (β), −0.017 (α); rms odd 0.068 / 0.091. Best: αout d06m 1.2105, βout d05p 1.1189.
- Estimates (E[odd²] = r²|g|²/D, E[even] = r² trH/(2D)): |g| outer β ≈ 68, outer α ≈ 91 per unit rms γ; inner (rms .05) β ≈ 12, α ≈ 22. tr H/D outer β ≈ −600 (r=.01) / −490 (r=.05) → quadratic scaling holds; inner β ≈ −140. Outer: 5× steeper gradient, ~4× stronger isotropic curvature → narrow but steep window (matches x, b: outer most cap-efficient).
- Waiting: inner rms .02 (32). Then post final result + done.

## 2026-10-14 ~16:50 — wakeup 8: closing
- Inner rms .02 landed (32/32 PASS). corr(odd,rule) β .89, α .78. Scaling: odd linear (×2.3–2.5), α-inner even quadratic (trH/D −93/−94), β-inner steepens at .05.
- Estimates |g|: βin 13.5, αin 21.9, βout 68, αout 91; trH/D: −84, −93, −596, −336; |g|²/(2|trH/D|): 1.1, 2.6, 3.9, 12.3.
- Unbiased transfer: 25 promoted points, 24/25 r46>1, 19/25 r46≥s21, median (R46−1)/(R21−1)=1.15.
- Posted final result 20261014T164551.373Z_swarm-af_result_d71b with coverage. 128/500 charged. Family closed; board saturated with optimizers on the angular rule → swarm done.
