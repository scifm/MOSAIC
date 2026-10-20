# swarm-x notebook

Started 2026-10-14T10:25:11+00:00.

## 2026-10-14 11:27 — wakeup 1
- Read board: a/b separable axis maps (dup), c jorb joint orbits, d chiral half-shell phase, e bigamp, f chiral-odd β orbits, g C3 channels, i kpow, l phase-even. Requests from g and l to human: block is cos·cos only (sin·sin sector unreachable) — state in coverage.
- Key observation: c's orbit probes give ±15–20 % at s21 for step 0.05 (α) / 0.03 (β) vs ~1 % on separable stars. Chiral-odd β pattern (+30 β+ ≈ −30 β−) confirmed at s21.
- My family **xcomb**: combos of d1 = α S1T1 ⊥(−0.05), d2 = β S1T1 +30 (+0.03), d3 = α S2T1 ∥ (+0.05), d4 = α S2T1 +60 (−0.05). Generator `work/xcomb.py`. Hypothesis 20261014T112611.462Z_swarm-x_hypothesis_3b7b.
- Batch b1: 12 requests submitted (req ids 112613–112626). Mailed swarm-c.
- Next: read b1 results; check r46 of c's ce1f / c9a2 (transfer test). If transfer collapses, scale down and pivot to verification/critique.

## 2026-10-14 11:48 — wakeup 2
- b1 (12) still queued (queue congested; ~45 agents now active, heavy herding in S1–S3×T1 orbits).
- c's result bc24: s21 ≈ r46 within 0.6 % for promoted orbit points → the orbit signal is not an s21 artefact. MT symmetry holds to <1 %.
- Leader now 1.6386 s21 (j/q ⊥ α line, larger step). f chiral-odd β S1T1 1.558.
- c confirmed split: x owns cross-orbit pairs; z/n/ag/am CMA; o/t surrogates; j/r/q ⊥ lines; ae S2T1 ±60 β line.
- u warns: |G|²=3×T1 directions consume 30–50 % of s21 splitting gate (split/Δ 0.04–0.05) — log split/Δ on my combos.
- Next: when b1 lands, compute additivity table (R_combo−1 vs Σ(R_i−1)), post result with split/Δ. Don't submit more until queue drains.

## 2026-10-14 12:13 — wakeup 3
- b1 still pending (47 min in queue).
- Board: STRONG claims already: j/q α⊥ S1T1 = −0.45 (s21 1.64, r46 2.63, r56 2.44, conv46 2.63); f S3×T1 chiral-odd β e5d5 (1.56/1.64/1.56); c S2×T1 +60 β=0.03 phase-only (1.25/1.40/1.35). k: density controls explain none of ⊥ gain (actually lower it). ak: ⊥ −0.45 sits past an s21 splitting turnover (branch-change suspicion). s: ⊥ channel is half static LL mixing (Q=0) — request to human.
- y's s2plane overlaps my d3+d4 (they cite my ids).
- My small-step additivity test is now less central; still useful for surrogates (o, t). Plan after b1: post additivity table; then consider leader×leader combos only if r (gc-perp, ⊥ + chiral-odd) doesn't cover them.

## 2026-10-14 12:48 — wakeup 4
- b1 landed. Super-additive: d524 (4 orbits) s21 1.9229 / r46 2.1491 / r56 1.9882 / conv46 2.1491 → STRONG; additive prediction 1.725. 3·d2 shows s21 falling (split/Δ 0.083) while r46 rises 1.47; 1.5·d3 FAILs s21 split 0.147 (never promoted). Posted result 20261014T124459.289Z_swarm-x_result_2250 with coverage.
- swarm-as is scaling the d524 ray (agreed by mail).
- Board records: t 8c01 s21 4.816 / r46 5.186; h c662 s21 4.760 / r46 5.226 (α+β union step, S1–S3). c note: leaders bring R_beyondM2 from 0.12 to ~0.6–0.72 — "repairing a defective parent to the smooth M2 law".
- Stage 2 (b2, 11 evals): c662 + outer T1 α contrasts from h eva1 (353f S4, 8a8a S5, 99f8 S6). Tools: work/merge.py (exact linear merge, checked 3e-16), work/gen_b2.py. Note 20261014T124729.261Z_swarm-x_note_6295. Mailed h.
- Budget: 23/500 charged.
- Next: read b2; if outer adds at the record, scan the best outer scale on t's 8c01 as well, and request density control.

## 2026-10-14 13:19 — wakeup 5
- b2 still queued (11). b1 promotions: 1ddc, 7e1b, f433, 676f reached STRONG (conv46 done).
- h: no overlap with b2; w runs S7–S10 cos2δ α on top of c662 (complementary, outer-outer).
- Debate: g says parent is a near-zero-mode (ideal band, short-range) so R_gap is amplified by breaking vortexability; p rebuts (contact term inert); u two-body: leaders lift 130–270 of 558 zero pair modes; ap: leader γ on uniform LL0 lowers the gap (gain needs γ×ρ* cooperation). k: density controls ≈ 0.995–1.0 for c662/353f.
- av: records are α ∝ cos2δ, β ∝ sin2δ on S1/S2×T1.
- I owe a critique post (rule 11) — look for one grounded in my own data.

## 2026-10-14 13:50 — wakeup 6
- b2 still pending (submitted 12:47; lanes slow, several agents reported 90-min latencies, resolved as slow-not-lost).
- New record: o f5f1 s21 6.28 / r46 8.33 / r56 8.12, Σ|β| = 1.88 near 2.0 cap. t asks human how to read representation-dependent Σ caps (pair stars inflate Σ by √3 vs full stars).
- STRONG claims: t 8c01, h c662, v S7T1 outer α (1.56/1.93/1.79), s noQ0, f/ae/t phase-only (s21 phase-only ceiling ≈1.72). Density controls for all α records ≈0.994–1.0. g retracted the 1/d² critique.

## 2026-10-14 14:24 — wakeup 7
- b2 landed (all PASS s21/r46): c662 + o456x1 = d2de s21 7.216 / r46 8.197; outer gains linear in scale, ~2× parent gain absolute, mutually sub-additive (80 %), lower s21 split. Posted 20261014T142209.461Z_swarm-x_result_5c12.
- Board: records now cap-limited: av e0a8 (cos2δ+i sin2δ S1–S3×T1) s21 10.39 / r46 9.87; s c325 (noQ0) 9.87/10.15; o f5f1 STRONG 6.28/8.33/8.12. Many agents finished (d, g, p, q, aj, ae, ac, ak).
- b3 (10): outer triple on e0a8 (cap-fill + trades) and c325 (room under cap). Note 20261014T142334.870Z_swarm-x_note_26d6; mailed av, s. Tool work/gen_b3.py.
- Budget 44/500.
- Still owe a critique post. Candidate: none concrete yet.

## 2026-10-14 14:56 — wakeup 8
- (Correction: budget charged is 33, not 44.)
- b3 s21 all PASS and all above their base records: e0a8 (10.39) → +0.15 o456 10.73, +0.33 o456 11.11 (cap), 0.9e0a8+0.8o456 11.47, 0.8e0a8+1.0o456 11.41; c325 (9.87) → +0.5/1/1.5 o456 10.97/11.47/11.61; +o56 x1/x2 11.29/11.84; 1.2c325+o456 11.87. r46 pending.
- d2de completed STRONG: 7.216/8.197/7.381/8.194.
- Board: av has an all-shell complex angular rule (55f9 12.5, b103 13.57 s21), w adds S7–S10 on top (df9b 14.52 s21, M2k 11.6). My outer-contrast merges are now subsumed by av's coherent rule; the frontier is cap-limited (Σ|α|, Σ|β| chart-dependent; ai/t asked human).
- Plan: post b3 result when r46/r56 land, with coverage; then probably close xcomb (optimizers av/w/s/z/o own the frontier) and switch to a verifier/critique piece.

## 2026-10-14 16:43 — wakeup 9
- b3: 10/10 STRONG. Best 06bb (c325 + 2·(o5+o6)): 11.844/11.821/11.804/11.894, min 11.80, noQ0, flattest R>11 point. 45f3 (0.8 e0a8 + o456) min 11.09 — outer α relieves e0a8's r46 split (0.077→0.026). e0a8-based cap-fill points have r46 < s21 (an's critique confirmed).
- Posted 20261014T164229.632Z_swarm-x_result_c055. Mailed k for 06bb density control.
- b4 (7): c325+o56 line to 2.5/3, 0.9/1.1 trades, +0.5 o4, + b's outer sin2δ phase (7e78 − c325) at 1×/2×. Then close xcomb with coverage.
- Board top min: w 407a 13.26 (STRONG); av 55f9 12.51; al lowsym a8c1 12.44. u: qmax-8 non-PSD pair spectra at R>11 — asks human for qmax ≥ 12 reruns.
- Budget 40/500 after b4.

## 2026-10-14 17:15 — wakeup 10
- b4 s21/r46 in: +b's outer sin2δ phase on 06bb: wout 717f 12.53/12.17, wout2 236b 12.78/12.22 (best). o56x2.5 2bbf 11.93/11.82; o56x3 6ba4 11.80/11.54 (saturated); 1.1c325+o56x2 561c 12.09/11.93; 0.9c325+o56x3 9ce9 11.23/11.51; +0.5 o4 e3e3 11.81/11.79. r56 pending.
- k queued 06bb density control (…_3718). w adds S7–S10 outer α on 06bb (disjoint shells).
- Many agents closing (h, o, r, an, at, af...). Frontier ~13.3–13.6 min (w, av), cap- and qmax-limited.
- Plan: once b4 r56/conv46 land, post final xcomb result + coverage, then swarm done.

## 2026-10-14 17:45 — wakeup 11
- b4 partial: 236b (06bb + 2·wout) 12.780/12.223/12.527 (conv46 pending), 717f 12.53/12.17/12.37, 561c 12.09/11.93/12.09; o56 line saturates (6ba4 r46 11.54). s21 split ~0.06–0.07 on all.
- k: 06bb density control 1.006 (s21) → beyond-M2 (density). u: 06bb is qmax class A (clean).
- v critique: N_A=2 count doesn't certify Laughlin; quote s21c N_A=3 EG — mine are 2.6–3.0 at s21c.
- Next wakeup: once conv46 lands for 236b/717f/561c, post final result+coverage and `swarm done`.

## 2026-10-14 18:17 — wakeup 12 (final)
- b4 done: 236b STRONG 12.780/12.223/12.527/12.364 (min 12.22, noQ0, density = 06bb's ctrl 1.006); 717f min 12.17; 561c min 11.93; o56 line saturates at s≈2–2.5.
- Posted closing result 20261014T181701.151Z_swarm-x_result_d1ab (family coverage) and claim 20261014T181701.903Z_swarm-x_claim_7a20.
- Ran `swarm done` (40/500 charged). Loop stopped.
