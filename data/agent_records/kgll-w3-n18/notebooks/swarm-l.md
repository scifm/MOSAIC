# swarm-l notebook

Started 2026-10-15T04:13:30+00:00.

## 2026-10-15 wakeup 1 (04:26–04:36 UTC)
- Read board: atlas (a, c=w2), joint orbits (b), bigamp (e), chiral phase (g), fsfloor (f). S1×T1 G⟂R class (b f06f) = 1.105/1.088/1.092 s21/r46/r56.
- Prepared matched-perpendicular (G⟂R, |R|=l²|G|) family (work/joint.py, scratch A/) but i and j claimed exactly it minutes earlier -> dropped (herding).
- Took role: mechanism controls (family w3-mechctrl). Facts (single-particle, work/avgdens.py):
  - BZ-avg diag density of ⟂ envelopes = w3 sharpened on its own shells; w3 min rho 0.005 -> 8-shell truncation negative for alpha>=0.1. Only f06f control admissible.
  - Order counting: gain linear in alpha (~2%/0.01) vs density O(alpha^2) -> beyond-M2 at small alpha.
- Submitted control 20261015T043517.435Z_swarm-l_req_2422 (avg-density static for f06f; s21,r46,r56).
- Posted hypothesis ..._0770, request to human ..._ec74 (control definition for large alpha). Mailed b,i,j.
- Next: read control result; await human; when ⟂ optimum settles -> MT/convergence checks + complement gradient sweep over non-⟂ joint classes (work/joint.py can build any class).

## 2026-10-15 wakeup 2 (04:52–04:57 UTC)
- My f06f control req_2422: R 1.0010 s21/r46/r56 PASS (f06f 1.09-1.11) -> posted result ..._fac5 with coverage. Left control role (8 agents now on controls).
- Board: j claims strong for S1⊥ α=0.2 (7d04: 1.369/1.386/1.306/conv 1.386). b's S2×T1 θ=0 (a90f) +10% s21, 1.092 r46. w2 gain in oblique S1T1 classes (c, g).
- work/resonance.py: guiding-centre harmonics G±G_R (G_R=(-R2,R1)). S2T1∥ (both on |G|²=4) wins but S1T2∥ (both on 4) loses -> heuristic unproven.
- New family w3-gcres (hyp ..._2d1b): 24 evals, outer shells 7,9,12,13 joint classes, resonant vs non-resonant at ±0.05. Submitted (req ids in submit output; files in scratch RES/, gen work/mk_res.py).
- work/survey.py <idfile>: dumps class content + R of visible requests (useful).
- Next: analyse odd/even parts; any odd >=3% -> stack on S1⊥ 0.2 base. Watch human answer to request ec74.

## 2026-10-15 wakeup 3 (05:18–05:21 UTC)
- gcres A (24): odd parts @0.05: (7,1,49) +5.6%, (7,1,131) +6.1% (MT partner, 0.8% floor), (13,1,16) +5.5%; (9,1,90) +0.1% (T1-rule MISS); T3/T4 & non-res ~0. 131@+0.05 -> r46 1.0335. Posted result ..._cdd6.
- Board: S2∥ (3,1,0) = 2nd linear class; r's 09f8 S2∥ 0.2: 1.45/1.41. h chiral β on S1⊥ base 1.43-1.46 (top). n: static sharpening reaches 1.45 at M2=8 (!), human asked how to state. o runs same outer T1 classes at ±0.1; p is assembler; d recentre atlas |G|²<=4 at 7d04; a CMA 14-D.
- Stage B submitted (12): achiral (7,±49) & (13,±16) sums ±0.05 on S1p(7d04) and S2par(09f8) bases + parent c=0.05,0.10. Gen: work/mk_stack.py (fixed joint.py angle tol to 0.2).
- Mailed o, p, m.
- Next: read stage B; if positive, line in c on best base and combo S1p+S2par+outer; then coverage + maybe switch to verifier.

## 2026-10-15 wakeup 4 (05:41–05:45 UTC)
- Stage B (12): outer achiral 7/13 T1 pairs on S1p/S2par bases gain only at c=-0.05 (badc 1.480/1.433, 067a 1.407/1.471), +c loses; M2^(k) drops for -c (anti-M2). Parent achiral 13@0.10 FAIL. Posted result.
- Leaders now: b 02f7 = S2∥0.25 + chiral resonant β 7×T1 ±0.08 -> 2.38/2.59 (b extending line); p fe3d 1.69 all clusters; h 0672 1.43/1.46/1.44.
- Submitted (6): 7/13 achiral ±0.05 on 02f7 base (work/mk_stack2.py, verified γ), plus -0.10 on badc/067a stacks.
- Mailed swarm-a (CMA box should allow negative c for 7/13).
- Next: read; if -c adds on 02f7, hand to CMA; consider verifier role (r56 trends for leaders; MT partner checks).

## 2026-10-15 wakeup 5 (06:04–06:06 UTC)
- Stage C on 02f7 (base 2.380/2.586): 7ach -0.05 2.314/2.621, +0.05 2.266/2.324; 13ach -0.05 1.820/2.061, +0.05 2.086/2.622 -> no gain. -0.10 stacks overshoot (01f5 0.791; 9821 1.167/1.360). o owns 02f7+outer from now.
- Leaders: a b3f2 2.88/3.08 (10-D CMA), b 8e7d 2.79/3.05. ~10 agents optimizing w3 leader -> I left.
- New family w2-phaseonly (hyp ..._ee1d): phase-only MT-even chiral pairs at w2 parent: (1,30/150),(7,10.9/169.1),(7,70.9/109.1),(13,43.9/136.1) × b ±0.02, ±0.04. 16 req d220..1944 in ls order of scratch W2PH (work/w2ph_order.txt). Gen work/mk_w2phase.py.
- NOTE: submit-batch uses python sort (+0.02,+0.04,-0.02,-0.04 per class), not ls order.
- TODO: final coverage post for w3-gcres when r56 values land (badc, 067a, 92d2, d893, e144, f747, 9821, 1334...).

## 2026-10-15 wakeup 6 (06:26–06:28 UTC)
- w2-phaseonly A: 13@43.9 +0.02 -> 1.069/r46 1.216 (d220); 7@10.9 -0.02 -> 1.038/1.171 (92d8); odd ±15-17% @0.02, even -10%; quad optimum b*≈+0.017 / -0.013. 1@30, 7@71 weak. Posted result (..._res4). c handed ownership to me.
- Submitted 10 (W2PH2, work/mk_w2ph2.py): lines 13 {.01,.015,.025}, 7 {-.01,-.015,-.025}; stacks 90e8 (13+.01,7-.01), 9c48 (+.015,-.012), 832d (+.02,-.02), 860f (+.015,-.012,1+.009).
- w3: b claim strong 02f7 2.380/2.586/2.530/2.583. a's CMA cc13 3.60/3.91.
- TODO: w3-gcres final coverage when r56 lands; w2-phaseonly stack -> if strong, matched M·T partner not needed (MT-even), coverage.

## 2026-10-15 wakeup 7 (06:48–06:50 UTC)
- w2 phase line/stack (s21/r46): L13 .010 1.059/1.123 (2900), .015 1.070/1.176 (be95), .025 1.054/1.250 (8c16); L7 -.010 1.044/1.113 (8172), -.015 1.048/1.150 (650a), -.025 1.016 (02ab); stacks 90e8 1.072/1.191, 9c48 1.067/1.230, 860f(+S1) 1.048/1.227, 832d(.02,-.02) 0.999. s21 peak ~1.07 sub-additive; r46 rises with |b|. r56 pending.
- Only 7@10.9 & 13@43.9 chiral pairs hit w2 +1/3 shell (|G|²=9) on T1.
- Submitted 4 (W2PH3): (13,7)=(.020,-.010),(.025,-.010),(.030,0),(.025,-.015).
- Next: wait r56; claims judged per-cluster thresholds (r46,r56,conv46 ≥1.05/1.10; s21 >1). Post claim if broker says so. Then coverage posts for both families.

## 2026-10-15 wakeup 8 (07:15–07:17 UTC)
- r56 queue bottleneck: no r56 since 05:00. Withdrew 18 low-priority promotions (all w3-gcres except badc; w2 2900,8172,650a,90e8,860f).
- Plane fill: 7d06 (13 .020, 7 -.010) 1.069/1.256; 80d4 (.025,-.010) 1.055/1.280; 17d0 (.030,0) 1.026/1.276; a8af (.025,-.015) 1.0185 (screen only).
- Posted w3-gcres abandon with coverage (..._d312).
- Board: w3 frontier 5.1 (Σ|β| cap binding, o asked human); w2 strong claim p c02a 1.262/1.383/1.362/1.384 (df59 amplitude + chiral β). Many agents done (d,g,i,m,n,p).
- Waiting: r56 for d220, 92d8, be95, 8c16, 9c48, 7d06, 80d4, 17d0 (w2 phase-only), badc.
- Then: w2-phaseonly result+coverage (+claim if broker gives one), then swarm done.
- 07:46 still waiting r56 (no movement). f closed w3-phasestack: phase-only pairs s21<=1.054, r46<=1.27 on w3 (similar to my w2 numbers).
- 08:28 still no r56 for my points (others' r56 landing, e.g. e a9a7). Waiting. Many agents done (h, j, c, f, q...).
- 09:10 r56 state=SUBMITTED for my points (running on cluster; 5x6 slow). Board: a's w3 headline 9a85 8.13/8.85/9.09/9.04 (box-limited); e w2-chistack s21 1.415. Most agents done. Waiting.
- 10:10 r56 still SUBMITTED; b reports same (withdrawn runs ahead?). Posted operational request naming d220/80d4/7d06/9c48. e claims w2 strong 89a0 1.440/1.538/1.553/1.532.
- 11:11 still SUBMITTED. a claims w3 a6a0 11.39/10.56/12.04/10.75 on boundary; a done. e: w2 0596 1.495/1.510/1.461/1.504.

## 2026-10-15 wakeup ~12:12 UTC — DONE
- Posted w2-phaseonly coverage (..._6f91) with r56 pending; posted swarm done summary. 75/500 charged. Loop stopped.
