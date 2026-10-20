# swarm-at notebook

Started 2026-10-08T04:37:29+00:00.

## 2026-10-08 ~05:35 — wakeup 1 (orientation)
- Read brief, pilot 024 (sign flip 4x6→5x6), doc 46 (s21 precision fine; Chern not evaluable on s21).
- Board (≈75 posts, 877 reqs): leaders are Z2×Z2-invariant achiral amplitude orbits S1T1⊥ and S2T1∥ (swarm-h rule m≡R2, n≡R1 mod 2).
  s21 1.19 (orbit amp 0.15) → swarm-e a7c2 S2T1∥ per-entry 0.3: s21 1.50, but M2k/M2 = 1.63.
  swarm-ab static calibration: R_static ≈ 1+0.19(M2−3.63) at s21 → 1.43 at M2 5.9 ⇒ large-amp leaders may be mostly M2.
- Everything low-order is claimed (atlases, joint orbits, invariant subspace CMA/grad, plane maps, M2-neutral, controls, numconv, w2 z3...).
- Built work/orbits.py (pair-star block builder), work/harvest.py (public results → work/harvest.json; slow, 877 ids).
- Plan: analyst/verifier role first (board-wide finite-size transfer s21→r46→r56 and R vs M2^(k) frontier); pick an eval niche after.

## 2026-10-08 ~05:57 — wakeup 2 (role chosen)
- Board saturated: ~110 posts; every low-order sector claimed (often 2-4 agents). Frontier at s21: j chidress 2.03 (α inv + chiral β, M2k 4.57),
  af/e plane 1.5 at M2 edge. swarm-ac: r46 excess over M2-matched static peaks ~1.2 at M2k 4.1-4.6; e a7c2 below static at r46;
  chiral-β r46≫s21 (40% disagreement) → r56 decides. No request has reached r56 yet (05:45 snapshot).
- Decision: verifier/reserve role, posted `20261008T055652.376Z_swarm-at_note_cdf6`. No own family. ≤60 own evals; rest for others' checks.
- Tools: work/lbparse.py (leaderboard → rows), work/audit.py (r56/conv46 sign flips, claim thresholds). harvest.py abandoned (swarm show too slow under load).
- Next: when r56 lands, run audit, post critiques (sign flips, excess vs static at r56), mail authors. Answer any verify-mail.

## 2026-10-08 06:30 — wakeup 3
- r56 stage has produced zero results in ~95 min, including the parent baselines (swarm-c request `…c_request_8cff` to the human). So the audit can't run yet.
- swarm-x (494 evals) and swarm-u (466) also switched to verifier/reserve, so three of us now hold reserve budget. No mail for me.
- Notable: ae refutation, chiral dressing at β≤0.02 is cluster-consistent s21↔r46, and the split appears only at large β. b: the chiral dressing transfers to w2 (d43f 1.16→1.30 s21).
  l/z: numerics converged (n_mesh/g_cutoff) for large-amp and chiral leaders. ab: equal-M2 static calibration to M2 6.5 shows leaders at 1.2-1.46× over static.
- Action: none (0 evals). Next: hourly checks, audit when r56 lands; consider `swarm done` if reserve remains redundant.

## 2026-10-08 07:30 — wakeup 4: DONE
- r56 still stalled. Seven other agents are now in reserve with ≈3000 unspent evals (x,u,w,a,r,k,n), and a and u will audit r56. No mail for me.
- Ran `swarm done` (`20261008T072922.686Z_swarm-at_note_e352`). Used 0/500 evals. Loop stopped.
