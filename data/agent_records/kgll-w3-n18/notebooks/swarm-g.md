# swarm-g notebook

Started 2026-10-15T04:13:13+00:00.

## 2026-10-15 wakeup 1 (04:20–04:27 UTC)
- Board: swarm-a w3-atlas (30 separable dirs ±α0.10 ±β0.05), swarm-b w3-joint ((G,R) classes + chiral 7-split×T1),
  swarm-c w2-atlas, swarm-e w3-bigamp (large amplitudes).
- Insight: MT (mirror∘TR) symmetry of LL0+parent maps (α,β)->(α,−β) on achiral stars; chiral orbit a<->b with β->−β.
  => TL response even in β on achiral dirs. All clusters (s21, r46, r56) are NOT mirror-symmetric (work/cluster_sym.py):
  s21 has C6 only, r46/r56 C2 only. So odd-β parts on any of them are cluster-shape artefacts. Control: run (α,−β).
- Posted note 20261015T042457.857Z_swarm-g_note_b6ff and hypothesis 20261015T042513.177Z_swarm-g_hypothesis_bf5c
  (family w3-chiral-phase). Mailed swarm-b.
- Tools: work/stars.py (orbits), work/gen.py (OUT PARENT S:T:alpha:beta ...), orbit 'a' contains (3,2)/(4,3)/(5,3)/(5,4).
- Submitted batch A1 (24 evals: 7a/b,13a/b × T1-3 × β±0.05), ids in work/batchA1.ids.
- NEXT: submit batch A2 (19, 21; work/batchA2/, 24 files) when in-flight allows; analyze g_chi vs g_shape.

## 2026-10-15 wakeup 2 (04:42–04:50 UTC)
- Chiral phase A1 results: M·T holds (Ra(+β)≈Rb(−β) ≤0.6%); chiral slope real (7×T1 g=+0.73, 13×T1 −0.56) but
  curvature huge (−0.1..−0.6 at β=.05) -> max gain ~0.3%. Posted result ee87 (with coverage) + abandon d524. Skipped 19/21.
- Board: G⟂R matched joint class (S1⊥, α>0) gives w3 1.37 (swarm-j 7d04, α=0.2/pair); f06f robust_positive 1.088.
  ~8 agents herd on mechanism controls; b, e, j, i, k on w3 ⟂.
- On w2, ⟂ class LOSES both signs; oblique 30°/150° classes at α=−0.05 gain (1.035–1.038 s21, 1.044 r46).
- New family w2-oblique (hyp 0abd). work/genjoint.py OUT PARENT SHELL c_perp c_150 c_30 [betas] (pair stars,
  R_j=(n,−m)). Submitted 14 (work/w2B.ids): obl line c=−0.05..−0.4; c150 line; c30 −0.2 (MT check); obl×⟂ cross.
- Mailed i, k (they duplicated each other's w2 runs), c.
- NEXT: analyse w2B; refine (c_obl, c_perp); maybe add S2/S3 classes; request matched-density control if winner.

## 2026-10-15 wakeup 3 (05:03–05:06 UTC)
- w2B results (s21 / r46): obl −0.05 1.0825/1.0883; **obl −0.10 1.1135/1.1491**; obl −0.15 1.0894/1.1218; −0.2 1.0108; −0.3, −0.4 FAIL.
  c150 −0.1 1.0528/1.0783; c150 −0.2 1.0052 ~ c30 −0.2 0.9953 (MT ok). obl−0.1 & ⟂+0.05 1.1140/1.1270; ⟂−0.05 1.0483/1.1197;
  obl−0.2 & ⟂+0.1 1.0635/1.0517; ⟂−0.1 0.8904. Several climbing to r56.
- swarm-c posted the SAME family w2-oblique 1 min after me (hyp 2372), with sign rule α·w_parent(G±G_R)>0. Mailed split:
  c = S2/S3 classes on top of B; me = S1×T2/T3 classes on top of B (B = obl −0.1), then (c_obl,c_perp) refinement.
- New tool work/genclass.py: TERM S,T,ANG,alpha[,beta] (angle = θ_R−θ_G mod 180). Verified vs genjoint and 7d04.
- Submitted w2C (8): B + {S1T2 ∥, S1T2 obl(60+120), S1T3 ⟂, S1T3 obl(30+150)} × ±0.05. NB T3 aliased on r46 (swarm-f).
- Board: w3 ⟂ strong claim 7d04 (1.369/1.386/1.306/1.386); controls say beyond-M2. swarm-h credits my MT note.

## 2026-10-15 wakeup 4 (05:21–05:30 UTC)
- STRONG w2 claims: 141f obl−0.1: 1.1135/1.1491/1.1311/conv 1.1473; 88e5 (+⟂0.05): 1.1140/1.1270/1.1136/1.1259.
  Posted claim f9c8 (claim 1 only). swarm-c reproduces (2aa0, e346).
- Recentred S1 atlas on B: S1T2∥, S1T2obl, S1T3⟂, S1T3obl all lower B; quadratic gain ≤0.4%. B = S1-space local max.
  Posted result (coverage block).
- Built work/matched.py (BZ-avg ρ̄ static control, |G|²≤64). M2(ρ̄)=2.491 (<2.5!) for 141f. Submitted controls
  1e03 (141f) and 8ad8 (88e5) as --control on s21,r46,r56.
- Split agreed with swarm-c: c owns |G|²=3,4 spatial classes on B (g4perp: df59 1.162/1.208); me S1 + refinements.
- NEXT: read control results -> post mechanism result (claim 2 if ρ̄ ≈ 1). Then maybe a critique post; consider
  combined local optimisation only after coordinating with c.

## 2026-10-15 wakeup 5 (05:44–05:47 UTC)
- ρ̄ controls: 1e03 (141f) 0.9974/0.9975/0.9975; 8ad8 (88e5) 0.9994/1.0004/1.0004 -> w2 gain beyond averaged density.
  swarm-q independently ran the same on 88e5/df59 (same numbers) + momentum-rotated copies 0.88-0.90.
- Built work/sharpen.py (M2-matched static ρ_P e^{κρ_P}); needed |G|²≤196 (box 14) to keep positivity on w2.
  Submitted 391d (M2 2.5828 for 141f) and 3e47 (2.6809 for 88e5), --control s21,r46,r56.
- Checked conv46: broker applies qmax/n_mesh/g_cutoff overrides to parents too (validate.expand) -> parent conv46=r46 to 7 digits is real.
- Board: w3 leader now 2.38 s21 (swarm-b 02f7: S2∥ 0.25 + chiral β 7); fe3d strong 1.69; swarm-h chiral β on S1⊥ strong 1.46.
  swarm-c strong w2 df59 (1.162/1.208/1.189/1.208). swarm-e doing w2 stacking CMA (I agreed to stay out).
- NEXT: post mechanism result once 391d/3e47 land. Then consider: chiral β on top of w2 leader is swarm-c's (w2-chiphase).

## 2026-10-15 wakeup 6 (06:06–06:08 UTC)
- M2-matched static w2 controls: 391d (M2 2.5828) 1.0201/1.0202/1.0201; 3e47 (2.6809) 1.0431/1.0435/1.0432.
  Beyond-M2 margin 141f +0.093/+0.129/+0.111; 88e5 +0.071/+0.084/+0.070. Posted result 6fdd. Mailed swarm-n (w2-staticfront).
- Critique/herding note bd77: w2-phasestack (c) == w2-phaseonly (l), 13 s apart; mailed both. Noted gap: β on top of
  B (141f) without 4⟂ — not taking it unless asked.
- Role switch: w2-oblique done; acting as verifier (controls on request). Budget 62/500.
- Board: w3 leaders ~2.4-2.9 (02f7, c89a) chiral-β dressed; r46>s21 for big leaders; r56<r46 in 43/45.

## 2026-10-15 wakeup 7 (06:38 UTC) — DONE
- Board saturated (i, d, m already done; h took my open item; c/l split resolved). Withdrew 9 low-value r56 promotions
  (kept 10c4, d35f). Posted `swarm done` summary with coverage for w3-chiral-phase and w2-oblique. 62/500 evals.
