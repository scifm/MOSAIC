# swarm-d notebook

Started 2026-10-14T05:16:56+00:00.

## Wakeup 1 — 2026-10-14 ~05:30Z
- Board: swarm-a = amp-map (30 full-shell α dirs). swarm-b AND swarm-c = phase-map (30 full-shell β dirs): herding.
- Physics I derived (posted hyp 8840 + critique note 5e23; mailed a/b/c):
  MT = mirror × conjugation is a symmetry of w1c. Full-shell β → −β and chiral (mirror-odd) α → −α under MT,
  so those are EVEN in the TL. First-order directions: full-shell α, and **chiral β** (12-member shells
  |G|²=7,13,19,21 split into C6 halves A,B, β_A=+x, β_B=−x).
  No cluster is mirror-symmetric (s21 is C6 but chiral; r46/r56 C2 only; work/cluster_sym.py), so the odd parts
  on clusters are finite-size artifacts.
- My family: `chiral-phase`. Tools: work/stars.py (solver-basis shells, chiral halves), make_chiral_map.py, make_beta_map.py.
- Submitted: 24-eval chiral β map x=±0.10 (work/chib10; req ids 6775…74b4), plus 2 diagnostics:
  chiral α ±0.15 S7×T1 (28f0 = m, 1e04 = p). Expect R(+)≈R(−) for the α pair (MT test at s21).
- Next: read the map; even/odd decomposition; line search on the top ≤4 at ±0.2 and ±0.3; then CMA-ES 12-D.

## Wakeup 2 — 2026-10-14 ~05:55Z
- My chiral-half × full-T product map: EVEN in ±x to ~1e-4 even on s21 (prediction of linear term FAILED). Best 1.0071 (S7T3).
  Outer shells collapse (S19/S21 FAIL). Chiral α probe also even (0.9916 both). Posted result d064 with coverage.
- swarm-e: orientation-locked joint orbits (two-member stars {±G}×{±R}, C6 orbits of pairs, β=+b on orbit P, −b on mirror MP)
  give HUGE gains at b=0.0245: O1T1m 1.28 all clusters (STRONG), O3T1m 1.62/1.79/1.67, O4T1m 1.69/1.99/1.83, O9T1m 1.52/2.42/2.28.
  Response strongly odd. => first-order lives in G–R orientation locking.
- New tools: work/orbits.py (joint orbits, mirror map), work/make_orbit12.py (orbit_input(s,t,{orbit:coef})).
- Submitted 72 evals: 12-member shells {7,13,19,21} × T{1,3,4} × 3 mirror-odd orbit pairs × ±b (work/orb12). Hyp ccfc; mailed swarm-e.
- Budget after: ~98/500.
- Next: read orb12 map; critique swarm-e's leaders (s21→r46 spread, PES gap 6.4, linearity); line search; combine.

## Wakeup 3 — 2026-10-14 ~06:30Z
- My 72 orb12 map duplicated swarm-b's odd-orbit12 by hash (b first). Ceded the 12-shell sector to b (mails sent).
  Best of mine: 130d s21 1.6309/r46 1.9855; 5688 1.6117/r46 2.475; 0367 1.49/1.56 — climbing the ladder.
- Board: s21 ceiling ≈1.73 on many unrelated directions; r46 1.8–2.5. O1T1− curve 1.28 (rms .06) → 1.71 (.20) → 1.73 (.25).
  Claims all limited by s21. Hypothesis: branch crossing (soft mode lifted, then a T1-insensitive branch sets the gap).
- Cluster symmetry (work/cluster_sym2.py): only Nk=9, 12, 27, 36 are C6v. Posted request 2225 to the human for Nk=27 diagnostics
  (+ an exact MT test). Seconded b's low_energies request 219c.
- New family `ceiling-break` (hyp 208b): base 92e8 (O1T1− rms .20, reproduced exactly by work/combo.py BASE_92E8)
  + β-odd T3/T4 steps rms .03 ± on S1,S3,S4,S9 (P−MP) and S7 (3 pairs) → 28 evals submitted (work/ceil1).
- Tools: work/combo.py combo_input([(s,t,kind,{orbit:coef})]), odd_pairs(s,t); work/showdef.py REQ... prints a request's deformation.
- Budget: ~126/500 after this batch.
- Next: read ceil1; if all flat or negative → ceiling is outside the T3/T4 β-odd subspace; post result + coverage.

## Wakeup 4 — 2026-10-14 ~06:58Z
- ceil1 results (posted 4190, with coverage): T3 β-odd "−" steps lift the s21 plateau at first order: S7T3 o0/3− c821 s21 1.899,
  r46 2.101, r56 1.812, conv46 2.101 → min 1.812 (base 92e8 min 1.711). Phase-only = clean beyond-M2. T4 loses on every direction.
  r56 tends to drop as s21 rises.
- Board: swarm-a's α-SM orbits on 29d3 break the ceiling hugely: 2fc4 s21 4.60 / r46 5.32 (contains α → needs a control).
  swarm-b 5f99: the s21 ceiling is the 4th level.
- Niche now: **best phase-only (beyond-M2-clean) point**. ceil2 (10 evals) submitted: gradient steps t=1..4, top3 ×1/1.5,
  S7o03 ×2/3, gradient on 29d3. Builder: work/make_ceil2.py (G list = slopes).
- Budget: 136/500.

## Wakeup 5 — 2026-10-14 ~07:27Z
- ceil2: every joint T3 step COLLAPSED (grad t=1 → 0.40 F; top3 → 0); S7o03 2× 1.367, 3× 0. Non-additive, cliff-bounded.
  Closed ceiling-break (result posted, with coverage). Phase-only frontier c821 min 1.812. swarm-e takes the 10-D phase-only CMA (mailed).
- Board: α+β joint CMA (swarm-c) R ≈ 10–12.7 at s21; 429f s21 10.78 / r46 10.47 / r56 9.68 (SUGGESTIVE, conv pending).
  Controls (swarm-a) R≈0.995 → beyond M2. Leaders are cliff-adjacent.
- Solver check: H is a normal-ordered two-body only (gpu_ed.jl rejects one-body), so the k-dependent envelope adds no hidden one-body dispersion.
- New family `robustness` (hyp 595c): 11 diagnostics around 429f (work/robust_429f; builder work/make_robust.py REQ TAG):
  base_copy (1032), nonsym02 (ee14, 90dd), scale 0.97/1.03 (33b8, a2c9), sym02 (bd5c, 506d, 347f), sym05 (419d, 9502, 5f19).
- Budget ≈ 147/500 (some may be free).

## Wakeup 6 — 2026-10-14 ~07:50Z
- Robustness around 429f: ±5% orbit perturbations → s21 10.32–11.13, all PASS; scale 1.03 → +3.2% (not stationary along its ray);
  C6-breaking noise second-order. Posted 179b (with finite-size drift table: R falls 1–10% from s21 to r56).
- Leaders now: 3b76 (c, ray t1.5) 12.71/12.33/12.14 converge; s21 up to 13.9 (a lead6 ea2a). a, b, c all probing leaders.
- Submitted 7 diagnostics: factorial α/β decomposition of 3b76 (work/decomp_3b76, builder make_decomp.py):
  (α,β) scales (0,1) (1,0) (.5,1) (1,.5) (.5,.5) (.75,1) (1,.75). Question: how synergistic is the gain (mechanism, claim 2).
- Budget ≈ 156/500.

## Wakeup 7 — 2026-10-14 ~08:13Z
- Decomposition of 3b76 (posted 1fbb): α only 0.078 F; β only 4.466 AMBIGUOUS (PES gap 0.23, counting OK);
  (.5,.5) 6.35 P, (.5,1) 7.54 P, (1,.5) 9.31 P, (.75,1) 11.34 P, (1,.75) 11.61 P; full 12.71. Superadditive.
  Reading: β-odd makes the gap, α-orbit restores Laughlin character (PES gap 0.23 → 4).
- Phase-only high-R region (AMBIGUOUS) laddered: family `phase-only-hiR`, β of 3b76 × {0.6 (2f2c), 0.8 (fe5a), 1.0 (06c6), 1.2 (bbdb)}.
  Want: where does PES gap cross 0.5; does it hold at s21c N_A=3 / r46 / r56?
- Leaders: s21 up to 15.9 (a lead6), abf0 (b) 15.77/14.61. c runs a 20-D CMA with boundary repair (Σ|α| ≤ 2.5 binds).
- Budget ≈ 156/500.

## Wakeup 8 — 2026-10-14 ~08:43Z
- phase-only-hiR closed (ec52): 06c6 (= f40c) s21c N_A=3 FAIL; 0.6×/0.8×/1.2× FAIL. No Laughlin phase-only point above e's 2.116.
- swarm-a critique 8a9b: s21-selected optimizers overfit s21 (spread 15–20%). Leader by min: abf0 (b) 15.77/14.61/14.66/conv 14.65 STRONG.
- New family `min-es` (hyp 0053; mailed c): work/es_min.py = (4/4,8)-ES over abf0's 14 coefficient groups (scale factors),
  fitness min(R_s21, R_r46), both PASS. State work/es_state.json. Run `es_min.py step` each wakeup: it collects the gen
  once every candidate has an r46 verdict (or failed) and then proposes + submits the next one. Gen 0 submitted (1e23…4b07).
- Budget ≈ 167/500.

## Wakeup 9 — 2026-10-14 ~09:12Z
- min-es gen0: 8/8 PASS, min(s21,r46) 14.16–14.69 vs abf0 14.61 → plateau. Closed (result 03bf). c's v3 also switched to
  min fitness (0bd5/262f min 15.90). Controls for all α leaders ≈0.98–0.9995 (c bacb) → beyond M2.
- Robustness on 262f (STRONG 17.17/16.42/15.90/conv 16.35; on the Σ|α|=2.5 boundary): 4 REGULAR requests
  (sym02 ×2, sym05_0, nonsym02_0) so r46/r56 are measured too. sym05_1 was rejected (Σ|α| > 2.5).
- Budget ≈ 176/500.

## Wakeup 10 — 2026-10-14 ~09:23Z
- 262f robustness at s21: nonsym02 17.125, sym02 17.110 / 17.044, sym05 16.836 (all PASS; base 17.171). r46/r56 in flight.
- swarm-a closed all its families. c claims 0bd5 (= 262f content) STRONG, best by min 15.90. b's 12-shell probe at 262f in flight.
- ~09:50Z: 262f probes r46 16.41–16.49 (base 16.42). r56 pending. All other agents have closed their families. b's critique 8c94:
  treat r56/Nk=27 as hold-outs, quote the frontier as a band. Agreed by mail. Next: post the robustness result once r56 lands, then
  final coverage + `swarm done` unless the human answers Nk=27 / Σ|α| (then do the follow-up).

## Wakeup 11 — 2026-10-14 ~10:16Z — DONE
- 262f robustness: r56 15.88–15.95, r46 16.41–16.49, conv46 16.43–16.48, all PASS (posted c643 with coverage).
- Final summary posted, and `swarm done` run. 168/500 charged. Open: Nk=27 request 2225, and a's Σ|α| request 091f (human).
