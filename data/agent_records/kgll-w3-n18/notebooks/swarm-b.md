# swarm-b notebook

Started 2026-10-15T04:12:56+00:00.

## Wakeup 1 — 2026-10-15 ~04:20Z
- Read brief, docs 40/46, kdep_envelope. Parents: w3 Δ_s21 = 4.5714e-4, w2 3.2271e-4.
  w3 density lives on even-G sublattice (|G|²=4,12,16), w2 on |G|²=3,9,12.
- Doc 46 hint (Nk21): w3 α[S1,T1] = +0.05 → +1.85 %, −0.05 → −9.04 % (big odd part).
- swarm-a took `w3-atlas` (separable 30 S×T directions, α ±0.10, β ±0.05, g_cutoff 4+max|m,n|).
- **My family `w3-joint`** (hypothesis 20261015T041912.094Z_swarm-b_hypothesis_9424):
  pair-star rep: spatial stars {±g^j G0}, momentum {±g^l R0} (j,l=0..2, g=60°), α/β = circulant
  M[j,l]=c[(l−j)%3]. Class d ↔ relative angle θ(G,R) (mod 180). Equal c=α/3 == separable α (verified).
  S1×T1 classes d=0,1,2 ↔ θ=30°, 90°(⟂), 150°(−30°). S1×T2(|R|²=3): 60,120,180(∥).
  Chiral: |G|²=7 split into C6 orbits L={(1,3),...} and R (mirror partners).
- Code: work/gen.py (helpers, joint()), work/stageA.py (inputs). Inputs saved in work/inputs/A1, A2.
  File naming uses |G|² and |R|²: j_S{|G|²}T{|R|²}_d{class}_{a|b}{p|m}; amplitude c=±0.05, phase c=±0.025;
  chiral c_S7{L|R}T1 α ±0.10, β ±0.05.
- Submitted A1 (32 reqs: S1T1, S1T3, chiral). A2 (24: S3T1, S4T1) pending a free slot.
- Next: collect A1 results, submit A2, analyse class decomposition vs swarm-a separable atlas.

## Wakeup 2 — 04:37Z
- A1 results (s21): **S1×T1 ⟂ class (d1) α+0.05 = f06f → ROBUST_POSITIVE** (s21 1.105, r46 1.088, r56 1.092, conv46 1.088).
  d1 α−0.05 = 0.833 (big odd part). All other classes (±30°, S1×T2 all three), all β, chiral |G|²=7 → <1.
  M·T mirror pairs agree ≤0.6 % (finite-size floor). Table in result post 20261015T043928.538Z_swarm-b_result_9d98.
- Posted claim 20261015T043952.019Z_swarm-b_claim_b453 (claim 1 only; mechanism + LL-mixing scope caveats).
- Swarm herded onto ⟂: j (S1⊥ α line to 0.55, S2⊥, S3⊥, stage B), i (S2⊥/S3⊥ + w2), k (cyclo decomposition),
  and controls by a, l, m, o, p, q, r. 7d04 (j, S1⊥ α=0.2) s21 1.369 / r46 1.386 but M2_k +30 %.
  Interpretation (j/i/o/p): matched G⟂R, |R|=ℓ²|G| term = cyclotron e^{iGη} (effective LL mixing) + counter-moving
  guiding-centre harmonic at 2G (on w3's |G|²=4 shell). Human asked by j (request 9d01) whether in scope.
- NOTE: first digest marked 11 mails read but I only saw 4 (head cut). Unseen: likely from k,l,m,o,p,q,r re f06f.
  Always run digest without truncation!
- Submitted A2 (work/submitted_A2.tsv, 24) and C02 complement probes around S1⊥ c=0.2 (work/submitted_C02.tsv, 17;
  builder work/stageC.py BASE). Mailed j & i: I own the orthogonal complement.
- Next: tabulate A2 + C02 (work/collect.py reads work/submitted_*.tsv). If complement directions add gain, line-search them.

## Wakeup 3 — 05:02Z
- A2: |G|²=3×T1 d0 (θ=180°, G∥R, "S2∥") α+0.05 = a90f s21 1.0995 r46 1.092; others <1; |G|²=4×T1 flat ~0.97–0.986.
  I ACCIDENTALLY withdrew a90f → resubmitted identical input = f022 (work/submitted_A2b.tsv). swarm-r runs S2∥ line + S1⊥ combos.
- C02 at B=S1⊥ c=0.2: base 065b reproduces 7d04 (s21 1.3693, r46 1.3857, r56 1.3060). All 16 complement
  probes below B on s21 and r46 → withdrew their promotions (and 065b). Posted result 20261015T050431.998Z_swarm-b_result_81d6.
- Board: j claim strong (7d04). Controls: ρ̄ matched gives 1.001 → beyond density; M2-matched static ~1.18–1.20 < 1.31–1.39.
  Uniform parent: S1⊥ loses → parent-interference (resonance onto w3 |G|²=4 shell). a: CMA 14-D around 7d04;
  d: re-centred atlas at B; o,l: outer-shell α classes (resonance rule); q: chiral l=2 on S1⊥; n: static front.
- NEW family `w3-cjphase` (hyp 20261015T050705.693Z_swarm-b_hypothesis_c971): phase-only on class-resolved chiral joint
  classes |G|²=7,13,19,21 × T1 (+7,13 × T2), β ±0.05; builder work/stageP.py + work/chiral_classes.py; 32 submitted
  (work/submitted_P1.tsv). Goal: clean beyond-M2 phase-only winner via M·T-allowed linear β on resonant chiral class.
- Budget: 73 + 1 (f022 free?) + 32 = ~106/500.

## Wakeup 4 — 05:28Z
- P1 (phase-only chiral classes at parent): 32/32 < 1. Odd β part in resonant 7×T1 class θ49/131 (±7.7 %),
  non-resonant ≤0.5 %; even part −12 % (7) … −39 % (21). M·T pairs ≤0.4 %. Result 20261015T053031.596Z_swarm-b_result_8b7b.
- Board: w3 leader fe3d (swarm-p, assembler) = S2∥ α=0.25 + full-orbit chiral β ±0.02 on |G|²=7 (L+,R−) × T1:
  s21 1.695 / r46 1.687. swarm-r: S2∥ alone α=0.2 1.452. swarm-h: chiral β on S1⊥ base pays.
  w2 strong: swarm-g (oblique), swarm-c df59 1.16+ (g4perp). swarm-n: static sharpening reaches 1.45 at M2=8 (control).
  swarm-p refutation: r56 orientation artefact for C6-breaking points → score by orbit average.
- X1 (work/stageX.py, submitted_X1.tsv, 15): on fe3d base S2∥ 0.25: X_full02 (≡fe3d, γ match 1e-16), X_base,
  resonant-class-only chiral β (L class (0,1)+c, R mirror (1,2) −c) at c 0.02..0.08, −0.04; non-resonant nA/nB ±0.02.
  X0_*: phase-only at parent, resonant pair c 0.01/0.015/0.02 + single L 0.015 (target ≥1.02 for promotion).
- Next: if res-only beats fe3d → line-search c, try res-only on 13 orbits (θ164/16) too, and combine with S1⊥.

## Wakeup 5 — 05:51Z
- **X1 big win:** resonant-class-only chiral β (7×T1 θ49 L+, mirror R−) on S2∥ α=0.25:
  c=0.02 1.734/1.709, 0.04 2.028/2.037, 0.06 2.271/2.358/r56 2.306, **0.08 = 02f7: s21 2.380, r46 2.585, r56 2.530**
  (conv46 pending). Non-resonant classes ±0.02: noise. fe3d (full orbit 0.02) 1.695. −0.04: r46 0.904.
- **Phase-only resonant pair at parent:** β 0.01/0.015/0.02 → s21 1.031/1.043/1.050, r46 1.058/1.101/1.146 (6826). Clean beyond-M2 candidate.
- Withdrew promotions of X_base, X_full02, nA, nB. Result post 20261015T055251.739Z_swarm-b_result_7ab4.
- Others now stack on 02f7: j c89a 2.45 (13/19/21 res β), h 4927 2.44, a 10-D CMA (resonant chiral frame), f phase-only stack.
- Y1 submitted (work/stageY.py; submitted_Y1.tsv, 15): line c 0.10–0.20 @α0.25; α 0.15–0.35 @c0.10; phase-only pair
  0.025–0.06; res β 0.04/0.08 on S1⊥0.2 base (Yp_).
- Budget ~135/500.

## Wakeup 6 — 06:14Z
- 02f7 done: conv46 2.583 → strong; claim 20261015T061535.548Z_swarm-b_claim_c33d. 8a2e (c0.04) and 396b (c0.06) also strong.
- Y1: α line @c0.10: s21 1.746/2.111/2.406/2.651/2.787 for α .15/.20/.25/.30/.35 (r46 2.35→3.05) — still rising.
  c line @α0.25: s21 2.406 (0.10), 2.358 (0.12), 2.154 (0.15), 1.411 (0.20); r46 2.80/2.98/3.11/2.91 → r46 unreliable
  at large chiral β. Phase-only pair: s21 1.050 (0.02), 1.054 (0.025), 1.054 (0.03), 1.037 (0.04), 1.002 (0.05),
  0.950 (0.06); r46 1.146/1.178/1.211/1.270. r56 pending for all. Yp (res β on S1⊥ 0.2): 1.670 (0.04), 1.764 (0.08) s21.
- Board leader: a cc13 (10-D CMA) s21 3.60 / r46 3.91. o w3-radial 3.1. d and i done early.
- Z1 submitted (8): α 0.40/0.45/0.50/0.53 at c 0.08 and 0.10 (0.53 at M2k ratio 2.94 edge). Mailed a.
- Pending deliverable: the phase-only (clean beyond-M2) 7-pair line: needs r56 ≥1.05 (and conv46) for robust_positive.

## Wakeup 7 — 06:36Z
- Z1: c0.10 α .40/.45/.50/.53 → s21 2.841/2.860/2.555/2.318, r46 2.921/2.593/2.173/1.896; c0.08 α .40 2.708/2.519 …
  Plane optimum (min s21,r46): 17fb (α0.40,c0.10) 2.84. Posted 20261015T063648.700Z_swarm-b_result_abcb.
- Withdrew 14 dominated promotions (broker congested: no r56 landed in 40 min). Kept r56-pending: 6826, 225b, f652, 651c
  (phase-only line), 6c72, b14d, 83eb, 8e7d, 17fb, bc13, bf6b.
- Leaders: a 713b s21 3.97 / r46 4.80 (CMA, many classes). h 4927 strong (02f7 + 19@67°). f: single phase-only pairs
  P13/P19/P21 beat parent too, but 4-pair stack loses (cross terms). l: w2 phase-only beats w2 parent.
- Mailed q asking for ρ̄ control on 02f7.
- Next: when phase-only r56 lands → if ≥1.05 on r46/r56 (and conv46), post claim (clean beyond-M2). No new evals planned.

## Wakeup 8 — 07:10Z
- No r56 of mine landed yet (state SUBMITTED at broker; queue slow). q queued ρ̄ control for 02f7 (convention: |h_k|²/⟨|h_k|²⟩_uc, 48² k avg).
- Leaders: a b4b8 strong min 4.497 (r46 5.75); o 7d52 s21 4.67; a 713b strong 3.97. o ablation: leader non-additive, β-only part 0.42.
- m, g, n, d, i finished early (directions over-owned). I'll finish once the phase-only line and plane r56 land + final coverage posts.

## Wakeup 9 — 07:40Z
- Still no r56 for my 12 pending points (2.5 h). q: ρ̄ control 02f7 → 1.028 (vs 2.38–2.59) → beyond density.
- Frontier: a 9419 s21 5.77 / r46 7.07 / r56 6.95; o: Σ|β|≤2.0 boundary-limited (request 752c to human).
  p, c, l finished. Waiting; then phase-only claim (if r56 ≥ 1.05) + final coverage + done.

## Wakeup 10 — 08:20Z
- Still no r56 (3+ h). 46 of my requests pending incl. withdrawn ones whose r56 is still SUBMITTED (withdraw ≠ cancel).
- f closed phase-only stacks: single pairs beat parent (s21 ≤1.054, r46 ≤1.27), stacking interferes; f652 ≡ f's bd8f (f withdrew dup).
- q, f, h, j finished. e: w2 a9a7 beyond M2. k: β reallocation at cap → 5.60/6.62.

## Wakeup 11 — 09:20Z
- r56 still stuck (>4 h). Posted operational request to human. Frontier: a 9a85 s21 8.13 / r46 8.85 / r56 9.09 / conv 9.04;
  k: same allocation independently. o, r, k finished.

## Wakeup 12 — 10:20Z
- r56 still stuck; swarm-l reports same issue (request ddd5). No human answer yet. Waiting.

## Wakeup 13 — 11:20Z
- r56 still stuck (~6 h). a closed: a6a0 min 10.56 strong (boundary). e: w2 0596 min 1.461. Waiting.

## Wakeup 14 — 12:20Z — FINISHED
- r56 stuck ~7 h (same for swarm-l). Posted phase-only coverage 20261015T122131.635Z_swarm-b_result_7683.
- Ran `swarm done` with summary (143/500 charged). Loop stopped.
