# swarm-y notebook

Started 2026-10-08T04:36:04+00:00.

## 2026-10-08 wakeup 1 (05:06–05:37 UTC)
- Read the brief, docs 40/46, ADR-0040, notes §7/§12. The board was already crowded: atlases (c,f,g,b,a), joint orbits (e,i,z,m), Hessian (d), Sobol (o), CMA (s), z2 (h), chiral-β (j), z3-w2 (q,v,u,x), and matched-density controls (swarm-ab). I had built the same controls (`work/matched_control.py`, `work/calib.py`, static `ρ²`-mixture M2-matched families, all positive) but did not submit; ab owns that role.
- Tools: `work/geom.py` (Berry curvature from Wilson loops of the exact overlap, tr g, validated against eq. 7.22); `work/orbits.py` (joint-orbit coordinates of any block); `work/pool.py` (pooled single-orbit table from cached `swarm show` in work/show/); `work/features.py`.
- Findings: (1) only S1×T1 90° and S2×T1 0° have a first-order slope (≈ +1.5/unit u); all other single-orbit probes are flat; consistent with swarm-h's half-translation rule. (2) The winners have a rougher Berry curvature (std F 0.12–0.25 vs 0.015) and a positive trace defect, so geometry is not the mechanism. Posted as note `976c`.
- Family `inv-hi-w3` (hypothesis `ecb4`): the 24 Z2-invariant orbits at S4–S10, one at a time, u = ±0.03 (T3: ±0.02). 48 requests submitted (batch `work/b1`). Mailed swarm-h.
- Next: read the slopes; extend any |slope| ≳ 0.3; test additivity with o1+o2. Re-run pool.py as new data lands (refresh work/show for new ids).

## 2026-10-08 wakeup 2 (06:02 UTC)
- My 05:35 family duplicated swarm-w/ah/ai/al (posted 05:14–05:29). I missed them because I didn't re-read the digest before posting. **Lesson: run `swarm digest` until the backlog is empty right before any hypothesis post.**
- All 48 done, all PASS. Small-step slopes: S7×T1 16°± +0.62, S4×T1 49°± +0.55, S9×T1 67°± −0.53; T3 orbits curvature −60 to −80. Chiral twins have equal slopes, so the slope is achiral (M·T rule). Posted result `7167` with a coverage block. Mailed swarm-ap (frontier gradient owner).
- Board state: w3 leaders s21 ≈ 2.0, r46 2.2 (chiral-β dressing of the S2×T1∥ α leader, swarm-j `ba1f`, swarm-am `08b5`); r56 pending. Geometry of ba1f vs its base c3f0: Berry-curvature spread unchanged (0.55), trace defect 0.27 → 0.37; R 1.45 → 2.03 from β = 0.015 per term. Verifiers present: l, z (numconv), at, x (reserve), ab/p (M2 controls), h (partners).
- Budget: 48/500 used. No new family: the space is saturated. Next: monitor, critique (rule 11), targeted checks only where a gap appears.

## 2026-10-08 wakeup 3 (06:36 UTC)
- Leaders now s21 3.33 / r46 3.09 (swarm-t 4a76, GP cross-family), ap 7a96 s21 2.81 / r46 4.07. r56 has produced zero results in about 95 min, including the parent references (swarm-c request 8cff). Many agents are now reserve/verifiers (at, x, u, w).
- Geometry of the top 5 (critique note `1ce3`, mailed t and ap): ⟨tr g⟩ 1.8–2.4; t 4a76/6191 have F < 0 over part of the BZ (F_min −0.52, converged at 36²); PES gap 4–5 vs parent 20; R correlates positively with non-ideality among the leaders.
- No evaluations spent (48/500). Next: when r56 lands, compare the s21/r46/r56 spread against R − 1 for the leaders. Possibly offer reserve budget for targeted checks.

## 2026-10-08 wakeup 4 (07:11 UTC)
- Frontier: ap 3a0e s21 4.39 (r46 pending → later 4.39), t 4020 s21 3.52 / r46 3.92. r56 still has no results (parents pending). Many agents have posted final summaries or moved to reserve.
- Mail: swarm-o says small invariant slopes can flip sign between s21 and r46. Accepted, and my S4/S7 slopes are labelled s21-only (reply sent). swarm-t accepted critique 1ce3 and asked for geometry columns; posted note `8563` (F_min < 0 beyond ×1.25 on t's line; dressing raises R at fixed ⟨tr g⟩; R tracks ⟨tr g⟩ along the frontier). Tool: `work/geomtable.sh ID…`.
- Budget 48/500. Next: once r56 lands, tabulate s21/r46/r56 for the frontier with geometry. Otherwise idle.

## 2026-10-08 wakeup 5 (07:56 UTC)
- Frontier ap 4547 s21 5.20 / r46 5.41; r56 still empty after ~3 h (swarm-c raised it with the human). About 20 agents have posted final summaries. Static M2 curve saturates at about 1.7 (as, l), so the frontier is about 3× its equal-M2 static (p, as).
- Nothing to do until r56 lands. Plan: final table of geometry (geomtable.sh) vs s21/r46/r56 for the top ~10, then `swarm done`.

## 2026-10-08 wakeup 6 (09:24 UTC), final
- Frontier ap 0328 s21 6.66 / r46 7.11; r56 still empty after about 5 h, parents included; most agents have posted final summaries.
- Geometry of the new frontier: ⟨tr g⟩ 3.1–3.4, F_min −0.3 to −0.6, PES 4.9. Final summary written to work/final.md and filed with `swarm done`. 48/500 evaluations used.
