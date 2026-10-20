# swarm-y notebook

Started 2026-10-14T10:25:14+00:00.

## 2026-10-14 ~11:28 — wakeup 1: scope chosen = `fsmatch` (finite-size-matched) + ladder audit
- Board: a/b map 60 axes (dup), c jorb orbits, d chiral half-shell phase, e bigamp, f chiral-odd joint β, g joint-orbit channels, i kpow, l phase-even.
- Leaders: swarm-c jorb at s21 +15..+25%, EVEN in sign of α and of β at |α|=0.05/|β|=0.03 (e.g. 37dc, ad6b, ce1f, c75e, d698) -> suspicious cluster-specific level effect; r46 pending.
- Measured (work/fsmatch.py): s21 has Γ,K,K' no M; r46 has Γ + 3 M (and T3 pair (2,0) aliased); r56 Γ + 1 M. F_T2 maxed at K (s21: two values only). F_T3 maxed at M.
- Designed KM = (5,4,3)/√50 (zero at K,M) and GK = (1,0,-1)/√2 (zero at Γ,K). Stage 1: S1-S3 × {KM,GK} × {α±0.05, β±0.03} = 24 evals submitted (work/fs1, ids 112802..112818).
- Hypothesis post 20261014T112800.834Z_swarm-y_hypothesis_6af5.
- Tools: work/pull.py pulls leaderboard ids + deformation + per-cluster R (reads ed_input via swarm show path).
- Next: read stage-1 results, compare with a/b single-T map at same amplitude; audit jorb r46/r56 when in.

## ~11:50 — wakeup 2
- WRONG premise retracted: jorb responses are linear (I compared different orbits with same diagonal matrix). Correction note 20261014T114936.960Z_swarm-y_note_0cdf; replied to swarm-p.
- Board: ~45 hypotheses, massive herding on S1/S2×T1 joint orbits; leaders ⊥ S1×T1 α to large amplitude R s21 1.6386 (swarm-r/j/q); transfers s21≈r46 (<1%) for single orbits (p, u audits). conv46 == r46 numerically for LL0 (swarm-l).
- swarm-k: matched-density control explains none of α⊥ gain. swarm-l: full-shell β at ±0.12 far outside Laughlin window. swarm-a: outer shells at 0.05 non-perturbative.
- My 24 stage-1 still queued (broker busy).
- Running work/audit.py (cross-cluster table + K/M weight of momentum profile).
- Audit #1 posted (20261014T115745.510Z_swarm-y_result_e222): S1 orbits transfer ≤1%; S2×T1 orbits r46 6–16% > s21, r56 between; ⊥ α −0.45 (j ea28) s21 1.64 vs r46 2.63; mesh-sampled M2(k) identical across clusters -> spread is kernel/many-body, not density sampling. Tools: work/audit.py (cache work/audit_cache.json), work/meshm2.py.
- New family s2plane (hyp 20261014T115854.748Z_swarm-y_hypothesis_b7c8): α = a_par·∥0 + a_e·(+60 + −60) in S2×T1 pair stars (work/gen_s2plane.py; matchings from swarm-c bc24). 15 evals submitted (work/s2p1, ids 115856..115909).
- Charged so far: 24 (fs1) + 15 (s2p1) = 39.
- Next: read fs1 and s2p1 results; refine s2plane around best cell; post fsmatch stage-1 result with coverage; ea28 r56 check.

## ~12:30 — wakeup 3
- fsmatch stage1 done: null (best 1.0137 S1 GK α−, 05ad); GK (T3-heavy) breaks manifold even at s21 → damage tracks |R| not point sampling. Abandon+coverage posted 20261014T123012.021Z_swarm-y_abandon_8466.
- Board: ea28 (⊥ α −0.45) r56 = 2.44 → s21 is the outlier (s21 manifold splitting binding, swarm-q/j). STRONG claims: swarm-c d698 (S2×T1 +60 β 0.03: 1.249/1.404/1.347), swarm-f 728b (S3×T1 chiral-odd β 0.05: 1.558/1.641/1.560). swarm-h S4T1 α contrast 1.572/1.720/1.614. PES entanglement gap drops for leaders (swarm-e).
- s2plane batch1 (15) still pending.

## ~13:00 — wakeup 4
- s2plane still queued (1h). Board frontier: multi-orbit α+β steps: h c662 STRONG 4.76/5.23/4.67 (s21/r46/r56), t 8c01 4.82/5.19; x 4-orbit sum 1.92/2.15/1.99; ae S2×T1 MT-odd β 0.03 1.687/1.989; j ⊥ α −0.45 STRONG 1.64/2.63/2.45.
- Mechanism: k (density controls <1), u (projected interaction moments flat), c (leaders restore w1c to smooth-static M2 law), g critique (d_sc, absolute Δ) refuted by p.
- Rerunning work/audit.py in background for updated cross-cluster table.
- audit.py too slow (swarm show per id); parse `swarm leaderboard` table directly instead (work/lb.txt + inline python).
- Audit #2 posted 20261014T132207.107Z_swarm-y_result_ccb3: 101 full-ladder reqs; Spearman ≥0.975; r56/r46 median 0.962; min cluster s21 46 / r46 10 / r56 45; r46 never binds R>1.5; one sign flip (g 1291). Top: h c662 4.76/5.23/4.67, t 8c01 4.82/5.19/4.55.
- s2plane still pending at 13:22.

## ~13:55 — wakeup 5
- s2plane b1 (s21): a_par 0.02 1.139, 0.035 1.220, 0.065 1.158, 0.1 FAIL; a_e −0.02 1.143, −0.035 1.154 (r46 1.238), ≤−0.05 FAIL; combos (a,−a): 0.025 1.410, 0.035 1.528, 0.05 1.619, 0.075 1.592; (0.05,−0.025) 1.566; (0.025,−0.05) 1.382. Best = contrast a_par=−a_e (cos2δ-like but ratio closer to 1:−1 than 1:−½). a_par stabilises the splitting that kills a_e alone.
- Refinement b2 submitted (6): (0.06,−0.06),(0.065,−0.045),(0.075,−0.05),(0.045,−0.06),(0.09,−0.09),(0.06,−0.035). Charged 45.
- Note posted: records' kernels exact at n_mesh 48 (work/meshconv.py).
- Board frontier: o f5f1 s21 6.28 / r46 8.33 / r56 8.12 at Σ|β|=1.88 (cap 2.0). Many STRONG claims. s21 lanes slow (stuck-lane reports).

## ~14:25 — wakeup 6
- s2plane promotions: (0.05,−0.05) 76ca s21 1.619 / r46 1.950; (0.075,−0.075) 7a27 1.592 / r46 2.393; (0.025,−0.05) c7c7 1.382/1.636; r56 pending. s21 underestimates at larger amplitude (splitting-limited) — same as ⊥ line.
- Board: cos2δ+i·sin2δ rule (av) s21 up to 10.4 at Σ|α| cap; records cap-limited (ae gate audit). Many agents finishing (p,q,g,ae,aj,d,ak done).
- Refinement b2 (6) still queued.

## ~14:57 — wakeup 7
- s2plane b2 s21: (0.045,−0.06) 1.512; (0.06,−0.035) 1.660; (0.06,−0.06) 1.634; (0.065,−0.045) 1.705; (0.075,−0.05) 1.731 e697; (0.09,−0.09) FAIL 1.48. Optimum ratio a_e/a_par → ≈ −0.67 at larger amplitude (near cos2δ ½…⅔).
- b3 along ratio ≈ −0.65: (0.085,−0.055),(0.095,−0.062),(0.11,−0.07),(0.1,−0.05) submitted. Charged 49.
- Board: av e0a8 STRONG 10.39/9.87/10.50 (conv46 9.96); s c325 noQ0 STRONG 9.87/10.15/9.54. Records cap-limited. u: qmax-8 makes pair interaction non-PSD for R≈10 (fixed at qmax 10).

## ~16:45 — wakeup 8
- s2plane b3: s21 plateau ~1.74 (04db 1.738/r46 2.293), r46 rises to 2.609 (0b19). Closed with coverage: 20261014T164125.542Z_swarm-y_result_a113. r56 pending for all — post follow-up note when in.
- Audit #3 posted: conv46/r46 shift 0 below R≈9 (163 pts), up to +20% at R 9–13 → qmax; r56 qmax-8 unconverged above R≈9.
- Board records: w 407a 13.93/13.26/13.79 (qmax not converged), h 5063 11.65/12.30/11.97, s 1c48 noQ0 11.21/11.67/11.60, e c577 11.42/11.59/11.38. Many agents done.
- Charged 49/500. Plan: wait for s2plane r56, post note, then likely `swarm done` (no unexplored direction worth budget; swarm saturated near caps).

## ~17:30 — wakeup 9: DONE
- s2plane r56 still pending (5h); will land in store. Board saturated at caps (records 11–14, many STRONG, density-controlled). No unexplored direction worth budget.
- `swarm done` posted with final summary (49/500 charged). Loop stopped.
