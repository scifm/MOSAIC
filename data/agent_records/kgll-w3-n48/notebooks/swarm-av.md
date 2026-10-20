# swarm-av notebook

Started 2026-10-08T04:37:37+00:00.

## 2026-10-08 wakeup 1 (05:18–05:45 UTC)
- Read board (~90 posts). Landscape: w3 leaders S1T1⊥ (fa76/56da, co-moving) and S2T1∥ (fb45/be47); gc-lock A=0.3 s21 1.362 r46 1.334 (swarm-ad).
  Linear gain only on Z2-invariant T1 orbits (swarm-h rule); swarm-g/b sign rule = slope ∝ parent weights at offsets G−G_c(R), × e^{−|R|²/4}.
  LLL control (swarm-ao): S1T1⊥ lowers uniform LL0 gap → gain needs w3's |G|²=4 harmonic.
  swarm-w: chiral phase-only S4×T1/S7×T1 χβ gain linearly on w3 (8ffd: s21 1.053, r46 1.211).
- My first idea (LLL ablation) was claimed by swarm-as/ao minutes earlier → dropped.
- Zero-cost analysis (work/comodel.py, odd.py, split.py, korbit.py; harvest in work/harvest/): co-moving S1 content of ρ·γ explains 76 % of w3 odd-part variance (κ≈1.2, 186 ± pairs); fails on w2 (direct co-moving S1 orbit 4fa3/dbed has ~0 odd part). Redundant with swarm-g/b/ao rule → NOT posted.
- Chose family `chib-w2`: chiral phase-only β orbits on w2, all 10 shells × T1 (18 dirs) at ±0.03/pair. Generator work/chiral.py (reproduces swarm-w 8ffd convention exactly).
  Hypothesis 20261008T054320.186Z_swarm-av_hypothesis_4cbf. Submitted work/chib1a (32 reqs); work/chib1b (4 reqs: S21 rest) pending.
  Mailed swarm-ar (S4×T1 β overlap) and swarm-w (w3 coordination).
- Next: submit chib1b when slots free; read odd/even parts; line-scan positives to |β|≤0.15; additivity; CMA.

## wakeup 2 (06:13 UTC)
- chib1a landed, 32/32 PASS (s21). Big odd parts on half-invariant dirs: |13|·44° acute+ (b2fe: s21 1.0263, r46 1.2758, r56 pending), |7|·169° (−sign gains), |4|·150°. Even parts −7…−33 % at 0.03 (w2 curvature ~5× w3).
- HERDING: an, aq, ah screened the same set; b took cross terms (chidress-w2, s21 1.299), q joint CMA, an line scans. My family is redundant beyond the screen.
- Unique contribution: Z3-breaking null test (|3|,|9|,|12|,|21|×3): |odd| ≤ 0.0085 so far. Submitted chib1b (4 reqs, |21| rest). Also g_cutoff 8 vs 10 agreement 1e-4 vs an.
- Next: when chib1b lands, post closing result + coverage, abandon/close chib-w2. Then pick a new role. Ideas: verifier of the s21→r46 jump for chiral β (r46 ≫ s21 at both signs per swarm-k/am); look at frontier (swarm-j chidress-w3 s21 2.03).

## wakeup 3 (06:36 UTC)
- chib1b landed: |21| dirs odd +0.005/+0.005. Z3 null complete (6 breaking dirs |odd| ≤ 0.0085).
- Withdrew b2fe (duplicate of an aa67/aq 7922/ah d734). Posted closing result + coverage: 20261008T063632.605Z_swarm-av_result_7c61. chib-w2 CLOSED.
- Frontier now: w3 t 4a76 s21 3.33/r46 3.09 (M2k 6.2, Σ|α| 1.97/2.5); ap 2848 s21 2.92/r46 3.72. w2 best b 8c39 s21 1.30/r46 1.34. r56 pending for all (incl. parents).
- Many agents in reserve/verifier. w2 optimizers: q (CMA 10-D), ai (gradient), b (dressing, closed). No w2 global surrogate.
- Mailed swarm-t asking whether they run xfam-gp on w2; if not I take `xfam-gp-w2`. Waiting ≤30 min before submitting.
- (06:50) w2 harvest: 714 rows (671 PASS, 39 FAIL), 17 agents; work/w2feat.py (pair-product basis, orbit-sum + orbit-norm features), work/w2gp.py (GP RBF+linear).
  LOAO corr 0.63; good inside screened blocks, under-predicts frontier (b 1.299→1.18, q 1.277→1.11). Not yet a reliable proposer. No reply from swarm-t yet.

## wakeup 4 (07:05 UTC)
- No reply from swarm-t re xfam-gp-w2 (w2 GP LOAO corr 0.63 — weak at frontier; parked).
- swarm-e critique 7556: w3 s21 frontier at M2k 6.2–7.4 is above static Δ(M2) calibration (≤6.5, swarm-ab a400 / swarm-p 2e62). Offered (mail to ab/e/p 07:05) to run shape P ρ^p controls at M2 6.5,7,8,9,10,10.88 on s21+r46 (12 controls), family `m2cal-hi-w3`.
- Built work/m2cal.py: ρ_w3^p/<ρ^p>, circular cutoff |G|²≤300 (C6-closed), positivity lift ε=2|min| (M2 shift ≤ 7e-4). Reproduces ab 3baa w(-2,-2)=0.66132 at M2 4.40. Inputs in work/m2cal/, all pass `swarm check --control`.
- Plan: submit ~07:25 unless ab says they're doing it; `--control --clusters s21,r46`.

## wakeup 5 (07:28 UTC)
- swarm-l took the M2 7–10 static calibration (m2hi-ctl b9d5); ab and p asked me to stand down. Did NOT submit work/m2cal/*. Offered M2 10.88 box-edge + 6.5 overlap inputs to swarm-l on request.
- Swarm converging: many final summaries (i, x, o, d, al, ah, w, v, ak, g); t paused until r56. r56 stalled campaign-wide.
- Switched to reserve/verifier: posted note (reserve-av). Next: long wakeups; when r56 lands, audit; answer requests.

## wakeup 6 (07:59 UTC) — DONE
- Frontier w3 ap 4547 s21 5.20/r46 5.41; static calibration to M2 10 done by as + l (agree 8e-4); 20+ agents finished; r56 still stalled; no requests to me.
- Ran `swarm done` with final summary (work/done.md). 36/500 evals used. Loop stopped.
