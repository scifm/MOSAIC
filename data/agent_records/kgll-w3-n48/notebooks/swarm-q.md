# swarm-q notebook

Started 2026-10-08T04:35:32+00:00.

## Wakeup 1 — 2026-10-08 ~05:10Z
- Read board: w3 heavily covered (atlases b/c/f/g, joint orbits e/i, Hessian d, global sobol o, z2-w3 h, chiral-β j, parent-shaped k, nematic k, c3break r). w2: atlas (a), joint orbits (m).
- Insight: w2 harmonics all have m+n≡0 mod 3 → exact Z3 magnetic translation τ=(a1+a2)/3 ↔ k→k+K, K=(G2−G1)/3 = (1/3,−1/3) frac.
  Pair product e^{iGr}e^{iRk} phase e^{−2πi[(m+n)+(R2−R1)]/3}. Invariant sector: {S2,S5,S6,S10}×T2.
  Verified S00(k±K)=S00(k) to 1e-16 in invariant sector (work/z3check.py). s21 mesh (5j mod 21, j)/21 contains K (j=14); r46/r56 don't.
  Selection rule: zero linear R response on s21/TL for S_inv×{T1,T3}, S_noninv×T2 (all orbits). Test vs swarm-a atlas when it lands.
- Posted hypothesis 20261008T050859.043Z_swarm-q_hypothesis_319d (family z3-w2, ≤160 evals).
- Submitted phase 1: 42 reqs (work/inputs/p1): S5,S6×T2 orbits α,β ±0.1; S10×T2 6 orbits α±0.1; sep S2,S5,S6×T2 α±0.3.
- Mailed swarm-m (overlap + selection-rule prediction for their blocks).
- Tools: work/stars.py (stars, joint_orbits), work/build.py (block_from_terms, orbit_terms, star_term, make_input).
- Next: collect p1; check selection rule vs swarm-a atlas (S2,S5,S6,S10×T1/T3; S1,S3,..×T2 ±0.1 pairs); post result; phase 2 line search / CMA in invariant sector.

## Wakeup 2 — 2026-10-08 ~05:30Z
- Phase 1 landed: fully Z3-invariant w2 sector all negative (best 0.927 S6T2 θ=+30 α+0.1, bd01); invariant odd parts ≤2%; β 0.1 → 0.43–0.59; α=0.3 sep S5/S6×T2 FAIL.
- Posted result 20261008T053210.010Z_swarm-q_result_4984 (closes fully invariant sector, coverage block).
- Board: 4 agents posted z3-w2 at once (q,u,v,x); v ceded to me. swarm-w critique: invariance = sum (m+n)+(R2−R1)≡0 — half-invariant blocks (S1T1,S3T1) can have slopes (consistent with what I wrote). swarm-m confirms selection rule; w2 leader S3T1⊥ (ba45: s21 1.062, r46 1.159).
- swarm-d: ideality defect D explains 72% of w2 variance (R−1 ≈ −2.7D). w3 leaders S1T1⊥, S2T1∥ (s21 up to 1.36).
- NEXT family idea: D-penalised orbit-resolved surrogate on w2: R−1 = Σ g_o a_o + Σ h_o b_o − λ D(x); fit to all public w2 s21 data; optimum x* ∝ Q^{-1} g (Q = Hessian of D in orbit subspace); line-scan with free promotion.
  Code: work/feat.py (D, M2k; static D=0 checked, quadratic, β weighs 4× α), work/model.py (orbit coords via pair-product basis), work/harvest.py (cache swarm show → work/cache).
- Note: other agents' processes visible via ps on the shared node — not reading their files (independence).

## Wakeup 3 — 2026-10-08 ~06:10Z
- Harvested 948 public requests (work/cache, 21 min; swarm show slow under load). D-penalised w2 model: R²=0.67 (D-only 0.64), lam≈2.7.
  swarm-d refuted D as a cost model far from parent (cutting D 4.7× dropped 1.36→1.03) → dropped the D-surrogate plan.
- Board state: w3 frontier s21 up to 2.48 (swarm-t GP, chiral-β dressing of S1T1⊥/S2T1∥ by j/am); no r56 results anywhere yet.
  w2 frontier: swarm-m d43f s21 1.161 (S1T1±30 α=−0.198 + S3T1⊥ 0.14); ff48 r46 1.22. Chiral β S7×T1 ±43.9° on w2 (ah d734 r46 1.269).
  w2 chiral-β herding (ah, an, aq, av); swarm-g's offset sign rule self-refuted.
- NEW family cma-w2 (hyp 20261008T060939.116Z_swarm-q_hypothesis_9a50, ≤200 evals): 10-D CMA-ES (work/cma_w2.py, state work/cma_w2/state.json).
  Coords: α sym S1T1±30, S3T1 90, S3T1±30, S4T1 ±10.9/±49.1/±70.9; chiral β S7T1 ±43.9/±16.1, S4T1 ±10.9, S3T1 ±30. Scales α .05, β .015. Mean0 = d43f + β S7(44) 0.03. Fitness s21 (FAIL→0).
  gen 0 submitted (12). Run `uv run ... python work/cma_w2.py step` each wakeup (waits until all landed).
- Mailed swarm-m, swarm-b, swarm-n about cma-w2.
- Note: `pkill -f work/fit_w2.py` killed my own shell — don't pkill by pattern matching my command.

## Wakeup 4 — 2026-10-08 ~06:30Z
- cma-w2 gen0: best d322 s21 1.239 (adds S4T1±11 α +0.069, S3T1±30 +0.024, S4 49/71 small; β S7 0.030). fs: 1.239,1.201,1.172,1.163,... 2 FAIL. σ→0.92. gen1 submitted.
- swarm-b chidress-w2 closed: 8c39 = d43f + S7χ44 β 0.0495 → s21 1.299 / r46 1.343 (w2 best). Probe submitted: d322 with β=0.0495 (req 803e).
- r56 stalled for EVERYONE (incl. parent baselines) — swarm-c asked human. Many agents now in reserve/verifier mode (a, u, w, x, at).
- swarm-ar slopes (mail): S4T1 10.9/49.1/70.9: +0.138/−0.093/+0.059; S7T1 43.9/76.1 α −0.087/−0.066; S8T1 90/30 −0.115/−0.074; S9T1 53.4/66.6 +0.077/+0.057. Note S4_49 slope negative but CMA mean drifted +.
- swarm-ai w2-fgrad covers off-set directions at ff48 (S1 30−150 chiral α etc.).

## Wakeup 5 — 2026-10-08 ~06:50Z
- probe 803e (d322 + β S7 0.0495): s21 1.277, r46 1.379 (vs 8c39 1.299/1.343). S4 α additive in r46 but not s21.
- cma gen1 best ee05 1.266; mean β_S7 → 0.047; σ 0.88. gen2 submitted.
- swarm-ai: off-plane gradient at ff48 nearly stationary; consistent (s21&r46) positive: chiral β S1T1 30−150 (+0.87/+1.31), S4T1 49−131 chiral... (not in my CMA set).
- swarm-aq: w2 Z3-breaking half has no linear r46 term; s21→r46 split is EVEN (s21 −, r46 +). swarm-m: w2 leaders E=R/R_static(M2k)=1.08-1.10 at s21.
- Many agents → reserve. r56 still pending everywhere.

## Wakeup 6 — 2026-10-08 ~07:10Z
- cma gen2 best 1370 s21 1.3062 (new w2 s21 best, > 8c39 1.299); 3/12 FAIL (edge near). gen3 submitted. mean: S4 α ±11 & ±71 ~0.08, β S7 0.054.
- swarm-v withdrew odd-artifact claim: w2 s21→r46 excess is EVEN (aq/an controls). Several agents done (v, ak, g, i, ao).

## Wakeup 7 — 2026-10-08 ~07:30Z
- Run 1 gen3 regressed (best cf75 1.238). KEY: 1370 (s21 1.306) has r46 1.103 → s21-only fitness non-robust. Run 1 stopped after gen4 (gen4 in flight; do NOT step run 1 further, just record).
- swarm-ai 0e27: s21 1.3248 / r46 1.4311 = 8c39 + step on S8T1±30, S9T1±66.6, S4T1±11 α (0.0283/orbit), chiral β S1T1±30, S4T1±49 (0.0141).
- Run 2: work/cma_w2b.py (state work/cma_w2b/state.json), 15-D, mean = 0e27, σ0 0.5, seed 20261109+gen, fitness min(s21, r46) (waits for promotions). gen0 submitted.
- Posted note 20261008T073149.854Z_swarm-q_note_df23; mailed swarm-ai.
- Many agents done/reserve. r56 still stalled for everyone.
- Each wakeup: `uv run --project "$MOIRE_MAIN" --no-sync python work/cma_w2b.py step`

## Wakeup 8 — 2026-10-08 ~08:00Z
- run2 gen0 best 15ef min 1.316 (all 12 PASS, range 1.18–1.32); σ 0.46; gen1 submitted. Mean drifts: S8/S9 α ~0.04, β S4T1_49 0.022.
- swarm-ai: λ·0e27 scale line: λ=1.2 → 37e1 s21 1.371/r46 1.350 (min 1.35); λ≥1.4 manifold FAIL. Keep step ≲1.3× 0e27 norm.
- w3 frontier: ap 4547 s21 5.20 / r46 5.41 (Σ|α| box edge); swarm-c critiques chart L1 inflation. Static M2 saturates ~1.7.
- swarm-aq: w2 r46 parent on a soft level (+5% saturating lift for ANY small T1 deformation) — r46 w2 numbers partly artifact.

## Wakeup 9 — 2026-10-08 ~08:25Z
- run2 gen1 best 92f0 min(s21,r46) 1.370 (> ai 37e1 1.350 = closing w2 best of w2-fgrad). σ 0.45. gen2 submitted. Mean: S3T1⊥ 0.167, β S7 0.058.
- Many agents done (m, ai, b, h, p, r, ac, as, av, aa...). aq: w2 r46 soft-level bonus is w2-specific (none on w3).

## Wakeup 10 — 2026-10-08 ~08:52Z
- run2 gen2 best 0d4c min 1.396 (all PASS, 1.16–1.40); σ 0.43; gen3 submitted. r56 still stalled. Most agents done.

## Wakeup 11 — 2026-10-08 ~09:20Z
- run2 gen3 best 356e min 1.408; σ 0.44; gen4 submitted. Slowing (+0.012/gen). Board quiet; r56 still stalled.

## Wakeup 12 — 2026-10-08 ~09:50Z
- run2 gen4 regressed: best a5a3 1.391, 4 FAIL. Plateau ~1.40 at manifold cliff. gen5 submitted (last).
- swarm-au critique: min(s21,r46) optimisation can fit the cluster split; r56 held-out. Accept.
- PLAN: after gen5 lands → stop CMA, post result+coverage for cma-w2 (run1+run2+probe), keep remaining budget in reserve for r56 checks.
- w3 frontier ap 0328 s21 6.66 / r46 7.11. r56 still zero results (swarm-t request).

## Wakeup 13 — 2026-10-08 ~10:17Z
- run2 gen5: best 69be 1.401, 5 FAIL → plateau. CMA stopped (do not step again).
- Posted result 20261008T101652.604Z_swarm-q_result_8379 (cma-w2 closed, coverage: 133 req, 114/0/19). Best 356e s21 1.4078 / r46 1.4391, r56 pending.
- Budget 175/500. Now WAITING: watch r56 for 356e (and 0d4c, 69be, 92f0). If 356e passes r56 with R>1 → request matched-density static control (α≠0, M2k/M2 1.11).
- No new family planned unless the board opens a gap.
- 11:08Z wait: r56 still stalled (356e SUBMITTED). w3 frontier ap 28b8 s21 8.86/r46 9.39.
- 12:09Z wait: r56 still stalled ~6h. ap closed tl-grad-w3 (077d s21 11.27/r46 10.54).
- 13:11Z conditioning audit posted (worst ratio w3 0.73, w2 0.67). r56 still stalled. w2 top-12 all mine.
- 13:37Z wait: r56 still stalled; board quiet.
- 14:38Z DONE: swarm done posted (175/500). Loop stopped.
