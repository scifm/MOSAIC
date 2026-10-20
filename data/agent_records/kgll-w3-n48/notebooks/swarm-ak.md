# swarm-ak notebook

Started 2026-10-08T04:36:52+00:00.

## 2026-10-08 05:15 — wakeup 1 (orientation)
- Board: ~25 families. Lead = joint (G,R) C6 orbits on w3: S1xT1 perpendicular (swarm-i fa76, s21 1.1885 at orbit α=0.15)
  and S2xT1 parallel (fb45, s21 1.1785). Low shells S1-S3 x T1-T3 orbits are claimed by e, i, z, ad, s (CMA), o (Sobol).
- Unclaimed: joint orbits on high spatial shells S5(|G|²=9), S6(12), S8(16) [6-member; S6,S8 = w3's own shells]
  and 12-member S4(7), S7(13), S9(19), S10(21).
- Tools: work/geom.py (solver 120° geometry, lines, C6 sub-orbits), work/build.py (orbit_terms(sv,tv,sub,d,a,b) -> input),
  work/peek.py (swarm show + deformation summary). Builder reproduces fa76 (S1T1 d=1) and fb45 (S2T1 d=0).
- Geometry: S1,S3,S5,S8 lines at 0/60/120; S2,S6 at 30/90/150; T1,T3 at 30/90/150; T2 at 0/60/120.
- 05:25 Data read: separable atlas (b 5319, f d55c): every direction concave, curvature ~|G|² (c_α −21..−82); only α S1×T1, S2×T1 have slopes.
  Orbit leaders: fa76 S1T1⊥ r46 1.156; fb45 S2T1∥ r46 1.171; ad d746 gc-lock (S1×T1⊥ at orbit α=0.3) s21 1.36; w2 m ba45 S3T1⊥ s21 1.06 → r46 1.159 (!).
- Built 54-input S5/S6/S8 × T1-T3 orbit screen (work/phase1/, α=±0.03 orbit amp, all pass check) — NOT submitted:
  w, ah, ai claimed the same corner within minutes. Posted herding note 20261008T052529.041Z_swarm-ak_note_f0b5, mailed w/ah/ai.
- Role now: verifier/critic, budget reserved (0/500 used). Ideas to watch: w2 s21↔r46 discrepancy (Z3 selection rule, K ∈ s21 mesh) may
  hide w2 winners behind the s21 promotion threshold (1.02); check when w2 r46 data accumulate. If w/ah/ai consolidate and drop the
  S6/S8×T2/T3 orbits, phase1/ batch can be reused.

## 2026-10-08 05:52 — wakeup 2
- Board moved fast. w3 leaders now: au a61f (S2T1∥ orbit A≈0.3 + S9×T1 dressing) s21 1.569; aa xab (S2T1∥ 0.45 + chiral β S3) s21 1.52;
  e phase-2 plane ⟂×∥ best r46 1.41. w2: m ff48/816b ~1.11–1.15 (r46). All gains live on T1; T2/T3 negative everywhere (f, g, z).
- High-shell corner closed by w/ah/ai/al/ag (all achiral concave; collapse converged in g_cutoff). Chiral β on S4/S7/S9/S10×T1 gains (w, j, am)
  but r46≫s21 at both signs (k's critique) → r56 decides.
- ah replied: closed hishell after T1. Posted 2nd herding note 20261008T055148.676Z_swarm-ak_note_d113 (4 agents on w2 chiral-β×T1: ah, an, aq, av), mailed them.
- Still 0 evals spent. First-order map of the bounded space is essentially complete; nonlinear frontier optimisation covered by au, e, af, s, t, ap, aa, o.
  Next: look for a verification gap once r56 lands (parent r56 Δ still pending); keep budget.

## 2026-10-08 06:25 — wakeup 3
- w3 s21 leaders now R 2.8–3.3 (t 4a76/6191/3126, ap 2848): S2T1∥ amplitude + high-shell α dressing + chiral β ×T1. Checked diagnostics:
  all PASS, split/gap ≤1.3e-3, PES gap 4.2–5.2, adm ratio 0.61–0.84, M2k/M2 1.25–1.72, R_beyondM2 1.34–1.62. Nothing numerically suspicious at s21;
  the risk is the cluster dependence of large chiral content (ae refutation: r46≫s21 only at large total chiral amplitude). r46 queued; r56 stalled for
  everyone ~95 min (c request 8cff to human).
- w2 leader: b chidress-w2 8c39 s21 1.299 (chiral S7 dressing of m's d43f) — transfer of the w3 dressing mechanism.
- Herding note d113 accepted: an = line scans, b = cross terms, q = CMA, av = Z3 null; ah, aq closed.
- Reserve/verifier roles already offered by at, x, u. I stay in reserve (0/500 spent). Next: when r56 lands, audit the s21→r46→r56 sign
  consistency of the chiral-dressed leaders; possible targeted check = mirror-partner (−χβ) of a leader on r46/r56 if nobody runs it.

## 2026-10-08 07:04 — wakeup 4: done
- ≥10 agents in reserve/verifier mode (~4500 evals unspent); r56 still stalled; every in-box parameterization owned.
- Posted `swarm done` (20261008T070422.677Z_swarm-ak_note_2ea4) with coverage block (0 evals). Loop stopped.
