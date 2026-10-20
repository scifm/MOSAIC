# swarm-i notebook

Started 2026-10-08T04:35:00+00:00.

## 2026-10-08 05:05 — wakeup 1: scope chosen, phase 1 submitted
- Read docs 40, 46, theory §6.4, brief. Board: only swarm-c (separable atlas, all 10 stars x T1, w3).
- Chosen family **joint-orbit-w3** (hypothesis 20261008T050123.512Z_swarm-i_hypothesis_7755):
  each 6x6 (S,T) separable term splits into 3 joint C6 orbits (achiral 90° or 0°, chiral pair 30/150 or 60/120).
  separable(α) = Σ orbits(α/√3) (verified numerically, work/check_sum.py). Orbit fns normalized to unit mean square.
- Tools: work/geom.py (orbits), work/gen_joint.py (inputs: "name=S,T,angle,alpha,beta;..."; S,T are |G|²,|R|² values).
- Phase 1: 48 requests in work/phase1 (6 pairs x 8), submitted 05:03, ids 20261008T0503*_swarm-i_req_*.
- Note: Nk=21 cluster is chiral → chiral-orbit B≠C split may be artifact; 4x6/5x6 not C3.
- Next: when results land, tabulate R per orbit, compare with swarm-c separable; build combined positive direction.

## 2026-10-08 05:30 — wakeup 2: phase 1 landed
- All 48 PASS. Leaders: fa76 (S1T1⟂ A=0.15) s21 1.1885/r46 1.156; fb45 (S2T1∥ A=0.15) s21 1.1785/r46 1.171 → r56 pending (auto).
  A=0.05: b6a4 1.0597 (r46 1.050), ed9c 1.0567 (r46 1.051). Everything else concave; chiral twins agree ≤0.3% on s21.
- Response is a cone (A<0 loses ~2x faster) — swarm-h half-translation (Z2xZ2) rule explains which orbits are linear:
  invariant iff m≡R2, n≡R1 (mod 2). Only invariant orbits can have linear response.
- Posted result+coverage: 20261008T052609.409Z_swarm-i_result_410c.
- Board is crowded on the u1/u2 plane: swarm-e (plane 0.05-0.2 per-entry), swarm-af (A grid to M2 boundary), swarm-ad (GC lock, S1T1⟂ A=0.3 → s21 1.36),
  swarm-ap (frontier gradient over 31 invariant orbits), swarm-s (robust CMA), swarm-t (GP). Controls: ab, p, ao, as.
- Decision: do not duplicate; wait for plane/r56 data, then look for the gap (likely: which 3rd invariant direction, r56 transfer).
- Budget: 48/500 charged.

## 2026-10-08 05:55 — wakeup 3: holding for r56
- r56 has not landed for any request yet (not even the parents' r56 refs). This is the decisive test.
- Board: e plane ridge c⟂+c∥≈0.2 per-entry, best r46 1.41; ad S1T1⟂ A=0.3 s21 1.362/r46 1.334.
  Chiral phase-only β on S4/S7/S9/S10×T1 (M·T-even, Z2-invariant) gains linearly (w, j, am); r46≫s21 (k critique).
  j's dressing of u2 (per-entry 0.2) + chiral β 0.015 on S4,S7,S9,S10 → s21 2.03 (ba1f).
  Controls (p, ab): static M2 law explains much of the large-M2 S2T1∥ gains; beyond-M2 excess ~1.2.
- Considered an M·T twin test of s21 chirality bias for chiral β. It is useless: a χβ config is itself M·T-invariant,
  so s21's chirality cannot bias it (it maps to itself on the mirror cluster). Twin splits only probe non-symmetric halves.
- Coverage: every first-order direction I could add is now taken (ap = full invariant M·T-even gradient; s = CMA; t = GP).
  Decision: no new submissions until r56 data show where the frontier holds.

## 2026-10-08 06:25 — wakeup 4: r56 stalled swarm-wide; reserve mode
- r56 has produced no result for anyone after ~95 min, parents included (swarm-c request 20261008T061052.874Z to the human).
- w3 s21 leaders are now 2.8–3.3 (t: 4a76 3.33; ap: 2848 2.92). They combine S2T1∥ with chiral-β T1 dressing and negative high-shell α.
  All are unconfirmed beyond s21/s21c. swarm-j: s21 and r46 agree at small β; they split at large β.
- Mechanism (ao): both of my leaders' slopes come from w3's S3 (|G|²=4) harmonic; setting S3 to 0 kills about 90 %.
- Several agents (at, x, u, w) are now in reserve. I join them. No submissions until r56 works;
  then check whether fa76/fb45 hold, and critique the top s21 leaders as they reach r46/r56.

## 2026-10-08 07:08 — wakeup 5: done
- r56 still stalled for everyone. The frontier and its verification are covered by many agents, and >12 agents hold reserve budget.
- Ran `swarm done` (summary in work/done.md). 48/500 charged. Leaders fa76/fb45 stay on the ladder (r56/conv46 run automatically).
