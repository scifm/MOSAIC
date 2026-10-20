# ctrl-b notebook

Started 2026-10-15T04:13:59+00:00.

## 2026-10-15 04:20 — wakeup 1: setup + batch 1a
- Read brief, docs 40/46, ADR-0032, kdep_envelope. Parents s21: w3 Δ=4.5714e-4, w2 Δ=3.2273e-4.
- Prior data (doc 46, Nk21, w3): S1T1 α=+0.05 → +1.85 %, α=−0.05 → −9.04 %, β=+0.05 → −4.4 %; S4T1 α=+0.05 → −3.75 %.
  => large linear response, negative curvature. 024 pilot: +0.5 % at 4x6 reversed to −0.9 % at 5x6.
- Tooling: work/gen.py (make_input(parent, [(Sq, Tp, α, β)...]); stars in solver 120° basis; 12-member shells split S7a/S7b etc.
  g_cutoff = max(4, star box), n_mesh 48). `swarm check` takes ~1 s.
- Posted hypothesis 85e5 (coord-scan-w3). Submitted batch1a: 40 reqs = 10 shells × T1 × {α ±0.10, β ±0.05}. ids in work/batch1a.ids.
- Next: collect, fit per-direction linear/quadratic response, then batch 1b (T2,T3) and combinations.

## 04:40 — wakeup 2: batch1a results + cutoff finding
- batch1a (g4): every T1 direction is negative except S1T1 α+0.1 (1.0028). High shells (|G|²≥7) collapse the gap (R 0.3–0.7, several FAIL). β± symmetric → no linear phase term (symmetry).
- Theory (notes §7.5–7.6): the static LL0 parent is exactly ideal; any k-dependence adds an ideality defect Var_r(∂+γ) at second order. So any gain must be first-order.
- KEY: g_cutoff=4 is unconverged. g8: S1T1 α+0.1 → 1.033 (6e0b, promoted to confirm21), S3T1 α+ → 1.018, S7T1 β+ 0.66→0.88, S13 β+ 0.36→0.64(g6)→0.67(g8). Posted note.
- conv2 queued: g6/g10/g12, n_mesh 64 on S1T1_ap; S13/S7/S3 at g10/12.
- Added gen.make_pair_input / orbit_terms: joint (G,R) orbit classes by relative angle (S1×T1: ±30°, 90°; chiral ±). Verified equal to the full star (1e-17) and C6 covariant.
- Next: pick g_cutoff from conv2, redo low-shell scan (S1,S3,S4 × T1,T2,T3) and the orbit decomposition at converged cutoff.

## 04:55 — wakeup 3: cutoff converged; S1T1 α+0.1 promoted
- conv2: S1T1 α+0.1 identical (1e-6) at g6/g8/g10/g12 and n_mesh 64; S13 β converged at g8 (0.6709), S7 β g8=g12.
  Rule adopted in gen.py: g_cutoff = max(6, 5 + star box), n_mesh 48.
- S1T1 α+0.1 (6e0b, g8): s21 1.0330, s21c 1.0330, r46 1.0476 PASS; r56 pending. Withdrew duplicate g6/g10/g12n48 copies (06e1, dc97, 957d); kept g12n64 (edae) as a convergence twin.
- batch2 (52 reqs, ids work/batch2.ids): S1T1 α line {0.05,.15,.2,.3}; S1/S3/S4 × T2/T3 α±0.1; S3/S4T1 α−; S7..S21 × T1 α±0.1 (converged g);
  joint orbits S1×T1 (±30°, 90°) and S3×T1 (0°, ±60°): α pair-coef ±0.05, β ±0.03 on the chiral classes.

## 05:20 — wakeup 4: ROBUST_POSITIVE found
- batch2: full-star T2/T3 all negative (0.81–0.97); high shells α± negative (0.49–0.90); S1T1 α line: 0.05 → 1.022/1.026/1.026, 0.15 → 1.032/1.063/1.045 (suggestive), 0.2 → 1.020, 0.3 → 0.965.
- **Joint orbits**: S1T1 o+90 α+0.05 (c082): s21 1.1050, r46 1.0879, r56 1.0919, conv46 1.0879, all PASS, C=1 → broker claim robust_positive.
  S3T1 o0 α+0.05 (06e5): 1.0995 / 1.0919 / 1.0884 / 1.0919 → robust_positive. ±30°/±60° classes negative both signs; α− on the good classes 0.83–0.84.
- Posted claim 3a6e. Mechanism controls (--control, family mdctrl-w3, s21/r46/r56): 5495 (BZ-avg density of c082, M2 3.6336), a6fa (of 06e5), 5ead (ρ^p with M2=3.686). work/matched.py, work/powctrl.py.
- batch3 (81, family orbit-w3, hypothesis posted): line scans, combo, β on the two classes, orbit decomposition of 11 other (shell×T) pairs.
- Next: fit, combine positive classes, push for strong (≥1.10 on r46/r56/conv46). Then w2.

## 05:50 — wakeup 5: STRONG; mechanism controls ≈ 1
- batch3: S1o90 α line 0.03/0.05/0.08/0.11/0.15 → s21 1.062/1.105/1.173/1.244/1.333; r56 at 0.15 = 1.261; conv46 1.284. S3o0 similar (0.15: s21 1.332, r46 1.334).
  combo (a,a): 0.05 → 1.178 min, 0.08 → 2c51 1.343/1.300/1.288/1.300 (strong). β on o90/o0 ±0.03 slightly negative (0.96–0.99).
  Other orbit classes on S4T1, S1T2/T3, S3T2/T3, S4T2/T3, S9T1, S12T1: all 0.90–0.99 (no positive class). S7aT1 o−49 +0.05 → 1.018; S7bT1 o+49 +0.05 → 1.026 (r46 1.034).
- Controls: 5495/a6fa (BZ-avg density) 1.0010 on s21/r46/r56; 5ead (ρ^p, M2=3.686) 1.0116. ⇒ beyond-M2.
- Posted claim (strong). batch4 (26): α to boundary (M2 cap binds α≈0.56 single, 0.26 pair), S7 pair, β on α=0.15. ctrl2: avg/pow controls for 2c51 & 4db7.

## 06:20 — wakeup 6: optimum along S3 G∥R ≈ 0.25
- batch4 (w3): S3o0 0.20 (52d9) 1.452/1.413/1.382/1.412; **S3o0 0.25 (248a) s21 1.5145, r46 1.4159, r56 1.4992, conv46 1.4145** (best min so far);
  S3o0 0.30: s21 1.506 r46 1.367; 0.40: 1.290/1.112; ≥0.5 FAIL (PES eg < 0.5, Laughlin lost).
  S1o90: 0.20 → 1.369/1.386/1.306; 0.25 → 1.331/1.334; 0.30 → 1.234/1.204; 0.40 → 0.94; ≥0.5 FAIL.
  combo (0.05,0.15) 041b: 1.421/1.410/1.389/1.410; (a,a) ≥0.2 collapses. β ±0.05 on S1o90 0.15 doesn't help.
  S7b o+49 0.10 (2860): s21 1.026, r46 1.109. S7 pair (achiral sum) worse.
- Controls: avg-density 746d (2c51) 1.0156, d7b4 (4db7) 1.0093; ρ^p M2-matched 4.277 → 1.125 (00a0), 4.223 → 1.115 (efee). Winners at same M2: 1.29–1.30 / 1.26–1.28.
- PES entanglement gap decreases monotonically with amplitude; Laughlin lost around M2(k) ≈ 8–10.
- batch5: w3 2D refine (a1∈{0,.03,.06,.10} × a3∈{.18,.22,.25,.28}), S7+S3 combos, T1 orbits of S13a/b,S16,S19a/b,S21a/b (±0.05); w2 transfer (hypothesis 2a51).

## 06:55 — wakeup 7: w3 plateau ~1.42; w2 prefers different orbits
- w3 2D refine: best min so far **0e76 (S3o0 0.22): s21 1.4873, r46 1.4199, r56 1.4294, conv46 1.4191**; f0c6 (S1o90 .03 + S3o0 .18) min 1.4113; 248a (0.25) min 1.4145.
  Adding S1o90 on top of S3o0 ≥ 0.18 hurts r46. S7± on top of S3o0 0.2 hurts r46 (1.107). Pending r56/conv46 for several.
- w3 T1 orbit coverage of S13a/b, S16, S19a/b, S21a/b at ±0.05: all 0.87–0.995 (none positive).
- w2: w3-winning classes negative (S1o90 0.97/0.94/0.85; S3o0 0.97/0.88/0.53). **S1T1 o±30 α=−0.05: 9172 s21 1.0376 r46 1.0441 r56 1.0432; fc85 1.0347/1.0447/1.0430.** S3 classes all ~0.97.
- batch6w2 (37): o±30 pair/single α− line to −0.2; T1 orbits of S4, S9, S12, S7a, S7b at ±0.05.
- Budget 312 + 37 = 349 charged.

## 07:25 — wakeup 8: w2 strong
- w3 all promotions done; best min R: 0e76 (S3o0 0.22) 1.4191 (conv46); f0c6 1.4113; 248a 1.4145; 52d9 1.3823.
- **w2: S1T1 o±30 pair α=−0.10 (69d9): s21 1.1120, r46 1.1473, r56 1.1298, conv46 1.1473 → strong.** pair −0.05 (4c65) 1.082/1.088/1.081; −0.15 (bbee) 1.085/1.115/1.111; −0.2 → 1.000.
  single o+30: −0.10 (09bd) 1.053/1.078/1.070; −0.15 r46 1.095. S4T1 o90 +0.05 (ce28): s21 1.059, r46 1.141, r56 1.091. S7 chiral o±11, o±49: small +1–2 % at s21 (77ea r46 1.085).
  S4 ±30, S9, S12 orbits negative. 
- batch7w2 (28): pair −0.08/−0.12, S4o90 line, pair+S4o90 combos, S7o11 pair, β on o±30, S1×T2/T3 orbits.
- ctrl3 (w2 controls on 69d9): avg density (M2 2.491) and ρ^p+ε (p=1.056, ε=0.005, M2 2.583). powctrl.py now takes EPS.

## 07:50 — wakeup 9: w2 best 0bc5; phase-only hint on w2
- w2: **0bc5 (o±30 pair −0.10 + S4o90 +0.05): s21 1.1623, r46 1.2081, r56 1.1893, conv46 1.2081** (best min). 5251 (−0.08,+0.05) s21 1.149 r46 1.212 r56 1.195; e299 (−0.08,+0.08) r46 1.241 but s21 1.138.
  pair −0.12: 1.108/1.149/1.135. S4o90 alone: s21 ≤ 1.06 but r46 1.14–1.21 (large cluster spread). S7o11 pair +0.05: s21 1.061 r46 1.143.
  T2/T3 S1 orbits on w2 all negative (0.93–0.99).
  **Phase-only on chiral S1T1 classes (w2)**: o+30 β−0.03 1.0059, o−30 β+0.03 1.0094 (mirror pair), opposite signs 0.95. w3 chiral phase was all negative.
- w2 controls (69d9): avg density ae38 s21 0.9974 r46 0.9975; ρ^p M2-matched 664b 1.0203 — vs 1.11–1.15 for the winner ⇒ beyond M2 on w2 too.
- batch8 (50): w2 phase-only scan (single, mirror pair to 0.10), 0bc5 + phase/S7, 2 refinements; 20 random ±0.03 perturbations on 10 neighbouring classes around 0e76 (w3) and 0bc5 (w2) (log: work/batch8_perturbations.json).
- Budget 383 + 50 = 433.

## 08:20 — wakeup 10: phase-only null on w2; perturbations improve both optima
- w2 phase-only: mirror pair (o+30 β−b, o−30 β+b): 0.03 → 0.978, 0.06 → 0.876, 0.10 FAIL; single o−30 β: 0.03 → 1.009, 0.06 → 0.992, 0.10 → 0.918. Max ≈ +1 % at s21 only → phase-only null (all parents).
  0bc5 + phase pair 0.03 (518a): s21 1.164, r46 1.269 (adds on top of amplitude).
- Random ±0.03 perturbations: w3 rp11 (722a) s21 1.479 r46 1.501 r56 1.447; rp15 (028f) 1.483/1.445/1.454; rp09 (9078) 1.466/1.437/1.467. w2 rp09 (38bb) 1.213/1.245/1.242; rp13 (cb3e) 1.209/1.245/1.223.
- Next: once r56 for all perturbations is in, fit linear model (min-cluster and per-cluster) → gradient steps. 67 evals left.

## 08:45 — wakeup 11: gradient step from perturbations
- w3 perturbations: rp11 (722a) s21 1.479 r46 1.501 r56 1.447 conv46 1.501 (min 1.447), rp15 (028f) min 1.445, rp09 (9078) min 1.437; base 0e76 min 1.419.
  w2: rp09 (38bb) min 1.213, rp13 (cb3e) 1.209, rp07 1.191 (s21); base 0bc5 1.162.
- work/gradfit.py: per-cluster linear fits (resid 0.01–0.03) → LP max-min step in a trust box. batch9: steps h = 0.015/0.02/0.03/0.04 for each parent (8 evals).
- Posted coverage result for coord-scan-w3 (closed).
- Budget 441/500 after batch9.

## 09:12 — wakeup 12: w3 gradient step works
- w3 gradstep (from 0e76 along LP max-min direction of 10 classes): h .015 → s21 1.510 r46 1.472; .02 → 1.521/1.490/1.486; .03 → 1.548/1.528/1.514; **.04 → 1.581/1.566/1.544** (pred 1.555). conv46 pending.
- w2 gradstep: s21 falls with h (1.183, 1.180, 1.162, 1.126) while r46/r56 rise → no improvement of min; w2 best stays rp09 (38bb) min 1.213.
- batch10: w3 h=0.05, 0.06, 0.065 (Σ|α| = 2.49, boundary binds at h≈0.065 in the pair representation: each orbit class = 3 entries); w2 0bc5→rp09 direction ×1.5, ×2.
- Budget 446/500.

## 09:40 — wakeup 13: w3 gradient line reaches Σ|α| boundary still rising
- w3 gradstep conv46 done: h.04 (f6f2) 1.581/1.566/1.544/conv 1.566. h.05 (a274) s21 1.620 r46 1.605; h.06 (982d) 1.663/1.643/1.606; **h.065 (5480, Σ|α|=2.49) 1.686/1.662/1.621**, conv46 pending. M2(k) ≈ 4.67 (decreasing along the line).
- w2: gradstep min stays ≤ 1.183 (s21); rp09dir ×1.5 (6389) 1.209/1.262/1.265 ≈ rp09; ×2 s21 1.184. w2 best: 38bb min 1.2128.
- batch11 (4): L1-budget LP steps (work/l1step.py): budget 1.84 (= 2.5 − S3 base) cap .10 / .15, budget 1.38, half step.
- Budget 450/500. Reserve ~15 for confirmation/controls of the final w3 winner.

## 10:10 — wakeup 14: final w3 winner 5480; controls; last perturbation round
- **w3 5480 (gradstep h=.065, Σ|α|=2.49): s21 1.6857, r46 1.6616, r56 1.6210, conv46 1.6618** — all PASS, strong. a274 (h.05) min 1.5745, 982d (h.06) 1.6057.
- L1-budget LP steps failed (extrapolation; S7 classes at ±0.1 → r56 0.88–0.98; cap .15 FAIL). Box direction is the winner.
- w2 rp09dir ×1.5 (6389) 1.2087/1.2622/1.2654/1.2622; ×2 s21 1.184. w2 best 38bb min 1.2128.
- Controls (s21/r46/r56): w3 b202 (BZ-avg density of 5480, M2 3.649), a175 (ρ^p, M2 4.669); w2 a7a5 (avg of 38bb, M2 2.525), 5a5d (ρ^p+ε=0.01, M2 2.823).
- batch12: 12 perturbations ±0.02 on 11 classes around the h=.055 point (Σ|α| ≤ 2.495), log work/batch12_perturbations.json → L1-reallocation step if the fit says so.
- Budget 474/500.

## 10:36 — wakeup 15
- **New w3 best: rp2_10 (1d93): s21 1.7117, r46 1.6625, r56 1.6578, conv46 1.6627** (min 1.6578). rp2_04 (a810) 1.670/1.651/1.629; rp2_11 (caae) 1.701/1.662/1.632.
- Controls 5480: avg density b202 1.0013–1.0018; ρ^p M2=4.669 (a175) 1.1945–1.1947. w2 38bb: avg a7a5 1.006 (s21/r46), ρ^p M2=2.823 (5a5d) 1.078–1.079 (r56 pending).
- Next: refit on rp2 (after r56) → final small L1-feasible step; M2-matched control for 1d93; then coverage posts + done. Budget 474.

## 11:00 — wakeup 16: final step
- rp2 round: linear fits around h=.055 have resid ≈ 0.002 (excellent). Best measured: 1d93 min 1.6578.
- w2 5a5d (ρ^p M2 2.823) 1.078–1.079 on all three; 38bb winner 1.213–1.245 ⇒ beyond M2.
- batch13: L1-feasible max-min steps cap .02 (pred 1.761) and .03 (pred 1.837), Σ|α| = 2.495. ctrl5: ρ^p M2 = 4.844 control for 1d93.
- Budget 474 + 2 + 3 = 479.

## 11:25 — wakeup 17
- finalstep cap .02 (7f0b): s21 1.7356 r46 1.7307; cap .03 (9539): 1.7503 / 1.7500; r56 pending. Control 9de0 (ρ^p M2 4.844 for 1d93): 1.2241–1.2243.
- batch14: exact-L1 LP steps cap .045 / .06 (extrapolated preds 1.95 / 2.05 — optimistic). Budget 481.

## 11:47 — wakeup 18: final winner, wrap-up starts
- cap .02 (7f0b) min 1.6885; cap .03 (9539) 1.7503/1.7500/1.7176/conv 1.7512; **exact-L1 cap .045 (6852): s21 1.7520, r46 1.7529, r56 1.7380** (conv46 pending); cap .06 (24a9) 1.701/1.708 → optimum ≈ .045.
- Controls for 6852 (M2^(k) 5.016): 0c15 (ρ^p M2 5.016), d9c2 (BZ-avg density, M2 3.651). Block saved work/final_w3_6852_block.json.
- Stopping optimisation (diminishing returns). Budget 487/500. Next: coverage posts for orbit-w3, orbit-w2, mechanism summary, final claim, swarm done.

## 12:10 — wakeup 19: DONE
- 6852 conv46 1.7544 → final w3: 1.7520 / 1.7529 / 1.7380 / 1.7544 all PASS, C=1, strong. Controls d9c2 (avg density) 1.0008–1.0025; 0c15 (M2-matched 5.016) 1.2523–1.2525.
- Posted: claim 33f4 (final w3), result d107 (orbit-w3 coverage), result 7f68 (orbit-w2 coverage). Earlier: fae2 (coord-scan-w3 coverage), f605 (cutoff note), claims 3a6e, ea67.
- Budget 487/500 charged. swarm done.
