# swarm-a notebook

Started 2026-10-14T10:23:49+00:00.

## 2026-10-14 11:13 — wakeup 1
- Read brief, docs 40/46, key-facts, ADR-0040, kdep_envelope. Board was empty (I am first active agent).
- Parent w1c gaps: r56 = 2.590e-4 PASS; s21 etc pending at start.
- Posted hypothesis 20261014T111220.783Z_swarm-a_hypothesis_163c: family `axis-map`, all 60 single-coefficient
  axes (S1..S10 × T(|R|²=1,3,4) × α/β), α=±0.05, β=±0.03, 120 evals, then gradient ascent + CMA (≤150 more).
- Tools: work/gen.py (stars, make()), work/mk_axes.py → work/inputs/axes/ (+ axes_chunk0..3, 30 each).
  NAMING: file `T1/T3/T4` = |R|²=1/3/4 = brief's T1/T2/T3.
- Submitted axes_chunk0 (30 req). Next: submit chunks 1-3 as slots free (cap 32 in flight).

## 2026-10-14 11:40 — wakeup 2
- Board exploded (≈45 agents). Leader: swarm-c jorb d698 = single chiral joint orbit S(|G|²=3)×T1, β=0.03/entry,
  phase only: s21 1.249, r46 1.404 (PASS). Joint orbits >> separable stars (separable = cancelling sum of 3 orbits).
- MT symmetry (d/f): separable β axes even in TL; only chiral-odd β linear. My β pairs confirm (even).
- Axis map 91/120: S1 ±0.05 mild (best α[S1,T1]=-0.05 +0.8%, α[S1,T2]=+0.05 +1.1%), S3/S4 lose 5-20%,
  |G|²≥7 at 0.05 collapse (R 0-0.5, FAIL). Posted note …note_8d6a (outer shells non-perturbative).
- swarm-b duplicated the axis map (linmap). Mailed b, c, d, f, m.
- New family `outer-chiral` (hyp …hypothesis_f330): 45 outer chiral-odd β mirror-pair directions, b=±0.002/entry
  (rms Imγ 0.0049), 90 evals. work/orbits.py (joint orbits), work/mk_outer.py → inputs/outer1. Inner 9 left to f.
- Next: post full axis-map table + coverage when last 29 land; analyse outer-chiral slopes; stage 2 line scans.

## 2026-10-14 12:05 — wakeup 3
- Herding: outer chiral-odd β claimed by ap (11:36, before me), ac, aq, as, + at/an (at-leader). Mine already charged
  (90). Posted dedupe note …note_d15a with construction/sign convention (+b on orbit with δ<90), mailed ap/ac/aq/as/an/ab.
- swarm-c posted STRONG phase-only claim (S2×T1 +60° β=0.03: 1.249/1.404/1.347). f: inner chiral-odd β S3×T1 +0.05 → s21 1.558, r46 1.641.
- Axis map: 115/120; outer separable axes all collapse at 0.05 (R→0 for S13,S19,S21). Waiting on β[S21,*] to post table.
- Thought: outer-shell sensitivity plausibly = band distance (e^{iGr}ψ nearly orthogonal to LLL for large G), breaks ideal-band zero mode.

## 2026-10-14 12:32 — wakeup 4
- Posted axis-map result + coverage: …result_8d36 (120 evals, best 1.0109 e6d6, 40P/80F). Axis-map DONE.
- outer-chiral: 0/90 landed yet (broker queue congested). Dedupe worked: ap, ac, aq, as ceded outer odd-β map to me.
- Board: f STRONG claim S(|G|²=4)×T1 chiral-odd β 0.05: 1.558/1.641/1.560, conv46 1.641. c STRONG 1.249/1.404/1.347.
  h: outer |G|²=7 (their S4) α orbit contrast at T1, rms 0.025 → 1.572/1.720/1.614. j: α⊥ S1×T1 -0.45 → 1.64/2.63/2.44.
  at: screen g_cutoff 8 loses 7-9% of first-order kernel change for |G|²=19,21 deformations → my outer slopes on those biased low.
- Next: analyse outer-chiral slopes (slope per unit rms), post result; stage 2 line scans of top 3-4 + combine with f's leader e5d5.

## 2026-10-14 13:00 — wakeup 5
- Board records: orbsurr (t) 8c01 s21 4.82 / r46 5.19; h union α+β s21 4.76 (c662); j STRONG α⊥ -0.45 1.64/2.63/2.45/2.63;
  ae S2×T1 odd β 0.03 → 1.687/1.989. Combos strongly superadditive. Mechanism: k/u say not density, not interaction scale;
  c: leaders restore M2 law (R_beyondM2 0.12→0.72), not exceed it. g critique (d_sc amplifier) vs p rebuttal.
- outer-chiral 6/90 landed: b=±0.002 (rms .005) already moves R by −11…+1% → big linear slopes (S7T1 δ49 − : 0.890).
- Next: full slope table; stage 2 = line of best outer odd-β dirs + add to record point (coordinate with at/an 'dress').

## 2026-10-14 13:27 — wakeup 6
- outer-chiral 17/90 landed (queue slow). STRONG claims now: c662 (h) 4.76/5.23/4.67, 8c01 (t) 4.82/5.19/4.55; density controls ≈1.
  conv46 == r46 to 4 digits for both (not independent; l already noted). r46/r56 spread ~13% at records.
  ap: leaders' γ on uniform LL0 lowers gap → gain needs γ×ρ* cooperation. g retracted 1/d² amplifier critique.
- No critique posted yet from me; look for a genuine one (not forced).

## 2026-10-14 14:00 — wakeup 8
- outer-chiral 40/90: T1 outer odd β all positive for +b (δ<90 orbit +), +4..+12% at rms .005, slope ~21-25/rms, convex;
  T3 (|R|²=4) opposite sign, T2 weak concave. Posted interim result.
- Records now f5f1 (o) 6.28/8.33/8.12 near Σ|β| cap. Many agents finishing (d, ak, p, g done).
- Submitted stage 2a: top-4 T1 dirs at b=.005/.01/.02 (inputs/outer2a, 12 req).
- Next: coherent slope-weighted outer-T1 odd-β direction (after |G|²16/19/21 land), then add to 8c01/c662.

## 2026-10-14 14:33 — wakeup 9
- Records now R≈10 at s21 (av e0a8 10.39/9.87/10.50; s c325 9.87/10.15/9.53). Records cap-limited (Σ|α|,Σ|β|). aq mapped outer T1 odd β at ±0.01 (sign sin2δ); at: outer β adds at inner leader 55-85%.
- Stage 2c submitted: coherent outer-T1 sin2δ β (15 pairs, ΔΣ|β|=62.8c) added to e0a8 (c=.0019/.0038/.0054) and c325 (c=-.0038,.0038,.008,.0127,.0167). work/mk_rec_outer.py. Posted note.
- Budget: 230 charged. Remaining queue: ~70 outer stage1 + 12 lines + 8 records.

## 2026-10-14 15:07 — wakeup 10
- outer-chiral stage 1 COMPLETE 90/90 PASS. Law: slope = A_T sin2δ, shell-independent; A_T1=22.6, A_T2=4.7, A_T3=-7.4 per unit rms Imγ.
  Posted …result_35cc with full table. work/outer_rows.json, outer_table.md.
- b mailed: overlap on c325 (b's density-weighted outer sin2δ vs mine shell-uniform) → replied: complementary, no more on c325/f5f1.
- Records: h un3_B s21 11.07; s c325 STRONG claim 9.87/10.15/9.53/10.15; av e0a8 STRONG 10.39/9.87/10.50/9.96. u: qmax-8 non-PSD for R≈13 records, asks qmax≥12.
- Pending: 12 line scans + 8 record points. Then coverage post and probably done (~240 charged).

## 2026-10-14 16:31 — wakeup 11
- Budget 220/500 charged (some dups free).
- Stage 2a lines: single outer T1 β pair: S7 δ49 b=.02 → s21 1.682 / r46 2.238 PASS (4f0f); S9 δ30 b=.02 → 1.619/2.196 (c745);
  S12/S13 at b=.02 FAIL (split). b=.01 all PASS ~1.50-1.53 / r46 1.58-1.76.
- Stage 2c records: c325 local max (both signs lose; + breaks gate); e0a8 +0.0019 s21 10.75 but r46 FAIL. Outer β spent at records.
- Posted …result_88e1. Next: wait r56 for 4f0f/c745 (+ b6f7 etc.); if R_r56≥1.1 & conv46 → claim (phase-only, outer-only). Then coverage + done.

## 2026-10-14 17:00 — wakeup 12
- r56 promotions of my 22 stage-1 + 10 line points still pending (5×6 queue). b's density-weighted outer sin2δ lifted c325 to min 10.105
  (7e78) while my shell-uniform version broke the gate → at records outer β must be weighted by parent shell weight (w_s/w_1).
- Board records now ~11–14 (h 5063 11.65/12.30/11.97; w 407a 13.9 but qmax unconverged). Many agents done.

## wakeup 13 (2026-10-14 18:44)
- Digest: 31 new posts (mostly closing summaries; frontier now w rec-out ~15.2 r46, z e327 STRONG min 14.23, av 023e STRONG). No mail.
- My lines still waiting on r56 (slow lane); 875a STRONG (7.02 min). Nothing new to act on; no new critique target not already raised (u covered qmax class of new frontier, aq self-flagged 4792's +1%).
- Next: wait for r56 on 4f0f/c745 etc., then claim (if ≥1.10 PASS) + final coverage + done.

## wakeup 14 (2026-10-14 19:45)
- Digest: 20 posts (closing summaries; ab chiral-quad phase-only frontier b081 2.05/2.29, f chiral-joint phase-only optimum ~1.88 s21 / best STRONG min 1.715; w 256c STRONG min 15.09; av fd2d STRONG 14.16; z rcma s21 ~16.7 pending r46). No mail.
- 4f0f r56 state SUBMITTED (queued). Still waiting; nothing else to act on.
- Note for final coverage: my phase-only lines (single outer pair, Σ|β| 0.12) reach r46 2.24 — comparable with ab/f phase-only frontier, and on outer shells only.

## wakeup 15 (2026-10-14 20:31)
- Digest: 4 posts (w, av, ab final summaries). r56 for my 32 lines still SUBMITTED.
- Posted final outer-chiral coverage now (result 20261014T203137.412Z_swarm-a_result_52f3): 110 req, s21 103/0/7, r46 33/0/2, r56 1/0/0 (32 pending). Counts from `swarm status` (work/status_all.txt).
- Remaining: wait for r56 on 4f0f/c745/cf0c/b6f7/2eae/0ad2; if ≥1.10 & PASS → claim (STRONG needs r46,r56 ≥1.10; also check conv46). Then swarm done.

## wakeup 16 (2026-10-14 21:32)
- Digest: z d7f2 STRONG min 15.99 (new top). r56 for my 32 still queued.
- Tried `swarm withdraw` on the 22 stage-1 (b=.002) r56 promotions to move them behind the lines; the harness permission check denied it. Not essential; left as is.
- Waiting on r56 of lines (4f0f, c745 lead).

## wakeup 17 (2026-10-14 22:33)
- ag note 78b2: r56 lane backlogged, asks withdrawing non-elites. Retried withdraw with explicit IDs → OK: 22 stage-1 probes withdrawn. Note posted. 10 line points still on r56 lane.
- z d7f2 density control ≈1.004 → beyond M2.

## wakeup 18 (2026-10-14 23:34)
- Quiet: no new posts from others, no mail. 10 line points still queued for r56. Waiting.

## wakeup 19 (2026-10-15 00:33)
- ag 353d: phase-only points far from parent have r56/r46 ≈ 0.71–0.78, some r56 manifold FAILs; best phase-only claim-metric min 2.106 (8172). Expect my 4f0f r56 maybe ~1.6–1.8 (r46 2.24) — claim threshold 1.10 still likely, but must check r56 gate verdict. My r46>s21 pattern at b≥.01 is the same kind of r46 overstatement; say so in the claim.
- z closed (plateau ~16.0). Still waiting on r56 of 10 lines.

## wakeup 20 (2026-10-15 01:34)
- Quiet: no posts, no mail; 10 lines still queued r56.

## wakeup 21 (2026-10-15 02:35) — FINAL
- r56 landed: 4f0f 2.069 PASS (STRONG 1.682/2.238/2.069/conv46 2.238), c745 2.046 PASS (STRONG). r56/r46 0.92–0.93; s21 binds.
- Posted claim 20261015T023556.086Z_swarm-a_claim_89fd; mailed swarm-ag (r56/r46 contrast to their CMA drift).
- swarm done posted (220/500 charged). Loop stopped. 8 line r56 promotions remain queued (free).
