# swarm-f notebook

Started 2026-10-14T05:20:03+00:00.

## 2026-10-14 05:30 — wakeup 1: scope chosen, stage 1 submitted
- Read brief, theory doc, pilot 40, progress 46, reference. Parent w1c: s21 Δ = 2.2586e-4, r46 2.4101e-4, M2 = 10.035.
- Deformation block = product of real cosine stars only (inversion-symmetric sets); sin·sin sector is unreachable.
- Board: swarm-a `linmap` (single term ±0.1/±0.05), swarm-b `jorbit` and swarm-c `jointorb` (joint orbits, small steps). Everyone is doing small local steps.
- My family **`bigamp`** (hypothesis 20261014T053025.497Z_swarm-f_hypothesis_b5cb): large amplitude, outer shells. Key pre-ED measurement: M2^(k)/M2 for α=±0.6 single terms: S1 ≈ 0.95 (lowers), S4 1.53/1.59, S7 1.87/2.17, S10 1.97/2.63; same for T1/T2/T3. Question: does Δ track M2^(k)?
- Tools: `work/mk.py OUT TERM...` (TERM = S<s>T<p>:a=x or :b=x; shells 1..10 = |G|² 1,3,4,7,9,12,13,16,19,21), `work/m2scan.py`.
- Submitted stage 1: 27 requests from work/stage1 (ids 053136–053152). Budget used 27/500.
- Next: read results; plot R vs M2^(k)/M2; decide stage 2 (multi-shell CMA-ES, or abandon with survival fraction).

## 2026-10-14 05:53 — wakeup 2: bigamp dead, switched to verifier (kconv)
- bigamp stage 1: 27/27 FAIL (manifold splitting/Δ>0.1, PES no separation). R≈1.2–1.9 at α=+0.3 on S4–S10 = competing phase (split/Δ≈0.4). Posted result 20261014T054940.974Z_swarm-f_result_a171 (with coverage) and abandon …054941.745Z_swarm-f_abandon_54e1. swarm-e `sharpen` independently found 30/30 FAIL.
- Board state: winners are joint orbits (swarm-b jorbit, swarm-c jointorb, swarm-i comove P_n). Top: 9de1 (comove P1 c=−0.5): s21 1.88, r46 2.65. Phase-only 2678 (chiphase β=0.02 mirror-odd on |G|²=9 pairs): s21 1.61, r46 2.22. Note that parent Δ_s21 is only 1.24×Δ_LLL despite M2=10 (R_staticM2 ≈ 0.12), so the parent gap looks limited by a competing level. Small deformations can lift it.
- swarm-d MT rule: on product/self-mirror directions β is even. All ladder clusters are chiral, so odd-β parts are artifacts.
- qmax is pinned (not agent-free); n_mesh/g_cutoff in the block are free (tightened = max).
- kconv: 18 diagnostic s21 runs, 9 candidates × (64,10),(96,14). Script work/mkconv.py REQ NMESH GCUT OUT. Hypothesis …055216.842Z_swarm-f_hypothesis_313e.
- Next: compare R with the originals; post a result; mail owners if drift > 2%. Then consider: what limits the parent's gap (which excited level)? Possibly a useful mechanism note.

## 2026-10-14 06:15 — wakeup 3
- kconv wave 1 done: all 9 converged to ≤5e-5 (posted result). Wave 2 (6 diag: ac14×2, 41dd, 1757, e317, 4385 at 96/14) submitted 0611xx.
- Leaders now: ac14 (swarm-r xsector) s21 4.44 / r46 4.93; trgrad 41dd 2.88/3.09. ac14 is small (α 0.06, β 0.02 per entry).
- New family statctl (hyp 20261014T061436.223Z_swarm-f_hypothesis_03f2): 14 --control static runs (mix δ, power t, frozen-k of ac14/c5b8). Script work/statctl.py. Question: does a small static change of w1c also give R≫1, i.e. is the parent soft?
- swarm-q is running the lllsub control (same blocks on uniform LLL). swarm-g geoflat: amplitude gain tracks Berry-curvature flattening; phase gain doesn't.
- Next: read statctl, post a result. If static R≫1, that is an important caveat: mail swarm-r, -n, -i and -l.

## 2026-10-14 06:38 — wakeup 4
- statctl done: static mix/power give R 0.83–1.06 (smooth; dlnΔ/dlnM2 ≈ 0.25–0.5); frozen-k statics of ac14/c5b8 0.97–1.02. Posted result 20261014T063224.914Z_swarm-f_result_f0da (coverage, incl. kconv wave 2: 15 leaders converged ≤1e-4).
- New leaders: swarm-r b55a s21 10.9 / r46 11.4 (3× ac14's steps); 2bb9 9.1; swarm-h josobol 53df 8.75. Δ/Δ_LLL up to 15.7 > M2=10. PES EG falls to ~3.5 (parent 13).
- work/escale.py: projected interaction scale E_sc = <Σ V|λ|²>, validated (LLL analytic; λ_0^kk=1). Parent 0.877 (8.8× LLL ≈ M2). Leaders are LOWER (b55a 0.87×). Posted 20261014T063802.484Z_swarm-f_result_e088; mailed swarm-l.
- Budget charged ~52+14+6 ≈ 72 /500.
- Open ideas: (a) when r56 lands for leaders, check finite-size consistency. (b) Is E1 rising? Needs the broker. (c) A critique of herding: everyone is now combining xsector levers. Maybe test the largest leaders' robustness to cluster (r56) once it's in.

## 2026-10-14 07:00 — wakeup 5
- b55a (swarm-r) is a STRONG claim: 10.91/11.39/11.16/11.42 (s21/r46/r56/conv46). ac14 is strong too (4.44/4.93/4.43/4.93). Many trgrad points cluster at s21 ≈ 10.9 (plateau?).
- swarm-a: the antisymmetrised two-body elements of b55a are ~2.5× the parent's. My E_sc (total) is 0.87×. Synthesis posted (note 20261014T070000.580Z_swarm-f_note_9bed): the gain moves vertex weight into the Pauli-surviving channel; R≈11 is tied to near-contact d_s=0.1 (scope caveat). Mailed swarm-a.
- Caveat to myself: swarm-q found that the same deformations on the uniform LLL LOWER the gap, so "break ideality → gain" needs w1c's density contrast too. Don't overclaim.
- Next: look for under-covered sectors (herding around b55a); maybe use budget on one distinct exploration; otherwise wind down with swarm done.

## 2026-10-14 07:28 — wakeup 6
- Board: strong claims b55a, c954 (josobol, 11.25 min), 9de1 (comove), ec27 (phase-only, 1.15). New top is ell2 3bd0 (swarm-k): s21 13.6 / r46 13.1, with 33 outer pair stars at entries ≤ 0.016 (max |m| = 5, so exp harmonics can exceed g_cutoff 8).
- swarm-a pairspec: the gain restores the V1 pair channel. The e2 proxy predicts R with R² 0.97, consistent with my Pauli-channel note.
- swarm-c statfront: w1c is the max of its ρ_t family, but static w3 has 2× its gap (context for the report).
- kconv wave 3 submitted (diag 96/14): 3bd0, 492f, 245d, e1b8 (0727xx–0728xx).
- Plan: post the wave-3 result. Then probably wind down (swarm done), unless a gap appears: most sectors are closed and mechanism work is well covered.

## 2026-10-14 07:40 — wakeup 7
- kconv wave 3 posted (20261014T073941.393Z_swarm-f_result_cb31): 3bd0 −3.6e-4, e1b8 −4.4e-3, 492f −3.3e-4, 245d +1.2e-5, all PASS. The outer ℓ=2 field is the first visible truncation. Offered 96/14 checks for λ ≥ 0.015 (mailed swarm-i and swarm-k).
- Open human requests on the board: E₁ exposure (swarm-l), whether the Σ|α| boundary is representation-dependent (swarm-k, swarm-h).
- My role now: on-demand verifier. Wake every ~30 min; check mail and new leaders; run 96/14 on new claim candidates in new families.

## 2026-10-14 08:11 — wakeup 8
- Many agents have finished (m, i, e posted final summaries). Strong claims: 3bd0 (ell2, 13.1 min), b55a, c954, 9de1, ec27. New tops: trgrad 2fb9 (s21 15.5 / r46 14.6), a3c2.
- swarm-p's kconv2: large-λ outer fields lose 12–30% on r46 (5a1c FAILs). It's r46 finite-size, not the kernel.
- kconv wave 4 submitted: 6fe2 (swarm-k asked), 2fb9, a3c2 (0810–0811).
- Next: post wave 4, then swarm done. My families are all closed: bigamp, kconv, statctl, escale.

## 2026-10-14 08:25 — wakeup 9: DONE
- kconv wave 4 posted (…result_1fea): 2fb9 −7.8e-4, a3c2 +1.3e-4, 6fe2 −6.3e-4.
- Posted the final summary and ran `swarm done`. All families closed. Loop stopped.
