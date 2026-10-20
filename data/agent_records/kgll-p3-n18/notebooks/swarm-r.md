# swarm-r notebook

Started 2026-10-14T05:20:44+00:00.

## 2026-10-14 wakeup 1 (05:38–05:50 UTC)
- Read docs (theory, notes §5.6–5.9/§12, pilot 024, doc 46, ADR-0040) + whole board (11 hypotheses + d's MT note).
- Built tools in work/: dataset.py (scrape all visible reqs via leaderboard + swarm show → canonical cells
  cos(G·r)cos(k·R), 42 G pairs × 9 R pairs), orbits.py (C3v joint orbits: 126 orbits → 72 even (_P,_M) + 54 odd (_X)
  coords; labels S<shell>T<tstar>g<|G·R|/2π>, board shell numbering), proj.py (projection), fit1d.py (separable quad),
  mk.py (coords → pair-star block; alpha_entry = A_cell, beta_entry = B_cell/2), x1.py.
- Key reading of pooled s21 data: physically linear sector = α on even ⊕ β on odd (MT). Top PASS levers:
  b S2T1g1_X (±0.071 → 1.25 / 0.45, odd), b S5T1g3_X −0.1 → 1.614 (d 2678), a S3T1g0_P −0.104 → 1.368 (c f721),
  a S1T1g0_P line (i) → 1.88 at −0.866 (9de1), a S2T1g2_P +0.104 → 1.18. Outer-shell large α: big R but PES FAIL.
- Observation mailed to d: star-level chiral contrasts (O_a−O_b)F_T are EVEN in β to 2e-4 (10/10 pairs); joint-orbit X odd.
- Posted hypothesis xsector (…_swarm-r_hypothesis_6164), budget ≤250.
- Submitted X1 (15 evals, work/x1/, ids in x1/submitted.txt): singles L4, pairs, α-all, β-all/2, all/2, all.
- NEXT: when X1 lands → compute cross terms (R_pair − R_i − R_j + 1), post result; build joint quadratic + gate model
  (log eg, split/Δ), trust-region batches (X2).

## 2026-10-14 wakeup 2 (06:06–06:13 UTC)
- X1 landed: ac14 (all five levers at single steps) s21 4.4429 P, r46 4.9347 P — top of the board. log R ≈ additive
  (pairs within −3…+19 % of product of singles). Two FAILs (L1L2, L4L5 phase-only) are s21 split/Δ > 0.1; splitting
  cancels in ac14 (0.005). r46 ≥ s21 on all PASS points. Posted result …result_ba0c (with coverage).
- Board: e/f/h/j abandoned large product stars (all FAIL); a/q matched-density controls of c5b8/f721 = 0.999 (gain not
  from averaged density); i P1 line s21 1.88/r46 2.65 at −0.5; n trgrad at P1 −0.5; h josobol 128 Sobol centred ac14
  (to 2×); p folds poolbo into xsector, offers to run sub-batches; d keeps S5/S6/S8 X sums, cross-sector is mine.
- Submitted X2 (5): ac14 line t=1.5,2,3 and α/β split (1,2),(2,1). ids in work/x2/submitted.txt.
- Mailed p (suggest phase-only cross-family split-cancelling combo), l (D1 control for ac14).
- NEXT: X2 results; refresh dataset (filter kind==search, n_mesh 48/g_cutoff 8); log-R GP/quadratic surrogate +
  split/Δ & PASS model on pooled data (incl. h's Sobol); propose trust-region batches beyond h's box.

## 2026-10-14 wakeup 3 (06:34–06:40 UTC)
- X2 line along ac14: t=1.5 6.55/7.09, t=2 9.15/9.20, t=3 10.91/11.39 (s21/r46), all PASS, EG ~3.5–3.9, split ≤0.02.
  a2b1 (α×2) 6.18/6.81, a1b2 (β×2) 4.42/6.79. ac14 broker STRONG: 4.44/4.93/4.43/4.93 (s21/r46/r56/conv46).
  Also fec3, 4385, e317 STRONG; b442, 583d suggestive-so-far.
- Mechanism (others): l D1 control ac14 0.998; f frozen-k statics 0.97–1.02 + kernel converged; q LLL substrate 0.85;
  a geometry: ac14 near-ideal, finite-q mechanism. n: P1 −0.5 basin plateaus ~2.75 (level crossing).
- Posted claim …claim_2999 (ac14 strong, mixed). Submitted X3 (8): t=4, t=4.6 (Σ|α|=2.49 boundary), β-extended
  (a3b5,a3b7,a4.6b6,a4.6b8 [Σ|β|=1.96]), t3 + extra β levers S1T1g1_X,S6T1g2_X,S8T1g4_X at −0.1/−0.2. work/x3/.
- NOTE: Σ|α| ≤ 2.5 binds at t≈4.6 on the pair-star representation. If the frontier is at the boundary → report as such,
  then reallocate α among levers / add α levers with best per-Σ|α| efficiency.
- Budget: 28/500 charged.

## 2026-10-14 wakeup 4 (07:00 UTC)
- b55a (t=3) STRONG 10.91/11.39/11.16/11.42; 2bb9 (t=2) STRONG 9.15/9.20/8.57/9.20. Posted claim …claim_c194.
- X3 all FAIL s21 split: t4 11.07 (0.18), t4.6 7.54 (0.61), β-heavy far worse (a3b5 0.30, a3b7 2.74, a4.6b8 R~0),
  extra β levers on t3: e1 8.43 (0.136), e2 5.35 (0.97). Lesson: more β → s21 splitting; s21 split gate binds at t≈3–4.
- Board: k ℓ=2 unification (∇_γ lnR ∝ e^{2iθ_GR}, corr 0.995); e: non-Laughlin 3-fold trap near phase-only sector
  (EG<0.3, N_A=3 FAIL) — treat AMBIGUOUS with EG<0.5 as FAIL; j: transfer r46 high outlier, r56≈r46^0.94, min is s21/r56;
  q: ρ_t substrate – ac14 at t=0.5 already 2.04× Δ_w1c; n stacking levers on b55a; i adding A−B α on ac14/b55a.
- Submitted X4 (7): (t_α,t_β) ∈ {(3.5,3),(3.5,3.5),(4,2.5),(4,3),(4,3.5),(4.6,3),(4.6,3.5)} → gate-edge map. work/x4/.
- Budget 35/500.
- NEXT: X4 → if a clean point > b55a, claim; else post X2–X4 result with coverage. Consider ℓ=2 reweighting of α levers
  (coordinate with k), and swarm-l D1 control for b55a.

## 2026-10-14 wakeup 5 (07:20 UTC)
- X4 (s21/r46): a3.5b3 492f 11.61/11.55 P (sp 0.002); a4b3 7b62 11.62/10.97; a4b2.5 6061 11.22/11.17; a3.5b3.5 11.32/10.89;
  a4b3.5 11.55/10.45 (sp .087); a4.6b3 F (.109), a4.6b3.5 F (.195). Frontier in my 5-lever space ≈ 11.6.
- k's ℓ=2 chiral field (γ coeff ∝ λ e^{+2iθ_GR}, θ = signed Cartesian angle G→R): 3bd0 s21 13.58/r46 13.11 leads. A-only
  = B-only → gap sees only E+; E− adds s21 splitting. My levers: every cell z = ρ e^{+2iθ}, ρ>0 (checked, work/chiral.py)
  — ac14 is a sparse, incompletely chiral E+ projection (β cells lack ρcos2θ α partner).
- l D1 controls: b55a 0.98, 2bb9 0.99 → beyond averaged density. i claim 9de1 strong. c: w3 static has 2×/1.8× w1c's gap.
- Submitted X5 (8): chiral-completed ac14 orbits ×t (1,2,2.5,3) and + k outer field λ (0.0005–0.002). work/x5/, x5.py.
  Σ|α| ≤ 2.5 (entry-counted) binds for t=3 + outer → refused at 2.53. Mailed k.
- Budget 50/500.

## 2026-10-14 wakeup 6 (07:45 UTC)
- X5 (s21/r46): completion c1 5.27/5.67 (vs ac14 4.44/4.93), c2 10.27/10.15, c2.5 11.34/11.19, c3 12.24/10.93 (r46 below
  b55a), c2+λ.001 11.48/11.17, c2+λ.002 0f3b 12.17/11.97, c2.5+λ.0005 11.72/11.47, c2.5+λ.001 12.11/11.69. All PASS.
- Board: k 3bd0 (outer E+ λ=0.008) 13.58/13.11 leads; i critique: outer field kernel tail 2.5–13% → f/p kconv at 96/14
  (3bd0 holds ≤4.4e-3); q: leader blocks don't transfer to w3/w2 (w1c-specific); g: flattening is marker not mechanism;
  k & h requests to human re Σ|α| representation dependence. n removing E− from b55a → 12.94.
- Posted result …result_2fe3 (X2–X5, coverage). Agreed with n: n keeps inner/outer splits & E− removal; I take per-shell
  E+ profile. Posted hypothesis …hypothesis_8a5f; submitted X6 (9): U08 + hi_s/lo_s tilts at Σ|α|=1.92 (x6.py).
  Note full E+ shell×T1 costs 6ρ of Σ|α|.
- Budget 59/500.

## 2026-10-14 wakeup 7 (08:10 UTC)
- X6 (min s21,r46 at Σ|α|=1.92): U 11.40; hi1 10.02 lo1 11.90; hi2 11.12 lo2 11.60; hi3 11.35 lo3 11.39; hi5 12.11 lo5 9.77.
  → efficiency S5 > S3≈S2 > S1; best tilts have larger s21 split (0.065). r46<s21 in this family. Posted …result_3ad4.
- Board: k claim 3bd0 STRONG 13.58/13.11/13.10/13.30 (D1 1.007). n: b55a−E− 12.94/12.37/12.18; l0 breathing (negative
  product star S1,S3 × T1) on 3bd0 → s21 15.47 (2fb9, screen). p: large-λ outer fields lose 12–30% on r46. a/g:
  e2 pair channel explains R (R²~0.97), e3 separates PASS/FAIL (AUC .965). d: T1 only best momentum profile.
  Split of work: n = l0 + E− removal; k = 12-member sub-star; b = higher ℓ on 12-member; me = per-shell E+ profile.
- Submitted X7 (14): outer-shell ablation (ρ_s→0) and boost (×2) per shell S4–S10 around 3bd0 (λ=0.008). x7.py.
- Budget 82/500.

## 2026-10-14 wakeup 8 (08:35 UTC)
- X7 around 3bd0 (13.58/13.11): drop S10 10.90, S9 10.92, S7 11.19, S4 11.92, S8 12.43, S6 12.58, S5 12.74 (s21).
  ×2 any shell: s21 13.8–14.1, r46 13.5–13.9 (best 01b2 S9×2 14.10/13.87; 8f06 S10×2 14.08/13.84), split ↑ to 0.05–0.074.
  Efficiency rises with |G|. Posted …result_828d; agreed with k's relabelling critique (all strong claims = one E+ field).
- n claim 2fb9 STRONG 15.47/14.59/14.27/14.70 = 3bd0 + l0 −0.048 on S1×T1, S3×T1 (decomposed; saved cache/z_2fb9.npy).
  h josobol closed (0914 min 13.06); many agents finished (c,e,f,i,j,m done).
- Submitted X8 (8): outer profile on 2fb9 (replica, S9×2, S10×2, S9S10×2, S7/9/10×1.5, all×1.25, tilt12, only12×1.3).
- Budget 104/500.

## 2026-10-14 wakeup 9 (09:05 UTC)
- X8 on 2fb9: replica a1dd 15.466/14.587 (exact); S9×2 15.43/14.55, S10×2 15.36/14.48, tilt12 15.16/14.29,
  only12×1.3 15.11/14.27, all×1.25 15.03/14.11, S7/9/10×1.5 14.40/13.54, S9+S10×2 FAIL split 0.127. → 2fb9 locally optimal
  in outer profile. X7 boosts reached STRONG: 8f06 14.08/13.84/14.33/14.42, 01b2 14.10/13.87/14.31/14.38, acda, fb7a, 8a9a.
- n leads: 8f40 strong 17.43/15.62/16.02/15.98 = outer E+ ρ .018 + l0 S3 −.048, S5 −.016 (decomp.py). s21 overstates
  at top by 12–17%. Many agents done (c,d,e,f,g,i,j,k,m,p). Broker charge for me: 74/500.
- Plan: pooled GP surrogate over 20-D chiral profile (E+ρ, l0 per T1 shell) with log min(s21,r46) target; mailed n.
  chirset.py builds the pooled set (dataset refresh running in background).
- 09:20 pooled chiral-profile set: 124 pts (98 with r46). GP (gp.py) is over-confident/extrapolating (log sd 0.5–0.8,
  short length scales on E1/E19/E21). Submitted X9 (6 GP-EI proposals, tight TR around 8f40) as a TEST of surrogate value;
  predictions saved in work/x9_pred.json (gp0 18.0, gp1 18.5, gp2 16.2, gp3 16.9, gp6 16.3, gp7 14.9). ids x9/submitted.txt.
  (pred.json in batch dir broke submit-batch after the 6 json had been submitted — keep non-inputs out of batch dirs.)

## 2026-10-14 wakeup 10 (09:40 UTC)
- X9 GP test: pred vs min(s21,r46): gp0 18.0→15.03, gp1 18.5→13.20, gp2 16.2→15.30, gp3 16.9→14.26, gp6 16.3→11.96,
  gp7 14.9→10.17. Surrogate over-predicts 15–35% at frontier; none beats 8f40 (15.62). Negative result for pooled GP.
- n done (8f40 strong min 15.62, D1 1.005). n gave go-ahead for GP, stepping out. Most agents done.
- My strong (full ladder): 14b1 15.43/14.55/15.06/15.61; 5d07 15.36/14.48/15.05/15.60; a1dd(=2fb9) 15.47/14.59/14.27/14.70;
  01b2, 8f06 (~13.9 min); 0f3b 11.68 min; 492f 11.27; b55a 10.91; ac14 4.43.
- FOUND: conv46 vs r46 shifts +1.5…+7.7% for outer-heavy (S9/S10) leaders (14b1 +7.3%, 5d07 +7.7%). Posted critique
  …note_e1bb. Submitted 4 s21 diagnostics (kc/: s9x2, s10x2 blocks at 64/10, 96/14) to split kernel box vs qmax.
- Budget 80 (+4 diag) /500.
- NEXT: read kc diagnostics; post final X8/X9 result + coverage; swarm done (frontier saturated across 3 methods).

## 2026-10-14 wakeup 11 (10:05 UTC) — DONE
- kc diagnostics: S10×2 64/10 = 96/14 = 15.4567 (screen 15.358), S9×2 15.5252 (15.425): kernel +0.65% only → conv46
  shift (+7%) is qmax 8→10. Posted request …request_e8da (qmax 12 check). Final result …result_9d87 (coverage).
- swarm done posted. 84/500 charged. Loop stopped.
