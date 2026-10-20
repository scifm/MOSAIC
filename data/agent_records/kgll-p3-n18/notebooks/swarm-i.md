# swarm-i notebook

Started 2026-10-14T05:20:13+00:00.

## Wakeup 1 — 2026-10-14 ~05:35 UTC
- Read brief, progress 40/46, theory §4.3–6.4, swarm-d MT note. Board: linmap (a), jorbit (b), jointorb (c), sharpen (e), bigamp (f), bigstep (h), chiphase (d), phasequad (j).
- Key data: swarm-c P orbit S1xT1 c=-0.06/entry -> s21 1.202 PASS (req c5b8); M=A+B -0.06 -> 0.776; product S1xT1 a=-0.1 -> 0.992. S2 (|G|^2=3) product terms: +-0.1 a / +-0.05 b all ~0.5 (very stiff). swarm-e G12xT1 a+0.3 -> 1.447 but FAIL.
- Note: I accidentally opened swarm-a's source json in their worktree (path from `swarm show`) to learn the block format. Same campaign, format only; avoid other worktrees going forward — use ed_input path from `swarm show` instead.
- Chose family `comove` (hyp 20261014T053527.997Z_swarm-i_hypothesis_fbaf): matched P_n = S_n x T_n, G.R=0. Physics: LL0 Bloch zero r0(k) = -l^2 z x k, so G.r0 = k.R_eff, R_eff = l^2 z x G in T_n. P_n = half co-moving, half counter-moving.
- Tools: work/build.py (orbit:S:T:c[:b] specs), work/board_table.py (leaderboard with deformation summaries; arg filters req ids).
- Submitted P1 line scan c in {-.02,-.04,-.09,-.12,-.18,-.25,-.35,-.5}: req 8dc1 93e8 5676 c340 2462 ee37 d770 9de1. Mailed swarm-c.
- Next: read P1 scan + swarm-c's P2/P3 ±0.06 map; c5b8 r46/r56 promotion outcome (finite size!). Then P2/P3 scans and combination.

## Wakeup 2 — ~05:54 UTC
- P1 scan (s21 / r46): -0.02 1.071/1.067; -0.04 1.139/1.136; -0.09 1.290/1.309; -0.12 1.370/1.415; -0.18 1.442/1.633; -0.25 1.466/1.895; -0.35 1.478 FAIL (split/D 0.108); -0.5 1.882/2.650. r56 pending for all. PES EG decreasing 10 -> 2.8. M2k falls.
- c5b8 (P1 -0.06) PASS r56 1.19 and conv46 1.20 -> small-c effect robust.
- swarm-c map: S2xT2-P concave (0.76/0.97) -> matched co-moving prediction refuted. S3xT1-P -0.06: s21 1.37, r46 1.62 (f721). S2xT1 +0.06 1.18 / -0.06 0.40.
- Posted interim result 20261014T055345.202Z_swarm-i_result_52f4. Mailed swarm-n (trgrad at P1=-0.5).
- Submitted w2 (12): P1 -0.4/-0.45/-0.55/-0.6; S3T1-P -0.12/-0.2/-0.3/-0.45; grid P1{-0.25,-0.5} x S3T1P{-0.06,-0.12}. Budget used 20/500.
- Next: r56 for P1 scan; conv46 (g_cutoff 10) for large c — exponentiation tail. Watch PES EG trend. Consider phase on P1 at optimum and adding T1-only G⊥R orbits of outer shells (S4+ have ⊥ pairs? check).

## Wakeup 3 — ~06:15 UTC
- Stage 2 results: P1 -0.4 FAIL(sp .102), -0.45 1.639/2.632, -0.55 1.842/2.458, -0.6 FAIL(sp .318). S3T1-P -0.12..-0.45 all FAIL. Grid: only (-0.5,-0.06) PASS 1.527/2.534 (worse than P1 alone).
- Board: swarm-r ac14 (5 small levers combined, log-additive) s21 4.44 / r46 4.93 / r56 4.43 -> SUGGESTIVE, conv46 pending. swarm-n: P1=-0.5 incumbent is a level-crossing plateau (~2.75 s21). Controls (a, q): rho_bar control R=0.999 -> beyond averaged density. Phase-only mirror-odd: b (u1+u2 1.73/2.28), d (S5T1 X 1.61/2.22). Product stars, large single terms, outer orbits at rms 0.1 all dead (a, e, f, h, j, k, m).
- Posted closing result 20261014T061624.230Z_swarm-i_result_c3cb (coverage). Key insight posted: MT-invariant deformations (alpha on mirror-even, beta on mirror-odd) give identical R on a cluster and its mirror -> chirality can't fake those gains.
- Mailed swarm-c (T1-P 3D refinement is theirs) and swarm-g (compare Omega against r46).
- Budget 20/500. Considering next: mirror-odd AMPLITUDE (A-B alpha) is even in alpha by MT -> pure curvature; check whether anyone measured it (work/mixed_alpha.py running).
- Board scan (work/mixed_alpha.py): no pure A-B alpha measured (only swarm-o E2 + combos). Posted hyp 20261014T062351.460Z_swarm-i_hypothesis_8163 (family oddamp).
- Submitted 12 DIAGNOSTIC (no promotion) A-B alpha probes: S1T1 +-0.04,+-0.08; S2T1(60/120) +-0.02,+-0.04; S3T1 +-0.02,+-0.04. Builder work/build_cls.py 'S:theta:alpha:beta'; classes work/classes.py. Budget 32/500.
- Next: symmetric part = curvature, antisym = chirality artifact. If sym > +2%, resubmit non-diagnostic.

## Wakeup 4 — ~06:42 UTC
- oddamp stage 1: A-B alpha CONVEX. sym part: S1 +0.006/+0.022 (c .04/.08); G3 +0.011/+0.044 (.02/.04); G4 +0.018/+0.065 (.02/.04). anti ~ -0.006..-0.011 (chirality artifact). Best b4ce G4 -0.04 1.0742.
- Board: claims STRONG swarm-r ac14 (4.44/4.93/4.43/4.93), swarm-b phase-only ec27 (1.15). Leaders now b55a = 3x ac14 (s21 10.9, r46 11.4). swarm-f: kernel-converged; energy scale falls -> not rescaling. Controls ~1. swarm-k ell2: log-slopes ~ cos(2 theta_GR).
- Posted 20261014T064235.729Z_swarm-i_result_3fb4. Mailed swarm-r.
- Submitted w4 (15, non-diag): lines S1 -.15/-.25, G3 -.06/-.09/+.06, G4 -.06/-.09/+.06; ac14 + G3/G4 A-B +-.04, ac14 + S1 A-B -.08; b55a + G4 A-B +-.04. Tools: work/merge.py BASE_REQ spec... Budget 47/500.
- Next: if convex at incumbents -> push A-B on b55a (larger c, multiple shells). Owe a critique post.

## Wakeup 5 — ~07:05 UTC
- oddamp stage 2: convex only to |c|~0.04; manifold fails at 0.09 (G3,G4), 0.25 (S1). At ac14/b55a A-B is concave on s21 (-1.5..-3%), flat r46 (+-1%) -> incumbents are local maxima. Posted result 20261014T070423.989Z_swarm-i_result_5b29 + abandon e2bb.
- 9de1 completed the ladder: 1.882/2.650/2.571/2.650 all PASS, C=1 -> broker claim 'strong'. Posted claim 20261014T070508.349Z_swarm-i_claim_ff45 (gap enhancement; beyond-M2 pending). Mailed swarm-l for D1 rho_bar control on 9de1.
- Board: leaders ~11 (b55a STRONG, h Sobol c954 s21 11.33). Saturation between t=3 and 4 along ac14; s21 splitting binds.
- Budget 47/500. Next options: (1) if swarm-l can't, run D1 control myself (--control); (2) phase-only splitting cancellation (crowded: b,d,e,p); (3) critique duty satisfied partially via oddamp-at-incumbents robustness. Consider winding down if nothing distinct remains.

## Wakeup 6 — ~07:33 UTC
- swarm-l submitted D1 control for 9de1 (-> cd68). Board: swarm-k chiral l=2 field on S4-S10 x T1 (E+ = lam e^{+2i theta}) -> 3bd0 s21 13.58 / r46 13.11, linear in lam; E- breaks manifold. swarm-h c954 full ladder 11.33/11.61/11.25/11.63. swarm-a mechanism: V1 pair channel (e2 proxy R^2 .97). swarm-c: static w3 has 2x w1c gap.
- Critique posted 20261014T073253.863Z_swarm-i_note_87a5: kernel tail (local FFT n_mesh 128) >8: 9de1 9e-5, b55a 5.5e-3, 3bd0 2.5e-2; scaled lam .02: 13% (>8), 6% (>10). Asked k and f for 96/14 kconv. (work/tail.py, work/tail_scale.py; run from repo root with PYTHONPATH=work.)
- Budget 47/500. Next: D1 result on 9de1 -> update claim. Then likely swarm done unless a distinct direction appears.

## Wakeup 7 — ~08:00 UTC (final)
- 9de1 D1 control (swarm-l cd68): 0.927/0.926/0.922 -> beyond M2. Claim update 20261014T075939.342Z_swarm-i_claim_4299.
- Truncation critique answered: swarm-f 96/14 on 3bd0 (-3.6e-4), e1b8 (-4.4e-3) hold; swarm-k claimed 3bd0 STRONG (13.1-13.6). swarm-p kconv2 on outer leaders.
- Frontier now chiral E+ field refinements (r, n, d, k, h) — no distinct direction left for me. Posting swarm done (47/500 used).
