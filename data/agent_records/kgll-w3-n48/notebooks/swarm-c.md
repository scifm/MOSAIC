# swarm-c notebook

Started 2026-10-08T04:34:38+00:00.

## 2026-10-08 wakeup 1
- Read brief, theory, pilot 024 (doc 40), doc 46. Board empty at start.
- Key priors: doc 46 at Nk=21 on w3: S1xT1 a=+0.05 -> +1.85%, a=-0.05 -> -9.0%, b=+0.05 -> -4.4%; S3xT1 a=+0.05 -> -3.75%. Pilot 024 (LL01 seed): 4x6 +0.5% reversed to -0.9% at 5x6.
- Tools: work/gen.py (SP = spatial stars by |G|^2 in 120 basis, MO = momentum stars; make(parent, terms, g_cutoff)). g_cutoff 8, n_mesh 48.
- Posted hypothesis atlas-T1-w3 (20261008T045800.340Z_swarm-c_hypothesis_419d): 10 stars x T1, a in {-.1,-.03,.03,.1,.3}, b in {-.1,-.03,.03,.1}; 90 evals.
- Submitted batch b1 (stars 1,3,4; 27 reqs). Batches b2 (7,9,12), b3 (13,16), b4 (19,21) in work/inputs/ pending (32 in-flight cap).
- Next: collect b1, submit b2..b4, post slope table.

## 2026-10-08 wakeup 2 (05:15)
- Board exploded (36 posts). Leader: swarm-i joint ⟂ orbit S1xT1 (pairs ±G with ±R, G.R=0), alpha 0.0866 each: s21 1.1885, r46 1.1560 (fa76). Joint orbits are where the gain is; my full-star S1xT1 a=+0.1 (6492): s21 1.033, r46 1.0476 (promoted).
- Atlas S1,S3,S4: full-star beta even & negative (confirms swarm-j); alpha odd, S1/S3 + slope, turnover by 0.3; S4 (parent shell) local max. Posted interim result d7e3.
- Trimmed rest of atlas (a ±0.03, ±0.1; b +0.1) stars 7..21 = 35 evals submitted (ids in work/inputs/rest_ids.txt). Charged so far 62.
- work/collect.py tabulates my requests (cache results_cache.json).
- Next: finish atlas, post full table + coverage; then pick a less-crowded direction (ideas: critique of leaders' finite-size, or extend top joint orbit with higher-star positive directions).

## 2026-10-08 wakeup 3 (05:37)
- Atlas T1 done: outer stars all concave, beta>=0.1 FAIL for |G|^2>=7. Closed with result+coverage 20261008T053813.207Z_swarm-c_result_4399. NB: coverage count posted 53/9 but correct is 52 PASS / 10 FAIL (S4 a+.3, S19 a+.1, S21 a+.1, 7 beta) -> correct in next post.
- Frontier now: plane-w3 (af) S2T1par A=0.45 alone s21 1.5176 (M2k 5.30, R_beyondM2 0.72); joint-pair (e) c3f0 s21 1.45/r46 1.41; cplx-dress (am) 5cec s21 1.24/r46 1.54 at M2 3.81 (phase dressing). r56 not landed for anyone (even parent r56 pending).
- Swarm saturated (~45 hypotheses). w2: m (S3T1perp leader), n, ar, a, q. Phase-only chiral: w (S4xT1, S7xT1 chiral beta, r46 1.21), j, am, aa.
- Mechanism scope question open: co-moving part of gamma = k-independent LL mixing (swarm-as request).
- Plan: role -> ladder/finite-size auditor once r56 lands (s21/r46/r56 sign & rank stability, R vs M2k across families). Keep budget (62/500 used) for targeted gap-filling later.

## 2026-10-08 wakeup 4 (06:10)
- Frontier: amplitude orbit (S2T1par A~0.45 / S1T1perp) + chiral-beta dressing on S4/S7/S9/S10 x T1: am 08b5 s21 2.054 / r46 2.063 (Chern 1, PES gap ~5); swarm-t GP 0e99 s21 2.478. Phase dressing increment is beyond-M2 by construction.
- r56: ZERO results board-wide after ~95 min (even parent baselines). Posted request to human 20261008T061052.874Z_swarm-c_request_8cff.
- Posted correction note: atlas coverage = 52 PASS / 10 FAIL.
- Reserve/verifier agents already: at, x, u (ladder audit too). Frontier optimizers: t (GP), j (chidress), q (cma-w2), b (chidress-w2), af, e.
- My role now: reserve/critic; 438 evals left. Ideas not taken: none compelling yet. Revisit when r56 lands or human answers.

## 2026-10-08 wakeup 5 (06:42)
- r56 still zero board-wide; no human reply yet to my request 8cff.
- Numerics of R~2 leaders converged (l, z, ag). Leaders: e 80c7 s21 2.151/r46 2.290; j chidress peak min-over-clusters 2.03 at beta 0.015; t 0e99 ablation (as): chiral beta worth +0.6 on alpha base; core alpha ~ static-M2.
- Reserve agents now: at, x, u, w, a, r, k, c. Low marginal value in new screens. Waiting for r56 to audit / do targeted checks. Waking hourly.

## 2026-10-08 wakeup 6 (07:43)
- Many agents done (ao, v, ak, g, i, x, o, d, al, ah, w, u, k, ar, at, ag). r56 still zero.
- Frontier: swarm-ap tl-grad 4547 s21 5.20; 3a0e s21 4.388 / r46 4.390. Static M2 curve saturates ~1.67-1.73 (as, l) -> frontier ~3x its equal-M2 static.
- Critique+request 20261008T074426.931Z_swarm-c_request_3772: frontier at Sum|alpha| 2.36-2.47 of 2.5, but L2 ~0.6 (L1/L2 ~3.9 from pair chart). Boundary chart-dependent. Mailed ap, t.
- Next: await human answers (r56, boundary). Consider swarm done if nothing to verify.

## 2026-10-08 wakeup 7 (08:45) — DONE
- Board: most agents done; r56 still zero; frontier ap s21 6.66 (confirm21). No human answers to 8cff / 3772.
- Ran `swarm done` with summary (work/done.md). 62/500 charged. Loop stopped.
