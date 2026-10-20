# swarm-ak notebook

Started 2026-10-14T10:26:00+00:00.

## Wakeup 1 — 2026-10-14 ~11:46–11:56 UTC
- Joined late (~36 min after start); 47 agents active, board heavily herded (7+ agents on outer chiral-odd β, 4 surrogates, 3 CMA-on-min, 3 nematic, 3 on α⊥ line).
- Facts learned: deformation block = pair stars, alpha/beta J×P, γ = Σ(α/2 + iβ) O_s(r) F_p(k), cos·cos only.
  Leaders: α⊥ S1×T1 line (j/r/q), chiral-odd β on S1/S2/S3×T1 (c/f), S4 α orbit (h). ce1f already "strong" (phase-only, min 1.149).
  Full-star axes break the Laughlin window at |α|~0.1, |β|~0.12 (e); outer shells need steps ≲0.01 (a).
  swarm-s identity: ⊥ channel is half static LL mixing (Q=0). swarm-k: matched-density control for α⊥=−0.05 = 0.999 (density explains none).
- Own analysis (work/splitline.py): along α⊥ line splitting/Δ rises to 0.108 FAIL at −0.35, then 0.073 at −0.45 with R jump 1.47→1.64 → suspected E4 level crossing / branch change. Posted critique (refutation f878), mailed j, r, q.
- Family `perp-cplx` (hypothesis 5ea0): β⊥ on S1×T1 ⊥ orbit at α⊥ ∈ {0, −0.2, −0.3, −0.45}. Batch 1 = 11 reqs submitted (work/pcx_b1, ids 2306 9e3a 314a 470e bba4 1045 4ca6 4f25 064e ea6a c592). Budget ≤ 20.
- Tools: work/showdef.py (print a request's deformation), work/splitline.py (R, splitting/Δ, EG per cluster), work/gen_pcx.py.
- Next: read batch-1 results; post result+coverage; then verifier/critic role (watch ea28 r46/r56; check other leaders' gate margins).

## Wakeup 2 — ~12:16 UTC
- My 11 perp-cplx reqs still pending (queue congested).
- Critique outcome: j/q/r confirm E4 crossing is s21-only; r46 line smooth (−0.3: 2.09, −0.45: 2.63), r56 2.44. ea28 now STRONG (conv46 2.63). Fill-ins −0.40…−0.55 submitted by j and r. α⊥=−0.6: 0.848 FAIL (sp/Δ 0.32).
- q: s21 splitting gate binds both S1×T1 leader lines (s21 sp/Δ grows 8–30× faster than r46). So relieving s21 splitting = the lever for min-over-clusters. That is exactly what β⊥ might test.
- k: density controls for α⊥=−0.45 give R 0.94–0.96 → gain is not density.
- Claims: c d698 STRONG phase-only (1.249/1.404/1.347), f e5d5 STRONG phase-only (1.558/1.641/1.560).
- New s21 leader x d524 1.92 (⊥α + S2 ∥/±60 α + S1 +30 β combo, sp/Δ 0.013) — combos add.
- aq started perp-prof (⊥ harmonics to relieve s21 splitting) — adjacent to mine, no overlap (they do α harmonics, I do β⊥).

## Wakeup 3 — ~12:42 UTC
- Mine still pending (queue ~45+ min deep).
- Frontier jumped: multi-orbit α+β combos from surrogates (t 8c01 s21 4.82; h c662 s21 4.76 / r46 5.23; all PASS, sp/Δ ≤ 0.02, EG ~4). h: α·β strongly superadditive along union step. j's α⊥ −0.45 now a STRONG claim.
- Mechanism: k/u/i — density controls all < 1; projected-interaction moments unchanged; gains = phase structure of form factor.
- My β⊥ study is now a side question; keep it (already charged), report, then likely verifier role or done.

## Wakeup 4 — ~13:13 UTC
- Mine still pending (80 min; o reports possibly stuck lanes, request 1724).
- Records: c662 STRONG min 4.67 (4.76/5.23/4.67/5.23), 8c01 STRONG min 4.55. av: records follow α∝cos2δ, β∝sin2δ on S1/S2×T1. Density controls ≈1 for all α claims (k). g/p debate whether d_sc=0.1 near-zero-mode amplifies R (request for d_sc control to human).
- r: ablations of ⊥ content in records in flight. Nothing for me to add right now; wait.

## Wakeup 5 — ~13:45 UTC
- perp-cplx batch 1 landed. β⊥ destructive at s21 for all α⊥ (raises s21 splitting; 5 FAILs at the 0.1 splitting gate); r46 +0.5% at α⊥=−0.2. Pure β⊥: 0.931 (0.06), 0.790 FAIL (0.10). MT spread at α⊥=−0.45: 1.584 vs 1.545.
- Posted result cbe4 (with coverage) and abandon. My earlier critique was resolved: avoided crossing in s21 spectrum (r fill-ins: −0.50 1.882, −0.55 1.842 clean).
- Board records: o f5f1 s21 6.28 / r46 8.33 / r56 8.12 (gates healthy), limited by the Σ|β| ≤ 2.0 cap. 40+ agents cover all sectors; queue is the bottleneck.
- Decision: swarm done (11/500 charged). Promotions of 2306/9e3a/4ca6/4f25/1045 will continue for free.
