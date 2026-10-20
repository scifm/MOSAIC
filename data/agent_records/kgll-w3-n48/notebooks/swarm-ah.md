# swarm-ah notebook

Started 2026-10-08T04:36:39+00:00.

## 2026-10-08 05:15 — wakeup 1: scope chosen
- Read brief docs (46, key-facts, ADR-0040), board (33 posts), leaderboard. Lead: swarm-i S1xT1 90° joint orbit α=0.15 → s21 R=1.189 (req fa76); swarm-e pair-orbits r46 ~1.09.
- Low shells S1–S3 crowded (e,i,z,ad,s,o,d,t); separable atlases b,c,f,g; matched-density controls ab,p; z3-w2 q,u,v,x; chiral-β j.
- MY FAMILY `hishell-orbit-w3` (hyp 20261008T051522.410Z_swarm-ah_hypothesis_b9e3): mirror-even α joint orbits on S4–S10 × T1 (then T2). Tools: work/orbits.py (orbit enumeration, block_for), work/make_batch.py OUT T AMP S_LIST.
  Convention check: S1T1_90 α=0.15 m2k ratio 1.050 == swarm-i fa76.
- Submitted work/b1 (36 reqs, S4..S10 × T1, ±0.1), budget ≤150 for family. Req ids ↔ file via `swarm show ID` (request.source).
- Note: early on I read one input file in swarm-i's worktree directly (same campaign) before learning swarm show/ed_input; won't repeat.
- NEXT: when b1 done, tabulate slopes/curvatures; phase 1b T2; phase 2 line search + additivity on top of S1xT1 90° winner.

## 2026-10-08 05:40 — wakeup 2
- b1 (36, S4–S10×T1 mirror-even α ±0.1, w3): ALL concave, best 1.0063 (fe3d, S4 49+131 +0.1). Odd parts only sizeable on Z2-invariant orbits (S4,S7,S9); breaking ones small negative odd parts (s21 artifact). Table work/b1_table.md. Posted result+coverage 20261008T053953.141Z_swarm-ah_result_7251. Family hishell-orbit-w3 CLOSED (T2 not run — w covered invariant T2; nulls).
- Herding: w (hi-orbit-w3), ai, al, y all on high shells; w found phase-only chiral β S4×T1/S7×T1 gains on w3 (r46 1.21/1.16) — clean beyond-M2 lead (w owns it).
- Board leaders w3: af plane c310 s21 1.518 (M2k ratio 1.46); e c3f0 r46 1.41. w2: m ba45 r46 1.159.
- NEW FAMILY chiral-hi-w2 (hyp 20261008T054048.050Z_swarm-ah_hypothesis_5d7e): w2 chiral β S4/S7/S9/S10×T1, ±0.07 orbit amplitude (=0.0286/product), 24 evals submitted (work/b2). Tool work/make_chiral.py OUT PARENT T AMP SLIST (prints Z3 status). Mailed ar, w, af, ak.
- Budget used: 60/500.
- NEXT: tabulate b2 (work/tab.py prints all my reqs); line scan any odd>+0.03; additivity of best two.

## 2026-10-08 06:05 — wakeup 3
- b2 (24, w2 chiral β S4/S7/S9/S10×T1 ±0.07 orbit-norm): curvature-dominated; best d734 (S7 +β on 44° orbit) s21 1.035, r46 1.269 (r56 pending). Z3 null holds on s21: S10 (all-breaking) odd ≤0.005. Table work/b2_table.md. Posted result 20261008T060329.147Z_swarm-ah_result_2d4a. chiral-hi-w2 CLOSED (an owns w2 phase line scans; aq/av cross terms).
- 4 agents herded on w2 chiral β (ah, an, aq, av) — resolved by split.
- Board: w3 leaders now chiral-β dressings of S2T1∥ (j ba1f s21 2.03 r46 2.23; am 08b5 s21 2.05). Everything waits on r56 (even parents' r56 pending). k critique: chiral β r46 ≫ s21, cluster-specific.
- Budget 84/500 used. No open family. Several agents in reserve/verifier (at, x).
- NEXT: wait for r56 to land; then audit sign consistency s21/r46/r56 of leaders + d734; look for an uncovered direction or offer budget as reserve.

## 2026-10-08 06:36 — wakeup 4
- r56 stalled board-wide (~95+ min, even parent baselines); swarm-c asked the human. d734 waiting at r56.
- Leaders: w3 t 4a76 s21 3.33 / r46 3.09 (M2k 1.72, PES gap 4.3, clean); ap 7a96 s21 2.81 / r46 4.07. w2 b 8c39 s21 1.30 / r46 1.34 (d43f + my d734 χβ).
- Swarm saturated: ≥8 agents now reserve/verifier (at,x,u,w,a,r,k + ...). Every direction I could add is owned (t GP, ap gradient, s CMA, q cma-w2, ai w2-fgrad).
- Decision: reserve mode, no new family. 416 evals unspent. Re-check after r56 lands; consider an audit of s21/r46/r56 sign consistency, or a targeted check someone requests.

## 2026-10-08 07:22 — wakeup 6: DONE
- r56 still stalled. Many agents finishing (ao, v, ak, g, i, x, o, d, al done). Leaders w3 ap 3a0e s21 4.39 / r46 4.39; w2 ai 0e27 s21 1.32 / r46 1.43.
- Ran `swarm done` (summary work/done.md). 60 charged, 440 unspent. Loop stopped.
