# swarm-e notebook

Started 2026-10-14T05:19:59+00:00.

## 2026-10-14 wakeup 1 (05:25–05:30 UTC)
- Read the brief, theory doc §6.4, progress/40 + 46, the kdep_envelope API. Parent w1c: s21 Δ = 2.2586e-4, r46 2.4101e-4.
- Board: swarm-a = linmap (single product terms, |α|≤0.1, |β|≤0.05); swarm-b = jorbit, swarm-c = jointorb (both joint orbits, small steps).
- My niche: **family `sharpen`**: large-amplitude α (0.3–0.6), outer shells first. Hypothesis 20261014T052929.793Z_swarm-e_hypothesis_b483.
- Local proxy (work/proxy.py): M2^(k)/M2 at α=±0.6, single term: S1 0.95, S3/S4 ~1.1, S7–S16 1.35–1.7, S13/S19/S21 1.9–2.6. Independent of T1/T2/T3.
- Tools: work/gen.py `make([(spatial_q, momentum_q, alpha, beta), ...])` builds an input (solver-basis stars by |G|² key).
- Submitted stage 1: work/batch1, 30 reqs (10 shells × T1 × α∈{+0.3,+0.6,−0.6}).
- Next: read results; check whether R_gap correlates with M2^(k); then line scans / T2,T3 / combos; watch the g_cutoff truncation of large-α outer shells.

## 2026-10-14 wakeup 2 (05:46–05:55 UTC)
- sharpen stage 1: 30/30 FAIL. Product terms at |α|≥0.3 leave the Laughlin phase on every shell. R>1 points (1.17–1.95 at +0.3 outer) have split/Δ 0.33–0.45 and failed PES, so they are a competing non-Laughlin state. R_beyondM2 ≤ 0.18. Posted abandon 20261014T054935.793Z_swarm-e_abandon_8884 with a coverage block.
- Board state: joint orbits are the right coordinates. Leaders: comove P1 (swarm-i) 1.88 s21. chiphase (swarm-d) 2678 = |G|²9×T1 mirror-odd phase contrast, β_entry 0.0204: s21 1.61, r46 2.22. jorbit (b) phase classes r46 ≈ 1.39. MT rule (swarm-d): linear response is only α on mirror-even or β on mirror-odd directions; all ladder clusters are chiral.
- Herding: integrators l, p, r (3 surrogates); controls a, l, q; outer even T1 k, m.
- New family **outerodd** (hyp 20261014T055305.066Z_swarm-e_hypothesis_b369): mirror-odd phase-only on |G|²9/12/16 × T2,T3 (one odd direction per block) and on the 12-member shells (7, 13, 19, 21) × T1, with 3 resolved odd pairs each. β_rms ±0.05. work/orbits.py (joint orbits plus a numerical mirror y→−y); work/mk2.py; batch2 = 36 reqs submitted. Mailed swarm-d.
- My sign convention for |G|²9×T1 is opposite to swarm-d's.
- Next: read the results, then line scans of the responsive directions (stage 2). If T1 is responsive, extend the 12-member shells to T2/T3.

## 2026-10-14 wakeup 3 (06:15–06:20 UTC)
- outerodd stage 1 done: the 12-member × T1 resolved odd pairs are strong. Good sign = β>0 on the class with θ<90° (G-axis/R-axis angle), universal (matches swarm-b's rule).
  Best: |G|²7 o2/o4 1.679 s21 / 2.261 r46 (86b1); 7 o1/o5 1.593/1.821 (ce60); 13 o0/o3 1.466/1.847 (427e); 13 o1/o5 1.449/1.762 (6881); 21 o1/o5 1.184/1.580; 19 o0/o3 1.24/1.33; 7 o0/o3 1.415/1.451.
  Six-member outer × T2/T3: 12/12 FAIL at rms 0.05 (cliffs).
- Posted result 20261014T061913.915Z_swarm-e_result_05f7 (with coverage).
- Agreed split: swarm-m takes 12-member × T2/T3 odd and outer even × T2/T3; swarm-d keeps S5/S6/S8×T1 X and S2/S3×T2/T3 X; swarm-b does u1/u2/u3 phase combinations.
- Board: swarm-r ac14 (all five cross-family levers) s21 4.44 / r46 4.93 PASS. log R ≈ additive; s21 split/Δ is the binding gate. Controls (a, q): c5b8/f721 R_ctl = 0.999, so the gains are beyond the averaged density.
- Stage 2 submitted: batch3 (21): line scans of the top 4, combos, all-12 at 0.02, and u1 cross points. Tools: work/mk3.py good() builds a θ-oriented odd direction; orbits.multi() builds multi-shell blocks.
- Next: find the phase-only optimum (combine my 12-member levers with b's u1/u2/u3 and d's S5 X, check splitting). Watch r56 for the six promoted points.

## 2026-10-14 wakeup 4 (06:40–06:47 UTC)
- outerodd stage 2 (batch3, 21): line scans peak near rms 0.05 (G7 o2/o4 1.68), except G7 o1/o5, which peaks at 0.075 (1.63 PASS). Small steps at 0.025: 1.30–1.54 PASS, promoted. Most in-family combinations FAIL on s21 splitting (0.13–0.48).
  c6 (all 12 good pairs at 0.02) gives R 7.31 with a clean manifold but EG 0.19 at N_A=2, and FAILs N_A=3: the TRAP state. c9 (top4@0.05 + u1) 3.95 A→F, same signature.
- Trap note posted (20261014T064515.694Z_swarm-e_note_87bd): 8 board AMBIGUOUS points with R 2–8.5 all share EG<0.35 and FAIL at N_A=3. It is a 3-fold non-Laughlin state; treat EG<0.5 as FAIL in surrogates. Mailed p and k.
- Board: leaders are mixed α/β at R ~9–11 PASS (r b55a 10.9/11.4; h josobol; n trgrad). swarm-r claimed STRONG for ac14 (4.4/4.9/4.4/4.9). swarm-b claimed STRONG phase-only ec27 (1.15). swarm-k: ℓ=2 unification ∇lnR ∝ e^{2iθ_GR} (my θ<90 rule = sin2θ). swarm-p: phasex grand sums of my levers.
- New family ell2t (hyp 20261014T064516.453Z_swarm-e_hypothesis_3838): k's ℓ=2 field on T2 and T3, A λ {5e-4, 1e-3, 2e-3} and B λ {1e-3, 2e-3, 4e-3}; work/ell2t.py; batch4 = 12 submitted.
- Open: r56 for my 6 promoted outerodd points is still pending. Budget 120/500.

## 2026-10-14 wakeup 5 (07:07–07:11 UTC)
- ell2t batch4 (+λ, T1 sign rule, all 10 shells): T2 (pq=3) A 5e-4 0.991, 1e-3 0.888, 2e-3 FAIL; B 1e-3 0.885, then FAIL. T3 (pq=4) A 5e-4 0.873, then FAIL; B 1e-3 0.397 FAIL. No gain; A ≈ B at matched entry size, like k's T1 finding.
- swarm-d: the T3 phase sign flips relative to T1/T2 (S2T3, S3T3). Submitted batch5 (8): opposite sign, A λ −2.5e-4/−5e-4, B λ −1e-3/−2e-3, on T2 and T3.
- Split agreed with swarm-k: e = T2-only and T3-only fields; d = T1+cT3 mixtures; k = T1 shell profile and A/B angle.
- Board: swarm-a mechanism = restoring the weak V1 pair channel (e2 proxy, R² 0.97 r46). Claims STRONG: r b55a 10.9/11.4/11.2/11.4; i 9de1 P1. n audited the top 25: none is a trap state.
- My promoted outerodd points: r46 1.34–2.26 (also f46c G7 o1/o5 r075: r46 2.20); all r56 still pending (queue).

## 2026-10-14 wakeup 6 (07:31–07:35 UTC)
- ell2t closed (20 evals): T2/T3-only ℓ=2 field is no lever. Best 1.032 (T3 reversed-sign A λ=−2.5e-4, cc8d). Posted abandon 20261014T073333.711Z_swarm-e_abandon_b6dd with coverage.
- Board frontier: mixed α/β T1 chiral ℓ=2 field. k 3bd0 13.58/13.11; h c954 full ladder min 11.25; r b55a claim STRONG 10.9–11.4. Phase-only is capped at s21 ~1.73 by the splitting gate (b's note), with r46 up to 2.58.
- My scope is exhausted: product sharpening (null), outer odd phase (done, absorbed into k's ℓ=2 field), T2/T3 (null). Every remaining direction has an owner (k shell profile/A-B angle, d kprof, h/n/r optimizers, a e2guide, controls by a/l/q).
- Plan: wait for r56 (and conv46) of my promoted phase-only points (86b1, f46c, ce60, 427e, 6881, 2b54, 55c7, 2876, plus the r025s). If 86b1 qualifies, post a phase-only claim; then `swarm done`. Budget 107+8=~115/500.

## 2026-10-14 wakeup 7 (08:04 UTC): DONE
- r56 for all promoted points is still queued (>2 h). Claims are computed by the broker from the store, so there's no need to wait.
- The board has converged: k's STRONG chiral ℓ=2 claim (3bd0 13.6/13.1/13.1/13.3); n's chiral projection 12.94 min; i and m have finished.
- Posted final summary note; ran `swarm done`. 115/500 charged.
