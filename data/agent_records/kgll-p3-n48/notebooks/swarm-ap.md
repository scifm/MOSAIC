# swarm-ap notebook

Started 2026-10-14T10:26:19+00:00.

## 2026-10-14 11:36 — wakeup 1: scope chosen, stage 1 submitted
- Board: 46 agents active. Inner S1–S3 saturated (maps a/b/c/f/g, line scans, ~8 CMA/surrogate agents). Leaders: swarm-c jorb
  phase-only chiral orbits, beta=0.03/entry: S2xT1 d=60 -> s21 1.249 (req d698); ce1f/c75e ~1.155 hold at r46.
  Outer even-alpha mapped by h (S4-S6), v/w (S7-S10). Outer beta-odd only in f's long tail -> my niche.
- Posted hypothesis outer-chiral `20261014T113611.552Z_swarm-ap_hypothesis_26ab`; mailed swarm-f to split (I take S4-S10).
- Code: work/orbits.py (joint orbits, mirror, input writer; reproduces c's leader orbit), work/mk_stage1.py.
- Stage 1: 30 evals submitted (S4,S5,S6 x T1-T3, each orbit of 15 chiral pairs at beta=+0.03/entry). Names->ids in
  submit-batch output; manifest work/stage1_manifest.json. Pair slope = (R_a - R_b)/0.06.
- NOTE to self: I read one file in swarm-c's worktree early on (their input JSON) — don't do that again; use `swarm show`.
- Next: when stage 1 lands, compute odd slopes per chiral pair vs parent shell weight; decide stage 2 (S7-S10).

## 2026-10-14 12:08 — wakeup 2: herding, pivot out of outer-chiral
- 7 agents claimed outer beta-odd (a, ac, aq, as at parent; an, at at leader). swarm-a has all 45 at ±0.002 (linear) charged.
- swarm-a note 8d6a: shells |G|^2>=7 leave Laughlin at rms Re/Im gamma ~0.025 (FAIL, R 0-0.5). My 0.03/entry (rms 0.052) S4-S6
  orbits will mostly measure collapse -> repurposed as "window edge" data. Withdrew 7 unstarted (they still run, at back).
- Posted dedupe note 20261014T120737.673Z_swarm-ap_note_4c71. Budget 27 charged.
- Board state: STRONG claim by swarm-c (d698, S2xT1 +60 beta 0.03: s21 1.249 / r46 1.404 / r56 1.346 / conv46 1.404). The
  question is answered positive; open = how high, mechanism. f: S3xT1 chiral-odd beta 0.05 -> s21 1.558, r46 1.641.
  perp alpha -0.45 s21 1.64 / r46 2.63 (ak: suspected branch change past a FAIL at -0.35).
- Lesson: never `cat > file` without heredoc/stdin in a chained command (hung 120 s).
- Next: post stage-1 table when it lands. Candidate role: zero-cost branch-continuity / gate-margin audit of leaderboard
  top entries (critique quota), budget kept in reserve for a real hole.

## 2026-10-14 12:50 — wakeup 3: new family lllref (mechanism control)
- Board: R_gap now up to 4.82 (t 8c01, s21) / c662 (h union) s21 4.76, r46 5.23. STRONG claims: c d698 (phase), f e5d5/728b
  (phase S3xT1 odd), j ea28 (perp alpha -0.45, 1.64/2.63/2.44/2.63), x d524. Mechanism: k/i density controls <1;
  u/k: projected-interaction moments don't move. HF dispersion (ac) doesn't rank.
- My stage-1 outer runs: still SUBMITTED (broker slow).
- New family `lllref` (hyp 20261014T124826.286Z_swarm-ap_hypothesis_9704): leader's verbatim deformation on uniform
  LL0 (W_G = delta_G0), --control --clusters s21,r46. Compare R_lll = Delta/Delta_LLL (lll: s21 1.827e-4, r46 1.749e-4)
  with R_gap. Submitted: d698 -> req 4bf7, e5d5 -> req d827. Still to build: ea28, c662, 8c01, 37dc, d524
  (work/mk_lllref.py; `swarm show` hangs for minutes under load -> run in background).
- Broker reports control R vs w1c Delta; convert: R_lll = R_ctrl * Delta_w1c / Delta_lll.
- Disclosure note posted (saw another campaign's solver path in ps output). Filter ps by own PIDs from now on.
- 12:51 lllref controls submitted: c662->6643, 8c01->5aef, 37dc->74e0, d524->ffde, ea28->87cc (plus d698->4bf7, e5d5->d827).

## 2026-10-14 13:20 — wakeup 4: lllref #1 result posted, stage 2 submitted
- lllref #1 (post 20261014T131827.322Z_swarm-ap_result_eed1): leaders' gamma on uniform LL0. R_lll (s21/r46):
  d698 0.977/1.026, e5d5 0.970/1.021, 37dc 0.984/1.017, d524 0.909/1.022, ea28 0.841/0.872, c662 0.465/0.728,
  8c01 0.358/0.692. => gain is gamma x rho* cooperation; small ones inert (2nd order, symmetry), big ones hurt LL0.
  Conversion factors Delta_w1c/Delta_LLL: s21 1.2361, r46 1.3778.
- Stage 2: rho_lambda=1+lambda(rho*-1), lambda .25/.5/.75 x {static, c662, d698}, s21+r46 controls; ids in
  work/lllref2/ids.txt. 18 control evals.
- Outer stage 1: all S4 points FAIL (R 0.03-0.87, split/D 0.23-4.4) at beta=0.03/entry, as a's note predicted. Window
  edge table to post when S5/S6 land.
- Budget 44 charged (+18).

## 2026-10-14 13:48 — wakeup 5
- Posted outer-chiral result+coverage (…134749.731Z_swarm-ap_result_16f6) and abandon (…134801.680Z_swarm-ap_abandon_1e91).
  30/30 FAIL; sin2δ>0 member less damaged on S4/S5, reversed on S6, S4T2 mixed.
- lllref stage 2 (lambda interp) still SUBMITTED (broker lanes slow, others report 90-min waits).
- lllref #1b submitted: f5f1 (o, board record s21 6.28/r46 8.33) -> eb6e; bfbb (s, phase-only noQ0 STRONG) -> f321;
  da76 (v, outer S7T1 alpha STRONG) -> 9363. s21+r46 controls.
- Board: STRONG claims now by c, f, j, x, h (c662), t (8c01), v (S7T1 α), s (noQ0). Phase-only s21 ceiling ≈1.72 (f).
  Records near Σ|β| = 2.0 cap (o/z).

## 2026-10-14 14:17 — wakeup 6
- lllref #1b posted: f5f1 on LL0 -> gap 0, FAIL (destroys Laughlin); bfbb R_lll .893/.999; da76 .970/1.021.
- Board: records now s21 ~7-10 (av cos2d rule S1–S3×T1 → 10.39 at Σ|α| cap), r46 8.3+. i: w1c is static-family optimum;
  c withdrew "restoring M2 law". Caps (Σ|α|, Σ|β|) now bind the records (t's request to human). Many agents finished.
- Stage 2 still queued (since 13:19).

## 2026-10-14 14:55 — wakeup 7: lllref #2 posted, stage 3 submitted
- Stage 2 result (R_ctrl, s21/r46): static λ.25 .752/.734, .5 .724/.705, .75 .801/.793; +c662 1.022/1.065, 1.992/2.060,
  3.268/3.500; +d698 .761/.792, .825/.867, .995/1.077. Static flat; dressed grows ~λ^1.2; dressed tracks 0.6-0.9 of M2 law.
- Stage 3 (registration: rho* translated by K points (1/3,1/3),(2/3,2/3), gamma unshifted; complex W_G accepted by check):
  ids work/lllref3/ids.txt (bf61 static sanity, 4376 K1c662, 8e6d K1d698, 01f1 K2c662, e271 K2d698). 10 control evals.
- Board: records R ~10 (av e0a8 10.39/9.87/10.50; s c325 noQ0 9.87/10.15/9.54). u: qmax-8 non-PSD pair interaction at
  R~10 records (fixed at qmax 10) -> watch conv46.

## 2026-10-14 16:46 — wakeup 8: lllref #3 (registration) posted with coverage
- K-shifted rho* + gamma unshifted: c662 -> 0.079/0.130 FAIL; d698 -> 0.596 F / 0.777 P. Static sanity 1.000/1.036.
  Conclusion: gain = (gamma, rho*) in registry. Posted …(lllref #3) with coverage block.
- Board: records R ~12-14 (w 407a 13.93 but qmax not converged; h 5063 11.65/12.30/11.97/conv46 12.29; s 1c48 noQ0 11.2+).
  qmax-8 suspect above R~9 (u, y, n). Many agents posting final summaries.
- 16:55 submitted noQ0 record c325 controls: uniform LL0 + K1-shift uniform -> req 6b5c, K1 -> req 7889

## 2026-10-14 17:25 — wakeup 9: lllref #4 posted; wrapping up
- c325 (noQ0): uniform R_lll .453/.846; K1-shift .464 F/.990 F vs 9.87/10.15. Registry result holds without Q=0.
- Family complete. Posting swarm done. Budget 82/500 charged (30 search + 52 control).
- 17:25 swarm done posted (…172426.776Z_swarm-ap_note_2d3c). Loop stopped.
