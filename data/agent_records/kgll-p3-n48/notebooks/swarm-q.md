# swarm-q notebook

Started 2026-10-14T10:24:45+00:00.

## 2026-10-14 wakeup 1 (11:18–11:25 UTC)
- Read brief, theory §6.4, doc 40 (024 pilot: +0.51% 4×6 → −0.92% 5×6), doc 46, ADR-0040, board.
- Parent w1c: s21 Δ 2.2586e-4, r46 2.4101e-4, r56 2.5901e-4. R_staticM2 ≈ 0.124 (deep M2 saturation).
- Board: a/b axis maps (60 full-star axes, duplicates of each other), c jorb (joint orbits), d chiral-phase half-shells,
  e bigamp, g joint-orbit channels (+ note: block is cos·cos only, sin·sin unreachable), i kpow, f chiral-joint, l phase-even.
- Key data (swarm-c s21): S1×T1 ⊥(90°) α=−0.05 → 1.1709 (req_7133), +0.05 → 0.8026; +30° β=+0.03 → 1.1595 (ce1f),
  −30° β=−0.03 → 1.1524 (c75e) [mirror partners agree → chirality artifact small]; ⊥ β±0.03 ≈ 0.98 both (even).
- My family `fs-scan` (hyp 20261014T112330.630Z_swarm-q_hypothesis_ed45): 1-D line scans to boundary along
  ⊥ S1×T1 α (per-entry −0.02…−0.6) and +30° S1×T1 β (0.015…0.3); 16 evals submitted (work/A, gen in work/gen.py,
  same star ordering as swarm-c). Purpose: finite-size curve via free promotions.
- Mailed c, g. Next: read results; stage B additivity grid (α_⊥, β_+30) around 1-D optima; mirror check; transfer analysis.
- Idea to post later: a linear-in-α slope cannot come from the BZ-averaged density (F_p zero-mean → ⟨ρ_k⟩_BZ changes at O(α²)).

## wakeup 2 (11:40 UTC)
- Board exploded (~45 hypotheses). Heavy herding on S1/S2×T1 orbits. Top s21: f chiral-joint 1.558 (e5d5), 1.483; c d698 S2×T1 +60 β0.03: s21 1.249, r46 1.404.
  c 7133 (⊥ α−0.05): s21 1.171, r46 1.170, r56 1.160 → "suggestive", in conv46. Chiral phases transfer (r46 ≥ s21).
- j/r/q triplicate ⊥ line. Agreed with j: I drop stage B (r owns ⊥×chiral grid/CMA). Keep +30 β line + finite-size line-profile role.
- swarm-s: ⊥ channels (S_s×T_s, R=ẑ×G) contain Q=0 = static LL mixing (guiding-centre identity) — I checked the logic, agree.
- My 16 requests still queued after 25 min (broker backlog). Spend few evals; value via analysis/critique.
- Next: read stage A results; then pick the best combined optimum from optimizers (z,n,ag,x,s) and run parent→opt→beyond line.

## wakeup 3 (12:07 UTC)
- Stage A landed (table in post 20261014T120853.419Z_swarm-q_result_5bc6). +30 β: s21 peak ~0.06 (1.247), r46 1.315; 0.09: s21 1.20, r46 1.465; ≥0.12 FAIL.
  ⊥ α: s21 plateau 1.45–1.47 (−0.2…−0.3), −0.45: 1.639/2.632/2.445 SUGGESTIVE (conv46 pending; hash shared with j ea28, r e99d). −0.6 FAIL.
- Key finding: s21 splitting/Δ grows 8–30× faster than r46 → s21 binds via gate; r46 smooth (no jump at −0.45, answering ak's branch critique).
- c claimed STRONG: d698 S2×T1 +60 β0.03: 1.249/1.404/1.347. f e5d5 (S3×T1 chiral β+0.05) 1.558/1.641/1.560.
- k: matched-density control for α⊥−0.05 explains none of gain; k running controls for −0.45.
- r has −0.40/−0.50/−0.55 ⊥ points; I submitted +30 β 0.075, 0.105 (f953, b5ea).
- Mailed ak, z, n, ag about the s21-gate caution.
- Next: r56 values; final coverage post. Then consider fs line through combined optimum (when optimizers report).

## wakeup 4 (12:35 UTC)
- ⊥ line now 3-cluster: α −0.15: 1.414/1.523/1.466; −0.20: 1.454/1.707/1.615; −0.30: 1.468/2.091/1.922; −0.45: 1.639/2.632/2.445 (conv46 = r46).
  j claimed STRONG on −0.45 (hash-shared with my c027). k: density controls for −0.45 give R 0.94–0.96 → density lowers gap; gain not density. Q=0 (static LL mixing) half not excludable in cos·cos block.
- f claimed STRONG S3×T1 chiral β+0.05 (1.558/1.641/1.560); c STRONG d698. e: EG drops 13→2.5 along leaders (still PASS). g: asks for gauge-covariance solver check.
- +30 β r56 pending; fill-ins f953/b5ea queued. Nothing new submitted this tick. Next: final fs-scan coverage post when r56 lands.

## wakeup 6 (13:06 UTC)
- Frontier moved to superadditive multi-orbit α+β combos: h c662 STRONG 4.76/5.23/4.67 (density control 0.995 → not density; contains ⊥ Q=0 α −0.058); t 8c01 s21 4.82/r46 5.19.
  av: records follow angular rule α∝cos2δ, β∝sin2δ on S1/S2×T1. c: leaders restore the smooth M2 law (R_beyondM2 0.12→0.72), w1c is anomalously weak (M2 saturation).
  g critique: parent ~zero mode at d_sc=0.1 (asks d_sc control); p counter-critique.
- My +30 β r56 and 2 fill-ins still queued (~1 h). My "line through combined optimum" is covered by h's un2 (s>1) and as's robustness → not doing it.
- Plan: low activity; post final fs-scan coverage when r56 lands; watch for human answers (sin·sin sector, LL-mixing control) that might open a new uncovered direction.

## wakeup 8 (13:37 UTC)
- My 2 fill-ins (submitted 12:08) and 7 r56 promotions still pending; o and j report stuck lanes (requests 1724, 6267) — likely same cause. Not adding a third report.
- Board: STRONG claims now from c, f, j, h (c662 4.76/5.23/4.67), t (8c01), v (S7×T1 single outer α 1.56/1.93/1.79), s (noQ0 phase-only 1.73/2.32/2.14).
  f: phase-only s21 ceiling ~1.72 across directions (s21 splitting gate) — consistent with my fs-scan reading. y audit #2: r56≈0.96×r46; min is s21 or r56.
  ap: leaders' γ on uniform LL0 inert/negative → gain is γ×ρ* cooperation. g retracted 1/d² critique.
- Still waiting to write final coverage.

## wakeup 9 (14:08 UTC) — closing
- Fill-ins: +30 β 0.075 → s21 1.237 (sp .048); 0.105 → FAIL (sp .143). Posted final coverage 20261014T140909.358Z_swarm-q_result_fee8.
- Board records now s21 6–8 (o f5f1 6.28/8.33/8.12, boundary-limited by Σ|β| cap); everything I could add is owned by ≥1 other agent.
- Decision: swarm done (12 evals charged). r56 for the +30 line will land in the store on its own.
