# swarm-ar notebook

Started 2026-10-08T04:37:22+00:00.

## 2026-10-08 05:25 — wakeup 1: scope chosen
- Board state: w3 leaders are S1T1⟂ orbit (swarm-i fa76 s21 1.189, r46 1.156) and S2T1∥ (fb45, r46 1.171). swarm-e/b/f found that all other
  w3 pair/orbit directions are concave. w3 low shells are crowded (~15 agents). w2: a (atlas), m (orbits on 8 blocks), n (6-D α), z3 ×4.
- My family: `orbit-w2-ext` (hypothesis 20261008T052201.767Z_swarm-ar_hypothesis_6098). w2 joint orbits nobody covers: ×T3, S4×T1-3, S5/S6×T2.
  Mirror-even combos (θ=∠R−∠G mod 180 grouping), unit mean square, α ±0.1. Tools: work/orbits.py, work/gen.py (OUTDIR parent Si:Tj:label:kind:amp).
- Submitted phase 1: 46 reqs (work/p1). Mailed swarm-m.
- Next: read results; slope = odd part, cone = even part. Phase 2: hi-shells S7-S10,S8 (scoped) + chiral β (odd combos). Phase 3: line scans/combos.

## 2026-10-08 05:55 — wakeup 2: phase 1 landed
- 46/46 PASS. ×T2/×T3 all negative cones (even −5…−34%). **S4×T1 has 3-D linear response**: odd per 0.1 = (+0.138 @10.9°, −0.093 @49.1°, +0.059 @70.9°).
  4413 (S4T1 10.9° +0.1): s21 1.0608, r46 1.1170. Posted result 20261008T055224.217Z_swarm-ar_result_1cf8.
- swarm-m: w2 leader S3T1⟂ (ba45, s21 1.062, r46 1.159); w3 leaders don't transfer to w2.
- Submitted p2 (32, ids in work/p2_ids.txt): S4T1 gradient ĝ3 a=.05-.2; 10.9° at .15,.2; 4-D G4=S3T1⟂⊕S4T1 grad a=.1-.25; S7/S8/S9/S10×T1 ±0.1.
- Dropped chiral β on T1 (ah/an/aq/av do it). swarm-a opened hiorb-w2 (S7–S10×T1) overlapping my p2 — mailed to dedupe.
- Tools: work/genmulti.py NAME amp 'Si:Tj:label:kind:weight,...' ; work/collect.py summarises all my reqs.
- Next: line results; fit vertex along G4; push best up ladder; consider S4T1 + S1T1 (m's 830d/c421) combos; chiral β ×T2/T3 low priority.

## 2026-10-08 06:23 — wakeup 3: phase 2 landed
- S4T1 ĝ3 line s21: .041/.057/.045/.997 at a=.05/.1/.15/.2; 10.9° alone 1.061/1.054/1.022 at .1/.15/.2. G4 (S3⟂⊕S4) s21 1.071 @.1 (r46 1.204), 1.053 @.15 (r46 1.257). Sub-additive.
- Hi shells ×T1 on w2: slopes on S7 (43.9 −, 76.1 −), S8 (90 −, 30 −), S9 (53.4 +, 66.6 +); S10 none (Z3). Only a74a (S8T1 90° −0.1) at 1.010.
- Board: w2 frontier is m's d43f (S3⟂×S1T1 me, s21 1.161); b's chidress-w2 1.299 with chiral β; q runs cma-w2, ai w2-fgrad. r56 stalled for all (swarm-c request).
- Posted result 20261008T062241.909Z_swarm-ar_result_1216; mailed q, ai the slopes.
- Submitted p3 (76, work/p3_ids.txt): coverage α ±0.05 S7-S10×T2/T3, chiral β ±0.03 all ×T2/×T3 blocks. After it: close family with coverage block; then switch to verifier/reserve or a gap.

## 2026-10-08 06:57 — wakeup 4: family closed
- p3 coverage (76): all <1 (best 0.987); hi×T2/T3 α |odd|≤.012; chiral β ×T2/T3 |odd|≤.012 except S4T3 10.9 (+.027). 154/154 PASS total.
- Posted abandon+coverage 20261008T065545.749Z_swarm-ar_abandon_3a50 (+ id-correction note). Best: 5302 (G4 a=.1) s21 1.0715, r46 1.2045, r56 stalled.
- Now reserve/verifier, 346 evals unspent. Many agents are already reserve (a,k,n,r,u,w,x,at,j). Plan: watch r56 for 5302/acea/4413/e3ef, answer mail; swarm done if nothing useful by ~2 more wakeups.

## 2026-10-08 07:38 — wakeup 5: done
- Swarm winding down (many agents done/reserve; w3 frontier ap 3a0e s21 4.39). r56 still stalled; my 8 promoted leads await it (automatic).
- Ran `swarm done` with summary (work/done.md). Loop stopped.
