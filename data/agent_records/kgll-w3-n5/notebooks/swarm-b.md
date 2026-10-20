# swarm-b notebook

Started 2026-10-13T18:08:44+00:00.

## Wakeup 1 — 2026-10-13 18:10–18:20 UTC

Read: brief, doc 40 (024 pilot), doc 46, theory §6.4, ADR-0040, kdep_envelope/contract.
Facts: Δ_s21(w3)=4.5714e-4, Δ_s21(w2)=3.2271e-4. Block = separable star products O_s(r)F_p(k);
stars must be inversion-symmetric → γ even in r and in k separately (no sin·sin joint orbits).
Shells (120° basis): S1..S10 |G|²=1,3,4,7,9,12,13,16,19,21 (S4,S7,S9,S10 12-member, split into
chiral C6 halves S4a/S4b etc. in work/gen.py CUSTOM). T1..T3 |R|²=1,3,4 (dual 60° basis).
w3 lives on S3,S6,S8 (half-period density). w2 on S2,S5,S6.

Insight (posted note …swarm-b_note_ee04): M·T antiunitary symmetry ⇒ R(α,β)=R(α,−β) for whole-star
families on mirror-symmetric clusters/TL. work/cluster_sym.py: Nk21 has C6 only (chiral);
4×6, 5×6 have only C2. So β-odd response at all ladder clusters is a finite-size artefact.

Board: swarm-a = w3 single-term map (S1..S10×T1..T3, α/β ±0.05); swarm-d = w3 CMA 18-D
(S1-S3×T1-T3 α+β); swarm-c = w3 joint orientation channels. → I took **w2** (hypothesis
…swarm-b_hypothesis_1650), mailed swarm-d to split.

Submitted:
- family `symmetry` (w3): β=±0.03 pairs on S1T1, S3T1, S2T2 + chiral S4aT1, S4bT1 (10). Test
  predictions: whole-star R(+β)≈R(−β) up to Nk21 chirality; R(S4a,+β)≈R(S4b,−β).
- family `w2-map-cma`: α=±0.03 on S1..S10×T1 (20), ids in work/w2map1/ids.txt.

Tools: work/gen.py (make inputs), work/cma_loop.py (resumable CMA-ES; needs work/swarm_results.py
r_s21(req) — write once a result format is visible).
Next: read results; post symmetry test outcome; w2 T2 map (S1..S3, 6 evals); then w2 α CMA.

## Wakeup 2 — 18:35–18:40 UTC

Results: symmetry test confirmed M·T rule (posted result …swarm-b_result_1e7b). Whole-star β odd ≤0.3%;
S4a/S4b chiral halves ±2% odd, mirror-paired to 0.3%.
w2 whole-star α ±0.03 × T1 map: S1 −α good (1.0126), S3 +α (1.0137), S4 +α (1.0085), S7 −α (1.0127),
S8 −α (1.0122), S9 +α (1.0056). Best 1.0137. (ids work/w2map1/ids.txt)
Board: swarm-c ROBUST_POSITIVE on w3 with orientation channels: S2×T1 0° α c=0.08 (68f6: s21 1.092,
r46 1.084, r56 1.082, conv46 1.084) and S1×T1 90° (3182: r56 1.085). Whole stars dilute channels.
swarm-d abandoned w3-cma18 → w2-orient (S1–S3×T1–T3 channels). swarm-e w3-orient chiral classes.
swarm-a: α S1T1 whole star monotone to 0.08 (r56 1.037).
Decision: new family `w3-hichan` (hyp …swarm-b_hypothesis_978a): outer shells S4..S10×T1 channels,
mirror-symmetric combos (θ+180−θ), α ±0.05. 30 submitted (work/w3hi1/ids.txt); S10 (6) in w3hi1_S10/.
Tools: work/channels.py (channels(), mirror_combos(), write(parent, [(orbits, a, b)], out)),
work/swarm_results.py r_s21(req).
Next: read w3hi1, submit S10, line-search best, combine with S1-90/S2-0 leads.

## Wakeup 3 — 18:52–18:57 UTC

w3-hichan probes (S4..S9×T1 mirror combos, ±0.05): all lose except S4 49+131 +0.05 (1.0083, req 783f)
and S7 16+164 +0.05 (1.0100, e06c). Outer shells weak on w3.
Board: swarm-c at R 1.42–1.50 with g3-D0 c=0.32–0.40 (3faf strong: conv46 1.4195); gain tracks M2^(k)
(swarm-d critique). swarm-d w2 winner g4r1-D90 +0.08 r46 1.129. swarm-a closed whole-star map.
New: mechanism controls (family mech-control, --control, s21): frozen-k static densities
(h_static=h_k0, Γ and K) + BZ-avg ρ̄ for 3faf, 8617, 68f6 + w3 sanity on box-10 → work/ctrl1/map.txt.
Tools: work/frozen.py, frozen2.py, make_controls.py. Note posted …swarm-b_note_8db3; mailed swarm-c.
w3hi2 submitted: S10 combos ±0.05 + S4 49+131, S7 16+164 at c=0.15/0.3 (+S4 10.89 removed).
Next: read controls; if frozen-Γ ≥ k-dep → gain is per-k sharpening; run r46/r56 for informative ones.

## Wakeup 4 — 19:09–19:13 UTC

CONTROLS (s21): 3faf k-dep 1.495 vs ρ̄ 1.024 / frozen-K 0.915 / frozen-Γ (M2 6.84) 0.653; 8617 1.419 vs
1.015/0.919/0.732; 68f6 1.092 vs 1.001/0.968/0.946; sanity 096b = 1.0000. → gain needs k-dependence;
static M2 law fails for these profiles. swarm-e matched-M2 statics agree (r46 ≤ 1.07).
Posted result …swarm-b_result_46cb. Submitted r46/r56 versions of all 10 (work/ctrl1/map_r.txt).
w2 controls for swarm-d strong f07b (S1 ch) & 9445 (S3 ch, box 14 needed: w2 touches zero) on
s21,r46,r56 (work/ctrl2/map.txt).
Closed w3-hichan (abandon …868e, best 1.010) and w2-map-cma (abandon, best 1.0137).
NAMING: others use g = |G|²/|G1|²: g1=S1, g3=S2, g4=S3, g7=S4.
Budget ~141/500 used after this (controls count).
Next: tabulate r46/r56 controls + w2 controls → result post; consider k-scramble / shift test of
what in the k-dependence matters; offer verification of top candidates.

## Wakeup 5 — 19:28 UTC

r46 controls: w3 3faf ρ̄ 1.024 / frozen-K 0.988 / frozen-Γ 0.707 (k-dep r46 1.419); 8617 1.015/0.991/0.789;
68f6 ≈1.000 all. w2: f07b controls r46 ≤1.003 (k-dep 1.143); 9445 ≤1.023 (k-dep 1.245). Sanity 1.0000.
r56 pending. swarm-c b3: g3-D0 optimum c≈0.40–0.44; PES FAIL past 0.7; R not function of M2^(k) at
equal M2 (plane). swarm-e w3-nematic (C2 single pairs). swarm-a w3-profile (3G harmonic).
New probe family `k-reassign` (--diagnostic): h'_k = h_{k+M} (same per-k density multiset, same ρ̄ and
M2^(k)) for 6f32 (M1,M2,M3 — must agree on C6 Nk21) and 68f6 (M1). work/mshift.py, mshift/ids.txt.
Next: post r56 control table (final) + k-reassign result.

## Wakeup 6 — 19:45 UTC

k-reassign (h'_k = h_{k+M}): 6f32 1.500 → 0.598 (M1/M2/M3 agree to 3e-4), 68f6 1.092 → 0.917. Same M2^(k).
Posted …swarm-b_result_98d0. Decisive: gain is in the k-assignment (cross-momentum kernel), not density.
Board: swarm-a square-wave g1-D90 (+−3G) a76c s21 1.955; swarm-d strong on w2 (5061 R_min 1.161, used
frozen-k controls ≤1.006). swarm-c w3-cma.
Queued: k-reassign for a76c (f03e) and w2 5061 (b20c); a76c static controls s21+r46 (ctrl3/map.txt; frozenΓ box14).
r56 of ctrl1/ctrl2 still pending (5×6 queue).

## Wakeup 7 — 20:02 UTC

Reassignment: a76c 1.955 → 0.326 (f03e); w2 5061 1.161 → 0.569 (b20c). a76c controls: ρ̄ 0.97/0.97,
frozen-K 0.88/0.96, frozen-Γ 0.53/0.58 (s21/r46). Posted mechanism table …03f1 + correction …50ca
(half-translation equivalence only for w3; w2 on m+n≡0 mod 3 sublattice → K shift).
Board: swarm-c w3-cma ece3 R_min 1.653; swarm-a g1sq+g3 r46 1.80; swarm-e superadditivity.
New family `w3-chiral-phase` (hyp …8c5b): β on antisymmetric chiral combos (C_θ − C_180−θ)/√2,
±0.04, 18 probes (phase1/ids.txt). Tools: channels.chiral_beta_combos, write_signed.
r56 controls still pending.

## Wakeup 8 — 20:20 UTC

w3-chiral-phase probes (β on (C_θ − C_180−θ)/√2, ±0.04): S1–S3 × T1/T2 all 0.972–0.989, odd parts ≤0.3%.
**S4T1 49.11−130.89 β=+0.04: s21 1.0450, r46 1.1137** (−0.04: 0.9408) — first phase-only positive,
clean beyond-M2 automatically. Other S4T1 combos lose. Submitted line β=0.02..0.25 on it + S7T1 chiral
combos ±0.04 (phase2/ids.txt). swarm-a STRONG claim 0208 R_min 1.80 (g1 square + g3-D0).
NOTE: `swarm show` loops over many ids can exceed 120 s — run them in background.

## Wakeup 9 — 20:39 UTC
S4T1 49−131 phase line: s21 peaks 1.054 (β 0.06); r46 1.045/1.114/1.175/1.228/1.274 at 0.02..0.10 (keeps
rising) — big cluster spread; r56 pending (my r56 lane hasn't completed anything yet).
S7T1 16−164 +0.04: s21 1.031, r46 1.079. Other S7 combos lose. Posted interim result.
Submitted phase3: S9, S10 × T1 chiral combos ±0.04 + S4(0.06)+S7(±0.04) combos (14).
swarm-c STRONG 38fd R_min 1.986. swarm-d critique: PES ent. gap shrinks with R (still PASS).

## Wakeup 10 — 20:56 UTC
Phase: S10T1 40.9−139.1 +0.04 s21 1.0265 r46 1.173; S9T1 66.6−113.4 + s21 1.030 r46 1.140; S4+S7(+) s21 1.037
r46 1.247; S4+S7(−) 1.037/1.094. Pattern: s21 ≈ +3–5 %, r46 +14–27 % → suspect 4×6 chiral sampling.
No r56 of mine ever completed; 17 control r56 SUBMITTED since 19:10 → request …12f0 to operator.
Artefact check controls (phase_art/ids.txt): antisym −0.04/−0.08 on r46/r56; sym combo ±0.04 s21/r46/r56.

## Wakeup 11 — 21:18 UTC
Artefact checks (r46): antisym −0.04 0.9855, −0.08 1.0071; sym ±0.04 0.9975/0.9956 (s21 0.9585/0.9602).
Odd part robust (s21 5.2 %, r46 6.4 %), artefact 0.1 %; even part cluster-dependent (r46 positive).
Posted …(phase artefact result). w2 transfer: phase_w2/ids.txt (S4 all, S9 66.6, S10 40.9, ±0.04).
r56 still never completed for me; no operator reply yet.

## Wakeup 12 — 21:40 UTC
w2 phase transfer: S4T1 10.89−169.11 β=−0.04 s21 1.0465 r46 1.1565 (β=+0.04 0.792; odd 12.7 %).
w3's 49−131 combo loses on w2 (0.987/0.911). Parent-dependent phase channel. S9/S10 on w2 lose.
Line on w2 combo β=−0.02..−0.13 queued (phase_w2b/ids.txt).
swarm-a testing my w3 S4 phase as add-on on 0fea (swarm-c strong R_min 2.145); replied go ahead.
r56: still none of mine completed (likely low priority in queue, not stuck — others' r56 complete).

## Wakeup 13 — 22:01 UTC
w2 phase line S4 10.9−169.1: β −0.02 1.038 (r46 1.091), −0.04 1.047 (r46 1.157), −0.06 1.019, then drops.
swarm-a: my w3 chiral phase on 0fea → s21 2.740 / r46 2.843 (big α×β cross term).
Withdrew 17 static-control requests (ctrl1 map_r + ctrl2) to unblock my r56 queue.
New family `phase-addon`: w2 044c + S4c10 phase at β −0.02/−0.04/−0.06/+0.04 (addon_w2/ids.txt; work/addon.py).

## Wakeup 14 — 22:12 UTC
w2 add-on on 044c: β −0.02 1.259/1.343, −0.04 1.267/1.379, −0.06 1.246/1.405, +0.04 1.046/1.093 (s21/r46).
swarm-a: w3 phase on 0fea rising to β=0.20: s21 3.43 r46 3.89 r56 3.77; asked human for sanity check.
r56 is a global queue (≈230 pending rows), not stuck. Posted note (w2 cross term, r56 resolved,
energy-scale critique: propose exposing low_energies → Δ/E_width).
Submitted S4/S7 chiral ±0.04 add-ons on swarm-e's f6be (addon_f6be/ids.txt); S9/S10 staged in addon_f6be_b/.
swarm-e w2-phasemap takes 6-member shells on f6be. swarm-c w3-cma2 joint α + chiral phase.

## Wakeup 15 — 22:36 UTC
f6be (swarm-e w2, s21 1.231 r46 1.309 r56 1.302) + 12-member chiral phase ±0.04 (s21/r46):
S4c10 −: 1.266/1.404 · S4c49 −: 1.214/1.321 · S4c70 −: 1.244/1.267 · S7c16 −: 1.199/1.329 ·
**S7c43.9 +: 1.350/1.470** · S7c76 +: 1.211/1.380. Others lower.
Queued (addon_f6be_c): S7c43.9 line β 0.08–0.25, S7c43.9(+0.04)+S4c10(−0.04) combo, S9 ±0.04 (12).
swarm-a: w3 0fea + phase optimum β≈0.40: s21 3.919 r46 5.013 r56 4.882.
S10 add-ons still staged in addon_f6be_b/.

## Wakeup 16 — 22:58 UTC
f6be + S7c43.9 line: β .08 s21 1.397 r46 1.620 r56 1.563 (6fc7, w2 #1); .12 1.372/1.675; .16 1.275/1.591;
.20/.25 FAIL (manifold). b87e (β .04) STRONG: R_min 1.350 → claim …claim_50b4.
S9 add-ons on f6be: c66.59 − 1.241/1.428; c53.41 − 1.234/1.356. S7+S4 combo 1.300 (non-additive).
Launched `phase-cma` (cma_w2ph): 6-D β CMA on f6be, x0 S7c43.9=0.08, σ0 .03, λ9. Step with:
  uv run ... python cma_loop.py step w2ph   (from work/)
swarm-a closed w3 families (d48b 0fea+phase R_min 3.919, α·β synergy). swarm-d testing my phase on its bases.

## Wakeup 17 — 23:21 UTC
phase-cma gen0 (s21): best 1.4527 (i02 = req 83f6), fits [1.30,0.93,1.45,1.29,1.15,1.43,1.40,0.15,1.20];
mean → [0.101,0.002,−0.012,0.007,0.020,−0.005], σ .027. gen1 submitted.
swarm-c w3 STRONG 4462 R_min 4.182 (joint α+chiral phase). swarm-a: conv46−r46 gap grows at large phase
(qmax maybe applied to candidate only). swarm-e: 6-shell phase gradient on f6be (7818 R_min 1.312), testing
on my b87e/6fc7.

## Wakeup 18 — 23:43 UTC
w2ph gen1: best 1.3888, two FAILs (cliff). Stopped w2ph after gen1 (18 evals; best gen0 83f6 s21 1.4527,
x=[.10,−.004,−.011,.014,.025,−.006]).
swarm-e: 6-shell chiral gradient u adds on S7 point (868e s21 1.4285, r46 1.717). Added as composite
coordinate 'UE' (COMPOSITES in cma_loop.py; verified vs 868e to 1.6e-5).
Launched w2ph2: 7-D (6 + UE), x0 = 83f6 + UE .03, σ0 .015, λ10, seed 23. Step: python cma_loop.py step w2ph2.

## Wakeup 19 — 00:06 UTC (Oct 14)
w2ph2 gen0 best s21 1.4870 (dd54, x=[S7c43.9 .092, S4c10 .010, S9c66 −.009, S9c53 .023, S7c76 .024, S4c70 .005, UE .028]).
gen1 submitted. Plan: 2 more gens then close w2 (swarm-e's w2-jcma joint α+β ES seeded at my 83f6 takes over).
swarm-c w3 STRONG 9d3e 4.823 (boundary Σ|α|), bb15 5.345 climbing. swarm-a done (final summary).
swarm-e closed w3 families + w2-profile/phasemap.

## Wakeup 20 — 00:28 UTC
w2ph2 gen1 best 1.485 → plateau; stopped. dd54 STRONG: s21 1.487 r46 1.834 r56 1.720 conv46 1.830.
Closed phase-cma + phase-addon (result …6ada, correction …830c: 66 evals, 61/0/5).
k-reassign probes on top candidates: swarm-c w3 bb15 → bfb6, my w2 dd54 → febe (diagnostic).
swarm-d closed (final summary). Remaining open: w3-chiral-phase phase-only candidates awaiting r56 (a05b, d421).
Budget ~272/500.

## Wakeup 21 — 00:50 UTC
Reassignment: bb15 (w3 ~5.3) → 0.083 FAIL (bfb6); dd54 (w2 1.487) → 0.211 FAIL (febe). Posted …4d80.
w3 phase-only candidates (a05b, d421, 15e0) still waiting for r56.
Launched `w3-phase-cma` (cma_w3ph): α=0 on bare w3 template (base=template:w3), 5 chiral coords
S4c49.11, S7c16.1, S9c66.59, S10c40.89, S4c10.89; x0 S4c49=.06; σ0 .02; λ8. Hypothesis posted.

## Wakeup 22 — 01:12 UTC
w3ph gen0: all ≤ 1.025 (seed a05b 1.054); σ .02 perturbations cost. gen1 submitted; close after gen1 if no
gain. swarm-c STRONG 6bcd R_min 5.643 (M2(k)/M2 1.11).

## Wakeup 23 — 01:34 UTC
w3ph gen1 best 1.034 < seed 1.054 → closed w3-phase-cma + w3-chiral-phase (result …7d01, coverage).
Static controls for swarm-c 6bcd (w3 R_min 5.643): ρ̄ (M2 3.13, box14) 141f, frozen-Γ (M2 4.28, box18,
+1e-4 floor) 3bd6, frozen-K (M2 3.93, box14) 44e8; s21+r46 (ctrl4/map.txt).
Still pending: r56 for a05b/15e0/d421 (w3 phase-only). Budget 288 + 6.
Remaining plan: post 6bcd controls; wait for a05b r56; then swarm done.

## Wakeup 24 — 01:56 UTC
6bcd controls: ρ̄ 0.907/0.911, frozen-K 0.897/0.974, frozen-Γ 0.735/0.799 (s21/r46). Posted …fefc.
swarm-c 97ac R_min 6.316; swarm-e w2 jcma 1413 STRONG 1.525 (seeded on my dd54).
Only thing left: a05b (w3 phase-only) r56 — queue slow. Waiting with long cadence, then swarm done.
- 02:15 UTC: a05b/15e0/d421 r56 still pending; quiet hold.
- 03:16 UTC Oct 14: hold. a05b/15e0/d421 r56 still pending. Board: swarm-c w3-cma2 closed R_min 7.06 (e688); swarm-e closed w2-jcma (3e70 R_min 1.540), opened w2-cma2. Nothing new for me; 294/500.
- 04:17 UTC Oct 14: hold. swarm-c and swarm-e now done (final summaries posted); I'm the last active agent. a05b/15e0/d421/0998/22f9/8c21 r56 still pending. 294/500.
- 05:18 UTC Oct 14: in-flight 21/32 unchanged since 03:16, no r56 completions; posted operator request about r56 lane. Not submitting. 294/500.
- 06:17 UTC Oct 14: still 21/32 in flight, no r56 completions (3 h). No operator reply to request_e380 yet. Holding.
- 07:18 UTC Oct 14: broker IS completing runs (1c22 conv46 landed; other-phases 4→8); posted correction note to request e380. My r56 still pending. Holding.
- 08:19 UTC Oct 14: hold; r56 for a05b/15e0/d421 still pending; no operator reply.
- 09:20 UTC Oct 14: hold (6 h no r56 for mine). Plan: if still no r56 by ~12:20 UTC, post final summary (a05b r56 marked pending; broker computes claim from store) and run swarm done.
- 10:25 UTC Oct 14: hold; drafted work/final_summary.md for swarm done at ~12:20 cutoff.

## Wakeup 25 — 11:26 UTC Oct 14
r56 LANDED. Phase-only w3 (M2(k)/M2 = 1 exactly), all PASS:
15e0 (S4c49 β.08) s21 1.0508 r46 1.2276 r56 1.1608 conv46 1.2274 STRONG; a05b (β.06) 1.0539/1.1746/1.1194 STRONG;
caa0 (β.10) 1.0345/1.2744/1.1999 STRONG; 175e (S4+S7+) STRONG; 84df (S10c40.9) STRONG; d421, ad0e, 024f, 670a, 22f9, 8c21
robust_positive; 0998 suggestive. w2 f7ba, 4c00 robust_positive. → posted claim …claim_abe6 (with coverage).
Extension: hypothesis …9f3a; submitted 24 probes S4/S7 × T2/T3 chiral ±0.04 (work/phase_t23/ids.txt, gen_phase_t23.py).
Next: read; if odd part ≥2 % → S9/S10 × T2/T3 and β line; else close and swarm done (final_summary.md needs update with abe6).
- 11:50 UTC: 24 T2/T3 probes all still pending (s21 queue).

## Wakeup 26 — 12:21 UTC Oct 14 (final)
T2/T3 phase probes (S4/S7, 24): all lose, 0.717–0.974; odd ≤1.9 %; S9/S10 gated out. Posted result …cdac (coverage).
Updated work/final_summary.md (318/500) and ran `swarm done`. Loop stopped.
