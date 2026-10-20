# swarm-q notebook

Started 2026-10-15T04:13:48+00:00.

## 2026-10-15 04:30–04:37 — wakeup 1: scope = mechanism controls (`mech-control`)
- Board: S1⊥ matched joint class (G ⟂ R, |R|=l²|G|) is the hot direction; b, i, j and k are all on it (herding). Best: swarm-j S1⊥ α=0.2 `…_req_7d04` s21 1.369 (M2k 4.73); f06f (α=0.05) s21 1.105 / r46 1.088 / r56 1.092.
- My role: claim 2 (beyond-M2). Built two controls:
  1. `work/matched_control.py` gives the static ρ̄ = <ρ_k>_BZ (ρ_k normalised to uc mean 1, as in the broker's M2k). ρ̄ ≈ w3: M2(ρ̄) = 3.634/3.649/3.714/3.822 at α = .05/.1/.2/.3. Submitted `--control` on s21,r46,r56: 85f4 (7d04), 50a3 (8e11), 00e4 (6139); s21 only: 6463 (f06f).
  2. `work/scrambled.py` gives a k-relabelled control (cyclic shift of the diagonal α along the momentum list = rotate R by 60°/120° = 30°/150° classes). M2k is identical (verified 4.73294). Submitted as search: d2d2, 86c3 (6139), de99, a1bc (7d04), ceb6, c66d (8e11).
- An M2-matched static control by scaling w3 is impossible: w3 sits on the positivity edge.
- Posted hypothesis f76e; mailed b, i, j, k.
- Next: read the control results; repeat both controls for every candidate reaching r46 with min R ≥ 1.05 (including w2 and the multi-class stage-B winners).

## 2026-10-15 04:52–04:56 — wakeup 2
- Controls done (result post 63b2): ρ̄ static R = 1.001 (α .05), 1.004 (.1), 1.017 (.2), 1.038 (.3), cluster-independent, PASS. k-relabelled (30°/150° classes, same M2k) give 0.91 / 0.75 / 0.49 (one FAIL). So the S1⊥ gain is k-correlation, not density.
- Nine agents piled onto density controls, so I switched.
- New family `w3-perp-chiral2` (hyp 947f): complex ℓ = ±2 patterns on the S1⊥ pairs at base α = 0.2: α_j/2 + iβ_j = 0.1 + c e^{iφ} e^{−2iχθ_j}. χ+ and χ− have the same α, opposite β, and α equal to swarm-e's e1 nematic points. 12 evals: c = .05 at φ = 0/90/180/270, c = .1 at φ = 0/180, χ = ±. Script `work/chiral_l2.py`; inputs in `work/chiral_A`.
- Next: compare χ+ vs χ− (floor ~0.6 %); if one wins above 1.369, line search in c, then φ, then S2⊥/S3⊥ chiral.
- Charged: 28/500.

## 2026-10-15 05:12–05:16 — wakeup 3
- Chiral ℓ = 2 C1 results (result 5191, abandon e137): none beats 7d04. At c = 0.1, χ+ (c_j ∝ e^{−2iθ_j}, the "a†²" channel) is at s21 1.03–1.05, while χ− is at 1.22 with the same α: a 17–18 point chirality splitting. χ− ≈ swarm-e's real nematic. The C6 S1⊥ point is a local max of the complex 3-pair space. Family closed (12 evals).
- New leaders: swarm-r S2∥ (|G|²=3 × T1, G∥R) α = 0.2, `…09f8` s21 1.452; swarm-h S1⊥ + |G|²=7 chiral β, `…0672` r46 1.461; w2: swarm-g oblique `…88e5` strong 1.11–1.13; swarm-c g4perp `…df59` s21 1.162.
- Controls extended (mech-control):
  - 09f8: k-relabelled 0bbb, ed18 (s21); ρ̄ 70ee (s21, r46, r56). M2(ρ̄) = 3.734 vs M2k = 4.571.
  - w2 88e5: ρ̄ 092e (3 clusters); rotated-R c715 (n=1), 08ad (n=2).
  - w2 df59: ρ̄ 01ce (3 clusters); rotated-R db9f (n=1), 419b (n=2).
- New tool `work/rotate_R.py`: rotates every momentum R by 60° (direct basis (m1,m2) → (−m2, m1+m2)). It is general, unlike `scrambled.py`, which needs ordered stars. w2 ρ̄ needs `--tol 1e-11 --n-mesh 96`, because w2 touches zero and truncation makes it slightly negative.
- Charged ≈ 28 + 2 + 13 = 43.

## 2026-10-15 05:33–05:38 — wakeup 4
- Control results (posted in a3e6):
  - 09f8 (w3 S2∥): ρ̄ 1.0175 / 1.0177; rotated 0.822 / 0.813.
  - w2 88e5: ρ̄ 0.9993 / 1.0004 / 1.0004; rotated 0.893 / 0.896.
  - w2 df59: ρ̄ 0.9999 / 1.0004 / 1.0004; rotated 0.882 / 0.884.
  - Conclusion: every amplitude leader is a k-assignment effect.
- New w3 leader: swarm-b 02f7 (S2∥ α = 0.25 + |G|²=7 resonant chiral β = 0.08), s21 2.380 PASS (PES gap 5.2). M2k 5.16; g_cutoff 7, n_mesh 48.
  - Queued rotated controls 1c2d, 7c8b and the s21 convergence diagnostic cbd0 (n_mesh 64, g_cutoff 10).
- swarm-c asked for w2 ρ̄ controls: df59 done; 2aa0 queued (c4f3).
- Static sharpening of w3 alone reaches about 1.56 (swarm-n). The ρ̄ control does not answer "beats all statics".
- Charged ≈ 49.
- Next: if cbd0 differs from 02f7 by more than 1 %, post a critique (convergence). Consider an independent convergence-check role for top claims at s21/r56 with g_cutoff/n_mesh (conv46 is 4×6 only).

## 2026-10-15 05:56–06:00 — wakeup 5
- 02f7 results:
  - convergence cbd0 (n_mesh 64, g_cutoff 10): s21 2.3670 vs 2.3801, −0.55 %, converged.
  - rotated 1c2d 0.279 FAIL, 7c8b 0.359 FAIL.
  - 2aa0 ρ̄: 0.996 on all clusters.
  - Posted result c2d8.
- Board: w3 stacking of resonant chiral β (|G|² = 7, 13, 19, 21 × T1) on S2∥/S1⊥ bases, s21 up to 2.88 (a b3f2), r46 up to 2.94 (h 4927). Healthy diagnostics: adm ≥ 0.75, M2k/M2 ≤ 2.1, PES gap ≥ 3.7. Heavily herded (a, b, h, j, p, r, l, o, d). Verifiers: f, n, m, d.
- Decision: no new search family (none uncovered that beats the herd). Keep a low-cost verifier service: rotated-R control plus an s21 convergence rerun for each new `strong` claim that nobody has checked. Charged ≈ 55.

## 2026-10-15 06:28–06:31 — wakeup 6
- Board: the swarm-a w3-stack CMA (10-D resonant chiral frame) leads: 713b s21 3.969; 772a s21 3.812 / r46 4.840; cc13 3.60 / 3.91 / 3.78. M2k/M2 ≤ 1.81, adm ≥ 0.8, PES gaps 4–5. Uses outer stars up to max|m,n| = 5 with g_cutoff 9 and n_mesh 48.
- Queued: convergence diagnostics 895d (713b) and fcb5 (772a) at n_mesh 96 / g_cutoff 14; rotated-60° controls 5564 (713b) and 857d (772a). Mailed swarm-a.
- w2 leader: swarm-p 8a0d, strong (1.23 / 1.41 / 1.38 / 1.41). Phase-only chiral at the w2 parent beats the parent (swarm-l, 1.07 / 1.22), which is a clean beyond-M2 result on w2.
- Watch item: the s21 → r46 spread grows with gain (27 % for 772a).

## 2026-10-15 06:48–06:53 — wakeup 7
- 713b converged (895d 3.9693 vs 3.9691); 772a converged (fcb5 3.8116 vs 3.8119). Rotated-60° copies 5564 and 857d: R 0.0003, FAIL (manifold destroyed). Posted result.
- At swarm-b's request, queued ρ̄ for 02f7 (4c20) and for 713b (e437) on s21, r46 and r56. M2(ρ̄) = 3.799 and 3.906.
- Frontier: a b4b8 s21 4.497 / r46 5.747; r 5d7c 4.11 / 4.91. The s21 → r46 spread is +21–28 %.
- Several agents have now run `swarm done` (d, g, i, m). Charged ≈ 69.

## 2026-10-15 07:15–07:19 — wakeup 8
- ρ̄ results: 02f7 → 1.028 (all clusters), 713b → 1.050 (all clusters). Posted.
- Frontier: a 9419 s21 5.77; o 90a9 s21 5.11 / r46 6.04 at Σ|β| = 1.94. It is boundary-limited (o asked the human about going past the boundary).
- qmax is not agent-free, so the qmax = 12 finalist rerun needs the human (said so in my post).
- Queued convergence diagnostics 0437 (9419) and 107b (90a9) at n_mesh 96 / g_cutoff 14.
- Many agents are done (d, g, i, m, n, p). My remaining role is narrow. Plan: post the convergence results, then `swarm done` unless something new needs a control.
- Charged ≈ 77.

## 2026-10-15 07:40 — wakeup 9 (final)
- Convergence: 9419 → 5.7743 (vs 5.7749), 90a9 → 5.1138 (vs 5.114). Posted result 1af8.
- Ran `swarm done` with a summary: 61/500 charged. Open item for the human: a qmax = 12 rerun of the headline point.
