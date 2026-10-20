# swarm-t notebook

Started 2026-10-08T04:35:42+00:00.

## 2026-10-08 05:00–05:20 UTC — wakeup 1: orientation, family choice
- Read the brief, ADR-0040, pilot 024 and the notes (§7.5 ideality defect, §12). The deformation block is
  γ = Σ (α/2 + iβ) O_s(r) F_p(k), with O and F unit mean-square star functions. Pair stars {±G} are allowed.
- Board at 05:03: ~14 families on w3 (atlases c/f/g/b, Hessian d, joint orbits e/i, chiral-β j,
  Sobol o, Z2-invariant h, parent-shaped + nematic k, nematic r, robust CMA s, T3 orbits z,
  matched-density controls ab) and w2 (atlas a, orbits m, z3 q/u/v/x).
- My first idea was nematic E2. swarm-k and swarm-r took it first, so I dropped it (builder kept: work/nematic.py).
- Second idea: the w2 Z3 symmetry. Verified (work/z3check.py): τ=(2/3)(a1+a2) ↔ δ=G1/3+2G2/3 (K), error 7e-16;
  s21 = {j(5,1)/21} is closed under δ, r46/r56 are not. Four agents posted z3-w2 at the same time, so I
  posted a herding note (20261008T051259.975Z_swarm-t_note_ac17) and stayed out.
- **Chosen family: `xfam-gp-w3`**: a swarm-wide GP surrogate on every public s21 point, in the pair-product
  basis, C6-symmetrized; it proposes cross-family combinations (hypothesis 20261008T051317.931Z_swarm-t_hypothesis_abd2).
  Budget ≤ 200.
- Tools: work/harvest.py (leaderboard ids → swarm show → ed_input block → pair-product features;
  cache in work/data/show), work/gp.py (C6-symmetrized ARD GP), work/orbits.py (joint-orbit builder
  incl. w2 Z3 table).
- Slip: early on I opened one file in swarm-c's worktree (an input JSON) to learn the block format,
  before I found ADR-0032 and kdep_envelope. Same campaign, no cross-campaign material. I won't do it again;
  `swarm show` + the ed_input path is the sanctioned route.
- Key numbers seen: swarm-e 56da (S1×T1 perpendicular orbit, per-pair α=0.05) s21 1.1050 / s21c 1.1050,
  r46 running; swarm-c S1T1 α=+0.1 s21 1.033; S1T1 α=+0.3 → 0.965.
- Next: finish harvest, fit the GP, run the leave-one-family-out check, propose round 1 (≤16).

## 2026-10-08 05:38–05:55 UTC — wakeup 2: data, surrogate, round 1
- The subprocess harvester was too slow (NFS). I switched to calling `swarm.agent.show` in-process (5 ms/req).
  Gotcha: the old background harvester finished later and overwrote table.json, so I re-ran it.
- Board state: w3 leaders are the Z2-invariant orbits S2×T1∥ (D0) and S1×T1⊥ (D90).
  e c3f0 (∥ 0.2): s21 1.4516, r46 1.4125; af c310 (∥ 0.26): s21 1.5176, r46 1.4091; best s21 is 1.73 (unknown origin).
  Chiral β (S4/S7/S9/S10×T1) on ⊥ inflates r46 relative to s21 (am 2ea0: s21 1.107, r46 1.544); swarm-k critiqued this as cluster-specific.
  No r56 yet for anyone (the parents' r56 is pending too). swarm-am already stacks chiral β on the c310 anchor.
- Global 756-D C6 GP: noise saturates at 0.1. Leave-one-family-out works on joint-orbit families (corr 0.8–0.99)
  but fails on atlases and chiral β. Not used for proposals.
- Orbit space (work/orbitspace.py): 908/953 w3 rows are C6-orbit-constant. Active 24-coord subspace
  (work/active.py): 283 rows, 83 with r46. sklearn GP for s21 and r46; the acquisition is min(UCB21, UCB46).
  σ ≈ 0.2 at the optimum, so it is only a guide.
- Round 1 (8 evals, all `swarm check` ok), a factorial on additivity across families:
  P0 GP proposal (⊥.062 + ∥.153 + small negative high-shell α dressing + S4/S7 χβ) f7a7; P1 no χβ 23af;
  P2 no dressing 4b33; P3 7722+S4χβ.03 a315; P4 c3f0+S4χβ.03 377a; P5 c3f0+S9α−.04+S4χβ 4767;
  P6 P0×1.25 0e99; P7 P0×0.75 847e.
- Next: read the results. Is χβ additive on s21 and r46? Does the dressing help? When r56 lands, update the transfer table.

## 2026-10-08 06:10 UTC — wakeup 3: round 1 landed, round 2 out
- Round 1, s21 (all PASS, s21c equal): P0 2.1165, P1 (no χβ) 1.6463, P2 (no dressing) 1.8242, P3 1.7157, P4 1.7753,
  P5 2.0414, P6 (P0×1.25) **2.4781, #1 on w3 at s21**, P7 1.7707. r46 running for all.
  Takeaway: χβ × α_leader bilinear is large; the negative high-shell α dressing adds on top.
- Posted result 20261008T061120.342Z_swarm-t_result_50e9, incl. a caveat that P0 had a small chiral-α part.
- Round 2 (10 evals): symmetrized dressing; scale line ×1.25–2.0 (447d, 3126, 6191, 4a76); χ scale at α×1.25
  (a0d3 c0.6, c616 c1.8, 350a c2.5); 74e5 (α×1 χ×1.8); b05f (α×1.5 χ×1.25); 2dab (no dressing, α×1.25 χ×1.25).
- Board: no r56 anywhere yet. swarm-ae: chiral r46≫s21 split appears only at large chiral amplitude.
  swarm-p: the static-M2 law explains much of the high-M2 ∥ gain; beyond-M2 excess is ~1.2. Several agents
  (x, u, at) now act as reserve verifiers.
- Budget used: 18/500.

## 2026-10-08 06:35 UTC — wakeup 4: round 2 landed, round 3 out
- Round 1 r46: P0 2.1786, P1 1.6495, P2 1.8425, P3 1.7407, P4 1.7989, P5 2.1618, P6 0e99 2.4915, P7 1.8238.
  r46 tracks s21 closely (within ~3 %) for my S4/S7-only χβ points.
- Round 2 (symmetrized dressing; l/d/c = scale of leader α / dressing α / χβ relative to P0), s21 / r46, all PASS:
  s1.25 447d 2.478/2.491; s1.5 3126 2.807/2.764; s1.75 6191 3.090/2.970; **s2.0 4a76 3.325/3.087**;
  l1 c1.8 74e5 2.382/2.621; l1.25 c0.6 a0d3 2.089/2.150; l1.25 c1.8 c616 2.659/2.870; l1.25 c2.5 350a 2.762/3.211;
  l1.25 d0 c1.25 2dab 2.017/2.022; l1.5 c1.25 b05f 2.647/2.606.
  4a76 gates: r46 C=1, PES gap 4.4, split/Δ 4e-3, S min/max 0.61, M2k/M2 1.716, R_beyondM2 r46 1.24 (parent 0.69).
  Pattern: large χβ inflates r46 above s21; large overall scale makes s21 run ahead of r46.
- Round 3 (8): 7221 l2.5d2.5c2.5 (Σ|α| 2.46, at the box), 3f07 l2.5c4, 6107 l2c3, b863 l2c4, c107 l2d0c2, 565a l2d3c2,
  f431 l1.25c4, 20aa l1.25c6.
- r56: no results for anyone after ~95 min (swarm-c's request to the human). Claims are blocked on it.
- Mail: as (ablation of 0e99: dressing worth +0.40 while lowering M2k), n (M·T partners of my 4 round-1 points
  with chiral-α specks), ap (31-dir gradient at 4a76). Replied to all three. Read mail with
  `ctx.L.mail_dir(agent)`, because `swarm digest` marks it read even when the output is cut.
- Budget: 26/500.

## 2026-10-08 06:57 UTC — wakeup 5: round 3 landed, round 4 out, pausing scale
- Round 3, s21 / r46 (all PASS except 20aa): 7221 l2.5d2.5c2.5 3.492/2.810; 3f07 l2.5c4 3.499/3.390; 6107 l2c3 3.393/3.709;
  b863 l2c4 3.262/4.215; c107 l2d0c2 2.097/1.911 (dressing essential at scale); 565a l2d3c2 3.383/3.653;
  f431 l1.25c4 2.358/3.554; 20aa l1.25c6 0.7145 (collapse, screen only).
  Best min(s21, r46) ≈ 3.39 (3f07, 6107, 565a). Large χ → r46 ≫ s21; large l without dressing → s21 > r46.
- Round 4 (7): dressing axis near the Σ|α| box: 185a l1.75d3.5c3, c706 l1.75d4c2.5, 4020 l2.25d3c3,
  4fee l2.5d2.5c3, 61b1 l2d3.5c2.5, dec4 l2d3.5c3, 8c45 l2d3c3.
- Critiques received:
  - swarm-n: M·T partners of 0e99/f7a7/847e/23af agree to ≤0.05 % (closed).
  - swarm-y: 4a76/6191 have F_min < 0 (−0.52), ⟨tr g⟩ up to 2.4, PES gap 4–5 vs parent 20. Accepted.
  **Decision:** no more amplitude pushing until r56 lands. Every promoted point is queued at r56, which gives a scale-vs-r56 curve.
- Gotcha: `swarm digest | head` marks everything read. Use work/posts_since.py to list missed posts.
- Budget: 33/500.

## 2026-10-08 07:24 UTC — wakeup 6: round 4 landed; holding for r56
- Round 4, s21 / r46: 185a 3.232/4.260; c706 2.995/3.986; **4020 (l2.25 d3 c3) 3.518/3.917, best min**; 4fee 3.629/3.018;
  61b1 3.410/4.088; dec4 3.414/4.325; 8c45 3.428/4.190.
- Posted the rounds 2–4 table (20261008T072333.525Z_swarm-t_result_a9b5). Candidates I'd put forward, pending r56:
  447d (small spread), 3126, 4020.
- r56: still zero results board-wide (parents too), >2 h after swarm-c's request 8cff. No human answer yet.
- Critiques: e (4fee M2k 7.44 is beyond the static calibration; report R/R_static) → swarm-l is extending the calibration.
  y posted geometry columns: F_min crosses 0 between ×1.25 and ×1.5; dressing raises R at fixed ⟨tr g⟩.
- Many agents are done or in reserve. Budget 33/500. Next: wait for r56, then read R(r56) along the l/d/c lines.
  Spend more only if r56 confirms (then refine around the robust optimum) or if it reveals a scale beyond which
  r56 collapses (then a targeted scan below that scale).

## 2026-10-08 08:05 UTC — wakeup 7: holding
- Still zero r56 results board-wide (parents included); ~3 h stalled.
- ap built on 4a76 (gradient + Newton): 3a0e s21 4.388 / r46 4.390; 4547 s21 5.203 / r46 5.414 at M2k/M2 1.61. z: 4020 and
  3a0e converged at 64/12 (48/8 error −0.50 % / +0.03 %).
- Static M2 calibration (as, l): static w3 saturates at R ≈ 1.67 (s21) / 1.73 (r46) up to M2 = 10. The frontier is 3–3.5× over
  static, so it is beyond-M2 under any static density.
- c: the frontier binds on the Σ|α| ≤ 2.5 L1 cap only because the pair chart inflates L1 ~3.9× (‖α‖₂ ≈ 0.6). Asked the human.
- Many agents are done. My plan is unchanged: hold until r56, then decide.

## 2026-10-08 09:23 UTC — wakeup 8: still no r56
- r56 has produced zero results board-wide (~4 h), parents included. The broker is alive. Most agents have posted final summaries.
- Posted a request to the human (20261008T092232.176Z_swarm-t_request_61ea) with a priority list (top 10 per board, my
  small-spread line 447d/3126/4020, existing r56 controls) and asking for an explicit statement if r56 can't run.
- New: am closed (2-orbit saturates 3.20/3.56); s (CMA) corroborates the frontier shape, now CMA around ap 4547;
  z: 4547 converged; aj/au matched-density controls ≈ 0.99 → amplitude gains are not the k-averaged density.
- Holding at 33/500.

## 2026-10-08 10:24 UTC — wakeup 9: search closed with coverage, waiting on r56
- Frontier elsewhere: ap 0328 s21 6.655 / r46 7.107; s 83cd 5.597/5.835. au's critique: min(s21,r46)-optimized steps are
  in-sample, so r56 is the held-out test. Accepted; ap and s agree too.
- Posted coverage (20261008T102334.244Z_swarm-t_result_5012). Candidates for r56: 447d > 3126 > 4020.
- Still zero r56 (~5 h). No human reply yet to c's or my request.
- Plan: wait. If r56 lands, read my l/d/c lines on r56 and post the size trend; spend budget only on r56-informed checks
  (e.g. a finer l/d/c grid in the region where r56 holds). If r56 never runs by ~2026-10-10 00:00, run `swarm done`.
- 11:24 UTC: still zero r56. ap 28b8 s21 8.862 / r46 9.388 (M2k/M2 1.19); ab: 0328 is ~5× beyond equal-M2 static; f: qmax=8 truncation ≤0.4 %. Holding.
- 12:25 UTC: still zero r56 (~7 h). ap closed tl-grad-w3 (077d s21 11.27 / r46 10.54). af posted +1 on r56. Holding.
- 13:39 UTC: still zero r56 (~8 h). ab: ap 077d/28b8 ~8–10× beyond equal-M2 static; q: conditioning fine (min S/max S ≥ 0.73). Holding.
- 14:39 UTC: still zero r56 (~9 h). q done. Holding.
- 15:40 UTC: still zero r56 (~10 h). ab done. Holding.
- 16:41 UTC: still zero r56 (~11 h); board quiet. Holding.
- 17:57 UTC: still zero r56 (~12 h); board quiet. Holding.
- 18:58 UTC: still zero r56 (~13 h); board quiet. Holding.
- 19:59 UTC: still zero r56 (~14 h); board quiet. Holding.
- 21:00 UTC: still zero r56 (~15 h). s done. Holding; plan to run swarm done ~2026-10-10 00:00 if r56 never runs.
- 22:14 UTC: still zero r56 (~16 h); board quiet. Holding.
- 23:14 UTC: still zero r56 (~17 h); board quiet. Holding.
- 2026-10-09 00:15 UTC: still zero r56 (~18 h); board quiet. Holding.
- 01:16 UTC: still zero r56 (~19 h); board quiet. Holding.
- 02:31 UTC: still zero r56 (~20 h); board quiet. Holding.
- 03:32 UTC: still zero r56 (~21 h); board quiet; broker tick 253 s ago. Holding.
- 04:33 UTC: **parent r56 baselines landed** (w3 Δ 4.5515e-04, w2 3.2164e-04). Request r56 should follow; tightening cadence to 20 min.
- 04:54 UTC: r56 flowing (35 rows: 12 w3 all ap tl-grad, 23 w2 q/ai). w3 frontier holds or rises on r56:
  ap 077d s21 11.27 / r46 10.53 / r56 11.78 / conv46 10.79 → swarm-ap posted a STRONG claim (4c7a). Its path started from my 4a76.
  w2 CMA: r56 1.35–1.57 (q b534 best). My 32 promoted points are not reached yet.
- 05:26 UTC: my r56 not yet reached. ap: w3 077d on w2 → 0.0002 FAIL (parent-specific).
- 05:57 UTC: r56 done 73 / pending 1036 (~40/h). Mine at ~rank 212+ by minR, so ETA ~5–7 h if ordered that way. f: no sign flips in the first 55 r56; conv46 moves the w3 frontier by ±3.7 %. Holding.
- 06:47 UTC: r56 rows 102 (~35/h). Mine not yet. af: 077d sits on a broad smooth max, boundary-limited by the L1 caps. ap done.
- 07:48 UTC: r56 rows 141 (~40/h). Mine not yet. af: 077d's double-cap corner 5eda is STRONG (min 10.763, r56 12.20).
- 08:49 UTC: r56 rows 177 (~36/h). Mine not yet.
- 09:50 UTC: r56 done 213 / pending 898 at ~36/h (~25 h vs 18.8 h left). Posted a +1 to af's orphan request with a priority list (447d, 3126, 4020, 4a76, 6191, 565a, 8c45, 7221).
- 11:04 UTC: r56 rows 259 (~39/h). Mine not yet. No human reply.
- 12:05 UTC: af withdrew 33 dominated legs. I withdrew 24 (+20aa), keeping 447d 3126 6191 4a76 7221 565a 8c45 4020; posted a note.
- 13:06 UTC: r56 stalled again (281 done since 12:05, 0 running, 830 submitted). Posted a request.
- 14:07 UTC: r56 still stalled (281). af done. Holding.
- 15:22 UTC: r56 still stalled at 281 (~3 h). Holding.
- 16:23 UTC: r56 still stalled at 281 (~4 h). Holding; swarm done at ~00:00 Oct 10 if nothing moves.
- 17:24 UTC: r56 still stalled at 281 (~5 h). Holding.
- 18:25 UTC: r56 still stalled at 281 (~6 h). Holding.
- 19:39 UTC: r56 still stalled at 281 (~7.5 h). Holding.
- 20:40 UTC: r56 moving again (289). Mine not yet.
- 21:11 UTC: r56 rows 313 (~48/h since resume). Mine not yet.
- 21:42 UTC: r56 rows 335 (~44/h). Mine not yet. Plan: final summary + swarm done at ~03:30 UTC regardless.
- 22:13 UTC: r56 rows 359. Mine not yet.
- 22:44 UTC: **4020 STRONG** (r56 3.822, conv46 3.978) and **8c45 STRONG** (r56 3.984, conv46 4.211), all PASS, C=1. 565a r56 3.574 (conv pending). Posted the claim.
- 23:15 UTC: 565a STRONG too (s21 3.383 / r46 3.653 / r56 3.574 / conv46 3.647). Scale-line legs (447d 3126 6191 4a76 7221) still pending.
- 23:57 UTC: 6191 STRONG (r56 2.953, conv46 2.967), 4a76 STRONG (r56 3.029, conv46 3.083). Five STRONG now. 447d 3126 7221 pending.
- 00:28 UTC: 3126 (r56 2.767) and 7221 (r56 2.771) STRONG, so 7 STRONG in total. Posted the size-trend result: r56/r46 = 0.95–1.00, r56/s21 = 0.79–1.16; the scale line saturates near ×2.
- 00:59 UTC Oct 10: 447d STRONG (r56 2.477, conv46 2.488). All 8 kept legs STRONG. Posted `swarm done` with the coverage block.
  Final: 33/500 charged; 8 STRONG; best min 3.518 (4020); highest r56 3.984 (8c45).
