# swarm-au notebook

Started 2026-10-14T10:26:39+00:00.

## 2026-10-14 11:38 — wakeup 1
- Read board: leaders are swarm-c joint orbits (S2×T1 +60 β+0.03 → s21 1.249, r46 1.404; d698). ~20 agents herd on S1/S2×T1 orbits.
  swarm-e: manifold breaks at |β|≈0.12, |α|≈0.1 on full stars → keep steps small.
- Chose family `harmladder`: add (2G,R),(G,2R),(2G,2R) harmonics at same chiral angle to 4 leaders
  (s2o60 β, s1o30 β, s2par α+, s2o60 α−). Generator work/ladder.py (pair stars, swarm-c matchings).
- Hypothesis 20261014T113735.668Z_swarm-au_hypothesis_28c0. Submitted b1 (28 s21 evals, 4 base reproductions).
- Mailed swarm-ae re overlap on S2×T3 β.
- Next: read b1 results; 4-D local ascent on live harmonics.

## 11:55 — wakeup 2
- Base reproductions hashed to existing evals (free): d698 r56 1.3465, ce1f r56 1.1492, 37dc r56 1.2761, ad6b r56 1.2190.
- b1 ladder gradients still running (8 charged so far).
- Board: swarm-f chiral-odd β (o+30 +b, o150 −b) S3×T1 b=0.05 → s21 1.558, r46 1.641 (e5d5); S2×T1 odd 1.483. S3 = 2×S1, so my s1o30 c21 is half of that.
  swarm-u: |G|²=3 leaders eat 30–50% of the s21 splitting gate.
- swarm-ao ceded T1+T3 β of s2o60 to me (c12).
- Idea for stage 2: chiral-ODD versions of the ladder (both mirrors with opposite β), since odd = TL-linear and cleaner.

## 12:15 — wakeup 3
- b1: all 24 charged, none finished (broker heavily loaded). Waiting.
- Board: claims STRONG by c (d698, S2×T1 +60 β 0.03: 1.249/1.404/1.347) and f (e5d5, S3×T1 chiral-odd β b=0.05: 1.558/1.641/1.560).
  ⊥ α line −0.45: s21 1.64, r46 2.63, r56 2.44 (j); s21 splitting gate binds. h: S4×T1 α contrasts ~1.57/1.72/1.61.
  conv46 ≡ r46 for S1–S3 deformations (l); g_cutoff 8 truncates S9/S10 by 7–9% (at).

## 12:41 — wakeup 4
- b1 still all pending (>1 h). Queue is the bottleneck.
- Board moved far: h union α+β step s21 R 4.76 PASS (c662), t orbsurr 4.816 (8c01); α·β superadditive. j STRONG ⊥ α −0.45 (2.63 r46).
  k/u: gains are not density or interaction-scale. e: PES ent. gap drops 13→4.
- Plan: when b1 lands, post ladder gradients as new coordinates (S3/S6 2G, T3 2R) for h/t surrogates; possibly test the best harmonics AT the record point (c662/8c01).

## 13:12 — wakeup 5
- First b1 results (s1o30 β leader base 1.1595): c12− (S1×T3 +30 β −0.015) 1.1846 (r46 pending); c12+ 1.1041; c21− (S3×T1 +30 β −0.015) 0.8984. T3 sign opposite to T1 (agrees with av's cos2δ/sin2δ note).
- Board: h STRONG c662 4.76/5.23/4.67, density control 0.995 (k). t 8c01 s21 4.82/r46 5.19. aa adds S3×T1 odd β at record, aq S1×T3 at record, w/x outer α at record.
  -> "harmonics at the record" is mostly taken; remaining from my ladder: S6 (2G of S2) and S2×T3/S3×T3 at record. Decide after b1.

## 13:43 — wakeup 6
- b1 22/24 landed. Posted result 20261014T134413.305Z_swarm-au_result_962c (coverage included; 2 pending 5409/b31d).
  S2 leaders: all harmonics lose both signs (S6 2G most destructive; S2×T3 loses). S1o30: +S3 (2G) 0.015 → s21 1.236 / r46 1.405 (d049); T3 opposite sign helps a bit (cff3 1.185/1.207).
- Record c662: R_beyondM2 0.72 at r46 (c's note: gains restore M2 law; parent was 0.12).
- Next: harmladder S2 ladder closed; S1 ladder at record covered by aa/aq. Need a new direction — look for gaps on the board next wakeup.

## 14:10 — wakeup 7
- b1 complete: s2par c22− 0.1649 F (5409), c22+ 1.0039 (b31d). Posted abandon 20261014T141052.112Z_swarm-au_abandon_e161 with coverage. 24/500 charged.
- Board: record f5f1 (o) 6.28/8.33/8.12/8.33 STRONG, Σ|β| 1.88 of 2.0 cap; t asked the human how to read the representation-dependent caps (789e).
  f5f1 already has S3×T1 odd β and S1×T3 β with opposite sign, plus ⊥ α on S1×T1/S2×T2/S3×T3 (Q=0). o's own no-⊥ ablation (07f8) and k/i density controls are queued, so no f5f1 ablation from me.
- Many agents done (d, ak, p, g, aj, q). The swarm is saturated near the records.
- Plan: wait for the human's answer on the caps (a new search space may open) or a request for verification help; critique when there's a claim nobody has checked.

## 14:55 — wakeup 8: DONE
- Board records now R≈10 (av e0a8 STRONG 10.39/9.87/10.50, s c325 noQ0 STRONG 9.87/10.15/9.54), cap-limited; all heavily verified.
- No unclaimed direction where my evals add value; ran `swarm done` with the summary (work/done.md). 24/500 charged.
