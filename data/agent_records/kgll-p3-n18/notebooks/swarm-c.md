# swarm-c notebook

Started 2026-10-14T05:19:53+00:00.

## 2026-10-14 wakeup 1 (05:20–05:30 UTC)
- Read docs 40 (024 pilot: +0.51 % at 4x6 reversed to −0.92 % at 5x6), 46 (Nk=21 search≈confirm; Chern N/A on Nk=21),
  kdep_envelope.py (γ = Σ (α/2 + iβ) O_s(r) F_p(k); stars must be inversion-symmetric → only cos·cos).
- Parent w1c s21 Δ = 2.2586e-4. Budget 500 evals, 32 in flight, deadline 2026-10-16T05:21Z.
- swarm-a took `linmap` (product stars, 10 shells × T1–T3, α±0.1 / β±0.05, 120 evals).
- I took **`jointorb`** (hypothesis 20261014T052710.966Z_swarm-c_hypothesis_852d): each 6-member S×T block = 3 joint
  C3 orbits of (G pair, R pair): self-mirror P + mirror pair A,B; product = (P+A+B)/3 per entry. Symmetric dirs P and M=A+B.
- Tools: work/gen.py (orbits(), write()), work/stage1.py. Pair-stars as 2-member stars in block.
- Submitted s1a: 36 evals, S1-3×T1-3, P and M, α entry ±0.06 (map in work/s1a_map.tsv).
- Pending: s1b (12 phase files, S1 blocks β ±0.03) — submit when slots free.
- Next: collect, compare with swarm-a product map, build combined direction, line search, CMA-ES.

## 2026-10-14 wakeup 2 (05:50 UTC)
- Stage 1 results (s21): T1 P orbits are the levers: S1T1 P c=-0.06 c5b8 = 1.202/1.204/1.191/conv 1.204 → **claim strong**.
  S2T1 P +0.06 (15a8) 1.184, r46 1.386; S3T1 P -0.06 (f721) 1.368, r46 1.620. M orbits weak; S2/S3×T2/T3 mostly FAIL (manifold).
  S1T1 M +0.06 (8fe0) robust_positive 1.049/1.075/1.061.
- Board: 18 agents, heavy herding on joint orbits: swarm-b (jorbit, same S1-3×T1 classes + chiral phase),
  swarm-i (comove: S1T1 P line scan, 9de1 s21 1.88 r46 2.65), swarm-k/m outer shells ×T1, swarm-d chiral phase,
  swarm-a/l/q matched-density controls (already running for c5b8, f721). Large product α all FAIL (swarm-e, f).
- Dropped s1b phase probes (P/M phase is even by MT rule; swarm-b saw P phase 0.899 both signs).
- Posted result 20261014T055223.138Z_swarm-c_result_2030 (with coverage). Mailed swarm-i (matched P_n contradicted; I own
  S2T1P/S3T1P scans) and swarm-b (overlap).
- Submitted stage 2 (18): work/s2_map.tsv: S3T1P c=-.02..-.25, S2T1P c=+.02..+.25, combos (c1,c2,c3) signs (-,+,-).
- Next: find per-orbit optima, then 3-D refinement in (c1,c2,c3) (coordinate with swarm-i), maybe add S1T1 M(+), S1T3 P(+).

## 2026-10-14 wakeup 3 (06:13 UTC)
- Stage 2 (s21 / r46): combos ba0d (-.06,+.06,-.06) 1.739/2.454; 9afd (0,+.06,-.06) 1.711/2.219; 5407 (-.06,+.06,0) 1.461/1.700;
  6160 (-.04,+.04,-.04) 1.696/2.005. S3T1P: -.02 1.20 (3cdc), -.04 1.35 (4883), ≤-.09 FAIL (manifold). S2T1P: +.02 1.14, +.04 1.23,
  +.09/.12 FAIL, +.18 2.56 FAIL, +.25 3.95 AMBIG→s21c FAIL (other phase region).
- Board: leader ac14 (swarm-r, 5 levers) s21 4.44 / r46 4.93 / r56 4.43. trgrad (n), josobol (h), xsector (r), poolbo (p),
  comove (i) all optimize combined. rho_bar controls of c5b8/f721: R_ctl 0.999 (q, a). swarm-g: gains track Berry-curvature flattening.
  swarm-q lllsub: same deformations on uniform LLL.
- Insight: parent w1c is static-inefficient: R_staticM2 ≈ 0.12–0.14 vs ~0.7 for w3/w2 (doc 46). ac14 ≈ 0.55.
- New family `statfront` (hyp 20261014T061619.330Z_swarm-c_hypothesis_602a): static ρ_t = 1+t(ρ−1) controls, t=.25,.5,.65,.8,.9 on
  s21/r46/r56 (work/sf_map.tsv). Left the T1-P refinement to optimizers.
- conv46 = r46 to 1e-7 for c5b8 (qmax 10, n_mesh 64): LL0 Gaussian form factor → qmax converged; not an issue.

## 2026-10-14 wakeup 4 (06:37 UTC)
- statfront s21/r46 (r56 pending): t=.25 .752/.734 (fff7); .5 .724/.705 (7c23); .65 .755/.743 (5406); .8 .832/.826 (7462);
  .9 .908/.905 (8570). LLL = 0.81 on s21. → my hypothesis WRONG: w1c is the best of its ρ_t family (non-monotone, min near t=.5).
  swarm-f statctl agrees (δ-mix/power scans: R 0.83–1.06, frozen-k statics ~1).
- Added static references from doc 46: w3 (45e7), w2 (a831) as --control on s21/r46/r56 → compare absolute Δ of ac14.
- ac14 (swarm-r): s21 4.443 / s21c 4.443 / r46 4.935 / r56 4.426 / conv46 4.934, PES EG ~3.5–4 (static ~13). It = my ba0d T1-P
  combo + 2 β-odd levers (S2T1 X, S5T1 X at 0.0204).
- Other: swarm-k ell2: ∇_γ lnR ∝ e^{2iθ_GR} across all orbits (unified ℓ=2 field). swarm-a qgeom: P1 = Berry flattening, ac14 not.
- swarm-i: S3T1-P minus line beyond −0.06 all FAIL (f17d, bbff, da5b, 9a90) — cite those.
- Next: post statfront result w/ coverage when r56 + w3/w2 land. Consider a critique post. Budget 71/500.

## 2026-10-14 wakeup 5 (06:59 UTC)
- Static refs: w3 (45e7) s21 2.024 / r46 1.818; w2 (a831) 1.429 / 1.284 (vs w1c). w3 s21 Δ = 4.571e-4 matches doc 46 exactly.
  → w1c is a weak static band in absolute terms; best known static (w3) has ~2x its gap. r56 pending.
- Leaders now: b55a (swarm-r) strong 10.91/11.39/11.16/11.42, R_beyondM2 1.38–1.62 (beats M2 law), PES EG ~3.5; trgrad ~10.98 s21.
  b55a / w3 ≈ 5.4 (s21), 6.3 (r46). swarm-q ρ_t×deformation: gain needs density contrast; leaders beat whole ρ_t family.
- Next: post statfront result (ρ_t + w3/w2) with coverage once r56 lands; frame "R vs best static ref" and R_beyondM2>1.

## 2026-10-14 wakeup 6 (07:20 UTC)
- Posted statfront result 20261014T072030.046Z_swarm-c_result_b13c (r56 pending; hypothesis refuted; w3 is 2.0x/1.8x w1c;
  leaders vs w3: b55a 5.4/6.3, ac14 2.2/2.7, c5b8 0.59/0.66).
- swarm-a pairspec: e2 (2nd 2-particle eigenvalue, 4x6) predicts R (R² 0.97 r46). Mailed swarm-a asking them to test e2 on my
  7 static controls (out-of-sample: ρ_t dip, w3).
- Board saturated: optimizers (n, h, r, a e2guide, b orthant), mechanism (a, f, g, q xparent on w3/w2), finite-size (j), controls (l).
- Holding budget (75/500 used). Next: r56 note for statfront; look for an uncovered niche or critique; else wind down.

## 2026-10-14 wakeup 7 (07:52 UTC)
- Posted jointorb closing result 20261014T075249.630Z_swarm-c_result_744a (coverage, 54 evals). 15a8 full ladder 1.18/1.39/1.31/1.39.
- swarm-a ran e2 on my static controls (note 0662): ordering transfers; overpredicts when e1 collapses (w3 pred 1.98 vs 1.82).
- Leaders now ~12–15 s21 (chiral ℓ=2 E+ field; n, r, h, k). Boundary Σ|α| representation question raised to human by k, h.
- Plan: wait for r56 of statfront controls, post short r56 note, then `swarm done` (space saturated; ~425 evals unused deliberately).

## 2026-10-14 wakeup 8 (08:24 UTC) — DONE
- r56 backlog (>2 h) for my controls and stage-2 points; values will land in store.
- Leaders converged to one chiral ℓ=2 E+ field (~13, swarm-k claim 3bd0); many agents done. Posted `swarm done` (75/500 used).
