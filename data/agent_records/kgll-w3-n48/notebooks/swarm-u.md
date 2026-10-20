# swarm-u notebook

Started 2026-10-08T04:35:46+00:00.

## 2026-10-08 05:10 — wakeup 1: scope chosen, phase 1 submitted
- Read brief, docs 40/46, ADR-0040, theory §2/§5/§6.4/§8, whole board. w3 is heavily herded (≥12 agents). w2: swarm-a (separable atlas), swarm-m (orbit-w2, joint orbits, 48-eval phase 1).
- **Finding (work/z3check.py):** w2 has only Q∈{3,9,12} harmonics → ρ_w2 invariant under τ=(a1+a2)/3. Magnetic translation: S00[γ(k−δ,r−τ)](k+δ)=S00[γ](k) to 1e-15 with δ=(−1/3,1/3) (G-frac coords). s21 (kk1≡5kk2 mod 21) is closed under δ → R_s21(γ)=R_s21(Pγ) exactly. Invariant monomials: m+n≡0 mod3 AND R1≡R2 mod3 → in box: {Q=3,9,12,21}×T2 only. All other w2 blocks: zero s21 slope (pure curvature); slopes at r46/r56 = finite-size artifacts.
- Posted hypothesis 20261008T051022.772Z_swarm-u_hypothesis_02e8 (family z3-w2, ≤150 evals). Mailed swarm-m, swarm-a with the rule.
- Phase 1: 24 evals submitted (work/p1, ids in swarm status): S5×T2 & S6×T2 orbits α±0.1, S10×T2 achiral combos α±0.1, chiral β(orbit−mirror) S2/S5/S6×T2 ±0.05. Convention: entry c per pair product (swarm-e style).
- Tools: work/z3lib.py (orbits, invariance, block builder), work/gen_p1.py.
- Note: early on I accidentally opened the first 5 lines of a file in swarm-e's worktree (via a path in `swarm show`). Nothing used. Don't open other worktrees.
- Next: read phase-1 results; check the prediction R(+a)≈R(−a) on a/m non-invariant data; phase 2 line scans/CMA-ES in invariant subspace.
- Accidentally ran submit-batch twice; withdrew the 24 duplicate requests (ids > 20261008T051100) before acceptance. Originals: 20261008T05103x–05105x.

## 2026-10-08 05:40 — wakeup 2: z3-w2 closed, switched to chi-phase-w3
- z3-w2 phase 1: all 24 strongly negative (best 0.746 S6×T2 90° α=−0.1; S10×T2 FAIL; chiral β ±0.05 → 0.48–0.56, S6 FAIL). Swarm-v, x, q found the same Z3 rule independently and also closed the invariant sector.
- **My error:** I claimed T1/S1/S3 blocks have zero s21 slope. Wrong: cos⊗cos is half-invariant when G and R carry opposite Z3 charges. Correct rule: (m+n)+(R2−R1) ≡ 0 mod 3 per monomial (swarm-w/x). Posted result+correction 20261008T053921.419Z_swarm-u_result_5e93 with coverage.
- Matched-density controls already done by swarm-ab (mdctl-w3) and swarm-p (m2-control). Static M2 ladder: M2 5.5→1.326, 6.0→1.398, 4.571→1.164 (p cefd). Leaders beat it (af c310 1.518 @ M2k 5.30; e c3f0 1.452 @ 4.57; am 6790 1.348 @ 3.81).
- New family chi-phase-w3 (hyp 20261008T054130.514Z_swarm-u_hypothesis_7b10, ≤70 evals): j's M·T rule plus h's Z2 rule leaves 11 chiral-β directions (Q4/12/16×T3, Q7/13/19/21×T1&T2). Phase 1: 10 evals on the 5 unscreened ones (work/chi1), β ±0.03 per entry. w has Q7/Q13×T1 positive (r46 1.21/1.16). Mailed w and j.
- Digest lesson: save `swarm digest > work/digest_TIME.txt`. Its output is persisted outside the worktree, and I can't read it there.
- Next: slopes → gradient line scan along g (all 11), then CMA in the top 2–3; phase 3 adds the phase optimum to the amplitude leader.

## 2026-10-08 06:08 — wakeup 3
- chi-phase-w3 phase 1: all 10 negative (0.37–0.87 at β=0.03; odd ≤0.8%). Duplicated swarm-j's batch 2, which I hadn't read in time. Closed with abandon 20261008T060735.952Z_swarm-u_abandon_6b70 (coverage included).
- Board state: frontier = S1T1⊥/S2T1∥ amplitude ridge (e, af; r46 ~1.41) + chiral-β T1 dressing (j ba1f s21 2.03, am). Controls ab/p: leaders keep 1.2–1.46× over equal-M2 static. Everything awaits r56 (the parent r56 reference is pending too).
- Switched to verifier/reserve (note posted). Plan: once r56 lands, odd/even ±β twin checks of the chiral-dressed leaders (coordinate with j), plus critiques.
- Lesson: read ALL digest pages (`swarm digest` repeatedly, saving each to work/) before opening a family. I've been herded/duplicated twice.

## 2026-10-08 06:40 — wakeup 4 (hold)
- r56 stalled for all requests, including the parents (swarm-c request 20261008T061052.874Z_swarm-c_request_8cff).
- The ±β odd/even checks I planned were done by ae (chicheck-w3), k (perpchi-w3) and j (β-profile). On small β the odd part is cluster-consistent; the large even part is about 2× on r46.
- Frontier: e 80c7 s21 2.151 / r46 2.290; t 0e99 s21 2.478 (as: χβ worth ~0 alone, high-shell negative α dressing +0.40). Numerics converged (l, z, ag).
- ≥8 agents are in reserve (at, x, w, a, r, k, u, …). No action. Wait for r56, then audit sign agreement s21/r46/r56 for the top claims.

## 2026-10-08 07:30 — wakeup 5: done
- r56 still stalled; many agents finishing; ≥10 reserves committed to the r56 audit. Ran `swarm done` (summary in work/done.md). 34/500 charged. Loop stopped.
