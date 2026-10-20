# swarm-aa notebook

Started 2026-10-14T10:25:22+00:00.

## 2026-10-14 ~11:45 UTC — wakeup 1 (first)
- Read brief/board. Board very herded: ~40 agents on low-shell joint orbits; 3–4 pooled surrogates (h,o,t,[u abandoned]), 3 CMA (z,ag,am), f owns chiral-odd β 54-D map/ascent.
- Leaders (s21, PASS, phase-only, chiral-odd β, swarm-f bodd units): S3×T1 +0.05 → 1.558; S2×T1 +0.05 → 1.483; S1×T1 +0.10 → 1.381. Transfer s21→r46 holds/grows for chiral phase orbits (c_d698 1.249→1.404).
- Outer shells (|G|²≥7) at 0.05 break Laughlin (swarm-a note). Full-star α ~0.1 → FAIL with big gaps (other phase).
- Tools written: work/pull.py (cache all leaderboard requests via swarm show → work/cache, 60 s timeout per call; first version hung on one show), work/coords.py (any block → pair-product coeffs → joint-C6 orbit coords; label G|G|²xR|R|²@δ), work/table.py (pooled table by direction), work/chi3/gen.py.
- Chose family chi3map: dense 3-D map of chiral-odd β on S1,S2,S3×T1 (b1,b2,b3 in f's bodd units). Hypothesis 20261014T114241.207Z_swarm-aa_hypothesis_3d6a. Mailed f.
- Batch 1 submitted: 26 reqs (ids in work/chi3/b1_ids.txt): axis lines 0.025..0.3 + additivity probes at 0.025/0.05. 4 should be free (hash = f's).
- Next: read results; batch 2 = 3-D grid in live region up to gate boundary (≤80). L1 wall: |b1|+|b2|+|b3| ≤ 1.0.

## 2026-10-14 ~12:12 UTC — wakeup 2
- The 4 hash-shared axis points came back free and are at converge stage: S3 0.05 (s21 1.558/r46 1.641/r56 1.560), S2 0.05 (1.483/1.507/1.453), S1 0.10 (1.381/1.388/1.354), S1 0.05 (1.192/1.184/1.175). All SUGGESTIVE already.
- Other 22 still queued at s21 (queue backlog).
- Board: f now runs an ascent along slope (3.85, 9.62, 11.29) and the balanced (1,1,1) direction in MY subspace + S1 line to 0.25; b's sin2d S123 is ≈ the (1,1,1) direction too. => batch 2 should avoid the slope line and the diagonal; spend on off-diagonal grid and the gate boundary.
- Leaders now α⊥ S1×T1 −0.45 (s21 1.64, r46 2.63, r56 2.44) — but ak critiques a branch change there; k shows density controls don't explain it.

## 2026-10-14 ~12:50 UTC — wakeup 3
- My chi3 batch1: 22 still queued at s21 (not started after ~1 h; ~900 evals ahead). 4 hash-shared points done through conv46.
- Board jump: h's union α+β step c662 s21 4.760 / r46 5.226; t's 8c01 4.816 / 5.186 (cos 0.91 — same direction). α·β superadditive. e: PES EG drops 13.4 (static) → 3–5 for any k-dependence; gate still passes.
- Leaders contain no S3×T1 chiral-odd β. New family lead3: leader + b3·S3odd, b3 ∈ {0.025,0.05,0.1,0.15} for both c662 and 8c01 (8 reqs, ids work/lead3/ids.txt (8c01 only) + 3dc1/49e3/ee89/b9a5 for c662). Note posted. Generator work/lead3/gen.py (works on any pair-star block).
- Next: read chi3 + lead3 results. If lead3 positive, extend (b3 larger, also S3×T1 α orbit pattern, scale leader step).

## 2026-10-14 ~13:25 UTC — wakeup 4
- chi3 landed (s21): S3 axis 0.025 1.296 / 0.05 1.558 / 0.10 1.7145 PASS / 0.15 1.412 FAIL(split 0.18) / 0.2 FAIL / 0.3 1.85 FAIL(split+PES). S2: 0.025 1.244 / 0.05 1.483 / 0.10 1.710 / 0.15 1.653. S1: 0.05 1.192 / 0.10 1.381 / 0.20 1.651 (r46 1.847). Combos: (0,.025,.025) 1.523 (≈additive), (0,.05,.05) 1.727 (saturating; additive pred 2.04).
- Withdrew S2 0.2/0.3 (ae's s2phase line = my S2 axis, gate closes at bodd≈0.18). Mailed ae.
- Board: STRONG claims c662 (h) 4.76/5.23/4.67/5.23, 8c01 (t) 4.82/5.19/4.55/5.19. av: records = cos2δ α + sin2δ β rule on S1/S2×T1; S3 and outer unused (supports my lead3). ap lllref: γ on uniform LL0 loses → gain is γ×ρ* cooperation. am: random phase directions FAIL — gains are directional.
- lead3 8 points still queued.

## 2026-10-14 ~13:55 UTC — wakeup 5
- lead3 s21 (all PASS): c662+b3 {0.025,0.05,0.1,0.15} = 5.033/5.236/5.392/5.153; 8c01+b3 = 5.211/5.556/6.076/6.318 (rising). NB ids: c662 0.025→3dc1 … 0.15→b9a5; 8c01 0.025→eaf8, .05→dc80, .1→8da0, .15→e3a7.
- Submitted 8c01+b3 0.2/0.25/0.3 (750b, cf21, a145). Posted interim result.
- Record now o's f5f1: s21 6.28 / r46 8.33 / r56 8.12 / conv46 8.33; already contains S3 odd β (b3≈0.167), Σ|β|=1.88 (cap 2.0). Cap is representation-dependent (t's request to human).
- chi3 phase-only: s21 ceiling ~1.72 everywhere, r46 keeps rising (S2 0.15: r46 2.54). S2/S3 single axes FAIL beyond ~0.15 (split gate). (0.025 triple) 1.584, (.05,0,.05) 1.659, (.05,.05,0) 1.606.

## 2026-10-14 ~14:25 UTC — wakeup 6
- lead3 r46: c662+b3 .025/.05/.1/.15 → 5.70/6.16/6.90/7.41; 8c01+b3 → 5.61/6.03/6.81/7.50 (r46 still rising past s21 peak for c662). r56 pending. 8c01 0.2–0.3 queued.
- chi3 conv46 done for several: S3 .10 1.714/2.299/2.134; (0,.05,.05) 1.727/2.194/2.024; (.05,.05,.05) 1.716/2.373/2.200; S1 .20 1.651/1.847/1.719. Phase-only s21 ceiling 1.73 confirmed; r46 best 2.54 (S2 .15).
- Board: records now cap-limited (Σ|α| ~2.3–2.5): av cos2d coherent rule s21 up to 10.39; x outer α at c662 7.22; o f5f1 STRONG 6.28/8.33/8.12. m adds S3 odd β to t's 6506 (complement to lead3, mailed me). ai/t asked human about chart-dependent L1 caps.
- Plan: wait for line + ladders, then post chi3map result+coverage and lead3 closing. Probably little more budget needed in my niche.

## 2026-10-14 ~14:55 UTC — wakeup 7
- 8c01+S3 line: 0.2 → 6.212, 0.25 → 5.730, 0.3 FAIL (split 0.153). Peak b3=0.15: e3a7 STRONG 6.318/7.500/6.877/conv46 7.500.
- New records: av e0a8 (cos2δ+i sin2δ rule S1–S3×T1) 10.39/9.87/10.50/9.96; s c325 noQ0 9.87/10.15/9.54/10.15. Both already include S3. My lead3 is superseded; line closed.
- Next: once chi3/lead3 r56 rungs land, post chi3map result + coverage and lead3 closing coverage. Then decide whether any unique use for remaining ~465 budget (maybe critique/verification).

## 2026-10-14 ~16:45 UTC — wakeup 8
- Posted closing results with coverage: chi3map `20261014T164230.350Z_swarm-aa_result_fe07` (best min 1.7266 5d79; best r46 2.539 90db; 20 PASS/6 FAIL), lead3 `20261014T164249.553Z_swarm-aa_result_9f4b` (best e3a7 STRONG 6.318/7.500/6.877/7.500; 10/1).
- Charged 32/500. Board records now 11–14 (h 5063 11.65/12.30/11.97; s 1c48 noQ0 11.21/11.67/11.60; w 407a 13.93 but qmax unconverged). Open issues: qmax-8 non-PSD pair spectra at R>11 (u → human), r46 manifold gate binds above s21 R≈12 (an), chart-dependent Σ caps (ai/t → human).
- No unclaimed direction needing my budget right now. Watch mode: wake hourly; act if the human answers (caps / qmax) opens new space, or a critique is needed.

## 2026-10-14 ~17:45–17:50 UTC — gate audit (audit-aa), 0 evals
- Board: frontier s21 ~14.9 (aq 7265 = z e327 + S1×T3), w a8eb 15.33/14.68; many agents done. 32/500 charged.
- Did v's (5b45) suggested check across the board: work/egaudit/pull.py → eg.json (243 reqs with s21 ≥ 9), r46fail.json (21 s21-PASS/r46-FAIL).
- Findings: s21c N_A=3 EG has no R trend (Spearman −0.01); it tracks r46/s21 (+0.61). an's 1.0–1.4 EG cases are all r46 manifold FAILs. EG<1.6 catches 21/21 r46 FAILs, with 15/237 false flags. Min r46/r56/conv46 N_A=2 EG 1.80.
- Posted refutation `…174953.073Z_swarm-aa_refutation_d5c3` (critique #1); mailed an, v.
- Next: watch. No new search family is warranted (records are cap-limited; CMA charts by z/n/av cover the frontier). Consider `swarm done` once the remaining r56 rungs land and no reply needs action.

## 2026-10-14 18:51 UTC — done
- Digest: no replies or mail. Frontier at min ~15 (w 256c/4b84, av fd2d), covered by w/av/z. 18 of my r56 rungs are still queued (broker backlog).
- Ran `swarm done` (`…185130.393Z_swarm-aa_note_be3b`) plus a count correction note (37 req / 32 charged / 5 free). Loop stopped.
