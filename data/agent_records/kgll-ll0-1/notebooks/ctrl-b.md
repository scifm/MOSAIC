# ctrl-b notebook

Started 2026-10-02T03:52:28+00:00.

## 2026-10-02 04:00 UTC — wakeup 1: orientation + batch 1

Read: charter/brief, ADR-0040, docs/progress/40 (pilot 024), 46 (Nk=21 precision), notes §5.6–5.9, §12, `physics.kdep_envelope`.
Key facts:
- Parents s21 Δ: w3 4.5714e-4, w2 3.2271e-4. Ladder: s21 → s21c (R≥1.02) → r46 (R≥1.0) → r56 → conv46 (R≥1.05, qmax 10, n_mesh 64, g_cutoff 6).
- doc46 at Nk=21: w3 α[S1,T1]=+0.05 → +1.85 %, −0.05 → −9.04 %; b1p −4.4 %; α[S3,T1]+0.05 → −3.75 %. Strongly concave around w3.
- 024 pilot: +0.51 % at 4×6 flipped to −0.92 % at 5×6. My working hypothesis: gains *linear* in the deformation
  come from how a finite cluster samples zero-mean F_p(k) → cluster artifacts. Look for responses that are *even* (both signs gain).
- Tools: work/gen.py (SPATIAL S1,S2,S3,S5,S6; MOMENTUM T1,T2,T3; build(parent, sstars, tstars, alpha, beta)). g_cutoff 6, n_mesh 48.
- `swarm check` takes ~5–10 s per file (admissibility); submit-batch runs it too.

Actions: hypothesis post 20261002T035811.047Z_ctrl-b_hypothesis_ec67. Batch 1 = 48 evals, w3, {S1,S2,S3}×{T1,T2}×{α,β}×{−0.3,−0.1,+0.1,+0.3};
ids in work/batch1_ids.txt. All 48 passed admissibility.
Next: collect R per direction; compute even part; pick directions for (a) finer line scans, (b) joint Sobol box.

## 04:20 UTC — wakeup 2: batch 1 half in (S1 rows done)
Digest showed "broker looks dead" (last tick 315 s) but results landed 04:10 and 16 in flight; recheck next wakeup, post `request` if still dead.
Collector: `work/collect.py work/batch1_ids.txt`.
S1T1 α: −0.3 0.636, −0.1 0.845, (+doc46 −0.05 0.910, +0.05 1.0185), +0.1 **1.0330** (promoted → confirm21, req 5a58), +0.3 0.965.
  → strongly odd (linear) response, max near α≈+0.15. Exactly the kind I distrust; the ladder will test it at 4×6/5×6.
S1T1 β ±0.1: 0.935/0.933, ±0.3: 0.63/0.67 → even, negative. Phase on S1 hurts, symmetric in sign.
S1T2 α ±0.1: 0.93/0.93; ±0.3: 0.54/0.73. S1T2 β ±0.1: 0.86; β ±0.3 FAIL (PES eg ~1, gap 0 — phase destroyed).
M2_k rises with |α| (4.42 at α=0.3) while R falls → gap does NOT follow M2^(k) for these deformations.
Next: wait for S2/S3 rows; then batch 2 = refine S1T1 α ∈ {0.15,0.2,0.25} + T3 and S5/S6 directions + first w2 probes.

## 04:40 UTC — wakeup 3: batch 1 complete (48 charged)
Broker alive again (tick 0 s).
**S1T1 α=+0.1 (req 5a58): s21 1.0330 P, s21c 1.0330 P, r46 1.0476 P (eg 7.3) → r56 pending.** Best so far; 4×6 gain larger than Nk=21.
Batch-1 map (s21 R): positive only for T1 amplitudes with α>0 on S1 (1.033) and S2 (1.019, req 9bd2). Everything else < 1:
- phases are even and harmful, worse for higher stars: S1 ±0.1 0.93, S2T1 ±0.1 0.87, S3T1 ±0.1 0.76, S2T2 ±0.1 0.59, S3T2 ±0.1 0.22; all ±0.3 phases FAIL except S1T1.
- T2 amplitudes all < 1 (S2T2 a±0.3 → FAIL/0.26). S3 (w3's own shell) T1 ±0.1: 0.91/0.95, ±0.3 FAIL.
- Large amplitude (0.3) → loses or fails everywhere.
Note: w3 uses only even G (|G|² = 4, 12, 16 → 2×S1, 2×S2, 4×S1) so ρ* has the half-cell periodicity; S1/S2 (odd) modulations break it k-dependently. Possibly why S1/S2 are the live directions.
Batch 2 (30 evals): w3 line scans S1T1 α {0.05,0.15,0.2,0.25}, S2T1 α {0.05,0.15,0.2}; joint S1T1×S2T1 α grid {0.05,0.1,0.15}² (family w3-joint-T1-amp);
S1T3, S2T3, S5T1, S6T1 α ±0.1; w2 S1T1/S2T1 α ±0.1, S1T1 α 0.05/0.2 (family w2-single-direction). Ids: work/batch2_*_ids.txt.

## 05:02 UTC — wakeup 4/5: batch 2 complete (78 charged), batch 3 submitted (35)
Batch 2 highlights (R s21 / r46, all PASS):
- w3 S1T1 α: 0.05 1.022/1.026; 0.10 1.033/1.048; 0.15 1.032/1.063; 0.20 1.020 (s21 only); 0.25 0.997.
- w3 S2T1 α: 0.05 1.021/1.029; 0.15 0.992; 0.20 0.937.
- w3 joint (αS1T1, αS2T1): (0.05,0.05) 1.034/1.050; (0.05,0.10) 1.021/1.072; (0.10,0.05) 1.034/1.065; (0.15,0.05) 1.021/1.073; (0.10,0.10) 1.009; others < 1.
- **r46 response grows faster than s21 with amplitude** → s21≥1.02 cut may drop good points.
- w3 S1T3/S2T3/S5T1/S6T1 α ±0.1 all < 1 (0.73–0.97).
- **w2: opposite sign.** S1T1 α −0.1: 1.026/**1.080** (d053); +0.05 0.949, +0.1 0.876, +0.2 0.673; S2T1 ±0.1 0.99/0.975.
- r56 for ALL nine promoted candidates is blocked: the parents' own r56 reference is still "SUBMITTED" (>1 h). If still stuck next wakeup → post `request`.
Batch 3: hypothesis 20261002T050008.544Z_ctrl-b_hypothesis_01ad. w3 plane refinement (11), third directions at base (0.1,0.05) (11), S4T1 ±0.1 (2);
w2 S1T1 −0.05/−0.15/−0.2, S1T1(−0.1)+S2/S5 ±0.05, S5T1/S3T1 ±0.1 (11). Ids work/batch3_*_ids.txt.

## 05:22 UTC — wakeup 6: batch 3 complete (113 charged), batch 4 submitted (20 → 133)
NB: collect.py over all batches now takes >2 min (one subprocess per req) — run per batch or in background.
Batch 3 (s21 / r46, all PASS):
- w3 plane: best s21 ~1.035 at (0.075,0.025),(0.125,0.025); r46 up to 1.073 at (0.10,0.075). Plane max at s21 ≈ 1.035.
- **Third directions at base (0.1,0.05), negative sign helps:** +α_S1T2 −0.05 → 1.054/1.051 (955b); α_S1T3 −0.05 → 1.051/1.056 (d78a);
  α_S3T1 −0.05 → 1.046/**1.077** (3d43); α_S2T3 −0.05 → 1.028/1.066. Positive signs all ≤ 0.99. β_S1T1 ±0.03 ~ neutral (1.026/1.034), β_S2T1 −0.03 1.025.
- w3 S4T1 ±0.1: 0.82/0.85.
- **w2 S1T1 α −0.15 → 1.024/1.101 (49ab)**; −0.05 1.018; −0.2 1.013 (not promoted). +S2T1 +0.05 → 1.027/1.083. S5/S3 T1 hurt.
- r56 still blocked on parent reference → posted request 20261002T051824.812Z_ctrl-b_request_68b6.
Batch 4: w3 base + combos of the negative third directions (all4 −0.05, pairs, each −0.1) + S2T2/S3T2/S3T3 entries; w2 at −0.15 + S1T2/S1T3/S3T1 ±0.05, S2T1 +0.05, S1T1 −0.125.
Plan: if combos are additive, set up CMA-ES (9 amplitudes S1-3×T1-3, β=0) on s21 for w3, budget ~120.

## 05:37 UTC — wakeup 7: batch 4 complete (133 charged); r56 unblocked
Human note 20261002T051851.105Z_human_note_efeb: r56 waited for H100s; GPU pool started 05:13 UTC. Expect r56 results soon.
Batch 4 (s21 / r46):
- w3 combos are sub-additive: base+S1T2−.05+S3T1−.05 1.066/1.067 (ca97, best s21); +S1T3−.05+S3T1−.05 1.064/1.069 (359b);
  all four −0.05 1.033/1.028; S1T2−.05+S1T3−.05 1.042/1.040. Single −0.1: S3T1 1.026/**1.095** (5f16), S1T2 1.037/1.032, S1T3 1.027/1.021, S2T3 0.982.
  S2T2 −.05 1.051/1.040; S3T2 −.05 1.035/1.040; S3T3 −.05 0.978. Positive signs lose.
- w2 at S1T1 −0.15: +S2T1 +.05 1.025/**1.103** (eec2); S1T3 −.05 1.027/1.077; S1T1 −0.125 1.026/1.096; S1T2 ±.05 lose; S3T1 ±.05 ~1.0.
Observation: s21 and r46 rankings disagree (S3T1 −0.1: s21 1.026 but r46 1.095; S1T2 dirs: s21 high, r46 flat).
Decision: hold new submissions until the first r56 numbers show which (s21 or r46) tracks 5×6. Then CMA-ES on the 9-amp space with the right proxy.

## 05:55 UTC — wakeup 8: still no r56; batch 5 (joint orbits, 25 → 158 charged)
r56 still pending for parents at 05:51 (GPU pool running since 05:13). Leaderboard top (w3): ca97 s21 1.066 / r46 1.067; 359b 1.064/1.069; 3d43 1.046/1.077.
New family joint-orbit-S1T1 (hypothesis 20261002T055205.256Z_ctrl-b_hypothesis_e009): split S1×T1 into pair stars, 3×3 α over
G lines {(1,0),(1,1),(0,1)} × R lines {(1,0),(0,1),(1,-1)}; classes perp/p30/m30 (diag patterns in work/batch5.py).
All-nine c = α_S1T1/3 reproduces the star (γ diff 2e-16; sanity run included, should match 5a58 s21 1.0330).
w3 c ∈ {.05,.1,.15,−.1}; w2 c ∈ {−.05,−.1,−.15,+.1}. Ids work/batch5_*_ids.txt.

## 06:12 UTC — wakeup 9: BREAKTHROUGH — w3 perp class (batch 5); batch 6 submitted (30 → 188 charged)
Batch 5: **w3 S1×T1 perp class (G line ⟂ R line), c>0: c=.05 1.105/1.088, c=.10 1.220/1.182, c=.15 1.333/1.284 (s21/r46, all PASS, eg 6–9).**
p30/m30 lose (≈0.95 at .05, 0.91 at .10); perp c=−0.1 0.698. Sanity all-nine run 1d5a reproduces 5a58 exactly (1.0330/1.0476).
The isotropic S1T1 star = perp (gain) + two losing oblique classes → explains the small star gain.
w2 opposite: perp loses everywhere; oblique classes with c<0 gain (m30 −.10 1.053/1.078, p30 −.15 1.036/1.097).
Result post 20261002T060948.242Z_ctrl-b_result_9adb.
New tool: work/orient.py `build_classes(parent, [(s, t, rel_angle, c), ...])` — pair stars per (s,t), class by rel. angle mod 180.
  S1T1/S3T1/S1T3/S2T2 have classes {30,90,150}; S2T1/S1T2 have {0,60,120}. Verified vs batch5 (γ diff 0).
Batch 6: w3 S1T1perp c ∈ {.2,.25,.3,.4,.5} (boundary widening); perp class of S3T1/S1T3/S2T2 at c ∈ {.05,.1,−.05};
  S2T1/S1T2 rel {0,60,120} × c ±.05; w2 oblique (both ±30 classes) c ∈ {−.1,−.15,−.2}, m30 −.2.
TODO: once a w3 perp winner stabilizes → `request` for matched-density static control (amplitude winner); also try β in perp class (phase-only = clean beyond-M2).

## 06:30 UTC — wakeup 10: batch 6 complete (188 charged); batch 7 submitted (27 → 215)
**w3 S1T1 perp class scan (s21 / r46, PASS unless noted):** .05 1.105/1.088; .10 1.220/1.182; .15 1.333/1.284; **.20 1.369/1.386 (007c, eg 4.8/5.3)**;
  .25 1.331/1.334 (eg 3.8); .30 1.234/1.204 (eg 2.8); .40 0.942 (eg 1.1); .50 FAIL. Optimum c≈0.2; PES gap shrinks with c.
w3 S2T1 rel0 (G line ∥ R line) c=+.05 → 1.0995/1.092 (c6f6); other S2T1/S1T2 classes ≈0.96; S3T1/S1T3/S2T2 perp all lose.
**w2 S1T1 oblique (±30 both) c=−.10 → 1.112/1.147 (c402)**; −.15 1.085/1.115; −.20 1.000; m30 −.20 1.005.
Request 20261002T062808.006Z_ctrl-b_request_b03b: matched-density control definition for 007c (option a: BZ-avg normalized kernel, b: M2-matched rescale).
Batch 7: perp c .175/.225; S2T1rel0 .1/.15; perp+S2T1rel0 combos; perp-class β alone ±.05/±.1 (beyond-M2 candidate) and with c=.2; S5T1perp, S6T1rel0 ±.05;
  w2 obl −.075/−.125, w2 S2T1 rel {0,60,120} ±.05. orient.py now supports β terms (5th field "b").
r56: still pending for parents (GPU) — nothing scored at 5×6 yet.

## 06:50 UTC — wakeup 11: batch 7 complete (215 charged); batch 8 (10 → 225)
Batch 7 (s21 / r46):
- perp c .175 1.363/1.338; .225 1.358/1.369 → plateau 1.36–1.37 at c∈[.175,.225]; best stays 007c (c=.2, 1.369/1.386).
- **phase-only perp class loses** (β ±.05 0.94/0.95, ±.1 0.88/0.85) → no clean beyond-M2 winner from phase here. β on top of c=.2 lowers (1.29–1.31).
- perp + S2T1rel0: no gain over perp alone (perp.2+rel0.025 1.355/1.371; perp.15+rel0.05 1.366; adding more lowers). Saturation.
- **S2T1 rel0 alone: c=.10 1.210, c=.15 1.333 (s21).**
- S5T1perp, S6T1rel0 ±.05 lose (0.92–0.96). w2 S2T1 all classes ≈0.97.
- w2 obl −.075 1.105, −.125 1.106/1.147 → w2 plateau ≈1.11 s21 / 1.147 r46.
Diagnostic R_beyondM2 = Δ/(M2_k Δ_LLL): parent ≈0.689; perp c=.10 0.788, .15 0.790, .20 0.724; S2T1rel0 .15 **0.808**.
  i.e. the gain exceeds the naive M2(k) scaling at moderate c (diagnostic only; control still needed).
Posted request 20261002T064516.556Z_ctrl-b_request_820b (r56 still pending 90 min after GPU start).
Batch 8: S2T1rel0 c .2/.25/.3; perp.1+rel0.1, perp.1+rel0.15, perp.05+rel0.15; perp.2 + oblique ±.03; w2 obl−.1 + perp ±.03.

## 07:12 UTC — wakeup 12: batch 8 (225 charged) → new best; batch 9 (14 → 239)
Human 20261002T064546.722Z_human_note_0a2c: earlier reply wrong — my arm's 5×6 GPU job had NOT started; resubmitted (H100 or A100).
**w3 S2T1 rel0 alone: c=.20 1.451, .25 1.509 (552f), .30 1.496 (s21, PASS, eg 5.7/4.8/3.9).** New best on s21. confirm/r46 pending.
perp+rel0 combos ≤ 1.418 (perp.05+rel0.15); perp.2 + S1T1 oblique ±.03 1.33/1.32 (lower than perp alone). w2 obl−.1+perp+.03 1.114 (≈ same).
Batch 9 (family joint-orbit-S2T1, hypothesis posted): rel0 c .225/.275; S2T3 rel0 ±.05, rel60/120 +.05; rel0.25 + S1T1perp ±.05;
  rel0.25 + S2T1 oblique ±.03; S2T2 rel30/150 +.05; rel0.25 + β rel0 ±.05.

## 07:33 UTC — wakeup 13: batch 9 complete (239 charged); batch 10 (20 → 259)
w3 S2T1 rel0 (s21 / r46): .20 1.451/1.411; **.225 1.489/1.419 (f0e5, best r46 overall)**; .25 1.509/1.415; .275 **1.511**/1.400; .30 1.496/1.372.
  → s21 peaks c≈.27, r46 peaks c≈.22. Neighbours at rel0 .25 (perp ±.05, oblique ±.03, β ±.05) all lower. S2T3/S2T2 classes lose.
w3 perp.1+rel0.1 r46 1.394. w2 obl−.1+perp±.03 r46 1.137/1.134.
Still no r56 numbers.
Batch 10 (family joint-orbit-S4T1, hypothesis posted): S4×T1 classes (6 chiral; 3 achiral pairs) on w3/w2; w2 S2T1 rel0 ±.15.
orient.lines now handles 12-member stars (6 lines).

## 07:55 UTC — wakeup 14: batch 10 complete (259 charged); batch 11 (7 → 266)
S4×T1 on w3: weak. Chiral rel49 +.05 1.017, rel131 +.05 1.025/1.035 (r46); others 0.94–0.96; achiral pairs all < 1 (0.77–0.99).
S4×T1 on w2: **rel11+169 +.05 → 1.056/1.139 (9531)**; rel71+109 +.05 1.004; others < 1. w2 S2T1 rel0 ±.15: 0.72/0.77.
Still no r56 numbers (4 h after first promotions).
Batch 11: w2 S4 rel11+169 c .1/.15; chiral 11, 169 +.05; w2 obl(−.1) + S4 rel11+169 +.05/+.1, + S4 rel71+109 +.05.

## 08:22 UTC — wakeup 15: batch 11 complete (266 charged); batch 12 (10 → 276)
w2 (s21 / r46): S4 rel11+169 +.1 0.949, +.15 0.712; chiral rel11 +.05 1.024/1.086, rel169 1.016.
**w2 obl(−.1) + S4 rel11+169 +.05 → 1.121/1.219 (d1bb); obl(−.1) + S4 rel71+109 +.05 → 1.101/1.232 (dd8d)** (best w2 r46). +.1 → 0.969.
w2 r46 runs ~10 % above s21 for these.
Still no r56 (none on either parent).
Batch 12 (family w2-obl-S4, 10 evals): grid obl c_o ∈ {−.075,−.1,−.125} × S4 rel71+109 ∈ {.025,.05,.075}; obl−.1 + S4a.05 + S4b.025; obl−.1 + S4b.025.

## 08:50 UTC — wakeup 16: r56 LANDED → STRONG claims (276 charged; batch 13 phase-only +6 → 282)
Parent r56: w3 4.5515e-4, w2 3.2164e-4.
**w3 S2T1 rel0 class: three broker `strong` claims (PASS on s21, s21c, r46, r56, conv46; C=1 = parent):**
- c=.225 f0e5: s21 1.4892, r46 1.4189, r56 1.4511, conv46 1.4196 (eg 4.4–5.5).
- c=.25 552f: 1.5085 / 1.4153 / 1.4886 / 1.4145.  c=.20 2871: 1.4511 / 1.4111 / 1.3881 / 1.4124.
- c=.275 991f: r56 1.4804 (conv pending); rel0.25+obl+.03 0947 r56 1.452; rel0.25+perp−.05 d349 r56 1.372; perp.05+rel0.15 9896 r56 1.393.
Claim post 20261002T084707.109Z_ctrl-b_claim_bd2e. w2 grid (batch 12): s21 up to 1.147, r46 up to 1.240 (ccc1) — r56 pending.
Matched-density analysis (work/matched.py): (a) BZ-avg normalized kernel → M2 3.764 (parent 3.629), odd harmonics cancel, admissible;
  (b) M2-matched rescale of parent infeasible (density < 0). Posted 20261002T084750.939Z_ctrl-b_request_ea4f: will submit (a) as --control next wakeup unless told otherwise.
Batch 13: phase-only S2T1 rel0 β ∈ {±.05, ±.1, ±.2} (beyond-M2 probe).
NEXT: build (a) control input (8 shells; outside-shell weight ≤ 0.011 dropped, ΔM2 ~ 0.002) and submit `--control`; coverage posts per family.

## 09:12 UTC — wakeup 17: phase-only loses; control submitted (282 charged + control)
Phase-only S2T1 rel0 (batch 13): β ±.05 0.962/0.977, ±.1 0.898/0.893, ±.2 0.489/0.402 → no clean beyond-M2 winner.
w2 d1bb (obl −.1 + S4 rel11+169 +.05) reached **STRONG**: s21 1.121, r46 1.219, r56 1.194, conv46 1.218.
Control (a) for f0e5 submitted: req 20261002T091017.407Z_ctrl-b_req_6026 (family control-matched-density, --control, clusters s21,r46,r56).
  Built by work/build_control.py: 8 shells + 18 extra harmonics (complete C3 orbits only; C3_hard check rejected incomplete orbits). M2 3.764, min dens 0.012.
  Note posted. No human reply yet to requests b03b/ea4f.
NEXT: read control; post coverage results for families: w3-single-direction, w3-joint-T1-amp, joint-orbit-S1T1, joint-orbit-S2T1, joint-orbit-S4T1, w2-single-direction, w2-obl-S4.

## 09:35 UTC — wakeup 18: control partial; CMA-ES gen0 (285 → 293 charged)
**Control (a) for f0e5 (req 6026): s21 1.0223, r46 1.0224 (PASS, eg 21–22); r56 pending.** vs f0e5 s21 1.489 / r46 1.419.
  → BZ-averaged density explains ≈ 2 % of a ≈ 42–49 % gain. Also: f0e5's PES gap ≈ 5 vs control/parent ≈ 20–22.
w2 dd8d also STRONG: s21 1.101, r46 1.232, r56 1.190, conv46 1.231.
CMA-ES started (family cma-classes-w3, hypothesis 20261002T093217.284Z_ctrl-b_hypothesis_1dd5): work/cma_es.py ask/tell,
  state work/cma/state.json; gen ids in work/cma/gen{g}_ids.txt (save submit-batch output there!). gen0 submitted (8).
work/summary.py running in background → work/summary.txt / summary.json (for coverage posts).
Loop per wakeup: `python work/cma_es.py tell` (after all 8 done) → `ask` → submit-batch work/cma/gen{g} > work/cma/gen{g}_ids.txt.

## 09:52 UTC — wakeup 19: CMA gen0 told, gen1 submitted (301 charged)
CMA gen0 (σ0=.05 around f0e5): best 1.385; all 8 below the f0e5 centre (1.489). Off-axis sensitivity is sharp: ~0.05 in other classes costs 10–50 %.
  → single-class rel0 looks like a sharp local optimum. If gen1–2 don't beat 1.49, stop CMA (save budget) and post the coverage.
Control 6026 r56 still pending. Summary (work/summary.txt): w3-single-direction 63 (48 P, 15 F); w3-joint-T1-amp 45 P; w2-single-direction 25 P;
  joint-orbit-S1T1 w3 66 (65 P, 1 F; 23 strong), w2 26 P (6 strong); joint-orbit-S2T1 w3 20 P (8 strong); joint-orbit-S4T1 w3 12, w2 15 (2 strong); w2-obl-S4 10.
  Star-chart families' r56 still queued (long GPU queue) → coverage posts once they land.

## 10:08 UTC — wakeup 20: control complete; CMA gen2 (309 charged)
**Control 6026 final: s21 1.0223, r46 1.0224, r56 1.0223 (PASS, C=1, eg ≈ 21–22).** Posted result 20261002T100543.282Z_ctrl-b_result_1de6
  (BZ-averaged density explains ≈ 5 % of f0e5's gain; caveat: not an M2-matched control; phase-only loses).
CMA gen1: f = [1.474, 1.383, 0.982, 1.274, 0.827, 1.128, 1.475, 1.348] (best 1.4751 < f0e5 1.489). mean → rel0 .253, rel120 .043, perp −.032, m30 −.026. σ .044.
gen2 submitted.

## 10:25 UTC — wakeup 21: CMA stopped (309 charged)
CMA gen2 best 1.4528 (one FAIL). 3 gens, 24 evals, never beat f0e5 → abandon posted with coverage.
Summary refresh running in background (work/summary.txt; CMA ids copied to work/batchcma*_ids.txt).
NEXT: coverage posts for families w3-single-direction, w3-joint-T1-amp, joint-orbit-S1T1, joint-orbit-S2T1, joint-orbit-S4T1, w2-single-direction, w2-obl-S4
  (after r56 of the star families lands). Then decide: remaining budget ~190 → maybe w2 refinement or swarm done.

## 10:50 UTC — wakeup 22: coverage posts
Posted coverage results: w3-single-direction (5b7b), w3-joint-T1-amp (63fa), w2-single-direction (397a), joint-orbit families w3+w2 (latest post).
S1T1 perp class also strong across all clusters (007c min 1.306 at r56; 49f0 c=.1 min 1.182). w2 best by min R: 9267 (1.1466; strong).
Budget 309/500. Remaining ideas are low-yield (local optimum confirmed by CMA). Considering `swarm done` next wakeup after a final digest check
  (wait for human replies to requests b03b/ea4f; keep a short tail open for any reply).
10:55 — extra mechanism controls submitted: single-k densities of f0e5 at Γ (M2 6.66, bd7a) and K (M2 3.94, 5483); --control s21/r46/r56.
  Built by work/kdens.py (n_mesh 64, g_cutoff 10; at g_cutoff 6 the Γ density goes negative from truncation). Note posted.
11:08 — single-k static controls (partial): Γ density (M2 6.66) bd7a: s21 0.662, r46 0.717 (PASS, eg 12); K density (M2 3.94) 5483: s21 0.915, r46 0.989.
  → static bands with the winner's own sharpest/softest densities LOSE vs parent; BZ-avg density gives 1.022. k-dependence essential. r56 pending.

## 11:25 UTC — wakeup 25: DONE
Single-k controls r46: Γ 0.717, K 0.989 (r56 queued). Posted mechanism result 20261002T112227.496Z_ctrl-b_result_5db5.
Ran `swarm done` with the final summary (work/done.md). 315/500 charged + 3 controls. Loop stopped.
