# swarm-t notebook

Started 2026-10-14T10:24:56+00:00.

## 2026-10-14 11:30 — wakeup 1: scope chosen, batch 1 submitted
- Read docs (gen-space theory, pilot 40, precision 46) and full board. ~20 agents active; maps: swarm-a/b separable 60 axes,
  swarm-c jorb (joint orbits S1-S3xT1-T3), swarm-d chiral half-shells, swarm-e bigamp, swarm-f chiral-odd β,
  swarm-g joint-orbit channels, swarm-i kpow, swarm-l phase-even.
- Key finding (store data): joint-orbit slopes are huge (S1T1 ⊥ A −0.05 → 1.171; S3T1 δ0 A +0.05 → 1.217;
  S3T1 δ60 B → 1.249) and ADD linearly (S1T1 orbit slopes sum −1.26 = separable slope −1.26).
  Phase slopes obey MT rule: achiral δ (0, 90) B even; chiral ±δ B odd.
- Built work/orbits.py (decompose any block into (|G|²,|R|²,δ) orbit coords A+iB on cos·cos),
  work/orbspace.py (54-D coords S{1,3,4}xT{1,3,4}; to_input builds pair-star block), work/fit.py (diag quadratic, u=x/0.05).
  NOTE labels are squared norms: S3 = |G|²=3 shell (2nd shell). A = alpha_pair, B = 2*beta_pair.
- Posted hypothesis 20261014T113037.275Z_swarm-t_hypothesis_438b (family orbsurr, budget ≤200).
- Batch 1 (15): b1/ gradient line (mix |u|=.5..3; phase |u|=.5..2) and diag-Newton (f=.25..1). Surrogate predicts
  absurd 1.4–2.8 (additive) — the batch tests additivity. Mailed swarm-c.
- NEXT: collect b1 (python3 work/collect.py work/all.json; check my reqs via swarm status), refit incl. cross terms,
  watch r46/r56 for swarm-c ce1f (first at r46) — finite size is the real question.

## 2026-10-14 ~11:50 — wakeup 2
- Board exploded (58 posts). Herding: ~20 agents in S1/S2×T1 orbits. Surrogate owners: h stepped back, u abandoned,
  o stops after its 14-eval line → I keep the pooled surrogate (mailed o).
- Facts: leaders s21 ≈ r46 for S1×T1 (cluster-flat), |G|²=3×T1 leaders r46 6–12% HIGHER than s21 but at s21 use
  split/Δ 0.03–0.05 (gate 0.1) (swarm-u audit). Response is kinked (min over branches). swarm-e: full stars break
  manifold at |α|~0.1–0.2. Leaderboard top s21 1.64 (swarm-j perp-amp, swarm-q). swarm-f chiral-odd β S1T1 1.38–1.56.
- result.json via swarm show has no per-sector energies → branch-resolved modelling impossible; use min-of-quadratics.
- My batch 1 still queued at 11:50.
- NEXT: collect, fit min-of-K model on TL-active coords incl. split/Δ as a second response (gate constraint), step.
- work/collect.py now parallel+cached (cache/), pulls all leaderboard+own reqs, records split_rel, eg, verdict per cluster.
  work/feats.py: general orbit features any shell, label g{|G|²}r{|R|²}d{δ}{A|B}.
- s21 top (12:00): ⊥ g1r1d90A −0.45 → 1.639 (split 0.073, still rising; j/q); g4r1 chiral-odd B ±0.033 → 1.558 clean (f e5d5);
  g7r1 orbit contrast (h 353f) 1.572; g3r1 chiral-odd B ±0.033 → 1.483 (f 2e98). kpow 1.94 FAIL.

## 12:10 — wakeup 3: batch 1 still queued (broker overloaded; only 237 results visible board-wide, no multi-orbit combos yet)
- STRONG claim (swarm-c 893d): S2×T1 +60° chiral β=+0.03 (phase-only) 1.249/1.404/1.347 s21/r46/r56. u verified input.
- ⊥ α −0.45: 1.64/2.63/2.44 (swarm-j bdd3); s21 split gate is binding; r46 ≫ s21 along leaders (q 5bc6, y e222).
- swarm-k: matched-density control for α⊥ −0.05 gives R_ctrl 0.999 → density explains none of gain.
- swarm-at: g_cutoff 8 drops 7–9% kernel change for S9/S10 deformations; outer candidates need conv46.
- Implication for orbsurr: objective = min over clusters ≈ s21, bounded by s21 split/Δ < 0.1. Model split/Δ too.

## 12:55 — wakeup 4: BATCH 1 LANDED (mix track) — record
- Newton line f=.25/.5/.75/1.0: s21 1.89/2.80/3.77/4.82; r46 1.84/2.91/4.06/5.19; r56 3542 3.58. Grad line u=.5..3: s21 1.42→3.51 (f0fb r46 3.86 r56 3.44).
  All PASS, split/Δ ≤ 4e-3, eg ≥ 3.5. Superadditive (additive model predicted 2.85 at f=1).
- Posted result 20261014T125336.048Z_swarm-t_result_58e1 (incl. scale note: Δ_LLL tiny, near-zero-mode regime).
- Others: STRONG claims c 893d (phase S2×T1 +60), f 728b (phase |G|²=4×T1 chiral-odd 1.558/1.641/1.560), j 3d0f (⊥α −0.45 2.63 conv46).
  h un1 α+β union step 4.76 s21. k/u: gains not density/interaction scale.
- Batch 2 (10) submitted 12:52: b2/ rec_A{fa}_B{fb} scaling of 8c01 + rec_plus_grad3. Σ|α| cap 2.5 binds at f≈1.83.
- ph_ track (6) of batch 1 still queued.
- NEXT: find turnover; if still rising at cap, reallocate L1 budget (which orbits carry gain per |α|); request matched-density control for record (swarm-i queued for f0fb).

## 13:20 — wakeup 5
- 8c01 completed ladder: s21 4.816 / r46 5.186 / r56 4.551 / conv46 5.186, all PASS, C=1, broker claim 'strong'.
  Posted claim 20261014T131946.789Z_swarm-t_claim_4fb4 (abs Δ r46 1.25e-3, Δ/Δ_LLL 7.1). Mailed swarm-k for matched-density control.
- Phase-only track: 452c (ph grad u2) 1.727/2.221/2.035 PASS 'suggestive' (conv46 pending), s21 split 0.042;
  c82f u1.5 1.673/1.937; 1802 (ph newt f1) FAIL split 0.134. s21 split gate binds phase-only.
- Board context: h claim c662 STRONG 4.76/5.23/4.67 (same direction as 8c01, cos .91). k: density excluded for c662/353f/f0fb.
  ap: γ on uniform LL0 lowers gap → γ×ρ* cooperation. c: leaders restore static M2 law (R_beyondM2 .12→.72).
  g refutation: parent near-zero-mode at d_sc=.1, R amplified; p and u counter (contact inert). d_sc control requested.
- Batch 3 (6, phase-only) submitted: b3/ u·(ph grad unit) + d·(f's g4r1 chiral-odd B ±1/30), grid.
- Batch 2 (10) still queued.

## 13:48 — wakeup 6
- 8c01 density controls (swarm-k): 0.994/0.994/0.994 (⟨ρ_k⟩), 1.000/0.999/1.000 (M2-matched) → beyond-M2 by brief's def. Posted note a2b1.
- 452c phase-only completed: 1.727/2.221/2.035/conv 2.221 (STRONG thresholds). Phase-only s21 ceiling ~1.72 (swarm-f) — gate-limited.
- RECORD now swarm-o f5f1: s21 6.28 / r46 8.33 / r56 8.12 on diag-Newton line of 126-coord pooled fit, at Σ|β|=1.88/2.0.
  o line2 (α boost, drop low-yield β) and z CMA at f5f1 cover the frontier near the β cap.
- Filed request 789e: Σ caps representation-dependent (pair vs full stars) — asked human for a reading. Not regrouping meanwhile.
- My b2 (8c01 direction to Σ|α| cap, fA/fB scaling) and b3 (phase-only) still queued (~1h broker latency).
- IDEA next: L1-efficiency per orbit coord (gain per unit Σ) from data → allocate budget; but o does this. Consider pivot.

## 14:25 — wakeup 7
- Batch 2 (s21/r46): 6506 (A1.8,B1.8) 8.706/8.705; 7ec7 (rec+grad3) 8.08/8.32; c269 (1.5,1.5) 7.15/7.42; 8cd5 (1.25,1.75) 6.93/7.38;
  92d1 (1,2.5) 6.27/7.92; 6a69 (1,2) 6.22/7.21; 87b2 5.94/6.32; 99ea 5.72/6.25; d1e0 4.83/5.60; af07 (0.5,2) FAIL split 0.10.
  → monotone rising to the Σ|α| cap (6506 Σα 2.46). Small α with big β fails the split gate (α stabilises the manifold).
- Board: everything cap-limited (ae audit). av coherent cos2δ+i sin2δ on S1–S3×T1: s21 10.39 (e0a8, pair stars, Σα 2.34 Σβ 1.64) — more cap-efficient than mine.
  o claim f5f1 8.33 r46. w: outer cos2δ α adds linearly on c662. aa: g4r1 chiral-odd β adds on 8c01 (→6.32). al: C6 records are saddles vs r-nematic strain (+4%).
  Many agents done (d, g, p, q, aj, ae, ac, ak).
- Batch 4 (6) submitted: fill Σβ at Σα cap (A1.8,B2.4/2.9), + g4r1 chiral-odd B 0.1/0.2, rec+grad3×1.28.
- collect.py: 1391 requests now; takes ~10 min.
- NEXT: cap-efficiency analysis (R per Σ) across top points; candidate direction = av rule + outer shells. Await human on caps (789e).

## 14:57 — wakeup 8
- 6506 full ladder: 8.706/8.705/7.726/conv 8.705. 7ec7 8.08/8.32/7.39/8.32. c269 7.15/7.42/6.54.
- Batch 4 s21: b232 (A1.8,B2.9; Σα 2.46 Σβ 1.96) 10.499; 6627 (B2.4+g4o.1) 10.26; 91de (B1.8+g4o.1) 10.255; b3a8 10.20; 066f 9.91; 0b2b 8.73.
  → board-top at s21 (av e0a8 10.39 claimed STRONG 10.39/9.87/10.50/9.96). Ladder pending.
- Batch 3 phase-only: all s21 1.67–1.73 (ceiling). Phase lane closed for me.
- Board: x: outer T1 α triple (h 353f/8a8a/99f8) adds at c662 ≈5 R/unit Σα, lowers s21 split. s claim c325 noQ0 9.87/10.15/9.54 at 60% Σα.
  r: ⊥ ablation keeps 83–93% of c662/8c01. u: qmax-8 makes pair interaction non-PSD at R≈10 → watch conv46.
  ai also filed request on Σ cap chart dependence (7a14).
- Built work/merge.py (block-diagonal exact stacking, drop_momentum, scale). Batch 5 (6): b232 T1-projection (+ outer triple at 0.5–1.5, α rescaled to fit Σα, β to 1.18).

## 16:52 — wakeup 9
- Batch 4/5 ladders done. cbe3 (b232 T1-proj α.9 β1.18 + h outer triple) 11.697/11.723/11.651/conv 11.747 → min 11.65, spread 0.8%.
  9aed 11.76/11.68/11.56/11.70. 6627 10.26/11.27/10.91. b232 10.50/10.64/9.71. Posted result 1b31 (with coverage) + claim c989.
- Board best: av 55f9 (all-shell S1–S10 × T1 angular rule μ=0.04) 12.52/12.71/12.79/conv 13.0 at only Σα 1.35 Σβ 1.01 —
  2× more cap-efficient than mine. h claim 5063 min 11.65. e c577 min 11.38. an: above R≈12 some r46 FAIL; u: qmax ≥12 requested.
- Batch 6 (5): blends t·cbe3 + s·55f9 at caps. Mailed av (not scaling 55f9 alone) and k (control for cbe3).

## 17:25 — wakeup 10
- Batch 6 blends t·cbe3+s·55f9: s21 13.7–13.96 but r46 manifold FAIL (3 of 4 that reached r46); 21da/72e1 FAIL at s21. 6eae s21 13.96 / r46 10.93 at gate. Posted result.
- cbe3 class A (qmax-clean, u 4060); s21c N_A=3 eg 2.67. k took the cbe3 density control (…_014b).
- Board: most agents done. Frontier (class A, min-over-clusters): x 06bb 11.80, cbe3 11.65, h 5063 11.65. Class B (qmax-suspect, +2..20%): w 407a 13.26, av 55f9 12.51.
  z runs CMA on min-over-clusters (32-D). Human hasn't answered cap request 789e.
- Plan: wait (long interval) for cbe3 control + human answer; close family with done if nothing new.

## 18:15 — wakeup 11: closing
- cbe3 density control 0.992/0.989/0.990 → beyond-M2. Posted note.
- Frontier moved (av 023e min 13.46, aq/z 4792 min 14.37) via all-shell angular rule; most agents done; open items are human's.
- Posted final summary via `swarm done` with coverage. Loop stopped.
