# ctrl-a notebook

Started 2026-10-14T05:20:47+00:00.

## 2026-10-14 05:26 — wakeup 1: orientation + axis screen launched
- Read brief, ADR-0040, progress/40, 46, theory §6.4. Parent w1c s21 Δ = 2.2586e-4 (PASS).
- Tools: `work/mk.py` builds inputs (stars S1..S10 by |G|² in 120° basis; T1..T3 by |R|² in 60° basis);
  `make([(S,T,alpha,beta),...], path)`. Block is separable: γ = Σ(α/2+iβ) O_s(r)F_p(k), real cos star fns.
- swarm check prints m2k_max_ratio = max M2^(k)/M2 (limit 3). α=0.1 on S1: 0.998; on S7/S9/S10: ~1.03.
- Hypothesis posted (family `axis`, 88 evals): S1..S6×T1..T3 α=±0.10, β=±0.05; S7..S10×T1 same.
- Submitted batch q1 (32): S1..S5×T1..T3 α± + S1T1 β±. ids in work/q1_ids.txt.
- Remaining axis inputs: work/axis_a (S6, S7-10), work/axis_b (all except S1T1).
- Next: collect, submit rest of axis (56), then build local model.

## 05:30–06:00 — axis screen results, first ladder outcomes, CMA started
- Axis (q1–q3, 87 evals): T1 directions negative; S4–S6 negative even at ±0.02 (±0.10 breaks manifold);
  α=±0.1 on S2+ fails manifold. Positive directions (s21): S1T3 β−.05 1.019, S1T3 α+.1 1.018,
  S1T2 α+.1 1.015, S2T2 α+.04 1.015, S2T3 α+.04 1.023, S3T2 α+.02 1.013, S3T3 α±.02 ~1.01-1.013, S3T3 β±.01 ~1.012.
  Not additive in general (S1T2+S1T3 α .1 → 0.970), but 0728 (S1T3 β−.05 + S3T2 α+.02) = 1.032 > both.
- Parent is fragile: Δ_parent/Δ_LLL = 1.24 at s21 despite M2=10 (R_staticM2 ≈ 0.126).
- Ladder: 0728 s21 1.032 / r46 1.040 / r56 1.018 all PASS → "suggestive". 0948 (S2T3 α.04) r46 1.046, r56 0.996 → sign flip.
  r56 runs slower (~15 min queue).
- cma1: own CMA-ES (work/cmaes.py, state work/cma_c1/state.json), 12-D S1-3×T2/T3 α/β, λ=12, mean at 0728.
  gen0 best 1.0385 (9bad), gen1 best 1.0543 (2a42), 1.0494 (47dd). Loop gens 2-4 in background
  (work/cma_loop.sh c1 cma1 3, log work/cma_c1/loop_g2-4.log).
- Tools: work/promo.py lists promoted requests with per-cluster R; work/wait_ids.py waits on an ids file.
- Next: watch r46/r56 transfer of CMA winners; if s21 overfits, consider robust objective (needs promotions).

## 06:06 — wakeup 2
- cma1 gens 2-4: best s21 1.0507/1.0553/1.0623 (d525), median rising to 1.030; σ 0.575. Mean drifting to
  S1T2 α −0.05, S1T3 α +0.054, S1T3 β −0.057, S2T2 α +0.013, S3T2 α +0.016.
- Ladder: 9bad (gen0) s21 1.0385 / r46 1.0554 / r56 1.0365 all PASS → suggestive, best min so far.
  acbc r56 0.9994 (flip). 2a42 s21 1.054 but r46 0.756 (!); 6777 s21 1.051 r46 0.954. Transfer noisy.
- Launched gens 5-7 (log work/cma_c1/loop_g5-7.log). 117 charged before this.

## 06:22 — wakeup 3: cma1 overfits s21 → robust cma2
- cma1 gens 5-7: best s21 1.0315/1.0428/1.0477, stagnating ~1.05-1.06. 96 evals total (gens 0-7).
- Transfer analysis: s21 winners with S1T2α ≲ −0.05 & S1T3α ≳ +0.05 collapse at r46 (d525 .949, f3e0 .844,
  1541 .432, 2a42 .756, 6777 .954; all PASS → gap collapse). Good transferers keep S1T2α≈0:
  9bad 1.039/1.055/1.037; 241c 1.030/1.040/1.029; 1930 1.049/1.051/1.018; 93a2 1.055/1.040/1.011; e302 r56 1.004.
  Hypothesis: T3 = 2·T1 aliases on 4×6 sub-mesh.
- cmaes.py: cfg "robust": true → f = min(s21, r46[, r56 if landed]); waits for r46 when s21 ≥ 1.02.
- cma2 launched: x0 = 9bad coefs, σ0 .5, seed 23, gens 0-3 in bg (work/cma_c2/loop_g0-3.log).
- Posted: hypothesis cma2 (112e; its --ref is a wrong id, ignore), axis result+coverage (76dc).
- TODO: post cma1 result+coverage once its r56 promotions land. Ask human for matched-density control
  for the best amplitude candidate once one is chosen.

## 06:45 — wakeup 4: ROBUST POSITIVE (cac1)
- cac1 (20261014T055037.062Z_ctrl-a_req_cac1, cma1 gen2 #10): s21 1.0293 / r46 1.0546 / r56 1.0532 / conv46 1.0546,
  all PASS, Chern 1. Broker claim = robust_positive. Has α≠0 → needs matched-density control.
  M2_k 10.0344 < parent 10.0354.
- Posted claim 994d, request dd90 (to human: which matched density? default proposal ⟨|h_k|²/S_k⟩_BZ).
- Other cma1 transfer: dc65 1.040/1.055/1.025, e527 1.032/1.049/1.020, 497a 1.030/1.036/1.023; bfa8 r46 .770.
- cma2 gen0: best robust 1.0459; 7559 (s21 1.046, r46 1.053) and 31d4 (1.046/1.059) waiting on r56.
  b9be r46 .715, baa3 .951, 54d3 .992 (overfit cases even near 9bad).
- Launched cma3 = phase-only robust CMA (9-D β S1-3×T1-3), λ 10, gens 0-3 (work/cma_c3).
- 177 charged at start of this tick.
- Next: post cma1 result+coverage once its last r56 land; watch cma2/cma3; push toward ≥1.10 (strong).

## 07:12 — wakeup 5
- 231 charged. cma2 gens 0-2 done (best min(s21,r46) 1.0487; 612d 1.049/1.056, 6255 1.048/1.058 await r56).
  cma3 (phase-only) gen1: 4466 s21 1.046 / r46 1.062 (r56 pending): candidate clean beyond-M2.
- r56 landed for 23 requests: only cac1 ≥ 1.05; r56 systematically < r46. corr(r56,s21) = −0.34,
  corr(r56,r46) = +0.45 (n=21). r56 likes S2T3α<0, S2T2β>0, S1T2α less negative, S2T3β>0.
- Changed objective: work/cma_<run>/r56.flag → score() also waits for r56 when r46 promotes (≥1.0, not FAIL).
  Flags set for c2, c3 (takes effect from the next tell). Generations will be slower (r56 queue).
- Loops: c2 runs gens 0-3, c3 gens 0-3; restart after they end (work/cma_loop.sh RUN FAM N).
- TODO: cma1 result+coverage once 3640/4507 r56 land.

## 07:39 — wakeup 6
- 241 charged. r56 backlog ~25 (~4 min each). Withdrew 13 told requests with r46 < 1.04 (their r56 to the back).
- New r56: c935 1.036/1.060/1.042, bf3e 1.035/1.044/1.034, 8bc8 1.042/1.063/1.017, 31d4 r56 1.014, 7559 1.009.
- cma2 restarted for gens 4-9 with r56 objective (log work/cma_c2/loop_g4-9.log). cma3 gen 3 tell in progress.
- Posted cma1 result+coverage ec15 (+ count correction note).
- Awaiting r56: 4466 (β-only, r46 1.062), 8feb (cma3, 1.057), 2704 (cma2, r46 1.0675), 6255, 612d, 4480, 5d72, dcfd.

## 08:11–08:30 — wakeup 7
- r56: 4466 (β-only) 1.046/1.062/1.018 → suggestive, clean beyond-M2 but < 1.05. 00b9 1.044/1.061/1.023,
  6255 r56 1.013, 612d 1.015, 8bc8 1.017, c935 1.042. Only cac1 ≥ 1.05 at r56 still.
- q4 (axis, 12): S4–S6 × T2/T3 α ±0.01 → 0.987–1.014 (T2 +α and T3 both signs positive, like S1–S3).
- sharpen family (28): best 1.0115 (log ρ T2 ε+.02); ρ template breaks manifold. Abandon posted a9dd.
- r56 lane very slow (~2-3 landings / 30 min, shared). Scorer now withdraws a point and skips r56 when r46 < 1.035.
- Restarted loops with a pending tell: cma_loop.sh RUN FAM N [IDS_TO_TELL]; PIDs in work/cma_<run>/loop.pid.
  NEVER pkill -f (matched my own shell and the process list shows other agents' processes → note c4b8 posted).
- cma3 gen3 told: best 1.0227, σ .80 (phase-only not improving much beyond 4466).
- 281 charged approx. Next: watch c2/c3; consider local refinement around cac1 (r56 1.053) with small σ.

## 08:56 — wakeup 8
- 291 charged. f84d (cma2 gen4) r46 1.0546 / r56 1.0525 → conv46 pending: likely 2nd robust positive.
- Other r56: 9a63 1.021, 00b9 1.023, a973 1.020, c106 1.005, 8778 0.995; cma3 a5b0 1.003, e157 1.008.
- Top-r56 pattern: S1T3α ≈ +.025–.03, S3T2α ≈ +.02–.026, S2T2β > 0, |S1T2α| small. Losers: big |S1T2α| or S1T3α≈0.
- c2 gen04 tell still waiting on r56 (lane ~10/30min, 23 queued incl. 13 withdrawn).
- No reply yet on control request dd90.

## 09:24 — wakeup 9
- Both nohup'd loops had DIED (unknown cause; nothing charged since 291). Restarted as harness-tracked
  background tasks (b5b6oigxn: c2 4 gens from gen04 tell; b380bpc4q: c3 3 gens from gen04 tell).
- f84d robust_positive confirmed (conv46 1.0546). Claim posted. Different point from cac1 (S1T2α −0.071, S3T2α +0.045).
- r46 gaps of cac1 & f84d equal to 2e-5 rel; many r46 ≈ 1.050–1.056 → possible deformation-insensitive ceiling at 4×6.

## 09:57 — wakeup 10
- r56 lane nearly stalled (19 queued). gen04 tells were stuck on f750/a1f8 r56.
- Scorer: r56 wait only if r46 ≥ 1.045 (else withdraw); objective for promoted = min(r46, r56) (s21 is a gate);
  unpromoted = s21 − 0.05. Note posted. Killed old loops by PID (loop.pid + children), restarted as tracked
  bg tasks bkq00tbso (c2, 4 gens) and b777d21qs (c3, 3 gens). Gen 4 told: c2 best 1.0315, c3 best 1.0244.
- 02a6 (cma2) 1.031/1.046/1.039; d7be (cma3 β-only) 1.039/1.045/1.017.

## 10:29 — wakeup 11
- 333 charged. cma3 (phase-only) gen5 best 1.0404, gen6 best 0.975; mean drifted (S1T3β −0.072). Let gen7 finish.
- Phase-only best transfer: 8feb 1.028/1.057/1.040 (suggestive, clean beyond-M2); a1f8 1.024/1.044/1.026.
- Started cma4: phase-only local refine around 8feb, σ .4, λ 8, 5 gens (bg task bj10vfrkk). Hyp 0b8a.
- c2 gen 5 tell in progress (bg bkq00tbso). Budget plan: c2 ≤36 more, c3 10, c4 40 → ~420; reserve ~80.
- cma3 closed, result posted. 8feb best phase-only.

## 11:10 — wakeup 12
- 353 charged. New robust positives: 6b04 (cma2 g5) 1.024/1.067/1.061/1.067 — best; 4480 1.023/1.056/1.054/1.056.
  Claim posted. Now 4 robust positives (cac1, f84d, 4480, 6b04).
- cma2 mean → S1T2α −0.098, S3T2α +0.049, S1T3β −0.058. Gen 6 best 1.030 (σ .62).
- cma4 gen0 submitted, waiting on promotions.

## 11:45 — wakeup 13
- 385 charged. cma2 g7 best 1.0415 (median .94; mean S1T2α −0.109 — risky); g8 is the last of that loop.
- cma4 g0 best 1.0447 (σ .36); g1 submitted.
- Plan: after cma2 g8 → c5 = local refine around 6b04 (σ .3, λ 8, 4 gens = 32). Reserve ~25 for controls.
- promo.py is slow (>2 min); use with timeout or run in bg.

## 12:16 — wakeup 14
- 385 charged; c2 g8 tell + c4 g1 tell waiting on promotions.
- Started cma5: refine around 6b04, σ .3, λ 8, 4 gens (bg bdlxvxjuz), hyp 0f13. Budget after: ~441, reserve ~59.

## 12:47 — wakeup 15
- 401 charged. cma5 g0 (σ .3 around 6b04): all 8 ≤ 0.994 — mostly s21 fell below the 1.02 gate
  (s21 0.986–1.018; 6b04 itself at 1.024), bdf2 promoted then r46 0.994. 6b04 sits at the s21 gate edge.
- Matched-density controls (work/matched_density.py; W̄ = <W(k,k)>/<W0>): W̄ ≈ parent to ≤ 3e-4/shell.
  Submitted --control s21,r46,r56: 4f3f (6b04), a2ec (cac1). Note posted. Files work/ctrl/.
- cma2 closed; result posted.

## 13:20 — wakeup 16
- 415 charged. Controls landed: 6b04-ctrl R 1.0003 on s21/r46/r56; cac1-ctrl 1.00003. Result posted (beyond averaged density).
- cma4 g1 best 1.0428 (phase-only, σ .36); cma5 g1 pending.
- Submitted controls b090 (f84d, M2(W̄) 10.019) and 97fc (4480, M2(W̄) 10.057). ~421 charged after these.

## 13:27 — wakeup 17 (session restarted; loops had been stopped)
- 421 charged, 2 in flight (controls b090/97fc). Resumed cma4 (tell g2 + 2 gens; bg blna8xfyl) and
  cma5 (tell g1 + 2 gens; bg bv0p86xp6). Expected end ~453 charged.
- Remaining to do: controls b090/97fc results post; cma4 + cma5 results/coverage; axis q4 addendum in final;
  then `swarm done` with summary.
- 13:58: controls f84d 1.0000/0.9999/1.0000, 4480 1.0004 ×3. Result posted. Loops waiting on promotions.

## 14:29 — wakeup 18
- 421 charged, r56 lane stalled (~40 queued). Withdrew all 29 told cma1–3 requests still queued for r56.
- Promising pending at r56: cma4 (phase-only) 927f r46 1.063, 8c83 1.0605, 106d 1.055, 5b84 1.045, d07a 1.043;
  cma5 38c6 r46 1.059, 6391 1.051.

## 14:59 — wakeup 19
- 429 charged, 8 in flight. cma5 g1 told (best 1.0516 = 38c6). 38c6: 1.0286/1.0590/1.0516/conv46 1.0590 → 5th robust positive
  (neighbourhood of 6b04). 6391 1.028/1.051/1.047; ad4a 1.036/1.060/1.032.
- cma4 phase-only r56: 8c83 1.040, 106d 1.030, bb8c 1.022, 04ef 1.014, d0d1 1.000. 927f pending. Phase-only tops out ≈1.04 at r56.

## 15:31 — wakeup 20
- 437 charged (+8 cma6 g0 = 445). 927f phase-only 1.026/1.063/1.041 (best phase-only; still suggestive).
- cma4 g2 told (best 1.0414), g3/g4 to go. cma5 g2 tell pending, g3 to go.
- Started cma6: 18-D (cma2 dims + S4–S6×T2/T3 α, scale .005), x0 6b04, σ .4, λ 8, 4 gens (g0 submitted; loop tells g0 then 3 gens).
  Budget plan: 445 + c4 8 + c5 8 + c6 24 = 485. Then final posts + swarm done.
- 16:03: 453 charged. cma4 g3 best 1.0408 (g4 submitted). cma5 g2 / cma6 g0 tells waiting on promotions.
- cma4 closed; result posted.
- 16:34: 461 charged, 8 in flight. cma5 g2 best 1.0502 (g3 = last, submitted). cma6 g0 tell waiting.
- 17:05: 469 charged (incl. in-flight). cma6 g0: 10ab 1.022/1.061/1.055 (conv46 pending) — outer-star comps ≤ .004, gain from S1–S3 part. cma5 g3 + cma6 g1 in flight.

## 17:29 — wakeup 21 (session restarted again)
- 469 charged. Resumed: cma5 final tell of g3 (bs4car1nn); cma6 tell g1 + gens 2,3 (bpohmietm) → ~485.
- 17:59: 469 charged. Waiting on r56 for cma5 g3 (17ef r46 1.061, 5ea5 1.060, db62 1.060, 6257, ffd9) and cma6 g1 (fe4a 1.052, cded, 9697). Lane queue 34.
- cma5 closed; result posted (38c6, ebac robust; db62 conv46 pending; 10ab robust confirmed conv46 1.061).
- 18:31: 477 charged. cma6 g1 best 1.0523; g2 submitted, g3 last → 485.
- 18:5x: cma6 closed (485 charged). db62 robust confirmed (conv46 1.0596), fe4a robust. Next: final summary + swarm done.

## 18:54 — FINAL
- 485/500 charged. 9 robust positives (6b04 best: 1.0242/1.0666/1.0609/1.0666), 0 strong, phase-only best 927f (suggestive).
- Controls: averaged-density static controls at R 0.9999–1.0004 → gain beyond averaged density.
- Final summary result 1ea8 (+ exact counts note a6d1: s21 460 PASS / 0 AMB / 55 FAIL over 515 search requests).
- swarm done issued. Loop stopped.
