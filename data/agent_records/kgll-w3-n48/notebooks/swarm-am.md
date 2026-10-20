# swarm-am notebook

Started 2026-10-08T04:37:00+00:00.

## 2026-10-08 05:20 — wakeup 1
- Read board. Leader: S1×T1 ⟂ (G⟂R, guiding-centre-locked) achiral α orbit, fa76 (swarm-i), s21 1.1885 at c=0.15 (0.0866/term).
  Z2 (half-cell) invariance rule from swarm-h: pair (G=(m,n), R=(R1,R2)) invariant iff m≡R2, n≡R1 mod 2. j: M·T rule → α linear only mirror-even, β linear only mirror-odd.
- Low-shell α saturated; high-shell invariant α taken by w and ah (they posted minutes before me — I had the same idea).
- Chose family `cplx-dress-w3`: β dressing at the ⟂ winner. hypothesis 20261008T051820.546Z_swarm-am_hypothesis_a821.
- Tools: work/orbits.py (126 C6 joint orbits, 31 invariant → work/orbits.json), work/gen.py (build blocks), work/mk_p1.py.
- Submitted phase 1: 25 evals (work/p1sub): bperp ±0.05,+0.10; 11 chiral-diff dirs ±0.10. Mailed j, w for α=0 slopes.
- Next: read results; compute odd/even parts vs fa76 baseline (1.1885); fill α=0 gaps for signal dirs; critique duty.

## 05:45 — wakeup 2
- Phase 1 results (base fa76 s21 1.1885 / r46 1.156). Table posted as a result. bperp is flat on r46, odd on s21. Chiral ×T1 (S4−, S7+, S9+, S10−) gains: s21 up to 1.348 (6790), r46 up to 1.536 (5cec). ×T2/×T3 lose or FAIL.
- swarm-k critique: r46 increments ≫ s21, at both signs → cluster-specific; wait for r56. Accepted. Kernel truncation ruled out (work/trunc.py).
- swarm-aa (xab-T1-w3) covers Z2-breaking chiral S1-S3×T1 at anchors; leaves invariant set to me.
- Frontier: S2T1∥ c=0.45 (af c310) s21 1.52 / r46 1.41.
- Phase 2 submitted (work/p2, 10 evals): β lines, combo, q45 (c310 anchor) + chiral, α=0 refs. Charged so far 35.
- Next: watch r56 of 6790/cfdc/5cec/2ea0; decide whether to go on along chiral β.

## 06:05 — wakeup 3
- BIG: c310 base (S2T1∥ c=0.45, af) + chiral β S4T1 −0.10 → 08b5 s21 2.0545 / r46 2.0633 (Chern 1, PES gap 5.2/5.5, splitting 1e-6). + S7T1 +0.10 → 846a 1.905/1.879. Wrong signs are much lower (48c3 1.133, fae3 1.285/1.044). Phase-only increment: M2k identical to c310 (5.30) → beyond-M2 relative to c310.
- At the ⟂ base: S4T1− line 0.05/0.10/0.20: s21 1.278/1.348/1.058, r46 1.302/1.496/1.579 (r46 keeps rising, s21 turns over). The S4−+S7+ combo is sub-additive (643a 1.109). α=0 refs: S4T1− 977c 1.0345/1.274; S7T1+ 9a77 1.019.
- Split agreed with swarm-j: I take c310 + ⟂ bases, single-orbit lines; j takes c3f0 + the all-four direction. z is running numconv on 08b5/846a.
- Phase 3 (work/p3, 8 evals on c310 base) submitting (swarm check is slow on the login node).
- Parent r56 is still pending → no r56 for anyone yet.
- Phase 3 submitted (8 evals). Charged ~43.

## 06:30 — wakeup 4
- Phase 3 s21 on the c310 base. S4T1− line: 0.05 1.748 / 0.10 2.054 / 0.15 2.303 / 0.20 2.413 (3b51). S7+ 0.05 1.682 / 0.15 2.104. S9+ 0.1 2.181 (7826). S10− 0.1 2.171 (a635). S4−+S7+ at 0.1: 2.268 (f760). r46 is pending for all of them.
- 48c3 (c310 + S4T1 +0.1, the wrong sign): r46 0.863. The odd response is consistent.
- Board: r56 stalled swarm-wide (c's request to the human). ae: chiral dressing is cluster-consistent at small β, and the s21/r46 split appears only at large β. j: on c3f0, s21 turns over at β≈0.016/entry while r46 keeps rising. t: the GP combo at P0×1.25 reaches s21 2.48.
- Plan: hold for phase-3 r46 values; no big search until r56 works. My S4 line at 0.20 = 0.082 per entry — beyond j's turnover; watch for the s21/r46 split.

## 06:55 — wakeup 5
- Phase 3 r46 values are in. Best: 3b51 (c310 + χS4T1 −0.20) s21 2.413 / r46 2.630, Chern 1, PES 5.2. Line still rising. Posted result c7b1 (two-orbit model table).
- Frontier elsewhere: t's GP combos s21 3.4–3.5 (M2k 6–7), ap gradient 3.3. j closed chidress-w3 (best ba1f 2.03/2.23). Many agents have moved to reserve/verifier.
- r56 still stalled for everyone.
- Phase 4 submitted (work/p4, 8 evals): 2-D map of the minimal model, c_par {0.35..0.65} × c_χS4 {−0.2..−0.3}. Charged 51.
- Next: find the 2-orbit maximum; consider adding S10(−)/S9(+) on top; wait for r56.

## 07:20 — wakeup 6
- Phase 4 map (s21/r46), c_par × χS4:
  0.35: −0.20 2.138/2.437 (1309); −0.30 1.966/2.732 (2e08)
  0.45: −0.20 2.413/2.630; −0.25 2.436/2.846 (3a76); −0.30 2.379/3.034 (bf51)
  0.55: −0.20 2.592/2.766 (8eb0); −0.30 2.706/3.219 (4f0e)
  0.65: −0.20 2.670/2.656 (4b90); −0.30 2.860/3.323 (13cb). M2k 7.28 (2.0× M2); PES 4.2–4.5.
- s21 rises with c_par; the s21/r46 split grows with |β| (the even part, per j/aa). min-over-clusters best = 13cb 2.86 (s21).
- Phase 5 (work/p5, 5 evals): c_par 0.75/0.90 × χ −0.3/−0.4, and 0.65 × −0.4. Watch the M2k ≤ 3×M2 = 10.89 bound.
- Many agents are done or in reserve. r56 still stalled. l is extending the static M2 calibration to M2 7–10 (needed for my high-c_par points).

## 07:45 — wakeup 7
- Phase 5 (s21/r46): (0.65,−0.40) 2.799/3.695 (1525); (0.75,−0.30) 2.903/3.162 (920e); (0.75,−0.40) 2.970/3.652 (1e77, M2k 8.48);
  (0.90,−0.30) 2.756/2.335 (2b3e); (0.90,−0.40) 3.024/3.101 (e626, M2k 10.44 = 2.88×M2, near the 3× edge; PES s21c N_A=3 gap 2.18).
- The 2-orbit model saturates at s21 ≈3.0. c_par is at the M2 edge. Static Δ(M2) saturates ≈1.67 (as/l) → e626 ≈1.8× its equal-M2 static.
- Frontier: ap 3a0e 4.39/4.39 (many orbits); t 4020 3.52/3.92. Many agents done/reserve.
- Phase 6 (3 evals): β extension at the edge, (0.75,−0.5), (0.9,−0.5), (0.9,−0.6). Then close the family with coverage → reserve/verifier.

## 08:12 — wakeup 8
- Phase 6: (0.75,−0.5) 2.812/3.833; (0.9,−0.5) 3.130/3.528; (0.9,−0.6) 3.196/3.562 (e8a0, best min; PES 3.2/3.0, N_A=3 2.4).
- Closed cplx-dress-w3 with a coverage post. 59 charged, 55 PASS / 4 FAIL.
- Frontier: ap 4547 5.20/5.41. r56 still stalled.
- Now reserve/verifier. Next: watch for r56; look for one useful critique (rule 11) or targeted check.

## 08:45 — wakeup 9 — DONE
- No new work for me. Most agents are done or in reserve, ~20 verifiers are waiting for r56. Ran `swarm done` with a summary. 59/500 charged.
