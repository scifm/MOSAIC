# swarm-j notebook

Started 2026-10-02T03:51:42+00:00.

## 2026-10-02 04:15 — wakeup 1
- Read board: a (w3 sep atlas), c (w3 CMA wide), b/e/f (w2 sep atlas — triple herd), g/h (w3 joint-orbit cos·cos modes S1-S3×T1-T2), d (w3 chiral β rest), i (MT parity note).
- Derived MT selection rule independently: β on separable/achiral orbits is MT-odd (no bulk linear slope); chiral β (θ vs 180-θ orbit) is MT-even -> linear slope allowed, beyond-M2 by construction. Clusters s21/r46/r56 are all chiral, so MT-odd slopes can appear as finite-size artefacts.
- MISTAKE: posted hypothesis chiral-orbit (w3) before reading g/h/d/i -> withdrew it (note ..._70d5), submitted none of it.
- Now family `w2-chiral`: 6 chiral-β directions on w2, unit-Frobenius ±0.03 (b=0.03/√6 per pair combo). 12 req submitted (ids ..._d00b .. _6aca). Sign: +b on θ<90 orbit.
- Posted request ..._c1b1: odd-odd sin·sin sector unrepresentable (contains k-dependent envelope displacement); asked human whether to extend the block.
- Tools: work/chiral.py (orbits, block builder), work/make_batch.py PARENT OUTDIR SPEC.json, spec format [[|G|², |R|², orbit_idx, alpha, beta],...].
- Next: when results land, fit slope g and curvature per direction (R(±)=1±g h - c h²), compare to h/g/d w3 β-C. Line search along the chiral-β gradient on w2 (box ≤0.15 Frobenius). Possible later role: g_cutoff convergence check of top candidates (conv rung keeps g_cutoff=6!).

## 04:33 — wakeup 2
- Broker was slow (fixed by human). conv46 now uses g_cutoff max(req,10) (human fix).
- Board: 18 agents; heavy herding on chiral β (d, g, h, i, k, l). d's chiral β S4T1c2 (+0.03) is at s21 R=1.0364 PASS (req ..._2400) and on its way to confirm21.
- Aliasing notes (o, r, p, m): only T1, T2 are clean on every ladder mesh; on s21 T2≡T5≡T6 and T4 = ½T3; T3 self-aliases on r46. My directions use T1/T2 only, so they're safe.
- i's w2 phase 1 overlaps my S1T1/S2T1/S3T1. Mailed i.
- My 12 still pending.

## 04:55 — wakeup 3
- My w2 phase 1 (12 PASS), slope/unit and even part: S1T1 −0.66; S3T1 **+1.60** (R(+.03)=1.0185, d4dc); T2 all dead. Posted result ..._e54d.
- Board: w3 leader o/968b, s21 1.609 / r46 1.710, = α S1T1-⟂ + α S2T1-∥ + chiral β S4T1/S7T1 (g10). Amplitude gradient is on the ⟂ orbit (h, k, g). Chiral β is live only on T1 (d C4T1 +1.32, i |G|²=13, l w2 C4 +3.7, C7 +3.3).
- b's critique: the G⟂R orbit pairs G with ẑ×G l² (S1↔T1), so half of the orbit is k-independent cyclotron e^{iGη}, i.e. static coherent LL mixing. VERIFIED the geometry; it matches the 968b rows. Posted note ..._ff87; the k-dependent half lives on T3 (2R0).
- Submitted: w2 S3T1 line search (b=0.015, 0.02, 0.025: 2368, e0d3, 7983) and ray (S3T1, S1T1) at 0.02/0.03 (2261, c08d), g10.
- Submitted cyclotron-test: α S1T3-⟂ ±0.03 (no static half), w3 (7b75 +, c112 −), w2 (4ce9 +, f1b9 −). Compare to k's S1T1-⟂ slope +2.79 on w3.
- Next: read results; post the cyclotron-test outcome; add to the c1b1 thread that odd-odd splits the ⟂ orbit into static and k-dependent halves.

## 05:19 — wakeup 4
- w2 S3T1 chiral-β line: b = 0.015/0.02/0.025/0.03 → 1.0133/1.0159/1.0177/1.0185 (vertex ≳ 0.03). Ray (S3T1, −S1T1): 0.02 → 1.0190; 0.03 (c08d) → s21 1.0238, r46 1.0764, r56 pending. r's w2-synth owns combined chiral-β on w2 (s21 1.137 leader 509c).
- Cyclotron test S1T3-⟂: flat (w3 +0.045, w2 +0.10 per unit). CONFOUNDED by the generic T1-only amplitude pattern (a ebe4); withdrew it as evidence. q: the C6 static half only feeds LL0 + LL6 (amp 0.03); S2T1∥ (no static half) has an equal slope. b's concern is now mostly answered. Posted result ..._91e4.
- w3 leader is p cc86 (s21 2.40, r46 2.47; M2_k 6.20 vs 3.63; R_beyondM2 0.97 vs parent 0.69). Large-amplitude, density-driven in part.
- Pattern: MT-even gains are 2–5× larger on r46 than s21. Submitted MT-odd controls (family mt-floor, --control --clusters s21,r46,r56): w2 β-U S1T1, β-U S2T1, α-chiral C4T1; w3 β-U S1T1, α-chiral C4T1; ±0.03, g10 (ids 4aa7, 86ee, 35f0, efb0, d541, e280, 901e, 9826, 9c30, ebf9). Goal: the artefact floor per cluster.
- Spent ~21 charged + 30 control evaluations.

## 05:46 — wakeup 5
- mt-floor controls at s21 and r46: MT-odd slopes ≤0.04 (s21), ≤0.003 (r46), so chiral/α slopes are real. NEW: the r46 even part is positive (+0.4..0.9%) where s21 is negative (−0.3..−1.5%): a generic r46 convex bias (supports q abc0). Posted note ..._d608; mailed q. r56 legs pending, and they decide.
- Board: w3 top o b7cb s21 2.74; o bd1a r56 2.567 (on conv46!). e: the leaders' β patterns lose at α=0 on w3 (β gain is α×β interplay). w2 top g 7f3e s21 1.21 / r46 1.37 (α S3T1⟂-type + ?). i's selection rule: T1 slopes only where parent harmonic a_{G+Gp} = −R gives k-independent content.
- My c08d (w2 ray) waiting on r56.

## 06:12 — wakeup 6
- Claims: p cc86 STRONG (2.40/2.47/2.46/2.47), o bd1a STRONG (2.27/2.63/2.57/2.63), both provisional on the Q=0 / static-content ruling. d 2400 robust_positive phase-only (1.036/1.080/1.056/1.076); q critiqued it already (r56 margin marginal: r56 keeps ~half the r46 excess). c: PES ent-gap falls 21 → ~5 on amplitude leaders. So I'm not duplicating a critique of c0eb.
- My r56 control legs are still pending (low queue priority: R_gap_min < 1). They will give the pure generic even-order excess on r56 for zero-slope directions, which is the baseline for q's split.
- No new submissions: the swarm is saturated on every live direction; I'm keeping budget for verification.

## 06:43 — wakeup 7
- f 48a8: the parents' r46 gap is 4.1% low on both parents, so r46 R_gaps carry a denominator boost; q corrected to own-gap ratio r46/s21 − 1 = 4.8·ΔT with zero intercept. My r46 positive even-part on zero-slope controls fits this: a deformation lifts the anomalously low r46 gap.
- c claims 776c STRONG, amplitude-only S2T1∥ (1.518/1.409/1.499/1.409). p static-free null: Q_tot-free orbits lose (best 0.746), which supports i's rule that the live T1 slopes need k-independent kernel content.
- My r56 controls and c08d are still queued. Plan: when r56 lands, post the final mt-floor result + coverage, then `swarm done` (no unique direction left; swarm saturated). Odd-odd request c1b1 is unanswered: record it as a coverage gap in the summary.

## 07:25 — wakeup 8
- c08d (w2 phase-only ray S3T1/S1T1 at 0.03): s21 1.0238 / r46 1.0764 / r56 1.0498. Misses the converge gate (needs ≥1.05 on r46/r56) by 0.0002, so it's "suggestive" only. Superseded by the stronger w2 phase-only claims r e064 and l 9fcb.
- r56 controls (5 of 10 in): w2 aC4T1 odd +0.02 / even −0.0011; w2 bU S1T1 odd +0.022 / even −0.0032. So the r56 even part sits between s21 (−0.3..−1.5%) and r46 (+0.4..+0.9%): r46 is the outlier, consistent with f's low-parent-gap-on-4×6 finding. Waiting for the last 5.
- Claims now: w3 cc86, bd1a, 776c, d49b (h, small α S2T1∥ 1.128/1.120/1.112/1.120); w2 e064 (r, phase-only), 9fcb (l, phase-only), 98ec/29a2 (g); d 2400 robust_positive.

## 07:56 — wakeup 9 (final)
- All r56 control legs in. r56 even part mean −0.4% (r46 +0.4%, s21 −1%). Posted final mt-floor result c910, w2-chiral closing result d6f1. Mailed d.
- `swarm done` posted. 51/500 charged. Loop stopped.
