# swarm-f notebook

Started 2026-10-14T10:24:06+00:00.

## 2026-10-14 wakeup 1 (11:12–11:20 UTC)
- Read docs 40, 46, theory §6.4/§8, kdep_envelope.py, reference, board (only swarm-a's axis-map hypothesis).
- Parent w1c s21 Δ = 2.2586e-04 (reference). Deformation block = spatial_stars, momentum_stars, alpha/beta J×P, n_mesh; broker sets g_cutoff 8.
- **Idea (my family `chiral-joint`)**: pair stars {±G},{±R} accepted by swarm check. Joint (G,R) orbits labelled by
  δ = ∠R − ∠G mod 180. MT symmetry maps (α_δ, β_δ) → (α_−δ, −β_−δ). ⇒ separable/chiral-even β: even in β (TL);
  chiral-odd β: linear allowed. 54 chiral-odd combos total (1 per 3×3 block, 3 per 12-member-shell block).
- work/joint.py: geometry, blocks(), chiral_split(), block_spec(terms) [coef per entry = c/sqrt(nG nR)], write_input.
  Separable reconstruction check = 1.3e-15.
- Posted hypothesis 20261014T111835.287Z_swarm-f_hypothesis_75c0; mailed swarm-a.
- Submitted batch 1 (16): work/inputs/b1 (S1T1 odd ±.05 ±.10; even-pair ±.05; S1T2,S1T3,S2T1,S2T2,S3T1 odd ±.05).
- Next: read results; check odd part (R+ − R−)/2 vs even part; compare control; if odd slope real, do all 54 odd directions.

## wakeup 2 (11:35 UTC)
- Board exploded: ~40 agents, ~20 in low-shell T1 joint orbits (herding note swarm-c 05eb). swarm-c jorb (bc24) confirms MT
  symmetry; swarm-h note 4bf9 confirms from 34 image pairs (s21 chirality artefact ≤ 2.5 %). swarm-a agrees by mail.
- swarm-e 703a: full-star axes break the manifold at |α|~0.1–0.2, |β|~0.12; useful window small.
- Batch1 so far (s21): S1T1 odd β +0.05 → 1.1921 (ceb6), +0.10 → 1.3806 (5098, board #1), −0.05 → 0.8067 (2e6e);
  even-pair control ±0.05 → 0.9822/0.9744 (even, as predicted). Rest pending.
- Convention note: my β is "separable units": per-entry = β/3 for 3×3 blocks. swarm-c uses per-entry values.
- Submitted batch 2: S1T1 odd β +0.13, +0.16, +0.20, +0.25 (bf63, 4211, fb1b, 0494) to find the line's maximum.
- Mail from j, u, s, a, ag (all coordination; no action needed). CMA/surrogates in odd-β space are heavily claimed
  (ag, am, n, z, u, o, t, h) → do NOT start another optimizer. Candidate niches: finite-size of the line (free via ladder),
  remaining odd combos, then maybe verifier role.

## wakeup 3 (11:52 UTC)
- Batch1 done (s21, separable units b, per-entry b/3):
  S1T1 odd −.10 .6157, −.05 .8067, +.05 1.1921 (r46 1.1840), +.10 1.3806 (r46 1.3875)
  S1T2 odd −/+.05 .9347/1.0132; S1T3 1.0460/.9191; S2T1 .5208/1.4832 (r46 1.5070); S2T2 .7461/.9528;
  S3T1 .4288/1.5582 (r46 1.6409, split/Δ ~1e-2, eg 4.8); even-pair control .9744/.9822.
- Leaderboard top s21 1.6386 = ⊥ α S1T1 large (j/q/r). Mine e5d5 1.558/1.641.
- Outer 45 odd directions claimed by a, ap, ac, aq, as (+at, an at my leaders). I keep inner 9 + ascent.
  swarm-aa maps S1/S2/S3×T1 3-D odd-β subspace densely (axis lines to 0.3, grid). e/i/ao map T2/T3 inner orbits.
- Submitted batch3 (7): gradient line dir (3.85,9.62,11.29)/norm at t=.04,.06,.08,.10,.13 + balanced (1,1,1)/√3 at .06,.10.
- Posted result a35e with coverage.
- Next: read b2 line (S1T1 to .25) and b3 ascent; if ascent peak found → refine with second-order fit in 3D,
  then add T2/T3 inner odd (from e/i data) and maybe α ⊥ combination (but j/r/q/x on that).

## wakeup 4 (12:13 UTC)
- e5d5 (S3T1 odd b=+.05) → STRONG: s21 1.5582, r46 1.6409, r56 1.5596, conv46 1.6409; split/Δ ≤1e-2, eg ~4.8.
  Posted claim 728b. Mailed swarm-p to include it in the N_A=3/27-site request.
- 2e98 (S2T1 odd +.05): r56 1.4527, conv46 pending. defd (S1T3 odd −.05) suggestive 1.046/1.060/1.009.
- Board: swarm-c STRONG claim 893d (S2T1 +60 single orbit β=.03: 1.249/1.404/1.347). Board leader by r46: ⊥ α S1T1 −0.45
  (j ea28: 1.64/2.63/2.44 STRONG, but ak critique: branch change). x xcomb s21 1.92.
- Queue slow: b2 & b3 (11) still pending after ~40 min.

## wakeup 5 (12:36 UTC)
- 2e98 now STRONG too (1.483/1.507/1.453, conv46 1.507). e5d5 checked by swarm-g (note 7d9a: input verified, MT-invariant, band distance 3.5e-4).
  swarm-p added e5d5 to N_A=3 request; p running rotation test of k≠k' phase handling. swarm-g asked human for gate-3 gauge check.
  swarm-e: PES eg of leaders ~4–5 vs static 13.4 → quote EG with R.
- Leaderboard now multi-orbit combos: t 8c01 s21 4.82 (Newton mix α+β, β_max .077), h c662 4.76. Mechanism (k, u): not density, not interaction weight.
- My b2/b3 (11) still not run after ~1 h (queue). Plan once in: quadratic model in inner 9-D odd β → phase-only Newton step (clean beyond-M2 combo).

## wakeup 7 (13:02 UTC)
- b2 S1T1 odd line (s21): .13 1.4911 (r46 1.5183), .16 1.5705, .20 1.6513, .25 1.7151 — all PASS, still rising (concave).
  Submitted b2x: .32 .40 .50 .65 (ac0c, 6def, d521, e6dc), per-entry up to .217.
- b3 ascent (7) still not run.
- Records: h c662 α+β union STRONG 4.76/5.23/4.67; density controls (k) exclude density. ae: S2×T1 odd per-entry .03 → 1.687/1.989.
- g critique 9d4e (R amplified ~1/d² at d_sc=.1), p rebutted (d376). For e5d5: Δ r46 3.955e-4, Δ_LLL 1.749e-4 → Δ/Δ_LLL 2.26 (parent 1.38).

## wakeup 8 (13:30 UTC)
- 0494 (S1T1 odd .25) STRONG 1.7151/2.0660/1.8997. b3: grad .04 1.5822, .06 1.7100, .08 1.7149 (sp/Δ .055); bal .06 1.6932, .10 1.6558.
- KEY: phase-only s21 plateau ≈1.71–1.73 for 4 different directions (mine + s bfbb + ai 4461); r46/r56 keep rising.
  Posted result. Phase-only claim metric capped by s21 ≈1.72 → breaking it needs α (others cover α+β).
- work/tab.py tabulates my requests with sp/Δ and eg.
- g retracted 1/d² critique.
- Next: b2x (S1T1 .32–.65) tests whether plateau is flat/turns over. Then claim the best phase-only point. Then consider
  pivoting: e.g., which α direction raises the s21 limiting branch while keeping phase-only... or verifier role.

## wakeup 9 (13:58 UTC)
- b3 more: grad .04 r46 1.6853; .06 (9b78) r46 2.0644 r56 1.8997; .08 (4ab1) 1.7149/2.3690/2.1959 (STRONG candidate, conv pending);
  .10 FAIL (sp/Δ .11), .13 FAIL (.32). So s21 gate binds just past the plateau.
- CURIOUS: 0494 and 9b78 have r56 gap 4.92035e-4 vs 4.92033e-4 (5e-6 rel) and s21 within 0.3% — a phase-insensitive
  branch seems to set Δ at the plateau. Phase-only s21 plateau ~3.87–3.90e-4 W0 (R 1.70–1.73) board-wide (s bfbb, t 452c, ai, ae).
- Records now α+β: o f5f1 6.28/8.33/8.12 STRONG; Σ|β| cap binding (rep-dependent, t request 789e).
- Submitted b4 (16): ± odd-β along S2T1,S3T1,S1T2,S1T3,S2T2 (±.03) and S4T1 three odd combos (±.01) on top of 0494.
  Goal: does any phase direction lift the s21 plateau? If none → phase-only s21 max ≈1.72 is robust → post + abandon/close.

## wakeup 10 (14:29 UTC)
- S1T1 odd line end: .32 1.7310 (r46 2.3210, sp/Δ .048) PEAK; .40 1.6436 (r46 2.5913); .50 FAIL (sp/Δ .2); .65 FAIL.
- swarm-b cd55: coherent sin2δ phase STRONG 1.730/2.254/2.083, no shell profile lifts s21 ceiling ~1.73 (agrees with my ff14).
  swarm-ab claims T1+.5T2−.5T3 lifts to 1.88; b critiques as s21 MT artefact.
- Records now ~10 (av cos2δ+i sin2δ coherent at Σ|α| cap). Many agents done.
- Plan: wait for b4 (plateau gradient) + ac0c r56; then claim best phase-only point (4ab1 or ac0c), post closing
  result with coverage, consider `swarm done`.

## wakeup 11 (15:02 UTC)
- b4 plateau gradient: + sides flat ~1.72–1.73, − sides drop; S2T2 odd +.03 → 1.7903 (36a8) lifts. Posted result.
- Submitted b5 (6): S2T2 +.06/+.09 on 0494; combo with S1T2− & S4o1+; bases .20/.32 with S2T2.
- Board: records s21 ~14.5 (w rec-out), STRONG claims ~10 (av e0a8, s c325 noQ0). u: qmax-8 non-PSD issue for records.

## wakeup 12 (16:33 UTC)
- 36a8 (0494+S2T2 +.03): 1.7903 / r46 2.1412 → S2T2 lift is real on r46 too (base 2.066).
- b5: 18d6 (b.25+S2T2 .06+S1T2 −.03+S4o1 +.01) s21 1.8847 sp/Δ .093, r46 2.2367; 8468 (b.32+S2T2 .03) 1.8161/2.4189;
  9fee 1.8349/1.9159; d264 1.7712/2.2659; a75c 1.6802/1.6349; 1db3 FAIL.
- Submitted b6 (4) final bracket. Then: claim best phase-only point by min, post closing coverage, swarm done.
- Board records: STRONG ~13 (w 407a 13.93/13.26/13.79). Phase-only class tops out ~1.8–1.9 (s21-bound).

## wakeup 13 (17:05 UTC)
- b6: 806d 1.9056 FAIL (sp .12), f22e 1.9061 FAIL (.11), d17f 1.8523 P (r46 2.281), b44b 1.7457 P (r46 2.524).
- Phase-only s21 optimum ≈1.89, bound by splitting gate (ag 4df7 1.896 agrees; mailed ag). ff14 ceiling = T1-only.
- Waiting for r56 promotions (18d6, 8468, d17f, 36a8, ac0c, 4ab1 conv). Then claim + closing coverage + done.
- 17:35 UTC: r56 still pending for 18d6/8468/d17f/ac0c/36a8; 4ab1 done (1.7149/2.369/2.196). v critique: N_A=2 match insufficient — my candidates pass s21c N_A=3.
- 18:05 UTC: r56 promotions still queued for all 7 phase-only candidates (18d6 best s21 1.8847, r46 2.2367). Waiting longer before claim+close.

## wakeup 16 (18:58 UTC) — CLOSED
- r56 stuck >3h for 7 candidates. Posted closing result 10e5 (+ correction note on promotion counts: 39/11/10).
- swarm done posted. 57/500 evaluations charged. Loop stopped.
