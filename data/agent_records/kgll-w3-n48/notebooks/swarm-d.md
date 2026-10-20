# swarm-d notebook

Started 2026-10-08T04:34:42+00:00.

## 2026-10-08 05:05 UTC — wakeup 1 (orientation + launch)
- Read brief, theory (generalized-space-theory, notes §5.6–5.9, §7.4–7.6, §12, App. B), pilot 024 (doc 40), doc 46, ADR-0037/0040, validate.py.
- Key physics: any k-dep γ breaks ideality: ⟨tr g⟩ − l_B² = ⟨Var_k ∂₊γ⟩ (eq 7.26), quadratic. First-order responses are cluster artefacts (024: +0.51% 4x6 → −0.92% 5x6). Doc 46 w3 S1T1 α±0.05 at s21: +1.85/−9.04 → mostly odd; even part −3.6%.
- Board at start: atlases by c (T1), f (T2/T3), b (all 30 at ±0.05; overlaps), a (w2), e (joint (G,R) pair orbits). Posted herding note + mailed b.
- MY FAMILY `hess-even-w3` (hyp 20261008T050202.650Z_swarm-d_hypothesis_fa14): 12-D subspace {S1,S2,S3}×{T1,T2}×{amp,phase}, coords c=α/2 or β; Sobol seed 4 directions on sphere, ±r·u, r=0.03, g_cutoff 8, n_mesh 48. Fit even parts → 12×12 Hessian (78 unknowns), odd → gradient. Then eigvec line scans. Budget ≤180 + ≤80.
- Tools: work/build.py (terms → input), work/hess_dirs.py OUTDIR RADIUS N START (writes dirs.json with x per name). Request "source" field in `swarm show` maps req → file name.
- Submitted batch1 = dirs 0–15 (32 reqs, sub1/). Next: batches of 32 for dirs 16–83 as slots free; write collector + ideality-defect feature calc.

## 2026-10-08 05:36 UTC — wakeup 2
- Board exploded (48 agents). Leaders: S1T1⊥ and S2T1∥ joint orbits (Z2 half-translation invariant; swarm-h rule), only linear directions. ad's d746 = ⊥ orbit at 0.173/pair: s21 1.362. swarm-w: chiral β on |G|²=7 twins ×T1 → s21 1.053, r46 1.21 (phase-only!).
- swarm-n critique: even part is a cone along Z2-breaking coords → separable Hessian invalid. Accepted. hess-even-w3 closed after 32 evals; result post 20261008T052801.627Z_swarm-d_result_c2af (odd additive corr .97; even tracks D, E≈−1.1D; board-wide D explains 72% w2, 15% w3).
- Tools: work/features.py (D_ideal, M2k, M2bar), work/board_feats.py LB.txt (features for all leaderboard reqs → board_feats.json), work/collect.py (my results → results.json), work/dress*.py.
- NEW FAMILY dress-w3: dress d746 with Z2-invariant achiral α orbits (G_i+2Λ*, R_i); D-min dressing: |G|²=7 twins −0.143 → D .259→.056, M2k 4.44→3.56. Submitted dress1/ 5 evals (dr_full 9cdf, dr_half 47f4, dr_7only 16ba, dr_7plus 3730, dr_alone 2355). Discriminates D-cost vs M2-gain.
- Budget: 37/500 charged.

## 2026-10-08 05:55 UTC — wakeup 3
- dress-w3 REFUTED D-as-cost: dr_full (D .056) s21 1.026 vs base 1.362; dr_7only 0.52; dr_alone 0.535; dr_7plus FAIL. Posted abandon 20261008T055201.201Z_swarm-d_abandon_d115 (retracts E≈−1.1D as a design rule).
- Frontier now: e's ridge c⊥+c∥≈0.2 (s21 1.45/r46 1.41); j chidress-w3 (S2∥ α .2 + chiral β .015 on S4/S7/S9/S10 twins ×T1) s21 2.03 (ba1f). r56 still pending for EVERYTHING incl. parent.
- Symmetry audit tool work/audit.py (C6, Mx parity of amp/phase in solver basis). Top 400: all C6 except 3 of h's; 72 entries have chiral-α (TL-linear-forbidden) e.g. s 9519/6210 → note 20261008T055406.709Z_swarm-d_note_7506, mailed s.
- Role now: verifier / finite-size auditor (s21→r46→r56 trends when r56 lands). w3 frontier saturated by ~10 agents; w2 by ~8.
- Budget 37/500.

## 2026-10-08 06:28 UTC — wakeup 4
- No r56 results yet anywhere (swarm-c filed request to human). Frontier: j chidress (S2∥ α.2 + chiral β .015 on S4/S7/S9/S10×T1) s21 2.03; pure phase-only owned by w; w2 owned by m/b/q/ai; verifiers: at, x, u, l, z, ae, n.
- Every direction I considered is owned; stay reserve, don't add noise. s replied re chiral-α (small, will ablate).
- Next: when r56 lands → finite-size audit (s21→r46→r56) of my promoted pts (3f7b, fc69) and look for systematic sign flips across the board; offer budget for sign-reversal checks if asked.

## 2026-10-08 07:18 UTC — DONE
- r56 still empty swarm-wide; ≥8 reserve/verifier agents. Nothing distinct left for me. Ran `swarm done` with summary (work/done.md). 37/500 evals used.
