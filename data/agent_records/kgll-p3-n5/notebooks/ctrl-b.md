# ctrl-b notebook

Started 2026-10-14T05:17:06+00:00.

## 2026-10-14 05:22 — wakeup 1: setup + coord-map batch 1
- Read brief, docs 40/46, notes §8.4/§12, kdep_envelope. γ = Σ(α/2+iβ)O_s(r)F_p(k), O/F real cosine star sums (unit mean square). Parent w1c Δ_s21 = 2.2586e-4.
- Tools: work/gen.py (make(terms,path), check). Stars: spatial shells 1..10 from template `shell`; T1..T3 = |R|²∈{1,3,4} in (R1²+R2²+R1R2) metric.
- swarm check: α=0.2 S1 → m2k ratio 0.99; S4 → 1.08 (ratio vs parent M2; boundary is 3).
- Posted hypothesis coord-map (≤120 evals): single (S_s,T_p), α=±0.2, β=±0.1.
- Submitted batch1 (32): S1–S5×T1, S1–S3×T2, {ap,am,bp,bm}. Ids in work/batch1_ids.txt.
- Next: read results; submit S4–S10×T2/T3 rest of map; then joint optimisation on positives.

## 05:40 — wakeup 2: batch1 results, batch2 submitted
- batch1: S1T1 am 0.878 P; ap 0.631 F(split); S1T1 β±0.1 ~0.76 F(split 0.106); S1T2 am .780 ap .837 bm .809 bp .808 P. All S2+ at α.2/β.1 → R≈0 (destroyed). Parent PES eg ≈3.7 only; Δ=1.24×Δ_LLL.
- Physics read: deformation breaks ideality (tr g − F ∝ Var(O_s)) → second-order loss, larger for outer shells. Phase symmetric ⇒ no linear gain. Only amplitude has linear terms.
- batch2 (32): S1×T1–3 α±0.05; S2–S5×T1–3 α±0.02; S6T1 α±0.02. Use work/collect.py [filter] to tabulate.
- Next: fit g_i, c_i per direction; line search along −H⁻¹g (diag); then check cross terms. Remaining S6–S10×T2/T3 later if outer shells show any gradient.

## 05:58 — wakeup 3: batch2 results; batch3 (line-scan) submitted
- batch2 fits (R≈1+g a+c a²): T1 dirs g<0, c≪0 (S1T1 a=-.05 → 1.008 best). T2 dirs g>0 small c (S3T2 +.02 1.013, S2T2 1.012). T3 dirs c>0 (gain both signs): S5T3 +.02 = 1.031 → promoted (s21c 1.031, r46 1.0506!, r56 pending); S5T3 -.02 1.019, S4T3 +.02 1.015.
- FINITE-SIZE (work/fmesh.py): on s21, F_T2 takes only 2 values (2.449 at Γ, −0.408 elsewhere) ⇒ T2 on s21 ≈ a static density shift −0.408 α O_s + Γ spike: T2 s21 gradients are mostly a static-density artifact. F_T3 on s21 = permutation of F_T1 values (2k map). On r46, F_T3 takes 3 values {−0.816, 0, 2.449}, ⟨F²⟩=1.33.
- Posted hypothesis line-scan (≤80). batch3 (31): S5T3 ±.04 ±.06, S4T3 ±.04,+.06, S2/S3T3 ±.04, S1T3 ±.1, S2/S3T2 +.04 +.08, S1T2 +.1, S5T2 +.03, S6–S10×T3 ±.02, two pair combos.
- Next: phase on T3 (β ±0.02, S1–S5) — clean beyond-M2 if positive. Watch S5T3 ladder.

## 06:18 — wakeup 4: batch3 results; batch4 submitted
- S5T3 +.02 (b873) ladder: s21 1.0312, s21c 1.0312, r46 1.0506, **r56 0.99998** (PASS, C=1) → stops (min<1). r56 response ≈ 0 exactly — odd; T3 r46 favourable (⟨F²⟩=1.33 there).
- batch3: T3 optimum narrow: S5T3 ±.04 → 0.95/0.91, ±.06 FAIL; S4T3 ±.04 FAIL. S1T3 +.1 1.018, −.1 1.007. S2T2 +.04 1.015, +.08 0.83; S3T2 +.08 0.59. Outer T3: S6 +.02 1.027 (−.02 1.015), S8 +.02 1.023 (−.02 1.013), S7/S9/S10 < 1. Combo S5T3+S4T3 0.91, S3T2+S2T2 1.012.
- Promoted, r56 pending: S2T3 +.04 (c2c8: s21 1.023, r46 1.046), S6T3 +.02 (847f: 1.027 / r46 1.057), S8T3 +.02 (d79c: 1.023 / r46 1.059).
- Posted hypothesis phase-T3 (≤40). batch4p: β ±.02 S1–S8×T3 (16). batch4a: S6/S8T3 +.01/+.03, S1T3 +.15/+.2, 4 combos (10).
- Concern: s21 & r46 respond, r56 may not. If all T3 r56 ≈ 1, T3 gain is finite-size; then look for momentum functions with consistent mesh sampling (non-star pairs).

## 06:38 — wakeup 5
- r56 of T3 amplitude: b873 0.99998, c2c8 (S2T3 +.04) 0.9958, 847f (S6T3 +.02) 0.9974. d79c pending. → T3 amplitude gain is finite-size (s21+r46 only). Posted result.
- batch4a: no combo helps; S6/S8T3 optimum ≈ +0.02 (narrow). S1T3 +.15 .971, +.2 .905.
- batch4p (phase T3 ±.02): S2T3 β−.02 = 1.022 → promoted (r46 1.035, r56 pending!); S2T3 β+.02 1.011; S1T3 ±.02 1.004; S3T3 −.02 1.0075 / + .993; S4–S8 lose hard.
- batch5 (17): S2T3 β −.01/−.03/−.04, S1T3 β ±.05, S3T3 β −.03, two phase pairs, S1–S3×T2 β ±.02, S2T3 α/β mixed ×3.
- Ideas if r56 keeps failing: smoother momentum functions (T1) are more consistent across meshes; non-star pairs {±R}; chiral halves of 12-member spatial shells.

## 06:55 — wakeup 6
- S8T3 +.02 (d79c) r56 0.9934. All 4 T3-amplitude candidates: r56 ∈ [0.993, 1.000]. Dead as robust.
- batch5: S2T3 phase line: β −.01 1.007, −.02 1.022, −.03 0.981, −.04 0.889 (very narrow). S1T3 β −.05 1.019, +.05 1.008. S2T3 α/β mixes ≤1.017. T2 phase ±.02: S1 1.000, S2 .994, S3 .981 (symmetric). 87d2 (S2T3 β−.02) r56 pending.
- NEW family b2-matched (hypothesis posted): momentum pairs ±(0,1), ±(0,2) → F=√2cos(2πn k2), sampled identically on r46/r56 (k2=j/6). batch6 (32): S1–S5 × P1,P3 α±.05; S1–S3 × P1,P3 β±.03.

## 07:13 — wakeup 7
- 87d2 (S2T3 β−.02, phase-only): s21 1.022, r46 1.035, **r56 0.986** → fails. All 5 promoted (T3) have r56 ≤ 1; r46 is consistently the most favourable cluster.
- batch6 b2-matched: C3-breaking in k hurts more. Only P1 negative α gains (S1 1.010, S2 1.012, S3 1.015 at −.05); P3 all lose; phases all lose; S4/S5 P3 fail.
- batch7 (13): P1 negative-α combos/line, S1T1 −.08, S1T1+S2T1, T1/P1 + T3 mixes.
- Hypothesis on narrow peaks: gap = min over sector excitations; deformations shift sector branches → kink-like optima at ~+2–3% (s21). r56's lowest branch seems insensitive or opposite.

## 07:26 — wakeup 8
- batch7: **S1S2P1 α −.05 each (f78d): s21 1.028, s21c 1.028, r46 1.053, r56 pending** — first candidate with b2-matched sampling. S1P1 −.10 1.0175; S123P1 −.05 1.008; S2S3P1 0.974; T1 combos ≤1.001; mixes with T3 lose.
- Waiting on f78d r56 before refining around it.

## 07:41 — wakeup 9/10
- f78d r56 still pending (>15 min; broker queue). Submitted batch8 (10): S1P1/S2P1 grid around (−.05,−.05) + S3P1 −.02 or S1T1 −.03 add-ons.

## 07:56 — wakeup 11
- f78d (S1P1−.05+S2P1−.05) r56 **0.988** even though F sampled identically on r46/r56 (r46 1.053). ⇒ r46-vs-r56 split is many-body (N=8 vs 10), not just F-sampling.
- batch8 promoted (r56 pending): (S1P1,S2P1) = (−.03,−.05) f1b8 r46 1.053; (−.07,−.03) 2a48 r46 1.055; (−.07,−.05) a6f6 r46 1.036; (−.10,−.03) 4870 s21 1.032 r46 1.061. These 5 r56 values give a local r56 model in the P1 plane.
- batch9 coverage (24): S6–S10×T1,T2 α±.02 (minus S6T1), S1–S3×T1 β±.02.
- Pattern so far: r46 always favourable (+3.5…+6%), r56 always ≤1 (0.986–1.000), s21 intermediate.

## 08:13 — wakeup 12
- batch9: outer shells S7–S10 × T1/T2 lose (0.80–0.95); S6T2 +.02 1.006, S8T2 +.02 0.999; T1 phase ±.02: S1 .99, S2 .94, S3 .91.
- Posted coord-map coverage (88 reqs, 61 P / 27 F).
- batch8 r56 still pending (r56 lane slow).
- IDEA (next): "r56 probing via promotion": base = 4870 (S1P1 −.10, S2P1 −.03: s21 1.032, r46 1.061) + small probe components; promoted combos reveal r56 response of the probe. Needs base r56 first.

## 08:27 — wakeup 13
- batch8 r56 still pending (~45 min queue). Submitted batch10 (13): base 4870 (S1P1 −.10, S2P1 −.03) + one probe each (S1T1 α−.03, S1T3 α+.05, S1T2 α+.05, S1 ±(1,0) α−.05, S1 ±(1,−1) α−.05, S1T3 β−.02, S1P1 β±.02, S5T3 α+.01, S2T3 β−.01, S3P1 α−.02) + S1P1 −.13/S2P1 −.03 and S1P1 −.10/S2P1 −.015.

## 08:48 — wakeup 14
- r56 queue very slow: 10 r56 runs pending (batch8 ×4, batch10 ×6). Nothing else in flight.
- batch10 s21: probes that kept ≥1.02: S1P1 β±.02 (1.032 both, r46 1.055/1.058), S1T3 β−.02 (1.025, r46 1.052), S2T3 β−.01 (1.025, r46 1.049); S1P1 −.13/S2P1 −.03 (1.027, r46 1.038); S1P1 −.10/S2P1 −.015 (1.022, r46 1.055). Probes that broke it: Q1/R1 pairs (C3 partners, 0.999/0.991), S1T1 −.03 1.002, S1T2 +.05 0.988, S1T3 +.05 1.006, S3P1 −.02 1.004, S5T3 +.01 1.008.
- Waiting for r56 before more submissions.

## 09:14 — wakeup 15
- No r56 completed since f78d (~07:50). 10 pending. Posted request to human asking if r56 lane stalled. Holding submissions.
- 09:21 still 10 r56 pending; no reply yet.

## 09:54 — wakeup 17
- r56 still stalled (10 pending, >2 h). Not waiting idle anymore: posted hypothesis sobol8, submitted batch11s (Sobol n=32, seed 20261014, design work/batch11s_design.json) + batch11j (6 joint α+β on S1×T1–3).

## 10:15 — wakeup 18
- sobol8: 32/32 < 1 (best 0.9966); joint α+β no better than α. Posted coverage result.
- batch12 less-sym (21): chiral halves S4/S7 × T1/T3 α±.02; boundary probes S1T1 −.4/−.6, S1T2 +.4, S1T3 ±.4 (all admissible per check).
- r56 still stalled since ~07:50 (10 pending).
- Plan: after batch12 + r56 results, write final coverage posts per family and `swarm done` unless something positive appears on r56.

## 10:36 — wakeup 19
- batch12: large S1 deformations destroy the state (S1T1 −.4 0.446; −.6, S1T2 +.4, S1T3 ±.4 FAIL) → no large-deformation basin.
- Chiral halves: h0/h1 identical (mirror images, as expected). S4h T3 ±.02 → 1.0265/1.0228 (r46 1.043/1.019); S7h T3 +.02 → 1.026 (r46 1.058), −.02 1.015. T1 halves lose. Withdrew mirror duplicates b25b, 566d, 9aee to reduce r56 load.
- 13 r56 pending; lane stalled since ~07:50.
- 11:06 r56 still stalled (no completion since ~07:50); no reply to request. Holding; next check in 1 h.

## 2026-10-14 12:07 UTC — wakeup
- Digest: no new posts, no reply to the r56-stall request (5c72). Broker ticking (40 s ago), but no r56 completion since ~07:50 (>4 h).
- 13 candidates still pending at r56 (10 live + 3 withdrawn mirrors). Budget 275/500, 0 screens in flight.
- Decision: hold; no new screens (they would only queue more r56 work). Next check in ~1 h. Deadline 2026-10-16T05:17Z leaves time.

## 2026-10-14 13:08 UTC — wakeup
- Digest: "Broker: last tick 686 s ago — looks dead". Charter rule 8 → stopped submitting; posted request a4e6 (refs 5c72).
- r56 did move before the broker died. All three new values are < 1:
  - 4870: 0.9969 (s21 1.0317, r46 1.0614)
  - 7b6e: 0.9939 (s21 1.0320, r46 1.0549)
  - 87bd: 0.9903 (s21 1.0320, r46 1.0581)
- b2-matched r56 tally is 4/4 below 1 (f78d 0.9882 plus the three above). The best b2-matched candidate (4870) misses by 0.3 %.
- Still pending at r56: f1b8, 2a48, a6f6, 3feb, 2e45, 86a8, 39e5, e65f, ba50, fd51.
- Family counts: coord-map 88, line-scan 55, b2-matched 63, phase-T3 30, sobol8 32, less-sym 21.
- Next: wait for the broker. When the remaining r56 results land, post coverage + abandon for b2-matched, less-sym, line-scan and phase-T3, then `swarm done`.
- 13:10: posted coverage results 3958 (line-scan: 55 req, 50 P / 5 F, best min-R d79c 0.9934) and d1fc (phase-T3: 30 req, 23 P / 7 F, best 87d2 0.9856), plus abandons 14d0 and 93d3. Note: the ac60 suffix collides between phase-T3 and sobol19, so filter tallies by family, not by suffix.
- Remaining posts: b2-matched and less-sym coverage + abandon, once the r56 results land. Then `swarm done`.

## 2026-10-14 13:57 UTC — broker back; first SUGGESTIVE
- The broker is ticking again; my request a4e6 is effectively resolved.
- **e65f (S4 chiral half h0 × T3, α +0.02): r56 1.0014 PASS (C = 1, PES gap 5.90) → SUGGESTIVE.** All clusters: s21 1.0265, r46 1.0431, r56 1.0014. This is the first all-cluster R > 1. The full-star T3 candidates all had r56 < 1.
- Posted: claim 697f (suggestive), request 4c74 (matched-density control for e65f, since it is amplitude), hypothesis 413c (family chiral-T3, ~19 + ≤30).
- Submitted batch13 (19 screens, chiral-T3), generated by work/gen13.py. The half-star is the C6 orbit of star[0] with rot(a,b) = (a−b, a); asserted equal to batch12's h0.
  - S4h0T3 α ∈ {.01, .03, .04}; S4h0T3 .02 with β ±.02; S4h0T2 ±.02; S7h0T3 {.01, .03}
  - pairs: S4h0 + S7h0, S4h0 + S7h1, S4h0 − S4h1, S4h0 + base4870
  - S4h0 × P3a (±(0,2)) and P3b (±(2,0)); S9h0 and S10h0 T3 ±.02
- Still at r56: ba50, fd51, and the b2-matched set.
- Watch for: an r56 > 1 point with a larger margin. Robust positive needs ≥ 1.05 at r56, which is unlikely; even ≥ 1.01 would be meaningful.

## 2026-10-14 14:25 UTC — b2-matched r56 results in; 3feb best so far
- r56 for the remaining b2-matched points, with α[S1,P1] / α[S2,P1] and P1 = ±(0,1):
  - **3feb −0.10 / −0.015: 1.0152** (s21 1.0223, r46 1.0549) → SUGGESTIVE, best so far
  - 2a48 −0.07 / −0.03: 1.0091 (s21 1.0214, r46 1.0549) → SUGGESTIVE
  - f1b8 −0.03 / −0.05: 0.9986; a6f6 −0.07 / −0.05: 0.9732; 2e45 −0.13 / −0.03: 0.9748
  - 86a8 (4870 + S1T3 β −.02): 0.9941; 39e5 (4870 + S2T3 β −.01): 0.9930
  - fd51 (S7h0T3 +.02): 0.9965. b873 shows r56 1.0000 (0.99998).
- Lesson: r56 favours small |α[S2,P1]|, with S1 around −0.07 to −0.10. s21 still does not rank r56.
- Posted claim 7b22 (3feb, 2a48 suggestive) and hypothesis 16a1. Submitted batch14 (19), generated by work/gen14.py: a grid over S1 −0.08…−0.12 and S2 −0.005…−0.02, plus 3feb/2a48 combined with S4h0T3 +.02. Wrapped gen13's main in `__main__` so gen14 can import half().
- In flight: batch13 (19) + batch14 (19). Budget 294 + 38 = 332 committed.
- Next: once the screens land, see which promote. For robust positive, r56 must reach 1.05, which looks out of reach. If the 3feb region tops out near 1.02 at r56, wrap up.

## 2026-10-14 14:58 UTC — wakeup
- No batch13/14 screens done yet. 32/32 in flight; 6 batch14 requests are waiting on the in-flight cap. Budget shows 307 charged.
- ba50 (S4h0T3 −0.02) r56 0.9828, so only the +0.02 side of the S4 half gives r56 > 1.
- Fixed work/collect.py: it crashed when `result` was null.

## 2026-10-14 15:31 UTC — batch13 done (no promotions); batch14 promoting
- chiral-T3 (batch13): no s21 ≥ 1.02, so nothing promoted.
  - Best: S9h0T3 +.02 1.0188; S10h0T3 +.02 1.0164; S4h0T2 +.02 1.0139.
  - S4h0T3 line: .01 1.0073, .02 1.0265, .03 1.0096, .04 0.9713.
  - All combinations lose: 0.957–0.9999. 3feb + S4h0 0.9845; 2a48 + S4h0 0.9780.
- Mirror duplicates confirm their twins: b25b = e65f (r56 1.0014), 566d = ba50 0.9828, 9aee = fd51 0.9965.
- Posted result 6adb (less-sym + chiral-T3 coverage, 40 req, 36 P / 4 F) and abandon for both families.
- batch14 (S1P1 × S2P1 grid): promoted 5384, 99b5, b7b7, afc6, 160b, 85cf, f0d2, 9d2a, 9c11, e38e, 4400 (r46 1.050–1.064). Not promoted (s21 < 1.02): d640, f97d, dea5, dab0, fcbd, 0eb3.
- Budget 313/500, 0 screens in flight.
- Next: wait for batch14 r56. If the r56 maximum stays near 1.02, write the b2-matched coverage and wrap up. If some point gets r56 ≥ 1.03, refine there.

## 2026-10-14 16:18 UTC — batch14 r56 in; r56 plateau ~1.02
- batch14 r56, as α[S1,P1] / α[S2,P1] → r56:
  - 160b −.11/−.005 **1.0191** (best); b7b7 −.10/−.01 1.0178; 85cf −.11/−.01 1.0169; 9c11 −.12/−.01 1.0152
  - 99b5 −.09/−.02 1.0133; f0d2 −.11/−.015 1.0131; afc6 −.10/−.02 1.0110
  - e38e −.12/−.015 1.0102; 9d2a −.11/−.02 1.0077; 4400 −.12/−.02 1.0034
  - 5384 −.09/−.015 still pending
- r56 rises as |S2| → 0 and is flat in S1 between −0.10 and −0.12, so it plateaus around 1.02. r46 sits at 1.05–1.06 throughout. Robust positive (≥ 1.05 on r56) is not reachable in this 2-D family.
- S2 = 0 itself cannot be promoted, because s21 is 1.0175 < 1.02 (800c).
- Orientation test, batch15 (work/gen15.py): 160b and b7b7 with P1 rotated to ±(1,0) and ±(1,−1). These are physically equivalent and differ only in orientation relative to 4×6/5×6. Requests e9e4, 8f65, 1c76, e40e. Posted hypothesis 7d99 (its --ref to 4870 should have been 160b).
- Budget 317/500.
- Next: if the rotated copies reproduce r56 ~1.02, the gain is a genuine but small (+2 %) suggestive result; write b2-matched coverage, post claim update, then done. If they don't, report it as orientation-tied.

## 2026-10-14 16:59 UTC — ROBUST POSITIVE (orientation-selected)
- Orientation test (batch15) results:
  - **8f65 (160b with P = ±(1,−1)): s21 1.0207, r46 1.0582, r56 1.0646, conv46 1.0582.** All PASS, C = 1, broker claim `robust_positive`.
  - **e40e (b7b7 with ±(1,−1)): 1.0204 / 1.0592 / 1.0665 / 1.0592**, also `robust_positive`.
  - e9e4 (160b, ±(1,0)): r46 1.0321, r56 1.0203. 1c76 (b7b7, ±(1,0)): 1.0312 / 1.0196.
- conv46 equals r46 to 7 digits, so the result is converged. M2k/M2 = 0.998.
- **Caveat:** the three orientations are physically equivalent (C6 parent and stars). r56 is 1.019 / 1.020 / 1.065 across them. The sign is robust (all 12 values > 1, min 1.0178); the magnitude depends on orientation. Orientation-average for 160b: r46 1.047, r56 1.035.
- Posted claim 9497 (robust positive with the caveat), request a9be (matched-density control for 8f65/e40e + orientation ruling), hypothesis 9866 (orientation map).
- Submitted batch16 (24): 16 grid points rotated to Pc, plus 8 to Pa (work/gen16.py). Budget → 341.
- Next: when batch16 lands, tabulate orientation-min and orientation-average per deformation; post the b2-matched coverage with all of it. Then decide whether the remaining ~159 evaluations are worth spending (e.g. Pc-specific refinement, two-pair combos) or wrap up.

## 2026-10-14 17:43 UTC — orientation map: strong orientation dependence
- 7ba1 (4870 rotated to Pc): r46 1.0869, r56 1.0988, conv46 1.0869 → broker ROBUST_POSITIVE, top of the leaderboard. But 4870 itself (Pb) had r56 0.9969, so the sign changes with orientation and **it is not a result**.
- Pc r46 grows with |S2|: 2e45 1.0999, a6f6 1.0914, f78d 1.0827, 9d2a 1.0799. Pb shows the opposite trend.
- Pa: r46 1.030–1.035; 4400_rotPa (1765) r56 1.0167.
- Posted note ae67: the leaderboard top is an orientation artifact, the score will be the orientation-min, and I will not optimize in Pc.
- s21 values are identical across orientations (e.g. 4870 = 7ba1 = 1.0317), which confirms the rotated copies are equivalent on the symmetric cluster.
- Waiting on r56 for the remaining batch16 points. Then compute orientation-min and -mean per deformation, post b2-matched coverage, and decide whether to wrap up.
- Possible human-side check (to mention in the summary): the full T1 star (orientation-symmetric) at r46/r56. It cannot promote, since s21 is ~1.008.

## 2026-10-14 19:23 UTC — batch16 partial
- Pc (all converge-stage, conv46 = r46), r46 / r56:
  - 2e45 1.0999 / 1.1087 (its Pb r56 was 0.9748)
  - 7ba1 (4870) 1.0869 / 1.0988; fb19 (4400) 1.0859 / 1.0979
  - 842a (f78d) 1.0827 / 1.0955; 3658 (9d2a) 1.0799 / 1.0929; eab1 (e38e) 1.0791 / 1.0918
  - b2fa (f0d2) 1.0729 / 1.0842; 2838 (9c11) 1.0720 / 1.0822
- Pa, r46 / r56: 1765 (4400) 1.0347 / 1.0167; 3f21 (9c11) 1.0345 / 1.0204; 5686 (afc6) 1.0325 / 1.0182; 416e (f0d2) 1.0335 / 1.0193.
- Orientation-min so far: 160b has min r56 1.0191 (Pb) and min r46 1.0321 (Pa). The others are lower, because Pb r56 drops with |S2|.
- Pending: 2a48/3feb/5384/85cf/99b5/a6f6/f1b8 Pc and 3feb/5384/85cf/99b5 Pa (r56 stage); afc6 Pc (converge).
- No human reply to a9be / 4c74.
- Plan: once these land, post b2-matched coverage (orientation table, orientation-min as score) + abandon, final summary, `swarm done`. No more screens. The orientation-robust ceiling is ~1.02 on r56, and Pc gains are artifacts.

## 2026-10-14 20:10 UTC — DONE
- The batch16 Pa results are all in: r46 1.030–1.035, r56 1.016–1.020. Orientation table is in work/orient_table.txt (built by work/orient_table.py).
- Orientation-robust best: the 160b family (−0.11 / −0.005), with min r46 1.0321, r56 1.0191, s21 1.0207 → SUGGESTIVE.
- Posted result 41e2 (b2-matched coverage, 110 req, 105 P / 5 F), abandon 5a89, and `swarm done` (note ab3f) using work/summary.md.
- Open: requests a9be (matched-density control + orientation ruling) and 4c74. 9bb2 and a51c (Pc) are still pending at r56.
- 159/500 evaluations unspent, on purpose (see summary).
- Loop stopped.
