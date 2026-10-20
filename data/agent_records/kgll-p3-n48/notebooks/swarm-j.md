# swarm-j notebook

Started 2026-10-14T10:24:20+00:00.

## 2026-10-14 11:25 — wakeup 1: scope chosen, batch 1 submitted
- Read brief, docs 40/46, theory §2/§6, key-facts, board (a,b axis maps; c jorb; d chiral-phase half-shells;
  e bigamp lines + Sobol S1-S3; f chiral-odd phase; g joint-orbit C3 channels + cos·cos note; i kpow (= my
  first idea, parent-shaped k-dependent contrast — dropped); l phase-even β² curvature).
- Representability: block is cos(G·r)cos(k·R) only (sin·sin unreachable) — already posted by g and l, not reposted.
- ED mode: default full_ed (no symmetry reduction) → C6/mirror-breaking deformations are safe.
- Key data (swarm-c S1×T1 orbits, s21): ⊥ (δ=90°) α=−0.05 → 1.1709, +0.05 → 0.8026; +30 β+0.03 → 1.1595;
  −30 β−0.03 → 1.1524 (mirror partner, ~0.7 % cluster-chirality artifact); ±30 α+0.05 → 1.046/1.052.
  Parent Δ_s21 = 2.2586e-4, Δ_LLL = 1.827e-4 (parent only 1.24×LLL despite M2=10).
- Chose family `perp-amp`: non-perturbative α_⊥ (R ⟂ G) line + S2T2/S3T3 ⊥; hypothesis 20261014T112216.867Z_swarm-j_hypothesis_ff8e.
  Mailed c, g, f. Scripts: work/perp.py (orbit geometry checked), work/s1t1.py (unused lines), work/breathe.py (dropped).
- Batch 1: 17 requests (work/inputs/batch1). Precheck: M2(k) decreases along −α_⊥ (9.17 at −0.6), S ratio ≥ 0.027.
- Next: read results; promotions give finite-size profile; batch 2 = α_⊥ × chiral-odd β plane + S1×T1 amplitude ascent.

## 11:45 — wakeup 2
- Board exploded (~45 posts). ⊥ line triplicated: j, r (gc-perp), q (fs-scan). Mailed r, q: I stop after batch 1 (already charged),
  r keeps ⊥ grid/CMA. Batch 1 still pending in queue.
- Leaders: S2×T1 +60 β+0.03 (c d698) s21 1.249, r46 1.404; S2×T1 ∥0 α+0.05 1.217; S1×T1 ⊥ α−0.05 1.171 (r46 1.170).
  MT symmetry confirmed. e: full stars break manifold at |α|~0.1-0.2, |β|~0.12 → my far ⊥ points likely FAIL.
- s's note: ⊥ channels (S_sT_s, R=ẑ×G) are half static LL mixing (Q=0) — tag in coverage.
- Holes per p: inner+outer combined optimizer; large-amp non-⊥ α orbits. Decide pivot after batch 1 lands.

## 12:06 — wakeup 3: ⊥ line is the board leader
- Batch 1 results: S1⊥ α −0.45 (ea28) s21 1.6386 / r46 2.6321 / r56 2.4446, conv46 running → SUGGESTIVE (dup of q c027, r e99d).
  r46 monotone: 1.12 (−.035) … 2.09 (−.3), 2.63 (−.45). s21 saturates ~1.47 with split/Δ → 0.094 at −0.3; r −0.35 FAIL 0.108; −0.6 FAIL 0.318.
  S2T2⊥, S3T3⊥: weak or FAIL (stiff) — matches g.
- ak critique: branch change at s21 between −0.35/−0.45. Submitted fill-ins −0.40,−0.425,−0.475,−0.50,−0.55 (batch2, 5 evals; total 22 charged).
- Posted result 20261014T120545.329Z_swarm-j_result_bdd3 (line table + coverage, Q=0 caveat).
- Agreed split: r owns ⊥×chiral grid + ⊥ CMA; q owns +30 β line + finite-size audit. k running density controls for −0.45.
- c claimed STRONG for S2×T1 +60 β 0.03 (phase-only): 1.249/1.404/1.347.
- Next: fill-ins → resolve branch; consider ⊥ line + S2×T1 phase leader combination? (r/x territory — check first).

## 12:33 — wakeup 4: STRONG claim posted
- ea28 conv46 2.6322 → broker STRONG. Also STRONG: 0f6d (−0.10, min 1.315), 7c30 (−0.15, 1.4135), 298a (−0.2, 1.4535), 0d26 (−0.3, 1.4675). b7de (−0.075) suggestive, conv46 pending.
- k density controls for −0.45: static <ρ_k> R 0.940/0.939/0.935, M2-matched 0.963 → gain not density.
- e: PES EG drops 13.4 (parent) → 2.5–3.8 on ea28 (still >> 0.5). g: band fidelity move ~3%. ac: HF dispersion flattens 7×.
- Posted claim 20261014T123244.118Z_swarm-j_claim_3d0f (STRONG, amplitude, Q=0 caveat, conservative fallback −0.30).
- Others now on ⊥: r (⊥×chiral grid, ⊥ CMA), m (perpchi: α⊥ × S3T1/S2T1 phase leaders), aq (⊥ momentum harmonics), ak (β⊥ on line).
- Fill-ins −0.40..−0.55 still pending. Budget 22/500.
- Next options: inner ⊥ + outer α contrast (h's S4×T1 c0+, no Q=0) combo — check x/h/o first; otherwise critique/verify role.

## 13:05 — wakeup 5
- Fill-ins still queued (broker congested). Board frontier moved: multi-orbit α+β steps superadditive — h c662 STRONG 4.76/5.23/4.67,
  t 8c01 s21 4.82/r46 5.19; both carry S1⊥ α (Q=0) content (r ablating). s noQ0 combo 2.51/2.61/2.40 with no ⊥.
- k: density excluded for all α claims. g critique: parent near-zero-mode at d_sc=0.1 → R amplified; asked human for d_sc control.
- s: α and β pieces split the s21 manifold oppositely → s21 splitting is the binding gate everywhere.
- Plan: wait for fill-ins, close perp-amp with final coverage; then pick small, distinct task (gate-aware / verify) — avoid herd.

## 13:40 — wakeup 6
- Fill-ins SUBMITTED since 12:05, no result (likely stuck lane, like swarm-o's). Posted request addendum to o's ops request.
- Board: g retracted 1/d² critique. f: phase-only s21 ceiling ~1.72 across 4 directions. v STRONG with outer S7×T1 α contrast (no Q=0).
  ap: leaders' γ on uniform LL0 → no gain / loss, so the gain is γ×ρ* cooperation. y audit: cluster ranks agree (Spearman ≥0.975).
- I'm not joining the crowded frontier. Holding budget (22/500). Will close perp-amp once fill-ins land.

## 14:17 — wakeup 7
- Fill-ins landed at s21 (lane was slow, not lost): −0.40 FAIL 1.523 (split 0.102); −0.425 1.5688; −0.475 1.7400 (r46 2.6633);
  −0.50 1.8819 (r46 2.6504); −0.55 1.8420 (r46 2.4579). r56 pending for a141/e99a/03c5.
  s21 splitting peaks at −0.35..−0.40 then falls back (avoided crossing in the s21 spectrum; r46 smooth) → ak's branch worry resolved.
  New ⊥-line best is −0.50 (s21 1.88 / r46 2.65), pending r56.
- Board records now ~10× at s21 (av cos2δ+i·sin2δ rule; s noQ0 9.87/10.15), cap-limited (Σ|α|, Σ|β|), not gate-limited.
  Many agents have run `swarm done` (d, ak, p, g, aj, q, ae).
- Plan: wait for r56 of the fill-ins, post closing result + coverage for perp-amp, then `swarm done` (nothing distinctive left
  for my budget: the frontier is crowded and boundary-limited).

## 14:48 — wakeup 8
- Fill-ins at r56 stage (r46: −0.425 2.5633). Waiting once more for r56 then close. r: removing ⊥ keeps 83–93% of c662/8c01; o: ⊥ ≈ 40% of f5f1. Records ~10× (av e0a8 STRONG).

## 16:35 — wakeup 9: closed perp-amp, done
- r56 for fill-ins still pending after >2 h; closed the family anyway (broker finishes rungs). Closing result
  20261014T163352.978Z_swarm-j_result_69d5 with full line table + coverage.
- Final: 22/500 evaluations charged. Best min-over-clusters 1.6386 (ea28, STRONG, claim 3d0f); best s21 1.8819 (e99a).
- Ran `swarm done`: the frontier (~10–14× records) is crowded and cap-limited, and verification requests are with the human.
