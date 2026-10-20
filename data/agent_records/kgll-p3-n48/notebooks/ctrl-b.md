# ctrl-b notebook

Started 2026-10-14T10:26:50+00:00.

## 2026-10-14 11:15 — wakeup 1: orientation + map1
- Read theory §1–6.4, pilot 40, progress 46, ADR-0040. Parent w1c: Δ s21 2.2586e-4, r56 2.590e-4.
- Tooling: `work/gen.py` (stars in solver 120° basis; `make_input(blocks)`), inputs in `work/gen/<family>/`.
  12-member shells (|G|²=7,13,19,21) used whole; `gen.chiral_halves` splits them into C6 orbits if needed.
  `swarm show REQ` → request.source gives the file name.
- Normalization: O_s, F_p unit-mean-square ⇒ max|Reγ| ≈ 3α for 6-member stars. α=0.05 on S1,T1 ⇒ M2k ratio 0.9995 (nearly neutral).
- Posted hypothesis map1 (20261014T111428.153Z_ctrl-b_hypothesis_3e47); submitted 64 single-block steps
  (10 shells×T1 + shells1,3,4×T2,T3; α=±0.05, β=±0.05). Budget 64/500.
- Next: collect map1 → pick positive-slope blocks → combined search (CMA-ES / coordinate) with explicit box.

## 2026-10-14 11:35 — wakeup 2: map1 collected, map2 submitted
- Collector: `python3 work/collect.py [family]` (caches swarm show).
- map1 (64): shells |G|²≥7 FAIL at 0.05 (manifold breaks; β → R≈0). S3/S4 β mostly FAIL. S1 benign.
  Positives: β[S1,R4]−.05 1.0191 (31cb); α[S1,R3]+.05 1.0109; β[S1,R4]+.05 1.0081; α[S1,T1]−.05 1.0080; α[S1,R4]±.05 1.006; α[S3,R4]+.05 1.005.
  Naming: my T1/T3/T4 = |R|²=1,3,4 (brief's T1/T2/T3).
- Parent Δ/Δ_LLL = 1.24 only (M2=10): M2 law far from saturated.
- Posted result+coverage (f0d4), hypothesis map2 (8754); submitted map2 (25): line scans b4 to −0.15, a3 to +0.15, combos, S7/S9 ±0.01.
- Next: if additive, CMA-ES in S1×{T1,R3,R4}×{α,β} (+S3 α) box |α|,|β|≤0.15.

## 2026-10-14 11:50 — wakeup 3: map2 collected
- map2 (25): P_b4m_a3p (β[S1,R4]−.05+α[S1,R3]+.05) **1.0308** (f6e9) and P_b4m_a1m 1.0254 (0726) → promoted to s21c (same value) then r46 pending.
  Roughly additive pairs, but triple (b4m+a3p+a1m) 1.0169 and a3p+a1m 1.0039: a1 and a3 conflict.
- β[S1,R4] even part: +1.4 % at |β|=.05, −11.6 % at .10 (−.15 FAIL). Sharp optimum |β|≈.05. α[S1,R4] +.10 → 1.018 (better than +.05).
  α[S1,R3] +.10 1.0151, +.15 0.976. α[S1,T1] −.10 0.992.
- S3 α=.10 bad (0.57, 0.75 FAIL). S7/S9 at ±0.01: all < 1 (β −5…−9 %). Outer shells closed; P_all6 (with S3) FAIL.
- Worry: R4 = 2×T1 harmonics alias on 4×6 (e^{iπ i}); watch r46 for f6e9/0726.
- Launching sob1: 48 Sobol in S1 6-D box a1[-.10,.05] a3[-.05,.12] a4[-.05,.15] b1[±.03] b3[±.08] b4[-.08,.06] + 12 targeted.
- 11:51 submitted sob1 (60 queued), hypothesis 98eb.

## 2026-10-14 12:20 — wakeup 4: first suggestive, sob1, gp1
- f6e9 (β[S1,R4]−.05, α[S1,R3]+.05): s21 1.0308, r46 1.0380, r56 **1.0062** → suggestive (all > 1, < 1.05). 0726: r56 0.9934 ✗.
- sob1 best: **sob1_19** (a1 −.040 a3 −.040 a4 +.098 b1 +.017 b3 +.033 b4 −.003; req 4934) s21 1.0552, r46 1.0562, r56 pending.
  sob1_41 (a4 +.109, b4 −.043, b1 +.022) 1.0443; several tg points 1.026–1.039 promoted.
- Tools: `dataset.py` (S1 x-vector from input files; cache), `surrogate.py` (sklearn GP ARD), `mkbatch.write(family, {name: x})`.
  Run with `uv run --project "$MOIRE_MAIN" --no-sync python`.
- gp1 submitted (19): GP mean max + 12 Thompson + 6 around sob1_19 incl. amp-only / phase-only split.

## 2026-10-14 12:40 — wakeup 5: r56 is binding; fac1
- r56 results: sob1_19 0.998 ✗ (a4-heavy region doesn't transfer); sob1_41 0.966 ✗; dfc0 0.997 ✗; 0726 0.993 ✗.
  Transferring: **84b6 tg_b4m_a3p_b3p03 (a3 .05 b3 .03 b4 −.05): 1.0371/1.0657/1.0449**; 21d2 (a3 .10 b4 −.05) 1.026/1.033/1.040;
  9471 (a1 −.03 a3 .05 b4 −.05) 1.026/1.045/1.024; d946 1.026/1.030/1.024; f6e9 1.031/1.038/1.006; 426d (b4 +.05!) 1.037/1.034/1.005.
- gp1 at s21: gp1_04 1.0728 (r46 1.060), l19_b4m03 1.0699 (r46 1.069), l19_ampOnly 1.054 (r46 1.064); r56 pending.
- fac1 submitted (17): 2^(5-1) around c=(a1 −.015, a3 .075, a4 0, b1 0, b3 .03, b4 −.05). Hypothesis a43a.
- Plan: build r56/r46 surrogates from promoted points; optimize min(R46,R56) not s21.

## 2026-10-14 13:03 — wakeup 6
- gp1 r56: l19_b4m03 1.0015, l19_a3m07 1.0084, gp1_04 0.973, ampOnly 0.997, x125 0.981. a4-heavy ⇒ fails 5×6. gp1_00 1.028/1.060/1.030.
- fac1 s21 main effects: a1 +.8 %/.02, a3 −2.0 %/.025, b1 +1.8 %/.015, b3 −3.2 %/.02, b4 +.4 %/.01; centre 1.0235.
  5 fac1 points promoted (r56 pending).
- Promotion requires s21 ≥ 1.02 → objective = max min(r46,r56) s.t. s21 ≥ 1.02.
- hand1 (12, hyp 7008): a3/b3 up for r56 with b1 to hold s21; 4 phase-only combos (b1,b3,b4).
- Budget 160 + 12 = 172.

## 2026-10-14 13:35 — wakeup 7
- hand1 s21: **ph2 phase-only (b1 .015 b3 .03 b4 −.05) 1.0516**, h4 (84b6+b1 .015) 1.0500, ph4 1.043, h7 1.0375, ph1 1.037; ph3 (b1,b4 only) 0.982 (nonadditive!).
  h1/h2/h3 (more a3/b3) < 1.02 on s21 → not promotable. fac1_center r46 1.071 (r56 pending); fac1_02 r56 1.014, fac1_08 1.0135.
- New tool `work/joint.py`: joint (G,R) orbits via 2-member pair blocks; aligned/oblique split; verified γ identical to star×star (2e-16).
- jo1 submitted (12; hyp posted): aligned/oblique contrasts around 84b6 and ph2.

## 2026-10-14 13:52 — wakeup 8
- jo1: jop2_b4_ob (phase-only) 1.0742/r46 1.0658; jo84_b4_ob 1.062/1.078; jo84_a3_al 1.057/1.086; jo84_b3_al 1.041/1.070; jop2_b3_al 1.053/1.060.
  Opposite contrasts lose (a3_ob 1.013, jop2_b4_al 1.004). → aligned α₃/β₃ and oblique β₄ help.
- hand1 r46: h6 1.075, h7 1.068, h4 1.066, ph2 1.061, ph1 1.060. Many r56 pending (5×6 queue is the bottleneck).
- jo2 submitted (11): combos of helpful contrasts; doubled contrasts; phase-only variants.

## 2026-10-14 14:20 — wakeup 9: first robust-threshold candidate
- **4c68 jo84_a3_al: s21 1.0567 / r46 1.0856 / r56 1.0635 PASS → conv46 pending.** (α₃ aligned .10 / oblique .025, β₃ .03, β₄ −.05)
- jo2 r46: a465 (a3al+b3al+b4ob) 1.087/1.108; adea (a3 aligned-only .15) 1.072/1.100; dfb1 1.083/1.096; 6ff7 1.069/1.088. r56 pending.
- Phase-only falls at 5×6: jop2_b4_ob 0.9987, ph2 1.008, jop2_b3_al 1.007, ph4 0.986.
- jo84_b4_ob r56 1.038; h4 r56 1.027.
- collect.py: now refreshes only non-final requests (was timing out).
- jo3 submitted (11, hyp d0f9). Posted request for matched-density static control for 4c68.

## 2026-10-14 14:47 — wakeup 10: claim posted
- **4c68 finished: conv46 1.0856 PASS → broker claim robust_positive.** Posted claim 94ae.
- conv46 Δ == r46 Δ to 1e-9 (parent too) — flagged in claim as possible override not applied; asked human to confirm.
- Broker slow (tick 273 s); jo2 9× at r56, jo3 11 in screen queue. No new submissions this tick.
- Next: when jo2 r56 lands, best min(r46,r56) → refine; consider "strong" (≥1.10 on r46, r56, conv46).

## 2026-10-14 16:32 — wakeup 11: STRONG candidate
- **dd93 x2_a1ob: 1.1387 / 1.1536 / 1.1048 / conv 1.1536 PASS → broker claim `strong`.** Posted claim 92fd.
  = a465 + α₁ (|R|²=1) pure joint contrast (aligned −.03, oblique +.015 star-equiv).
- Others robust (r56 < 1.10): b7d3 (α₄ aligned) 1.113/1.140/1.071; cd1a 1.100/1.122/1.074; e00c 1.096/1.132/1.067; adea 1.072/1.100/1.076; 571f; a465 1.087/1.108/1.061; dfb1.
- x1 (α₁ contrast other sign) 1.036/1.063/1.016; x5 β₁ ob 1.109/1.117/1.042; e3 β₄ ob ×2 r56 1.038.
- jo4 submitted (11): α₁ contrast ×2/×3, combos with α₄/α₃ aligned, ×1.2, amp-only / phase-only split, 84b6+α₁ only.
- Budget ≈ 217 + 11 = 228.

## 2026-10-14 17:00 — wakeup 12
- jo4 (s21/r46; r56 pending): y2 a1 contrast ×3 (71b2) 1.241/1.248; y7 ×2+a4al (8149) 1.221/1.240; y8 (37b9) 1.209/1.226; y5 (16f4) 1.182/1.209;
  y1 ×2 (8a8b) 1.190/1.2005; y6 ×1.2 (dc94) 1.160/1.190; y3 (147b) 1.167/1.189; y4 (1464) 1.151/1.169; y11 84b6+a1ob (1387) 1.090/1.110;
  amp-only (67d8) 1.075/1.066; phase-only (6390) 1.063/1.077 → synergy.
- jo5 submitted (13): α₁ contrast ×4..×8, pure α₁ contrast alone, combos.

## 2026-10-14 17:28 — wakeup 13: α₁ contrast is the mechanism
- jo4 r56: y2 (71b2) **1.194** (conv46 1.248), y7 1.161, y8 1.168, y1 1.149, y5 1.131, y6 1.123, y3 1.116, y4 1.119, y11 1.089.
- jo5 s21/r46: α₁ contrast on dd93 base: d=−.06 1.292/1.297; −.075 1.343/1.347; −.09 1.393/1.398; **−.12 1.491/1.502**.
  pure α₁ contrast alone: d=−.045 1.146/1.137; d=−.09 1.288/1.285. z11 (a1×3 + a4al2) 1.303/1.315.
  α₁ star-uniform ±.02 on y2: ~no effect. β₁ contrasts: ±1 %.
- M2^(k)/M2 decreases along α₁ contrast (0.957 at d=−.54) — not density sharpening.
- jo6 (12, hyp 49b6): pure α₁ contrast d to −0.54; dd93 base to −0.36; + α₄ aligned; opposite sign.
- `work/matched.py`: matched-density static control (k-avg unit-mean diagonal density, |G|²≤48, C6-sym).
  Submitted controls 0b0c (dd93), bfeb (71b2) on s21,r46,r56 (--control). Note posted.

## 2026-10-14 17:58 — wakeup 14
- **Controls: ctrl_dd93 s21/r46 0.9994/0.9994; ctrl_71b2 0.9993/0.9993** (r56 pending) → beyond M2.
- jo5 r56: z4 (d −.12 on dd93 base) 1.4184 (conv 1.5019); z3 1.329; z2 1.284; z1 1.239; pure z6 1.263; z11 1.211.
- jo6: base d −.18 1.681/1.720; −.27 1.936/1.995; −.36 1.962/2.228; pure −.27 1.633/1.942; −.36 1.631/2.188; −.54 FAIL; +.09 0.705.
  s21 saturates ~d −0.3; r46 keeps rising.
- joint.py: `blocks_general({(s,t,kind):(a,b)})`, aligned = rel angle 0/90°. Verified = S1 version.
- jo7 submitted (13).

## 2026-10-14 18:25 — wakeup 15
- Controls r56: dd93 0.9994, 71b2 0.9992 → beyond-M2 on all clusters. Posted result aa0e (mechanism).
- jo6 r56: 8e3e (b360) 1.962/2.228/2.097; 9a82 1.947/2.009/1.875; 8c4c 1.936/1.995/1.856; pure 9d4d 1.631/2.188/2.012.
- jo7: w3_b310 (6148) 1.962/2.103/1.966; S4T1 −.02 on p180 1.622/1.857; S3T1 +.02 1.609/1.809; β×2 s21 2.075/r46 1.950;
  amp-only b270 1.708/2.002; a3al/a4al2 small effects; β₁ contrasts null.
- jo8 submitted (12).

## 2026-10-14 18:52 — wakeup 16
- **jo8 best dc7c (v7_b310_s4s3_beta15): 2.234/2.368/2.332 PASS** (conv pending). b157 1.957/2.383/2.264.
  β×1.5 lifts s21 (binding). S3T1 +, S4T1 − contrasts add ~+0.3 on r46.
- jo7 r56 all in: 6148 1.966; fbb4 1.714; 7d7d 1.680; f822 1.857; d73e 1.862; adc7 (amp-only b270) 1.820.
- jo9 submitted (12). Budget 285.

## 2026-10-14 19:20 — wakeup 17
- jo8 r56 in: dc7c 2.234/2.368/2.332 (conv 2.368); dcf9 1.865/2.514/2.411; cf9c 1.926/2.440/2.324; ed7d 1.944/2.412/2.295.
- jo9: **e010 β×1.75: 2.425/2.339/2.337** (best min); b141 β×2 2.540/2.301/2.331; 7ace d−.27 2.262/2.287/2.229.
  r46 boosters (β×1.5 base): S3T3 −.02 2.221/2.448; a3al 2.229/2.447; s3 .04 2.179/2.478; d −.36 2.164/2.458.
  u3/u6 (S3/S4 ×2) FAIL s21: splitting/Δ 0.103 — manifold is the limiting gate at large deformation.
- jo10 submitted (12). Budget 297.

## 2026-10-14 19:50 — wakeup 18
- jo9 r56: 37fc (d−.36) 2.164/2.458/2.453; 48a0 2.179/2.478/2.475; e010 2.425/2.339/2.337 (conv 2.339); b141 2.540/2.301/2.331.
- jo10 s21/r46 (r56 pending): t6 bb91 2.389/2.541; t11 5046 2.374/2.538; t5 433a 2.400/2.484; t7 β2 8bbc 2.580/2.470; t12 2.193/2.607.
  s21 splitting/Δ 0.065–0.094 → close to 0.1 gate.
- joint.py: `blocks_chiral` (aligned / obl+ / obl−). jo11 submitted (12): chiral contrasts.
- Budget 309.

## 2026-10-14 20:16 — wakeup 19
- jo11: chiral α null (pure base ≤0.3 %; t6 ≤2 %). **Chiral β S1×T1 e=−0.02 (fc93): 2.553/2.673, s21 split 0.065**; +0.02: 2.222/2.406.
- jo10 r56 still pending (5×6 queue).
- jo12 submitted (12): chiral β scan + neighbours + pure-base attribution. Budget 321.

## 2026-10-14 20:36 — wakeup 20
- jo12 s21: **8600 (fc93 + S3T1 chiral β −.02) 2.961**, split .046; b2f2 (b11 −.06) 2.875; 63c5 (−.04) 2.715; 805b (b13 −.02) 2.686;
  b14 ±.02 null; b31 +.02 2.128; pure+b11 −.05 1.777 (+.05 1.256). Chiral β cleans manifold.
- Withdrew 18 dominated jo10/jo11 requests (chiral α, t1–t4, t8–t10, c7) to free the 5×6 queue.
- jo13 submitted (12). Budget 333.

## 2026-10-14 21:10 — wakeup 21
- jo12 complete: **8600 2.961/3.000/2.712 (conv 3.000)**; b2f2 2.875/2.930/2.657; 63c5 2.715/2.803/2.556; fc93 r56 2.454.
- jo13: **h7 58ff 3.717/3.608/3.220**; h5 d9ed 3.708/3.601/3.198; f1c8 (S4T1 chi −.02) 3.588/3.503/3.129; h3 3.496/3.429; h9 (S4T1 +) 2.617.
  pure base + chiral: h10 1.921/1.934; h11 2.128/2.144. Splitting/Δ s21 down to 0.023.
- jo10 r56 in: t3 2.489, t9 2.430, t4 2.415, t10 2.404 (all superseded).
- Controls submitted: 9ada (8600 & h7 share matched density, M2 9.779; 4658 dedups).
- jo14 submitted (12). Budget ≈ 348.

## 2026-10-14 21:45 — wakeup 22
- Control 9ada (8600/h7): 0.990/0.990/0.989 → beyond-M2. h7 complete (conv 3.608) → claim 5117 posted (+ coefficient correction note 09fd).
- jo14: **g5 (S4T1 chi −.04) 4.530/4.327/3.855**; g2 (S3T1 −.10) 4.405/4.182/3.725; g6 4.452/4.235/3.754; g12 S4T3 chi −.02 3.942/3.775; g10 S3T3 3.904/3.749.
- jo15 submitted (12). Budget 360. Remaining 140.

## 2026-10-14 22:16 — wakeup 23
- jo14 complete: g5 4.530/4.327/3.855 (conv 4.327); g2 4.405/4.182/3.725; g6 4.452/4.235/3.754; g12 3.942/3.775/3.320.
- jo15 s21: **f12 5.854**; f2 5.628; f3 5.486; f10 (S9T1 chi −.01) 5.421 vs f5 5.160; f9 pure+all 2.975.
- jo16 submitted (12): scale chiral vector ×1.25..×2.5, S9T1 chiral, S3T4 chiral. Budget 372.

## 2026-10-14 22:50 — wakeup 24
- jo15 complete: f12 5.854/5.760/5.011 (conv 5.761); f2 5.628/5.560/5.021; f10 5.421/5.297/4.617.
- jo16: **e7 (×1.5 V + S9T1 chi −.015) 6.684/7.542/6.561**; cd67 ×1.5 6.571/7.182/6.176; ×2 6.354/8.108; ×2.5 5.293/8.306 (split .091).
  e9 (S3T1 −.18) 6.421/6.593/5.742; e8 6.372/6.468/5.645. s21 turns over ×1.5–2.
- jo17 submitted (12). Budget 384.

## 2026-10-14 23:22 — wakeup 25
- jo16 complete: e7 6.684/7.542/6.561 (conv 7.542); e3 ×2 6.354/8.108/6.936; e4 ×2.5 5.293/8.306/7.058; e11 6.071/8.336/7.246.
  conv46 ≠ r46 at large deformation (e4 8.3074 vs 8.3059) → overrides applied; caveat resolved (posted in hyp jo18).
- jo17: **d8 (no S3T3/S4T3 chiral) 7.063/7.293/6.909**; d3 6.721/7.883/6.931; d10 6.627/7.848/6.856; d6 FAIL (split .11).
- jo18 submitted (12). Budget 396; 104 left.

## 2026-10-14 23:57 — wakeup 26
- jo17 complete: d8 7.063/7.293/6.909 (conv 7.294); d7 6.531/8.385/7.684; d4/d5 r56 7.40.
- jo18: **q10 (S12T1 chi −.02) 7.335/7.681/7.347**; q5 7.183/7.751/7.658; q8 7.186/7.643/7.384; q6 7.163/7.667/7.453.
- jo19 submitted (12). Budget 408; 92 left. Plan: one more round, final control (3), coverage/done.
- Note: 12-member shell chiral normalization in joint.py uses /3 (true star-equivalent would be /(3√2)).

## 2026-10-15 00:30 — wakeup 27
- jo18 complete: q10 7.335/7.681/7.347 (conv 7.681).
- jo19: **p1 (S12 −.03) 7.448/7.832/7.523**; p10 (S7 chi −.01) 7.412/7.889/7.655; p3 7.405/7.912/7.691; p9 7.436/7.945/7.381.
- Plateau ≈ +0.1/round. jo20 submitted (12, last round). Budget 420. Then control + coverage + done.
- 00:34 jo20 in flight; p1 complete 7.448/7.832/7.523 conv 7.831. Waiting.

## 2026-10-15 01:07 — wakeup 28: plateau; closing out
- jo20: no improvement over p1 (best z8 7.376/7.941/7.640; z5 6.993/8.241/7.795; z7 FAIL split .14). s21 manifold-limited.
- **Final best p1 (2ffb): 7.448/7.832/7.523, conv46 7.831, all PASS.**
- Control fc99 for p1 = same matched density as 9ada (same amplitude) → expect 0.990/0.990/0.989 (dedup).
- Submitted split (2): p1 amplitude-only (00eb), phase-only (9b64).
- Next: coverage result post (all families), final claim for p1, swarm done.

## 2026-10-15 01:35 — wakeup 29: done
- split: p1 amp-only 1.82 FAIL (split .16), phase-only 1.35 FAIL (split .22). Control fc99 0.990/0.990/0.989.
- Posted final claim 8c8b (req_2ffb strong, beyond-M2), coverage result 3524 (+ count correction note).
- 422/500 charged. Plateau reached (Nk=21 manifold-limited). Running `swarm done`.
