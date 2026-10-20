# swarm-l notebook

Started 2026-10-02T03:51:51+00:00.

## 2026-10-02 wakeup 1 (04:08–04:20 UTC)
- Read board: a w3-atlas (S1-S8xT1-T3 ±0.02), c w3-wide CMA (S1-S4xT1-T2), e w2-map, b+f duplicate w2 atlas,
  g+h w3-orient (pair-star joint-orbit modes U/X/C = U/A/B). Broker "looks dead" at the time (queued anyway).
- Physics insight: symmetry is MK (mirror x conj), not M. Mirror parity p: (α,β)->(α,-β) for p=+1, (-α,β) for p=-1.
  => physical linear terms only in α(mirror-even) and β(chiral). work/symcheck.py: s21 has C6 only, r46/r56 C2 only:
  no mirror on any cluster => MK-forbidden linear terms = chirality artefacts that can flip sign between clusters.
- Posted note 20261002T041448.600Z_swarm-l_note_aff7 and hypothesis 20261002T041505.565Z_swarm-l_hypothesis_9c44 (chiral-phase).
- Chiral spatial modes: C4/C7/C9 = (O_a - O_b)/√2 on 12-member shells |G|²=7,13,19 (two C6 halves, mirror images). work/gen.py, work/stars.py.
- Submitted phase 1 (24): w3 C4,C7 x T1,T2 x {β±0.03, α±0.03}; w2 same β only. ids in work/p1_w3_ids.txt, work/p1_w2_ids.txt.
- Mailed g, h (their chiral predictions reversed), a (β± asymmetry = artefact floor).
- Next: when results land, compare slope(β_chiral) vs slope(α_chiral) vs a's β± asymmetry. If β_chiral slope clearly
  exceeds floor -> phase 2 line search (β-only, box |β|≤0.15), combine with g/h C/B β data.

## wakeup 2 (04:44 UTC)
- Phase 1 results (all PASS): MK test passed — chiral α slopes ≤0.012/unit. Chiral β T1 live: w3 C4T1 +0.92, C7T1 −0.63;
  w2 C4T1 +3.69 (curv −0.18), C7T1 +3.30 (curv −0.26). T2 chiral β no slope, big curvature. Posted result aa4b.
- Board: d found w3 S4T1 orbit c2 chiral β (+1.32, curv −0.006; s21 1.036, r46 1.080). o's pooled surrogate: w3 α orbits
  (S1T1⟂, S2T1∥) + chiral β give s21 up to 1.61. i has w2 orbit-resolved |G|²=7,13×T1 queued (b2_w2) — don't duplicate.
- Submitted p2 (11, g_cutoff 10): w2 β C4T1/C7T1 at .01/.015/.02, (C4+C7)/√2 at .015–.03, C4T1 .03 g10 truncation check. ids work/p2_w2_ids.txt
- Next: fit w2 line search; after i's orbit data, line-search slope-carrying orbit(s) on w2 phase-only; aim to push w2 phase-only >1.02 to ladder.

## wakeup 3 (05:07 UTC)
- p2 results (w2, β-only, g10), s21/r46:
  - C4T1: .01 → 1.0200/1.042; .015 → 1.0248/1.064; .02 → 1.0265/1.084; .03 → 1.0201/1.108 (g6 .03 was 1.0186, so truncation +0.15 %).
  - C7T1: .01 → 1.0158; .015 → 1.0162; .02 → 1.0117 (screen only).
  - (C4+C7)/√2: .015 → 1.0279/1.0845; .02 → 1.0257/1.107; .025 → 1.0176; .03 → 1.0036. Sub-additive.
  - r56 pending for the promoted ones.
  - The r46 vertex sits further out than the s21 one: curvature is cluster-dependent.
- i's w2 orbits (±0.03): 13c3 +3.45 (curv −.076, p = 1.0655 s21 / 1.152 r46); 7c1 +3.32 (curv −.10; r46 1.135); 13c1 +1.87; others weak.
- swarm-r split: r does combos, I do single modes. Submitted p3 (8): 13c3 at .04/.05/.06/.08, 7c1 at .04/.05/.065, 13c1 at .05. ids in work/p3_w2_ids.txt.
- Board: w3 leaders are α orbits + chiral β with s21 up to 2.40 (p cc86: M2k 6.2 vs 3.63, cond 0.80, PES gap 4.7). w2 best: r e064 at s21 1.077 / r46 1.20.
- Next: fit single-orbit lines; watch r56 signs; post result with coverage. Possible: a w2 orbit-resolved T1 chiral sweep on the |G|²=19, 21 shells (d is scanning those on w3).

## wakeup 4 (05:34 UTC)
- p3 (w2 β-only single orbits, g10), s21 / r46:
  - 13c3: .04 9fcb 1.0711/1.187; .05 a4fe 1.068/1.219; .06 ccd8 1.056/1.247; .08 4f05 1.0066 (screen).
  - 7c1: .04 e269 1.0465/1.157; .05 8b73 1.037/1.172; .065 0682 1.006.
  - 13c1 .05 8e67: 0.978.
  - The s21 vertex is ~.04 while r46 keeps rising; all wait on r56. r56 queue is served by R_gap_min, so w3 points at 2.x go first.
- Board: q (abc0) finds the phase-only r46−s21 excess = 0.04 + 5·ΔT_ideality on both parents, with r56 pre-registered.
  i (f044): live T1 orbits all carry k-independent (Q_tot = 0 via parent harmonics) kernel content, i.e. LL-mixing-type static;
  this questions beyond-M2 / "momentum dependence" even for phase-only. Under question to the human via b's request 3942.
  d 2400 (w3 phase-only S4T1c2): r56 1.056, now in conv46.
- Mailed q the 1-parameter test. Mail split: r does combos, I do singles; i asked me to own the w2 single-orbit lines.
- Next: wait for r56 on 9fcb/a4fe/ccd8/e269/8b73 and 2d79/fde3, then post result + coverage. No new submissions until r56 says which cluster to trust.

## wakeup 5 (06:16 UTC)
- None of my r56 results are in yet (queue served by R_gap_min; leaders at 2.x go first).
- Withdrew 4 redundant promotions (654a, 5da4, ce79, fde3). Still kept for r56: 7213, 2d79 (C4 line), 9fcb, a4fe, ccd8 (13c3), e269, 8b73 (7c1).
- Board: claims are d c0eb (w3 phase-only 2400, robust_positive: r56 1.056, conv46 1.076; margin marginal per q),
  p cd9d (w3 cc86 STRONG, provisional), o 0125 (bd1a STRONG, provisional).
  - q 656b: phase-only r56 keeps ~half the r46 excess.
  - f 48a8: parents' r46 gap is 4.1% low, so every r46 R carries a +4.3% boost.
  - e cf2e: w3 leaders' β alone loses; r 4866: on w2 phase-only gain is real.
  - c 241d: PES eg falls 21 → ~5 on the leaders.
- Next: wait for r56 on the 13c3/7c1 lines → result post with coverage. If 13c3 r56 ≥ 1.05, a w2 phase-only claim candidate (beyond-M2 by construction, modulo i's static-content caveat).

## wakeup 6 (07:02 UTC)
- **9fcb STRONG** (w2 13c3 β = .04, phase-only): s21 1.071 / r46 1.187 / r56 1.128 / conv46 1.187, C = 1, eg ≈ 7, M2k = M2*.
  Posted claim 20261002T070244.869Z_swarm-l_claim_6c59 with caveats (f's 4×6 denominator, r56 keeps ~half the r46 excess, purity, i's static content, w2 only).
- a4fe r56 1.155, ccd8 r56 1.178; conv46 pending. e269/8b73/7213/2d79 r56 pending.
- Board: r claimed e064 (w2 phase-only combo, STRONG); w3 leaders at s21 3.47 (k 435c); claims by c (776c α-only), h (d49b), g (w2 α-only).
- Next: when the conv46/r56 runs land, post the final coverage result for chiral-phase. Then decide: done, or a new direction (the board is saturated).

## wakeup 7 (07:44 UTC)
- All ladder results in. STRONG: 9fcb, a4fe, ccd8 (13c3 at .04/.05/.06), 8b73 (7c1 .05).
  robust_positive: e269 (7c1 .04), 2d79 (C4 .03). suggestive: 7213.
- Posted final coverage result 20261002T074447.092Z_swarm-l_result_a852.
- Box-edge rule: r56 is maximal at β = .06 (box edge). Submitted a955 (β = .07, normal) and controls 3a3a (.08), a325 (.10) on r46,r56 only. Posted note.
- Next: read the vertex, then a short addendum. Then swarm done (the board is saturated; ~452 budget left unspent on purpose).

## wakeup 8 (08:10 UTC)
- Box-edge r46 legs: a955 (.07) s21 1.0355 / r46 1.2693; ctrl 3a3a (.08) r46 1.2862; a325 (.10) r46 1.2941. So r46 saturates ~.10. r56 pending.
- Board: r 75aa phase-only 636e r56 1.185 (w2 best phase-only); j c910 says the even-order cluster bias orders r46 (+0.4 %) > r56 (−0.4 %) ~ s21 (−1 %);
  e e71b audit: the top tier R>3 has split/Δ 4–9 %. Several agents are done (c, f, j, m, o).
- Next: r56 of a955/3a3a/a325 → short addendum → swarm done.
- 08:51: r56 legs still pending. q 6210 final: r56 excess ≈ 80% of r46 slope → s21 is the low outlier. ce79/fde3 r56 1.048/1.055 (suggestive).
- 09:37: r56 legs still pending (controls build on ccd8, unclaimed, so no priority bump). Plan: one more cycle, then swarm done regardless.

## wakeup 11 (10:23 UTC) — DONE
- r56 box-edge legs still pending. Posted addendum fc26, then `swarm done` (48/500 charged). Loop stopped.
