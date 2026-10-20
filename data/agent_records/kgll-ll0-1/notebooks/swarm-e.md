# swarm-e notebook

Started 2026-10-02T03:51:19+00:00.

## 2026-10-02 wakeup 1 (04:00Z)
- Read the brief, ADR-0040, doc 40 (024 pilot: +0.51% at 4x6 flips to −0.92% at 5x6), and doc 46 (Nk=21: w3 α[S1,T1]=+.05 gives +1.85%, w2 the same gives −5.05%).
- Board: swarm-a has `w3-atlas` (±0.02 single-axis, S1-8 x T1-3 x α/β, 96 req); swarm-c has `w3-wide` (CMA-ES on S1-4 x T1-2, box α≤.6, β≤.3). Both asked for w2.
- KEY: promotions are free, so the budget is screening only. The goal is a diverse set of s21 candidates with R ≥ 1.02; the ladder then tests them across clusters at no charge.
- Block = separable cos·cos only (inversion-symmetric stars), so γ is even in r and in k.
- Posted hypothesis `w2-map` (20261002T040359.864Z_swarm-e_hypothesis_ec08): w2 atlas ±0.03 (S1-8 x T1 α/β = 32, + α S1-3 x T2 = 6), then CMA-ES, then w2<->w3 transfer. Budget ~280.
- Tools: work/gen.py (make_input(parent, {(s,p):(α,β)})), work/atlas_w2.py writes work/batches/atlas_w2 (38 files). g_cutoff 6, n_mesh 48.
- Submitted 32 T1 atlas reqs (ids in work/batches/atlas_w2.ids). Pending: 6 T2 files in work/batches/atlas_w2_T2. Wrote work/cmaes.py (resumable CMA, maximize, reflect bounds).

## wakeup 2 (04:29Z)
- 18 agents are active. The w2 atlas is triplicated (f = α ±0.02 S1-8 x T1-3, b = β ±0.02, me = T1 ±0.03). Dropped my T2 batch. r = w2-synth (local Newton |c| ≤ .15), g = w2-orient α-X, j = w2 β-chiral.
- Symmetry (notes from i and l): MT/MK-even, so a linear gap response is physical only for α on star×star / achiral modes and for β on chiral (joint-orbit) modes. β star×star odd parts are cluster-chirality artefacts (s21 has C6 only, r46/r56 C2 only), so treat my β ±0.03 as the artefact floor.
- Aliasing: only T1, T2 are clean on all ladder meshes (s21: T5,T6 ≡ T2; r46: T3 self-aliased).
- Truncation (note from n): g_cutoff 6 loses up to 13% of the kernel for S4 at |α| 0.6. Use g_cutoff 10 for wide boxes. The human fixed conv46 to max(req, 10).
- Posted revision note 20261002T042943.311Z_swarm-e_note_5d4c. CMA plan: α-only on S1..S8xT1 + S1..S3xT2 (11-D), |α| ≤ .4, g_cutoff 10. Waiting for atlas slopes (mine, plus f's) to set the mean/σ0.

## wakeup 3 (04:56Z)
- Atlas done, 32 PASS. α slopes: S1 −.71, S3 +.91, S4 +.55, S7 −.99, S8 −1.31. β odd parts ≤ .05, all concave. Best 1.0137. Posted result 20261002T045858.770Z_swarm-e_result_032e (with coverage).
- Board breakthrough on w3: the amplitude gradient lies on joint orbits S1T1⊥ and S2T1∥ (h, k). c's S2T1∥ far ray reaches 1.52 (s21), and o/968b 1.61 s21 / 1.71 r46. w2 best is r/w2-synth chiral-β at 1.077.
- p: S1T1⊥ is half Q=0 (static coherent LL mixing, pinned-out channel). S2T1∥ is LL-mixing-free.
- Found that R_staticM2 is just R/1.450 (a constant) on w3 s21. Use ρ = R·M2*/M2^(k) instead. c's 776c has ρ 1.04/0.97 (density at work); o's 968b has ρ 1.45/1.54 but carries S1T1⊥. Posted critique 20261002T045950.309Z_swarm-e_note_3494, proposed an ablation, mailed o and c.
- DROPPED the star-α CMA (star directions average out the orbits; diagonal Newton ~6%).
- Submitted 18 w2 orbit rays (work/orbit.py, batches/w2_orbit_rays.ids): S2T1∥ and S1T1⊥ at ±.1, ±.2, ±.35, ±.5, plus 2 combined; g_cutoff 12. Geometry verified identical to c/776c.
- Next: read the w2 rays. If S2T1∥ is positive on w2, refine (line + combine with w2 chiral β from j/l/r). Consider the 968b ablation if o/c decline.

## wakeup 4 (05:21Z)
- The w2 orbit rays are a null at both signs (best .968; S2T1∥ ±.5 FAIL on manifold). This agrees with f's w2-far. Posted result e6ea and abandon 0f50 (w2-map: 50 evals).
- n refuted my ρ (static M2 doesn't predict R: frozen slices .61/.92). Withdrew it publicly. o's b2 shows the beyond-density part survives without S1T1⊥.
- w3 board: LL-free α(S2T1∥) + chiral β reaches s21 2.4-2.6 (o, p, m). Heavy herding on w3 combos; w2 is covered by g, b, r, j, l.
- NEW family `w3-phase-only` (hyp 20261002T052253.143Z_swarm-e_hypothesis_6e5e): β patterns of cc86 and bd1a with α=0, at ×1, 2, 3, −2 (work/phase_only.py, batches/w3_phase_only.ids). Clean beyond-M2 if positive. Prior phase-only best: d/2400 s21 1.036, r46 1.08, r56 1.056 (suggestive); d/0f55 r46 1.23.
- Budget: 58 charged.

## wakeup 5 (05:44Z)
- Phase-only b1 (α zeroed): cc86-β ×1 0.885, ×2 0.300; bd1a-β ×1 0.689; ×3 gives non-Laughlin large-Δ states (F). So the leaders' β gain is an α×β interplay; they are amplitude winners for claim 2. Posted result 20261002T054451.245Z_swarm-e_result_cf2e, mailed o and p.
- d gave 4 live w3 chiral-β modes: (|G|²,c) = (7,2) +1.32, (13,0) −.90, (19,1) −1.22, (21,2) +1.51 (unit Frobenius, γ = i b X). Copied d's chiral.py to work/chiral_d.py; built work/pcma.py (init/ask/tell; box ±.3; g_cutoff 12). Verified the (7,2) mode at .08 reproduces d/0f55 exactly.
- Waiting for d's 4-mode gradient line (Frob .04-.14) to centre the CMA. Asked d for its ids.
- Other news: n's static yardstick gives R_static = 1+0.193(M2−M2*), ≤1.50; bd1a r56 2.567 (w3 r56 is in!); f flags k/13f5's gain as S2T2⊥ (half Q=0).

## wakeup 6 (06:06Z)
- d's 4-mode gradient line (ĝ = .52 C7, −.36 C13, −.48 C19, +.60 C21): t=.04 1.021 (r46 1.242), .07 .867, .10 .616. The modes interfere destructively; the best single mode is C7 at β .06-.07, s21 ~1.054. d/2400 is CLAIMED robust_positive, phase-only (conv46 1.076).
- r's critique: phase-only works on w2 (e064 +7.5%/+20%). Accepted the scope (cf2e covers the w3 leaders' α-tuned β only).
- Claims on the board: p/cc86 STRONG provisional (2.40/2.47/2.46/2.47); o/bd1a STRONG provisional; d/2400 robust_positive phase-only. n: the M2-matched static reaches cc86 at 1.42, so the leaders are ~30% density.
- Launched phase-only CMA gen0 (m0 = C7 .065, σ .02, λ 8, seed 1; state work/pcma_state.json; ids batches/pcma_g0.ids). Objective: s21 R. Treat FAIL as 0.5×R or worse.

## wakeup 7 (06:28Z)
- CMA gen0 (s21): 1.023, 1.023, 1.046, 1.043, **1.0495** (C7 .066, C13 −.006, C19 −.016, C21 −.005), 1.042, 1.035, .980. r46 1.08-1.28 (f: parents' r46 gap is 4.1% low, so r46 R is boosted ~4%; r56 is binding). Gen1 submitted (σ .016, m ≈ C7 .065).
- Board: w3 leaders keep stacking orbits (h fea3 s21 2.80 / r46 3.59; k Q0-free T2 betas +0.24). p's w3-sobol is a global map. n: static M2-matched gives 1.49-1.57 vs leaders 2.7-3.6. o: β gain is sign-locked to α∥ (bilinear).

## wakeup 8 (06:50Z)
- CMA gen1 s21: best 1.0549 (g1_06: C7 .070, C13 −.016, C21 −.015), plus 1.053 and 1.0495. Plateau ≈1.055 = d's single-C7 peak; the other modes add ≤ .002. Gen2 submitted (σ .014). If gen2 doesn't beat ~1.056, close w3-phase-only with coverage: the phase-only ceiling on w3 at s21 is ~1.055.
- T2 chiral β at the parent was already found dead (h, i, l), so I skipped it.
- c claimed 776c STRONG (amplitude only, r56 1.499), and is careful about claim 2 (static 1.28/1.29). No critique needed.

## wakeup 9 (07:12Z)
- CMA gen2 best 1.0521, below gen1's 1.0549, so it has converged to the single-C7 basin. Closed w3-phase-only: result 20261002T071318.720Z_swarm-e_result_cbb9 (coverage: 32 req). r56 for my points is pending (free). d/e25f r56 1.119 means a phase-only w3 STRONG is plausible for d.
- Zero-cost verification (work/mt.py): all 66 claimed points are exactly MT-invariant, so R_C(x) = R_MC(x): no chirality artefact at any order. Only m's w3-E probes are MT-odd. Posted note 20261002T071529.044Z_swarm-e_note_e388.
- Budget 90/500. Board mature: STRONG claims on both parents, phase-only claims on both. Herding on leader stacking (b, k, h, r, g on w2; o, p, h, k, d on w3).
- Options next: (a) stay as verifier at slow cadence; (b) a joint optimizer in the full C3-symmetric MT-even orbit basis (60-D T1+T2) — too high-D for the remaining value. Leaning (a), then done.

## wakeup 10 (07:46Z)
- Phase-only w3 now has STRONG claims (d e25f/3ea2, o 84e4). My CMA points are still awaiting r56.
- Re-ran the MT check on the 17 new claims: all invariant.
- Built work/audit.py → work/audit.md, a 98-claim audit (R per cluster, eg, split/Δ, Chern, S ratio, MT). Top tier R>3: split/Δ 4-9% (p/9fc9 8.7e-2, k/cd46 7.4e-2). Posted note 20261002T074855.783Z_swarm-e_note_e71b, mailed k and p.
- Correction 3600: the split ≤ 1e-2 tier tops at cc86 2.40 (w3) and r/509c (w2).
- Budget 82 charged (the digest number). Verifier mode. Next: re-run audit.py when r56/conv46 land; answer mail; consider `swarm done` when the board quiets.

## wakeup 11 (08:20Z)
- Quiet. p confirms the 9fc9 ridge ends at the r46 split gate (agrees with e71b). f, j and o have posted final summaries. My CMA r56 legs are still queued. Waiting for them before swarm done.

## wakeup 12 (08:50Z) — DONE
- Withdrew 22 redundant phase-only replicas (kept 8bb0 and 0acd). Posted final summary via swarm done. 82/500 charged.
