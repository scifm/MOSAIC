# swarm-e notebook

Started 2026-10-08T04:34:45+00:00.

## 2026-10-08 wakeup 1 (05:00 UTC)
- Read charter, docs 40/46, theory §5–8, kdep_envelope.py. Board had only swarm-c's atlas-T1-w3 (separable single-term, all 10 S × T1).
- Chose family **joint-pair-w3**: pair-resolved C6-covariant (G,R) couplings. Pairs {±G},{±R} ordered so C6 = cyclic shift;
  shift d couples G_i with R_(i+d). S1×T1: d=1 ⟂, d=0 +30°, d=2 −30° (chiral). Separable star = c0=c1=c2=α_star/3 (checked: same M2k).
  Builder: work/build.py (`classes(shell,mshell,{d:(α,β)})`, `write(parent, entries, path, g_cutoff=8)`).
- Hypothesis post 20261008T045909.312Z_swarm-e_hypothesis_0393 (budget ≤180).
- Phase 1 submitted: 30 reqs (work/p1, ids in work/p1_ids.txt): S1T1,S3T1 all d × {α±0.05, β±0.03}; S2T1 α only.
  Pending: work/p1b (S2T1 β ±0.03, 6 files) — submit when slots free.
- Next: read results, compute per-shift slopes, compare with swarm-c separable atlas; chiral asymmetry c0−c2.

## wakeup 2 (05:19 UTC)
- Phase 1 results (s21): only S1T1 d1 (⟂) α+0.05 → 1.1050 (56da, r46 1.0879) and S2T1 d0 (∥) α+0.05 → 1.0995 (be47, r46 1.0919) are positive.
  α−0.05 on these: 0.833 / 0.839 (linear). All other shifts (incl. chiral d0/d2, all S3T1) negative at both signs = cone.
  Matches swarm-h half-translation selection rule (invariant: m≡R2, n≡R1 mod 2) and swarm-j M·T rule. My chiral idea: refuted.
- Swarm: ~48 agents, heavy herding on joint orbits. swarm-i orbit normalization a = √3·c; their S1T1⊥ a=0.15 → s21 1.1885, r46 1.156.
  swarm-ad GC-lock (S1T1/S2T2/S3T3⊥ up to large α), swarm-s robust CMA 18-D, swarm-t GP, swarm-ab/p matched-density controls.
- Posted result 20261008T051856.737Z_swarm-e_result_ecc5. Mailed h, m, i.
- Phase 2 submitted (work/p2_ids.txt): plane c⊥(S1T1) × c∥(S2T1) ∈ {0.05..0.2}² + (0,0.15),(0,0.2),(0,0.3),(0.3,0). (0.3,0.3) out of bounds (M2k 3.48).
  Also S2T1 β ±0.03 (work/p1b_ids.txt).
- Spent: 56 charged.
- Next: find the ridge in the plane; watch r46/r56 transfer; consider adding S5T1⊥-type invariant terms (higher shells) or β on invariant combos.

## wakeup 3 (05:42 UTC)
- Phase 2 plane landed: ridge c⊥+c∥≈0.2 favouring c∥. Best r46 ≈1.41: c3f0 (0,0.2) s21 1.452/r46 1.413; 7722 (0.05,0.15) 1.421/1.410; fbb9 (0.05,0.2) 1.454/1.408.
  (0,0.3) a7c2: s21 1.505 but r46 1.364 (finite-size drop grows w/ amplitude). Strongly sub-additive.
- S2T1 β ±0.03 all d: negative (0.96–0.99). 
- Posted result 20261008T054156.195Z_swarm-e_result_b1c4. Mailed af (duplicate plane-w3), ab (mdctl request for c3f0, 7722).
- Phase 3 refinement submitted (work/p3_ids.txt): c∥∈[0.175,0.25], c⊥∈[0,0.075], 11 evals.
- Board context: swarm-ad gc-lock S1T1 A=0.3 orbit s21 1.362/r46 1.334; swarm-w chiral β S4T1/S7T1 r46 jumps (cluster-specific per swarm-k).
  swarm-ao: S1T1⊥ on uniform LL0 lowers gap -> gain needs w3's S3 harmonic.
- Next: r56 values for plane points (the decider); refine; then maybe add third ingredient (phase dressing / higher-shell invariant) on top of ridge.

## wakeup 4 (06:05 UTC)
- Phase 3 refinement: plane saturates at r46 ≈1.42 (d888 (0,0.225): s21 1.494/r46 1.420; c89f (0.025,0.2): 1.470/1.419). r56 pending everywhere (bottleneck).
  s21-r46 drift grows with c∥ (s21 overestimates at c∥≥0.2). Best agreement: (0.05,0.15) 7722, (0.075,0.125–0.15), (0.1,0.1).
- M2 controls (swarm-ab/p): c3f0 ≈1.20 above M2-matched static at r46; 7722 ≈1.19; a7c2 (c∥=0.3) fully M2-explained.
- Frontier moved to chiral-β dressing (swarm-j chidress, swarm-am): ba1f = c3f0 + 24 chiral β entries (|G|²=7,13,19,21 ×T1) ±0.015 → s21 2.03, r46 2.23.
  fe2e (β 0.03): s21 1.63 vs r46 2.63 → cluster-specific.
- Submitted p4 (work/p4_ids.txt, 6 evals): j's chiral pattern on my mixed bases. Mailed swarm-j.
- Charged so far ~73+6.
- Next: r56 of plane; p4 results; write coverage post for the plane when r56 lands.

## wakeup 5 (06:32 UTC)
- p4 (j's chiral χ pattern on mixed bases): increments +0.57..0.68 at χ=0.015 on all ridge bases → cross term couples to total invariant amplitude.
  Best: 80c7 (0.025,0.2)+χ0.015: s21 2.151 / r46 2.290 (beats ba1f 2.031/2.225). (0.15,0.05)+χ: 1.933/1.943 most cluster-consistent.
  χ=0.0225: s21 turns over (1.85), r46 2.41 — large-β curvature split.
- Posted result 20261008T063142.349Z_swarm-e_result_7171.
- p5 submitted (work/p5_ids.txt, 6 evals): refine around 80c7.
- r56 stalled board-wide (~95+ min, swarm-c request to human). Many agents in reserve/verifier mode.
- Plan: after p5, stop s21/r46 optimizing; wait for r56; then coverage post. Consider w2 transfer of mixed-base dressing? (swarm-b covers chidress-w2.)

## wakeup 6 (07:03 UTC)
- p5: best bab7 (0.05,0.2,χ0.015) s21 2.273 / r46 2.352; 3c13 (0.025,0.225) 2.263/2.367. Negative c⊥ costs.
- Board frontier now s21 3.4–3.6 (swarm-t xfam-gp, swarm-ap tl-grad) at M2k 6.2–7.4. My ridge is outclassed in raw R.
- Closed joint-pair-w3 for search: coverage post 20261008T070249.914Z_swarm-e_result_ea08 (79 evals, all PASS; 44 promoted, r56 pending).
- Critique note 20261008T070324.020Z_swarm-e_note_7556: frontier M2k above static calibration (≤6.5); asked swarm-ab to extend to 7–9; mailed t, ap.
- r56 still stalled campaign-wide.
- Next: when r56 lands, post ladder update for my 44 promoted; check whether ab extends calibration (else consider doing it); otherwise reserve/verifier.
  Budget left: 421.

## wakeup 7 (07:35 UTC)
- Critique 7556 acted on: swarm-as (b1bb) and swarm-l (b9d5) extended static M2 calibration to 10: saturates ≈1.67/1.73; frontier ap 3a0e (s21 4.388/r46 4.390, Σ|α| 2.39/2.5 near box edge) = 3.0× static. 4fee r46 falls to 3.02.
- Many agents done (ak, g, i, x, o, d, al, ah, w, at, u). r56 still stalled.
- I'm in waiting/verifier mode, 421 evals unspent. Plan: wait for r56; post ladder update for my 44 promoted; then done.
- 08:05 still no r56. swarm-c critique 3772: Σ|α| L1 cap is chart-dependent; pair chart (mine) inflates L1 ~3x vs full stars. Frontier ap 4547 s21 5.20. Waiting.
- 08:37 swarm done posted; loop stopped (r56 still stalled).
