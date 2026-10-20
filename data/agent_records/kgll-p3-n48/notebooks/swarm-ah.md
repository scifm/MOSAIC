# swarm-ah notebook

Started 2026-10-14T10:25:48+00:00.

## 2026-10-14 ~11:35 — wakeup 1: orientation, family `nematic`
- Board: ~20 families, all C6-invariant. Chiral joint orbits dominate: S2xT1 o+60 beta 0.03 → s21 1.2494 (_d698); S1xT1 o+30 beta 0.03 → s21 1.1595, r46 1.1586 (_ce1f). Full-star axes are ≤ 1 %.
- Unclaimed brief item: "less symmetric choices". Took it: nematic (E-irrep) combos inside joint orbits. Hypothesis post _f9ad.
  Prediction: cusp maximum at s21 (degenerate C3-related excitations split linearly).
- Builder: work/build.py (pair stars, orbit(s,t,delta), my angle convention: G1 0°, a1 30°, delta = ang(R)-ang(G) mod 180).
- Submitted: N0 replicas _9784 (d30 b+0.03), _6dc8 (d150 b+0.03); N1 pure nematic on S1T1 d30: E1± _2386/_e58c, E2± _0829/_f81d, single entry ±0.09 _8fba/_8a74.
- Next: read replicas → map my d30/d150 to c's ±30; then leader+eps*E (promotable → free r46/r56 data).

## ~11:50 — wakeup 2
- Three agents in E sector: ad (`nem`, pure E at parent), al (`lowsym`, leader+E2 at fixed orbit sum), me. Agreed split by mail: I do leader+εE (3 rotations × ±) via free ladder → orientation-resolved r46/r56. No more pure-E at parent from me.
- Orientation: my d30 orbit == swarm-c +30 (ce1f 1.1595); my orbit(2,1,60) == c's S2×T1 +60 (d698 1.2494). So replica _9784 should ≈1.1595, _6dc8 ≈0.8114.
- c result: s21≈r46 within 0.6% for all promoted chiral points. u audit: S2×T1 leaders eat 30-50% of the splitting gate.
- Prepared work/n2 (ε=0.01, 12 files: L1/L2 × Er0,Er1,Er2 × ±), checked OK. Not yet submitted: waiting for N1 cusp size so the leader+E points stay ≥ 1.02.

## ~12:12 — wakeup 3
- My N0/N1 still queued (40+ min). Queue is the bottleneck.
- Board: c STRONG claim d698 (S2×T1 +60 β 0.03): 1.249/1.404/1.347 (s21/r46/r56). f: S3×T1 chiral β +0.05 s21 1.558 r46 1.641. j: ⊥α −0.45 1.64/2.63/2.44 (s21 splitting binding). k: density controls explain none of it.
- al agreed split; al has 6 pure-E points at larger amplitude (κ readout).
- Submitted N2 (12) without waiting for N1, to save queue time: L1 = S1T1 d30 β0.03 (ce1f), L2 = S2T1 d60 β0.03 (d698), + ±0.01·rot_i(2,−1,−1), i=0,1,2. ids bac2,3777,7d37,fb7f,1171,8acf (L1 r0m,r0p,r1m,r1p,r2m,r2p), 9a93,8e7f,5a85,82a2,a5d1,43e6 (L2 same order).
- Charged so far: 20.

## ~12:40 — wakeup 4
- Replicas: _9784 = 1.1595 (matches c ce1f exactly; promoted), _6dc8 = 0.8114 (matches c −30 bp). Orientation confirmed.
- Pure in-orbit E, d30 β, norm 0.037: E1− 0.9968, E1+ 0.9942, E2− 0.9960. Compared with ad's norm 0.09 (0.9877/0.9540): loss ×3.8/×7.9 for a ×2.45 step → smooth ε²+ε³, NO cusp. My cusp prediction is refuted/not supported.
- ad: k-nematic (full S1 × w·Q_T1) gains +5% both signs at the parent (s21), +4% r46. Gain comes from cross terms between E copies.
- Submitted N3: leader + knem β±0.09 (pair-entry form, verified = ad's block to 1e-16): L1 r0 −/+ b35a/9d49; L2 r0 −/+ d257/73a6; L2 r1+, r2+ 6f20/fd11. Charged: 26.
- Board: STRONG claims by c (d698), f (S3×T1 chiral-odd β 0.05: 1.558/1.641/1.560), j (⊥α −0.45: 1.64/2.63/2.45). h: S4T1 α orbit 1.57/1.72/1.61.

## ~13:10 — wakeup 5
- N1 done: E2+ 0.9951, single entry −0.09 0.8070, +0.09 1.1172 (promoted; = al's ded4). Posted interim note _4467: no cusp (smooth ε²+ε³), prediction not supported.
- Board moved: records R≈4.8 s21 / 5.2 r46 (h c662 STRONG claim; t 8c01). They follow an angular rule: α ∝ cos2δ, β ∝ sin2δ on S1/S2×T1 (av). c's note: leaders lift R_beyondM2 from 0.12 to ≈0.72, i.e. back to the smooth-static M2 law. g/p debate on d_sc: p is right that the contact term is inert for a scalar band, so both gaps are q² (d³) and there is no 1/d² amplifier.
- al stage 2 covers nematic strain at the records. ad covers k-nematic orientations. So I won't add E at the records.
- Plan: wait for N2 (12) + N3 (6), then post the result plus coverage and close nematic. Queue latency is ~1h; stay frugal and don't congest it. Then pick a verifier role if one is needed.

## ~13:41 — wakeup 6
- N2/N3 (18) all still pending ~90 min; several agents report stuck s21 lanes. Posted operations request _baf4. Not submitting more.
- 8a74 (single entry +0.09): s21 1.1172, r46 1.0336, against leader 1.1595/1.1586. The single-entry loss is 3× larger on r46 (C2 orientation), consistent with al.
- Board: g retracted the 1/d² amplifier. More STRONG claims: t 8c01, v S7T1 α, s noQ0 (phase-only 1.73/2.32/2.14). f: phase-only s21 ceiling ≈1.72. ap lllref: records need γ×ρ* cooperation.

## ~14:12 — wakeup 7
- Lane cleared. s21 results:
  - L1 (ce1f 1.1595) + 0.01·rot_i E1: − 1.1564, + 1.1554, identical for i=0,1,2 (C6 check on s21 passes). Loss 0.3–0.4 %.
  - L2 (d698 1.2494) + 0.01·rot_i E1: − 1.2255, + 1.2129, identical over i. Loss 1.9–2.9 %.
  - knem β ±0.09: L1 − 1.1979 (+3.3 %), + 1.1653 (+0.5 %); L2 − 1.2338 (−1.2 %), + 1.2005 (−3.9 %, r0=r1=r2).
  - So knem is not additive: +5 % at the parent, sign-selective at L1, negative at L2.
- All 18 promoted to r46 → orientation-resolved r46/r56 pending (free).
- Board: records now f5f1 (o) 6.28/8.33/8.12, on the Σ|β| cap. al: records are saddles vs r-nematic strain at s21 (+4.2 %).
- Next: wait for r46/r56, then post the final nematic result + coverage.

## ~14:45 — wakeup 8
- r46 for N2/N3 landed (r56 pending):
  - L1 (r46 1.1586) + E rot r0/r1/r2, −/+: 1.1890/1.1212, 1.1450/1.1609, 1.1314/1.1776. Linear orientation term ±3 %; it sums to ≈0 over rotations. Mean of the six is 1.1542 (−0.4 %, same as s21).
  - L2 (r46 1.4041) + E: 1.2926/1.2948, 1.3112/1.3792, 1.2889/1.2741. Mean 1.3068 (−6.9 % even loss; s21 −2.4 %).
  - knem: L1 r0 −/+ 1.2099/1.1808 (+4.4/+1.9 %). L2 r0 −/+ 1.4664/1.4166; L2 r1+/r2+ 1.2957/1.4819, orientation mean for + is 1.398 (−0.4 %).
  - Best min-over-clusters nematic gain so far: L1 + knem β−0.09 (b35a), +3.3 % s21 / +4.4 % r46.
- Board: records R≈10 (av e0a8 STRONG 10.39/9.87/10.50, cap-limited). Nematic effects are a few % at most, so they're irrelevant for the record race.
- Next: when r56 lands, post the final result + coverage and close `nematic`.

## ~16:47 — wakeup 9
- Posted the final nematic result + coverage, `_2067` (s21 + r46 complete, r56 pending).
- ad batches 2–3: the pure S3 k-nematic α −0.60 reaches s21 4.01 (EG ≈1.0, M2 +14 %), with an r46 orientation spread of 5–10 %. ad covers it carefully.
- Considered record + S3 k-nematic: low expected value (al says records lose under k-strain, and my L2 result is negative). It would also need the record blocks from other agents. Skipped.
- Plan: append r56 as a short note when it lands, then `swarm done`. Charged 26/500.

## ~17:30 — wakeup 10
- r56 still pending for all 20 promoted requests (5×6 lane slow). al closed lowsym (no robust E2 gain, consistent with mine). Waiting one more cycle, then swarm done regardless (r56 lands in the store anyway).

## ~18:20 — wakeup 11: done
- r56 still pending for all 20 promoted requests; they'll land in the store anyway.
- Ran `swarm done` with the final summary. 26/500 charged. Family `nematic` closed (result _2067).
