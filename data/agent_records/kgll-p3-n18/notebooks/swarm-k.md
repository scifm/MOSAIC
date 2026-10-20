# swarm-k notebook

Started 2026-10-14T05:20:20+00:00.

## 2026-10-14 05:40 — wakeup 1: scope chosen, stage 1 submitted
- Read brief, docs 40/46, theory §6.4, board (a linmap; b/c joint orbits S1–S3; d chiphase (MT rule: all ladder clusters chiral; α physical-linear on mirror-even, β on mirror-odd); e/f/h large-amp product; j phasequad).
- Board facts (s21): S1T1 P-orbit α_entry=−0.06 → 1.2022 (c5b8), 1.1952 (b 73fe); +0.06 → 0.76. Product S1T1 α±0.1 → 0.99/0.90. S2×T2 product α/β ±0.1/0.05 → ~0.5 both signs (very concave). Large-amp outer product α=0.3 → R 1.4–1.9 but PES FAIL.
- My family `outerjo`: mirror-even joint orbits on S4–S10 × T1, amplitude, rms ±0.1 (per-entry 0.058 for P, 0.041 for M). 18 dirs, 36 evals. Hypothesis 20261014T053828.920Z_swarm-k_hypothesis_2298. Mailed b, c.
- Code: work/outerjo.py (orbits, mirror, block), work/gen_stage1.py, work/summarize.py (board summary of all leaderboard reqs).
- Next: read stage-1 map; stage 2 T2/T3 + line scans + combine with S1T1 P; watch r46/r56 for c5b8/73fe (finite-size!).

## 2026-10-14 06:02 — wakeup 2: stage 1 all FAIL; stage 2s (rms 0.03) submitted
- Stage 1 (rms ±0.1, outer even orbits × T1): 36/36 FAIL on s21 (manifold + PES). R from 0.0 to 3.27, but every large R is another phase. Kernel tail outside g_cutoff 8 is 0.2–2% (work/trunc.py), so not truncation. Result post 20261014T060046.440Z_swarm-k_result_90a9 (with coverage).
- swarm-m `outerorb` = exact duplicate of my stage 1. Mailed m to split: I do rms ±0.03 map, m does follow-ups.
- Board state: P1 = S1T1 P orbit amplitude (G⊥R) is the main lever: c=-0.5 → s21 1.88, r46 2.65 PASS (i 9de1). ac14 (r, xsector) = sum of 5 small levers (P orbits S1/S2/S3 + β odd S2,S5) → s21 4.44 PASS: log R ~ additive.
- Submitted stage 2s: the same 18 dirs at rms ±0.03 (36 evals, total charged 72).
- Next: if any outer direction is PASS with a clear slope, hand it to m/r/p; otherwise abandon outerjo with coverage. Consider the critic role: s21-vs-r46 divergence at large c, PES EG trend.

## 2026-10-14 06:37 — wakeup 3: angle rule found; ell2 submitted
- Stage 2s (rms ±0.03): 36/36 PASS. Each direction has one gaining sign. Per-entry log-slope = +5.05·cos2θ_GR, corr 0.995 (work/anglefit.py; θ = signed Cartesian angle G→R, G1=(2.6935,0), G2=(−1.3468,2.3327), a1=(2.3327,1.3468), a2=(0,2.6935)). Best: S7T1_M1 α− s21 1.242/r46 1.338 (e835). r46 ≥ s21 on all 14 promoted points.
- All board phase winners project positively on β ∝ +sin2θ (per-entry slope ≈8.6 sin2θ vs ≈10 cos2θ for Re γ = α/2) → ∇_γ lnR ∝ e^{2iθ}.
- Posted result 20261014T063659.919Z_swarm-k_result_3184 (outerjo closed, coverage) and hypothesis ell2 20261014T063343.916Z_swarm-k_hypothesis_796c.
- Submitted 17 ell2 line scans (work/dwave.py, work/stage3): Aout/Bout/Cout (S4–S10), Aall/Ball (S1–S10). Predicted lnR ≈ 500λ (Aout) if additive.
- Mailed p and m: outer × T2/T3 belongs to m; step ≤ 0.02.
- Next: read ell2 scans. Turnover vs additivity, phase-only Bout as a clean beyond-M2 candidate. Then shell-weight profiles, T2/T3 cos2θ, A/B mixing.

## 2026-10-14 07:05 — wakeup 4: ell2 is chiral; Cout strong
- ell2 scans (17): Aout ≈ Bout at every λ (1.45/1.46 at 0.001; 1.49/1.50 at 0.002; both FAIL at 0.004). Cout (λe^{2iθ}) much better: 0.0005 → 1.57, 0.001 → 2.19, 0.002 → s21 3.58 / r46 3.88 PASS (481d), split/Δ 0.007. Phase-only at 0.008 → trap state (9e0d, 73bc).
- Interpretation: only the E+ = e^{+2iθ} component gains; E− adds splitting. Posted 20261014T070444.755Z_swarm-k_result_e370.
- Split T2/T3 via mail: e = T2/T3 alone (ell2t), d = T1+cT3 mixtures, me = shell profile + A/B angle on T1.
- Submitted stage 4 (14): Cout 0.003–0.008, Call 0.001–0.004, E− control 0.001/0.002, B/A ratio 0.5/1.5/2 at 0.002.
- Asked swarm-l for a D1 matched-density control of 481d.
- NOTE: work/mytable.py is slow (it shows every request); use work/ell2table.py (filters by family).

## 2026-10-14 07:31 — wakeup 5: chiral field confirmed; 3bd0 is #1
- Cout (λe^{+2iθ}, S4–S10×T1) is nearly linear: 0.004 → 6.90/7.32; 0.005 → 8.54/9.10; 0.0065 → 11.16/11.54; 0.008 → s21 13.58 / r46 13.11 PASS (3bd0, board #1). Call (S1–S10) is slightly better at fixed λ (0.004 → 7.52/8.00).
- E− control: 0.577 F and 1.014 F (manifold broken). The gain is chiral (E+ only).
- B/A ratio: every E− admixture costs.
- Posted result 20261014T073023.358Z_swarm-k_result_6134 and request c1fc (Σ|α| boundary depends on the representation).
- Submitted stage 5 (10): Cout 0.010–0.0199, Call 0.006–0.0154, up to the Σ|α| 2.5 boundary.
- D1 controls in flight from swarm-l: 481d→516b, 3bd0→58a2.
- Division of labour: r = inner-shell weight profile (X5); d = T1+cT3 (kprof); e = T2/T3 (ell2t); m: T3 sign flips (η_R).
- Next: r56 for Cout points → claim if R ≥ 1.10 on r46/r56/conv46. Watch the D1 controls. Find the turnover at large λ.

## 2026-10-14 07:56 — wakeup 6: STRONG claim posted (3bd0)
- 3bd0 (Cout λ=0.008): s21 13.582 / r46 13.106 / r56 13.099 / conv46 13.297, all PASS, C=1, broker claim=strong. D1 control 58a2: R_ctl 1.007 on all clusters. kconv 96/14 −3.6e-4 (swarm-f). e1b8 (λ=0.0065) also strong: 11.16/11.55/10.88/11.59.
- Turnover: Cout 0.010 → 14.11/13.68; 0.012 → 14.74 / r46 10.25; ≥0.015 FAIL. Call 0.008 → 13.84/13.55, 0.010 → 14.27/12.58, 0.012 → r46 FAIL.
- Claim post 20261014T075332.626Z_swarm-k_claim_72b3.
- Board: n has ℓ0 (b55a − E− → 12.94/12.37/12.18; 3f5f s21 14.70); r and h have the inner E+ profile; d has T1+cT3; e closed T2/T3 alone (no lever).
- Submitted stage 6 (7): Cout 0.009, Call 0.007/0.009, 12-member sub-star a/b split of E+ at δ = ±0.5, ±1 (λ=0.008).
- Theory note: γ = λ F(k) O(r) with F = Σ_R e^{2iφ_R}cos(k·R), O = Σ_G e^{−2iφ_G}cos(G·r) — a chiral E2⊗E2 → A1+iA2 product. By MT, Re c is linear and Im c is stationary.
- Todo: critique post on the s21-vs-r46 turnover shift for optimizers that use s21 (josobol, xsector).

## 2026-10-14 08:22 — wakeup 7: ell2 closed; relabelling critique
- Stage 6: sub-star split flat on r46 (13.09–13.11); MT-even (±δ agree to ≤ 0.007). λ: Cout 0.009 → 13.94/13.71, Call 0.009 → 14.07/13.69. 6fe2 (Cout 0.010) is now strong with min 13.675, my best.
- Posted the ell2 closing result with coverage, 20261014T081926.340Z_swarm-k_result_1305.
- Critique note 20261014T082108.533Z_swarm-k_note_61fb: all 40 strong claims project onto ℓ0/E+/E− per T1 shell (rest ≤ 0.07), E+ phase 0°. Claims with min ≥ 13 have E− = 0; the 10–12 tier has E− 0.16–0.27. Tool: work/chiral_decomp.py. Mailed n, r, h, b, i.
- Mailed q: test the chiral field on w3 (chirality × sign).
- Budget 120/500. My families are closed. Remaining value: verification and critique. Consider `swarm done` once r56 for d50f/6fe2 lands and nothing new is open.

## 2026-10-14 08:56 — wakeup 8: wrap-up
- Final ladder: d50f (λ 0.009) 13.94/13.71/13.95/14.04 strong (my best min 13.709); 6fe2 14.11/13.68/14.24/14.39; cf3b 14.07/13.69/14.11/14.27; 85ac; 3bd0; e1b8.
- Board best: n 2fb9 = my field + ℓ0 on S3/S1 × T1, min 14.27. r X8 is stacking the outer profile on it. q: E+ on w3 gives only +3%/+14%; E− is a cliff there too.
- Posted final summary; running `swarm done`. 120/500 charged.
