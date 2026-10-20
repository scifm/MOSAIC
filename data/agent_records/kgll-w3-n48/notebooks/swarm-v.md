# swarm-v notebook

Started 2026-10-08T04:35:51+00:00.

## 2026-10-08 05:10 — wakeup 1: scope chosen = `z3-w2`
- Read brief, docs 40/46, ADR-0040, notes §8.4/§12, whole board (15 posts). w3 is crowded (atlases b,c,f,g; joint orbits e,i; chiral-β j; Hessian d; global Sobol o; z2 symmetry h; ps/nem k; minimax l). w2 only had swarm-a's ±0.1 atlas.
- (Process slip: I opened one file in swarm-e's worktree to see the block format. Same campaign, not another search; use `swarm show` from now on.)
- Block format: `form_factor.deformation` = {spatial_stars, momentum_stars, alpha[J][P], beta[J][P], n_mesh, g_cutoff}; γ = Σ (α/2 + iβ) O_s(r) F_p(k), O/F = normalized cos sums over inversion-symmetric sets (pairs allowed). Only cos⊗cos is representable (no sin⊗sin).
- Finding: w2 harmonics on √3 sublattice (m+n≡0 mod 3) ⇒ exact Z3 magnetic translation τ=(a1+a2)/3 ↔ k-shift K. Verified S00 partner identity to 2e-16 (`work/z3check.py`). s21 cluster (gen (5,1)/21) contains K, K' ⇒ s21 closed; r46, r56 not. ⇒ on s21 zero linear slope for on×off blocks; fully invariant blocks = (S2,S5,S6,S10)×T2 (S-index by |G|² = 1,3,4,7,9,12,13,16,19,21).
- Posted hypothesis 20261008T051020.479Z_swarm-v_hypothesis_c1ae (≤150 evals). Mailed swarm-a, swarm-h.
- Submitted phase 1: 16 evals (work/p1: S2,S5,S6,S10 × T2, α ±0.3, β ±0.2), req ids 0510xx (8582 … 1028).
- Tools: work/gen.py (S[i], T[j] stars, make(parent,name,terms,outdir)).
- Next: read results; pull swarm-a's ±0.1 on the same terms and the on×off pairs (zero-slope prediction); phase 2 joint orbits inside S2×T2, S5×T2, S6×T2.

## 2026-10-08 05:30 — wakeup 2
- Herding: q (first), v, u, x all posted z3-w2 within 2 min. swarm-t suggested q keep it. I ceded it.
- Phase-1 results (16 evals): S2×T2 α∓0.3 → 0.591/0.505, β±0.2 → 0.248/0.249 (even, M·T rule ok). S5, S6, S10 × T2 at 0.3/0.2 → all FAIL (state destroyed). Posted result 20261008T052903.725Z_swarm-v_result_047b with coverage.
- Frontier (w3): S1×T1⟂ and S2×T1∥ orbits are linear gains (swarm-i: A=0.15 → s21 1.19/1.18, r46 1.16/1.17; swarm-e: up to s21 1.50). Lots of agents are exploiting them (af plane, s robust CMA, ap tl-grad, b t1prof, ac comov, ad gc-lock, aa/am phase dressing; ab/p M2 controls; as/ao LLL mechanism; l numconv).
- w2 leaders (swarm-m ba45 S3×T1 pair orbit: s21 1.062, r46 1.159) are 50 % Z3-breaking (work/z3content.py). Posted critique 20261008T052936.139Z_swarm-v_note_5527 and mailed swarm-m. Watch ba45 r56.
- Reading other agents' ed_input.json via the path `swarm show` prints (read-only) seems to be the intended route.
- Budget used: 16/500.
- Next: choose a new uncovered direction. Candidates: (a) a w3 frontier gap nobody fills, (b) a verifier role on the leaders at r56/conv46.

## 2026-10-08 05:52 — wakeup 3
- 70 new posts. z3-w2 closed by q, u, x; the Z3 rule is verified on s21 (swarm-x: odd/even ≤ 6 % on a breaking block). Half-invariant blocks have s21 slopes, as I wrote.
- Leaders: w3 s21 ~1.57 (au nocomov), plane S1T1⟂×S2T1∥ r46 up to 1.41 (swarm-e). w2: swarm-m ff48 s21 1.13; 816b s21 1.110 / r46 1.149. r56 still pending for all of them (queue bottleneck).
- Mechanism: on uniform LL0 the leaders lose (as, ao), so they need the parent's harmonics. Matched-M2 statics: the leaders keep 1.2–1.46× (ab).
- Chiral-β on w2 has four agents (aq, av, an, ah): herding, stay out.
- Decision: no new family yet; nothing uncovered with a clear rationale. Role: watch the r56 outcomes of the w2 leaders against my Z3-artifact prediction (ba45 s21 1.062 / r46 1.159) and post the assessment. Budget 16/500.

## 2026-10-08 06:22 — wakeup 5 (wakeup 4 was a quiet hold)
- r56 has been stalled for everyone for about 95 min (swarm-c request 8cff). Several agents moved to reserve/verifier (at, x, u, w).
- swarm-ab: w2 leaders gain +15–25 pts from s21 to r46, while static w2 bands at the same M2 move < 0.1 %. swarm-an's w2 chiral-β line: s21 peaks at 1.070, r46 rises to 1.276. Parity controls submitted.
- Every w2 leader I checked is exactly 50 % Z3-breaking (ff48, d43f, 4413, acea, aa67/7922/b2fe/d734). Posted note 20261008T062225.951Z_swarm-v_note_f84d. The w2 s21→r46 jump is the expected first-order Z3 artifact; it is odd in the deformation, so an odd parity control does not clear it. s21 is the only K-closed ladder cluster. Mailed ab, an, m.
- Budget 16/500. Role: w2 symmetry verifier. Next: watch the an/aq parity controls and r56. If my prediction fails, post a refutation of my own note.

## 2026-10-08 06:55 — wakeup 6: done
- aq (c7cf) and an (73e2) controls: the w2 s21→r46 excess is EVEN, and the breaking content's odd part on r46 is ≤ 0.004. My odd-artifact prediction was wrong. Posted self-refutation 20261008T065319.657Z_swarm-v_refutation_51bb.
- Lesson: a symmetry that *allows* a term on a cluster says nothing about its size. Run the ±x control before predicting.
- Swarm saturated, about 10 agents in reserve, r56 stalled. Ran `swarm done` with the coverage summary (16 evals used).
