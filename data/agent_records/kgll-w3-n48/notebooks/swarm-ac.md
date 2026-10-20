# swarm-ac notebook

Started 2026-10-08T04:36:19+00:00.

## 2026-10-08 05:25 — wakeup 1: scope chosen = comov-w3
- Board at start: ~15 hypotheses; atlases (c,f,g,b; a on w2), joint-pair (e), joint-orbit (i), orbit-w2 (m), hessian (d), chiral-beta (j), sobol (o), z2-invariant (h), ps/nem (k), c3break (r), minimax (l).
- s21 leaders: swarm-i fa76 1.1885 (S1 pair-orbit, 0.0866/pair), swarm-e 56da 1.105 (same, 0.05/pair).
- KEY INSIGHT (work/geom.py): those leaders pair G=(m,n) with R=(-n,m) = l_B^2 z x G, |R|/|a|=|G|/|G1|.
  cos(G.r)cos(k.R) = 1/2[cos G.(r-X_k)+cos G.(r+X_k)], X_k = LL0 guiding centre. => "comoving" envelope.
  Prediction: comoving partners S1<->T1, S2<->T2, S3<->T3 (the only in-bound ones). In swarm-h's Z2 invariant subspace.
- Posted hypothesis 20261008T052119.631Z_swarm-ac_hypothesis_272e (<=150 evals). Mailed e, i, h re de-dup.
- Generator: work/comov.py OUT --parent P A1 B1 A2 B2 A3 B3 (orbit amplitudes; per pair = A/sqrt3).
- Phase 1 submitted (19): ids in work/p1_ids.txt. S2c/S3c alpha lines (-0.15,+0.15,+0.3,+0.6), S1c alpha 0.3/0.6,
  beta-only +-0.1 (S1 also +0.2), combos C123 0.15 each, C12 0.3 each.
- M2 ratio note: S3c barely changes M2^(k) (1.013 at A=0.6); S1c 0.6 -> 1.93; S2c 0.6 -> 1.85.
- Next: read results; fit per-shell curves; phase 2 = joint (A1,A2,A3) surface + CMA-ES.
- work/survey.py / survey.json: survey of all visible requests (slow: ~2-3 s per swarm show).
- 05:35 survey result: swarm-i S2xT1 0deg orbit (non-norm-matched) s21 1.1785 / r46 1.1712 ~ as strong as comoving S1 (fa76 s21 1.1885 / r46 1.156).
  => comoving |R|=|G| not unique; selection rule likely swarm-h Z2 invariance (R ≡ (-n,m) mod 2). Posted correction note.
  r46 holds up for these directions so far (e 56da r46 1.088, i fa76 r46 1.156).

## 2026-10-08 05:50 — wakeup 2: comov-w3 closed; critique posted
- Phase 1 results: S1c A=0.3 s21 1.3618 / r46 1.3342 (f373, at r56); A=0.6 1.108/1.028. S2c, S3c all negative (S3c 0.3 FAIL at M2r 1.002!).
  All comoving beta negative & even. C123 0.15 -> 1.063 (r46 1.049). Prediction refuted (also swarm-h, swarm-ad gc-lock duplicate).
- Posted result+coverage 20261008T054512.479Z_swarm-ac_result_2ad8 (family closed). 19 evals charged.
- Board: frontier = S1T1perp/S2T1par plane (e, af, au nocomov s21 1.57, ap, s, t, o); mechanism (ab, p static controls; ao, as, aj; g offset rule
  w/ b's e^{-|R|^2/4} factor); chiral beta phase-only (w line, j dressing, am dressing, aa); w2 (m, n, ar, q, g, ah).
- My analysis (work/drift.py, work/excess.py, ED-free): k-dep r46/s21 drift falls with M2k/M2 (0.956 at 1.5-2) while static controls <=1%.
  r46 excess over swarm-ab static calibration: best pure-amp a5c2 1.23, c3f0 1.20; edge points 1.09-1.13; e a7c2 below static.
  am phase-dressed: r46 1.54 vs s21 1.11 -> cluster-specific; wait r56.
  Posted critique 20261008T054602.774Z_swarm-ac_note_85cf; mailed e, af, am.
- No new family yet: all main lines are claimed. Next: wait for r56 data (parent r56 pending), then decide (maybe verifier role,
  or robust/excess-targeted optimisation at moderate M2 if nobody does it).

## 2026-10-08 06:20 — wakeup 3: hold
- r56 still pending for everything incl. parents. No mail. Budget 19/500.
- Board: swarm-at and swarm-x switched to reserve/verifier. j chidress-w3 claims s21 1.45->2.03 with chiral-beta dressing (r56 decides).
  ae: chiral dressing cluster-consistent at beta<=0.02; split only at large chiral amplitude. p confirms my a7c2-below-static finding.
  g refuted own offset rule. ab: leaders keep 1.2-1.46x over equal-M2 static.
- Decision: no new family (saturated). Hold budget; when r56 lands, redo work/excess.py with r56 + static r56 calibration and audit
  s21/r46/r56 sign consistency of the top candidates (the robust-claim question). Offer budget for targeted checks if asked.

## 2026-10-08 07:10 — wakeup 4: hold
- r56: still zero results swarm-wide (swarm-c request 8cff to human). Budget 19/500.
- Frontier (s21/r46): j chidress c3f0+chiral beta min-over-clusters 2.03; t super-linear s21 2.478; au a61f 1.569/1.637 (M2k/M2 1.11).
  w2: b 8c39 1.299/1.343. Numerics converged (l, z, ag). Many agents now reserve/verifiers (a, u, w, x, at) -> my r56 audit is redundant.
- Plan: one or two more long waits; if r56 lands and reveals a gap nobody covers, act; otherwise swarm done.

## 2026-10-08 08:10 — wakeup 5: done
- r56 still stalled; many agents done/reserve. No uncovered direction worth my budget. Ran `swarm done` (work/done.md). Loop stopped.
