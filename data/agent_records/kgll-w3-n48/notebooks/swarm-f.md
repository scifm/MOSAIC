# swarm-f notebook

Started 2026-10-08T04:34:49+00:00.

## 2026-10-08 04:59 — wakeup 1
- Read brief, docs 40/46, theory §2/§6.4, kdep_envelope API. Board had only swarm-c's `atlas-T1-w3` hypothesis (w3, 10 stars × T1, α/β, 90 evals), inviting T2/T3 or w2.
- Claimed `atlas-T23-w3` (hyp 20261008T045913.326Z_swarm-f_hypothesis_d475): w3, 10 spatial stars × {T2,T3}, α∈{−0.1,0.1,0.3}, β∈{±0.1}; n_mesh 48, g_cutoff 8 (= swarm-c). 100 evals, budget ≤140.
- Tools: work/mk.py builds inputs (stars by |G|² in 120° basis, |R|² in 60° dual). Inputs in work/atlasT23/. Shells: |G|²=1,3,4,9,12,16 are 6-member; 7,13,19,21 are 12-member (chiral pairs).
- w3 support = |G|² ∈ {4,12,16} (half-period lattice). w2 = {3,9,12}.
- Note: on Nk=21, k→2k permutes the mesh, F_T3(k)=F_T1(2k): T3 diagonal samples = permutation of T1's. Compare T3 vs swarm-c T1.
- M2^(k) ratio at α=0.3 single term: ≤1.37 (S7). Independent of T.
- Submitted batch1 = 30 T3 amplitude evals (work/batch1.log). Next: T3 β (20), T2 α/β (50) as in-flight slots free.

## 2026-10-08 05:20 — wakeup 2
- LABEL BUG: in work/mk.py-driven atlas I looped p over |R|² (3,4) and named files T{p}; so "T3" files = T2 (|R|²=3), "T4" = T3. Inputs correct. Always name momentum stars by T-index: T1=|R|²1, T2=3, T3=4.
- batch1 (30) = T2 α∈{−0.1,0.1,0.3}: all <1; ±0.1 symmetric (no linear term on T2); |G|²≥4 collapses the gap (≤0.3 at |G|²≥12); α=0.3 FAILs except |G|²=1 (0.539). Reproduces swarm-g's T2 ±0.1 to 4 digits.
- swarm-g duplicated atlas-T23-w3 (T2/T3 α±0.1 β±0.05). I closed mine: result 20261008T052024.036Z_swarm-f_result_d55c with coverage; mailed g.
- Board: ~30 hypotheses. Leader swarm-i joint-orbit S1×T1 ⟂ orbit (pair stars, α=0.0866 diag), s21 1.189, r46 1.156, r56 pending; M2k/M2 1.05.
- Budget used 30/500. Next: wait for leader r56; pick an uncovered direction (ideas: amplitude+phase compensation on the winner; verifier/critic role).
- work/fam.py prints source+R per family from leaderboard (slow: one swarm show per row; run in background).

## 2026-10-08 05:50 — wakeup 3
- Board ~90 posts. Mapped landscape (w3, s21): only two Z2-invariant achiral T1 orbits are linear: S1T1⟂ and S2T1∥ (|G|²=3, ∥). Plane leaders: af c310 s21 1.518/r46 1.409; e c3f0 (S2T1∥ α=0.2/pair) 1.452/1.413; am 6790 (S1T1⟂ + phase) s21 1.348/r46 1.496. r46 turns over with amplitude (e a7c2 s21 1.50 r46 1.364 at M2k 5.9).
- Phase-only beyond-M2: chiral β on 12-member shells × T1 (S4,S7: w; S9,S10: j) gain linearly; s21 +3–5%, r46 +16–21% (cluster-dependent, k critiques).
- Mechanism: offset rule (g, b, ao): slope ∝ parent weight at G ± G_c(R), times e^{-|R|²/4}; LL0 control (ao): S1T1⟂ lowers uniform LL0 → needs w3's S3 harmonic. ab: static Δ(M2) slope 0.19/unit M2 on s21; fa76 beats M2-matched static by 15%.
- No r56 results yet (even the parents' r56 is pending). Leaders far inside the boundary (Σ|α|≤0.78, M2k/M2≤1.46).
- Decision: no new family now (everything low-order is covered by ≥2 agents). Wait for r56; then do an ED-free finite-size analysis (s21→r46→r56 vs amplitude/direction) as verifier/critic, and look for a gap after it.
- swarm-ag is re-running my high-shell T2 points at g_cutoff 12/16 (kernel tails 1–7% outside the box at gc 8).

## 2026-10-08 06:15 — wakeup 4
- Frontier jumped: chiral-β dressing (S4/S7/S9/S10×T1 chiral phase, Z2-invariant) on amplitude leaders. swarm-t 0e99 (36 pair stars × 9 T pairs, Σ|α|1.23, Σ|β|0.30, M2k/M2 1.29): s21 2.478, r46 2.491, PES N_A=2 gap 5.6 (parent ~20), adm ratio 0.72. w2: b chidress-w2 s21 1.30.
- Verified convergence: l (n_mesh/g_cutoff to 96/16, ≤1e-4), ag (my high-shell collapse is converged physics).
- r56 has produced nothing for ~95 min, parents included; swarm-c posted request to human. at, x, u switched to reserve/verifier.
- Decision: hold budget (30/500). Fewer submissions help the r56 queue. Re-evaluate after r56 lands; possible roles: finite-size trend analysis, targeted checks of the 2.5× leaders.

## 2026-10-08 06:47 — wakeup 5
- w3 frontier s21 3.50 (swarm-t 3f07, xfam-gp, r46 pending). ap 7a96 s21 2.81 / r46 4.07 (large cluster spread). w2 frontier b 8c39 s21 1.30 / r46 1.34.
- Critiques on board: y (leaders non-ideal, Berry curvature sign changes, ⟨tr g⟩ 1.8–2.4; PES gap ~4–5 flat vs R); a (PES gap uncorrelated with R); g (cluster-sampled M2 identical across clusters, explains no drift); n (M·T partners reproduce to 0.05%); l/z/ag (converged at 64/12 = 96/16).
- ~10 agents in reserve (w,a,r,k,n,at,x,u,j,ao done). r56 still stalled (no results, parents included).
- Decision: reserve. 470 evals unspent. Will act if (a) r56 lands → audit finite-size ordering of the frontier vs amplitude scale, or (b) someone requests a targeted check.

## 2026-10-08 07:27 — wakeup 6
- w3 frontier ap 3a0e s21 4.388 / r46 4.390 (tl-grad). t 4020 3.52/3.92. w2 ai 0e27 1.325/1.431. r56 still stalled (~2.5 h, parents included).
- Many agents done (v, ak, g, i, x, o, d, al, ah, w). l extending static M2 calibration to M2 7–10 (frontier M2k up to 7.4, e's critique).
- Staying in reserve (470 evals) because if r56 refutes the frontier, reserve budget will be needed for an r56-robust re-search. Hourly checks.

## 2026-10-08 08:28 — wakeup 7
- w3 frontier ap e2f1 s21 5.43 / r46 5.56 (on Σ|α|=2.5 L1 box edge; c's request 3772 asks human whether L1 chart-dependent box is intended). w2 frontier q 92f0 1.370/1.393.
- Static Δ(M2) saturates ~1.7 (as, l replicate); frontier ~3–3.5× beyond equal-M2 static.
- r56 still stalled (~3.5 h). Most agents done. I stay in reserve (470 evals) in case r56 refutes the frontier.

## 2026-10-08 09:15 — wakeup 8
- w3 frontier ap 0328 s21 6.655 / r46 7.107. w2 q 356e 1.408/1.439. r56 stalled ~4.3 h. Nearly all agents done (active searchers: ap, q, s, t?). Still reserve, 470 evals.

## 2026-10-08 10:16 — wakeup 9
- w3 frontier ap c270 s21 7.88 (confirm21 pending); 8946 s21 7.23 / r46 7.27. ap stopped climbing (au's critique: min(s21,r46) steps fit the cluster split; r56 is the held-out test). s closed at 5.60/5.84. w2 q 356e 1.408/1.439.
- r56 stalled ~5.3 h; t re-requested human. Still reserve, 470 evals.

## 2026-10-08 11:17 — wakeup 10
- w3 frontier ap 8589 s21 9.42 / r46 9.60 at M2k/M2 1.21 (adm ratio 0.98); ab: 0328 ~5× beyond equal-M2 static. w2 frontier q 356e 1.41/1.44 (cma-w2 closed).
- qmax is broker-fixed (swarm check rejects qmax≠8). Wrote work/qtail.py (incoherent upper bound on interaction weight outside the qmax hexagon): parent 7e-21, 8589 2e-3 mean / 4e-3 max. Posted note 20261008T111906.479Z_swarm-f_note_2733 (qmax cannot explain the gain); mailed ap.
- r56 still stalled ~6.3 h. Reserve, 470 evals.

## 2026-10-08 12:20 — wakeup 11
- ap closed tl-grad-w3: best 077d s21 11.27 / r46 10.53 (323 evals). Swarm idle, waiting on r56 (~7.3 h stalled; af +1 to c's request). Reserve, 470 evals.

## 2026-10-08 13:32 — wakeup 12
- No change: r56 stalled ~8.5 h. ab: 077d/28b8 ~8–10× beyond equal-M2 static. q: conditioning audit null (min S/max S ≥ 0.73 for w3 top-26). Reserve, 470 evals.

## 2026-10-08 14:33 — wakeup 13
- No change (no posts, r56 stalled ~9.5 h). Reserve.

## 2026-10-08 15:34 — wakeup 14
- r56 stalled ~10.5 h. 43/48 agents done; alive: f, s (~390 reserve), t, af, ap (177 reserve). Keep waiting hourly.

## 2026-10-08 16:35 — wakeup 15
- No change (r56 stalled ~11.5 h). Reserve.

## 2026-10-08 17:50 — wakeup 16
- No change (r56 stalled ~12.8 h). Reserve.

## 2026-10-08 18:51 — wakeup 17
- No change (r56 stalled ~13.8 h). Reserve.

## 2026-10-08 19:52 — wakeup 18
- No change (r56 stalled ~14.8 h). Alive: f, s, t, af, ap. Reserve.

## 2026-10-08 20:53 — wakeup 19
- No change (r56 stalled ~15.8 h). Reserve.

## 2026-10-08 22:07 — wakeup 20
- s done. r56 stalled ~17 h. Alive: f, t, af, ap. Plan: keep hourly reserve until r56 lands; if still stalled ~6 h before deadline (2026-10-10 04:38), post final summary and swarm done.

## 2026-10-08 23:08 — wakeup 21
- No change (r56 stalled ~18 h). Reserve.

## 2026-10-09 00:09 — wakeup 22
- No change (r56 stalled ~19 h). Reserve.

## 2026-10-09 01:10 — wakeup 23
- No change (r56 stalled ~20 h). Reserve.

## 2026-10-09 02:23 — wakeup 24
- No change (r56 stalled ~21 h). Reserve.

## 2026-10-09 03:24 — wakeup 25
- No change (r56 stalled ~22 h; broker tick 192 s ago). Reserve.

## 2026-10-09 04:25 — wakeup 26
- r56 STARTED. Parent r56: w3 4.5515e-4, w2 3.2164e-4. ap 077d: s21 11.27 / r46 10.53 / r56 11.78 / conv46 10.79 PASS → claim STRONG. ap 43a7 strong (r56 11.44, conv46 10.16). conv46 (qmax10, n_mesh64, gc10) consistent → qmax note confirmed.
- Plan: wait ~1 h for more r56 results, then ED-free audit (sign/ordering s21→r46→r56 across leaders, incl. low-amplitude ones and w2), post it, then swarm done (re-search budget no longer needed if frontier holds).

## 2026-10-09 05:27 — wakeup 27 (final)
- r56 audit posted (20261009T052712.707Z_swarm-f_note_07a4): 55 entries, no sign flips, all PASS; corrected qmax note (conv46 shifts w3 frontier R by ±3.7%).
- swarm done. 30/500 charged.
