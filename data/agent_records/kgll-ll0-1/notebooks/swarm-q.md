# swarm-q notebook

Started 2026-10-02T03:52:14+00:00.

## 2026-10-02 04:20 UTC — wakeup 1: scope chosen = `geom-mech`
- Board: atlases (a w3; b, e, f w2), wide CMA-ES (c), chiral/orbit phase (d, g, h, i, j, k, l), K7/T4 column + aliasing (m, o, r),
  contrast-pump (n), pooled surrogates (o, r). Broker "looks dead" (no tick for 16 min, 0 charged). Nothing submitted by me.
- Built `work/geom.py`: single-particle Berry curvature (plaquettes) + tr g (fidelity along G1, G2, G1+G2) from the solver's raw LL0
  form factor x kernel W_G(k,k'). Validated: uniform LL0 gives Omega = -1 everywhere (C = -1 is the solver's sign); static parents ideal.
  The O(delta^2) offset in T_viol is about -0.0056 at N = 18, so always quote dT relative to the parent at the same N.
- Doc-46 points: a1p (+1.85%) and a1m (-9%) are geometrically almost identical (sigma_Omega 0.071 / 0.077, dT 0.006), so the amplitude linear
  term is NOT geometric. b1p: dT = 0.025, -4.4%. Static w3 curvature is flat to 1.5%.
- `work/alias.py`: s21 has only 4 independent C6 k-profiles (T1, T2, T3, T4/K7); |R|^2 = 21 is mesh-constant on s21 (static loophole).
  m, o, r posted this first, so I did not post it.
- Posted hypothesis 20261002T041945.088Z_swarm-q_hypothesis_d7b6 (budget <= 60 req).
- NEXT: once results land, pull the evaluated inputs (swarm show) for every request on the board/leaderboard, compute geometry,
  and regress R-1 on dT and sigma_Omega for alpha / beta / joint. Key test: is beta-only R a single function of dT?

## 04:51-05:00 UTC — wakeup 2
- Broker alive (human: it was slow). Huge w3 amplitude gains: o 968b s21 1.609 / r46 1.710 (r56 pending); c far-field 1.41-1.52.
  w2 best is chiral beta (i ffbc 1.066). Board: amplitude gradient sits on S1T1-perp and S2T1-par A orbits (h, k, g); chiral beta live on S4T1 and |G|^2=13 x T1.
- Geometry of the leaders (work/geom_batch.py, cache work/geom_cache.json): strongly NON-ideal, dT +0.10 to +0.46, sigma_Omega 0.24-0.80.
  968b is the least non-ideal and has the largest R, so geometry is not the amplitude mechanism. Chiral-beta w2 points barely move the geometry.
- swarm-b critique (e1e5): the S1T1-perp cos.cos cell has a k-independent cyclotron half. Checked in the solver convention: partner R^ = (n,-m) for G = (m,n).
  The C6 sum over S1 feeds only cyclotron n = 0 mod 6 (LL0 + LL6, first-order amp ~0.028 for 968b). S2T1-par has no static half but the same slope (k: 2.60 vs 2.79).
  Posted 20261002T045514.688Z_swarm-q_note_2b46; mailed b.
- Diagnostics: R_staticM2 (= R_gap / (M2k/M2*)) is 0.97-1.18 for the w3 leaders, so most of the gain tracks M2^(k).
  Yet p's M2-max rays lose gap: M2^(k) is necessary-ish but not sufficient.
- Solver a_n are incoherent |a_n|^2 component weights, so no a_n control can emulate a coherent LL0+LL6 seed.
- Mailed o for full request ids of the pooled set. NEXT: run the regression; decide whether any ED budget is worth spending (iso-geometry probes look low value now).

## 05:22-05:26 UTC — wakeup 3
- Board: w3 up to s21 2.62 (o 48bf); the LL-free recipe is alpha S2T1-par + chiral beta (C7 = S4T1, C13 = S7T1); p cc86 s21 2.40 / r46 2.47.
  w2 best is r's chiral-beta combos (s21 1.14 / r46 1.29). No r56 results for any non-parent point yet (2 GPU lanes; c asked the human).
  i's selection rule: live T1 directions have k-independent (Q_tot = 0) kernel content via parent harmonics, i.e. LL-mixing-type; raised with the human under b's 3942.
- o shared the pooled dataset (o/work/board.json, regenerate with o/work/board.py). geom_board.py: 998 pts in 25 s -> work/geom_board_N12.json; mailed o.
- RESULT abc0: phase-only r46 - s21 = 0.04 + 5*dT on w3 (n = 15, R2 .93) and w2 (n = 19, R2 .91), same slope; |beta|^2 slopes differ 2.7x.
  Phase-only s21: R - 1 anti-correlated with dT (kappa 1.3 w3 / 4.3 w2). Amplitude: geometry is not predictive.
  Pre-registered r56: d 3ea2 -> ~1.30 if r46-like, ~1.05 if s21-like; r 636e -> ~1.26 / ~1.06.
- Submitted 2 controls (s21 + r46): 7a28 (877a mode x1.605), d093 (9818 mode x0.623), matched in dT. Weak discriminating power (stated in note e51c).
- NEXT: watch the r56 results for phase-only points (3ea2, 636e, 7e0b, 0f55, e064, 7f96, ...) against the pre-registration; fit the joint points as
  phase-law + amplitude drift; possibly a w2 matched-dT pair with ratio 5 vs 13.

## 05:51-05:55 UTC — wakeup 4
- My controls: 7a28 s21 1.034 / r46 1.103; d093 1.025 / 1.069. At equal dT the cross-mode excess ratio is 1.4-1.5, at equal |beta|^2 it is 3.2.
  So dT absorbs most of the mode dependence but not all.
- r56 verdict: phase-only 2400 (.45) and 877a (.50) keep about half the r46 excess; joint leaders keep .7-.8. Non-monotone in N (s21 7, r46 8, r56 10).
  Posted result 656b; critique of d's robust_positive claim c0eb (>=1.05 margin is marginal) posted and mailed to d.
- Refit with more data: w3 phase r46-s21 = .037 + 5.06 dT (R2 .88, n = 18); w2 .047 + 5.28 dT (R2 .91, n = 24).
- Posted a request to the human for a 4th cluster (sym Nk = 27) as a control target for ~8 phase-only points.
- Board: p's claim cd9d STRONG (cc86 s21 2.399 / r46 2.470 / r56 2.456 / conv46 2.469), provisional on the LL-mixing ruling.
  e: chiral-beta patterns at alpha = 0 LOSE (the beta gain is an alpha x beta interplay). w3 leader h fea3 s21 2.80.
- Tooling: work/board.py (copy of o's) -> work/board.json; geom_board.py work/board.json; geom_regress.py and geom_split.py now read work/board.json.
- NEXT: l's 13c3 line at r56 (one-parameter test); the human's answer on a 4th cluster; fit joint excess = phase law (on the beta part) + amplitude drift.

## 06:23-06:26 UTC — wakeup 5
- f's critique (48a8): the parents' r46 gap is 4.1 % low, so every r46 R carries +4.3 %. Accepted. Refit on the candidate's own gap ratio (work/geom_raw.py):
  phase-only own-gap r46/s21 - 1 = -0.009 + 4.80 dT (w3, n = 25, R2 .91) and +0.002 + 4.78 dT (w2, n = 24, R2 .92). Intercept gone; slope identical.
- PES eg vs dT (work/geom_pes.py): eg ~ A dT^-0.2 (w2 all R2 .85, w3 all .64); eg barely correlates with R_s21. Purity loss tracks ideality loss.
- Posted result 19e3 (correction + PES law); mailed f.
- Board: leaders w3 h fea3 s21 2.80 / r46 3.59; claims STRONG: p cc86 and o bd1a (provisional on the LL-mixing ruling); d 2400 robust_positive (phase-only).
  w2 leader g's alpha+beta 1.26 s21. p's static-free null supports i's rule.
- NEXT: l's 13c3 line at r56; the human's answer on a 4th cluster (ad5e). Consider whether any own-budget experiment is worth it (probably not; the board is saturated).

## 06:55 UTC — wakeup 6
- n 262d: static bands lose PES eg with M2 (21 -> 6), so purity has a density channel. Joint fit (work/geom_pes2.py): for phase-only points
  (M2 fixed) log dT carries all of it (eg 21 -> ~10 at dT .003); for amplitude and joint points dT and M2k are collinear. Reconciled in note.
- Suspected singular parent: the own-gap r46/s21 is .959 for the parent and n's statics but ~.99 for the smallest phase points; eg 21 -> 10.
  Submitted continuity controls 8f92 / f6df / 67cf (2400 mode x0.03 / 0.1 / 0.3; dT 3.7e-6 / 4.1e-5 / 3.7e-4) on s21 + r46.
- Board: k 435c s21 3.47 / r46 3.84 (w3 top); claims STRONG: c 776c (amplitude-only), h d49b (small amplitude, LL-free), p cc86, o bd1a.
  m finished (final summary). w2 top k c6a8 s21 1.33.
- NEXT: read the continuity results (fast, s21 + r46); if singular, post a critique about the r46 baseline.

## 07:12 UTC — wakeup 7 (short)
- Continuity controls still pending. New phase-only r56 on w2: r e064 (dT .0122) s21 1.077 / r46 1.205 / r56 1.141; l 9fcb (dT .0109) 1.071 / 1.187 / 1.128.
  Own-gap terms (parent factors removed): e064 r46 +7.3 %, r56 +5.6 %; 9fcb r46 +6.3 %, r56 +5.0 %. So r56 keeps ~0.8 of the own-gap r46 excess at dT ~ .01,
  while 2400 (dT .004) has own r46 -0.1 %, r56 +1.5 %. To be folded into the next result once l's full line has r56.

## 07:33 UTC — wakeup 8
- Continuity controls are done: own r46/s21 ratio 0.9586 -> 0.9589 -> 0.9597 -> 0.9633 -> 0.9993 at s = 0, .03, .1, .3, 1. Smooth, so the parent is not singular.
  R_s21 is linear in s (slope ~.04 per unit s). Single-mode eg = 4.3 - 2.7 log10 dT, i.e. non-Laughlin weight ~ dT^1.2. Posted result 0af5.
- Board: agents finishing (m, c, o done). o claim 84e4 phase-only STRONG with r56 margin +0.1 % (o flags it).
- NEXT: one more wait for l's 13c3 line at r56 (own-gap r56 vs dT), then the final coverage result + swarm done.

## 08:16 UTC — wakeup 9: CLOSED
- 26 phase-only r56 points: own-gap r56 excess = .005 + 3.30 dT (w3, R2 .97), .005 + 3.80 dT (w2, R2 .96); r46 4.42 / 4.46.
  r56 keeps .70-.88 of the r46 excess above dT .006, so s21 is the low outlier. This retires 656b's "half is cluster shape" worry, which came from the smallest-dT points.
- Posted final result 6210 (coverage) and ran `swarm done`. 10/500 evaluations used, all controls. Open: human request ad5e (larger cluster).
