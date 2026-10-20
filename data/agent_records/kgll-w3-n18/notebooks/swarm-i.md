# swarm-i notebook

Started 2026-10-15T04:13:20+00:00.

## 2026-10-15 04:30 — wakeup 1: scope chosen = `perp-matched`

Board at start: a (w3 separable atlas), b (w3 joint classes + chiral), c (w2 atlas), e (w3 big amplitude),
f (s21 finite-size floor via mirror pairs), g (w3 chiral phase-only). d,h not posted yet.

Key board facts (from leaderboard / swarm show):
- b `…_req_f06f` S1T1 ⟂ class (G(1,0)↔R(0,1), G(1,1)↔R(-1,1), G(0,1)↔R(1,0)) α=+0.05: s21 1.1052, r46 1.0881 PASS. α=-0.05 (`8020`): 0.8333. Non-⟂ classes (c30 `7203`/`f883`, c150 `dfcc`/`f4aa`) lose both signs (0.94–0.96).
  Quadratic fit through ±0.05: slope 2.72/unit, curv -12.4 → vertex α≈0.11, R≈1.15 (extrapolation only).
- a `…_req_6553` separable S1T1 α=+0.1: s21 1.034, r46 1.048.
- c `…_req_5515` w2 separable S1T1 α=-0.1: s21 1.026, r46 1.080 (sign opposite to w3!).
- f: s21 is chiral (C6, no mirror); r46/r56 C2 only. |R|²=3 two-valued on s21; |R|²=4 aliased on r46. Only T1 sampled faithfully everywhere.
- g: MT symmetry → β-odd responses on achiral directions are cluster-shape artefacts; control = run (α,-β).

My hypothesis (post 20261015T043019.709Z_swarm-i_hypothesis_b878): b's winning class is the magnetic-translation
matched one: R_G = l² ẑ×G is a lattice vector ⟂ G with |R|=l²|G| (one flux/cell); e^{iGr} acts on LLL as e^{ik·R_G}.
Predict: S2T2⟂, S3T3⟂ also linear-responsive; S1T3⟂ (length mismatch) weak; w2 S1T1 signal in ⟂ class.

Tools: work/build.py (class builder; CLASSES dict), work/dump_board.py (board table; arg = substring filter).
Stage A submitted (20 evals): w3 S2T2⟂/S3T3⟂ α±.05 β±.025, S1T3⟂ α±.05; w2 S1T1{⟂,c30,c150}, S2T2⟂, S3T3⟂ α±.05.
Mailed b (I leave w3 S1T1⟂ line search to them) and c (w2 decomposition).
Next: read Stage A; line search on responsive matched classes; combine shells with b's optimum (--builds-on).

## 2026-10-15 04:55 — wakeup 2: stage A in; pivot to `w2-joint`

Stage A (perp-matched, 20 evals, all PASS on s21). Result post 20261015T045256.554Z_swarm-i_result_aaac.
- w3 S2⟂ ±α: 0.988/0.957; ±β 0.985/0.969. S3⟂: 0.934/0.950, β 0.943/0.943. S1×2R_G ⟂: 0.955/0.963. → only S1⟂ responds.
  Heuristic: cyclotron factor e^{-|G|²/4}: S1 0.16, S2 4e-3, S3 7e-4.
- w2 S1T1: ⟂ 0.973/0.960; c150 −α 1.0376 (r46 1.0441) `2834`; c30 −α 1.0346 (r46 1.0446) `89dd`; +α ~0.90.
  w2 S2⟂ 0.980/0.961, S3⟂ 0.847/0.921.
Board: swarm-j S1⟂ line: α=0.1 1.22/1.18(r46); 0.2 `7d04` s21 1.369 r46 1.386 r56 1.306; 0.3 1.235/1.204; 0.45 0.77A.
 b claim robust_positive f06f (α=.05: 1.105/1.088/1.092/1.088). ~7 agents (d,l,m,n,p,q,r,a,o) on mechanism controls (herding).
 a's M2-matched static control of S1⟂ line: +18% at M2 ratio 1.30 (`…a6e6`).
 swarm-p: chart term (G,R) = cyclotron e^{iGη} × guiding-centre harmonic at G±G_R; ⟂ → {0,2G}; 2G=S3 is a w3 shell, not w2.
 swarm-o: C6 co-moving S1⟂ mixes LL6 only; nematic needed for LL2 (swarm-e family w3-perp-nematic).
Ownership now: w3 S1⟂ line + matched joint = j; complement at optimum = b (S1T1/S1T2) and l (all non-⟂ later);
 w2 oblique line = g; w2 follow-ups = c; k: w2 (1,1),(3,3), w3 (1,4),(3,3),(4,4).
Pivot: family `w2-joint` (hyp 20261015T045314.571Z_swarm-i_hypothesis_2127): w2 classes of (1,3),(3,1),(1,4),(4,1),(4,4) at α±0.05,
 28 evals submitted. work/classes.py generates C6 classes (label = G–R angle mod 180); build.py accepts C<g2>_<r2>_<angle>.
Next: read w2-joint; line search any class ≥1.02 that holds at r46; else post null + coverage. Consider critique post (rule 11).

## 2026-10-15 05:20 — wakeup 3: w2-joint done

w2-joint (28 evals) result post 20261015T051944.829Z_swarm-i_result_d114. Only (4,1)⟂ gains: +0.05 → s21 1.0588, r46 1.1411 (`2ea0`),
−0.05 → 0.7863; odd slope 2.72 (= w3 S1⟂). All other T2/T3 and non-resonant T1 classes concave <1.
swarm-m T1 guiding-centre rule (note 20261015T050608.269Z_swarm-m_note_5d24): T1 class active iff G'=G±G_R hits parent shells
 (Σw(G') sign = slope sign); 0 misses on T1; fails on T2/T3. Suppression ∝ exp(-|G_R|²/4) (|R|), not |G| → my e^{-|G|²/4}
 heuristic in result_aaac was wrong (corrected in d114).
swarm-c already owns w2-g4perp (same class line + combos with oblique S1×T1; df59 s21 1.162 / r46 1.208). Not duplicating.
Board leaders: w3 j 7d04 S1⊥ α=.2 strong (1.369/1.386/1.306/1.386). w2 g 141f oblique achiral −0.1: 1.114/1.149/1.131/1.147 strong.
 n: static sharpening of w3 → 1.45 at M2=8 (control) — k-GLL wins at matched M2 (1.37–1.43 vs 1.19).
Lesson: check `swarm leaderboard` for identical/sibling inputs before submitting (g flagged duplicate spend i/k).
Next: wait for o/l/m resonance tests (outer-shell T1 classes). If nobody combines ALL T1-active classes on w3 (S1⊥+S2∥+outer
 resonant), propose that; otherwise act as critic/verifier, then `swarm done`.

## 2026-10-15 05:50 — wakeup 4: verifier role (kernel convergence of new leaders)

Board jumped: chiral resonant β stacked on amplitude leaders.
- w3: b `02f7` (S2∥ α=.25 + chiral β ±.08 on 7×T1 49° L/R): s21 2.380, r46 2.586; j `c89a` (02f7 + 19×T1 β ±.02): s21 2.451;
  h `0672` strong 1.427/1.461/1.440/1.461; p `fe3d` strong 1.695/1.687/1.688/conv46 1.686 (conv matches r46 → converged).
- w2: c `df59` strong 1.162/1.208/1.189/1.208; c w2-chiphase `beed` s21 1.19; e w2-stack CMA.
- static frontier (n): peaks ≈1.56 at M2≈8–10; leaders beyond it.
- T1 rule (m/o/l): picks active classes on outer shells but sign 2/4–4/6; signs flip on S1⊥ base.
Everything (w3 stacks, w2 stacks, controls) is owned. My niche now: numerics verification.
Submitted family `kernel-conv` (--diagnostic, s21): `1f4e` = 02f7 with g_cutoff 7→12, n_mesh 48→64; `94f8` = c89a g_cutoff 9→12,
 n_mesh 64. Isolates kernel-harmonic truncation from qmax (conv46 changes all three at once).
Concern to watch: qmax 8 hexagon inradius ≈6.9|G1|; |G|²=19/21 harmonics are 4.4–4.6|G1| and exp-products go higher; d_s=0.1
 interaction is still strong there. conv46 (qmax 10) for c89a/j-chistack is the test; if it drifts, post a critique.
Budget 50/500.

## 2026-10-15 06:10 — wakeup 5: kernel-conv done; finishing

`1f4e` 02f7 at g_cutoff 12/n_mesh 64: s21 2.3670 (orig 2.3801, −0.55%); `94f8` c89a at 12/64: 2.4514 (= orig at 9/48).
→ 02f7 shift is g_cutoff 7 truncation (q got 2.367 at 10/64). Posted 20261015T060941.402Z_swarm-i_result_9ce0. qmax untested (conv46 only).
Board: f/d verified leaders are M·T-invariant; o: r56<r46 in 43/45 multi-cluster gains, no sign changes; h 19@67° chiral β on 02f7 r46 2.944.
Every direction (w3 stacks, w2 stacks/phase, controls, verification) is owned by ≥2 agents (g flagged herding on w2 phase).
Decision: swarm done. 50/500 used; unused budget left to the swarm rather than duplicating.
