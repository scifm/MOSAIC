# swarm-d notebook

Started 2026-10-14T05:19:56+00:00.

## 2026-10-14 wakeup 1 (05:25–05:36 UTC)
- Board at start: swarm-a `linmap` (product stars, alpha +-0.1 / beta +-0.05). While I prepared a joint-orbit
  family, swarm-b (`jorbit`) and swarm-c (`jointorb`) claimed joint orbits; e/f/h claimed large amplitude.
  Dropped my joint-orbit plan (work/phase1/ inputs NOT submitted).
- **Finding (verified, work/verify_mt.py):** antiunitary MT (mirror x TR) maps kernel exactly:
  mirror-even directions (alpha,beta)->(alpha,-beta); mirror-odd (alpha,beta)->(-alpha,beta), with G->-MG, k->Mk.
  All three ladder clusters are chiral (s21: C6 only; r46, r56: C2 only; work/cluster_mirror.py).
  => physical linear responses only for alpha_even and beta_odd; beta-odd part on product stars = cluster artifact.
  Posted note 20261014T053401.075Z_swarm-d_note_a0b1; mailed a, b, c, h.
- **My family `chiphase`** (hypothesis 20261014T053416.760Z_swarm-d_hypothesis_b769): phase-only, mirror-odd.
  Stage 1 = 38 requests (work/cp1/, submitted 05:34): 12-member-shell sub-star contrasts (|G|^2=7,13,19,21 x T1-T3,
  `work/chiral.py`, sub-star a contains the 0-30 deg member) + orbit odd contrasts S2T2,S2T3,S3T2,S3T3,S5T1,S6T1,S8T1
  (`work/jorbit.py` kind="odd" = (o_theta - o_{180-theta})/sqrt2, theta<90 first), beta=+-0.05 unit-ms.
  swarm-b covers S1-S3xT1, S1xT2/T3 classes at b=+-0.05 -> take A-B from them.
- Next: collect stage 1; fit linear g_d = [R(+)-R(-)]/2 and curvature per direction; build combined odd-beta step,
  line search, then bounded CMA-ES (box |beta_entry|<=0.3). Budget used: 38/500.

## 2026-10-14 wakeup 2 (05:56 UTC)
- Stage 1 results (order of ids = sorted filenames of work/cp1). Table in result post 20261014T055820.551Z_swarm-d_result_03e3.
  * 12-member star-level contrasts: EVEN in beta (|R+ - R-| <= 3e-4), best 1.010 -> sub-family closed (coverage posted).
  * Orbit X (odd) at +-0.05: S5T1 +: 1.614 PASS (req 2678, r46 2.218 PASS, r56 pending); S5T1 -: 0.257 FAIL.
    S6T1 +: 1.449 FAIL(split .107); S8T1 +: 1.17 FAIL(split .19); minus sides collapse (0.01-0.08).
    S2/S3 x T2/T3: both signs <1 (curvature-dominated at 0.05).
- Board: huge gains everywhere (leader swarm-r 4.44 s21). swarm-e (outerodd) took |G|^2 9/12/16 x T2/T3 + resolved 12-member orbits x T1.
  swarm-b: S1-S3 x T1 odd phase. swarm-r: cross-sector combos. Agreed splits by mail.
- Stage 2 (22, work/cp2, ids in work/cp2_ids.txt): S5T1 X scan 0.02..0.15; S6/S8T1 X 0.01..0.035; S2/S3xT2/T3 +-0.015;
  combos S5+S6, S5+S8 (0.035 each), S5+S6+S8 (0.025 each). Budget 60/500.
- Next: fit slopes, line search on best combined odd-beta direction; consider CMA-ES in (S5,S6,S8,S2T2..) X-beta space.

## 2026-10-14 wakeup 3 (06:19 UTC)
- Stage 2 (work/cp2_ids.txt; table via `work/tab.py`): S5 X 0.02/0.035/0.05 -> 1.42/1.61/1.61 (split/D .007/.023/.057), >=0.075 FAIL.
  S6 X .01/.02/.035 -> 1.22/1.44/1.56; S8 X -> 1.21/1.41/1.44. Pairs at .035 FAIL on split (0.21, 0.43): splitting ~beta^2, same sign, adds.
  S2T3 X -0.015 1.044 (r46 1.056), S3T3 X -0.015 1.050 (r46 1.071): small gains, ~no splitting. S2T2/S3T2 +0.015 ~1.01.
- Context: parent R_staticM2 = 0.123 (Delta_parent ~1.2 Delta_LLL despite M2=10) -> parent is "soft"; board leaders s21 ~10.9 (swarm-r mixed alpha/beta).
  swarm-r: log R ~ additive across levers; s21 split/D is binding gate; phase-only combos need splitting cancellation.
- Agreed with swarm-b: they combine S1-|G|^2=4 x T1 odd + S5; I keep S6/S8 + combos with S5 + T2/T3 odd levers.
- Stage 3 (12, work/cp3, ids work/cp3_ids.txt): small-step multi-lever phase-only combos (A, B at t=.6/1/1.5, pairs).
  Budget 72/500. 2678 still waiting r56.

## 2026-10-14 wakeup 4 (06:43 UTC)
- Stage 3 done: best combo cf77 (S5 .02+S6 .01+S8 .01) s21 1.598 / r46 2.018; phase-only s21 ceiling ~1.6-1.73 (also b, p).
  T3 levers don't lift it (99f0, b8c0 lower). Posted result+coverage 20261014T064551.403Z_swarm-d_result_1c9b; chiphase search CLOSED
  (PASS points remain on ladder; 2678 waiting r56 ~1h).
- New handle: phase linear sign flips for T3 vs T1/T2 (S2T3/S3T3 favour -X, S2T2/S3T2 favour +X) => momentum profile matters.
- Board: swarm-k ell2 = one l=2 field gamma_entry ∝ e^{2i theta_GR} (corr .995); r/b claims STRONG (ac14 4.44/4.93/4.43/4.93; b phase-only 1.15).
- Plan: family `kprof` = momentum profile (T2-only, T3-only, T1+cT3) of k's l=2 field, A and B. Mailed k (proposal) and p (T3 data).
  Wait for k's reply + their T1 lambda scan before submitting. Budget 72/500 (nothing in flight).

## 2026-10-14 wakeup 5 (07:07 UTC)
- swarm-k ell2 result: chiral C field lam*e^{2i theta_GR} on S4-S10xT1: lam .001 -> 2.188 (350a), .002 -> 3.584/r46 3.875 (481d), clean split.
  A-only == B-only R (gain sees only E+). Split agreed (k mail): d = T1+cT3 / T1+cT2 mixtures; e = T2/T3 alone (ell2t); k = shell profile + A/B angle.
- work/ell2.py reproduces k's 350a block to 1e-7. Posted hypothesis kprof (20261014T070854.321Z_swarm-d_hypothesis_c337).
- kp1 (8, ids work/kp1_ids.txt): C on S4-S10, lam .001 T3 c in {-.5,-.25,.25,.5}, T2 c=+-.5; lam .002 T3 c=+-.25.
- Withdrew 17 redundant chiphase points from r56 queue; kept 2678, a1e5, 3727, cf77. Budget 80/500.
- Other board: r claim STRONG b55a 10.9/11.4/11.2/11.4; i claim STRONG P1 single orbit 1.88/2.65/2.57/2.65; e's trap = non-Laughlin
  3-fold gapped state (EG<0.5) near large phase steps; a: mechanism = restoring weak V1 pair channel (e2 proxy, R2 .97).

## 2026-10-14 wakeup 6 (07:31 UTC)
- kp1 (C field S4-S10): T2 +.5 @.001 -> 2.512 (2dc1) vs 2.188 base; T2 -.5 -> 1.670. T3: all worse or equal
  (@.001: -.25 2.114, -.5 1.969, +.25 2.178, +.5 1.984; @.002: -.25 3.208, +.25 3.596 vs 3.584). T3 c<0 prediction (m, eta_R) fails in mixture.
- k: Cout R-1 ~ 1600 lam linear to lam .008 (3bd0 s21 13.58 / r46 13.11); E- control fails; B/A>1 better at fixed lam.
  k asked human about Sigma|alpha|<=2.5 being representation-dependent (binding at lam~.02 for pair stars).
- kp2 (9, work/kp2_ids.txt): c2 line @.001 {.25,1,1.5}; @.002 {.5,1}; @.004 {.5,1}; @.002 T2.5+T3.25; T2-only @.002.
  Compare also at equal Sigma|alpha| (T2 adds cells). Budget 97/500.

## 2026-10-14 wakeup 7 (07:55 UTC)
- kp2: T1+.5T2 s21/r46: .001 2.512/2.364, .002 4.396/4.045, .004 8.094/6.121 (vs T1-only 6.900/7.322) -> T2 gain s21-only;
  c2>=1 collapses; T2 alone kills. Worse per Sigma|alpha| too. kprof CLOSED: result 20261014T075607.549Z_swarm-d_result_8c71, abandon _0265.
- Theory: on 12-member shells e^{6i theta} const per chiral sub-star -> higher harmonics = sub-star weights of l=0/+-2.
  MT: real antisym weight MT-odd; conjugate phase pair e^{+-i phi} MT-invariant (verified work/verify_subphase.py) -> last T1 angular knob.
- subphase (hyp 20261014T075831.828Z_swarm-d_hypothesis_dc52), sp1 6 evals (work/sp1_ids.txt): E+ S4-S10 lam .002 phi +-30,+-60; lam .004 phi +-30.
  builder work/ellc.py (general complex c(G,R)). Budget ~95/500.
- chiphase keepers (2678,a1e5,3727,cf77) still waiting r56 (>2h). k STRONG claim 3bd0 13.58/13.11/13.10/13.30.

## 2026-10-14 wakeup 8 (08:20 UTC)
- subphase: +-phi agree to 2e-3; phi=+-30 @.002 3.31/3.57, +-60 2.60/2.75, @.004 +-30 6.30/6.65 (all below phi=0 baselines).
  CLOSED: result 20261014T082041.776Z_swarm-d_result_7f32 (coverage). Mailed b (ellhi overlaps: l=-4 == sub-star phase).
- Empirical rule: every sub-star-antisymmetric deformation is even (MT allows linear but it's absent).
- T1 angular space covered: {l=0, E+} x shell weights x lambda (E- breaks manifold). Others (k, r, n) cover shell weights/lambda.
- Remaining: chiphase keepers 2678/a1e5/3727/cf77 waiting r56 (~3h). Plan: wait for r56 -> phase-only claim if min holds, then swarm done.
  Budget 95/500 (deliberately not spending: no uncovered direction left that I can justify).

## 2026-10-14 wakeup 9 (08:52 UTC) — DONE
- r56 queue runs in R order; my phase-only keepers (rank ~400) still pending; broker assigns claim tiers automatically.
- Withdrew 19 subphase/kprof pending promotions (no-lever controls). Posted `swarm done` summary (work/done.md). 95/500 charged.
