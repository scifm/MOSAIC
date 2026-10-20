# swarm-s notebook

Started 2026-10-14T10:24:52+00:00.

## 2026-10-14 ~11:30 — wakeup 1: orientation, theory note, family noQ0

**Read:** theory doc §1–8, pilot 40 summary, precision 46, kdep_envelope.py (block = Σ(α/2+iβ)O_s F_p, inversion-closed stars → cos·cos only). Board: a/b axis maps (duplicate), c jorb (orbits; top results), d chiral half-shell β, e bigamp, f chiral-odd β, g joint-orbit channels, i kpow, j/r ⊥ amplitude, k mech (density controls), l phase-even, m phasehess, q fs-scan, h union quadratic model.

**Insight (posted note 20261014T112614.191Z_swarm-s_note_7996):** on LL0 Bloch states e^{iG·r} = η_G e^{ik·R'_G} e^{iG·η}, R' = l²ẑ×G ∈ lattice. ⇒ e^{γ}φ_k = (e^{Γ_k(η)}|0⟩)⊗|k⟩: every deformation = k-dependent LL mixing, Q = R'_G ± R. Fully comoving (Q=0) = static LL mixing (C6 orbit → LL0+LL6+…). ⊥ cos·cos channels (S1T1,S2T2,S3T3) are the only ones with Q=0 content (half). Request to human: 20261014T112626.349Z_swarm-s_request_dc6c.

**Family noQ0** (hyp 20261014T113100.099Z_swarm-s_hypothesis_6507): TL-active combos (chiral-odd β, chiral-even α), ⊥ held 0. Budget ≤230.
Directions (pair-entry units; work/gen.py DIRS): D1 β_odd S1T1(±30); D2 β_odd |G|²=3×T1(±60); D3 α |G|²=3×T1 δ0; D4 −α_even |G|²=3×T1(±60); D5 α_even S1T1(±30).
Sign conventions verified vs swarm-c data (my `delta` labels match: d698 = |G|²=3×T1 d60 β+0.03 → 1.2494).

**Batch 1 submitted (16):** work/b1, spec work/spec_b1.json. ids 20261014T1131*_swarm-s_req_{bdef,bfbb,0d89,9eab,256a,ad1d,1778,7324,af1f,a038,327e,8faa,4d18,0165,e91e,8943}.

**Tools:** work/scrape.py (cache all leaderboard requests → work/db.json as pair coords), work/orbits.py (print in orbit coords; label S{|G|²}xT{|R|²}d{δ}, * = Q0), work/geom.py (geometry, Qset, orbit, make_block).
Note: orbits.py labels use |G|² and |R|² (T3 label = |R|²=3 = T2 index!). geom.shell_idx/t_idx convert.

**Next:** read batch-1 results; check additivity of chiral partners; fit 1-D quadratics; batch 2 = other |Q|²=1 noQ0 orbits + quadratic model.

## 11:50 — wakeup 2
Batch 1 still queued (all 16 pending; 48-agent queue). Board: leaders now ⊥ S1T1 α at large amplitude (j/q ea28/c027 s21 1.6386), f chiral-odd β S1T1 1.56. g result: ⊥ channel not special beyond S1T1 (S2T2/S3T3 ⊥ weak/opposite) — weak evidence against LL-mixing dominating. u audit: |G|²=3×T1 leaders use 30–50% of s21 split gate (split/Δ ~0.05 at 0.05 amp) and grow on r46 (d698 r46 1.404); S1T1 leaders cluster-flat. Expect my D2/D3/D4 high-amp points to FAIL at s21 on splitting. p: holes = inner+outer combined optimizer; large-amp non-⊥ α orbits (mine). ag (fsmin) is CMA on min-over-clusters, β-only no-Q0 = superset of my β lane → I should not do β-only CMA; focus α_even non-⊥ + combinations.
scrape.py slow (serial swarm show); make parallel next time.

## 12:10 — wakeup 3
Batch 1 still all pending (queue). Board: c STRONG claim (phase-only S2×T1 +60° β=0.03: 1.249/1.404/1.347) — in noQ0 subspace (u verified no Q=0). j: ⊥ α −0.45 1.64/2.63/2.44 (s21 splitting binding gate). k mail: algebra checked OK; solver LL mixing is incoherent (t_n=|a_n|²) so a coherent static LL-mixing control is impossible without solver change. y s2plane overlaps D3/D4 (cites mine). Herding heavy; plan for batch 2: only after batch 1 returns; avoid y's S2×T1 α plane; candidate: combined β_odd(S1T1+S2T1)+α_even combos at the cusp, and S1×T2 ±60 (|Q|²=1) α/β lines if unmapped.

## 12:35 — wakeup 4: batch 1 partly back
s21 results (split/Δ, eg): B12_015 1.5675 (1.1e-2, 4.8); B12_030 1.725 (4.9e-2, 3.2 — near split gate); C_035 1.546 (2e-4, 6.0); C_070 2.060 (1e-4, 4.9); C_100 **2.5055** (4e-4, 4.4); D1_020 1.230; D1_040 1.4545; D2_010 1.292. Others pending.
=> combined α+β direction C is near-linear (≈ +1.5/unit t), with *tiny* splitting (α parts cancel the β-induced splitting). Partners add (D1 at 0.02 → +23% vs single orbit 0.03 → +16%).
Batch 2 submitted (8): C line t=1.3,1.7,2.2,3.0,4.0 (ids 7010,5e99,e1b1,86c6,9a30), α-only part Ca t=1,2 (8acf,e727), β-only Cb t=1 (b2a2).
Board: combos everywhere huge at s21: h c662 4.76 (has ⊥), t 3542 3.77 (has ⊥), w S19×T1 α_even 0.05 → 4.36 (noQ0, outer; g_cutoff caveat → needs conv46), q S1T1 +30 β 0.3 → 2.75, r S3T3⊥ α 0.3 → 2.71. k: density controls for α⊥−0.45 lower gap (density not the mechanism). f STRONG claim S3×T1 chiral-odd β 0.05: 1.558/1.641/1.560.

## 13:05 — wakeup 5
Batch 1 ladder: C_100 256a 2.506/2.610/2.399 (converge); B12_030 bfbb β-only 1.725/2.322/2.142 (converge); C_070 9eab 2.06/2.06/1.955. Single α lines FAIL on split at 0.08–0.10 (8faa, 0165, 8943). Posted result 20261014T130349.665Z_swarm-s_result_c628.
C = complex angular rule α∝cos2δ, β∝sin2δ (S1,S2×T1, D4/D5 at 2× rule weight). gen2.py adds rule blocks {"rule":[[g2,tq,A,B]]}.
Batch 3 submitted (6): E1 = C + rule|G|²=4×T1 (t=1,2: b786, 9ac7); E2 = E1 + rule|G|²=7×T1 A=0.01 (6bc8, c325); phase-only P = D1+D2+rule4 β (464b 0.02, ee47 0.03).
Board: h claim STRONG c662 4.76/5.23/4.67 (has ⊥ α); t 8c01 4.82/5.19; r doing no-⊥ ablations of records; g critique d_sc zero-mode amplification (p refutes).
Next: if conv46 holds for 256a/bfbb → post claim. Read b2 line → find turnover; then optimize ratio α:β and shell weights (small CMA / coordinate search) in noQ0 rule space.

## 13:30 — wakeup 6
Ladder done: bfbb (β-only) 1.725/2.322/2.142/conv 2.322 STRONG; 256a (C t=1) 2.506/2.610/2.399/2.610 STRONG; a038 (D2 0.04) 1.722/2.274/2.095/2.274; 9eab 2.06/2.06/1.955/2.06. Posted claim 20261014T132932.937Z_swarm-s_claim_9cef; asked k for density control on 256a.
Board: t claim 8c01 4.82/5.19/4.55; v claim S7×T1 α cos2δ 1.561/1.933/1.787; ap: leaders' γ on uniform LL0 inert/lower → gain is γ×ρ* cooperation; g retracted 1/d² critique; am: random phase directions all FAIL → gains directional; av: records follow angular rule (S3 & outer unused).
Batch 2 (C line t≥1.3) and batch 3 still queued (o reports stuck lanes ~80 min).

## 13:57 — wakeup 7
C line s21: t1.3 2.959, 1.7 3.580, 2.2 4.390, 3.0 5.785, 4.0 7.345 (split ≤7e-3, eg 3.2, S ratio 0.34). Ca t1 1.539, t2 1.653 (split 5e-2); Cb t1 1.669. Superadditive.
Posted result b2. Batch 4 submitted (bbf8 C470, c4f4 C550, d517 Cb15_400, 2655 Cb15_550, 53ce Ch400, ad50 Ch600, 6ac2 Ch800). Batch 3 (rule ext) still queued.
k queued 256a density control (…_2385). Board: o f5f1 record 6.28/8.33/8.12 (Σβ 1.88 cap). Σ cap representation question open (t request 789e).

## 14:23 — wakeup 8
C line r46: 7010 3.20, 5e99 3.90, e1b1 4.78, 86c6 6.16, 9a30 7.78 (r56 pending). Ca t2 r46 2.25; Cb r46 1.91.
Batch 3: E1_100 3.81; E1_200 7.06/7.44; E2_100 5.15/5.66; **E2_200 c325 9.866/10.147** (Σα 1.48 — cap-efficient); P_020 464b 1.63; P_030 FAIL (split 0.68).
Board: r ablation — removing ⊥ keeps 83–93% of records (Q=0 is boost not origin; supports noQ0). av cos2d rule S1–S3×T1 → s21 10.39 at Σα cap (same region as mine). ae: records cap-limited not gate-limited. k: density control rule R_ctrl−1 = 0.06ΔM2 (256a control landed ~0.99–1.0). ap: f5f1 γ on uniform LL0 destroys state; bfbb inert there.
Batch 5 submitted: E2 t2.7 (31a0), t3.3 (79fd, Σα 2.45), E2h t3/t4 (4257, 2178), E3 t2.7 with outer rule |G|²=9,12,13 A=0.005t (17c1).

## 14:50 — wakeup 9
c325 DONE STRONG 9.866/10.147/9.535/conv 10.153 (noQ0) → claim 20261014T144925.350Z_swarm-s_claim_0298. 9a30 STRONG 7.345/7.777/7.028/7.778. 9ac7 (E1_200) 7.06/7.44/6.74.
Batch 4 s21: C_470 8.35, C_550 9.22 (cap), Cb15_400 8.42, Cb15_550 8.51 (more β ≈ no help), Ch_400 5.68, Ch_600 7.76, Ch_800 FAIL split 0.138 → D4/D5 at 2× rule weight help; β not binding.
Component efficiency: rule4+rule7 parts (Σα 0.58) added ≈ +5.9 at t=2 → most cap-efficient. Batch 6 ablations at E2_200: no7 (=E1_200 dup, 2446), noD45 (c29a), r7×2 (1c48), r4×1.5 (7860).
k queued c325 density control (…_3378). u: qmax8 non-PSD tiny at c325. av claim e0a8 10.39/9.87/10.50 (has S1⊥). x adding outer α to c325.

## 16:40 — wakeup 10 (long gap; wakeup fired late)
Results: 1c48 (E2 r7×2) 11.21/11.67/11.60/conv 11.72 STRONG — noQ0 record → claim posted. 31a0 (E2 t2.7) 10.86/11.43/11.50/11.48; 79fd (t3.3) 11.24/10.47/11.15/10.61 (r46 split 0.068 → past optimum); 4257 E2h t3 10.09/10.73/10.94; 7860 r4×1.5 10.43/10.95/10.67; 2178 E2h t4 FAIL r46; 17c1 E3 outer 12.79 s21 FAIL r46 split 0.129; c4f4 C550 9.22/9.67/9.11/9.67; 86c6, 9ac7 STRONG. c29a (noD45) 8.21/8.79.
Lessons: |G|²=7 rule most cap-efficient; s21 split binds at 1c48 (0.057); r46 split binds for outer additions & larger t.
Board: k: c325 density control 0.998/0.997/0.997. b: c325 + outer sin2δ phase → 7e78 min 10.105. h claim 5063 11.65/12.30/11.97. u: qmax concerns R>11 (conv46 shift +0.5–0.9%). an: rank by min(r46,r56) above 11.
Batch 7 submitted around 1c48: bcb2 (r7 α×1.5), 769e (×1.15), f80e (r4×1.25), 79dc (r7 β×0.5), 0cb1 (D1/D2 β×0.75).

## 17:07 — wakeup 11
Batch 7 (s21/r46): bcb2 r7α×1.5 11.84/11.83 (best); 769e ×1.15 11.50/11.65; f80e r4×1.25 11.29/11.70; 0cb1 β×0.75 11.27/11.55; 79dc r7β×0.5 10.81/10.80. c29a (no D45) STRONG min 8.21.
Board: records now 12.5–13.9 (av 55f9 12.51/12.71/12.79/13.00; w 407a 13.93 qmax-suspect; t cbe3 11.65 min). x: c325 + outer T1 α → 06bb min 11.80 noQ0. y/u: conv46 shift up to +20% above R≈12; r56 qmax8 unconverged >9. k: density controls all within 1%. ap: registration test — shifting ρ* by K kills gains (γ×ρ* cooperation).
Batch 8 (final local push around bcb2; Σα ≈2.0–2.15): 7a26 r7α 0.08; 29c3 r4α 0.075; 2f3f + outer α |G|²=9,12 A=0.01; 1524 ×1.1.
Plan: after b8 + r56 land → coverage result + abandon/close noQ0 family; consider done (budget mostly unused but frontier saturated by herd).

## 17:38 — wakeup 12
Batch 8 s21/r46: 2f3f (+outer α 9,12) 12.18/11.89; 29c3 (r4α .075) 11.94/11.82; 7a26 (r7α .08) 12.11/11.57; 1524 (×1.1) 12.03/11.59 → plateau ~11.9 on r46. r56 pending for b7/b8.
Batch 1 r56 rungs still pending for many small points (low priority queue).
k: 1c48 density control 1.000 (s21). ap: c325 on uniform LL0 0.45/0.85; K-shifted ρ* FAIL → γ×ρ* registration. u: 1c48, c325 class A (qmax-clean).
Batch 9 (final): 6ee0 H5 = bcb2 + r4α .075 + outer 9,12; cd17 H6 = H5 + r7α .07.
Next wakeup: once r56 lands for bcb2/2f3f/29c3/H5/H6 → coverage result post + `swarm done`.

## 18:10 — wakeup 13: closing
2f3f done: 12.176/11.887/12.131/11.970 STRONG (best noQ0 min). Posted coverage result 20261014T180946.171Z_swarm-s_result_20d1 and claim 20261014T180955.147Z_swarm-s_claim_c64e. Family plateau ~11.9; other agents' frontier 13.7–14.9 is in other subspaces (outer shells/⊥). 56/500 charged. Running `swarm done`.
