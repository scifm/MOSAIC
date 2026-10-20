# swarm-ao notebook

Started 2026-10-14T10:26:15+00:00.

## 2026-10-14 ~11:36 — wakeup 1
- Read board: ~45 agents, heavy herding on S1–S3×T1 joint orbits (CMA z/n/ag/am, surrogates h/o/t, lines j/q/r/ae/s, nematic ad/al/ah).
- Leaders (swarm-c jorb): S2×T1 +60 β+0.03 → 1.249 s21; S1×T1 ⊥ α−0.05 → 1.17 (r46 1.170); +30 β+ 1.16 (r46 1.159). s21≈r46 within <1%.
- swarm-e: full stars break the manifold at |α|~0.1–0.2, |β|~0.12. Steps of 0.05/0.03 per entry are the right scale.
- My orbit generator: work/orbits.py (matches c's pair matchings). Template: work/w1c_template.json.
- Posted hypothesis kprof (…_8b15): S2×T3 and S3×T2 joint orbits, α±0.05 / β±0.03 per entry; 24 evals submitted (work/b1).
- Mailed ae re overlap on S2 T2/T3 β profile.
- Next: read results; if S2×T3 live, stage 2 = T1+T3 profile mixtures within one orbit (λ ∈ ±0.25, ±0.5). Later: audit role (neighbourhood robustness of leaders, curvature across clusters = c's thin spot 1).

## 11:53 — wakeup 2
- 15/24 charged so far, none finished. Leaderboard top now 1.64 (⊥ α line, j/q/r same hash) ; f chiral-odd S1×T1 β 5098 = 1.38 s21, cleanest (u audit).
- d698 (S2×T1 +60 β) r46 = 1.404 > s21 1.249; S2 leaders use 30–50% of s21 splitting gate (u audit).
- kprof heavily duplicated by av (same name!), aj, ar, i, e(orbmap2), au(harmladder). ae ceded T1+T3 β to me, but au's c12 is the same object → handed to au; DROPPED stage 2. Mailed au, ae.
- conv46 ≈ r46 to 5e-8 for pure LL0 (l's request) — claims rest on s21, r46, r56.
- Plan: post stage-1 table + coverage when results land; then find an unherded role (p holes: inner+outer combos — taken by at/an/aq; large-amp non-⊥ α — s/x/aj). Consider critique posts.

## 12:13 — wakeup 3
- My 24 still pending (queue heavy). e has S3×T2 ∥0/+60 at smaller step (α±0.03, β±0.02) → my S3×T2 is a different-step duplicate; S2×T3 is mine (e mail). au accepted T1+T3 β.
- Board: STRONG claims exist: ⊥ α −0.45 (j ea28 / q c027): s21 1.64, r46 2.63, r56 2.44, conv46 2.63. c's phase-only S2×T1 +60 β 0.03 STRONG 1.249/1.404/1.347. f e5d5 STRONG 1.56/1.64/1.56.
- s21 is the binding cluster (its manifold splitting grows 8–30× faster than r46's). k: density controls lower the gap → gain not density.
- Next: post stage-1 table when done; look for critique target.

## 12:39 — wakeup 4
- All 24 of mine still pending (submitted 11:36). Board s21 record now 4.82 (t 8c01) / 4.76 (h c662): α+β multi-orbit combos, strongly superadditive. Verifiers: as (robust width), i (density controls), p (PES N_A=3), g (gauge covariance request), u/k (mechanism: not interaction scale, not density).
- Nothing unique to add right now; waiting for my map, then post coverage.

## 13:10 — wakeup 5
- First 7 results (S2×T3): ∥0 α− 0.936P, α+ 0.705F, β− 0.732F, β+ 0.551F; +60 α− 0.677F, α+ 0.946P, β− 0.853P. T3 copy of the top S2×T1 block is destructive for every sign (agrees with av: T3 opposite sign; y: damage tracks |R|).
- Queue throughput is the swarm bottleneck (o: 80-min waits). Keep my eval use small and targeted.
- Board: records c662/8c01 STRONG ~4.8–5.2 (α+β multi-orbit, cos2δ α + sin2δ β angular rule on S1/S2×T1). g vs p on d_sc amplification: p right (contact term inert for spinless single band).

## 13:42 — wakeup 6
- kprof stage 1: 22/24 in. S2×T3 destructive in all 12; S3×T2 best ∥0 α+ 1.034 (a50a → r46). s21 MT-partner mismatch ~10% for T2/T3 vs ≤1% T1. Posted result+coverage …_3133.
- New: mtrec — MT images (work/mt_image.py, validated d698→dbab) of the records 8c01 (→5fde) and c662 (→d864). Posted note. Expect ≈ equal; >5% lower on r46/r56 ⇒ chirality artefact in claim.
- Board: many STRONG claims (records 4.8/5.2/4.6; phase-only noQ0 1.73/2.32/2.14; outer S7×T1 α 1.56/1.93/1.79). Density excluded (k, i). g retracted 1/d² critique. Queue stuck lanes reported (o, j, m).

## 14:13 — wakeup 7
- a50a (S3×T2 ∥ α+): s21 1.034 → r46 0.775 — sign flip. 5184 0.577F vs MT partner c265 0.720 (20% mismatch). Posted addendum …_cb74, kprof CLOSED with final coverage. Mailed b (supports their refutation 3b65 of ab's T2/T3 lift, which cites my ~10% artefact).
- mtrec: added MT image of record f5f1 (o; r46 8.33; carries T2/T3) → req 2d3f. Pending: 5fde (8c01 img), d864 (c662 img), 2d3f (f5f1 img).
- Board: av cos2δ+i·sin2δ rule on S1–S3×T1 → s21 10.39 (Σ|α| cap). Many agents finishing (ak, p, g, q, aj done).

## 14:44 — wakeup 8
- mtrec s21: 8c01 image 5fde 4.7992 vs 4.8159 (−0.35%); c662 image d864 4.7578 vs 4.7599 (−0.04%). Records not chirality-driven at s21. Waiting for r46/r56 of the images (free promotion) and f5f1 image 2d3f.
- New #1 e0a8 (av, cos2δ+i·sin2δ rule) is MT-self-dual (cos2δ even, sin2δ odd with β flip) → image = itself; no test needed.
- After mtrec lands: post result, then likely `swarm done` (board saturated; queue is the bottleneck).

## 16:49 — wakeup 9
- mtrec: images vs records — 8c01: s21 4.7992/4.8159, r46 5.1880/5.1860; c662: 4.7578/4.7599, 5.2293/5.2257; f5f1: 6.2753/6.2767, 8.3274/8.3254. ≤0.35% s21, ≤0.07% r46. r56 pending (orig r56: 4.5509, 4.6741, 8.1173).
- Board: records now ~12–14 at s21 (h 5063 STRONG 11.65/12.30/11.97; w 407a 13.9 qmax not converged); y/an/u: above R≈9–12 conv46 shifts and r46 gate start to bind.
- Plan: once r56 lands, post mtrec result + coverage, then `swarm done`.

## 17:20 — wakeup 10
- mtrec r56 still queued. Will post next wakeup regardless, then swarm done.

## 17:51 — wakeup 11 (final)
- Posted mtrec result …_a02c (images = records ≤0.35% s21, ≤0.07% r46; r56 pending). Ran swarm done. 27/500 charged.
