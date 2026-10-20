# swarm-q notebook

Started 2026-10-14T05:20:40+00:00.

## 2026-10-14 wakeup 1
- Read brief, theory docs (gen-space, pilot 024, key-facts), board (11 hypotheses), leaderboard.
- Board state: joint-orbit P (G⊥R) amplitude at c=-0.06/entry gives s21 +20..+37% (f721 S3xT1 P 1.3676; c5b8 S1xT1 P 1.2022, r46 1.2044). Crowded: a linmap, b/c/i/k joint orbits, d/j phase, e/f/h large amp.
- Chose niche: family `m2ctl` = matched-density static controls (beyond-M2 claim). Def: rho_bar = <|h_k|^2/<|h_k|^2>_uc>_BZ, truncated to parent's 10 shells. Script work/matched_control.py (reproduces broker M2k). Submit with --control --clusters s21,r46,r56.
- Submitted fbad (ctl of f721), 2c5a (ctl of c5b8). Posted hypothesis 5ae5. Mailed swarm-c.
- Expect R_ctl≈1.00 (rho_bar-parent = O(alpha^2), max dw 9e-4).
- Next: read results; control any large-alpha candidate reaching r46 >=1.05; critique posts; pick a search direction after large-step waves land (avoid herding).

## 2026-10-14 wakeup 2 (05:57)
- Controls done: fbad (f721) R_ctl 0.9992 on s21/r46/r56; 2c5a (c5b8) 0.9989. Uniform across clusters. Gain is fully beyond rho_bar.
- swarm-a (mdctl) and swarm-l (mdens) did the SAME control. Dedup: swarm-a owns rho_bar controls; posted result 81ae, mailed a and l.
- Board: P-orbit T1 amplitude dominates. swarm-i P1 line: c=-0.5 gives s21 1.88, r46 2.65. swarm-r ac14 (3 T1 P orbits at 0.06 + odd beta on |G|2 3/9) gives s21 4.44 (superlinear!). Phase-only chiral: swarm-b af08/9a9a r46 1.39.
- Product-star large alpha/beta: all FAIL (e, f, j abandoned).
- New family `lllsub`: same deformation on uniform-LLL density (--control); read Δ_sub/delta_lll. Submitted d158(c5b8), d9a7(9de1), 6ee5(af08) on s21/r46/r56; 9892(f721), 67a7(06d6), 6cc6(ac14) on s21. Script work/lll_substrate.py.
- Ideas pending: critique ac14 superlinearity once r46 lands; check s21 manifold reorganization at large c.

## 2026-10-14 wakeup 3 (06:20)
- lllsub results (Δ_sub/Δ_LLL): c5b8 0.955/1.019/0.977 (s21/r46/r56); 06d6 (opp sign) 0.974; f721 0.973; 9de1 0.816/0.843; af08 0.979/1.024; ac14 0.850. The deformations are harmful or neutral on uniform LLL, and the signed response vanishes. So the gain needs w1c's density ("repair of a soft parent"). Posted result 148b.
- Conversion: R_vs_w1c × Δ_w1c/Δ_LLL; ratios s21 1.2361, r46 1.3778, r56 1.4252.
- Board: leader swarm-r b55a s21 10.9. swarm-c statfront (static ρ_t, t=.25,.5,.65,.8,.9) and swarm-f statctl (mix/power/frozen-k) test the "soft parent". swarm-a owns rho_bar controls (a440 ac14, 203e 41dd, f032 9de1).
- Submitted 13 ρ_t×γ controls (s21+r46): c5b8, 9de1, ac14, b55a × t∈{0.5,0.65,0.8} + b55a t=0. Script work/tsub.py. Goal: Δ(ρ_t,γ) vs swarm-c's Δ_static(ρ_t) → does the best k-dep beat max_t static?
- Budget ~44/500.

## 2026-10-14 wakeup 4 (06:45)
- ρ_t results, as G(t) = R_kdep/R_static(t) (s21/r46). The static values are from swarm-c's statfront: t=.5 .724/.705, .65 .755/.743, .8 .832/.826.
  - c5b8: .95/1.02 → 1.09/1.12 → 1.15/1.17 → 1.19/1.20 → 1.20
  - 9de1: .82/.84 → .79/.60 → .74/.67 → .97/1.01 → 1.88/2.65 (gain only at t→1: the "repair the near-zero region" lever)
  - ac14: .85 → 2.81/2.95 → 3.60/3.81 → 4.16/4.48 → 4.44/4.93
  - b55a: .24F/.57 → 3.0F/2.7 → 4.9F/4.6 → 7.4/7.5 → 10.9/11.4
- w1c is the maximum of its static ρ_t family (swarm-c), and is not soft (swarm-f). ac14 on t=0.5 gives Δ = 2.04 Δ_w1c, which beats every static member of the family. Posted result 53a3 (with critique of the b55a s21 split edge); mailed swarm-r.
- Leader b55a: s21 10.9, r46 11.4. Claims so far: ac14 STRONG (r); ec27 STRONG phase-only (b).
- Budget ~56/500. The board is crowded with optimizers (r, h, n, p, k-ell2). The physically linear sectors (α even, β odd) are MT-invariant, so they need no mirror check.
- Next: critic/verifier mode; look for an uncovered gap; long wakeups.

## 2026-10-14 wakeup 5 (07:15)
- Board: claims now ac14 STRONG, b55a STRONG (11.4 conv46), 9de1 STRONG (i), ec27 STRONG phase-only (b). Leader 3bd0 (swarm-k ell2) at s21 13.58. Mechanism: swarm-a e2 pair-channel proxy, R² 0.97 (27fc). There is a non-Laughlin trap state (swarm-e 87bd); swarm-n audit finds the top 25 clean.
- swarm-c static refs: w3 Δ = 2.02×w1c (s21), 1.82× (r46) [45e7]; w2 1.43/1.28 [a831]. So w1c is a weak static GLL in absolute terms.
- New family xparent: leader blocks on w3/w2 densities (--control, s21+r46), 24 evals. Hypothesis dcd2. Script work/xparent.py. Reqs: 9be2, fc9a, 416d, d87b, f77d, 9c13, 1b19, 32dc, c97c, 5382, e008, c400 (names in work/xp).
- Budget ~80/500.

## 2026-10-14 wakeup 6 (07:38)
- Transfer results: G on w3 / w2 (s21/r46). c5b8 .80/.86 | .95/1.02. 9de1 .26/.25 | .29F/.32F. ac14 .83/1.00 | .65/.82. b55a .16F/.13F | 0F/.03F. 3bd0 .93/1.09 | .93/1.04. ec27 .97/.99 | 1.01/1.04. Nothing transfers. Posted result.
- Submitted the w3 linear-response probe on s21+r46: P1+ (e3c7), P2+ (9551), P2- (4f9f), u1 b- (3ea5), P3+ (170a), P3- (3216). c5b8 = P1- on w3 is 5382.
- Board: josobol c954 full ladder min 11.25; ell2 3bd0 at 13.6 has a truncation critique (swarm-i); boundary Σ|α| representation question raised by k and h.
- Budget ~92/500.

## 2026-10-14 wakeup 7 (08:00)
- w3 linear response (G s21/r46): P1+ 1.127/1.106; P1- .803/.858; P2+ 1.120/1.113; P2- .807/.874; P3± ~.97/1.02; u1 β± ~.97/.99. On w3 the P1 sign is flipped vs w1c and P2 keeps its sign. Posted result.
- Submitted the w3 re-tune (12 evals): e1bf (.06,.06), 0430 (.12,.12), f86c (.2,.2), 3988 P1 .15, 8d35 P1 .3, 1bf2 P2 .15. The blocks are in work/xp4.
- Board: new strong claim 3bd0 (k); swarm-n chiral projection of b55a gives min 12.18; several agents done (m, i).
- Budget ~104/500.

## 2026-10-14 wakeup 8 (08:22)
- w3 re-tune, G (s21/r46): (.06,.06) 1.256/1.217; (.12,.12) 1.380/1.387; (.2,.2) 1.012/0.935; P1 .15 1.333/1.284; P1 .3 1.235/1.204; P2 .15 1.332/1.334. So w3's best is about ×1.39, against ×11–13 on w1c. In absolute terms the w3-tuned band is 2.79/2.52 × Δ_w1c, while the w1c leaders are about 11–13.
- swarm-k asked for the chiral l=2 field on w3. Submitted the 3bd0 block scaled 0.25/0.5 × (E±, ±λ): 2a85 f061 3bb5 1c75 (E+ +,-,+,-; the λ .002 pair, then .004), 0aae e2f6 ec1a d4c7 (E-).
- Board: swarm-k notes all 40 strong claims are one chiral E+ field. Several agents are done (e, i, j, m).
- Budget ~128/500.

## 2026-10-14 wakeup 9 (08:45)
- w3 chiral, G (s21/r46): E+ +λ .002 1.021/1.097, .004 1.034/1.144; E+ −λ .996/1.030, 1.003/1.088; E− ± .85-.87/.93-.95 (λ .002), .53-.57/.61-.64 (λ .004). Posted xparent closing result with coverage.
- Submitted the ρ_t substrate for the E+ field leaders: 3bd0 at t = 0/.5/.8 (f07a, 3223, b1dd) and 2fb9 (n's strong claim 14.27 min) at t = 0/.5/.8 (4fb4, 2c2d, 2f65), on s21+r46.
- Budget ~156/500. Plan: post the ρ_t addendum, then likely swarm done unless something new needs a verifier.

## 2026-10-14 wakeup 10 (09:08), final
- ρ_t for E+ leaders, G (s21/r46): 3bd0 at t0 .87/1.07, .5 6.03/6.05, .8 10.97/11.15. 2fb9 at t0 .67/.86, .5 1.63F/2.05, .8 7.73/7.87. Posted addendum 06ff with the updated lllsub coverage.
- All my families are closed: m2ctl (handed to swarm-a), lllsub, xparent. Ran swarm done.
