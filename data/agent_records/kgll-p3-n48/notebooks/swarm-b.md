# swarm-b notebook

Started 2026-10-14T10:23:53+00:00.

## 2026-10-14 11:15 — wakeup 1: scope chosen
- Board empty at start (only swarm-a active). Read progress/40, 46, ADR-0040, theory §2.3/5/8.
- Parent w1c: r56 Δ = 2.59e-4 (C=1, PASS); s21 baseline still running at start.
- Helpers: `work/stars.py` (S[|G|²] in 120° basis, T[|R|²] in 60° direct basis, make_input()).
  `work/w1c_template.json` = `swarm template --parent w1c`.
- Posted hypothesis `linmap` (20261014T111233.912Z_swarm-b_hypothesis_cb3e): 60 single directions
  S1..S21 × T1..T3 × {α ±0.05, β ±0.03} = 120 evals. Inputs in work/linmap_a, work/linmap_b.
- Next: submit in batches ≤ 30 (in-flight cap 32), fit slope/curvature per direction, then
  line search along gradient + couplings among strongest.
- NAMING: file labels use |R|² — `T1` = |R|²=1 (charter T1), `T3` = |R|²=3 (charter T2), `T4` = |R|²=4 (charter T3).
  Spatial `S<n>` = |G|²/|G1|² = n.
- 11:15 submitted batch1 (α×T1 all 10 stars ±, β×T1 S1..S9 ±) = 30 reqs. Queued batch2..4 dirs (30 each) in work/.

## 2026-10-14 11:40 — wakeup 2: pivot linmap → sin2d
- swarm-a ran the identical 60-axis map; abandoned linmap (post 0acd, coverage incl.). 10 charged.
- Board: ~45 agents; leaders all phase-only chiral joint orbits (f e5d5 S3×T1 odd β 0.0167 → s21 1.558;
  c d698 S2×T1 δ=60 β=.03 → s21 1.249, r46 1.404; c ce1f in conv46).
- Found: every phase leader has β·sin(2δ_GR) > 0 (δ = ∠R−∠G mod 180, Cartesian; G1 0°, G2 120°, a1 30°, a2 90°).
  `work/angles.py REQ...` prints δ per entry. `work/sin2d.py make(t, mu, g, h)` builds the coherent block
  (verified: reproduces f-5098 γ to 3e-12 at mu=1/30).
- Posted hypothesis sin2d (af8e). Stage 1 submitted (15): S123 / Wall (g=w_s/w1) / Wout lines, T1 only, inputs work/s2d1.
- Next: read stage 1; stage 2 = shell profile + T-profile (sign of T3 open: f defd anti-rule S1×|R|²=4 still 1.046).

## 11:59 — wakeup 3
- Stage 1 (15) still queued. swarm-ab posted chiral-quad (4865, 11:49): the same sin2δ rule, and its L1flat overlaps my S123.
  Mailed ab with a split: I take the shell profile g_s along T1, ab takes the T profile and the slope-weighted line.
- Units: my μ = per-entry β; ab b = 2μ (pair coefficient); f's b = 3μ (separable units for 3×3).
- f's slopes per unit b (sep units): S1T1 3.9, S2T1 9.6, S3T1 11.3; T2/T3 weak or negative. f is also running the (1,1,1) and ascent lines in the S1-S3 odd subspace.
- Leaders: α⊥ S1×T1 line s21 1.64 / r46 2.63 (j ea28; ak critiques it as a branch change). c claims STRONG for d698.
- conv46 ≡ r46 for pure LL0 (l's request 28b0).

## 12:20 — wakeup 4
- Stage 1 still all pending (37 min queued, broker congested). Split agreed with ab (mail 3b20): I own the shell profile g_s along T1.
  ab owns the momentum profile d_p on slope-weighted S1–S3 (c ∝ 0.35, 0.87, 1) plus L1grad and L2T123, and withdrew L1flat.
- Caveat from swarm-at (8343): g_cutoff 8 drops 7–9 % of the kernel change for S9/S10 deformations, so judge Wall/Wout on conv46.
- Board: f STRONG claim 728b (S3×T1 odd b=.05 sep → 1.558/1.641/1.560); h: outer α orbit contrasts S4T1 1.57/1.72/1.61;
  j: α⊥ −0.45 1.64/2.63/2.44 (density control by k: not density).

## 12:41 — wakeup 5
- Stage 1 still SUBMITTED (accepted 11:43). Queue latency is ~1 h board-wide (h's 11:24 step landed 12:38).
- Board: h's α+β union step gives s21 up to 4.76 (adcf), strongly superadditive. j's STRONG claim for α⊥ −0.45 (2.63 r46).
  av's cos2d (0649) is the amplitude analogue (α·cos2δ > 0) plus the complex e^{2iδ} mix on S1–S3×T1.
- e (91cc): the PES entanglement gap drops from 13.4 (static) to 4–5 (leaders), still well above the gate.

## 13:07 — wakeup 6
- First results: S123 sin2d μ=.005 → s21 1.3796 (8219), μ=.01 → 1.6494 (1910), both PASS and promoted to r46. Phase-only.
- Board records: h c662 4.76/5.23/4.67 STRONG; t 8c01 4.82/5.19/4.55. av (ddbc): these records ARE the complex
  angular rule α∝cos2δ, β∝sin2δ on S1/S2×T1(+T2), with T3 opposite in sign; S3 and the outer shells are unused. av stage 2 runs the complex rule incl. S3/outer.
- My niche is the best phase-only (clean beyond-M2, no Q=0) shell profile.
  Stage 2 submitted (6): S23, S1-6h (outer |G|²=7,9,12 at 0.5), S3hv (.5,1,1.5) at μ=.01/.02 → work/s2d2.

## 13:34 — wakeup 7: stage 1 landed (s21 / r46 / r56)
| line | μ=.005 | .01 | .015 | .02 | .03 | −.01 |
|---|---|---|---|---|---|---|
| S123 | 1.380 (8219) | 1.649/1.850/1.720 (1910, SUGG→conv46) | 1.730/2.254/… (d586) | 1.629/2.601/… (197d) | 0.797 F split | 0.289 P (7a78) |
| Wall | 1.597/1.762 (1863) | 1.613/2.473 (1309) | 0.873 F | 0.743 F | 4.22 A→s21c F (other phase, d8c9) | 0.015 F |
| Wout | — | 1.622 (b70e) | 1.261 F (.02) | — | 2.735 F (.04) | — |
- The sign rule is confirmed (−0.01 collapses). Phase-only s21 saturates ~1.73 (f ff14 sees the same ceiling ~1.72), then the s21 splitting gate fails;
  r46 keeps rising (2.60 at μ=.02). Outer shells follow the rule with tiny coefficients (Wout entries ≤ .0044 → 1.62).
- Board: o f5f1 6.28/8.33 (α+β); h/t STRONG ~4.6; s bfbb phase-only noQ0 1.725/2.322/2.142 STRONG.
- Plan: stage 2 (6, queued) decides whether any shell profile lifts the phase-only s21 ceiling; then post result + coverage.

## 14:05 — wakeup 8
- d586 (S123 μ=.015) STRONG phase-only 1.730/2.254/2.083/2.254; 1910 STRONG 1.649/1.850/1.720/1.850.
- Stage 2: S23 .01/.02 1.591/1.708; S3hv .01 1.693, .02 FAIL; S1-6h FAIL at both μ. No profile lifts the s21 ceiling (~1.73).
- Posted result cd55 (coverage incl.) and critique 3b65 of ab18: the T2/T3 lift to 1.88 is ~ the size of the s21 chirality artefact; suggested an MT-image test. Mailed ab.
- Stage 3 submitted (5): outer sin2d (Wout, T1) merged on top of the records f5f1 (μ .005, .01) and c325 (μ .005, .01, .02).
  `work/merge.py` merges pair-representation blocks; `work/mk_s2d3.py`.
- Board: s c325 s21 9.87, av 0d8f 9.67 (pending ladder). Records are Σ-cap limited (t request 789e).

## 14:39 — wakeup 9
- b70e (Wout μ=.01) STRONG 1.622/1.942/1.790/1.942. Stage 2 r46: S23 .02 2.398, S3hv .01 1.999, S23 .01 1.705.
- ab conceded 3b65: the T2/T3 lift is s21-only (4be4 r46 1.934 vs T1-only 1.918). ao's mail supports it (S3×T2 sign flip s21→r46).
- swarm-a 076d duplicates my stage 3 on c325 (also does e0a8). Mailed a.
- Records: av e0a8 STRONG 10.39/9.87/10.50/9.96; s c325 STRONG 9.87/10.15/9.53. Cap-limited; chart-dependent caps (ai request).
- Plan: when stage 3 lands, post result and coverage, then likely `swarm done` (board saturated; my family is exhausted).

## 16:30 — wakeup 10: stage 3 landed; family closed
- c325+Wout μ=.005: 84e7 10.059/10.556/10.078/10.562 STRONG; μ=.01: 7e78 10.105/10.835/10.455/10.841 STRONG (+6 % min);
  μ=.02: 5f71 9.49 s21 (falls). f5f1+Wout: .005 → 5.69 s21 (−9 %), .01 FAIL split 0.104.
- Posted ec78 (stage 3 + full family coverage). Mailed s.
- Board top: w 407a min 13.26 (outer α+β on c662). Board saturated: ~20 agents done; families closing.
- Decision: swarm done (36/500 charged). Pending free promotions (r56 of 1863/1309/135e/543b/db3a, conv46 of 5f71, r56 of 670d) land in the store regardless.
