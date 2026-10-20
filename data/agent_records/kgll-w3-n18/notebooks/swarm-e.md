# swarm-e notebook

Started 2026-10-15T04:13:06+00:00.

## 2026-10-15 04:22 — wakeup 1: orientation, family w3-bigamp
- Read brief, progress/40, /46, kdep_envelope + validate. Board: swarm-a w3-atlas (30 separable dirs at α±0.1/β±0.05),
  swarm-b w3-joint (joint (G,R) orbits, chiral stars, small steps).
- My niche: large-amplitude end of box on w3. Question: does R_gap follow M2^(k)? Local calc (work/scan_m2.py):
  α=0.6 single direction gives M2k/M2 1.05 (S4) .. 2.8 (S7, 12-member); all admissible (S ratio ≥ 0.03);
  kernel converged (work/cut.py).
- Posted hypothesis 20261015T042124.010Z_swarm-e_hypothesis_e96a (~200 evals).
- Helpers: work/lib.py (gstar(g2), rstar(r2), build(parent, sstars, rstars, alpha, beta), diag()).
- Submitted A1 (28): α=±0.6 on all 10 spatial classes × T1, β=±0.3 on S1,S3,S4,S7 × T1. A2 (α±0.3, β±0.15) staged in work/A2, not submitted.
- Next: read A1 results, submit A2 (or skip parts), compare with swarm-a's ±0.1 atlas, plan stage B.

## 2026-10-15 04:42 — wakeup 2: A1 negative, pivot to nematic ⟂
- A1 (28): separable α=±0.6 / β=±0.3 all lose; 23/28 FAIL; best 0.667 (β S1T1 −0.3, req_31a2). No M2^(k) law.
  Posted result+coverage 20261015T044059.779Z_swarm-e_result_ce22. Dropped A2 (work/A2 unsubmitted).
- Board: matched-⟂ joint class (G ⟂ R, R_G=(n,−m) for G=(m,n)) is the big winner: swarm-j 7d04 S1⊥ α=0.2/pair
  s21 1.369 r46 1.386; swarm-b f06f robust_positive. ~7 agents on mechanism controls (herding on controls).
- swarm-o: C6 co-moving ⟂ only admixes LL6. My new family w3-perp-nematic (hyp 20261015T044146.897Z_swarm-e_hypothesis_cf36):
  nematic C2 unequal pair weights → LL2 admixture at 1st order. N1 (16) submitted from work/N1 via work/nem.py.
  Mailed swarm-j.
- Tool: work/collect.py FAMILY → markdown table of my requests with per-cluster R_gap.
- Next: read N1; if nematic curvature positive → line search / S2⊥,S3⊥ nematic; else null + coverage.

## 2026-10-15 05:05 — wakeup 3: nematic null, pivot to global S1 map on w2
- N1 nematic: all 16 below 7d04 on s21 & r46; C6 point = cusp max on s21 (loss ∝ |u|, isotropic, ~0.23/unit u),
  quadratic-ish on r46. C3 equivalence on s21 verified (6895 = b1e9 to 4 digits). Result 20261015T045948.176Z_swarm-e_result_b51b,
  abandon 20261015T045957.183Z_swarm-e_abandon_eced. Mailed j, q.
- Board state: S1 shell is the only one that gains (cyclotron factor e^{-|G|²/4}: 0.16 for S1). w3: S1⊥ (T1 d=90°) strong (7d04),
  peak α 0.2–0.3; swarm-a running 14-D CMA there. w2: oblique T1 (30/150) at α<0 gains (~1.04); c, g doing lines.
  Gain is not density (matched ρ̄ controls ≈1.001) and needs parent (uniform LL0 loses).
- New family w2-s1global (hyp 20261015T050428.333Z_swarm-e_hypothesis_89ab): 6-D achiral S1 class space
  (work/classes.py: achiral_to_c(x) with x = T1⟂,T1obl,T2∥,T2obl,T3⟂,T3obl; build_classes(parent, c)).
  Sobol n=64 seed 7 in work/S2a (design.json has x); S2a_1 (32) submitted, S2a_2 (32) pending (in-flight cap).
- Next: submit S2a_2 when slots free; fit GP (sklearn) on s21 R_gap; EI follow-ups; maybe same on w3.

## 2026-10-15 05:30 — wakeup 4: S1 global map closed; plan w2 rule-stack CMA
- Sobol S2a_1 (32) on w2: 16 FAIL; best 0.9946; surrogate: single oblique-T1 basin (opt T1obl≈−0.09), all else concave.
  Result 20261015T052235.817Z_swarm-e_result_e981. S2a_2 NOT submitted (dropped).
- Board: T1 guiding-centre rule (swarm-m/o/p): class (G,R∈T1) gains at 1st order with sign of Σ w_parent(G±G_R), G_R=(−q,p).
  w3 leaders: p xcombo 1.69 s21 (S2∥ + chiral β), h S1⊥+chiral β 1.43/1.46/1.44. w2 leaders: c df59 (S1obl + |G|²=4⟂) 1.162/1.208/1.189;
  g 88e5 oblique strong 1.11.
- swarm-p critique: my nematic 813f vs 18be mirror pair r56 1.342 vs 1.260 → cluster shape artefact (813f min > 7d04 is artefact).
- Built work/t1classes.py: classes(g2) by relative angle; rule(parent,g2); build_t1(parent, [(g2,theta,c)...], beta_terms=...).
- Mailed c, g, m proposing w2 multi-class T1-rule stacking CMA seeded at df59, after m's w2-resonance results.
- Next: read m's results + replies; post hypothesis; write CMA (work/cma.py) with state on disk.

## 2026-10-15 05:47 — wakeup 5: launched w2-stack CMA
- c and m handed me the w2 stacking optimizer. m's w2 outer slopes (per unit α, one orbit): 7@10.9 +1.29, 7@70.9 +0.80,
  7@49.1 −1.37, 13@43.9 −1.06, 16⟂ −1.94, 13@16.1 +0.41 (rule sign wrong 4/6). c's grid: ridge flat at (obl −0.10, 4⟂ +0.05..0.07); r46 rises with 4⟂.
- w3: o/l show that outer classes flip sign on a strong base. Strong claims: p fe3d 1.69 all clusters; h 0672; j 7d04; c df59 (w2) 1.162/1.208/1.189.
- Hypothesis 20261015T054556.537Z_swarm-e_hypothesis_5e49. Code: work/w2stack.py (COORDS, make(x)), work/run_cma.py STATE [noask]
  (tells the pending gen if complete, then asks+submits next). State: work/w2stack_state.json. λ=10, σ0=0.03, seed 11.
  gen 0 submitted (10). Also df59 at gc=8 baseline (w2center/).
- Each wakeup: `uv run ... python work/run_cma.py w2stack_state.json` (from work/). Stop rules: σ<0.005 or 4 gens without improvement, ≤12 gens.

## 2026-10-15 05:59 — wakeup 6
- CMA gen0: all 10 below df59 (best 1.1144 f35a); baseline a75e (df59 @gc8) s21 1.1623 = df59. Outer classes at ±0.03 cost a lot.
  gen1 submitted. m=[-0.126,0.071,-0.008,-0.035,0.01,0.002,-0.007,0.011], σ 0.0287.
- Board: w3 leader 02f7 (b): S2∥ 0.25 + resonant 7×T1 chiral β 0.08 → s21 2.38 / r46 2.59 / r56 2.53. Chiral (mirror-odd, L−R) β on
  resonant classes is the big lever. On w2, c (w2-chiphase) and p (w2-chiclass) test chiral β on df59 → if positive, add β coords to my CMA.

## 2026-10-15 06:13 — wakeup 7
- CMA gen1 best 1.1563 (9d1c) < df59 1.1623; gen2 submitted. m≈[-0.129,0.068,-0.012,-0.02,-0.005,0.011,-0.015,0.022], σ 0.026.
  Expect a null (outer amplitudes don't add, as on w3: o, l, d).
- w2 new lever: p's chiral β on |G|²=9-hitting classes 13[9,19] (8a0d s21 1.228 / r46 1.408 on df59) and 7[7,9].
  Mailed p proposing a joint α+β CMA on w2 after their W2 lines. Herding note (g): 4 w2 chiral-phase families.

## 2026-10-15 06:30 — wakeup 8: w2-stack closed, w2-chistack launched
- w2-stack (amplitude CMA) closed: 3 gens, best 1.1563 < df59 1.1623. Result 20261015T062850.671Z_swarm-e_result_3d21.
- w3: swarm-a w3-stack CMA in resonant chiral frame → cc13 s21 3.60 / r46 3.91 (a19 & b19 same sign, moved jointly).
- New: w2-chistack (hyp 20261015T062907.352Z_swarm-e_hypothesis_432e), module work/w2chiral.py (reproduces 8a0d exactly, α & β).
  run_cma.py generalized: `python run_cma.py STATE FAMILY PARENT MODULE SIGMA0 LAMBDA SEED [noask]`.
  Command: `uv run ... python run_cma.py w2chi_state.json w2-chistack w2 w2chiral 0.02 12 5` (from work/). gen0 submitted (12).
  Old w2-stack: `python run_cma.py w2stack_state.json w2-stack w2 w2stack 0.03 10 11 noask` (closed).
- p has not replied to my mail yet.

## 2026-10-15 06:45 — wakeup 9
- w2-chistack run 1 (w2chi_state.json, σ0 .02 at 8a0d): gen0 12/12 < 0.95 → discarded. p: b ≥ 0.06 FAIL; best min at b13 = .02 (8eb3:
  1.255/1.356/1.339). Restarted: w2chi2_state.json, σ0 0.008, seed 6, X0 b13 = 0.02.
  Command: `python run_cma.py w2chi2_state.json w2-chistack w2 w2chiral 0.008 12 6` (from work/).
- c's note: w2 gains cap ~+20% (only one double-resonant class on w2) vs w3 ×2–3. l: phase-only on w2 parent beats parent (13@43.9 β+0.02: 1.069/1.216).
- w3 leaders: a cc13 s21 3.60 / r46 3.91; h 4927 strong 2.44/2.94/2.90. m, g, i, d done early (they say all directions are owned).

## 2026-10-15 06:59 — wakeup 10
- w2-chistack (restart) gen0: best s21 1.3066 (a9a7) > 8eb3 1.255; 11/12 ≥ 1.19. gen1 submitted. σ 0.0084.
- w3: a 713b strong 3.97/4.80/4.56/4.80; r 5d7c 4.11/4.91. n closing: w2 static frontier 1.63/1.68 (s21/r46) — no w2 k-GLL beats it yet.

## 2026-10-15 07:13 — wakeup 11
- gen1 best 1.290 (8755, r46 1.474); all-time a9a7 s21 1.3066 / r46 1.3159 / r56 1.3237 → conv46 pending (best w2 min so far; p's c02a strong min 1.262).
  gen2 submitted. Pattern: r46 ≫ s21 (min binds on s21). p closed and handed joint α+β to me.
- w3: a b4b8 strong 4.50/5.75/5.54/5.74.

## 2026-10-15 07:30 — wakeup 12: a9a7 strong claim
- a9a7 completed ladder: s21 1.3066 / s21c 1.3066 / r46 1.3159 / r56 1.3237 / conv46 1.3182, all PASS → `strong`. Posted claim
  20261015T072650.731Z_swarm-e_claim_578c. Best w2 min (prev c02a 1.262).
- gen2 best c7a7 s21 1.314 (ladder pending). gen3 submitted. σ ~0.009.
- ρ̄ control (work/rhobar.py IN OUT NSHELLS [margin]): 8/12/16-shell projections negative (w2 touches 0) → 16 shells + uniform δ=0.0141
  (M2 2.465). Calibration: w2 parent with same δ (M2 2.458). Controls: 5a1f (ρ̄) and 0296 (parent-δ), --control on s21,r46,r56.
- NOTE: cma dirs are overwritten per gen name: cma_w2-chistack_gNN now holds the RESTART run (first run's g00 files overwritten).

## 2026-10-15 07:44 — wakeup 13
- gen3 best 1.330 (22ce); all-time improving per gen (1.307 → 1.314 → 1.330). gen4 submitted.
- ρ̄ controls: 5a1f (a9a7 ρ̄, δ-mixed) s21 0.9886 / r46 0.9898; 0296 (parent δ) 0.9878 / 0.9878 → density explains ≈ +0.1%. r56 pending.
- w3 frontier: k (bcap) cd23 5.60/6.62. q, others finishing.

## 2026-10-15 08:01 — wakeup 14
- Controls done: ρ̄(a9a7) 0.9886/0.9898/0.9897 vs parent-δ 0.9878 ×3 → beyond M2. Posted 20261015T080050.345Z_swarm-e_result_439d
  (also cites n's static M2=3.2 points ≤1.17). work/powsharp.py: ρ^p sharpening inadmissible on w2 (cusp at zeros) — not submitted.
- CMA gen4 best 1.3337 (6ef9); best mins on ladder: 22ce 1.330, ccd9 1.325, c7a7 1.314 (conv pending). gen5 submitted.
- Many agents finishing (f, h, j, q, p, c, n, m, g, i, d). Remaining idea: w2 high-M2^(k) region (n: box allows 7.5, search at ≲3).

## 2026-10-15 08:22 — wakeup 15
- gen5 best 1.3664 (b97f), 1.361 second; ladder mins: 6ef9 1.3337, 22ce 1.330, ccd9 1.325. gen6 submitted.

## 2026-10-15 08:38 — wakeup 16
- gen6 best 1.3898 (8a57). ladder mins: b97f 1.3664, 4237 1.3606 (conv pending). Still improving ~+0.02/gen → continue past 8 gens if so. gen7 submitted.

## 2026-10-15 08:54 — wakeup 17
- gen7 best 1.4149 (2c49); ladder mins 4316 1.380, b97f 1.366. Extended CMA ≤8 more gens (note posted). Stop: 2 gens w/o improvement or σ<0.005. gen8 submitted.

## 2026-10-15 09:11 — wakeup 18
- gen8 best 1.400 (no improvement over 1.4149; 1st miss). ladder mins: 988f 1.397, 3f98 1.384, 4316 1.380, 2c49 1.376. gen9 submitted.

## 2026-10-15 09:28 — wakeup 19
- gen9 best 1.4397 (89a0) — improved, counter reset. ladder mins: 988f 1.397 (full ladder strong-level), cb4a 1.392, 3f98 1.384. gen10 submitted.

## 2026-10-15 09:47 — wakeup 20
- gen10 best 1.412 (miss #1 after 89a0 1.4397). 89a0 min 1.4397 at r56+ (conv pending). gen11 submitted. work/top.sh FAMILY N = fast ladder summary.

## 2026-10-15 10:03 — wakeup 21: CMA stopped
- gen11 best 1.433: 2nd consecutive miss → w2-chistack CMA STOPPED (12 gens restart = 144 evals + 12 discarded first run).
- best: 89a0 s21 1.4397 (min), conv pending. ρ̄ control for 89a0 (δ 0.0343, M2 2.381) + parent-δ2 (M2 2.399) submitted (--control s21,r46,r56).
- Next: post final claim on 89a0 + coverage/result for w2-chistack after conv46 and controls land.
- Posted claim 89a0: 20261015T100221.643Z_swarm-e_claim_7e64. Controls b509 (ρ̄) / 8060 (parent δ2) pending.
- Idea next: expanded 15-D frame (+13@16.1 a/b, +19@66.6 a/b) seeded at final mean, σ0 .006, λ 14, ≤6 gens; or IPOP restart. Budget left ≈225.

## 2026-10-15 10:22 — wakeup 22
- 89a0 ρ̄ control b509 0.963/0.966/0.966 vs parent-δ2 8060 0.971/0.971/(r56 pending) → beyond M2. Closing result 20261015T101853.060Z_swarm-e_result_471f (coverage).
- w2-polish P1 (8): S2⊥-T2 on 89a0 (α ±0.025, ±0.05), β×1.25/1.5, all×1.1/1.2. work/polish.py.

## 2026-10-15 10:37 — wakeup 23
- w2-polish: scaling ×1.1/1.2 and β×1.25/1.5 raise s21 (1.46-1.49) but FAIL splitting/Δ>0.1 → s21 frontier bounded by manifold-splitting gate. S2⊥T2 +0.025 (0596) s21 1.495 PASS r46 1.510 (r56 pending); +0.05 FAIL; −α lowers s21 raises r46.
- New: w2-chistack2 (hyp 20261015T103548.383Z_swarm-e_hypothesis_9839), module work/w2chiral2.py (12-D, X0 = 89a0 exact + 0.025).
  Command: `python run_cma.py w2chi3_state.json w2-chistack2 w2 w2chiral2 0.006 12 7` ; gen0 submitted. ≤6 gens.

## 2026-10-15 10:55 — wakeup 24
- 0596 (89a0+S2perpT2 +0.025) strong: 1.4952/1.5102/1.4611(r56)/1.5043 → claim 20261015T105146.191Z_swarm-e_claim_c876 (r56-bound; split/Δ s21 0.087).
- CMA2 gen0 best s21 1.491. Switched objective from gen1 on: CMA_OBJ=min → min(s21,r46,r56) via cma.score_min (waits while status pending). Gens slower (~45 min).
  Command: `CMA_OBJ=min python run_cma.py w2chi3_state.json w2-chistack2 w2 w2chiral2 0.006 12 7`
- w3: a a6a0 strong 11.39/10.56/12.04/10.75 on boundary; a done.

## 2026-10-15 11:20 — wakeup 25
- CMA2 gen1 waiting on r56 (10/12). 54a4 (gen0) full ladder 1.4809/1.5802/1.5751/1.5808 → best w2 min 1.481 (claim later, at CMA end). b022 s21 1.536 r46 1.581 (r56 pending). 2 FAILs at split/Δ 0.118, 0.168.

## 2026-10-15 11:46 — wakeup 26
- CMA2 gen1 told (min objective): best b022 min 1.5135 (s21 1.536, r46 1.581, r56 ≥1.5135). 4908 1.483, 54a4 1.481. gen2 submitted.

## 2026-10-15 12:17 — wakeup 27
- gen2 waiting on 7/12 r56. b022 (1.5135) still best; b449 1.487, 19d4 1.481 so far from gen2.

## 2026-10-15 12:41 — wakeup 28
- CMA2 gen2 (min obj) best 1.487 < b022 1.5135 → miss #1. gen3 submitted.

## 2026-10-15 13:35 — wakeup 29: CMA2 stopped
- gen3 miss #2 → CMA2 stopped. b022 strong 1.5356/1.5808/1.5135/1.5828 → claim 20261015T133257.032Z_swarm-e_claim_3c0b. ρ̄ control da2b (δ 0.0389) submitted.
- Closing result w2-chistack2+polish posted with coverage. Remaining budget ≈166. Next: wait for da2b and 8060 r56, then final summary/swarm done unless a new idea.

## 2026-10-15 14:00 — wakeup 30: DONE
- b022 ρ̄ control da2b 0.9555/0.9587/0.9585 → beyond M2 (result 20261015T135923.190Z_swarm-e_result_0376).
- Posted swarm done summary (work/done.md). 334/500 charged. Loop stopped.
