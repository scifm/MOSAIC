# swarm-o notebook

Started 2026-10-02T03:52:05+00:00.

## 2026-10-02 04:20 — wakeup 1: orientation, role choice
- Board: a (w3 U atlas ±0.02, 96), c (w3 CMA-ES S1-4×T1-2 wide), b/e/f (three w2 atlases — herding),
  g/h (w3 orientation X/C, A/B pair-star modes), d (w3 chiral β beyond h), i (MT parity note; MT-even β).
- Broker "looks dead" (no tick for 13 min, 253 queued, nothing charged). Posted request 20261002T041549.808Z_swarm-o_request_d64d.
- Chosen role: **pooled-surrogate** (integrator). Hypothesis 20261002T041544.364Z_swarm-o_hypothesis_2e7a, ~150 req.
- Tools in work/: board.py (dump every visible request via swarm API → work/board.json),
  canon.py (block → canonical pair coords a_gR=α·2/√(d_s d_p); C6 joint-orbit projection),
  alias.py (momentum-star aliasing per cluster), fit.py (direction-grouped cubic fits + LSQ pooled gradient).
- Key fact: on s21, F_R depends on m = 5R1+R2 mod 21; T1↔{1,4,5}, T2↔{3,6,9}, T3↔{2,8,10}; |R|²=7 half-aliased;
  |R|²≥9 exactly aliased; R=(4,1) constant on mesh. Keep surrogate on T1–T3.
- Next: once results land, run board.py + fit.py --parent w3; post pooled gradient table; design first joint step.

## 2026-10-02 04:40 — wakeup 2: first data, first batch
- Broker was slow, now fixed (human note). swarm-r took w2-synth; I'm w3 only (mailed).
- Pooled w3/s21 (365 pts): gradient on α S1T1⟂ (+1.55), α S2T1∥ (+1.40), β-chiral S4T1 (d 2400, 1.036 s21 / 1.080 r46),
  β-chiral S7T1 (i 877a, 1.025 / 1.057). h's gc10 line scan along ⟂ is nearly linear to +13.5% at t=0.11 (6e88);
  2D ⟂/∥ (0.055,0.055) = 1.129 (7b23). M2k only +2.6%. Small-step quadratic is misleading.
- Tools: work/raw.py (raw points on orbits), work/build.py (combine requests' canon vectors → pair-star block).
- Submitted b1 (11 req, gc10): A=7b23 × C7=d2400 × C13=i877a combos; β-only combos; 2A. Note 20261002T044004.003Z_swarm-o_note_4353.
- Next: fit additivity R(A+C)-R(A)-R(C)+1; if additive, push along joint direction; watch r46/r56 of promoted.

## 2026-10-02 04:58 — wakeup 3: b1 results, LL-mixing pivot
- b1: strong α×β-chiral superadditivity. 968b (2A+2C7+2C13): s21 1.609, r46 1.710; 2A alone 1.272/1.231 at SAME M2k 4.0207
  → phase-on-amplitude increment is beyond-M2 at fixed density. Result post 20261002T045759.341Z_swarm-o_result_5751.
- Caveat (b e1e5, p f9b6, j): S1T1⟂ orbit is half Q=0 static coherent LL mixing (Q=a_G+R, a_G=z×G l²). A contains it.
  Human asked by b (request 3942). Use S2T1∥ (Q=0 fraction 0) as base.
- c's pure S2T1∥ ray: t=.15/.20/.27/.35/.45 → s21 1.179/1.246/1.347/1.456/1.518, r46 1.171/1.241/1.351/-/1.409; M2k up to 5.3 (largely M2).
- b2 submitted (9, gc12): cc20/776c/d49b + m·(C7+C13). p covers t=.11-.22 + 2P.
- Next: fit β increment vs α; find β optimum at large α; check r56 for 968b/230c/776d; push LL-free best.

## 2026-10-02 05:16 — wakeup 4: b2 LL-free results, b3
- b2 LL-free: bd1a (776c t=.45 + 4P, β=.12/mode) s21 2.271 / r46 2.627; c86d (2P) 2.081/2.092; 392d (t=.27,3P) 1.813/2.072.
  Phase increment at fixed M2k: +37-50% s21, +48-86% r46. r46 > s21 grows with β (b130: 1.115/1.690!) — finite-size risk.
- Board top: p cc86 (t=.55, β=.09) 2.399/2.470; m w3-E points around it. No r56 results yet for any w3 point.
- Tools: work/top.py (top points summarized as perp/par/C7/C13/other norms).
- b3 submitted (12, gc12): t∈{.45,.55,.70}×β to .18; C7:C13 5:3/3:5; +k's α49 (cf1c) / α16 (1434) at .10.
- Result post 20261002T051633.357Z_swarm-o_result_8465 (herding + r56 warning). Mailed p, q (board.json path), e, k.
- Spent so far: 11+9+12 = 32 requests.
- Next: r56 results — the decisive test. Fit (t,β) model per cluster; if r56 sign holds, prepare final candidate + LL/density checks.

## 2026-10-02 05:39 — wakeup 5: first r56, b3, b4
- bd1a r56 2.567 (s21 2.271, r46 2.627) → conv46. cc86 r56 2.456. r56 tracks r46 within ~2%.
- b3: 48bf (t=.7, β=.15) 2.621/3.035 (qmax/PES edge); bb6e (t=.55, β=.12) 2.476/2.766; s21 peaks β≈.12, r46 keeps rising.
  C7:C13 5:3 slightly better. k's α49/α16 subtract. Result post 20261002T053905.717Z_swarm-o_result_3301.
- i's critique f044 (parent-harmonic static content): mailed counter-point (β increment grows with α → cross term).
- b4 (8): α∥ × 4 chiral modes (C19=38eb, C21=9818 from d). Requests used: 40.
- Next: b4 results; r56/conv46 of bd1a, bb6e, 48bf; consider final-candidate write-up with coverage; maybe density control request for bd1a amplitude part.

## 2026-10-02 06:00 — wakeup 6: STRONG claim bd1a, b4, sign probes
- bd1a: s21 2.271 / r46 2.627 / r56 2.567 / conv46 2.628 → broker `strong`. Claim posted (provisional, static-content ruling pending):
  20261002T060020.321Z_swarm-o_claim_0125. Also strong: 392d (1.813/2.072/2.004/2.071), c86d (2.081/2.092/2.052/2.090).
- Controls: a's avg-density for bd1a α block = 1.030/1.031; e: β of bd1a alone (α=0) = 0.689 → β is multiplier on α, not standalone.
- b4: C19 (38eb) / C21 (9818) also superadditive with α. b7cb (t=.7, 4P+2C19+2C21) 2.741/3.572; 3eea 2.719/3.014;
  but s21/r46 diverge badly at large β (558f 1.407/3.303) — r56 must decide, distrust.
- Other claims: p cc86 strong (provisional); d 2400 robust_positive phase-only (r56 margin 0.6%).
- b5 (4): sign probes 776c ±β, −α — bilinear cross-term test. Requests used: 44.
- Next: r56 of b3/b4 → fit per-cluster (t,β) model; post b4 result + sign-probe result.

## 2026-10-02 06:30 — wakeup 7: sign probes, purity, mode model
- b5 sign probes (s21): +α,−2P 1.141; +α,−4P 0.755 FAIL; −α 0.314; −α,+4P 0.104 FAIL. log-R cross term +0.78/−0.73 under α→−α:
  β-chiral gain is sign-locked to α∥ (one bilinear κ≈10). Note 20261002T062805.529Z_swarm-o_note_7147 (+ bd1a eg 4.3–5.0, split/Δ ≤5e-3).
- Mailed n bd1a M2k 5.2995 for M2-matched control.
- work/fit3.py: log-quadratic on 6 modes (par, C7, C13, C19, C21, S1T2par[orbit (1,0)|(2,-1)]); 152 pts in span.
  LOO rms log R: s21 0.25, r46 0.032, r56 0.028 (25 pts). work/opt3.py: unconstrained optimum runs to the box edge (par .82) — not trusted.
- b6 (2): model validation at par .55, C7=C13=.15, S1T2par −.05/−.09 (+C21 .025); predicted r46 ≈3.2. Requests used: 50.
- Board: p's cc86 strong + 8/8 grid strong; p now running global Sobol over 10 live orbits; i static-free CMA; static-free fixed probes null (p).
- Plan: low-spend from here. Validate model; critique; final coverage + done when board saturates.

## 2026-10-02 06:55 — wakeup 8: ladder results, wind-down
- Strong (all 4 stages PASS): bd1a, 392d, c86d, 2150 (1.730/2.227/2.148/2.227), 4c16, 586b, 4203, 2eff, b130 (1.115/1.690/1.648/1.692),
  968b (1.609/1.710/1.580/1.710, LL-mix provisional), 230c, 776d, 32c5, b984, 23f3, 3738, 4d63. 17 strong.
- b3/b4 still waiting on r56 (queue). Validation ea3b (e18d+S1T2par −.05) 2.443/2.982 vs e18d 2.438/2.970: add-on ≈ +0.4%, so the model overpredicted.
- Board: c claim 776c strong (α only), h claim d49b strong (small α only), p Sobol df8f 2.74/3.46, m done.
- Plan: one more cycle for r56 of b3/b4 + befd; then final coverage result + swarm done.

## 2026-10-02 07:28 — wakeup 9: final
- 829c (= d e25f) and 84e4 phase-only reached strong. Mailed d (e25f is theirs). Claim 84e4: 20261002T072701.286Z_swarm-o_claim_26bd.
- Final coverage result posted. 50 requests charged; 19 strong; b3/b4 r56 pending (broker finishes them).
- swarm done.
