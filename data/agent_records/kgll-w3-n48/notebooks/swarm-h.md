# swarm-h notebook

Started 2026-10-08T04:34:56+00:00.

## 2026-10-08 wakeup 1 (~05:00 UTC)
- Board at start: maps claimed by b (full 30x{a,b}), c (T1 atlas), f (T2/T3 atlas), a (w2 atlas), e (joint (G,R) pair orbits).
- KEY INSIGHT (my family `z2-w3`): w3 harmonics all on 2Z^2 -> density period a/2 -> magnetic half-translation
  tau in {a1/2,a2/2,(a1+a2)/2} maps gamma(k,r) -> gamma(k-delta, r-tau), delta = b2/2, b1/2, (b1+b2)/2.
  Pair term O_{±G}F_{±R} sign: (-1)^(m tau1 + n tau2) * (-1)^(R1 d1 + R2 d2). Verified S00 to 9e-16 (work/z2check.py).
  => 4x6 mesh invariant (partners exact), 5x6 only b2/2, Nk=21 none (twist).
  => TL gradient lies in invariant subspace: pair (G=(m,n), R=(R1,R2)) with m≡R2, n≡R1 mod 2.
     even stars (|G|²=4,12,16) invariant only with T3; odd stars x T1/T2 one matched pair per class; odd x T3 / even x T1,T2 purely breaking.
  - S1xT1 invariant coupling = G ⟂ R (swarm-e d=1).
- Code: work/gen.py (separable inputs), work/z2lib.py (pairs, invariant_orbits, partner, build, separable).
  File naming uses |G|² and |R|²: D_g{G2}t{R2}o{orbit}_{a|b}{p|m}.
- Posted hypothesis 20261008T050359.286Z_swarm-h_hypothesis_e706; request to human 20261008T050602.397Z_swarm-h_request_28a4
  (2 control r46 evals: separable a[S1,T1]=0.05 and its a1/2 partner). Mailed swarm-e re chiral direction.
- Submitted phase 1: 36 reqs (work/p1): 9 invariant C6-sym dirs x {a ±0.05, b ±0.03} per pair.
- NEXT: collect slopes/curvatures; compare with atlas separable values (breaking part = separable - invariant share);
  line search along best invariant directions; partner twist checks for others' R>=1.02 candidates.
- Note: pair-level representation inflates Σ|α| (separable 0.05 -> 0.15 pair-level). Watch the 2.5 cap.

## wakeup 2 (~05:22)
- Phase 1 results (s21, c per pair α±0.05/β±0.03): S1T1⊥ 1.1050/0.8329 (=e's 56da, promoted r46 1.0879);
  S2T1∥ 1.0995/0.8387 (r46 1.0919); S4(|G|²=7)T1 o0 α+ 1.0258 (r46 1.0336!), α− .9046, β− 1.0071, β+ .9113.
  S1T2, S2T2(=S2c), S3T3 x3 orbits: all negative at both signs (cone). β on achiral invariant: negative both ways.
- Board: 48 agents; ~10 crowd the S1T1⊥×S2T1∥ plane. My symmetry idea adopted widely (z3-w2 for w2 by q,u,v,x; hi-orbit w; ap tl-grad).
  Leader: swarm-i fb45 (S2T1∥ orbit amp 0.15 = c 0.0866) s21 1.1785, r46 1.1712; r56 pending.
- Posted critique of comov-w3 (ac): S2c/S3c not S1c-like. Mailed ac, e.
- Submitted p2 partner-identity test (no control needed, rides promotion): Z_id 017d, Z_t1 935e (tau=a1/2, δ=b2/2),
  Z_t12 be8d, Z_t2 bffb. = S1T1⊥ c0.05 + separable α[S3,T1]=0.04. Predict r46 all equal; r56 id==t1; s21 differ.
- NEXT: read p2 results; o1 (S4T1 mirror twin) results; pick a non-crowded niche (maybe chiral β in invariant sector
  for clean beyond-M2, or S4T1 o0/o1 combination with leader). Act as critic.

## wakeup 3 (~05:45)
- PARTNER IDENTITY CONFIRMED: r46 Δ all four = 4.78711e-4 (rel 2.3e-7); s21 id 5.04727e-4 vs partners 5.04036e-4 (3 partners equal,
  C6 of s21). Posted result 20261008T054557.642Z_swarm-h_result_f346 (with coverage block). Withdrew control request there.
  r56 still pending: predict 935e == 017d.
- S4T1 (|G|²=7) mirror twins: o0 α+ 1.0258 / β− 1.0071; o1 α+ 1.0176 / β+ 1.0076 -> β odd part flips between mirror twins (M·T rule ok).
- Frontier (s21): au nocomov a61f 1.569; s robust-cma 9519 1.474; af/e plane ~1.41-1.45 (r46 1.41). r56 backlog.
- work/decomp.py: invariant vs breaking norms of any req (reads ed_input path from swarm show). All top-10 leaders are
  purely invariant -> twist-partner service moot; swarm adopted selection rule.
- NEXT: wait for r56 of leaders. If they reverse -> finite-size work; else mechanism/maximization. Conserve budget (40/500 used).

## wakeup 4 (~06:13)
- r56 stalled ~95 min (c posted request to human). Many agents switched to reserve/verifier (at, x, u).
- Posted phase-1 result + coverage: 20261008T061343.924Z_swarm-h_result_8530.
- Board frontier: chiral-β dressing of S2T1∥ leader (j: s21 1.45->2.03 at β=0.015; t: 2.478 s21). z/ae/k checking numerics/cluster consistency.
  p/ab: static M2 law explains much of high-M2 gains; beyond-M2 excess ~1.2.
- Decision: hold budget (40/500) until r56 lands; candidates for my next work: r56 check of partner test (935e==017d),
  critique of chiral-β dressing slopes if r56 disagrees.

## wakeup 5 (~06:45): r56 still stalled; no mail. Board: chiral-β dressing leaders s21~2.0-2.15, r46 up to 2.29-2.63; numerics converged (l, z, ag).
  Many agents in reserve. Holding budget (40/500).

## wakeup 6 (~07:16): r56 still stalled (>2h). Several agents already 'done'. My families closed; only pending item is r56 check of partner test. Will wait up to ~1h more then swarm done.

## wakeup 7 (~08:17): r56 still stalled >3h. Ran swarm done (summary work/done.md). Loop stopped.
