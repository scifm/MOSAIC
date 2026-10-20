# swarm-o notebook

Started 2026-10-14T10:24:38+00:00.

## 2026-10-14 ~11:30 — wakeup 1: orientation, family choice
- Board: a,b separable axis maps; c jorb (S1xT1 orbits: +17-22% at s21!); d chiral half-shells; e bigamp;
  f chiral-odd beta; g joint-orbit S_sxT_s; i kpow; j perp-amp (S1T1 d090 alpha scan); l phase-even beta^2.
- Heavy herding on S1xT1 orbits. I chose `orbit-fit`: integrator role — map every block onto the 126 C6
  joint-orbit coords (work/orbits.py), pool all s21 data (work/harvest.py, cache in work/cache), fit
  per-orbit slopes, then line-search along the pooled gradient (full, alpha-only, beta-only), then a
  quadratic surface in top ~6 coords. Hypothesis: 20261014T112803.266Z_swarm-o_hypothesis_b532. Budget <=150.
- Mesh facts (work/mesh_moments.py): R=(2,0) at Nyquist on 4x6 (T3 msq 4/3 on r46); T2 on s21 takes 7 values.
- Orbit conventions: rotG (m,n)->(m-n,m); rotR (a,b)->(-b,a+b); unit full-star = unit vector; c's per-entry
  0.05 = alpha_o 0.0866.
- Next: when harvest finishes, fit slopes; design line search.

## 11:45 — pooled fit + line1 submitted (14 evals)
- Harvest (work/harvest.py, threaded; cache work/cache) -> 139 s21 points; work/fit.py diag-quadratic in orbit coords.
- Strongest slopes (s21): chiral-odd beta S3T1 (d030 +11, d150 -11), S2T1 (d060 +7.5, d120 -8), S1T1 (d030 +3.5,
  d150 -3.4); alpha S2T1d000 +4.1, S2T1d060/120 -2.7, S1T1d090 -2.1. Outer separable S5/S6xT2 alpha +-0.05 -> -50..-60% (huge even curvature).
- Best board points: f chiral-odd beta S3T1 +56%, S2T1 +48%, S1T1 +38% (all PASS). e large alpha S3T1 +60% but FAIL.
- line1 = diag-Newton point x* (work/line1_xstar.npy; coords S<=3, >=2 pts, gain>=0.015), scanned:
  full t=.1,.2,.3,.45,.65,.85; alpha-only t=.25,.5,.75,1; beta-only t=.15,.3,.5,.75. Sigma|beta| binds at t~0.9.
- Diag model predicts +400% at x* -> certainly overestimates (no cross terms). The line tells the cross-curvature.
- 11:46 herding: 4 pooled surrogates (h,o,t,u; u abandoned). Mailed h,t: I stop fitting after line1, hand off
  quadratic/TR, move to a hole (p#3 large-amp non-perp alpha orbits S2xT1 d000/d060/d120, S1xT2; or c#1 FS of combined optimum).
- Board facts: chiral phase orbits transfer (r46 > s21; c d698 s21 1.249 r46 1.404). Response is min-of-branches (kinked).
  Outer shells |G|^2>=7 at 0.05 break the manifold (a's note).

## 12:13 — wakeup 2
- line1 still pending (queue congested). t keeps orbsurr (min-of-K-quadratics); I move to a hole after line1.
- Leaderboard: STRONG claims already: S1T1 perp alpha large (j ea28 / q c027: s21 1.64, r46 2.63, r56 2.44, conv46 2.63,
  M2k 9.44); chiral-odd beta S3T1 (f e5d5: 1.56/1.64/1.56/1.64, phase-only => beyond-M2).
- line1 itself = FS motion of combined optimum (points >=1.02 get r46/r56 free). Next hole TBD after line1.

## 12:40 — wakeup 3
- line1 still pending (55 min). Board: multi-orbit combos from t/h reach s21 4.82 (t 8c01), 4.76 (h c662); f0fb 3.51/r46 3.86.
  So orbit gains are roughly ADDITIVE (my sub-additivity prior was wrong). Claims STRONG: f 728b (phase), j 3d0f (perp alpha).
- Mechanism posts: k/u: gains not from larger projected interaction; density controls < 1. e: PES entanglement gap drops 13->4-5.
- g requests a solver gauge-covariance check before phase-only claims are final; p doing rotation test.
- Plan: post line1 result + coverage when it lands; then decide whether a TR step adds anything beyond t/h.

## 13:10 — wakeup 4
- line1: all 14 SUBMITTED since 11:48, no result in ~80 min while others' later jobs finish -> posted ops request
  20261014T130930.549Z_swarm-o_request_1724. Not resubmitting.
- Board: h STRONG claim c662 4.76/5.23/4.67/conv 5.23 (alpha+beta; density control k: 0.995 -> density excluded).
  t 8c01 s21 4.82 / r46 5.19. alpha*beta superadditive (h). av: records follow angular rule alpha~cos2delta, beta~sin2delta.
  g raised d_sc critique (parent near zero mode), p refuted (contact term inert for scalar LL0).

## 13:45 — wakeup 5: line1 landed — BOARD RECORD
- full line s21: t .1 1.86, .2 2.59, .3 3.23, .45 4.03, .65 4.97, .85 6.28 (f5f1; r46 8.33, r56 8.12, all PASS; conv46 pending).
  alpha-only breaks at t>=.75, beta-only at t>=.3 (manifold), beta-only .75 s21 5.33 but s21c PES FAIL. Combo stays clean (splits cancel).
- f5f1 at Sigma|beta| 1.882/2.0 -> boundary. Posted result 20261014T134255.580Z_swarm-o_result_68e8.
- line2 (8 evals, builds on f5f1): A alpha boost t_a 1.0/1.15/1.3 at t_b .85; B drop S1T3+S2T2 beta (work/line2_bD.npy) t .85/1/1.15/1.25;
  C (t_a 1.3, t_b 1.25). Box widened to |beta_o|<=0.30.
- Stuck-lane request resolved (note posted).
- TODO: when f5f1 conv46 lands -> claim post (STRONG if >=1.1 everywhere). alpha!=0 + perp content -> ask k/i for density control.

## 14:10 — wakeup 6
- f5f1 conv46 8.3252 PASS -> broker claim strong. Posted claim 20261014T140941.147Z_swarm-o_claim_2208.
- Controls for f5f1 queued by k (_2a80 <rho_k>, _11cb M2-matched) and i (A/B). My no-perp ablation 07f8 pending; line2 (8) pending.
- Others working around f5f1: z rcma centred at f5f1 (S1-S3xT1 vary), e S3T1 cos2d alpha on top of f5f1 (8710,d7da,6438,...).
- Board: s no-perp combined line to s21 7.35 at t=4 (no turnover); h union s21 6.59; aa S3T1 beta on records 6.32.
  Phase-only s21 ceiling ~1.73 (several agents). t asked human re representation-dependent caps (789e).

## 14:45 — wakeup 7
- line2 s21: A ta 1.0/1.15/1.3 @tb.85 -> 7.37/8.21/8.94 (a334 best, Sigma|a| 2.43). B (bD) .85 7.01, 1.0 FAIL split, 1.15 6.47, 1.25 6.42; C 6.78.
  no-perp ablation 07f8: 3.91 (perp ~40% of f5f1's s21 gain). f5f1 density controls 0.992/1.001 (k).
- Posted line2 result. Submitted grid3 (6): a0/aD (aD drops S2T2,S3T3 alpha) x ta 1.3-1.65 x bD .6/.85.
- Board: av e0a8 rule STRONG 10.39/9.87/10.50/conv 9.96 (cap-limited). Records cap-limited; human asked re chart-dependent caps.
- Plan: after grid3 lands -> coverage post, then likely `swarm done` (direction saturated at caps, swarm crowded).

## 16:37 — wakeup 8
- grid3 all STRONG-tier: 31e4 (aD1.65,bD.85) 10.98/11.11/10.86/conv 11.11 (best, Sigma|a| 2.477 cap); 6267 10.40/10.76/10.46;
  2256 9.47/10.17/9.82; ffeb 9.74/9.52/10.08; a365 10.01/10.04/9.25; df6e 9.18/9.15/8.81. line2 A points STRONG (a334 min 8.94).
  bD line beyond t .85 at low alpha: r46 FAIL splitting (a27b, 004b, 8925).
- Posted claim 31e4. grid4 submitted: aD1.65 x bD 1.0/1.15/1.25 (2c9f, beac, 6dca) to use Sigma|beta| room.
- Board frontier ~11-12 (h 5063 min 11.65, e c577 11.38); u: qmax-8 truncation suspect at R>11-13.
- Plan: grid4 lands -> coverage result -> swarm done.

## 17:10 — wakeup 9: family closed, done
- grid4 (beta at alpha cap) lowers R: 10.30/11.09, 9.35/10.34, 8.70/9.43 -> 31e4 is family optimum (min 10.86, STRONG).
- Posted closing result + coverage 20261014T170856.178Z_swarm-o_result_0361. 32/500 evals charged.
- Reason to stop: direction is cap-limited; frontier (~11-14) crowded with cap-reallocation agents; open items are
  the human's (cap reading, qmax at R>12, N_A=3 PES on rectangles, 31e4 density control by k/i).
