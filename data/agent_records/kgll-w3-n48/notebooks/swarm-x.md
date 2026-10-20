# swarm-x notebook

Started 2026-10-08T04:35:59+00:00.

## 2026-10-08 05:12 — wakeup 1: scope chosen
- Board: ~15 hypotheses, heavy coverage of w3 (atlases c/f/g/b, Hessian d, joint pairs e, joint orbits i, chiral β j, Sobol o, z2 h, ps/nem k, c3break r). w2: swarm-a atlas, swarm-m orbit-w2.
- Found: w2 harmonics on m+n≡0 mod 3 sublattice → exact Z3 partner symmetry τ=(1/3,1/3) frac ↔ δ=(2/3,1/3) frac (work/z3_check.py, 1e-15).
  s21 mesh k=j(5,1)/21 contains δ → exact on w2 screen; r46/r56 not closed.
- Selection rule (work/z3_rule.py): on-sublattice stars (|G|²=3,9,12,21)×T1/T3 and off-sublattice×T2 have zero linear response; on-sub×T2 fully invariant; off-sub×T1/T3 half.
- Posted hypothesis 20261008T051105.531Z_swarm-x_hypothesis_5fc3 (family z3-w2, ≤150). Mailed a, m.
- Submitted phase 0 (6): w2 S|G|²=3×T1 α±0.03 (d11d, cdd4), β±0.03 (8954, 0f51), S3×T2 α±0.03 control (6dfa, ebd7).
- Builder: work/build.py (make(parent, terms, out); star_G(q), star_R(q)).
- Next: check phase 0 (R+ vs R−), wait for a's atlas & m's orbits, then w2 optimizer in allowed subspace.
- Possible secondary role: matched-density static control (request to human) for amplitude winners; c's 6492 r46=1.0476.

## 2026-10-08 05:33 — wakeup 2
- Phase 0 done: rule verified (S3×T1 α ±0.03: 0.9978/0.9975; β: 0.9966/0.9966; S3×T2 α: 1.0010/1.0011). Posted result 20261008T053304.197Z_swarm-x_result_b8fc with coverage; ceded z3-w2 (q, v, u also posted it; q closed invariant sector; n does w2-opt).
- Board state: w3 leaders s21 1.3–1.52 in S1T1⊥/S2T1∥ plane at large amplitude, M2(k) 4.3–6.7; r46 pending. ab's static calibration R_static ≈ 1+0.19(M2−3.63) at s21 → most of the s21 gain may be M2. Controls: ab, p, as, ao. w2 leader m ba45 (S3×T1 ⊥) s21 1.062 r46 1.159.
- Swarm is saturated (~45 agents). No new family yet; holding budget (6/500 used). Next: read r46/r56 for leaders + control results, look for an uncovered gap or a critique target.

## 2026-10-08 06:00 — wakeup 3
- w3 leaders hold on r46 (au a61f 1.637, s 9519 1.485, e c3f0 1.41); r56 pending for all. p: static M2 law explains most of high-M2 S2T1∥ gains; excess over M2-matched static ~1.2. j: chiral-β dressing s21 1.45→2.03 (r56 decides; k critique on cluster chirality).
- Swarm saturated; posted reserve/verifier note (w2 audits first). No submissions.
- Next: when r56 lands, audit w2 leaders (m ba45, ar 4413) for Z3-breaking content vs r46/r56 drift; respond to mail requests.

## 2026-10-08 06:23 — wakeup 4
- r56 stalled for everyone (~95 min, incl. parent baselines); swarm-c request 8cff to human.
- v posted the w2 Z3 audit (w2 leaders 50% breaking; s21→r46 jumps = expected first-order artifact) — agrees with my rule; no need to duplicate.
- Leaders: chiral-β dressing on w3 (j c3f0+χ: min-over-clusters 2.03 at β=0.015; t 0e99 s21 2.478), w2 b chidress d43f 1.299 s21. Numerics converged (l). p: R/R_static(M2k) well-defined beyond-M2 reading.
- Reserve agents now: at, u, w, x. No mail. No submissions. Holding.

## 2026-10-08 07:05 — wakeup 6: done
- Swarm winding down; r56 still stalled; ~10 reserve agents. v withdrew w2 odd-artifact claim (aq/an: excess is even).
- Ran `swarm done` with summary (work/done.md). 6/500 evals used. Loop stopped.
