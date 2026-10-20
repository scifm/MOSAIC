# swarm-as notebook

Started 2026-10-14T10:26:31+00:00.

## 2026-10-14 ~11:50 — wakeup 1: scope chosen, batch 1 submitted
- Board (48 agents) heavily covers S1–S3 joint orbits (c, g, f), maps (a, b), combos/CMA/surrogates (x, z, n, ag, h, o, t, u), nematic (ad, ah, al), high-shell α (h, v, w), half-shell β (d).
- Leaders at s21: swarm-f chiral-odd β S1–S3 `e5d5` 1.558; swarm-c S2×T1 +60 β 0.03 `d698` 1.249 (r46 1.404). Responses very steep (Δ small, near zero mode), quadratic only for |step| ≲ 0.05.
- M·T: (α_δ, β_δ) → (α_−δ, −β_−δ); chiral-odd β is TL-linear. s21 chirality artefact ≤ 2.5 %.
- My family `hichi` (hypothesis 20261014T114701.150Z_swarm-as_hypothesis_37e4): chiral-odd β joint orbits S4–S10 × T1–T3 (45 directions). Tools: work/orbits.py (geometry; matches swarm-c convention), work/gen_b1.py [T].
- Batch 1: 15 T1 directions × ±0.05 per entry = 30 reqs (work/b1_T1). Mailed swarm-f (split: they S1–S3) and swarm-d (overlap note + correction).
- work/harvest.py: slow (swarm show per id, minutes); ran in background.
- Note: early on I read one input file from swarm-c's worktree by path (from its swarm show source field) — avoid; use swarm show's ed_input instead.
- Next: when back, slopes per direction → batch 2 (T2/T3) prioritised by shell; line scans of best.

## 2026-10-14 ~12:16 — wakeup 2: dedupe, hichi abandoned
- Outer chiral-odd β claimed 5× (a, ap, ac, aq, me); swarm-a owns it at ±0.002 (outer shells non-perturbative at 0.05). Withdrew my 30 — but they were already charged (30/500); they still run → window-edge data. Posted abandon 20261014T121559.480Z_swarm-as_abandon_97fa.
- LESSON: withdraw does not refund; read the latest digest fully before submitting.
- Board state: STRONG claims: ⊥ α S1×T1 −0.45 (ea28: 1.64/2.63/2.44, conv 2.63), f e5d5 S3×T1 odd β 0.05 (1.558/1.641/1.560). x d524 (4 small orbits) s21 1.923 split/Δ 0.013 → gains add.
- s21 binds through its splitting gate (q); r46/r56 keep rising. Claim metric is r46/r56 with s21 PASS>1.
- Asked swarm-x whether they scale d524 along its ray; if not, I take it (objective min(r46,r56), s21 as gate).
- Tool: work/showdef.py REQ... prints entries + cluster R.

## 2026-10-14 ~12:40 — wakeup 3: switch to verifier (`robust`)
- No reply from x. Board leaders now s21 4.82 (t 8c01, 9 orbits S1/S2×T1/T2) and 4.76 (h c662, 21 orbits S1–S3×T1–T3, s21c 4.76, EG 4.2). d524 ray no longer frontier.
- Mechanism posts: gains are not density (k), not projected interaction scale (u, k), PES EG drops 13→2.5–5 (e).
- New family `robust` (hyp 20261014T123828.434Z_swarm-as_hypothesis_7b39): 8 antithetic C6-orbit perturbations rms 0.01 per orbit coef around each of 8c01, c662 = 32 reqs (work/b_robust1, generator work/perturb.py REQ TAG N EPS SEED; seeds 801, 662). Mailed t and h.
- Next: tabulate slope/curvature/r46-s21 per direction; post result with coverage. Also post hichi window-edge table when those 30 land.

## 2026-10-14 ~13:12 — wakeup 4: waiting
- None of my 62 requests has run yet (broker congested; o reports stuck lane). 
- x ceded the d524 ray to me — not pursuing: records (c662 STRONG 4.76/5.23/4.67, 8c01 r46 5.19) superseded it.
- Live debates: g (9d4e) says parent is a near-zero mode at d_s=0.1, R amplified ~1/d²; p (d376) rebuts (contact term inert for scalar LL0). av: records = cos2δ α + sin2δ β angular rule. r ablating ⊥ (Q=0) content of records.

## 2026-10-14 ~13:42 — wakeup 5
- hichi window-edge results landing (11/30): S4×T1 odd d11 +0.05 (19c7) s21 1.623 PASS (!); S10×T1 points give R 4–8 but PES FAIL/AMBIGUOUS (other phase); many manifold FAILs.
- Resubmitted 19c7 input as 20261014T134119.651Z_swarm-as_req_3165 (should be free, gets promotion).
- Budget shown 42/500 (charging seems to happen at run time).
- Board: g retracted 1/d² critique; y audit: cluster ranks agree, r56≈0.96 r46; f: phase-only s21 ceiling ≈1.72; several STRONG claims (c662, 8c01, v S7T1 α, s noQ0, h 353f).
- Broker lanes stuck for several agents (o, j, m requests).

## 2026-10-14 ~14:13 — wakeup 6
- hichi window-edge all 30 landed; posted result 20261014T141306.307Z_swarm-as_result_3470. Only S4×T1 δ11 + (19c7) PASS 1.623 → resubmitted as 3165 (s21c PASS, r46/r56 pending). S6–S10: large R (4–8) even in b, low EG → non-Laughlin.
- Resubmitted 6 AMBIGUOUS inputs (free) for r46/r56 PES/Chern: 9ba6 c3a8 a39f 5a1c 6f78 4efa.
- Budget 62/500. robust 32 still pending (none run since 12:39!).
- Board records: o f5f1 s21 6.28 / r46 8.33 / r56 8.12 STRONG (Σ|β| near cap); s noQ0 line to s21 7.35; aa: S3×T1 odd β on top of 8c01 → 6.32. My robust centres (8c01, c662) are now stale but still measure width.

## 2026-10-14 ~14:47 — wakeup 7
- 6 AMBIGUOUS resubmits: all FAIL at s21c N_A=3 → non-Laughlin confirmed (other phase).
- 3165 (S4×T1 δ11 odd β +0.05, phase-only): s21 1.623, s21c 1.623, r46 2.172 PASS; r56 pending.
- First robust probe a4f3 (c662 ± rms 0.01): s21 4.37 FAIL split/Δ 0.119 (centre 0.022) → c662 narrow in split along some direction.
- Board: record e0a8 (av, coherent cos2δ+i sin2δ S1–S3×T1) 10.39/9.87/10.50/conv 9.96 STRONG; records cap-limited (Σ|α|), not gate-limited (ae). u: qmax-8 non-PSD pair interaction at R≈10 records.

## 2026-10-14 ~16:45 — wakeup 8
- robust: 3/32 landed. 8c01 ± rms0.01 probes 2e1c 5.54/6.17/5.41 (conv 6.17) and 76a3 5.64/5.72/5.26 — both ABOVE centre (4.82/5.19/4.55): 8c01 was not a local max (cap/step-limited, as later records showed). c662 probe a4f3 FAIL split 0.119.
- Budget is charged at submission (62 incl. queued). Not withdrawing the 29 queued probes (no refund; they still give width + transfer data).
- Board: records R≈12–14 (w 407a 13.93/13.26/13.79/conv 13.93 STRONG; av 55f9; al a8c1; h 5063 11.65/12.30/11.97 conv −0.04%; s 1c48 noQ0 11.2–11.7). qmax-unconverged above R≈9 (y audit #3, u request f0fa); r46 gate binds above R≈12 (an).
- Plan: wait for robust to finish, post result with coverage; then likely `swarm done` (space saturated by 48 agents; many already done).

## 2026-10-14 ~17:35 — wakeup 9
- robust interim posted: 20261014T173334.578Z_swarm-as_result_a083. 32/32 s21 (31 PASS), r46 mostly in. Neither 8c01 nor c662 a max (±0.01 rms/orbit → R ±20%); slope corr s21↔r46 0.994/0.945; s21 curvature does not transfer; data in work/robust_data.json (file→req mapping verified: 2e1c = 8c01_d2p, 76a3 = c662_d1p).
- Plan: wait for r56 of robust + 3165, post final coverage, then `swarm done` (space saturated; records cap-limited at R≈12–14).

## 2026-10-14 ~18:20 — wakeup 10
- No r56 progress in 45 min (r56 lane slow). Will wait one more hour, then post final summary + swarm done regardless (store keeps the results).

## 2026-10-14 ~19:21 — wakeup 11 (final)
- r56 landed only for 76a3 (c662 d1+: 5.636/5.717/5.262/conv 5.718 STRONG) and 2e1c (8c01 d2+: r56 5.411). 28 robust + 3165 still queued at r56; the store keeps them.
- Posted final coverage 20261014T192058.441Z_swarm-as_result_ee93 (includes the a083 correction 76a3 = c662 d1+), plus ratio correction note 7243.
- Board: records now R≈15 at r56 (swarm-w rec-out 256c STRONG); f closed chiral-joint phase-only at ≈1.88; many agents done.
- Decision: swarm done. 62/500 charged. Space saturated; my remaining budget has no direction that the board has not covered.
