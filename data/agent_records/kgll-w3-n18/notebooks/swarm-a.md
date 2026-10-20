# swarm-a notebook

Started 2026-10-15T04:12:53+00:00.

## 2026-10-15 04:20 — wakeup 1 (first agent active; board empty)
- Read brief, progress/40 (LL01 pilot: +0.51% 4x6 -> -0.92% 5x6), progress/46 (Nk21 w3: a[S1,T1]=+0.05 +1.85%, -0.05 -9.0%, b +0.05 -4.4%, a[S3,T1]+0.05 -3.75%).
- Physics prior: static LL0*h(r) is an ideal (vortexable) band; any k-dependence breaks it -> expect concave, mostly negative responses.
- Tools: work/gen.py (star(g2), tstar(r2), make(parent, sp, mo, alpha, beta, path)); g_cutoff = 4+max|m|. swarm check ~1 s.
- File naming: S{|G|^2}_T{|R|^2}_{ap,am,bp,bm}; NB "T3" in filenames = |R|^2=3 (brief's T2), "T4" = |R|^2=4 (brief's T3).
- Posted hypothesis f668: family w3-atlas, 30 directions x {a=±0.10, b=±0.05} = 120 evals.
- Submitted atlas/c0 (30). Pending: atlas/c1..c3 (90) when in-flight < 32.
- Next: collect atlas table -> result post; line searches on positive slopes; CMA-ES in best subspace.

## 04:35 — wakeup 2
- Atlas: all 120 accepted (broker queues beyond 32). First 30 done: almost all R<1 (0.81–0.97); S1T1 a=+0.1 -> s21 1.034, r46 1.048, r56 1.043 (req 6553, SUGGESTIVE); S1T1 a=-0.1 0.846; S3T1 a=+0.1 1.019.
- Board hot spot: G⟂R joint orbit (G=(1,0)↔R=(0,1), (1,1)↔(1,-1), (0,1)↔(1,0)), swarm-b f06f a=0.05: 1.105/1.088/1.092 (s21/r46/r56); swarm-j 7d04 a=0.2: s21 1.369. Herding there (b, i, j, k).
- My niche now: mechanism controls. work/matched.py (BZ-avg density static control; g2max 64), work/sharpen.py (rho*exp(k rho), M2-matched). Controls submitted (w3-mechctl): 8e7b (f06f avg, M2 3.6336), f0e2 (7d04 avg, M2 3.7138), a6e6 (sharp M2 4.733). Note baa9 posted; mailed b, j.
- Read other agents' inputs via path from `swarm show` (ed_input path) read-only.
- Next: atlas table post when done; control results post.

## 04:58 — wakeup 3
- Atlas done; posted result 7460 (table). Key: only S1xT1 a>0 gains (6553 suggestive 1.034/1.048/1.043); beta even; damage grows with |G|; |R|^2=3 extra-bad on s21; 18 FAIL at |G|^2>=13.
- Controls done: 8e7b (rho_bar f06f) 1.001 all; f0e2 (rho_bar 7d04) 1.017 all; a6e6 (sharp static M2 4.733) 1.184/1.196/1.191 vs 7d04 1.369/1.386/1.306. Posted result b1ca.
- 7d04 (swarm-j S1perp a=0.2) is STRONG claim; leaderboard top ~1.38-1.39 (swarm-h phase additions, b, e nematic).
- Mechanism controls now herded (p,m,l,q,r,n,d) -> I leave that.
- New family w3-cma (hyp e566): CMA-ES pop 12, 14-D C6-symmetric joint classes around 7d04. Driver: work/cmaes.py (`step` is idempotent; state cma/state.json). Gen 0 submitted.
- Budget used ~129 + 12.

## 05:12 — wakeup 4
- CMA gen0: best 1.3008 (7288), median 1.215 — all below 7d04 (1.369). σ0=0.04 in 14-D too large; 7d04 is a sharp (cusp on s21) local max for most dims (swarm-e eced, swarm-b 81d6).
- Gen1 submitted (σ 0.037). Plan: after gen1, re-scope CMA to small subspace of classes positive at base: S1⊥ α, S2∥ α (|G|²=3×T1, G∥R: b a90f; swarm-r combining), chiral β L−R S7/S13×T1 (swarm-h owns lines; e9e8 +0.6–0.9% all clusters).
- Mail: h (leave chiral dims to h), b (no joint optimizer), n (extending a6e6 into static frontier), e (w2 global GP).

## 05:30 — wakeup 5
- 14-D w3-cma closed (abandon 2cdf): 24/24 PASS, all < 7d04 (best 1.304).
- New positives on board: S2∥ (r 09f8 a=0.2: 1.452/1.413; S1⊥ and S2∥ COMPETE), chiral β L−R S7/S13 on top of 7d04 (h 0672: 1.427/1.461/1.440/conv 1.461 STRONG), outer T1 classes 7@49° (o 7ad6), 13@16°. w2 strong claim (g 141f). Static sharpening reaches 1.45 at M2=8 on s21 (n 7477) — k-GLL still wins at matched M2.
- New family w3-stack (hyp 7c56): 8-D CMA in u-space (x=SCALE*u), work/cmastack.py (imports cmaes.py machinery; state stack/state.json). Pop 10, ≤10 gens. Gen0 submitted.
- cmaes.py refactored: main(cmd), `tell` command; gen dir = ST.parent.
- Budget ~177 + 10.

## 05:52 — wakeup 6
- Stack v1 gen0 (10 evals): best 1.625 (6721), median 1.465 — BUT coords a_7at49 / a_13at16 were WRONG (o's table lists G_R reciprocal; R = z×G_R). Correct: c7=(3,1)↔(1,-1), c13=(4,1)↔(1,0), c19=(5,2)↔(0,1), c21=(5,1)↔(1,-1). Posted correction note.
- Board jump: class-resolved chiral β on resonant c7 (+0.08 on mirror, −0.08 on c7) + S2∥ 0.25 = 02f7 (b): s21 2.38 / r46 2.59. j c89a (+chiral 19) s21 2.45. p fe3d strong 1.69. 
- New CMA: work/cmastack2.py (state stack2/), 10-D, start c89a, pop 12, ≤8 gens. Gen0 submitted.

## 06:03 — wakeup 7
- stack2 gen0: best b3f2 s21 2.881 / r46 3.079 (PASS, climbing to r56) — new board high. x = S1⊥ .05, S2∥ .273, a7 .015, b7 .103, a13 .007, b13 −.013, a19 −.016, b19 −.036, a21 .027, b21 −.029. Landscape rugged: gen0 median 1.73, range 0.87–2.88.
- Gen1 submitted (mean S2∥ .269, b7 .087).
- Board: f/d verify leaders are M·T-invariant (no chirality artefact); n: best static ≈1.58–1.62; q: 02f7 converged (−0.55% at n_mesh 64/gc10); h: 19@67° chiral +0.03 on 02f7 → s21 2.44 / r46 2.94.

## 06:20 — wakeup 8
- stack2 gen1: best cc13 s21 3.599 / r46 3.909; f395 r46 4.024; 8839 3.19/3.81. median 2.87. All PASS, r56 pending. Posted interim result.
- Widened S2∥ hi to 0.50 (b: S2∥ keeps paying to 0.35 at c=0.10). Gen2 submitted.
- Others verifying: o radial scan through b3f2 (w3-radial: λ scaling, M2 up to 9.4 → 3.1), m replicating cc13 convergence.
- Done agents: i, d.

## 06:37 — wakeup 9
- b3f2 ladder complete: s21 2.881 / r46 3.079 / r56 3.083 / conv46 3.090 all PASS (strong-level). cc13 r56 3.775 (conv pending); 8839 r56 3.683.
- gen2 best 713b 3.969 (s21), 772a 3.81. median 3.18.
- Objective switched (gen3+) to min(s21, r46) for promoted points (cmaes.USE_R46) — j warned 13/21 classes raise r46 but cut s21.
- One gen3 candidate rejected: m2k_max_ratio 3.18 > 3 (S2∥ 0.305) → M2^(k) boundary is near for large S2∥; leaders at ratio ~1.8.
- q checking 713b/772a at n_mesh 96 / g_cutoff 14 (19/21-shell harmonics near cutoff 9).
- Pending: claim post once cc13 conv46 lands.

## 06:55 — wakeup 10
- Ladder complete: 713b s21 3.969 / r46 4.803 / r56 4.563 / conv46 4.797 (strong) → CLAIM posted 6e55. 772a 3.81/4.84/4.65/4.81; cfd4 3.70/4.78/4.61/4.77; cc13 3.60/3.91/3.78/3.90; f395 3.16/4.02/3.91/4.03.
- ρ̄ control for 713b queued: 0a34 (ρ̄ M2 3.906 vs M2_k 6.56).
- gen3 best (min s21,r46) b4b8 4.497. σ=1.23 (still growing). Gen4 submitted.
- o ablation: 713b α-only 1.82, β-only 0.42 → strong α×β interaction. m: qmax 8→10 shift −0.35% for cc13; suggests qmax 12 for finalist (ask human?).
- Agents done: i, d, m, g.

## 07:12 — wakeup 11
- b4b8 ladder: s21 4.497 / r46 5.747 / r56 5.543 / conv46 5.742 → CLAIM posted (supersedes 713b). M2_k 5.26.
- 713b ρ̄ control 0a34: 1.0498/1.0499/1.0499 → beyond averaged density. b4b8 ρ̄ control queued 0197.
- gen4 best 4.327, median 3.75. gen5 submitted (MAXGEN 8 → gens 5,6,7 left).
- r: S2⊥-T2 (|G|²=3×|R|²=3 ⟂, α −0.05) adds ~3.5% on 713b (5d7c 4.108/4.907); r testing on b4b8.

## 07:30 — wakeup 12
- gen5 best 9419 min(s21,r46) 5.775 (r46 7.066), 6b73 5.28/6.83. Σ|α| hit my 2.4 shrink cap → frontier is boundary-limited (o: R linear in λβ to Σ|β| cap; o asked human re beyond-boundary).
- Raised shrink caps to Σ|α| 2.49, Σ|β| 1.99. gen6 submitted (one cand rejected m2k ratio 3.22>3).
- b4b8 ρ̄ control 0197: 1.0075/1.0082/1.0080.
- Done agents: i, d, m, g, n, p, c.

## 07:47 — wakeup 13
- 9419 ladder: 5.775 / 7.066 / 6.948 / conv46 7.150 all PASS (strong). Not yet claimed (will post consolidated claim at CMA end).
- gen6 best 37c9 6.209 (min s21,r46), median 5.29. σ 1.70 growing (boundary ridge). MAXGEN raised to 12. gen7 submitted.
- Trend: a13 → +0.12, b19 → −0.15..−0.17, S2∥ 0.3–0.37, b7 ~0.09–0.12.
- k (w3-bcap): β reallocation at cap toward 19, off 21: cd23 5.60/6.62. q: 9419 kernel-converged (n_mesh 96/gc 14 ≤1e-4); only qmax unmeasured → plan a human request for qmax=12 on the final headline.
- Done agents: i,d,m,g,n,p,c,q.

## 08:04 — wakeup 14
- gen7 best 9a85 min(s21,r46) 8.127 (r46 8.855), 93d4 8.08/8.70, 1298 7.92. Both at Σ|α| 2.49 and Σ|β| 1.99 caps. ent gap falling (5 → 3.4), split/Δ ~1e-2 (gate 0.1) — watch PES margin.
- Trend: a13 → 0.13–0.15, a19 → −0.13, b19 → −0.18 (β_max 0.18 ≤ 0.3), S2∥ drifting down 0.24–0.33.
- gen8 submitted. σ 1.93.
- Done agents now include f, h, j (most of swarm finished early).
- 08:17 gen8 5/12 scored; 9a85 r56 9.088, 93d4 r56 8.881 (both converge stage).

## 08:30 — wakeup 16
- 9a85 ladder: 8.128/8.855/9.088/conv46 9.038 (strong); 93d4 8.08/8.70/8.88/8.81; 1298 7.92/8.62/8.55/8.64.
- gen8 best 7.27, median 6.00 (no new best). gen9 submitted.
- Posted request to human: qmax=12 rerun of final headline + boundary-limited frontier.
- k (w3-bcap) still reallocating β at cap on 713b-family: e5e5 6.18/7.39.
- 08:45 gen9 best 7.76 median 5.17 (no improvement 2 gens). gen10 submitted. o, r done. Plan after gen11: facet-local polish of 9a85 (β/α reallocation at caps; S2⊥-T2 probe).
- 09:03 gen10 best 7.76 (plateau). gen11 (last) submitted. Facet polish P01-P13 around 9a85 submitted (ids work/polish/ids.txt; base coords work/polish_base_9a85.json). Posted budget-overrun note.

## 09:20 — wakeup 19
- CMA finished (gen11 best 7.96). CMA overall best 9a85 (8.128 min).
- Polish (Δ vs 9a85 s21 8.128/r46 8.855): P01 b13→19 8.765/9.222 (best); P06 S2→a13 8.51/9.00; P07 a13→a19 8.44/9.19; P13 S2⊥T2 8.40/9.27; P03 b7→19 8.41/9.08; P11 a13→a7 8.37/9.14; P10 S1→S2 8.24; neg: b21→19 7.66, a7→a13 7.65, a13→S2 7.73, a19→a13 7.74, b19→7 7.78, S2→S1 8.00.
- Gradient step G05/G10/G15 (t=0.5,1,1.5 of the combined positive moves, at caps) submitted (polish/ids_grad.txt).

## 09:35 — wakeup 20
- Gradient step from 9a85 worked: G05 9.19/9.78, G10 (bb41) 9.58/10.06, G15 9.61/9.69 (s21/r46). Base G10 coords in work/polish_base_G10.json.
- Round-2 polish (11 one-sided budget-preserving moves around G10) submitted; tool work/polish2.py (transfer(x,src,dst,budget)).
- r56 promotions queue slow (b reports stuck >4h). Our polish r56 pending.

## 09:50 — wakeup 21
- Round-2 polish around G10 (s21 9.577): S2→a19 10.185, S2→a13 10.153, a7→a19 9.863 (r46 10.36), S1→S2(all) 9.658, b13→b19(all) 9.634; neg: b7→19 9.55, a13→a19 9.44, S2→S2⊥T2 9.26, a13→a7 8.96; b21 removal catastrophic (b21→19 4.84, b21→7 5.75) — b21≈−0.02 is critical.
- G15 r56 11.125.
- Gradient step 2 H05/H10/H15 submitted (polish3/ids.txt; coords polish3/H*.coords.json).

## 10:04 — wakeup 22
- Step 2: H05 10.40/10.14, H10 (bf0d) 11.11/10.17, H15 11.39/10.11 (s21/r46) → now r46 limits (~10.1–10.2).
- G10 ladder: 9.577/10.058/10.742/conv 10.268 (strong). G15 r56 11.125 conv 9.867.
- Round 3 from H10 (r46-improving moves a7→a19, b7→b19, both): polish4/ids.txt. After that: finalize (claim + coverage), consider done.
- 10:15 R_a7_to_a19 (7a22) 11.30/10.44 (new best min); R_b7_to_b19 s21 11.19, R_both s21 11.39 (r46 pending). r56 queue slow (b, l report stuck promotions).

## 10:33 — wakeup 24
- Round 3: a6a0 (R_both: a7→a19 + b7→b19 from H10) 11.393/10.556/r56 12.044 (conv pending) = best min 10.556. 7a22 11.30/10.44/11.83. 32ea 11.19/10.27.
- H-series ladders: H05 10.40/10.14/11.35/conv 10.38; H10 11.11/10.17/11.68/10.39; H15 11.39/10.11/11.83/10.33.
- Diminishing returns (9.58→10.17→10.56 per round, r46-limited). Decision: wrap up after a6a0 conv46 + ρ̄ control.
- ρ̄ control for a6a0 needed |G|²≤400, nm 96 (sharp averaged density): 49f5 (M2 3.409 vs M2_k 4.628). matched.py now nm=96, range ±24.

## 10:50 — FINAL
- a6a0 ladder: 11.393 / 10.556 / 12.044 / conv46 10.753 strong, on Σ boundary. ρ̄ control 49f5: 0.960/0.970/0.966.
- Posted claim 41f1, coverage result 0abd, swarm done (~349/500 charged).
- Open for human: request 0136 (qmax=12 rerun of a6a0; widen Σ box?).
