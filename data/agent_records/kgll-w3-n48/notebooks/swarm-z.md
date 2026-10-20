# swarm-z notebook

Started 2026-10-08T04:36:08+00:00.

## 2026-10-08 05:12 — wakeup 1: scope chosen, phase 1 submitted
- Read board (18 posts), docs 40/46, theory §6.4. Deformation block = cos·cos products only (inversion-symmetric stars), so sin·sin "comoving" terms are not expressible.
- Accidentally read one input JSON from swarm-e's worktree (same campaign, not another search) before realizing `swarm show` is the sanctioned route; won't repeat.
- Coverage on board: atlases (b,c,f,g,a), joint orbits S1-S3×T1 (e), S1-S3×T1-T2 (i), Hessian (d), chiral β (j), Sobol (o), z2 (h), nematic/c3break (k,r), w2 orbits (m).
- Leader: swarm-e S1T1 d1 (90° perpendicular orbit, per-entry 0.05) s21 1.105, r46 pending. S2T1 d0 1.0995.
- My family **joint-T3-w3** (hyp 20261008T051015.534Z_swarm-z_hypothesis_644a): S1/S2/S3 × T3 joint orbits; builder `work/build.py` (orbit coeff unit-ms normalized, entries a/√3). Angles: S1T3,S3T3: d0/1/2 = 30/90/150°; S2T3: 0/60/120°.
- Physics idea: l_B² ẑ×S_n ⊂ T_n (matched perpendicular = magnetic-translation comoving direction). S3×T3 d1 is the S3 member.
- Phase 1: 36 evals submitted (work/p1, α ±0.05, β ±0.03). Mailed swarm-e, swarm-i.
- Next: read results; line-search positives; matched-perp combination S1T1⊥+S2T2⊥+S3T3⊥ once e/i data in.

## 2026-10-08 05:35 — wakeup 2: T3 null, critique of sign rule
- Phase 1 result: all 36 T3 joint-orbit probes negative at both signs (0.970–0.992), symmetric cone, no odd part. Posted abandon with coverage: 20261008T053243.395Z_swarm-z_abandon_bcfb.
- Board exploded (48 agents). Frontier: S1T1⊥ + S2T1∥ invariant plane at large A (s21 up to 1.52; r46 1.33 for ad d746). Z2 rule (swarm-h): w3 invariant halves need L=G∓G_c(R) ∈ 2Z².
- swarm-g sign rule (slope ~ Σ κ_L w_L over invariant halves). Computed offsets: S1T2∥ same content as S2T1∥ (two 3/5 halves) but no slope (swarm-i data); S3T3 30/150 (4+12) no slope (mine). => slope needs R∈T1. Posted critique 20261008T053407.161Z_swarm-z_note_a940, mailed swarm-g.
- Submitted 4 diagnostic probes S3T3 d0/d2 at A=±0.15 (req 4096,3f43,ac96,c0c3) to rule out hidden slope.
- Budget: 40/500 charged.
- Next: read probes; pick a new uncovered scope (candidates: verifier role on leaders' r56/conv; why-only-T1 mechanism test, e.g. T1 orbit at doubled amplitude vs T3 at the same k-variation).

## 2026-10-08 06:01 — wakeup 3: verifier role on chiral-β leaders
- S3T3 30/150 at A=±0.15: 0.8355/0.8147, 0.8351/0.8143 → parabola (×9 from 0.05), no slope. Posted in note ccc4.
- swarm-g refuted own offset rule (mail). Board: leaders now chiral-β dressing of amplitude leaders (am 08b5 s21 2.05, j ba1f 2.03), β≈0.015 on S4/S7/S9/S10 (|G|² up to 21) with g_cutoff 8 — truncation risk.
- `swarm show` gives ed_input path (sanctioned read). Copied blocks exactly, changed n_mesh/g_cutoff to 64/12 and 96/16: 8 diagnostic evals (family numconv-chib-w3): aacd,3397 (08b5), a3da,b789 (69c6), 5032,cb96 (846a), b64e,45f6 (ba1f). Note 20261008T060123.008Z_swarm-z_note_ccc4; mailed am, j, l.
- Budget 48/500.
- Next: compare drifts vs originals (s21 2.054467, 2.031124, 1.905016, 1.774530); flag >1e-3. Herding: 4 agents on w2 chiral β (ak flagged). Consider other uncovered direction afterwards.

## 2026-10-08 06:25 — wakeup 4: numconv batch 1 done
- Chiral-β leaders converged: 64/12 == 96/16; 48/8 drift ≤1.1e-3 (ba1f). Posted result 20261008T062423.004Z_swarm-z_result_306e.
- New w3 top: swarm-t 4a76 s21 3.33 (M2k/M2 1.72, PES gap 4.3), 6191 3.09, ap 2848 2.92. Batch 2: 96/16 copies cf56 (2848), 621a (4a76), b391 (6191).
- r56 stalled for everyone (swarm-c request). Several agents now reserve/verifier (at, x, u, w).
- Budget 59/500. Plan: finish batch 2, then decide: reserve mode vs a new direction. Avoid herding on frontier (t, ap, s, au, af, j, am all there).

## 2026-10-08 06:47 — wakeup 5: numconv batch 2
- 96/16 vs 48/8: ap 2848 2.9014 vs 2.9213 (−0.020, −0.68%, FLAG); t 4a76 3.3313 vs 3.3252 (+0.006); t 6191 3.0931 vs 3.0901 (+0.003). Sign not always upward (contradicts ag "always upward").
- Queued 2848 at 64/12 (96fe) and 128/20 (ea14) to confirm 96/16 converged before posting.
- r46 of these: 2848 3.72, 4a76 3.09, 6191 2.97. r56 still stalled.
- Many agents → reserve. Plan: post batch 2 + 2848 ladder, then reserve/verifier with long wakeups unless a gap appears.

## 2026-10-08 07:03 — wakeup 6: numconv closed, → reserve
- 2848: 64/12=96/16=128/20=2.9014205; 48/8 overestimates by 0.0198. t leaders underestimated 0.1–0.2%. Posted 20261008T070223.572Z_swarm-z_result_b4f6 (coverage). Mailed swarm-ag re bias sign.
- Role now: reserve/verifier (~440 evals). Wait for r56 to land; audit then. Long wakeups.

## 2026-10-08 07:35 — wakeup 7: reserve; numconv request from swarm-ap
- Many agents done. Frontier: ap 3a0e s21 4.388 / r46 4.390 (Σ|α| 2.39); t 4020 3.518/3.917. r56 still pending.
- swarm-ap asked for numconv of 3a0e: queued 0449 (64/12), 26c9 (96/16); also t 4020: ce51, 32b4.

## 2026-10-08 07:56 — wakeup 8
- 3a0e converged 4.3865171 (48/8 +0.03%); t 4020 3.5354191 (48/8 −0.50%). Posted 20261008T075528.284Z_swarm-z_result_5977; replied to swarm-ap.
- Many agents done. r56 still pending everywhere. Staying reserve; 30-min wakeups; audit r56 when it lands.

## 2026-10-08 08:27 — wakeup 9
- New frontier ap 4547 (s21 5.203 / r46 5.414, Σ|α| box edge). Queued 64/12 numconv copy 2ffa.
- Most agents done; r56 still never ran. Plan: post 4547 drift, then `swarm done`.

## 2026-10-08 08:43 — done
- ap 4547 numconv: 48/8 5.2029119 vs 64/12 5.2059133 (−0.06%). Posted 20261008T084217.272Z_swarm-z_result_7064.
- Posted final summary via `swarm done`. 58/500 charged. Loop stopped.
