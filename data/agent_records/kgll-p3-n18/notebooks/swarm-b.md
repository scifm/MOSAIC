# swarm-b notebook

Started 2026-10-14T05:19:49+00:00.

## 2026-10-14 05:30 — wakeup 1
- Read brief, docs 40/46, theory §2–8, kdep_envelope, contract. Parent w1c s21 Δ = 2.2586e-4.
- swarm-a claimed `linmap` (product stars, 10 shells × T1–T3, α±0.1/β±0.05, 120 evals).
- I claimed `jorbit` (post 20261014T052701.977Z_swarm-b_hypothesis_a86f): joint (G,R) orbit classes via pair stars
  + permuted-diagonal α/β, c = a/√3 (unit rms). 3 classes per 6-member (S,T) pair, by signed axis angle mod 180.
  ±30°/±60° classes are mirror (chiral) partners — inequivalent because mirror flips C.
  Verified: sum of 3 classes = product block to 1e-16 (work/verify_joint.py). sin·sin half inexpressible in block.
- Tools: work/gen.py (product stars, chiral 12-shell halves '7a'/'7b'), work/joint.py (classes, block, build).
- Submitted J1a (31 reqs, work/j1a): S1T1, S3T1 (a±0.1, b±0.05), S1T3 a±0.1, plus sum3 check (=linmap α[S1,T1]=0.1).
- Queued for later: work/j1b (30): S4T1, S1T4 all, S1T3 phase.
- Next: when J1a lands, tabulate R per class, chiral asymmetry; submit j1b; compare sum3 with swarm-a.

## 2026-10-14 05:47 — wakeup 2
- Board crowded: c(jointorb S1-S3 P/M amplitude), i(comove G⊥R, s21 1.88 leader), k/m outer joint orbits, d chiphase
  (mirror-odd phase, other blocks), j phasequad, e/f/h large-α, a/l/q matched-density controls.
- swarm-d MT rule: R even in β on mirror-even dirs, even in α on mirror-odd; linear phase only via mirror-odd (A−B).
  All ladder clusters chiral (s21 C6 only; r46/r56 C2) → odd parts on product dirs = cluster artefact.
- J1a results (s21): see post 20261014T054708.749Z_swarm-b_result_6aa2. Best: |G|²3×T1 60° b+ 1.2525 (r46 1.389, phase-only!),
  120° b− 1.2444 (r46 1.388), 0° a+ 1.193 (r46 1.373), S1T1 90° a− 1.195. MT pairs agree ≤0.009.
- My labels S3 = |G|²=3 (swarm-c's S2). Note this when cross-referencing.
- Submitted J2 (12): u1=S1T1(30+,150−) and u2=|G|²3T1(60+,120−) phase line scans b∈{.025,.05,.1,.15}, u1±u2 at .05/.1.
- Submitted J1b (18): |G|²4×T1 all, S1×T3 phase. Held: work/j1c (S1×T4, 12).
- Mailed swarm-d: I keep mirror-odd phase in S1T1 + |G|²3T1; they keep other blocks.
- Next: J2 results → local 2-D search in (u1,u2), maybe add |G|²4 phase; watch r56 of af08/9a9a.

## 2026-10-14 06:10 — wakeup 3
- Board: product-star large steps all FAIL (a,e,f,h,j abandoned). Joint orbits dominate. Leader swarm-r ac14 s21 4.44/r46 4.93
  (α_even+β_odd combo, amplitude → needs control). trgrad (n) 2.7–2.9. Controls (a,q) for c5b8/f721 R_ctl 0.999.
- 73fe (S1T1 P a−0.1) finished ladder: s21 1.195, r46 1.197, r56 1.184, conv46 1.197 PASS → meets "strong".
- J2 (phase-only, beyond-M2 clean): u1 b .025/.05/.1/.15 → 1.17/1.33/1.60/1.72 (r46 2.10); u2 .025/.05 → 1.42/1.68,
  ≥0.1 FAIL manifold; u1+u2 @.05 → 1.7287 (r46 2.2785, req 69d3); u1−u2 bad. u3=|G|²4 30+/150−: 1.20 (r46 1.47).
- Pattern: β>0 on θ<90° class gains for all T1 mirror-odd blocks (incl. swarm-d S5T1 X, 2678 1.61/r46 2.22).
- swarm-d normalisation: X=(o−o')/√2 at β ↔ my u at b=β/√2.
- Posted J2 result 20261014T061025.371Z_swarm-b_result_45ae. Mailed d re cross steps.
- Submitted J3 (22): u1 to .3, u1×u2 grid, u3 line, u1+u3, u1+u2+u3, u1(+u2)+u5.
- Next: J3 → find best phase-only vector; consider local CMA in (u1,u2,u3,u5) + T2/T3 mirror-odd?; critique post due
  (candidate: check ac14 conditioning / MT partner / control).

## 2026-10-14 06:35 — wakeup 4
- LABEL WARNING: my mom keys are |R|²: '3' = T2, '4' = T3. So files "S1T3" = S1×T2, "S1T4" = S1×T3.
- Claims: ec27 (S1T1 30° β+0.05, phase-only) STRONG: 1.154/1.153/1.144/1.153; MT partner 8741 strong; 73fe (P a−0.1) strong.
  Posted claim 20261014T063208.341Z_swarm-b_claim_40b6.
- J3: phase-only s21 plateau ≈1.73 (split gate binds on s21 only; r46 split ≤0.011, r46 R up to 2.576 (3e85)).
  Posted note 20261014T063504.556Z_swarm-b_note_fda0 (critique-ish: s21 can't rank phase-only).
- Board leaders now amplitude+phase combos R ~ 10.9 s21 (swarm-r b55a, M2k 9.81 < parent). Parent soft: R_staticM2=0.137.
  statfront (c) / statctl (f) test the static frontier. swarm-p phasex combining phase-only levers across b/d/e.
- Submitted j1c (12): S1×T3 classes (completes declared J1 map).
- Tool: work/table.py prints all my requests with R/split per cluster.
- Next: r56 of phase-only frontier (69d3,0a35,3e85,d5c0,e4ac,9024,f506,c6d3,b857,18e0,81da); then coverage post for jorbit;
  consider a phase-only escape from s21 plateau, or switch role (verifier) if phasex covers it.

## 2026-10-14 07:05 — wakeup 5
- Posted jorbit coverage/closing result 20261014T070431.165Z_swarm-b_result_828c (95 evals, 65P/1A/29F s21).
- Board: swarm-e trap = non-Laughlin 3-fold state (EG<0.3) next to the phase-only sector; swarm-j: r46 is the high outlier,
  r56≈r46^0.94, min set by s21/r56. swarm-p PX1: phase-only splittings add coherently; PX2 will test T2/T3 phase levers
  on my capped points. ac14 claimed strong (4.43 min). ℓ=2 field (swarm-k) consistent with my class slopes
  (S1T1: A2≈1.9, A0≈−0.3; |G|²3T1: A2≈5.6, A0≈−0.5 from ±0.1 log slopes; phase sin2θ exact).
- Mailed swarm-p (S1×T2/T3 odd levers for PX2) and swarm-l (D1 control request for 73fe).
- Status: no new submissions; waiting for r56 of the phase-only frontier. Budget 95/500.
- Ideas if something opens: orthant/basin-uniqueness scan (sign patterns of α_P ×3, β_odd ×3 at ac14-like steps, 64 evals);
  only if nobody does it.
- 07:08 Posted hypothesis `orthant` (20261014T070744.940Z_swarm-b_hypothesis_a63c); submitted work/k1 (32): 2^(6-1) res VI,
  levers P1(S1T1 90 α−.1), P2(|G|²3 0 α+.1), P3(|G|²4 90 α−.1), u1(β.05), u2(β.025), u3(β.025); sign s=+1 good; I=ABCDEF.
  Analysis plan: fit log R = b0 + Σ b_i s_i + Σ b_ij s_i s_j (21 params from 32 pts); report gates per corner.

## 2026-10-14 07:37 — wakeup 6
- Orthant half-fraction (32) done (work/orth.py). PASS with R>1 only for P2+,P3+ corners with ≥2 good u's:
  ++++++ 3.90 (r46 4.21, 1113); -++-++ 2.54 (split 0.000!, r46 2.71); -+++-+ 2.28; -++++- 1.98.
  Any corner with P2 or P3 flipped: FAIL or R<1 (many R≈0, manifold destroyed). No second basin at these steps.
  Good corner 3.90 vs product of singles 5.56 → subadditive 0.70. log-R linear model meaningless across signs (rms resid 2.8).
- Submitted 8 complementary P2+P3+ corners (work/k2) → full 2^4 in (P1,u1,u2,u3) inside basin.
- swarm-l running D1 control for 73fe → ded6.
- Board: leaders now josobol c954 min 11.25 (strong), b55a strong 10.9-11.4; swarm-k chiral ℓ=2 field 3bd0 s21 13.6
  (truncation critique by swarm-i). Mechanism (swarm-a): restores weak V1 pair channel; e2 proxy R² 0.97.

## 2026-10-14 08:03 — wakeup 7
- orthant closed: posted 20261014T075936.110Z_swarm-b_result_16bc. In-basin 2^4 effects (log R): u3 .59, u2 .43, u1 .16, P1 .05;
  u1u2u3 −.27. 12P/28F. No 2nd basin.
- Board converged on swarm-k chiral ℓ=2 field E+ = λe^{+2iθ_GR} (θ = ang(R) − ang(G), α=2λcos2θ, β=λsin2θ). 3bd0 strong
  13.58/13.11/13.10/13.30, D1 1.007. E− breaks manifold. Mechanism: V1 pair channel e2 (a, g). Transfer to w3/w2 fails (q).
- New family `ellhi` (hyp 20261014T080217.639Z_swarm-b_hypothesis_a3dc): ℓ = −4, +4, 6 perturbations (μ=±0.002, φ∈{1,i}) on
  12-member shells at 3bd0 (block saved work/blk_3bd0.json; generator inline in this wakeup, files work/l4). 12 + replica ef13.
- Pending: r56 of phase-only frontier, 73fe D1 control (ded6 by swarm-l).
- Plan: after ellhi, likely wrap up (swarm done) unless something new opens; budget 135+13 used.

## 2026-10-14 08:27 — wakeup 8
- ellhi closed: posted 20261014T082445.090Z_swarm-b_result_7c55. ℓ≠2 on 12-member shells at 3bd0: −7.5..+2.8%, no lever.
  Best variants e215 (ℓ4 re μ−: 13.73/13.47), 4e60 (ℓ6 re μ−: 13.88/13.38). Replied to k's relabelling critique (agree).
- 73fe D1 control = 0.999 (swarm-l f075). 
- Withdrew 17 low-value pending r56 promotions (weak S1×T2/T3 points, 9 ellhi variants) to free the broker queue.
- Remaining: wait for r56 of phase-only frontier (0a35, 69d3, e4ac, 9024, 3e85, d5c0, 18e0, 81da, b857, c6d3, f506, ba6c, 4dea)
  and orthant 1113/abc0/858d; then post phase-only claim if strong, then `swarm done`.
- 08:57 ellhi variants done: 4e60 min 13.37 (13.88/13.38/13.37/13.56), e215 min 13.21, 0778 min 13.28 — all strong variants of 3bd0. Phase-only frontier r56 still SUBMITTED (queue). Many agents done.
- 09:25 still 47 at r56 (SUBMITTED; higher-R requests from others seem to go first). Waiting.
- 10:00 swarm done posted (work/done.md). Loop stopped.
