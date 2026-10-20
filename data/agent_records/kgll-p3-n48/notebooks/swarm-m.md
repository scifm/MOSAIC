# swarm-m notebook

Started 2026-10-14T10:24:31+00:00.

## 2026-10-14 ~11:25 — wakeup 1: orientation, family choice, stage 1
- Read brief, docs 40/46, theory §6.4/§8, notes §5.6-5.7, §7.4-7.6, §12, App. B. Parent w1c: Δ s21 2.2586e-4, r46 2.4101e-4, r56 2.5901e-4.
  R_staticM2 ≈ 0.125: w1c's gap is ~8× below the M2 law (ρ_min = 0.05 is the bottleneck, presumably).
- Built work/geom.py: exact single-particle Berry curvature F(k) (plaquettes) and tr g from the kernel overlap
  R(k,k') = Σ_G W_G(k,k') η_G exp(-G²/4 + (k'-k)·G/2 - i(k+k')×G/2). Validated: static w1c mean F = 1.000, mean tr g − F ≈ 0.
  w1c curvature is wildly non-uniform: F ∈ [0.10, 14.8], std 2.07. work/collect.py pulls all visible results + descriptors to work/data.jsonl.
  First correlation look: neither F_std nor trace defect predicts R_gap (phase-only pairs keep F_std = parent but R varies 0.79–1.01).
- KEY observation: β ± pairs are even (R(+β) ≈ R(−β)) → β-gradient ≈ 0, info is in the β-Hessian.
  Only positive β axis: β[S1, T(|R|²=4)] ±0.03 → 1.0098/1.0089 (swarm-a 9fed/244e).
- Posted hypothesis `phasehess` (20261014T112304.952Z_swarm-m_hypothesis_2495), budget ≤180.
- Stage 1 submitted (11): β[S1,T3] ∈ {.06,.09,.12,.16,.20,.25,.30,−.09,−.20}; β[S1,T2] ∈ {.09,.20}. Inputs work/in/st1, generator work/mk.py
  (star lists sorted, n_mesh 48 — identical to swarm-a's block format).
- Mailed swarm-a (β-gradient≈0 critique) and swarm-e (scan overlap).
- Caveat: T3 = 2·T1 → aliasing on 4×6 ((4,0) superlattice) — finite-size risk.
- NEXT: read stage-1; if R grows with β, find other positive-curvature β axes from the a/b map (S4–S10), measure couplings (c,±c), Hessian eigvecs.

## 11:45 — wakeup 2
- Board exploded (~45 agents). MT symmetry (f/d/l): separable full-shell β axes are even in TL → my "observation" was already the theory. swarm-l owns β² curvature of all 30 full-shell axes at ±0.12. => phasehess is redundant + weak.
- My β[S1,T3]=0.12 FAILS (splitting/Δ=0.159, R 0.72; req 7402). swarm-e: full-star manifold breaks at |β|≈0.12, |α|≈0.1 (S1), 0.05 (S2+).
  Withdrew β13 = 0.20/0.25/0.30/−0.20 (25d8, 2c67, ff8b, f196). Still pending: .06 .09 .16 −.09, b12 .09 .20.
- Leaders: chiral(-odd) phase joint orbits (f, c). f e5d5 1.558 s21 at 0.0167/entry; 5098 (2× amp) 1.38 → peak at ≤ ~0.02/entry.
  c d698 (+0.03) 1.249/r46 1.404 and dbab (−0.03) 1.240/1.403 → even in β with huge curvature (level-repulsion-like?).
  c ce1f: s21 1.1595 r46 1.1586 r56 1.1492 conv46 1.1586 → heading to "strong".
- geom descriptors of the leaders: phase leaders leave F(k) unchanged (std 2.069), trace defect ~0.005 → single-particle geometry is not the mechanism (agrees with swarm-k).
- NEXT: when stage-1 lands, post result + abandon phasehess with coverage. Candidate pivot: small-amplitude structure / peak location of leading phase orbits (0 < amp < 0.02/entry), analytic (β²) vs cusp, with free ladder transfer. Coordinate with f first.

## 12:20 — wakeup 3: abandon phasehess, pivot to perpchi
- Stage 1 done: β[S1,T3] .06→0.990, .09→0.916, −.09→0.940, ≥.12 FAIL; β[S1,T2] .09→0.882, .20 FAIL. Posted abandon w/ coverage (20261014T120631.619Z_swarm-m_abandon_5def). 10 evals charged.
- Board state: STRONG claim by c (d698 S2×T1 +60 β .03: 1.249/1.404/1.347). Top min: ea28 α⊥ −0.45 (1.639/2.632/2.445; ak: branch change suspected), e5d5 chiral-odd β S3×T1 (1.558/1.641/1.560).
- 0-eval mechanism probes (work/dens*.py, filled.py, fcorr.py): BZ-averaged |h_k|² is orientation-blind; the filled-band density
  ρ_f = <|h_k|²|u_k|²/S(k)>_k (|u_k|² from LL0 diag form factor) IS orientation-sensitive and rises for α⊥<0 (0.0616→0.066) — right sign,
  but explains little (corr 0.34 on small steps; phase-only leaders leave it unchanged). Not posted (weak). Possibly mention later.
- harvest.py → board.jsonl (all leaderboard requests: block, R per cluster, verdict, split/Δ). At 12:10 no finished request had α≠0 AND β≠0.
- New family perpchi (20261014T121617.787Z_swarm-m_hypothesis_e7ee), budget ≤80: P=α⊥ S1×T1 (−0.1..−0.3) × E=e5d5 × D=d698 scales. 19 submitted (in/pc1, names: P0.2 = α⊥ −0.2).
  Tools: work/orbits.py (joint pair orbits, δ = ∠R−∠G), work/comb.py (combine blocks), leaders.json (E, D, P blocks).
- NEXT: read pc1 + their r46/r56 promotions; fit additivity; local Nelder-Mead in (P,E,D) on min-over-clusters with split/Δ ≤ 0.08.

## 12:45 — wakeup 4 (waiting)
- pc1 (19) all still pending (queue). Budget 29/500 charged.
- Board: multi-orbit α+β steps are hugely superadditive: t 8c01 s21 4.816 / r46 5.186; h c662 4.760 / 5.226 (α+β union step; α-only saturates 1.68).
  Claims STRONG: c d698 (phase), f e5d5 (phase), j ea28 (⊥α −0.45: 1.639/2.632/2.445/2.632).
  k/u: gains are NOT density nor larger projected interaction (leaders lower form-factor weight). e: PES entanglement gap drops 13→2.5–5 at leaders.
- My perpchi is a small instance of the α+β superadditivity; keep, read results next.

## 13:10 — wakeup 5 (waiting)
- pc1 still all pending after ~55 min (others landing; queue long). No action needed.
- Board: STRONG claims h c662 (4.76/5.23/4.67, conv 5.23; density control 0.995 → not density). av: records = angular rule α∝cos2δ, β∝sin2δ on S1/S2×T1(+T2).
  aa adds S3×T1 chiral-odd β to the record (my E direction!) ; x adds outer α at record; aq S1×T3 at record. am: random phase dirs all FAIL → gains directional.
  g critique: d_sc=0.1 parent near-zero-mode → R amplified; p counter-critique. Requests to human pending.
- perpchi is now a small-scale version of what the records already contain (S1⊥α + S2 β). Keep for additivity data; don't expand unless results surprise.

## 13:40 — wakeup 6
- pc1 still pending after 85 min; o and j report stuck lanes too. Posted operations request (adds my case). Not resubmitting (avoid double charge).
- Board: STRONG claims now also t 8c01 (4.82/5.19/4.55), v S7×T1 single outer α (1.56/1.93/1.79), s noQ0 (2.51/2.61/2.40; phase-only 1.73/2.32/2.14).
  f: phase-only s21 ceiling ≈1.72 for 4 directions. ap: leaders' γ on uniform LL0 do nothing/lower → gain is γ×ρ* cooperation.
  c: α·β within one orbit additive; superadditivity is cross-orbit (relevant to perpchi: P, E, D are on different shells → expect superadditive).

## 14:15 — wakeup 7
- pc1 landed (stuck lane resolved itself). Posted result 20261014T141155.274Z_swarm-m_result_34e7:
  P(α⊥)×E / P×D superadditive, excess grows with |α⊥| (+0.37 at −0.3); E+D destructive at s21 (1.478 < E 1.558). Best ba06 P−.3+E+D 2.811/3.516 (r56 pending).
- Records now R≈6–10 at s21 (o f5f1 6.28/8.33/8.12 conv 8.33 STRONG; t 6506 8.71/8.71; av e0a8 10.39 s21; s c325 9.87 s21), hugging Σ|α|≤2.5 / Σ|β|≤2.0 caps.
  Records use S1/S2(/S3) × T1(/T2/T3). Mechanism: not density (k,i controls), not interaction scale (u,k), needs γ×ρ* (ap).
- Submitted re1: t's 6506 + E×{1,2,3,4} (S3 chiral-odd β; β room under cap). ids 9a3c 858c 3d93 8482. Mailed aa (lead3 does c662/8c01).
- Plan: if E lifts 6506, post; otherwise close perpchi with final coverage. Consider wrapping up — swarm is saturated on record rays.

## 14:45 — wakeup 8
- ba06 (P−.3+E+D) full ladder: 2.811/3.516/3.135/conv 3.516 (STRONG by metric; dominated by records).
- E1+D1 (3991): s21 1.478 but r46 2.084 ≈ additive (1+.641+.404 = 2.045) → E·D destructive interference is an s21 artefact (as the result post anticipated). Post in the final update.
- Board: av e0a8 STRONG 10.39/9.87/10.50/conv 9.96 (coherent cos2δ+i sin2δ rule on S1–S3×T1). Many agents closing (c, ae, ac, p, q, g, ak, aj, d).
  u: qmax-8 makes pair interaction non-PSD at R≈10 (watch conv). ai/t: Σ caps chart-dependent (requests to human).
- re1 (6506+E) still pending. NEXT: when re1 + r56 land → final perpchi result/coverage, then swarm done.

## 16:36 — wakeup 9: closing
- re1 done: 6506 + E×{1..4}: min 8.52 / 9.37 / 10.20 / 10.24 (8482: 10.239/11.029/10.665/conv 11.034). s21 plateaus; r56 lifted most.
- E1+D1 r46 2.084 = additive → s21 interference artefact.
- Posted final result + coverage 20261014T163533.977Z_swarm-m_result_4a32; mailed t.
- Board records ~11.6–12.8 (h 5063, e c577, av 55f9), cap-limited; qmax concerns above R≈12 (u, an). Swarm saturated; most agents closing.
- Decision: swarm done (33/500 charged). Nothing distinctive left for me that others aren't covering.
