# swarm-w notebook

Started 2026-10-08T04:35:55+00:00.

## 2026-10-08 05:16 — wakeup 1: scope chosen = hi-orbit-w3
- Board: w3 low shells (S1-S3 x T1-T3) are crowded (e,i,h,s,z,ad,d,l,o,t); w2-Z3 crowded (q,u,v,x,m,n);
  mechanism controls taken by p, ab. Leaders at s21: swarm-i S1xT1 perp orbit c=0.087 -> 1.1885 (s21c 1.1886);
  S2xT1 parallel c=0.087 -> 1.1785; swarm-e c=0.05 versions -> r46 1.088 / 1.092.
- Block format: gamma = sum (a/2 + i b) O_s(r) F_p(k) with inversion-pair "stars" allowed; only cos x cos.
- Verified symmetries numerically (work/z3check.py, work/z2check.py on single-particle S00):
  w3: tau=(1/2,0)<->delta=(0,1/2), tau=(0,1/2)<->delta=(1/2,0); invariant product iff m≡R2, n≡R1 mod 2.
  w2: tau=(1/3,1/3)<->delta=(2/3,1/3); monomial invariant iff (m+n)+(R2-R1)≡0 mod 3 (SUM condition).
- Posted critique (note e7d9) that z3-w2 agents' rule (separate conditions) is too strict; mailed u,q,v,x,m.
- Hypothesis 84ac: hi-orbit-w3, invariant joint orbits of S4-S10 (work/hiorb.py, gen_hi1.py).
  Submitted 40 (work/hi1): 16 achiral alpha ±0.05 per product, 4 chiral beta ±0.03 (S4,S7 x T1,T2).
- Discarded w2 phase-1 batch (work/p1) — herding on w2.
- Next: read hi1 results; compute slope (R+ - R-)/2 and even part; line-scan strongest; additivity on leader.

## 05:35 — wakeup 2
- Phase 1 results (work/mytab.py prints my table): all achiral S4-S10 alpha orbits concave (s21 0.47-1.00).
  KEY: chiral PHASE-ONLY beta on T1: S4xT1 chi +0.03 -> s21 1.0532, r46 1.2108 (8ffd); S7xT1 chi +0.03 -> 1.0351, r46 1.1634 (c7e6).
  Minus sign 0.87/0.91. T2 chiral beta purely even (~0.83/0.88). Beyond-M2 automatically (alpha=0).
- Posted result 5a35; mailed am (slopes) and al (overlap).
- Submitted phase 2 (work/hi2, 11): S4 chi b .06/.09/.12, S7 chi .06/.09, S4+S7 .03/.06, S9/S10 T1 chi ±.03.
- Board leaders now s21 ~1.5 (af plane-w3, e) — large amplitude S1T1perp/S2T1par.
- Next: r56 of 8ffd/c7e6; line-scan optimum; then combine best chi-beta with T1 chi of S9/S10 and maybe
  low-star chiral beta; target a phase-only robust_positive.

## 05:52 — wakeup 3
- hi2 results (s21): S4chi .06 .948, .09 .716, .12 .440; S7chi .06 .945, .09 .734; S4+S7 .03 .966 (sub-additive, cross term ~-136 in b4*b7),
  .06 .483; S9chi +.03 .994/-.03 .824; S10chi +.03 .939/-.03 .748. Optimum narrow ~b=.03, R~1.05 at s21.
- swarm-k critique: chiral beta at r46 raises the gap at BOTH signs (on the am-dressed points); r56 decides. Parent r56 still pending.
- Many agents copying the chi-beta line to w2 (ah, an, aq, av); u screens the other 5 TL-linear chiral directions (T2/T3); j has S9/S10 at ±.02.
- Submitted hi3 (7): S4 .02/.04; S4+.03 with S7 -.03/-.015, S4+S7 +.015 each; S4+.03 with S9 +.02 and S10 +.02.
- Next: r56 of 8ffd/c7e6 is the decisive test. If it holds, aim the best s21 phase-only point at the ladder (promotion is automatic at s21>=1.02).

## 06:20 — wakeup 4
- hi3: S4 .02 1.0504 (r46 1.1456), .04 1.0367 (r46 1.2700); mixes S4+S7(.015 each) 1.0487 (r46 1.184), S4+/S7-.015 1.0482, S4+/S7-.03 1.0201,
  S4+S9 .9734, S4+S10 .9119. Phase-only peak s21 1.0532 (8ffd). r46-s21 drift grows with beta (curvature artifact per ae/k).
- r56 rung has produced nothing for anyone (c's request 8cff). Leaders now are amplitude + chiral-beta dressing (s21 2.0-2.5, j/t/am/ap).
- Posted result 6fee with coverage (58 evals). Switched to reserve/verifier (note). Budget 58/500.
- Next: watch r56 for 8ffd/e0e9/47e4; respond to verification requests; consider new family only if the ladder moves.

## 06:52 — wakeup 5 (reserve)
- r56 still stalled for everyone. ao measured: 8ffd mirror (-beta) 0.8725; on uniform LL0 zero odd part; w3 with S3 removed -> odd part reverses (-0.08).
  So the phase-only gain also needs the parent's S3 = 2*S1 harmonic (as for the amplitude leaders).
- Many agents now in reserve (a,j,k,n,r,u,x,ad,at). Frontier: chiral-dressed amplitude leaders, s21 ~2.0-2.5, r46 higher.
- No action; waiting for r56.

## 07:25 — wakeup 6: DONE
- Frontier w3 ~4.4 (ap 3a0e, Sigma|alpha| 2.39 near 2.5 boundary, M2k/M2 1.74). r56 still stalled.
- Nothing unique left for me; ~10 agents already in reserve. Ran `swarm done` with summary (work/done.md). Loop stopped.
