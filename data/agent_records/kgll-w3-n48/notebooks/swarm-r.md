# swarm-r notebook

Started 2026-10-08T04:35:35+00:00.

## 2026-10-08 05:07 — wakeup 1: scope chosen, phase 1 submitted
- Board at start: atlases (c T1, f/g T2-T3, b all-pairs ±δ, a w2), joint orbits (e, i), 12-D Hessian (d). All C6-covariant.
- Chose family `c3break-w3`: pure E-irrep (C3-breaking) pair-star deformations. On the C6 Nk=21 cluster they have zero linear response,
  so s21 measures curvature directly. Hypothesis post 20261008T050618.153Z_swarm-r_hypothesis_5625. Budget <=120.
- Generator: work/gen_c2.py (pair stars; lines via R_G (m,n)->(-n,m-n), R_R (p,q)->(-p-q,p); asserts C3-orbit average of C = 0).
  Amplitude = Frobenius norm of pair-coef matrix C (same normalization as separable star α: separable α=0.1 ↔ ||C||=0.1).
- Phase 1: 24 req S1×T1 {sp,mo,jd0} × α ±0.15,±0.30, β ±0.10,±0.20 (ids 20261008T05065x–050709 swarm-r).
- Early board: swarm-c S1T1 star α=+0.1 → s21 R 1.033 (promoted). T2/T3 amplitude atlas strongly negative (down to 0.11).
- Next: read phase-1 results; check ±x symmetry (cubic) and curvature sign; phase 2 S3×T1, S2×T1, S1×T2.

## 2026-10-08 05:25 — wakeup 2: phase 1 done (all negative), frontier probes
- Phase 1 (24 E-irrep S1xT1): all PASS, all < 1 (best 0.9264 jd0 β+0.10). Cone linear in |x| (drop at 0.30 ≈ 2.2× drop at 0.15):
  degenerate excited multiplet split by symmetry breaking. Posted result 20261008T052511.680Z_swarm-r_result_05e6 with coverage.
- Missed earlier: swarm-k nem-w3 (8 evals) overlaps; mailed them.
- Board: big w3 frontier = Z2(half-translation)-invariant S1T1⊥ ("guiding-centre-lock/comoving") and S2T1∥ orbits.
  swarm-ad d746 (S1T1⊥ ||C||=0.3) s21 1.362; swarm-i fb45 (S2T1∥) s21 1.179 r46 1.171. Heavy herding on these (~15 agents).
- In my gen_c2 line order the ⟂ orbit is the d=j-i=2 diagonal. work/gen_front.py adds E perturbations to d746.
- Submitted 10 diagnostic probes (ids 20261008T05244x) around d746: jd2 α ±0.1/±0.2, sp/mo α ±0.1, jd2 β ±0.05.
- Next: read probes; decide on pivot (avoid herd). Candidate ideas: verifier/critic role on leaders; check rect-cluster C3 artefact.

## 2026-10-08 05:48 — wakeup 3
- d746 frontier probes (base s21 1.362, S1T1⊥ ||C||=0.3): jd2 α +0.1 1.3314 / −0.1 1.3405 / +0.2 1.2037 / −0.2 1.2520;
  sp ±0.1 1.3238/1.3222; mo ±0.1 1.3256/1.3305; jd2 β ±0.05 1.3457/1.3424. All below → C6 frontier is a local max vs C3-breaking.
  At the frontier the drop looks closer to quadratic (0.1: −2.3%, 0.2: −11.6% for jd2 +) than the parent's cone.
- Generalized work/gen_front.py (env BASE, S0, DIAG, TAG, OUT). Submitted 6 diagnostics around swarm-e c3f0
  (S2T1∥ c=0.2/pair, s21 1.4516, r46 1.4125): ids 20261008T0546xx–054702 (jdb/sp/mo α ±0.1). In my line order ∥ is diag d=0.
- swarm-k ceded E-perturbations to me (nem-w3 closed). Board leaders: au a61f s21 1.569; S2T1∥ ridge; r56 pending everywhere.
- Board concerns: s21→r46 drift grows with M2^(k) (ac); chiral β r46≫s21 (k, am). Rect clusters break C3 and are mirror-symmetric(?).
- Next: post frontier-stability result + close c3break-w3 with coverage. Then consider a verifier role for r56 outcomes.

## 2026-10-08 06:10 — wakeup 4
- c3f0 frontier probes (base s21 1.4516, S2T1∥ 0.2/pair): jdb ±0.1 1.3969/1.4196; mo ±0.1 1.4032/1.4038; sp ±0.1 1.4006/1.4107. All lower → stable.
- New w3 frontier: chiral-β dressing of S2T1∥ (j ba1f s21 2.031 r46 2.225; am 08b5 2.055/2.063; t 0e99 s21 2.478). β only 0.015/term!
- work/gen_front2.py: adds E perturbation to the S×T1 pair block of ANY request block (locates pair stars by member).
- Submitted 6 diagnostics around j ba1f (ids 20261008T0609xx): jdb/sp/mo α ±0.1 on S2×T1.
- Budget 40 charged (+6 now). Next: when chi probes land, post a closing result with coverage for c3break-w3.
  Then pick next role: perhaps verifier on chiral-dressing steepness (why +40% from β=0.015?), or reserve.

## 2026-10-08 06:30 — wakeup 5: family closed, reserve mode
- ba1f probes (base 2.0311): jdb ±0.1 2.0023/2.0033; sp 1.9690/1.9711; mo 1.9671/1.9506 → stable.
- Posted closing result 20261008T063028.517Z_swarm-r_result_583e (coverage: 46 evals, 46 PASS, best parent-anchored 0.9264).
- Posted note: reserve/verifier role, 454 evals. r56 stalled for everyone (swarm-c asked human).
- Board w3 leaders now R≈3 (t 4a76 s21 3.33 r46 3.09; ap 7a96 r46 4.07 s21 2.81). w2 leader b 8c39 1.30/1.34.
- Next: wait for r56; audit leaders for r46/r56-vs-s21 splits; respond to mail requests.

## 2026-10-08 07:01 — wakeup 6 (reserve)
- r56 still pending board-wide (parents too). No mail. Many agents in reserve/done.
- w3 leaders: ap tl-grad s21 ≈3.47 (980e). w2: q 1370 s21 1.306, b 8c39 s21 1.30 / r46 1.34.
- Board: even-part s21↔r46 splits (aq, an, v refutation); y: leaders strongly non-ideal. Nothing for me to act on. Waiting.

## 2026-10-08 07:42 — wakeup 8
- r56 still pending everywhere. ~15 agents done. w3 s21 frontier ap 4547 5.20; ap 3a0e s21 4.388 / r46 4.390 (Σ|α| 2.39 of 2.5, box edge).
- Static M2 curve saturates ~1.67 (as, l): frontier is ~3× equal-M2 static.
- Submitted 6 E diagnostics around ap 3a0e (S2T1∥ block): jdb ±0.1, sp/mo ±0.05 (±0.1 broke Σ|α|≤2.5). ids 20261008T074xxx.

## 2026-10-08 08:11 — wakeup 9: done
- 3a0e probes (base 4.3879): jdb ±0.1 4.2714/4.2826; mo ±0.05 4.3396/4.3537; sp ±0.05 4.3496/4.3659 → stable.
- Posted addendum 20261008T081021.122Z_swarm-r_result_38e7 (cumulative coverage 52/52 PASS). Ran `swarm done`. Loop stopped.
