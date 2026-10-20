# swarm-m notebook

Started 2026-10-08T04:35:15+00:00.

## 2026-10-08 05:10 — wakeup 1: scope chosen, orbit-w2 phase 1 submitted
- Read brief, docs 40/46, notes §7.5 (ideality defect = Var_r ∂₊γ, grows with |R|²), board.
  Board: w3 single-term atlases x3 (b, c, f/g), joint orbits on w3 (e, i), 12-D Hessian (d), chiral-beta (j),
  global sobol (o), z2 half-translation (h), parent-shaped/nematic (k). w2: only swarm-a's atlas.
- Hot lead: swarm-e S1xT1 G⊥R orbit on w3, s21 R=1.105 (req 20261008T050007.471Z_swarm-e_req_56da).
  Separable S1xT1 α=+0.1 (c) 1.033 at s21, promoted to r46.
- MY FAMILY: `orbit-w2` (hyp 20261008T050634.350Z_swarm-m_hypothesis_b68d). Joint (G,R) orbits on w2.
  Tools: work/orbits.py (build_orbit(template, [(s,p,d,a,b)]), amplitude a -> a/sqrt3 per pair entry, unit mean square;
  separable = sum_d (α/√3) orbit_d, verified 1e-16, work/test_orbits.py). d index: pairs sorted by Cartesian angle
  in [0,180); S1T1 d0=30°, d1=90° (G⊥R), d2=150°. work/build.py for separable stars. work/collect.py = results table.
- Phase 1: 48 evals (8 blocks S1T1,S1T2,S2T1,S2T2,S3T1,S3T2,S5T1,S6T1 x 3 orbits x a=±0.1), inputs work/p1/.
- Posted request 20261008T050747.076Z_swarm-m_request_6833: block only spans cos⊗cos; C2-allowed sin⊗sin
  (k-dependent pattern displacement) unrepresentable — asked human if in scope.
- Posted note 20261008T050920.156Z_swarm-m_note_586f: mesh moments of F_T: T3 aliased 2nd order on r46 (<F²>=4/3),
  T2 aliased 3rd order on s21 (<F³>=2.04 vs 0.816). work/alias.py.
- Mailed swarm-e: I keep w2, they keep w3; asked their per-entry amplitude.
- Next: read phase-1 table; compare Σ_d slope_d/√3 against swarm-a's separable w2 slopes; phase 2 (β on best orbits,
  line scans to |a|=0.4, combos).

## 2026-10-08 05:30 — wakeup 2: phase 1 landed, phase 2 submitted
- Phase 1 (48, s21 all PASS) — result post 20261008T052855.561Z_swarm-m_result_4997. Leaders:
  S3T1 d1 (G⟂R) a=+0.1 req ...ba45: s21 1.0617, r46 1.1587, r56 pending. a=−0.1: 0.748 (strongly odd).
  S1T1 d0/d2 (30/150°) a=−0.1 (830d, c421): s21 1.038/1.042, r46 1.051/1.050, r56 pending.
  w3 leaders (S1T1⟂, S2T1∥) are negative/even on w2. Z3 rule holds for linear term; S5T1 odd −0.02 equal on
  all 3 orbits = allowed cubic.
- Caveat (swarm-ae note): symmetry-breaking content costs less on r46 than s21 → r46>s21 not robustness. For w2,
  s21 contains K (Z3 exact), r46/r56 do not. The Z3-invariant half of a half-invariant orbit, cos(G·r+k·R),
  needs the sin⊗sin sector (not representable).
- Mails: q,u,x,w (Z3 rule), e (per-entry c=0.05 → my a=0.087; keep w2/w3 split), as (sin⊗sin = co-moving =
  k-independent LL mixing via D_G(η)), ar (orbit-w2-ext: T3, S4, S5/S6×T2 blocks — not mine).
- Phase 2 submitted (15, work/p2): S3T1⟂ line a∈{.03,.06,.08,.13,.16,.2,.3}; β±0.03 at a=.1; S1T1 (d0+d2)/√2
  line a∈{−.1,−.14,−.2,−.28}; combos S3⟂+0.1 with S1 d0,d2 at −0.1/−0.05.
- Next: r56 of ba45/830d/c421; fit S3T1⟂ line; consider S3T1⟂ + S1 pair optimum; cross-parent check (S3T1⟂ on w3
  — w3 has Z2: S3 is on w3's sublattice? (2,0) even → S3T1 on w3 per e's result was negative).

## 2026-10-08 05:52 — wakeup 3: phase 2 landed, plane map submitted
- S1T1 mirror-even (d0+d2)/√2 line a=−.10/−.14/−.20/−.28: s21 1.070/1.090/1.108/1.110; r46 1.073/1.099/1.131/1.149
  (816b at −0.28; M2k/M2 1.04; PES gap 4.9). Plateau ~−0.25.
- S3T1⟂ line: 0.03 1.025, 0.06 1.047, 0.08 1.057, 0.10 1.062, 0.13 1.062, 0.16 1.054, 0.20 1.029 (0.30 not yet seen).
  r46 at 0.03/0.06: 1.045/1.095. β±0.03 at a=.1 → both 1.053 (even, −0.9%).
- Combos: S3⟂ .1 + S1 d0,d2 −.05 (8211) 1.100; + −.1 each (ff48, = mirror-even −0.141) 1.1296 (sub-additive vs 1.152).
- r56 pending for all: parent w2 r56 itself still pending.
- Mailed swarm-ai: they take w2 frontier gradient (26 off-plane dirs) centred at ff48; I keep plane S3T1⟂ × S1T1-me.
- swarm-v critique: my leaders are 50% Z3-breaking; r46>s21 may be artifact → r56 is the test.
- Phase 3 submitted (9, work/p3): plane grid a3∈{.06,.1,.14}×a1∈{−.2,−.28}, a1 alone −.36,−.45, (0.1,−0.36).
- TODO: matched-density control for w2 amplitude winners (ask swarm-ab/p or request); coverage post at end.

## 2026-10-08 06:15 — wakeup 4: plane done, M2 controls submitted
- Plane (s21): best d43f (a3 .14, a1 −.28) 1.1606, 59b3 (.10,−.28) 1.1596, 0d2e (.10,−.20) 1.149, f33c 1.148.
  a1=−.36: 1.088, −.45: 1.034 (turns over). S3⟂ line r46 keeps rising (1.22 @ .20) while s21 turns at .12 → Z3 split.
- Result post 20261008T061350.906Z_swarm-m_result_ae0a.
- Controls (swarm-p's B: static (1−t)ρ*+tρ*²/M2*, work/ctlB.py, n_shells 19, 61 coefs) at M2 2.816/2.743/2.607/2.526:
  reqs ...4aea / 97ed / 0bcd / 0f13, clusters s21,r46,r56, --control.
- w2 now covered by q (cma-w2 from d43f), ai (frontier gradient at ff48), ar (S3⟂⊕S4), b (chiral-β dressing). Mailed all.
- Looked at swarm-t 0e99 (s21 2.478, r46 2.49, M2k 4.67, PES 5.6, split/gap 7e-4): clean on gates; concern =
  qmax 8/g_cutoff 8 truncation for high-shell+large-amplitude envelopes (parent conv46==r46 to 7 digits since parent
  harmonics ≤4|G1|) — conv46 stage tests it; r56 stuck (swarm-c request 8cff). No critique posted yet.
- Next: r56 + controls → final orbit-w2 result with coverage block; then decide new role (verifier?).

## 2026-10-08 06:41 — wakeup 5: controls landed
- Control B (s21/r46): M2 2.816 → 1.0737/1.0753 (4aea); 2.743 → 1.0575/1.0583 (97ed); 2.607 → 1.0259/1.0260 (0bcd);
  2.526 → 1.0064/1.0064 (0f13). E_s21: d43f 1.081, 59b3 1.097, ff48 1.101, 816b 1.082, ba45 1.055. Post ...a662.
- r46 now: d43f 1.2026, 59b3 1.2002. r56 still pending everywhere (parents too).
- Others on w2: b chidress-w2 closed (d43f + S7χ44° t≈1: s21 1.299/r46 1.343, 8c39); ai w2-fgrad at ff48; q cma-w2.
- Many agents switched to reserve/verifier. My family only waits for r56 → then final coverage post.

## 2026-10-08 07:13 — wakeup 6: orbit-w2 closed
- aq/an/v showed w2 s21→r46 split is EVEN (curvature), not first-order Z3; v withdrew. Corrected in close post.
- Closed orbit-w2 with coverage: 20261008T071244.814Z_swarm-m_result_b0c7 (+ addendum note: a3=0.30 → s21 0.896, 1f54).
- Frontier on w2 moved to others: b 8c39 (s21 1.299/r46 1.343), ai step from 8c39 s21 1.325.
- r56 still stalled everywhere. Plan: reserve mode, slow loop (~1 h) to report r56 for my leaders; then swarm done.

## 2026-10-08 08:16 — done
- r56 still stalled. Posted swarm done (work/done.md). 72 search + 4 controls. Loop stopped.
