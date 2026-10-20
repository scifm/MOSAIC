# swarm-o notebook

Started 2026-10-14T05:20:33+00:00.

## 2026-10-14 05:40 — wakeup 1: scope chosen, stage 1 submitted
- Board: a linmap (product stars), b/c joint orbits (P/A/B classes; c's S1T1 P α=-0.06 → s21 R=1.202 PASS, top of board),
  d chiphase (mirror-odd phase; note: s21 is C6 no mirror, r46/r56 C2 only), e/f/h large amplitude, i comove (P1 line scan),
  j phasequad, k outerjo (S4-S10 joint orbits). ALL C3-invariant.
- My family: `nematic` = E2 (C3-breaking) component of each joint orbit. Hypothesis 20261014T054040.044Z_swarm-o_hypothesis_b019.
  Generator work/nematic.py (orbits via C3_G(m,n)=(-n,m-n), C3_R=(-R1-R2,R1); E vec (2,-1,-1)/√6 within orbit ordered by C3).
  Note label GR<dot> in filenames is sign-ambiguous (canonical pairs); c-index is what matters. For S1T1: c2 = P (G⊥R), c0/c1 = A/B.
- Stage 1: 36 reqs (work/stage1): α=±0.2 E on 5 blocks × 3 orbits; β=±0.1 E on S1T1 orbits. On s21 (C6) linear term must vanish
  → R(+)≈R(−) is a check; mean−1 = curvature.
- Next: tabulate stage1; Stage 2 = E curvature at the symmetric optimum (swarm-i P1 line), off-diagonal K, r46/r56 orientation triplets.

## 2026-10-14 06:10 — wakeup 2
- Board exploded: incumbent ac14 (swarm-r xsector) s21 4.44 / r46 4.93 PASS = P orbits S1,S2,S3×T1 α=∓0.06 + odd β 0.02 on S2, S5.
  Product-star large steps all FAIL (e,f,h,j abandoned). Matched-density controls (a,q): R_ctl 0.999 → gain beyond ρ̄.
- Stage 1 result posted (…swarm-o_result_a894): E2 curvature negative on all S1 orbits (T1 −2..−5%, T2 −7..−13%, T3 −18..−22% at a=.2),
  phase E2 also negative; S2/S3 at a=.2 nonlinear/FAIL. Parent is local max in E2 sector.
- Stage 2 submitted: work/stage2_ac14 (19 reqs), E vec a=±0.05 on 9 S1–S3×T1 orbits on top of ac14 + C3-rotation check
  (S1T1_c2_aErot_p must equal S1T1_c2_aE_p on s21). Generator work/nematic2.py (decompose → add → emit; verified γ identical 1e-16).
  Forgot --builds-on ac14 on submit; mention in post.
- Next: tabulate stage 2 vs ac14 (4.4429 s21). If any E curvature >0 → line scan + orientation triplet on r46/r56.
  Owe a critique post (rule 11).

## 2026-10-14 06:40 — wakeup 3
- Stage 2 (E2 at ac14) done: s21 ± symmetric ≤0.08%, rotated==unrotated 1e-4 (C6 confirmed); all E curvatures negative
  (−0.2% S1 … −1.7% S3 at a=.05). r46: linear E2 artifact up to ±2.7%/0.05, orientations differ 1.3%; ±avg below ac14.
  Withdrew 12 (keep 7 on r56 as artifact calibration: 76f2,c448,f85b,3aa4,e383,3b66,6720).
- Wrote work/c3audit.py: top-30 leaderboard all exactly C3-symmetric (E-frac <1.3e-16). Posted …swarm-o_result_f203.
- Incumbent now b55a (swarm-r, 3× ac14 line): s21 10.91 / r46 11.39 PASS, split/D 0.022.
- Stage 3: 12 --diagnostic E2 probes at b55a (+a=0.05 only; S1-S3×T1 + S1×T2 orbits) in work/stage3_b55a.
  Question: does E2 soften near the gate-limited (level-crossing) regime?
- Remaining ideas: final-candidate E2 check (offered on board); otherwise consider swarm done early — the frontier is crowded.

## 2026-10-14 07:08 — wakeup 4: family closed
- Stage 3 at b55a (s21 10.912): all 12 E2 orbits −0.16..−1.05% (S3 most negative). Posted …swarm-o_result_6056 (coverage),
  abandon …swarm-o_abandon_309e. Replied to swarm-j re 5f28 sign flip (mail_a273).
- Board: b55a claimed STRONG (10.91/11.39/11.16/11.42 s21/r46/r56/conv46). Optimizers crowded (r,h,n,a e2guide); phase-only capped ~1.73 s21.
- Plan: stay as verifier — if a new leader beats b55a, run a 6–12-eval E2 diagnostic on it (nematic2.py INPUT OUT 0.05 plus).
  Otherwise swarm done. 67/500 used.

## 2026-10-14 08:00 — wakeup 5: E2 check of new leader 3bd0
- New claimed leader 3bd0 (swarm-k ell2: chiral ℓ=2 field λe^{+2iθ_GR} on S4–S10×T1, λ=.008): 13.58/13.11/13.10/13.30 PASS.
  ("E+/E−" on board = ℓ=±2 angular parts, C3-invariant — not my E2.) n's 2fb9 at 15.47 s21 climbing.
- c3audit 3bd0: E-fraction 1.7e-6 (rounding) → symmetric. Extended nematic.py with S4–S7 shells (_shell(q)); nematic2.py takes
  extra blocks "S4xT1,S5xT1". Verified decompose reproduces 3bd0 γ to 3e-16.
- Submitted 18 --diagnostic E2 probes at 3bd0, +a=0.04: S1–S3×T1 (9), S4×T1 (6 orbits, 12-member), S5×T1 (3). work/stage4_3bd0.

## 2026-10-14 08:30 — wakeup 6
- 3bd0 E2 check done: 17/18 negative (−0.06..−1.09%, S4T1 c3 most), S1T1 c1 flat (+1.6e-5). All PASS. Local max.
- New top claim 2fb9 (swarm-n): 15.47/14.59/14.27/14.70 PASS. c3audit 1e-16. Submitted 18 E2 diagnostics (work/stage5_2fb9, a=.04).
- Many agents posting final summaries. Plan: post combined 3bd0+2fb9 result, then swarm done.

## 2026-10-14 09:00 — wakeup 7
- 2fb9 E2 (a=.04): 17/18 negative (−0.13..−1.5%, S4T1 c3 / S5T1 most), S1T1 c1 flat (+1.7e-5) — same soft orbit as at 3bd0.
  S1T1 c1 curvature: parent −3.1%@.2, ac14 −0.23%@.05, b55a −0.27%@.05, 3bd0/2fb9 ≈0@.04 → softening along the chiral field.
- Submitted 4 diagnostics: S1T1 c1 at a=±0.08, ±0.15 on 2fb9 (work/stage6_2fb9_soft). Then final post + swarm done.

## 2026-10-14 09:22 — wakeup 8: done
- S1T1 c1 at 2fb9: ±0.08 → −0.33/−1.06%, ±0.15 → −1.60/−3.05% → concave (cubic makes tiny +a flat).
- Posted addendum …swarm-o_result_68b0 (3bd0 + 2fb9 E2 tables, coverage). Ran `swarm done`. 107/500 charged.
