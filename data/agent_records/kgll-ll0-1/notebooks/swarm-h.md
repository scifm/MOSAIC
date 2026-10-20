# swarm-h notebook

Started 2026-10-02T03:51:32+00:00.

## Wakeup 1 — 2026-10-02 ~04:05 UTC
- Board: a = w3-atlas (U star directions S1-S8×T1-T3, ±0.02), c = w3-wide (CMA-ES S1-S4×T1-T2),
  e = w2-map. Parents s21: w3 Δ 4.5716e-4, w2 Δ 3.2271e-4.
- Block facts: γ = Σ (α/2 + iβ) O_s(r) F_p(k), stars must be inversion-symmetric → γ even in r AND in k
  separately (no sin·sin). Pair stars {±G} are legal → orientation-resolved couplings are representable.
- My family **w3-orient** (hypothesis 20261002T040737.360Z_swarm-h_hypothesis_422d):
  per (S,T) 3×3 α_ab on pair stars; C3 classes by angle(G_a,R_b); modes U (= star product, a's),
  A (⟂/∥ vs oblique contrast, mirror-even), B (chiral, mirror-odd). Verified C3/C2 exact, U ≡ star product.
- Tools: work/orient.py (modes, block), work/mk.py OUTDIR parent name=S:T:mode:a|b:coef,... ,
  work/check_orient.py (symmetry checks). Templates work/w{2,3}_template.json.
- Phase 1: work/p1/ 48 inputs, A/B × {a,b} × ±0.03 on S1-S3 × T1-T2.
- Submitted 32 (S1,S2 × T1,T2) → ids in work/p1_ids.txt. S3 batch (16) waits in work/p1b/ (in-flight cap 32).
- Next: when results land, tabulate slopes (R+ − R−)/0.06 and curvature; B± asymmetry = Nk=21 chirality.
  Then submit work/p1b. Read swarm-a's U slopes to combine.

## Wakeup 2 — 04:33 UTC
- Phase 1 results (32, all PASS): A-α S1T1 slope +1.51 (R 1.0283 @+0.03), S2T1 +1.36; T2 tiny; B-β tiny;
  MT-odd artifact floor ≤0.18/unit. Posted result 20261002T043500.499Z_swarm-h_result_4e3f.
- CORRECTION accepted: symmetry is M·T, so B-β slope allowed, B-α forbidden; U/A-β forbidden. No ladder cluster has a mirror.
- Board: swarm-k = same family (joint-orbit), best 1.0413 = pure ⟂ orbit S1T1 0.02/entry. g pivoted to w2-orient.
  d's S4T1 chiral β 0.0122 → 1.0364 (phase-only!). c CMA best 1.0386.
- Gradient in orbit coords: S1T1 c0 (⟂ orbit) ≈1.86/unit, others ≈0 → whole amplitude gradient on one orbit.
- orient.py: modes O0/O1/O2 = pure orbits (unit Frobenius); default g_cutoff now 10.
- Phase 2a submitted (16): L11_t, L21_t line scans t=0.03..0.11, combos C_x_y (S1T1 c0, S2T1 c0). ids work/p2a_ids.txt
- Dropped p1b (S3) — k covers S3T1. Mailed k a split: I take α-orbit, k takes β_chiral.
- Next: fit 1-D maxima, then CMA-ES in α-orbit subspace (S1-S3×T1 c0,c+,c−; maybe S4 halves) ; watch promotions of c581/4605.

## Wakeup 3 — 04:56 UTC
- Phase 2a: pure-orbit lines LINEAR & unsaturated. L11 (S1T1⟂) t=0.11 6e88 s21 1.135 r46 1.113; L21 (S2T1∥) 0.11 d49b
  s21 1.128 r46 1.120; combo 7b23 r46 1.111. All PASS, at r56 stage.
- Board leaders: o 968b s21 1.61 r46 1.71 (mixed α + chiral β); c 776c pure S2T1∥ t=0.45 s21 1.518 r46 1.409 (M2_k 5.3).
- CRITIQUE (b e1e5, p f9b6): S1T1⟂ orbit is half static LL mixing (Q=a_G+R=0). S2T1∥ is clean. Accepted; my 6e88/7b23 tainted.
- k agreed split: I do S1-S3 α orbits + matched-density control; k does S4-S8 α orbits.
- Verified kernels converged (work/trunc.py): 776c box loss 1.8e-10, 968b 5.8e-7; mesh alias 1e-16. Posted note 1018.
- Phase 2b submitted: 12 probes ±0.05 at 776c base (S2T1:O0:0.45, GCUT=12) dirs S3T1 O0/Os, S2T1 Os, S1T1 Os,
  S1T2 O0, S3T2 O0. ids work/p2b_ids.txt. Mode Os=(P1+P2)/√2 added. mk.py honours GCUT env.
- Next: compute gradient at 776c, post; step along it (LL-free) if positive components; watch r56 of L21/d49b.

## Wakeup 4 — 05:20 UTC
- Board: LL-free recipe S2T1∥ α + chiral β (S4T1/S7T1) leads: p cc86 s21 2.399 r46 2.470; o 48bf s21 2.62 (M2k 7.86).
  α-only S2T1∥ peaks t≈0.45 (c). r56 bottleneck (2 GPU lanes) — no w3 r56 yet. Converge gate now r46/r56 only.
  n controls: 6e88 static-density explains ≤1.9% of 13.5%; 968b M2-matched static 1.077 vs 1.609.
- Phase 2b (gradient at 776c): S1T2∥ live, slope −0.46 s21/−0.38 r46 (c3a9 −0.05: 1.534/1.421), LL-free (|Q|²=4).
  Oblique-even slopes only on s21 (r46 exactly symmetric). S3 flat. Posted 20261002T052321.750Z_swarm-h_result_7f99.
- qmax check (work/qtrunc.py): |G|²-weighted kernel outside qmax-8 hexagon: 48bf 1e-2, cc86 2.4e-3, 776c 1.2e-4.
- Phase 2c submitted (6): S1T2∥ at cc86 −0.05/−0.10/−0.15/+0.05; at 776c −0.10/−0.15. ids work/p2c_ids.txt.
  Tool work/addto.py BASE OUT parent name=terms merges orbit terms into any existing block (verified 1e-16).
- Budget used 66/500.

## Wakeup 5 — 05:44 UTC
- r56 arriving: cc86 r56 2.456, bd1a (o) r56 2.567 → LL-free recipe survives 5×6. c581/4605 r56 1.027/1.026.
- Phase 2c: S1T2∥ on cc86: −0.05 → e9f5 s21 2.426 r46 2.526 (M2k drops 6.20→5.99); slope −1.45/unit; opt −0.04..−0.12.
- work/q0.py: Q=0 (static LL mixing) fraction, criterion R = −a_G, a_G=(−n,m). Top 15 all 0 except k 13f5 0.05, 56b7 0.03.
- Phase 2d submitted (6): S1T2∥ −0.05/−0.08 on o's b7cb, 3eea, 48bf (ids work/p2d_ids.txt).
- Withdrew 33 non-candidates (swarm withdraw). Kept e9f5, fd37, d49b.
- New broker tools: --diagnostic (probes, never promoted), --control --clusters, withdraw. USE --diagnostic for future probes.
- Next: if S1T2∥ helps o's leaders, it's a general add-on; then a coverage post for my S1–S3 α-orbit scope.

## Wakeup 6 — 06:07 UTC
- Claims on board: p cc86 STRONG (prov.), o bd1a STRONG (prov.), d 2400 robust_positive phase-only (marginal per q).
  e: chiral β alone (α=0) LOSES on w3 → α×β interplay. c: PES eg falls 21→~5 on amplitude leaders.
- Phase 2d: S1T2∥ −0.05 lifts all of o's leaders: fea3 (b7cb+) s21 2.800 r46 3.589; ecfd 2.692/3.110; 3dc8 2.734/3.018;
  also raises PES eg +0.1..0.3, lowers M2k. Posted result+COVERAGE 20261002T061007.996Z_swarm-h_result_f661 (72 evals w3).
- work/proj.py: project any request onto S1–S3×T1–T2 orbit coords. w2 leader g/e214 = α S1T1 Os(−0.276) + S3T1⟂ 0.12 + chiral β 7,13.
- Submitted 12 --diagnostic probes at e214 (family w2-orient-grad, parent w2), ids work/p3w2_ids.txt. Mailed g and o.
- Budget charged 72 (+12 diag pending) of 500.
- Next: read w2 gradient; if a live LL-free direction appears, coordinate with g before line search. Consider verifier role.

## Wakeup 7 — 06:31 UTC
- w2 diagnostics at g/e214 (s21 1.2484): S1T2∥ slope −2.20 (c178 −0.05 → s21 1.333, best w2 s21 on board), S2T1Os −1.30,
  S2T1∥ +1.04, S3T2∥ +0.80, S1T2Os −0.70, S3T1Os +0.35. Posted 20261002T063135.734Z_swarm-h_result_34a4.
  S1T2∥ is the first direction live with SAME sign on both parents.
- Mailed g proposal (7 ladder requests); promised to submit at next wakeup unless g objects. Prebuilt in work/p3w2b/
  (e214_full_t0.07/0.12 = 6-D gradient; e214_c0_t0.07/0.12 = c0-orbits only; e214_S1T2m08/m12; 0f4e_S1T2m06). All checked.
- Board: p cc86 8/8 STRONG grid; f: parents' r46 gap 4.1% low → r46 R_gap +4.3% inflated, r56 binding.
  n: fea3/b7cb M2-matched static 1.49–1.57 vs 2.74–3.59. p starting w3-sobol incl. S1T2∥.

## Wakeup 8 — 06:53 UTC
- d49b (S2T1∥ t=0.11, LL-free, α only) completed the ladder: s21 1.128 r46 1.120 r56 1.112 conv46 1.120, broker STRONG.
  M2k 3.709 (+2.2%), static yardstick ~1.015 → mostly beyond-density. Posted CLAIM 20261002T065446.955Z_swarm-h_claim_1c56.
  Asked n for a matched-density static control on d49b.
- b proposed w2 lanes (b α classes, r/g β, k T2 β, h gradient diagnostics). Accepted; dropped prebuilt batch
  (work/p3w2b_dropped). b's f0fd (bb0d + S1T2∥ −0.04) s21 1.305 r46 1.474 confirms S1T2∥ on w2.
- c claimed 776c STRONG (r56 1.499). p w3-sobol found df8f s21 2.740 r46 3.458 off-path.
- Pending: r56 for fea3/e9f5/ecfd/3dc8 etc.

## Wakeup 9 — 07:21 UTC
- Claims now: w3 cc86, bd1a, 776c, d49b (mine), 2400 (phase-only robust); w2 e064 (phase-only), 9fcb, 98ec/29a2.
- k: fea3 + T2 β-chiral S4T2 → 435c s21 3.472 / r46 3.835; cd46 s21 3.817. p 9fc9 s21 3.514 (M2k 10.6).
- b asked for gradient diagnostics at w2 fb0c (s21 1.394): submitted 14 (--diagnostic), ids work/p3w2c_ids.txt
  (S2T1 O0/Os, S3T1 O0/Os, S3T2 O0, S2T2 Os, S1T1 Os; skipped b's in-flight dirs).
- qmax calibration: conv46−r46 ≤7e-4 for proxy ≤4.7e-3 (proxy overstates ≥10×). New top T2-β points proxy 4–5e-2.
  Posted note 20261002T072423.459Z_swarm-h_note_588a; mailed k, p.
- My w3 large points still waiting r56 (queue).

## Wakeup 10 — 07:45 UTC
- fb0c (w2) gradient: S1T1Os + (+0.041), S2T1∥ + (+0.037), S3T1Os − (+0.032), S3T1⟂ − (+0.031); others flat.
  Posted 20261002T074539.007Z_swarm-h_result_5532; mailed b (step c0 dirs first; Os likely s21-only).
- n submitted M2-matched control 2645 for d49b (s21/r46/r56).
- k 7966 = fea3 + S4T2 β 0.08: s21 3.727 r46 3.832 r56 3.785 (built on my fea3). o, m, c finished.
- Submitted 4 diagnostics at 7966: S2T1∥ ±0.05 (base t=0.70), S1T2∥ ±0.03 (base −0.05). ids work/p4_ids.txt.

## Wakeup 11 — 08:06 UTC
- n: d49b M2-matched static 1.015 vs 1.11–1.13 → ~87% beyond density (supports my claim 1c56).
- 7966 conv46 3.787 vs r46 3.832 (−1.2%!) — T2-β family not qmax-converged to <1%. Posted note (verify).
- 7966 re-tune diag (s21): S2T1∥ +0.05 → 4.007 (c08e), S1T2∥ +0.03 → 3.842 (a055); minus sides lower.
  Submitted ladder versions (free s21): a58e (S1T2 +0.03), 181c (S2T1 +0.05). Watch r46 split (gate 0.1).
- e audit: R>3 tier split/Δ 4–9%. Many agents finished (c, f, j, m, o).

## Wakeup 12 — 08:33 UTC
- Ladder tests on 7966: a58e (S1T2∥ +0.03) s21 3.842 r46 3.890; 181c (S2T1∥ +0.05) s21 4.007 r46 3.882; r46 sp/D 0.034, eg 4.63. r56 pending.
- k claimed 7966 STRONG (conv46 3.787). p claimed 9fc9/8bc7 (conv46 −2.8/−2.3%, sp/D 0.094 near gate).
- k on T2 α lane: 3d90 = 7966 + S7T2 α −0.10 → s21 3.903 r46 4.222. Submitted my T1 re-tune on 3d90 (builds-on):
  a965 (both), 125c (S1T2 +0.03), 864b (S2T1 +0.05). ids work/p5_ids.txt. Mailed k.
- Withdrew superseded fd37, 3dc8, b213, ecfd, 5524, 1975. Keep fea3, e9f5, a58e, 181c, new p5.
- Budget charged ~105.

## Wakeup 13 — 08:55 UTC
- On 3d90: a965 (both T1 moves) s21 4.336 r46 4.327 split 0.018; 125c 4.127/4.304; 864b 4.151/4.243. Posted result.
- k new base feba (fea3 + β S4T2 0.08 + α S7T2 −0.20): s21 4.120 r46 4.556 split 0.011, M2k 6.79.
- Submitted re-stack on feba (builds-on): f5b0 (both), 9ad3 (S1T2 +0.03), 9b77 (S2T1 +0.05). ids work/p6_ids.txt.
- Withdrew a58e, 181c, 125c, 864b. Active: fea3, e9f5, a965, p6.
- p, e finished. k refuted p's 9fc9 (near gate); p accepted.

## Wakeup 14 — 09:17 UTC
- feba re-stack: 9ad3 (S1T2 +0.03) s21 4.370 r46 4.626 BEST; 9b77 (S2T1 +0.05) 4.261/4.459; f5b0 (both) 4.239/4.457.
  → S2T1∥ push doesn't carry to feba; S1T2∥ toward 0 does.
- Withdrew a965, f5b0, 9b77. Active: fea3, e9f5, 9ad3, p7.
- p7 submitted: feba+S1T2 +0.05 (8421), +0.07 (d3d9); 459c+S1T2 +0.03 (edc0). Mailed k.
- d finished. k 459c (β S4T2 0.05 on feba-like) 4.111/4.603 split 0.005.

## Wakeup 15 — 09:39 UTC
- S1T2∥ bracket on feba: +0.03 (9ad3) 4.370/4.626 best; +0.05 4.349/4.589; +0.07 4.322/4.544; 459c+0.03 4.367/4.539.
  T1 lane converged. Withdrew 8421, d3d9, edc0. Posted result with recipe lineage.
- Active: fea3, e9f5, 9ad3 (all waiting r56). k re-tuning β on 9ad3.
- a, r finished. Plan: wait for r56 → claim 9ad3 / e9f5 / fea3 if they pass; then final coverage + swarm done.
- 10:20 quiet: r56 pending for 9ad3/fea3/e9f5; asked n for 9ad3 control (M2k 6.8879). k: recipe converged (686f +0.6%).
- 11:11: 9ad3 r56 4.375 PASS → converge stage. n control 24bb (M2 6.888, n=3 mixture; n=2 bracket 385c 1.498/1.520). fea3, e9f5 still r56-queued. Lane bugs fixed by human.
- 11:42: 9ad3 strong (r56 4.375, conv46 4.619, control 1.42–1.49), fea3 strong (r56 3.510, conv46 3.581). Posted claim. e9f5 r56 2.465, conv pending. k claimed 686f (min 4.395). n, k finished.
- 12:08: e9f5 done strong (s21 2.426 / r46 2.526 / r56 2.465 / conv46 2.525). g said yes → 16 diagnostics at w2 0356 (work/p8_ids.txt). b finished. After these: final coverage post + swarm done.
- 12:34: 0356 gradient: S2T1∥ + slope 2.46 (+0.089 s21); S1T2∥ − +0.03; obliques large but untrusted. g finished → I submitted 4 ladder steps (p9): dd68, 6425, 5e93, e4ee. Posted result.
- 13:01: w2 steps from 0356 all lift r46: e4ee (S2T1 +0.10, S1T2 −0.05) s21 1.970 r46 1.941, M2k ~unchanged (2.662). Withdrew dd68/6425/5e93. Widening: p10 S2T1 +0.15/+0.20 (S1T2 −0.05), +0.15 (S1T2 −0.08).
- 13:28: line still rising: 15c6 1.983/1.969, ac34 1.987/1.976, 53a7 (+0.20) 1.997/1.999 (s21 sp/D 0.047). Withdrew e4ee/15c6/ac34. p11: +0.30/+0.40 (S1T2 −0.05), +0.30 (S1T2 −0.08).
- 13:55: 53a7 done strong but r56 1.710 < 0356 1.789 → S2T1∥ on w2 hurts r56. cb28 +0.30 s21 1.951 (turning over), ebb8 +0.40 FAIL gate. Withdrew faa5. Re-activated e4ee as 2641 to test small step r56. Posted finite-size warning.

## Wakeup 20 — 14:37 UTC — FINISHING
- w2 line r56: 0356 1.789, +0.10 (2641) 1.755, +0.20 (53a7) 1.710, +0.30 (cb28) 1.688 → s21/r46-only direction.
- Posted final result + coverage for w3-orient (87 req) and w2-orient-grad (53 req): 20261002T143755.962Z_swarm-h_result_84c5.
- Claims: d49b (1c56), 9ad3 + fea3 (30a9); e9f5 strong (in final post). Budget charged 136/500.
- Ran swarm done.
