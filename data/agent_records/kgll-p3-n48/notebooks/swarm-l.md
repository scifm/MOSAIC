# swarm-l notebook

Started 2026-10-14T10:24:27+00:00.

## 2026-10-14 ~11:20 — wakeup 1 (orientation, family choice)
- Read docs 40, 46, notes §7.5/§12, theory §6.4. Key priors: k-dep responses are small (≲1–2 %) and flip sign
  between clusters (pilot: +0.51 % 4×6, −0.92 % 5×6). Ladder: confirm21 needs s21 ≥ 1.02; r46/r56 ≥ 1.0; conv ≥ 1.05.
- Board at start: swarm-a + swarm-b (duplicate 60-axis ±0.05/±0.03 maps), swarm-c (jorb, joint orbits S1-3×T1-3),
  swarm-e (bigamp: line scans to boundary + 18-D Sobol S1-3×T1-3), swarm-i (kpow: ρ^(1+λF) — my first idea, taken),
  swarm-d (chiral-phase: half-shell β; Θ=M·K argument: full-shell linear β slopes are cluster-chirality artifacts).
- Early map: best s21 R = 1.0109 (swarm-a axis); α[S1,T1] = −0.05 → 1.0080 (req c99b).
- MY FAMILY `phase-even` (hypothesis 20261014T111948.310Z_swarm-l_hypothesis_f7fb): β = ±0.12 on all 30 full-shell
  axes; read even part [R(+)+R(−)]/2 (mirror-cluster average, artifact-free). Motivation: phase keeps Σ|W_G(k,k')|²
  but pushes weight to high G → effective scattering-kernel flattening; w1c is over-sharp. Budget ≤ 180.
- Submitted stage 1: 60 requests, work/inputs/pe012 (generator work/gen_phase.py OUTDIR BETA [axes]).
- Posted request 20261014T112056.018Z_swarm-l_request_73f0: block excludes separately-odd sector sin(Gr)sin(kR)
  (k-dependent envelope translation). Await human answer.
- NEXT: when results land, tabulate even/odd per axis (write work/analyze_pe.py), stage 2 at ±0.24 / ±0.06.
  Also do a critique post (~1 in 5).

## 2026-10-14 ~11:45 — wakeup 2 (pivot)
- Board exploded (~40 agents). KEY: joint (G,R) orbits carry big signal; separable stars cancel it (swarm-c).
  Leaders: ⊥ α S1×T1 (swarm-j, s21 1.64), chiral-odd β (swarm-f 1.56), c's S2×T1 +60 β 0.03 (s21 1.25, r46 1.40).
  A "strong" claim already exists: swarm-c ce1f (S1×T1 +30 β+0.03, phase only): s21 1.159, r46 1.159, r56 1.149, conv46 1.159.
- swarm-e/swarm-a: full-star |β| ≈ 0.12 and outer shells at 0.05 break the manifold. My stage 1 confirmed: all 30 β axes
  at ±0.12 have even part −22…−100 %. Withdrew 27; 43 charged. Posted abandon 20261014T114611.242Z_swarm-l_abandon_f34d.
- swarm-g had already posted the sin·sin note (before mine). Fine; mine is a duplicate request.
- Audit: ce1f conv46 vs r46 gap differ 5e-8 → conv rung is not independent for pure LL0. Posted request
  20261014T114629.779Z_swarm-l_request_28b0 asking for a 27-site / other-shape cluster for finalists.
- Mailed swarm-m re S1T3.
- Herding is extreme (≥10 optimizers/surrogates, 3 nematic, 3 ⊥, 4 kprof). NEXT: find an unclaimed concrete piece or act
  as a critic; don't spend budget for its own sake. ~457 evals left.

## 2026-10-14 ~12:10 — wakeup 3 (hold)
- Withdrawn requests still RAN (withdraw only deprioritises): charged 58 total, my S6–S9 β data will land; ignore.
- New: ⊥ α S1×T1 line (swarm-j): α⊥=−0.45 → s21 1.64 / r46 2.63 / r56 2.44 (ea28), but ⊥ is half static LL mixing
  (swarm-s), ak suspects an s21 branch change. swarm-c STRONG phase-only claim d698 (S2×T1 +60 β+0.03): 1.249/1.404/1.347;
  swarm-u verified S00(k)=parent pointwise. f: S3×T1 chiral-odd β+0.05 → s21 1.558, r46 1.641.
- swarm-at: g_cutoff 8 drops 7–9 % of first-order kernel change for S9/S10 deformations (so conv46 matters for outer shells;
  my "conv46 = r46" observation holds for S1–S3 leaders only — keep in mind).
- Every idea I had is claimed ≥1×. Holding budget (~440) rather than duplicating. Watch for: abandoned pieces, a need for an
  independent replication of the final optimum, human answers to my two requests.

## 2026-10-14 ~12:45 — wakeup 4 (watch)
- Board leaders now multi-orbit α+β combos (surrogate steps): t 8c01 s21 4.82 (r46 pending), h c662 s21 4.76 / r46 5.23
  (split/Δ 0.0013, EG 3.8). STRONG claims: c d698, f 728b (S3×T1 odd β, conv46 1.641), j 3d0f (⊥ α −0.45).
- Verifiers active: p (PES N_A=3 request, sewing test), g (gauge-covariance request), u, k (density controls all < 1:
  gains are not density), e (EG drops 13.4 → 3–5 with any k-dependence; flat in N), as (robustness), y.
- My mechanism thought (not posted): k-dependent envelope = k-dependent LL mixing (swarm-s identity) → larger short-range
  pseudopotential; "beyond-M2" true but mechanism may be effective LL mixing. k/u diagnostics partly address it (projected
  interaction moments flat), so not posting unless I can test it.
- Still holding ~440 evals; no unclaimed piece. Next: watch for human answers / gaps; consider `swarm done` if nothing opens.

## 2026-10-14 13:11 — wakeup 6 (slow watch)
- New claims: h STRONG c662 (4.76/5.23/4.67, conv46 5.23; density control 0.995 by k). Mechanism debate: g (gap ∝ d³,
  R amplified by vortexability breaking; requests d_sc control) vs p (contact term inert). c: leaders restore the static
  M2 law (R_beyondM2 0.12 → 0.72), not beyond it. ap: leaders' γ on uniform LL0 (lllref). My LL-mixing idea is covered.
- My withdrawn S5–S9 β ±0.12 runs landing as expected: all FAIL (S6T1 −81 %, S7T1 −50 %). Not worth a post.
- Lanes are contended (o reports 80-min stalls) → not submitting duplicates is the useful choice.
- Plan: hourly watch. Act if (a) human opens sin·sin sector (my request 73f0 / g's 9c9e) → take it; (b) a claim needs a
  critique nobody has made. Otherwise `swarm done` near the deadline (2026-10-16T10:27).

## Wakeup 7 — 2026-10-14 14:13 UTC (watch)
- Board: s21 leaders now ~10 (av e0a8 10.39, s c325 9.87/r46 10.15, av 0d8f 9.67/r46 10.49); o f5f1 STRONG 6.28/8.33/8.12. Records sit on the Σ|α|/Σ|β| caps (t request 789e on cap representation, unanswered). k: density control predictable, all records ≈0.96–0.99 → density excluded. g retracted 9d4e; c withdrew the M2-law reading (ec66).
- My zero-cost gate audit of the top 6 (swarm show): S ratio 0.077–0.214 (fine), M2k/M2 ≤ 1.00, split/Δ ≤ 0.065 (e0a8 s21 highest; r46 ≤ 0.02), EG(N_A=2) 2.3–4.1, EG(N_A=3, s21c) 1.6–3.4 — consistently lower at N_A=3 but all well above 0.5. Nothing to critique; u/y already audit records.
- No human answer on sin·sin (73f0 / g 9c9e). No unclaimed direction; lanes still congested. Hold budget (58/500). Plan unchanged: watch hourly, `swarm done` near deadline.

## Wakeup 8 — 2026-10-14 16:34 UTC (done)
- Board: STRONG records now ~10–12 (h 5063 11.65/12.30/11.97; e c577 11.42/11.59/11.38; s c325 9.87/10.15/9.54; av e0a8). The caps bind. u/n flag qmax-8 non-PSD pair spectra at R > 10 (u request f0fa). Many agents are done.
- No human answers on the board in ~5 h; nothing unclaimed left for me. Ran `swarm done` (summary post 20261014T163449.271Z_swarm-l_note_669a; text in work/done_summary.md). 58/500 charged. Loop stopped.
