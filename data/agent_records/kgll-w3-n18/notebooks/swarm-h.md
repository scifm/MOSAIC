# swarm-h notebook

Started 2026-10-15T04:13:16+00:00.

## Wakeup 1 — 2026-10-15 ~04:30 UTC
- Board: swarm-a w3-atlas (separable S×T, α±0.10, β±0.05), swarm-b w3-joint (joint (G,R) classes, chiral S7 L/R),
  swarm-c w2-atlas, swarm-e w3-bigamp (large amplitudes). Early hit: swarm-b j_S1T1_d1_ap (G⟂R α+0.05) s21 1.1052 (req f06f);
  swarm-a S1T1 α+0.10 1.0343 (6553). All β singles so far < 1 (curvature ≈ −11 to −41 per γ-rms²).
- Finding (posted note 20261015T043135.244Z_swarm-h_note_4b5a): Nk=21 cluster is C6 but chiral (no mirror); 4×6/5×6 only C2.
  Continuum has M·T: α→α, β→−β (stars mirror-permuted). ⇒ β even on mirror-symmetric directions (odd part = cluster artefact),
  L/R mirror partners redundant, only mirror-odd (chiral) phases carry a linear β term. Board data consistent (≤0.6 %).
- My family: `w3-phase` (hypothesis 20261015T043052.916Z_swarm-h_hypothesis_a119). Phase-only = clean beyond-M2.
- Tools: work/gen.py (stars, chiral_split, joint_pairs, circulant, block, write_input), work/stageA.py, work/tab.py (board table).
- Submitted stage A: 26 evals in work/A/ (jc_* joint chiral b=0.01 c(θ)=+b,c(−θ)=−b; sc_* spatial chiral β_L=+b,β_R=−b, b=0.015).
- Next: read stage A → g (odd part) and c (even part) per direction; stage B Hessian/linear model in best chiral + least-curved
  mirror-even directions; stage C CMA-ES box |β|≤0.10.

## Wakeup 2 — 2026-10-15 ~04:45 UTC
- Board exploded: matched G⟂R ("S1⊥") α joint class is the big winner. swarm-j 7d04 (S1⊥ pair stars, diag α=0.2, g_cutoff 6)
  s21 1.369 / r46 1.386; swarm-b f06f robust_positive claim (α=0.05, 1.088 min). 8+ agents on mechanism/matched-density controls
  (herding there). swarm-g posted the same M·T note 6 min before me (credited) and covers single chiral orbits of 12-member shells.
- Stage A result posted (20261015T044542.349Z_swarm-h_result_3112, with coverage): all 26 < 1; max quadratic-model gain 0.5 %
  (sc S7×T1, at b≈−0.007). Joint-chiral classes shells 1,3,4: odd ≤0.5 %, even −0.4…−2 %.
- Parity rule: linear directions = mirror-even α ⊕ mirror-odd β (also around any mirror-symmetric base).
- Stage B submitted (13 evals, work/B, builds-on 7d04): base S1⊥ α=0.2 at g_cutoff 8 + chiral β ± (jcS1T1, jcS1T4, jcS3T4 c=0.01;
  scS7T1, scS13T1 b=0.0075 on T1 pairs; scS7T3 b=0.0075). gen.py now has merge(), perp_S1_atoms(), joint/spatial_chiral_atoms().
- Next: odd/even parts at the base; if any odd part gives >1 % gain, line search + combine; else close w3-phase with abandon/coverage
  and pick a new role (candidates: chiral β on the eventual best ⟂ optimum; or w2 parity check).

## Wakeup 3 — 2026-10-15 ~05:00 UTC
- Stage B (at S1⊥ α=0.2 base, 8c8f s21 1.3693/r46 1.3857): chiral β S7(L−R)×T1 b=−0.0075 (e9e8): s21 1.3799, r46 1.3941,
  r56 1.3173 (base 7d04 r56 1.306) → +0.6–0.9 % on all clusters, same sign as at parent. S13×T1 b=+0.0075 (cdd5) s21 1.3773 r46 1.3914.
  Even parts at base POSITIVE (+0.003) for both — unlike parent. jc S1T1/S1T4/S3T4, sc S7T3: ≤ base.
- Board: swarm-j claim strong for 7d04 (r56 1.306). Mechanism controls: gain not density (ρ̄ control 1.00–1.02; M2-matched 1.18–1.20;
  uniform parent loses). swarm-g abandoned chiral-phase at parent (≤0.3 %). swarm-a starting w3-cma (14-D incl. chiral β on S1×T1);
  mailed them that S1×T1 chiral is flat and the useful chiral dims are S7/S13 L−R × T1.
- Stage C submitted (15 evals, work/C): S7 b ∈ −{0.015,0.025,0.04,0.06}, S13 b ∈ +{same}, sum at 0.015/0.025/0.04, S19/S21 ±0.0075.

## Wakeup 4 — 2026-10-15 ~05:25 UTC
- Stage C (chiral β lines on S1⊥ α=0.2 base): gains grow with b; NOT capped like at parent.
  S7 L−R b=−0.06 (0672): s21 1.4271 / r46 1.4611 / r56 1.4397 (base 1.3693/1.3857/1.306). S13 b=+0.06 (8293): 1.4253/1.4512/r56 1.4356.
  Combos S7−/S13+ overlap (s21 at b=0.04 < 0.025). S19(+) and S21(−) at 0.0075: +1.2 %/+1.5 % on s21, +0.7/+0.9 % r46.
- Posted result 20261015T052225.267Z_swarm-h_result_7ae5; mailed swarm-a (CMA dims) and swarm-b (cjphase at base, not parent).
- Withdrew 21 dominated B/C requests from promotion (free GPU queue). Kept 0672, 8293, 827c, 82b5, cb73, 8c8f, e9e8.
- Stage D submitted (16, ids in work/D_ids.txt): S7 to 0.17, S13 to 0.13, S19+/S21− lines to 0.06, 3 combos.
- Tools: work/fast.py [pattern] (fast table from swarm status; names.json maps ids→names — append new ids!).
- Next: find turnover; then 2-D/4-D refinement (S7,S13,S19,S21 chiral + maybe re-optimise α_⊥ jointly with β); consider claim.

## Wakeup 5 — 2026-10-15 ~05:40 UTC
- Stage D: S7 line peaks b≈0.05–0.06 (0.08: 1.4066 s21; ≥0.13 FAIL manifold). S13 peak ~0.06–0.08 (0.08: s21 1.4209 r46 1.4581).
  S19+ and S21− peak ~0.03 (s21 1.418/1.422, r46 1.440/1.450). Combos overlap (no additivity). Withdrew all D from promotion.
- CLAIM posted: 0672 broker `strong` (s21 1.4271 / r46 1.4611 / r56 1.4397 / conv46 1.4613), 20261015T053756.364Z_swarm-h_claim_28ca.
- Board: fe3d (swarm-p: S2∥ α 0.25 + my S7 chiral β) 1.69 all clusters; swarm-b 02f7 = S2∥ 0.25 + class-resolved chiral-7
  (L class 130.9°, b=−0.08 per pair entry; R class 49.1° +0.08) s21 2.38 (r46 pending). swarm-a w3-stack 8-D CMA; swarm-j RSM
  (α⊥, α∥, β7); swarm-c chiral on w2.
- gen.py: orbit_joint(), chiral_class_atoms(q, theta_L, b) — reproduces 02f7 bit-for-bit.
- Submitted V/ (2 diagnostics: 02f7 at g_cutoff 10/12, n_mesh 64 on s21) and stage E (19: base 02f7 at gc9 + 13/19/21 × 3 classes ± 0.03).
  Mailed swarm-b proposing split (they keep 7-classes; I take 13/19/21).

## Wakeup 6 — 2026-10-15 ~05:55 UTC
- 02f7 convergence: gc7 2.3801 → gc9/10/12 (nm64) 2.3670 (−0.55 %). Converged from gc9.
- Stage E (class-resolved chiral β b=±0.03 on 02f7; base gc9 s21 2.3670 / r46 2.5828): 19@66.6°(+) 2.4398/2.9441 (4927, both);
  13@16.1°(+) 2.268/2.777 and 21@139.1°(−) 2.145/2.922 r46-only. = swarm-j's resonant picks. Others < base. Kept 4 for r56; withdrew 15.
- Posted 20261015T055347.499Z_swarm-h_result_d901. Mailed j, a. 02f7 r46 2.59/r56 2.53 (swarm-b). fe3d claim strong (swarm-p).
- swarm-f: leaders exactly M·T-invariant. Herding: a (10-D CMA), j (chistack), b, d, r, f all at 02f7.
- Stage F (4): 19@67 b=0.05/0.08 with 7-class 0.08; 7-class b=0.06/0.10 with 19@67 0.03.
- Next: if F small, step away from w3 stack (saturated) — candidates: phase-only clean beyond-M2 ceiling (swarm-f doing at parent);
  w2 transfer (c, p doing). Maybe verifier/critique role on claims (cluster disagreement 13@16/21@41).

## Wakeup 7 — 2026-10-15 ~06:12 UTC
- Stage F: 19@67 best at 0.03 (0.05: 2.311, 0.08: 2.029 s21); 7-class 0.06 + 19@0.03 s21 2.4439 (1356), 0.10: 2.3578. Withdrew 2.
  swarm-j's c89a stack ~same. Leaderboard s21 now 3.6 (swarm-a CMA cc13), swarm-o w3-radial ~3.1. w3 stack saturated by others.
- Switched to swarm-g's open item: chiral β on w2 S1-only base 141f (stage G, 9 evals, family w2-phase-141f, work/G), to compare
  with swarm-c's c722/beed on df59 (beed strong 1.19/1.228/1.208). Posted note.

## Wakeup 8 — 2026-10-15 ~06:30 UTC
- CLAIM 2 posted (0f1d): 4927 = 02f7 + 19@66.6° chiral β b=+0.03: s21 2.4398 / r46 2.9441 / r56 2.9014 / conv46 2.9386 strong.
  02f7 gc9 base: 2.3670 / 2.5828 / 2.5259 / 2.5834.
- w2 stage G (141f base gc9: 1.1121/1.1473): S7 b=−0.02 → 1.1268/1.1602 (+1.3/+1.1 %); S13 −0.02 +0.2 %; +0.02 lose ~5 %; ±0.05 lose/FAIL.
  swarm-c beed (= S7 b=−0.02 on df59): +2.4 % s21, +1.7 % r46, +1.6 % r56. ⇒ 4⊥ roughly doubles the phase increment; same sign.
  Withdrew G +0.02 points. Waiting r56 for G base/S7−/S13−.
- Finite-size check: re-submitted F b19 0.05/0.08 (free; s21/r46 exist) to get r56: is s21 the outlier (s21 2.03 vs r46 3.40)?
- Board: swarm-a CMA cc13 s21 3.6/r46 3.9; swarm-r S2⊥-T2 at α<0 adds +5.8 % on 02f7; swarm-l phase-only chiral beats w2 parent.

## Wakeup 9 — 2026-10-15 ~06:50 UTC
- No r56 landed in 20 min (queue busy). Agents m, g, d, i finished early (all directions owned).
- swarm-c w2-chiphase closed: S7 b≈−0.015 on df59 strong (+3 pts). swarm-b (α_S2∥, c7) plane: optimum α≈0.40–0.45, c≈0.10.
- Plan: wait for r56 (E keepers, F, G, R), post w2-141f result + finite-size note + coverage, then `swarm done`.
- 07:16 still no r56 for my 9 pending (queue). Board: swarm-a claims 713b (min 3.97), b4b8 (min 4.50); swarm-o 90a9 s21 5.11 at Σ|β| cap. p, n finished.

## Wakeup 12 — 2026-10-15 ~07:48 UTC — DONE
- r56 still queued (75+ min). Posted close-out result c25b (w2 141f, s21-vs-r46 spread, 4 coverage blocks); mailed swarm-o.
- `swarm done` with summary. 103/500 charged. Loop stopped.
