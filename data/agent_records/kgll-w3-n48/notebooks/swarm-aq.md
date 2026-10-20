# swarm-aq notebook

Started 2026-10-08T04:37:17+00:00.

## 2026-10-08 wakeup 1 (05:15–05:45 UTC)
- Read the brief, the docs (40, 46, key-facts, theory §4–9) and the whole board (~110 posts). The board is heavily herded on the S1xT1 ⟂ / S2xT1 ∥ amplitude orbits on w3 (i, e, h, ad, ac, af, s, o, ap, aj, d, …), with many mechanism/control agents (p, ab, as, ao, al).
- The clean beyond-M2 positive: swarm-w's chiral phase-only S4xT1 (49.1°) / S7xT1 (16.1°) on w3 (`…swarm-w_req_8ffd` s21 1.053, r46 1.211). Nobody has chiral β x T1 on w2 → my family.
- Wrote `work/chiral.py`: joint-orbit builder (Cartesian G1=(1,0), G2=(−½,√3/2)), chiral pairs θ/180−θ, magnetic-translation invariant fraction (w2: τ=(1/3,1/3); w3: Z2×Z2). It reproduces swarm-w's w3 invariant list and 8ffd's β matrix exactly (my "bp" = w's "+").
- w2 chiral T1: S2/S5/S6/S10 fully Z3-breaking (skipped); 12 half-invariant directions.
- Posted hypothesis 20261008T054305.085Z_swarm-aq_hypothesis_4054 (≤110 evals). Submitted phase 1: 24 evals (work/p1, ids in work/p1_submitted.txt). Mailed swarm-ar (dedupe S4xT1 β) and swarm-w.
- Note: `swarm show` on ~300 ids is too slow under node load (survey.py timed out). Use targeted shows only. Set OMP_NUM_THREADS=1.
- Disclosure: I read one file in swarm-i's worktree early on (noted in the hypothesis post).
- NEXT: when p1 lands, compute odd/even parts per direction (work/analyze.py to write), line-scan the positive ones (0.06/0.09/0.12), check additivity, promote.

## 2026-10-08 wakeup 2 (06:10–06:15 UTC)
- Phase 1 landed (24/24 PASS). Only S7xT1 44°+ gains (7922: s21 1.026, r46 1.276, r56 pending). w2 χβ curvature ~5–10x w3. Odd>even also for S4 11°− and S3 30°− (s21 vertex estimates ≈1.04, 1.03).
- HERDING: ah, an, av ran the same screen within 3 minutes; ak flagged it. Their results agree with mine. Line scans → an; cross terms with w2 α leaders → swarm-b (chidress-w2); joint CMA → swarm-q (cma-w2). I closed chiral-beta-w2 with result 20261008T061240.819Z_swarm-aq_result_31d3 (coverage block included).
- New piece (family z3twist-w2): w2's Z3 is exact only on s21. On r46/r56 the Z3-breaking half of any w2 direction can give a linear twist artefact. The partner test is not representable for Z3 (2π/3 shifts need sin terms). So I measure the odd part of FULLY breaking directions on r46/r56 directly: 8 controls (S2/S5/S10 χβ ±0.03, S2 achiral α ±0.05), clusters s21,r46,r56. ids in work/twist_submitted.txt.
- r56 stage is stalled board-wide (swarm-c request 8cff), so the r56 legs may take a while.
- NEXT: when the twist controls land, compute the odd parts per cluster (analyze.py handles _[ab][pm] names). If the r46 odd part is ≳0.05 at 0.03, post a critique of w2 r46-based leaders and mail m, ar, an, b, q. If it is ~0, post that w2 r46 numbers are not twist-contaminated at this level.

## 2026-10-08 wakeup 3 (06:39–06:45 UTC)
- Twist controls landed on s21 + r46 (r56 pending). Fully Z3-breaking w2 directions: r46 odd ≤ 0.004 (no linear twist artefact), r46 even +0.02..+0.05 against s21 even −0.03..−0.16. Posted refutation 20261008T064015.315Z_swarm-aq_refutation_c7cf of swarm-v's first-order-artefact explanation (v f84d). Mailed v, an, ab, m.
- swarm-an's acute− r46/r56 controls (205e/b39a/7c6d) decompose 7922/aa67, so I did not duplicate them.
- Submitted 3 more controls: S10 χ19 at ±0.015 and +0.06 on s21/r46/r56. They test whether the r46 even term scales as c² (work/twist2_submitted.txt).
- Budget: 35 requests charged as of this note (24 search + 11 controls; controls may cost per cluster).
- NEXT: read the c-scaling, the r56 legs when they land, and an's parity controls. Then decide: possibly the reserve/verifier role (many agents are there already), or a new direction if a gap opens.

## 2026-10-08 wakeup 4 (07:10–07:15 UTC)
- c-scaling of S10 χ19 (fully Z3-breaking, w2): s21 even −0.040 at 0.015 → −0.163 at 0.03 (quadratic, ×4). r46 even +0.050 at 0.015, +0.049 at 0.03 (plateau!), and 0.699 at +0.06. So the r46 gain is NOT curvature. It saturates at ≈ +5 % immediately: a soft-level / level-crossing picture. The parent w2's r46 Δ is likely set by a very deformation-sensitive state; any deformation lifts it until a second level ≈ 5 % higher sets the gap. Implication: R_r46 ≈ 1.05 is "free" for w2, right at the robust_positive threshold.
- Controls cost 3 evals each (charged per cluster). Budget 57/500.
- swarm-v self-refuted the first-order artefact claim (…refutation_51bb), citing my controls + an's parity controls. an's parity controls: odd part is cluster-consistent, split all even.
- swarm-as (…result_fad2): w3 phase-only β also splits s21 1.009 vs r46 1.297, and the split vanishes once α is on → the same soft-level effect may exist on w3's r46?
- Submitted twist3 (r46,r56 only): S10 χ19 ±0.005 (onset), S2 χ60 +0.015, S5 χ30 +0.015 (plateau universality). ids in work/twist3_submitted.txt.
- NEXT: when twist3 lands, post the soft-level result. Possible w3 analog: tiny Z2-breaking/phase deformation of w3 at 0.005/0.015 on r46 to test whether w3's r46 parent Δ also sits on a soft level (as's data suggest). Ask the human whether sector-resolved low_energies can be exposed (they would settle it directly).

## 2026-10-08 wakeup 5 (07:38–07:42 UTC)
- twist3 landed (r46): S10 χ19 r46 even +0.0058 (0.005), +0.050 (0.015), +0.049 (0.03), −0.30 (0.06) → quadratic then saturating = soft-level crossing. S2 χ60 +0.020 at 0.015, S5 χ30 +0.025 at 0.015.
- Posted result 20261008T073901.230Z_swarm-aq_result_3308 (w2 r46 parent sits on a soft level; ≤ ~5 % of any w2 r46 R_gap can be this effect) and request 20261008T073901.971Z_swarm-aq_request_6e98 (expose sector-resolved low_energies).
- Submitted the w3 analog: χβ S1×T1 30° (fully Z2-breaking on w3) at +0.005, ±0.015, +0.03 on s21/r46/r56 (work/w3soft_submitted.txt). Budget charged so far: ~57 + 12 + 12 = 81.
- NEXT: read w3 onset. If w3 r46 also shows a positive even plateau → critique for the r46 readings of w3 phase-only points (8ffd etc.). Check the human's reply to my request. Then probably close and go to reserve, or done.

## 2026-10-08 wakeup 6 (08:05–08:10 UTC)
- w3 onset test landed: χβ S1×T1 30° (fully Z2-breaking) r46 even −0.0005/−0.006/−0.038, s21 −0.003/−0.020/−0.070. Analytic, no plateau → the w2 r46 soft level is w2-specific. Posted result (w3 control).
- Board: most agents are done or in reserve; the w3 frontier is at R ≈ 5 (ap 4547), and r56 is still stalled for all, parents included.
- My remaining value: report the r56 legs of my 19 controls (does w2's r56 also have a soft level?) when they land. Otherwise I am done. Budget 77 + 12 = ~89/500.
- NEXT: long wakeups (~1 h). When r56 lands, post the r56 table, then `swarm done`.

## 2026-10-08 wakeup 7 (09:34 UTC) — DONE
- r56 still stalled (~4 h, swarm-t request 61ea). Withdrew my 19 controls + 7922 so their r56 legs go behind the leaders' r56 runs (data will still land, readable via swarm show).
- Posted the final summary via `swarm done`. Loop stopped.
