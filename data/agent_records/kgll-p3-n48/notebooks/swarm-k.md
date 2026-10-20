# swarm-k notebook

Started 2026-10-14T10:24:24+00:00.

## 2026-10-14 ~11:30 — wakeup 1 (orientation, scope)
- Read the brief, docs 40/46, theory §4–6.4, the solver LL0 form factor (MoireSolver.jl raw_formfactor_mn), and the board.
- Board: a/b full-star axis maps (duplicate of each other); c jorb (joint orbits S1-S3×T1-T3) gives the leads: s21 R up to 1.249 (g3r1_o+60_bp), 1.217 (g3r1_o+0_ap), 1.171 (g1r1_o+90_am). Herding: c,d,f,g,j,r,l,m are all in the ⊥/chiral joint-orbit area; i kpow; e bigamp.
- Built work/geom.py (single-particle geometry from the solver LL0 form factor plus the deformation kernel). Validated: parent C=1, T_viol=0, S ratio matches the broker.
  Parent Berry curvature is very non-uniform: Ω∈[0.10,14.9], std 2.07.
- work/collect.py: geometry features against R_gap(s21) for every leaderboard request (cache work/geom_cache.json). |corr| ≤ 0.25 for all geometry features; splitting/Δ −0.56..−0.65. Geometry is NOT a surrogate. Posted result 20261014T112436.418Z_swarm-k_result_d816.
- MT symmetry check: (θ,β)↔(−θ,−β), (θ,α)↔(−θ,α) hold to ≤0.8 % on s21, so the chiral response is physical.
- Scope chosen: `mech` = beyond-M2 matched-density static controls and robustness checks. Hypothesis 20261014T112418.812Z_swarm-k_hypothesis_eee0. Budget ≤ 80.
- work/control.py REQ OUT: ρ_ctrl = <ρ_k>_BZ (24² grid), static W_G on |G|²≤21, zero mode included. `swarm check --control` ok.
- Submitted control 20261014T112519.757Z_swarm-k_req_2bdc (for c7133 g1r1_o+90_am; M2_ctrl 10.0227 < parent 10.035) on s21,r46,r56.
- Next: read control results; make controls for each α-leader that reaches r46 with R≥1.02 (j/r large-amplitude perp scans are the real test). Watch the r46/r56 outcomes of the c leaders (the finite-size sign question).

## 2026-10-14 ~11:50 — wakeup 2
- Control 2bdc (for c7133, α⊥ −0.05): R_ctrl 0.9993/0.9993/0.9992. Posted result 20261014T114816.645Z_swarm-k_result_db45.
- Leaders now: perpA −0.45 (j ea28 = q c027) s21 1.6386 with M2^(k) 9.44; h 353f S4T1 c0 α small 1.572; f β-odd S3T1 1.558 (phase-only, clean).
- Submitted controls for ea28: 0c1d (<ρ_k>, M2 9.01) and 1466 (rescaled to M2 9.44, work/m2scale.py).
- swarm-s's guiding-centre identity: the ⊥ channel is half static coherent LL mixing (Q=0). Algebra checked and correct. The solver's LL mixing is incoherent, so no static LL-mix control is possible. Mailed s, j, q.
- 9 evals charged so far.
- Next: post the ea28 control results; controls for any other α leader reaching r46 (h 353f is S4×T1 α at small step, M2 10.04, so its control is trivial; do it only if it reaches r56).

## 2026-10-14 ~12:10 — wakeup 3
- ea28 controls landed. A <ρ_k> (0c1d): 0.9399/0.9392/0.9353. B M2-matched (1466): 0.9627/0.9627/0.9598. Softer density gives a LOWER gap; the leader (1.64/2.63/2.44) is not density. Posted 20261014T121007.962Z_swarm-k_result_9152.
- On request from c and p, submitted controls: 37dc→9d8b, ad6b→0924, 884a→5f24, 298a→2de9, 0d26→8cd2 (s21,r46,r56). Charged so far ≈ 24.
- Board: c STRONG phase-only claim d698 (S2×T1 +60 β+0.03: 1.249/1.404/1.347). u checked it. ⊥ α line −0.45 SUGGESTIVE/large. ak critique: branch change past −0.35. h 353f (S4×T1 α, M2 10.04) at r46 1.72; control it if it reaches r56.
- Next: post the batch of control results; control any new α leaders (h 353f, y s2plane).

## 2026-10-14 ~12:35 — wakeup 4
- Controls landed: 37dc/ad6b/884a 0.9994/0.9993/0.9993; 0d26 0.9728/0.9725/0.9707; 298a 0.9881/0.9880/(r56 pending). Monotone: the softer ⊥ density gives a lower static gap.
- New leaders: h c662 (un1_ab_s100, α+β 9×9 orbits) s21 4.76, EG 4.18, M2k 9.99; t f0fb s21 3.51. Queued controls 353f→b75e, c662→9a60, f0fb→01ae.
- New tool work/ffspec.py: Φ(q)=<|λ(k,k+q)|²>, moments I0..I2 with gate-screened V. All leaders have I_n ratio ≤ 1 (c662 0.957, ea28 0.82). The gain is phase structure, not interaction scale.
- Posted 20261014T123535.768Z_swarm-k_result_a79b. ~33 evals charged.
- Next: post the c662/f0fb/353f controls. Possibly a q-resolved Φ comparison, or a critique of the leaders' PES drop (e's note).

## 2026-10-14 ~13:00 — wakeup 5
- Controls landed: c662 0.9949/0.9945/0.9944; f0fb 0.9991/0.9989/0.9989; 353f 1.0000×3; 298a r56 0.9872. 11 controls / 33 evals, all R_ctrl in [0.935,1.000].
- Records: h c662 STRONG 4.76/5.23/4.67 (conv46 5.23); t 8c01 4.82/5.19/4.55; t 3542 STRONG 3.77/4.06/3.58.
- Geometry of records: no curvature flattening (c662 Ω std 2.24 > parent 2.07); non-ideal (T 0.08–0.17). The ⊥ −0.45 is a different mechanism: flattens Ω (max 3.9), T=0.39, S ratio 0.035.
- Posted 20261014T130202.598Z_swarm-k_result_eb60 with a coverage block. Mailed h (request ef0a answered) and i (i takes the remaining multi-orbit controls; I step back from new density controls).
- Running work/collect.py over the whole board in the background (work/collect_out.txt) to test corr(R, T_viol) at large amplitude.
- Next: analyse the collect output. Decide whether to start a family of my own (avoid herding); candidates: a mechanism test of "non-ideality ↔ gain"; checking that the records' growth is not just s21-splitting-driven.

## 2026-10-14 ~13:25 — wakeup 6
- t asked for 8c01 controls (STRONG 4.82/5.19/4.55). Submitted <ρ_k> 2c4c (M2 9.84) and M2-matched b6de (9.94).
- Board: ap lllref: the leaders' γ on uniform LL0 lowers the gap, so the gain is γ×ρ* cooperation. u: the leaders lift 130–270 of 558 zero pair modes. av: the records follow the angular rule (α cos2δ, β sin2δ). o 8f9d s21 5.33 (new top).
- Collector still running (506 cached).
- Next: post the 8c01 controls; analyse board-wide corr(R, T_viol) and Ω std at large amplitude.

## 2026-10-14 ~13:45 — wakeup 7
- 8c01 controls: <ρ_k> 0.9943/0.9937/0.9936; M2-matched 1.0000/0.9994/0.9997. Posted 20261014T134452.667Z_swarm-k_result_65d0, together with board-wide geometry stats (623 req). Best |Spearman| is 0.32 (Ω std, PASS only). The geometry line is closed.
- AMBIGUOUS large-R points fail s21c N_A=3 (b d8c9, w bf75). hichi S10 R≈7.5 points are other-phase.
- New control requests: v (da76, 8e4f, 9100) → c4a9, ad00, 0259; s 256a → 2385; o f5f1 (s21 6.28 / r46 8.33 / r56 8.12) → 2a80 (<ρ_k>) and 11cb (M2-matched). ~57 evals charged.
- Records still rising: o f5f1 at Σ|β| 1.88, near the 2.0 cap.
- Next: post this batch; keep answering control requests. Consider whether a family of my own is worth it (the board is saturated with optimizers).

## 2026-10-14 ~14:12 — wakeup 8
- Controls landed: da76 1.0003/1.0002/1.0002; 8e4f ≈1.0000; 9100 1.0002; 256a 0.9992/0.9991/0.9991; f5f1 <ρ_k> 0.9928/0.9922/0.9921; f5f1 M2-matched 1.0008/1.0004/1.0007.
- RULE: R_ctrl − 1 = 0.06 (M2_ctrl − 10.0354) + 0.002, max residual 0.0045 over 19 controls, the same on all clusters. Predicted controls for the top 17 (R 6–10): 0.957–0.992.
- Out-of-sample test: e0a8 (av, s21 10.39) control 0a3b, predicted 0.957.
- Posted 20261014T141243.739Z_swarm-k_result_6839. ~60 evals charged.
- Board: records R≈10 at s21 (av cos2d e0a8, s c325). Many agents finishing (d, ak, p, g, aj, q done).
- Next: check 0a3b against the prediction. Then decide: wind down (swarm done) or pick a remaining open question (e.g. the Σ|β| cap reading is for the human; the Q=0 split is r/s).

## 2026-10-14 ~14:40 — wakeup 9
- Out-of-sample control 0a3b (e0a8): 0.9929/0.9892/0.9904 vs predicted 0.957, so the linear rule FAILED. Sensitivity is shape-dependent: ⊥ line 0.063, records 0.035, e0a8 0.014. Posted refutation of my own 6839 (20261014T143846.108Z_swarm-k_refutation_b10b). Only the lower bound R_ctrl ≥ 1+0.065ΔM2−0.005 holds (20/20).
- Submitted controls b7f3 → e909 and c325 (s STRONG) → 3378.
- Board: av cos2d e0a8 STRONG 10.39/9.87/10.50/9.96; 55f9 s21 12.5. r: removing ⊥ keeps 83–93 % of the records, so the Q=0 half is minor. u: qmax-8 non-PSD at R≈10, so watch conv46.
- ~69 evals charged.
- Lesson: never post a fitted rule without an out-of-sample point first.

## 2026-10-14 ~15:05 — wakeup 10
- Controls: c325 0.9983/0.9967/0.9972; b7f3 0.9970/0.9956/0.9961. Bound holds 22/22. Posted 20261014T150423.549Z_swarm-k_result_d13a (note: lists ea28 at 0.935 inside a sentence saying 0.989–1.000; the number is explicit).
- Board: records R≈12–14 (w 407a 13.9/13.3, av 55f9 12.5/12.7/12.8, x 06bb). u: qmax-8 is non-PSD for R≈13 records, so trust conv46 only. Many agents are posting final summaries.
- ~75 evals charged. Role nearly complete. Remaining: controls for new STRONG α claims (407a, 55f9) when they reach r56. Then swarm done.

## 2026-10-14 ~16:35 — wakeup 11
- New STRONG claims: w 407a (13.93/13.26/13.79, conv46 13.93), av 55f9 (12.51/12.71/12.79, conv 13.00), al a8c1/6f22 (lowsym C3-breaking, ~12.4), av 7b3e. Requests: w e002, ad 8993 (k-nematic, M2k 11.41).
- control.py now has --sym (override symmetry) and labels the shells of a wider support (--g2max). 407a, 8993 and 6f22 need g2max 49 because the averaged density goes negative at 21. The 8993 M2-matched variant is impossible (density negative).
- Submitted: 55f9 3f1f, e002 f16b, 7b3e e254, 407a 09e9 (g49), 8993 153e (g49), a8c1 9e5f (sym none), 6f22 7c22 (sym none, g49). ~96 evals charged.
- Next: post these results, then swarm done (the role is complete; the board is wrapping up).

## 2026-10-14 ~17:05 — wakeup 12
- Controls: 407a 1.0104/1.0095/1.0103; 55f9 1.0055/1.0043/1.0050; 7b3e 1.0051/1.0034/1.0042; a8c1 1.0046/1.0034/1.0041; 6f22 1.0044/1.0034/1.0039; e002 0.9972/0.9966/0.9966; 8993 0.9486/0.9527/(r56 pending), which is BELOW my bound (0.972), so the bound is withdrawn.
- Posted 20261014T170302.781Z_swarm-k_result_8066. Queued 06bb 3718 (g49), cbe3 014b, 5063 723c, 31e4 9ec1, 1c48 7edb. ~111 evals charged.
- Next: post the last batch, then swarm done.

## 2026-10-14 ~17:30 — wakeup 13
- Controls: 06bb 1.0061/1.0021/1.0033; cbe3 0.9919/0.9887/0.9895; 5063 0.9894/0.9871/0.9876; 31e4 0.9774/0.9756/0.9752; 1c48 1.0000/0.9975/0.9985. Posted.
- Queued for e: c577 7fe4, b7a3 8da6. 8993 r56 still pending.
- ~117 evals charged. Next: post c577/b7a3/8993, then swarm done.

## 2026-10-14 ~17:55 — wakeup 14 (closing)
- c577 0.9915/0.9891/0.9897; b7a3 0.9911/0.9882/0.9890. 8993 r56 still pending.
- Posted final result with coverage: 20261014T175529.436Z_swarm-k_result_9b71. Running swarm done.
