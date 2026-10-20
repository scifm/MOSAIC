# swarm-i notebook

Started 2026-10-14T10:24:17+00:00.

## 2026-10-14 wakeup 1 (11:14–11:20 UTC)
- Read board: swarm-a (axis-map) & swarm-b (linmap) both do the 60-axis ± map; swarm-c joint (G,R) orbits S1-S3×T1-T3; swarm-e bigamp (large-amp line scans + 18-D Sobol S1-S3×T1-T3).
- Key observation: parent w1c s21 R_staticM2 = Δ/(M2 Δ_LLL) ≈ 0.124 → deep M2 saturation (ρ 0.05..19.9). Sharper ≠ better here.
- My family `kpow` (hypothesis 20261014T111638.921Z_swarm-i_hypothesis_39e2): α[s,p]=λ_p c_s, β[s,p]=μ_p c_s,
  c_s = star coefs of log ρ_* (work/kpow_stars.json, from work/kpow_setup.py). Generator: work/kpow_gen.py OUTDIR name:l1,l2,l3,m1,m2,m3.
  Constraint: |λ| ≤ 0.475 single-p (|α|≤0.6), |μ| ≤ 0.237.
- Submitted stage 1: 32 requests (λ_p ∈ ±{.05,.15,.3,.45} p=1..3; μ1, μ2 ∈ ±{.05,.15}). ids in work/kpow_ids.txt.
  Pending: M3 phase (4 inputs in work/kpow_s1/M3*.json) once slots free.
- Next: read results, fit 1-D curves, then 2-D/CMA in (λ,μ).

## wakeup 2 (11:36–11:43 UTC)
- Board exploded (~40 agents). Leaders: joint (G,R) orbits — swarm-c S2×T1 +60 β+0.03 → s21 1.249 (d698), swarm-f chiral-joint 1.38 s21.
  Separable full stars CANCEL (orbit slopes of opposite sign). swarm-e: full-star manifold breaks at |α|≈0.1–0.2, |β|≈0.12.
- kpow results (s21): λ1=-0.05 → 0.941, +0.05 → 0.839, L2m005 0.955; |λ1|≥0.15 all FAIL (manifold). Family negative.
  Withdrew 16 large-amplitude kpow requests (L2/L3 |λ|≥0.15, M1/M2 ±0.15). Remaining kpow: L2/L3 ±0.05, M1/M2 ±0.05. M3 never submitted.
  TODO: post kpow abandon once remaining land.
- Pivot: family `hiT-orb` (hypothesis 20261014T113959.725Z_swarm-i_hypothesis_c196): origin slopes of joint orbits
  S1×T3, S2×T2(±30), S2×T3, S3×T1, S3×T2, S3×T3(±30); α ±0.05 on self-dual + +θ orbit; β ±0.03 on +θ. 32 submitted (work/hiT_ids.txt).
  Generator work/orbit_gen.py (spec g{G2}r{R2}_o{θ}_{a|b}{p|m}:val), convention verified = swarm-c's. Mailed swarm-c.
- Next: tabulate hiT-orb, post result w/ coverage; line-scan anything > 1.10; −θ partners if MT check needed.

## wakeup 3 (12:03–12:06 UTC)
- kpow: all done; posted abandon 20261014T120405.119Z_swarm-i_abandon_6670 (with coverage). Best 1.0014 (λ2=+0.05, 0a41). 6 PASS / 26 FAIL.
- hiT-orb: six agents mapped the same inner T2/T3 orbits (c's herding round 2). Withdrew 26/32 (withdrawn requests STILL RUN, at the back of the queue, and are charged).
  Kept β ±0.03 on S1×T3 +30, S2×T2 +30, S2×T3 +60 (6 reqs). Note 20261014T120500.095Z_swarm-i_note_aa00; mailed e, av.
- Leaders now: α⊥ S1×T1 −0.45 (ea28): s21 1.64 / r46 2.63 / r56 2.44, all PASS (ak: suspected branch change at −0.35..−0.45).
  swarm-c STRONG phase-only claim S2×T1 +60 β 0.03: 1.249/1.404/1.347. swarm-f S3×T1 +30 β 0.05: s21 1.558, r46 1.641.
  swarm-k: matched-density control explains none of the α⊥ −0.05 gain. swarm-s: ⊥ channel = half static LL mixing. swarm-l: conv46 ≡ r46 for pure LL0.
- Can't read broker run files (spectra); only `swarm show`.
- Next: hiT β results → post with coverage. Then verifier role: critique a claim (rule 11), look for unclaimed checks.

## wakeup 4 (12:31–12:35 UTC)
- Board top: swarm-h union c662 s21 4.76 PASS (multi-orbit α+β, 9×9 stars, S≤4,T≤4), 9462 3.77, swarm-t f0fb 3.51 — additive orbit gains.
  swarm-f STRONG claim S3×T1 chiral β 0.05: 1.558/1.641/1.560 (+conv46 1.641). swarm-k controls: α⊥ −0.45 density control R≈0.94–0.96 (density lowers gap).
- hiT-orb 32 still all pending (broker 32/32 in flight).
- New role: mech-i — matched-density controls for multi-orbit α combos. work/dens_ctrl.py (validated vs swarm-k ea28: M2_A 9.008, scale 1.0267).
  Submitted 5 controls (s21,r46,r56): c662_A c302, c662_B 3187, 9462_B 5738, f0fb_B 73fe, 353f_B 9e3b (work/ctrl_ids.txt). Note posted.
  Prediction: all within ±2% of 1.
- Next: collect controls → result post; hiT β → result post with coverage. Consider a critique post (rule 11).

## wakeup 5 (13:04–13:08 UTC)
- STRONG claims now: h c662 4.76/5.23/4.67 (conv46 5.23), t 8c01 4.82/5.19/4.55, h 9462, t 3542; j α⊥ STRONG; f, c phase-only STRONG.
- swarm-k density controls for c662/f0fb/353f A = 0.995/0.999/1.000. Mine: c662_A c302 = 0.9949/0.9945/0.9944 (same as k), c662_B 3187 = 1.0008/1.0004/1.0007. Others pending.
- Debate: g (9d4e) says R amplified 1/d² (zero-mode unprotection); p (d376) rebuts: contact term is inert for spinless scalar band; responses linear & sign-selective. I agree with p. d_sc control requested by g (human).
- c (88b2): leaders restore R_beyondM2 0.12 → 0.6–0.72 ≈ smooth static M2 law (w3/w2 ≈ 0.7).
  My finding: exp(κ O_S1) at M2=10 within 10 shells ≈ w1c (and negative) → w1c is the family's only shape at M2=10.
  Queued static calibration controls M2 = 2,3,4,5 (exp κ O_S1) and 6.5, 8 (convex mix M2=5 tri ↔ w1c) on s21+r46:
  5c50 09c9 c703 9505 3b71 60c1. Note 20261014T130559.347Z_swarm-i_note_da9b. Prediction: static peak ≈2.5–3 Δ_LLL at M2≈4–5 vs leaders 5.9 (s21).
- hiT partial: g1r4 +30 α∓: 0.9994/0.9913; g3r4 ∥ α−/+: 0.936 / 0.705F; g3r4 +60 α−/+: 0.677F/0.946; g3r4 +60 β− 0.853. Rest pending.
- Next: collect static calibration → result post (key deliverable); hiT result post w/ coverage; control result post.

## wakeup 6 (13:37–13:40 UTC)
- Density controls all landed: c662 A 0.995, B 1.0004–1.0008; 9462 B 1.0002–4; f0fb B 1.0005–7; 353f B 1.0009–10. Posted result 20261014T133728.925Z_swarm-i_result_7101 (coverage).
- hiT β (kept six): S1×T3 +30 β− (8181) s21 1.0585 → r46 1.0711 (promoting); β+ (3484) 0.916. S2×T2 +30 β− (421f) 0.707, β+ (4adc) 0.977.
  S2×T3 +60 β− (bdac) 0.853, β+ (3492) 0.552 FAIL. Withdrawn ones ran anyway (see status6). Pending: g4r1, g4r4 bits.
- Board: swarm-o f5f1 s21 6.28 / r46 8.33 (r56 pending). g retracted 1/d² argument. ap: leaders' γ on uniform LL0 LOWER gap → needs ρ*.
  u: w1c keeps 558 ideal zero pair modes; leaders lift 130–270.
- Static calibration (5c50 09c9 c703 9505 3b71 60c1) still pending.
- Next: post static calibration result (key), hiT result w/ coverage once last pending land.

## wakeup 7 (14:03–14:06 UTC)
- Static calibration (s21 R / r46 R): M2 2: 0.738/0.711; 3: 0.781/0.754; 4: 0.829/0.804; 5: 0.872/0.850; 6.5: 0.895/–; 8: 0.934/–.
  Monotone, nearly flat; w1c is family optimum. My peak prediction WRONG. Posted result 20261014T140420.338Z_swarm-i_result_365e; mailed c.
- New s21 leaders: s c325 9.87, av 0d8f 9.67, t 6506 8.71. o f5f1 6.28/8.33/8.12 (needs density ctrl, requested by o).
- Submitted density controls A+B on s21,r46,r56: f5f1 (839d, ecf7), c325 (d6a1, b796), 0d8f (1176, 7925).
  M2: f5f1 A 9.827 / B 9.971; c325 A 9.717 / B 10.028; 0d8f A 9.579 / B 9.949.
- p's rotation test of k≠k' handling PASSES (≤1.6e-6). g retracted. t asks the human about representation-dependent Σ caps.
- hiT: 8181 (S1×T3 +30 β−0.03) at r56 stage (s21 1.0585, r46 1.0711). Post hiT result w/ coverage when it lands.

## wakeup 8 (14:29–14:32 UTC)
- Static calibration complete (r46: 6.5 → 0.882, 8 → 0.927). c withdrew "restoring M2 law" (ec66) citing my 365e.
- Controls: f5f1 A 0.993/0.992/0.992, B 1.0008/1.0004/1.0007; c325 A 0.998/0.997/0.997, B 1.016/1.015/(r56 pend); 0d8f A 0.996/0.993/–, B 1.017/1.015/–.
  swarm-k now has a predictive formula R_ctrl−1 = 0.06 ΔM2 + 0.002 → further controls low value. Post addendum when r56 lands.
- hiT-orb closed: result 20261014T143047.450Z_swarm-i_result_7e51 (coverage). 6fe5 S3×T1 ⊥ α−.05 = 1.3679 replicates ar.
- Leaders: av e0a8 10.39/9.87/10.50 (conv46 pending), c325 9.87/10.15/9.53, 0d8f 9.67/10.49. u: qmax 8 projected pair interaction non-PSD for R≈10 records (fixed at qmax 10).
- Σ cap chart-dependence: ai/t requests to human. Don't rewrite blocks to evade.
- Next: 0-eval verify — compare conv46 (qmax 10) vs r46 for e0a8/c325 when landed (u's non-PSD concern). Then consider `swarm done`.

## wakeup 9 (15:02 UTC) — DONE
- Last controls landed: c325 B 1.016/1.015/1.016, 0d8f A 0.996/0.993/0.994, B 1.017/1.015/1.017. Posted 20261014T150231.988Z_swarm-i_result_5093.
- e0a8 conv46 9.96 vs r46 9.87; c325 conv46 10.153 vs r46 10.147. Records now s21 ~14.5 (w df9b), cap-limited.
- Decided to finish: space densely covered by ~45 agents; remaining open items (qmax, Σ-cap chart, 4th cluster, best static reference) need the human.
- swarm done posted. 97/500 evals charged. 8181 r56 still pending at exit.
