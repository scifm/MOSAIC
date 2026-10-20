# swarm-aa notebook

Started 2026-10-08T04:36:12+00:00.

## 2026-10-08 ~05:20 UTC — wakeup 1: orientation, family choice
- Read: brief, docs/progress/40 (024 pilot: +0.51% at 4x6 flipped to -0.92% at 5x6), 46 (s21 search≈confirm, Chern n/a on s21), kdep_envelope.py
  (gamma = sum (alpha/2 + i beta) O_s(r) F_p(k); stars = any inversion-symmetric set, so pair stars {±G},{±R} allowed).
- Tools written: work/pull.py (leaderboard -> swarm show -> cached table with deformation summary), work/orbits.py
  (joint C6 orbits of pair products in solver 120° basis; block()/write_input()).
- Board state at ~05:15: the hot channel is T1 joint orbits: S1T1 90° (G⊥R) and S2T1 0° (G∥R). i's fa76 (S1T1-90, 0.0866/entry):
  s21 1.1885, r46 1.156; fb45 (S2T1-0, 0.0866): s21 1.1785, r46 1.171. Response ~linear for c>0 (slope ~2/unit), steeper drop for c<0.
  T2 orbits, T3 separable, S3 (w3's own shell) T1 orbits: all negative so far. All β at α=0 negative (0.93-0.99).
- Herding: T3 joint orbits (z), gc-lock S1T1/S2T2/S3T3 (ad), S4-S10 orbits (w, ah), CMA (s), GP (t), z3-w2 (q,u,v,x), m2 controls (p, ab).
  My first plan (T3 + S4-S6 orbits, inputs in work/unused_p1/) was claimed by others before I posted -> dropped.
- Chosen: family xab-T1-w3 (hypothesis 20261008T051948.790Z_swarm-aa_hypothesis_32ae): alpha_sym x beta_chiral bilinear term
  (allowed by j's M·T rule) at anchors A=S1T1-90 α=.0866, B=S2T1-0 α=.0866. 18 probes submitted (work/x1/).
  Mailed j, s, i.
- Next: read results; odd part [R(+)-R(-)]/2 vs achiral control; if a chiral β slope > control, line search + ladder sign check.

## 05:40 wakeup 2
- xab phase 1 (18 evals, all PASS s21). A=S1T1⊥ .0866 (1.1885), B=S2T1∥ .0866 (1.1785). Chiral β odd parts ≤1%, below the achiral (M·T-odd)
  control's odd part (1.5-2.3%) => no resolved α·β_chiral bilinear at s21. Even parts negative (−2.6..−4.6%) EXCEPT S3T1 chiral β: +1.3% (A), +0.9% (B), both signs.
- Frontier now S2T1∥ α=0.26/entry (af c310: s21 1.5176, M2k 5.30); ab calibration R_static ≈ 1+0.19(M2−3.63) → much is M2.
- am (cplx-dress-w3) overlaps at S1T1⊥ anchor (Z2-invariant chiral β); mailed my numbers; I keep S3T1 (Z2-breaking) + S2T1∥ frontier.
- Phase 2 submitted (14, work/x2): B with β_c3 ±.06,+.10; orbit decomposition (S3T1 30° only, 150° only, 90° ±); F=S2T1∥ .26 base + β_c3 ±.03,±.06; A β_c3 ±.06.
- Watch: ladder r46/r56 of A_c3_bp/bm (b7b8, 6b16) vs A_base 65f1 — Z2-breaking effects are cluster-dependent (ae note).

## 06:00 wakeup 3
- Phase 2 results: S3T1 β bump is small and turns over (B ±.06 → 1.119/1.101; +.10 → 0.82); at the 0.26 frontier increments ≤ +0.4%.
  r46: S3T1 chiral β +3.2..3.5% both signs (s21 +1%); achiral control odd part on r46 = 0.0 (M·T check passes at finite α).
- Withdrew 24 near-duplicate requests (r56 queue is the swarm bottleneck; even the parents' r56 is still pending). Kept 65f1, dfbc, b7b8, 6b16, a018, 0afa.
- Posted result+coverage: 20261008T055930.208Z_swarm-aa_result_c298. Family xab-T1-w3 closed (32 evals).
- Board: frontier now chiral-β dressing of S2T1∥ (j chidress, am cplx-dress): s21 up to 2.05; k critique: chiral increments r46≫s21, r56 decides.
  p/ab: high-M2 S2T1∥ gains mostly static-M2; beyond-M2 excess ~1.2.
- Next role idea: once r56 lands, meta-analysis of s21→r46→r56 transfer by content class (Z2-inv α, chiral β, Z2-breaking) — ED-free, for the final report.
  Building cache: work/cache_all.txt (pull.py over the full leaderboard).

## 06:35 wakeup 4
- r56 stalled board-wide (0 results incl. parents, ~95+ min); c posted request 8cff to human. conv46 is behind r56, so qmax-10 checks also blocked.
- Frontier: t 4a76 s21 3.33 / r46 3.09 (M2k/M2 1.72, adm ratio 0.61), ap 2848/7a96 s21 2.92/2.81, r46 3.72/4.07:
  invariant T1 α (S1⊥, S2∥) + negative high-shell T1 α + chiral β on |G|²=7,13,19,21 × T1. s21↔r46 diverge as β grows (k, ae, j already posted this).
- Many agents now reserve/verifier (x, u, w, at). Nothing unclaimed + decidable before r56 → holding budget (32/500 used).
- Next: when r56 lands, audit transfer s21→r46→r56 by content class (α-invariant vs chiral-β vs Z2-breaking) and check my 6 kept requests.

## 07:20 wakeup 5
- r56 still stalled. Frontier ap 3a0e s21 4.39/r46 4.39. Many agents done/reserve.
- Posted note on S3T1 β even part flipping sign s21 vs r46 (β .06 at B: s21 −5..−7%, r46 +5..+7%; at A: r46 +10%).
- Plan: wait for r56 (long ticks), report my kept requests (65f1, dfbc, b7b8, 6b16, a018, 0afa), then `swarm done`.

## 08:20 wakeup 6 — DONE
- r56 still stalled >3 h; most agents done. Posted `swarm done` (32/500 evals). Kept requests 65f1, dfbc, b7b8, 6b16, a018, 0afa await r56 in the store.
