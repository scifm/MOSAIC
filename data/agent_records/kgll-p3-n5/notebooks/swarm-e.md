# swarm-e notebook

Started 2026-10-14T05:16:59+00:00.

## 2026-10-14 05:30 — wakeup 1: scope chosen, map batch 1 submitted
- Board: swarm-a = `amp-map` (α, 30 full-star products, ±0.15), swarm-b = `phase-map` (β, 30 full-star products ±0.15, then S1–S3×T1–T3 joint orbits, CMA). c, d silent.
- Parent w1c Δ: s21 2.2586e-4, r46 2.4101e-4.
- **Key physics (mine):** M·T (mirror × TR) is a symmetry of LL0 in field; with C6v w1c it maps α→α, β→−β on mirror-even directions. So the TL gradient lives in {α mirror-even} ⊕ {β mirror-odd}. Verified the solver S00(k) has C6v about k=0 (no origin shift). Clusters: s21 is C6 but chiral (no mirror), r46/r56 are C2 only → a linear β term in mirror-even directions is a cluster-chirality artifact (`work/clustersym.py`).
- Family `chiral-phase` (hyp 20261014T052924.402Z_swarm-e_hypothesis_9601): 30 mirror-odd β directions. O{1,3,4,9,12,16}T{1,3,4} = joint orbit P − mirror partner MP (3×3 β over ±G/±R pair stars); H{7,13,19,21}T{1,3,4} = chiral halves A − MA × full T. rms Im γ = 0.06 per step. Builder `work/build.py`, geometry `work/geom.py`, parity check `work/symcheck.py` (all odd to 1e-16, C6 to 1e-16).
- Submitted batch 1 (30 reqs: O1,O3,O4,O9,O12 × T1,T3,T4 ±) at 05:29. Batch 2 (O16 + all H, 30 files) in `work/map06_b2`, to submit when in-flight frees.
- Posted note 20261014T053023.302Z_swarm-e_note_d5cb (critique of mirror-even β maps). Mailed swarm-a and swarm-b.
- Next: when batch 1 lands → compute slope s = (R₊ − R₋)/2 and curvature per direction; submit batch 2; then line search on the top slopes.

## 2026-10-14 05:50 — wakeup 2: big signal
- Map batch 1 (O1,O3,O4,O9,O12 × T1,T3,T4 ±, rms 0.06) results (my table: `work/table.py`):
  T1 "−" side gains: O1T1− 1.28 (r46 1.28, r56 1.26), O3T1− s21 1.62/r46 1.79/r56 1.67/conv46 1.79 (STRONG, ff86), O4T1− 1.69/1.99/1.83 (5f81), O9T1− 1.52/r46 2.42 (3d9d), O12T1− 1.22 FAIL(split .22). "+" sides collapse (0.03–0.72). Mostly linear: slope ~0.3–0.7 per 0.06 rad, symmetric part ≈ 0.
  T3/T4: mostly losses; outer shells (≥9 with T3/T4, 12) destroy manifold. O1T4+ 1.05 (r46 1.07).
- swarm-d holds the same family (12-member halves); I dropped my H batch → split: d = halves, me = joint-orbit-odd O dirs. Mailed d.
- Submitted O16 map (6) + line search ls1 (18): rms 0.12/0.2/0.3 on O1T1−, O1T4+, O3T1−, O4T1−; O9T1− 0.12/0.2; O12T1− 0.03; combos C134 (0.06, 0.12 each), C34 (0.10 each). Builder `work/build.py combine()`; `work/build_ls1.py`.
- Posted result 36a6, claim eb7b (O3T1− strong). Charged so far: 54.
- Next: read ls1 → find optimum along T1 odd direction; then CMA/local in span {O1,O3,O4,O9,(O12,O16)}×T1 odd + maybe T1 with T3/T4 small; mail swarm-a new leader.

## 2026-10-14 06:10 — wakeup 3: line search ls1 in
- ls1 (s21; r46/r56 where promoted): O1T1− smooth: rms .06/.12/.20/.30 → s21 1.28/1.54/1.71/1.69, r46 1.28/1.60/2.05/2.48, r56 1.26/–/1.88/–. PES eg falls 6.6→2.9.
  O3T1−: .12 → 1.665 (r46 2.51); .20 → 0.60 F (manifold); .30 → 1.95 F. O4T1−: .12 1.44 F (sp .17); .20 0.68 F; .30 3.63 AMBIG (PES eg .31, s21c FAIL) = likely another phase. O9T1−: .12 0.94 F; .20 5.96 AMBIG (eg .1) suspicious. O12T1− .03 → 1.54 P, r46 1.82.
  Combos C134 .06/.12 FAIL (splitting .2/.14), C34 .10 FAIL → effects not additive; the manifold breaks.
  O1T4+ dies past .06. O16 map: all FAIL (T1 ±: .75/.62 F).
- Best min-over-clusters: O1T1−0.20 (92e8) 1.71/2.05/1.88 (conv pending); O4T1−.06 (5f81) 1.69/1.99/1.83/conv 1.99; O9T1−.06 (3d9d) 1.52/2.42/2.28/conv 2.42.
- Board: a = amp-x-chiral (α around 5f81), c = orbit-amp (α orbits) + geometry check (claim not gauge; Ω_min moves first order), b & d BOTH doing 12-shell odd orbits → mailed both to dedupe.
- Submitted ls2 (16): finer 1-D on O1/O3/O4/O9/O12 T1−, O1T1− to 0.5, small 2-D combos around O1T1−.2; ls2b: O1T1−, O3T1− at 0.03 (linearity check requested by c).
- Charged: 54 + 18. Next: assemble R(x) curves; local optimizer (Nelder–Mead or CMA) in T1-odd span {O1,O3,O4,O9,O12} with PASS constraint, target max min-over-clusters, using r46 as free confirm.

## 2026-10-14 06:32 — wakeup 4: ls2 in, CMA launched
- Linear at small step: O1T1− R−1 = .141 (0.03), .281 (0.06); O3T1− .357, .624. s21 CEILING ≈ 1.72–1.735 for every direction/combination; r46 up to 2.51, r56 ≈ 0.93×r46. Past the ceiling the s21 manifold breaks.
- AMBIGUOUS high-R points (285c 3.63, 0b5f 5.96) have PES eg 0.1–0.3 and fail s21c → other phase; discounted.
- Best min-over-clusters: 29d3 (O1T1− .25, s21 1.735, r46 2.27, r56 pending), 92e8 (1.711/2.047/1.882/conv 2.047), 1c74 (1.693/2.484/2.307/2.484). All strong, phase-only.
- Board: a closed amp-map (null), now α around 5f81 → told to use 92e8. c: orbit-amp has α orbit slopes (S4T1-SM− 1.37). b: 12-shell odd orbits gain on T1 (J7 1.63), doing 6×12 cross combos. d: ceiling-break (T3/T4 β-odd around 92e8) + Nk=27 request 2225.
- Launched CMA-ES `work/cma_t1.py` (own minimal implementation, seed 20261014, λ=10, μ=5, σ0=.04, mean (.15,.03,.02,.01,.01) over O1,O3,O4,O9,O12 T1−; box [−.1,.5]; fitness s21 R if PASS, .5R if AMBIG, .5·min(R,1) if FAIL; 4 gens). Gen 0 submitted (10). Run `python work/cma_t1.py step` each wakeup.
- Posted result 499d. Charged ≈ 100.

## 2026-10-14 06:56 — wakeup 5: CMA fitness bug fixed; α+β leaders
- CMA gen0 told with 0.5R for AMBIGUOUS → top = 17fd (5.59 A, eg .29, s21c FAIL) = other phase. BUG. Fixed fitness (AMBIG = FAIL), re-told gen0 from scratch (gen0 zs == xs, all in box). Backup `work/cma/state_gen1_badfitness.json`. New mean (.126,−.007,.017,−.002,−.006), σ .038. Gen1 (10, ids 858a…7858) was drawn from the biased mean → told as injected samples.
  Gen0 PASS points: b248 1.663 (r46 1.977), 0837 1.363, afe3 1.284.
- Board: α-SM (self-mirror orbit amplitude) on top of my β-odd breaks the s21 ceiling: a/2fc4 4.60/5.32 (s21/r46), a/b4d4 2.58/3.05/2.72/conv 3.05 (strong), c/87e3 2.92/3.18. Genuine Laughlin by gates (PES eg ≈ 4, N_A=3 PASS). Need matched-density controls (α ≠ 0); M2(k) ≈ 9.97–10.04.
- Phase-only frontier: d/c821 (T3/T4 β-odd on 92e8) 1.90/2.10/1.81/2.10 strong; mine 92e8/29d3 ≈ 1.71–1.735.
- b: s21 ceiling = 4th level (E4−E1)/Δp saturates 1.80.
- Posted critique note 4002; mailed a for controls.

## 2026-10-14 07:18 — wakeup 6
- CMA gen1 told: best PASS 1.625 (58c2). New mean (.169,.024,.047,−.020,.007), σ .036. Gen2 submitted (3c5e…e8eb).
- c: α-orbit matched controls ≈ 0.998 → beyond M2; c now runs joint-cma (α-orbit ⊕ β-odd, 12-D) from 2fc4. a: controls for 2fc4 (74b6) / b4d4 (61bd) submitted. d: phase-only T3 β-odd lifts the s21 plateau (c821 min 1.812).
- Mailed d: propose a 10-D phase-only CMA over {O1,O3,O4,O9,O12}×{T1,T3} odd, seeded at c821, after my T1 CMA closes.

## 2026-10-14 07:43 — wakeup 7
- T1 CMA gen2 told: best PASS 1.590; mean (.148,.016,.029,−.033,−.003), σ .032. Gen3 (last) submitted. T1 span saturated (best CMA 1.663 < line search 1.735).
- Board: c joint-cma (α-orbit ⊕ β-odd from 2fc4) → 429f R 10.78 s21 / 10.47 r46, PASS incl N_A=3, but cliff-adjacent; d now does basin-width robustness on 429f; b lead12 gradient at 429f; a: controls R≈0.995 → α+β leaders beyond M2.
- d handed me phase-only CMA. d: T3 directions are cliff-bounded and non-additive.
- Launched `work/cma_po.py` (8-D offsets on c821: O1/3/4/9 T1, O1/3/4 T3, S7T3 dir; σ0 .02, λ 8, 3 gens, seed 20261015). Base reproduction verified. Gen0 ids 3b34…954f. Hyp 6d29 posted.

## 2026-10-14 08:07 — wakeup 8
- T1 CMA closed: best PASS b248 1.663; gens 1.663/1.625/1.590/1.642. Posted coverage result 0a1b (112 evals, P/A/F 50/7/55).
- Phase-only CMA (c821) gen0: best cee9 s21 1.969 (> c821 1.899), offsets O1T3 .015, O3T3 .014, O4T3 −.016. Gen1 (8) submitted (18ed…17ab).
- Leader now c/3b76 12.71/12.33/12.14/conv 12.33 STRONG (α+β, Σ|α| 2.04, adm ratio .069); control on file only for 429f (f21d 0.989) → mailed c to control 3b76 itself. d robustness: 429f basin finite (±5% → R within −4.3…+3.2 %).

## 2026-10-14 08:30 — wakeup 9
- Phase-only CMA gen1: best f13c s21 2.116 PASS (offsets O1T1 −.008, O4T1 −.011, O9T1 .022, O1T3 .006, O3T3 −.008, O4T3 −.011, S7T3 .02). Gen2 (final) submitted (43b8…5fc4).
- Board: leaders now ~15–16 at s21 (b abf0 15.77/14.61; a 0da0 15.86/r46 13.52); a critique: s21-selected optimizers overfit s21 (spread 15–20%); a asks human to widen Σ|α| ≤ 2.5 (binding). d: factorial of 3b76: α alone FAIL, β alone 4.47 AMBIG (PES .23) → synergy; d laddering f40c.
- Posted note 5339: my 4 phase-only AMBIG points (285c, 0b5f, 17fd, ef86) all FAIL N_A=3 at s21c → phase-only high-R is not Laughlin; predicted f40c will fail s21c too.
- Next: close phase-only CMA → coverage post. Then consider: finite-size/other-cluster checks of phase-only leaders, or done.

## 2026-10-14 08:55 — wakeup 10
- Phase-only CMA (c821) closed: 24 evals, 18 P / 6 F. Best f13c s21 2.116 / r46 2.459 (r56 pending); 5fc4 2.055/2.467; cee9 1.969/2.260. Coverage post pending r56.
- d confirmed my prediction: phase-only R≈4.5 point FAILs N_A=3 (ec52).
- Leaders: c 0bd5 17.17/16.42/15.90/conv 16.35 (Σ|α| 2.45 boundary), 763d; b abf0 15.77/14.61/14.66/conv 14.65.
- NEW (0 evals): all leaders exactly M·T-invariant (`work/mt_image.py`, controls 0.017/0.012 detect non-invariance) → no chirality bias in any leader's numbers.
- NEW family mt-odd-hessian (hyp fe6a): 2nd-order curvature along 9 M·T-odd directions at abf0 (bF/bSM/aO × S1,S3,S4 × T1), rms .03 ±, --diagnostic, 18 evals. `work/build_mtodd.py`, inputs `work/mtodd/`. Image(base+t)=base−t verified.

## 2026-10-14 09:25 — wakeup 11
- mt-odd-hessian results (18 diag at abf0, R0 15.7680): all 9 curvatures NEGATIVE (−0.01…−0.30 % at rms .03) → abf0 local max in M·T-odd dirs. Antisymmetric (chirality) part 0.07–0.63 %, always m>p, larger than curvature → one-sided M·T-odd steps fake +0.35 % on s21. Posted result 222d (coverage incl.). Mailed c re entry-space CMA chirality trap.
- c: matched-density controls for all α leaders R = 0.982–0.9995 (bacb) → beyond M2 established. d: min-es on abf0 = plateau.
- 29d3 complete: 1.735/2.272/2.099/conv 2.272 → phase-only T1 best min 1.735.
- Phase-only CMA r56 still queued (f13c 2.116/2.459, 5fc4 2.055/2.467, cee9 1.969/2.260). Post phase-only CMA coverage when r56 lands.
- Charged ≈172/500. After that: verifier role (M·T invariance + conv checks on new leaders) or done.

## 2026-10-14 09:57 — wakeup 12
- All other agents have closed their families (a, b, c, d wrap-up; waiting on human re Σ|α| widening 091f). Best by min: c/0bd5 17.17/16.42/15.90/conv 16.35 STRONG, control 0.995/0.992.
- b critique 8c94: ladder clusters are now the selection set; gains <3 % between leaders unresolved.
- My phase-only CMA r56 promotions are SUBMITTED (5×6 compute queue). Waiting; then coverage post + swarm done.

## 2026-10-14 10:28 — wakeup 13: DONE
- Posted phase-only CMA coverage e5ae (f13c 2.116/2.459, r56 queued in 5×6). Posted swarm done summary. 172/500 charged. Loop stopped.
