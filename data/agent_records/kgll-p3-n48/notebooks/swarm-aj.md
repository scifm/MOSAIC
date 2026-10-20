# swarm-aj notebook

Started 2026-10-14T10:25:56+00:00.

## 2026-10-14 ~11:40 — wakeup 1 (orientation, first batch)
- Read brief, theory §6.4, docs 40/46, board (≈45 posts). Parent w1c: Δ s21 2.2586e-4, r46 2.4101e-4, r56 2.5901e-4.
- Board state: joint (G,R) C6 orbits (pair stars) carry 10–20× the separable-star response. Leaders (swarm-c jorb, per-entry units):
  S2×T1 +60 β+0.03 d698 s21 1.249 / r46 1.404; S2×T1 ∥0 α+0.05 37dc s21 1.217 / r46 1.327; S2×T1 +60 α−0.05 ad6b 1.178 / r46 1.248;
  S1×T1 ⊥90 α−0.05 7133 1.171/1.170. MT symmetry holds to <1% (θ,α)≡(−θ,α), (θ,β)≡(−θ,−β).
  Full stars break the manifold at |α|≈0.1 (S2/S3), |β|≈0.12 (swarm-e).
- Herding: ~25 agents in S1/S2×T1 orbits, many surrogates/CMA (o,t,h,z,n,ag,am,x). I took swarm-c thin spot #4:
  **s2kprof** = α momentum-profile of S2 orbits (S2×T3 δ0/60, S2×T2 δ30, T1+T3 profile at 37dc/ad6b). ae has β side.
- Tools: work/orb.py (orbits, pair-star blocks, block→entries), work/gen.py (make_input), work/harvest.py (board → orbit coords, work/harvest.json).
- Batch b1 (10 reqs) submitted 11:37: 7d04 8117 ab57 0a46 bb68 8c6e 3966 1605 3cb2 2b1f. Hypothesis 20261014T113718.122Z_swarm-aj_hypothesis_f795.
- Independence note posted (accidental `ls $MOIRE_MAIN`).
- Next: read b1; if T3/T2 slopes ≥3%/0.01 or profile beats leader → batch 2 ratio lines; watch r46/r56 of leaders.
  Critique candidates: Σ|α| boundary is representation-dependent (swarm-h already noted).

## 11:55 — wakeup 2
- b1 still pending (queue loaded). Board: ⊥ α S1×T1 lines (j/q/r triplicate) at s21 1.6386 (M2k 9.44); f chiral-odd β S1×T1 e5d5 s21 1.558 / r46 1.641.
  d698 now r56 1.3465 → "suggestive", in conv46.
- **My s2kprof is herded**: ao (kprof, posted 1 min before me), av, ar, i (hiT-orb), e (orbmap2), au (harmladder) all cover T2/T3 copies.
  Plan: let b1 land, post its numbers as a result w/ coverage, cede the family, switch.
- Remaining holes (p's note): (1) final-candidate verification [p took]; (2) inner+outer direct optimizer [at, an, am-B partly];
  (3) large-amplitude non-⊥ α orbits (∥, ±60 on S2×T1) — but u: S2×T1 points already use 30–50% of s21 split/Δ gate.
- Candidate next role: critique (rule 11) + something un-herded. Think about s21 split gate on S2 directions.

## 12:15 — wakeup 3
- b1 still queued (37 min). Withdrew 6 S2 T2/T3 map points (bb68 8c6e 3966 1605 3cb2 2b1f): ar owns the full inner T2/T3 α map (±0.05). Kept 4 T1+T3 profile points at S2 leaders (7d04 8117 ab57 0a46) — c recommends profile shaping at leaders as the non-dup work.
- Board: STRONG claim S1×T1 ⊥ α=−0.45 (j ea28 / q c027): s21 1.639, r46 2.632, r56 2.445, conv46 2.632. s21 splitting is the binding gate (q, j, u).
  k: density controls lower the gap (0.94–0.96) → not density. s: ⊥ is half Q=0 static LL mixing (untestable in cos·cos block).
  c STRONG phase-only claim d698 (S2×T1 +60 β 0.03). x d524 s21 1.92 (combo).
- Next: post s2kprof result when profile points land; then pick audit/critique work or a non-herded niche.

## 12:45 — wakeup 4
- My 4 profile reqs still SUBMITTED (queued since 11:39). Board records now multi-orbit α+β small-amplitude combos:
  t 8c01 s21 4.816; h c662 s21 4.760 / r46 5.226; t f0fb 3.51/3.86. h: α·β strongly superadditive.
  Claims STRONG: j ⊥α −0.45 (3d0f), f S3×T1 chiral-odd β 0.05 (728b), c d698.
- work/audit_top.py: top-15 table — records use small per-entry amps (am ≤0.13, Σα ≤1.5, Σβ ≤0.72; well inside boundary),
  S-ratio 0.10–0.19 (fine), s21 split/Δ ≤ 2.2e-2, PES eg 3.8–6 (vs ~13 static, per e). No gate/boundary issue to flag.
- Considered (and REJECTED) mechanism note "near-contact V=tanh(0.2q)/q makes parent gap D'^3-suppressed; LL mixing unlocks contact term":
  wrong — contact term vanishes for spinless fermions in ANY band (Pauli). Not posted.
- Next: result for s2kprof when profile points land; then decide (audit/verification spot evals, or a niche).

## 13:15 — wakeup 5: first data
(R s21 / split/Δ s21; r46)
- 7d04 S2T1∥+0.05 & S2T3∥−0.02: 1.0387 FAIL split 0.120
- 8117 S2T1∥+0.05 & S2T3∥+0.02: 1.1760 (0.018); r46 1.2271  [T1-only 37dc: 1.2166 / r46 1.3269]
- ab57 S2T1+60 −0.05 & T3 −0.02: 1.0703 (0.016); r46 1.1448
- 0a46 S2T1+60 −0.05 & T3 +0.02: 1.1126 (0.075!); r46 1.2592 [T1-only ad6b: 1.1784 / r46 1.2478] → +0.9% at r46 only, s21 split near gate
- map: S2T2 δ30 α−0.03 0.9271, +0.03 1.0199; S2T3 ∥ α−0.03 1.0306, +0.03 0.9067 (T3 opposite sign to T1, as av says). 3cb2/2b1f (S2T3 δ60) pending.
- Reading: T1+T3 shaping at the S2 α leaders is strongly concave in T3 (curv ≈ −450…−550 /unit² in R); optimal T3 ≈ 0.001–0.003, gain ≲0.5% s21. T3 raises s21 splitting fast.
- Board: STRONG c662 (h) 4.76/5.23/4.67/conv 5.23; 8c01 (t). Mechanism debate: g (d³ amplification) vs p (contact inert — same as my rejected idea).
- Plan: post s2kprof result+coverage when 3cb2/2b1f land; then low spend (queue congested: my evals waited ~90 min), critique role.

## 13:40 — wakeup 6
- s2kprof CLOSED: result 20261014T133534.382Z_swarm-aj_result_0e53 (coverage inside). 3cb2 S2T3+60 α−0.03 0.9077, 2b1f +0.03 1.0373.
  r56 promotions of 8117/ab57/0a46 still pending — reply to the result when they land.
- New record o f5f1: s21 6.277 / r46 8.325 PASS; Σ|β| 1.88 (94% of bound), Σ|α| 1.59, eg 3.0/2.3, S 0.088, R_beyondM2 r46 1.15. Mailed o.
- Records: c662, 8c01 STRONG ~4.6 min; claims also from v (S7×T1 α contrast), s (noQ0), f (phase-only s21 ceiling ≈1.72).
- Plan: low spend (queue congested, swarm saturated). Critique/audit; watch for human answers opening new questions.

## 14:08 — wakeup 7: finishing
- Board: s21 records ~10.4 (av cos2d e0a8), 9.87 (s noQ0). Many agents done (d, ak, p, g). Queue congested (stuck-lane reports o/j/m/ah).
- Every sector I could name is covered (orbit maps all shells/T stars, nematic, MT-odd, profile, inner×outer, record-gradients, density/LL0 controls, kernel numerics, rotation test).
  t asked human about representation-dependent Σ caps (789e); u confirmed f5f1 Σ|β| minimal over rewritings.
- Decision: swarm done at 10/500 charged — extra load would slow agents on the frontier; no non-duplicated direction left for me.
