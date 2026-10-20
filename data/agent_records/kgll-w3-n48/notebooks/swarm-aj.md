# swarm-aj notebook

Started 2026-10-08T04:36:47+00:00.

## 2026-10-08 wakeup 1 (05:10–05:30 UTC)
Read: brief, docs 40/46, theory §2/§6.4, contract DeformationBlock (pair stars ok: any inversion-symmetric set), board (≈45 hypotheses).
Board state: leader = S1T1⊥ joint orbit (swarm-i fa76: s21 1.1885, r46 1.156; fb45 S2T1∥ 1.1785/1.171). swarm-h: w3 has exact half-cell
magnetic translation symmetry → only Z2xZ2-invariant products (m≡R2, n≡R1 mod 2) have true linear response; rest = cone + s21 twist artifacts.
Low and high shell orbits all claimed (e,i,z,ad,s,h,w,ah,ai,...). Static controls (swarm-ab mdctl): static M2k=3.812 → s21 1.0365 only.

My family `m2n-gc-w3` (hypothesis 20261008T052845.972Z_swarm-aj_hypothesis_8c40):
- work/orbits.py: 31 invariant C6 orbits; work/m2form.py: M2^(k) Hessian on them (20/31 negative eigenvalues; strong couplings via parent harmonics).
- work/dressed.py: gc-lock dressed by w_λ = 1 + λ ρ̃_w3. λ=−0.25 is M2-neutral (A=S1T1⊥ base keeps 0.87 overlap with pure S1T1⊥).
- Phase 1 submitted (22 reqs, work/p1/*.json, s21): A/B at λ∈{−0.25,+0.5,−0.6}, A+B, C=S2T2⊥ (λ=−0.25).
Comparison points (λ=0): swarm-i fa76 (orbit 0.15: 1.1885), b6a4 (0.05: 1.0597); swarm-e 56da (orbit 0.0866: 1.105).
Prediction: A λ=−0.25 α=0.2 ≈ R(S1T1⊥, 0.17) if locking (≈1.2); ≈1.0 if M2 law.
Next: read results; phase 2 = frontier optimization (R at M2^(k)/M2 ≤ 1, 1.25, 1.5); request matched-density control if positive.
Tools: work/board_table.py (slow: swarm show for every req; cache in work/show_cache.pkl).

## wakeup 2 (05:45)
A (S1T1⊥ base) results s21: λ=−0.25: α −0.1 0.872 (8759), +0.1 1.038 (85f1, M2k/M 1.0003, promoted), +0.2 0.969, +0.35 0.652, +0.5 FAIL.
λ=+0.5: 0.1 1.112 (5943), 0.2 1.083 (1b57, M2k/M 1.47). λ=−0.6: 0.1 0.758, 0.2 FAIL. AB λ=−0.25: 0.2 0.814, 0.35 FAIL.
Reading: linear slope survives M2-neutral dressing (~80%; trivially, since M2^(k) is 2nd-order for every γ), but high-shell
dressing adds strong negative curvature → pure orbits (λ=0) beat both dressings at finite α. Peak dressing (λ>0) does not help either.
Board: leaders now 1.4–1.57 s21 (au S2T1∥ to M2 edge; e/af plane ridge c⊥+c∥≈0.2, r46 1.41). b's rule-t1-w3 and d's dress-w3 overlap my dressing idea.
Next: wait for B, C; post result; decide phase 2 (probably small: λ∈[0,0.3] at α on the ridge, or close family).

## wakeup 3 (06:05)
Phase 1 complete. M2-neutral winners (all Z2-invariant): 85f1 A λ-.25 α.1 s21 1.038 r46 1.083 (M2k/M 1.0003);
8a4a B λ-.25 α.1 1.042/1.075 (0.9996); 85fb B λ-.25 α.2 1.033/1.143 (0.9984). r56 pending for these + 5943/0f33 (λ+.5 α.1).
λ=+0.5 α=.2 collapses at r46 (0.934, M2k 1.47). AB combos and C (S2T2⊥) negative.
Posted interim result 20261008T060301.790Z_swarm-aj_result_e91a.
Phase 2 submitted: work/p2 (12 reqs, λ∈{-.25,-.2,-.15}, α .1–.25, M2k/M 0.997–1.006).
Todo: when r56 lands on best M2-neutral point → `request` post for matched-density static control (swarm-p definition).
Critique candidate: swarm-j chidress-w3 claims s21 1.45→2.03 at β=0.015 — suspicious jump; check splitting/PES/r46.

## wakeup 4 (06:25)
Phase 2 results (s21 / r46 / M2k/M): ef7f B λ-.2 α.25 1.141/1.231/0.998 (best M2-neutral); ce12 B λ-.2 α.2 1.128/1.180/0.999;
a7d3 B λ-.15 α.2 1.180/1.197/1.006; 1593 B λ-.15 α.15 1.135/1.141; 670b A λ-.15 α.15 1.144/1.146/1.0055; 3832 A λ-.2 α.15 1.112/1.138/1.0006;
6e6d B λ-.2 α.15 1.107/1.130; 9594 B λ-.25 α.15 1.044/1.117; 412f B λ-.25 α.25 1.009; f650 A λ-.25 α.15 1.018.
→ steep λ dependence: λ=-0.25 too much high-shell content; -0.2 near optimum of M2-constrained frontier.
Dressed A and B at λ=-0.2 are anti-correlated (cos≈-0.36) → explains AB collapse in phase 1.
r56 stage stalled board-wide (swarm-c request). Phase 3 submitted (work/p3, 11): B λ∈{-.22,-.2,-.18} α .25–.35, A λ-.2 α .2/.25, AB mixes.
Request 20261008T062547.678Z_swarm-aj_request_0b97 (matched-density control on ef7f); mailed swarm-p.
Budget: 45 charged.

## wakeup 5 (06:50)
Phase 3 (s21/r46/M2k/M): bbfb B λ-.18 α.3 1.210/1.298/1.0015 (best M2-neutral so far); 779b B λ-.18 α.25 1.190/1.241;
f99a B λ-.2 α.35 1.141/1.274/0.996; a9c3 B λ-.2 α.3 1.145/1.261; b5d0 AB(.1,.2) 1.159/1.243/1.005; c430 A λ-.18 α.2 1.165/1.194.
R still rising with α at λ≈-0.18. r56 still stalled board-wide.
Board: swarm-t xfam-gp 3.3–4.2 (leader+neg high-shell α dressing+chiral β; M2k/M 1.72, R_beyondM2 1.3–1.7; gates clean, adm 0.61) —
checked, no critique. Chiral β (S4/S7/S9/S10×T1, +β on positive signed angle; j's ba1f = 0.026 per orbit) keeps M2k fixed.
Phase 4 submitted (work/p4, 10): bbfb base + chiral β {0.017,0.026,0.035,−0.026}, 779b+0.026, λ-.2 α.35+0.026; α push at λ-.18 (.35,.4), λ-.16 (.3,.35).
Budget 66 charged.

## wakeup 6 (07:10)
Matched-density control (swarm-ab b939, ⟨ρ_k⟩ of ef7f): s21 0.9911 r46 0.9911 vs ef7f 1.141/1.231 → amplitude gain fully k-dependence.
Phase 4: chiral β (all-four S4/S7/S9/S10×T1) on bbfb base (M2k/M 1.0015): χ.017 8be5 1.460/1.672; χ.026 f3b5 1.446/1.866;
χ.035 e713 1.333/1.966; χ−.026 e0c9 0.455 (odd). α pushes: a703 λ-.18 α.4 1.231/1.356; 538c λ-.16 α.35 1.302/1.372 (M2 1.012).
Posted result 20261008T071142.968Z_swarm-aj_result_45d2. Mailed ab for optional bbfb control.
Phase 5 submitted (work/p5, 7): χ .017–.022 at α .3–.5, single-orbit χS4 .05.
Budget ~62 charged. r56 still stalled. Plan: after phase 5, stop search unless a clear direction; wait for r56; final coverage post.

## wakeup 7 (07:33)
Phase 5 (s21/r46, M2k/M ~1.002–1.005): b480 λ-.18 α.5 χ.02 1.640/1.935; 61df α.4 χ.02 1.572/1.849; fc47 α.35 χ.022 1.527/1.846;
8382 α.35 χ.017 1.510/1.725; 7edb α.3 χ.021 1.467/1.765; 4006 λ-.2 α.45 χ.02 1.481/1.813; 794d χS4-only .05 1.458/1.564.
Still rising with α at fixed M2 → phase 6 (work/p6, 5): α .6/.7 at λ-.18, χ .02/.025; λ-.2 α.6 (M2 0.989); λ-.16 α.6 (1.037).
swarm-ab submitted bbfb avg control (M2 3.570). Board frontier: ap 3a0e 4.39/4.39 (Σ|α| 2.39); static saturates ~1.7 (as).

## wakeup 8 (07:53) — search closed
Phase 6: caf6 λ-.18 α.6 χ.025 1.719/2.139 (M2 1.008) best min; 1393 1.670/1.997; 3e38 α.7 1.661/2.030 (saturating);
0391 λ-.16 α.6 1.863/2.109 (M2 1.037); 9ccd λ-.2 α.6 1.471/1.855 (0.989).
Posted coverage/closing result 20261008T075347.324Z_swarm-aj_result_c6fb. 67 evals charged, 47 at r56 pending.
Now: reserve/waiting. Todo: when r56 lands, post short update (sign agreement for caf6, b480, bbfb, ef7f) + bbfb control result; then `swarm done`.

## wakeup 9 (08:24)
bbfb control 302c (swarm-ab) = 0.9874 s21/r46 → posted note. r56 still stalled. Most agents done.
Plan: wait (hourly) for r56; post sign-agreement update when it lands; then swarm done. If nothing by ~10:30, done anyway.

## wakeup 10 (09:30)
r56 still stalled (swarm-t request 61ea). Mailed swarm-af: their 2-orbit wedge has s21<1 at neutrality; my dressed T1 block gives s21 1.21 (bbfb). Next: one more hourly wait, then done.

## wakeup 11 (10:31) — DONE
r56 still stalled; posted swarm done with summary (work/done.md). Loop stopped.
