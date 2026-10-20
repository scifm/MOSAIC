# swarm-p notebook

Started 2026-10-14T05:20:37+00:00.

## 2026-10-14 05:45 — wakeup 1 (orientation, scope)
- Read the docs (40, 46, theory §1–2, kdep_envelope.py) and the board: 17 posts. Families: a linmap, b jorbit, c jointorb, d chiphase,
  e/f/h large-α (identical inputs → shared evals), i comove, j phasequad, k outerjo + m outerorb (both outer-shell orbits!),
  o nematic E2; controls: a mdctl, l mdens (+integration), q m2ctl.
- Key data (s21): P(|G|²=4)×T1 c=−0.06 1.3676 (c_f721); P(1)×T1 c=−0.06 1.2022, r46 1.2044 (c_c5b8);
  S3×T1 orbit2 +β(Im c .0577) 1.2525 / its MT partner 1.2444 → chirality artifact small; −β 0.46 → strongly odd.
  Large outer-shell α (product) gives R 1.2–1.9 but FAIL (manifold split 0.43, PES no separation).
  S3/S4 product terms are cliffs (a's note). s21→r46 transfer good so far for S1×T1 orbits.
- I had built the outer-shell orbit map (work/o1, 36 files) but k and m claimed it minutes earlier → NOT submitted.
- Chose family `poolbo` (hyp 20261014T054512.177Z_swarm-p_hypothesis_84c2): pooled GP surrogate in joint-orbit coords,
  B0 pairwise interaction probes (~10), B1 GP+PASS-classifier batches (~100), B2 transfer. Mailed swarm-l to split work.
- Tools: work/pool.py (pool all leaderboard requests → work/pool_cache.json), work/canon.py (cos·cos coefficients:
  Re c = α_entry for pair blocks, Im c = 2β_entry), work/orbits.py (joint-C6 orbits + mirror partner), work/orbit_id.py,
  work/table.py, work/build_outer.py.
- Next: re-pool once maps land; design B0 combos among top PASS directions (P4×T1−, P1×T1−, (3,1) self orbit +, (3,1) A+B α−, best β).

## 2026-10-14 06:07 — wakeup 2 (pivot)
- Board exploded: r xsector ac14 = 5 levers at small step (P(1×1)−0.06, P(4×1)−0.06, self(3×1)+0.06, X(3×1) β, X(9×1) β)
  → s21 4.44, r46 4.93 PASS (r56 pending); t=0.5 version e317 2.66. Roughly log-additive (product of singles ≈3.9).
  i: P1 line monotone to c=−0.5: s21 1.88 / r46 2.65; n: trust region at P1 −0.5 (s21 up to 2.88).
  d: S5T1 X β+0.05 phase-only 1.61 s21 / 2.22 r46. g: gain tracks Berry-curvature flattening (phase is separate mechanism).
  Large product / outer orbits at rms 0.1: cliffs, all FAIL (a, e, f, h, j, k).
- swarm-r's xsector = my poolbo, further along → folded poolbo into xsector (mail to r). Noted: every α_even ⊕ β_odd point is
  MT-invariant (c on (G,R) → conj(c) on (MG,MR)), so mirror-partner checks are redundant there.
- Offered r to run surrogate sub-batches from my budget. Asked k and m whether they take outer shells × T2/T3 even α.
- Built work/o2 (72 files): outer shells |G|²=7..21 × T2,T3 (|R|²=3,4), mirror-even orbits, amplitude ±rms 0.03 (unit-rms over cells).
  NOT submitted yet — wait for k/m replies.
- work/pool.py is slow (one `swarm show` per request); run it in background.

## 2026-10-14 06:25 — wakeup 3 (family phasex)
- ac14 now r56 4.43 PASS (s21 4.44, r46 4.93). Leaders s21 10.9 (r b55a), 9.1 (r), 6.8 (h josobol).
- m took outer × T2/T3 → dropped work/o2. l leaves integration to r/n/h; l owns ρ̄ controls.
- r suggested I take the phase-only cross-family combination → family `phasex` (hyp 20261014T062428.922Z_swarm-p_hypothesis_0114).
- work/levers.py → work/levers.json: lever cells pulled from source requests (b ba6c/18e0/b857/c6d3, d 2678, e 86b1 ce60 55c7 427e 6881 2876 2b54).
  work/build_px.py: combos; block() with Re c = α_entry, Im c = 2β_entry; round-trip verified.
- PX1 submitted (11): grand(10 levers) t=.15,.25,.35,.5,.7 (72c8 27bf 437a f7fd 702a); inner(u1,u2,S5X) t=.7,1 (3927 520d);
  outer(7 e-levers) t=.35,.5 (3be6 f59c); grand w/o u2 t=.35,.5 (ab4c 2930). Log-additive prediction grand: 1.75,2.6,3.7,6.5,14.
- Watch: s21 split/Δ gate (binding); r56 for phase levers (none yet).

## 2026-10-14 06:43 — wakeup 4 (PX1 results)
- PX1: only grand t=0.15 PASS (72c8 s21 1.637, split .042, now on r46). Others FAIL on s21 split (coherent add);
  t=0.35 R 0.055 (split 16); t=0.7 702a R 6.86 clean manifold but PES EG .20 / N_A=3 none → competing phase.
- b: phase-only s21 ceiling ≈1.73 (pinned s21 level), r46 keeps rising (to 2.58). k ell2: all orbit slopes ∝ e^{2iθ_GR}
  (corr .995) → levers ≈ one field; k line-scans the unified field (covers my grand line). Closed grand line.
- Claims: b STRONG phase-only ec27 (1.15 all clusters); r STRONG ac14 (4.44/4.93/4.43/4.93), D1 control .998.
  Leaders b55a s21 10.9 / r46 11.4 (EG ~3.5 healthy), h 53df 8.75/9.42.
- Posted result 20261014T064252.571Z_swarm-p_result_ecb2 with coverage.
- Spent 11/500. Next PX2: wait for m (12-member odd β × T2/T3 rms .02) and d (S2/S3×T2/T3 ±.015); test whether adding T2/T3
  phase to the capped points (b 18e0, 3e85) lifts s21 above 1.73 with PASS. If not, close phasex.

## 2026-10-14 07:05 — wakeup 5 (close phasex; reserve role)
- d's data answers PX2: T3 odd phase has opposite sign and lowers s21 when added to S5X; T2 = T1 sign. No cap-breaking.
  → posted abandon 20261014T070504.689Z_swarm-p_abandon_a2aa. 72c8: r46 2.103 PASS, r56 running.
- Board: r STRONG b55a 10.91/11.39/11.16/11.42; h c954 s21 11.33; a: e2 (2nd two-particle eigenvalue) predicts R (R² .97 r46);
  f: interaction moved into Pauli-surviving channel; j: transfer κ, r46 is the high outlier, r56/s21 conservative.
- Checked j's "conv46=r46 to 1e-6": actually 6e-5 (ac14), distinct hashes; parent Δ identical because Gaussian kills q>8. Mailed j.
- Spent 11/500. No unclaimed direction with clear value right now. Role: reserve — r accepted my offer to run xsector
  sub-batches; wait for mail. Long wakeups (30 min).

## 2026-10-14 07:40 — wakeup 6 (verifier: kconv2)
- New leaders: k's chiral ℓ=2 field λe^{+2iθ_GR} on S4–S10×T1 (c55d s21 14.74; 3bd0 13.58/r46 13.11); n trgrad 3f5f 14.70.
  h c954 full ladder min 11.25. Claims: i STRONG P1 9de1. k & h asked the human: Σ|α| is representation-dependent.
- i's critique: outer-shell field kernel tail 2.5% (λ .008) → 13% (λ .02) outside screen box, 6% outside conv46 box.
  f's kconv only covered inner leaders. → I took kconv2: --diagnostic s21 copies of top-5 (c55d, 3f5f, f5f3, 0d7f, 5a1c)
  at n_mesh/g_cutoff 64/10 and 96/14 (work/kc, 10 files). Submission running in background (swarm check at 96/14 is slow).
- kconv2 results (07:58): 64/10 = 96/14 to 1e-6; vs 48/8: c55d −0.27%, 3f5f +.02%, f5f3 +.01%, 0d7f −.09%, 5a1c +1.24%.
  Finite size: c55d r46 10.25, 0d7f 12.58, 5a1c r46 7.20 FAIL (split .238) → large-λ outer fields have r46 < s21.
  Posted result (critique-type) with coverage. Budget 21/500. k STRONG 3bd0 13.58/13.11/13.10/13.30 (D1 1.007).
  Mechanism consensus: e2 pair channel (a, reproduced by g); flattening falsified (g); w1c-specific (q, c).

## 2026-10-14 08:30 — wakeup 7
- Board converging: k's critique — all 40 strong claims are one chiral E+ ℓ=2 field on T1. n STRONG 2fb9 (E+ + negative
  ℓ0 breathing on S1/S3): 15.47/14.59/14.27/14.70. n's new s21 tops 8f40 17.43, d130 16.73, 2bd5 16.38 (M2k/M2 ~1.1).
  Many agents done (c, e, f, i, j, m). a: e2 explains R inside the phase, e3 separates PASS/FAIL (AUC .965).
- Submitted 3 more kconv2 diagnostics at 96/14 on n's 8f40, d130, 2bd5 (work/kc2). After they land: post, then likely `swarm done`.
- 08:50: kconv2 wave 2 done: 8f40 +0.07%, d130 +0.01%, 2bd5 +0.02% at 96/14; posted. Budget 24/500. Wrapping up with `swarm done`.
