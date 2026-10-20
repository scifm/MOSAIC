# swarm-r notebook

Started 2026-10-14T10:24:49+00:00.

## 2026-10-14 ~11:25 — wakeup 1: scope chosen, stage 1 submitted
- Board at start: a/b both doing the 60-axis full-star map (duplicate), c joint C6 orbits S1-S3×T1-T3, d chiral half-shell phases,
  e bigamp full-star line scans + Sobol, g C3 channels (incl. ⊥ R=ẑ×G), i kpow (log-density power), f chiral-odd β orbits,
  l phase-even β² curvature. Phase sector heavily covered.
- Key data (swarm-c, s21): S1×T1 ⊥ orbit α=−0.05 → 1.171 (req_7133), +0.05 → 0.803; ⊥ β ±0.03 → 0.98/0.99 (even, MT-consistent).
  ±30 orbits: (+30,+β .03) 1.160 vs (−30,−β) 1.152 (MT pair agree → small s21 chirality artifact). Full-star axes ≤ +1 %.
- Chose family **gc-perp**: ⊥ amplitude orbits S1–S3 at large amplitude, then combine with chiral-odd β(S1 ±30). Hypothesis
  20261014T112305.979Z_swarm-r_hypothesis_e6de. Budget ≤200.
- Generator: work/gen.py (channel keys S1p,S2p,S3p,S1o30,S1o150; per-entry coefficient). Admissible to α=−0.6 (check ok).
- Stage 1 submitted (27): work/s1/*. S1p line −0.02…−0.6,+0.02,+0.1; S2p/S3p ±0.06,±0.15,±0.3; logp λ(1,.49,.32) λ∈{−.08,−.15,−.3,−.45,+.1}.
- Mailed swarm-c, swarm-g proposing the split.
- Next: read stage 1; fit S1⊥ turnover; 2-D grid α⊥(S1) × β_odd(S1o30 = +b, S1o150 = −b).

## 2026-10-14 11:42 — wakeup 2
- Stage 1 (27) still queued; nothing landed. ~45 agents active and heavy herding on S1-S3×T1 orbits.
- Leaders: swarm-f chiral-odd β: S3×T1 per-entry 0.0167 → s21 1.558 (req_e5d5); S2×T1 → 1.483; S1×T1 per-entry 0.0333 → 1.381 (s21c 1.381, r46 pending).
  swarm-c d698 (S2×T1 ±60 phase) s21 1.249, r46 1.404.
- swarm-s note: on LL0, e^{iG·r} = η e^{ik·ẑ×G}·(cyclotron op), so the ⊥ cos·cos channel = ½ static LL mixing (Q=0) + ½ k-dependent (Q=2R').
  ⊥ winners are mechanism-ambiguous; tag ⊥ content in coverage. Mechanism-clean subspace = noQ0 (swarm-s).
- swarm-j ceded ⊥ 2-D grid + ⊥ CMA to me; j posts the ⊥ line; q does the cross-cluster line audit.
- gen.py: added key S1odd (= +b on S1o30, −b on S1o150; matches swarm-f's sign pattern; f's β_odd = 3b).
- Submitted s2a (5): α⊥S1 ∈ {−.05,−.10,+.05} × b ∈ {.0333,.0667} (subset).
- Next: when stage 1 + s2a land: is ⊥ additive with chiral-odd β? If yes, 2-D/4-D CMA (α⊥ S1–S3, b_odd S1/S2/S3?).

## 2026-10-14 12:05 — wakeup 3
- S1⊥ α line (s21 R, sp/Δ, PES EG): −.02 1.071; −.05 1.171 (c); −.08 1.262; −.12 1.370 (r46 1.415); −.18 1.442 (.038); −.25 1.466 (.071);
  −.35 1.478 FAIL (.108); −.45 1.639 (.073; r46 2.632 C=1, EG 3.8); −.6 0.848 FAIL (.32). +.02 0.925, +.1 0.571.
  ak: jump between −.35 and −.45 looks like a branch change/level crossing → submitted −.40/−.50/−.55 as --diagnostic (s1b).
  (Resubmit non-diagnostic later if wanted: same hash = free.)
- S2⊥, S3⊥ are hypersensitive: S2⊥ ±.06 → .976/.760; |α| ≥ .15 FAIL (manifold destroyed). S3⊥ −.06 FAIL. g: S3⊥ wants α>0.
  → ⊥ beyond S1 is dead except tiny steps; logp combos likely fail.
- k: matched-density control at α⊥ −.05 → R_ctrl .9993 (density explains none). s note: ⊥ = half static LL mixing.
- c claims STRONG: S2×T1 +60 β=.03 phase-only 1.249/1.404/1.347. f: S3×T1 chiral-odd β per-entry .0167 → s21 1.558, r46 1.641.
- Next: grid results (s2a); then combine α⊥S1 ∈ [−.25,−.1] with chiral-odd β on S1/S2/S3 ×T1 → small CMA.

## 2026-10-14 12:27 — wakeup 4
- S1⊥ ladder: −.12 1.370/1.415/1.376; −.18 1.442/1.633/1.555; −.25 1.466/1.895/…; −.45 1.639/2.632/2.445, conv46 2.632 (all PASS).
  j has priority on −.45 (ea28); q/j: s21 splitting is the binding gate on every leading line (8–30× r46's sp at equal step).
- S2⊥/S3⊥/logp closed → result post 20261014T122606.522Z_swarm-r_result_1d93 (coverage incl.). S3⊥ +.3: R 2.71 but PES FAIL (other phase).
- Leaders/claims: f STRONG S3×T1 chiral-odd β b=.05: 1.558/1.641/1.560, conv46 1.641. c STRONG S2×T1 +60 β .03.
  h: S4×T1 α orbit contrast c0+ 1.572/1.720/1.614. k: density controls at −.45 lower the gap (0.94–0.96) → not density.
- swarm-m does α⊥ × (e5d5, d698) combos (19). swarm-aq does ⊥ k-profile (S1×T3⊥, 2G harmonics). I keep α⊥ × S1 chiral-odd.
- Idea: since s21 splitting is the binding gate, look for a combination direction that cancels s21 splitting growth
  (min-over-clusters objective). Result.json gives only |E3−E1|, not momenta → empirical only.

## 2026-10-14 12:50 — wakeup 5
- My s2a grid + −.4/−.5/−.55 diag still queued (submitted 11:41/12:04; broker backlog ~1 h).
- Board jumped: t 8c01 s21 4.816/r46 5.186; h c662 4.760/5.226/4.674 (suggestive→converge); x d524 STRONG 1.92/2.15/1.99/2.15.
  j claimed STRONG ⊥ −.45 (3d0f). k/u: gains not density, not bigger projected interaction. c: leaders restore smooth M2 law (R_beyondM2 .12→.72).
- Decomposed leaders (work/decomp.py): both contain S1⊥ α (8c01 −.134, c662 −.058) + ±30 α_even/β_odd + S1×T2, S2×T1(.. T3) etc.
  8c01 already contains my α⊥×S1odd combination → my s2a grid is subsumed.
- New tool work/ablate.py (noperp / phase / perponly on another req's block, onto my template).
- Submitted abl1 (4): 8c01 noperp 2132, 8c01 phase cc75, c662 noperp 5c65, c662 phase d562. Note posted.
- Next: if phase-only/no-⊥ versions keep most of the gain → clean beyond-M2 and noQ0; then line-scale them (×1.25, ×1.5) for min-over-clusters.

## 2026-10-14 13:15 — wakeup 6
- s2a grid (α⊥S1 × S1 chiral-odd b per entry) landed — roughly MULTIPLICATIVE in R, and s21 splitting stays low:
  b .033 (f alone 1.381): α −.05 → 1.607 (r46 1.573), α −.10 → 1.766, α +.05 → 1.120 (r46 1.204).
  b .067: α −.05 → 1.918, α −.10 → 2.130 (sp/Δ .009 vs α⊥ −.10 alone .013).
- Submitted s2b (13): α ∈ {−.15,−.2,−.3} × b ∈ {.067,.1,.133} + α ∈ {−.05,−.1} × b ∈ {.1,.133}.
- Still pending: abl1 ablations, −.4/−.5/−.55 diag (o reports stuck lanes).
- Board: h claimed STRONG c662 (4.76/5.23/4.67/5.23); k: density controls ~1 for all α leaders.
  g critique: parent near zero mode at d_sc=.1, R amplified; p disputes. Human asked for d_sc control.
  s noQ0: no-⊥ combo 2.51/2.61/2.40; phase-only noQ0 1.73/2.32/2.14. av: records = cos2δ α / sin2δ β angular rule.

## 2026-10-14 13:45 — wakeup 7
- S1⊥ diag fill-ins (s21): −.40 1.523 FAIL (sp .102), −.50 1.882 (sp .030), −.55 1.842 (sp .019). Splitting peak at −.35/−.40 → avoided crossing; clean window −.50…−.55. Mailed ak, j.
- Grid ladder: b.033 α−.05 r46 1.573 r56 1.532; b.067 α−.05 r46 2.054; b.067 α−.10 r46 2.260 (sp .0008).
- s2b (13) + abl1 (4) still queued; several agents report stuck s21 lanes (o, j, m, ah requests to operator).
- Board: g retracted 1/d² critique. ap lllref: leaders' γ on uniform LL0 LOWER gap → gain needs γ×ρ* cooperation.
  f: phase-only s21 ceiling ≈1.72 across directions. s STRONG noQ0 claims (bfbb phase-only 1.725/2.32/2.14/2.32).
  t STRONG 8c01. v STRONG S7×T1 α contrast.

## 2026-10-14 14:20 — wakeup 8
- Ablations: c662 no-⊥ 5c65 s21 4.421 / r46 4.878; 8c01 no-⊥ 2132 4.018 / 4.396; phase-only parts FAIL (sp .27/.13).
  → Q=0 is a 7–17% boost, not the origin. Posted result 20261014T141931.093Z_swarm-r_result_44b0 (with coverage). Mailed s.
- Plane: 4dff (α⊥ −.10, b .067) 2.130/2.260/2.109/2.260 (STRONG-level, not claimed: far below records). a8fb (−.15,.067) s21 2.298.
- Board top: av cos2d e0a8 s21 10.39 / r46 9.87; s noQ0 c325 9.87/10.15 (no ⊥!). Records are cap-limited (Σ|α|).
- swarm CLI slow (>100 s per call): run tab.py in background.
- Plan: let the 12 queued outer-plane points land, post the final plane coverage, then `swarm done` (family exhausted;
  frontier is the coherent angular rule, owned by av/s/t/h/o/z; Q=0 question settled by s c325 + my ablations).

## 2026-10-14 14:55 — wakeup 9
- Plane grid complete to α⊥ −.3, b .133: monotone in both; best 7ed1 (−.3, .133) s21 3.513 / r46 4.234; s21 sp ≤ .045 everywhere.
  (b .1: −.05 2.09, −.1 2.38, −.15 2.62, −.2 2.81, −.3 3.10; b .133: 2.11, 2.49, 2.81, 3.08, 3.51.)
- Submitted s2c (6) to find the plane's turnover: (−.2,.2), (−.3,.2), (−.3,.267), (−.45,.133), (−.45,.2), (−.5,.267).
- Board: av STRONG e0a8 10.39/9.87/10.50/conv 9.96; s STRONG c325 noQ0 9.87/10.15/9.54/10.15. o: f5f1 without ⊥ α keeps 3.91 (⊥≈40%).
  Cap (Σ|α|) chart-dependence raised to human by t and ai. c, ac done.

## 2026-10-14 16:40 — wakeup 10
- Plane continues rising to the box edge: (−.45,.133) 4.09/4.82; (−.3,.2) 4.07/5.24; (−.45,.2) 5.06/5.85; (−.3,.267) 4.24/6.09;
  (−.5,.267) 5.572/6.206 (s21 sp .020). Turnover not reached inside |α|≤.5, b≤.267.
- Submitted s2d (3) at the campaign boundary corner: (−.5,.3), (−.6,.3), (−.6,.267). Then final post + done.
- Board: h STRONG 5063 11.65/12.30/11.97/12.29; e c577 11.42/11.59/11.38 cap-limited; an: above s21 R≈12 the r46 gate binds;
  u: qmax-8 pair spectra non-PSD at R≈13–14 (request to human). Many agents finishing (j, l, m, b, i, am, au done).

## 2026-10-14 17:06 — wakeup 11: family closed, done
- Corner: (−.5,.3) 5.562/6.234; (−.6,.3) 3.246; (−.6,.267) 3.368 → turnover in α⊥ between −.5 and −.6; b saturates by .267.
- Final result + coverage: 20261014T170519.166Z_swarm-r_result_fe10 (count correction note af55: 61 requests, s21 P/A/F 42/0/19).
- Ran `swarm done` (61/500 charged). Frontier (cap-limited multi-shell angular rule, R 11–14) is owned by av/s/t/h/o/x/w/z;
  the plane is a 2-D slice of it, and the Q=0 question is answered (my ablations + s's noQ0 records).
