# swarm-a notebook

Started 2026-10-14T05:16:46+00:00.

## 2026-10-14 05:22 — wakeup 1
- Read brief, docs 40/46, ADR-0040, kdep_envelope. Board empty; b, c just started.
- Parent w1c s21 Δ = 2.2586e-4. Budget 500 charged evals/agent, ≤32 in flight, deadline 2026-10-16 05:17.
- Wrote `work/build.py` (solver-basis shells S1..S21, T1/T3/T4 = |R|²=1,3,4; build(terms,out)).
- Posted hypothesis 20261014T052038.842Z_swarm-a_hypothesis_67a7: family `amp-map`.
  α=±0.15 on all 30 (S,T) single directions (60 evals), then line search ±0.3/±0.6 on best ≤6, then CMA-ES in span. ≤160 evals.
- Submitted map1a (30 reqs: S12,S13,S16,S19,S1 × T × ±). map1b (S21,S3,S4,S7,S9) still to submit (in `work/map1b/`) when slots free.
- Physics prior: k-dependence breaks vortexability → mostly negative; first-shell amplitude possibly positive.
- Next: submit map1b; collect map → result post; pick line-search directions.

## 2026-10-14 05:37 — wakeup 2
- map1a results: S1 α ±0.15 all <1 (T1 0.950/0.801, T3 0.917/0.976, T4 0.958/0.971, −/+). S12,S13,S16,S19 at ±0.15: 24/24 FAIL (Laughlin destroyed).
- Dropped map1b (0.15 on outer shells pointless). Built map2 (54): S3,S4 ±0.15; S7..S21 ±0.03, all T. Submitted map2a (30); map2b (24) in `work/map2b/` pending.
- Posted interim result 20261014T053706.906Z_swarm-a_result_2178.
- Board: b,c on phase-map (β full shells; duplicate effort); d,e on chiral-phase (mirror-odd β, MT argument). e's leader 5f81 s21 R=1.687 PASS:
  joint-orbit S4 pairs {±(2,2)},{±(2,0)},{±(0,2)} × T1 pairs, antisymmetric β=±0.0245. Checked: it's MT-invariant
  (mirror in solver labels: G(m,n)->(m-n,-n), R(R1,R2)->(R1,-R1-R2); MT: β->-β). Mailed e.
- Symmetry: full-shell α MT-even → TL linear allowed; chiral α → even in TL (skip).
- Tool: `work/collect.py [pattern]` tabulates my requests (cache in work/collect_cache.json).
- Next: submit map2b; finish α coverage; then α map around chiral-phase optimum (combined step) + matched-density control request if positive.

## 2026-10-14 05:52 — wakeup 3
- map2a: all α at ±0.03 on S12–S21 below 1 (best S12T4p 0.990); S13/S19/S21 × T1/T4 FAIL even at 0.03. α sector at the parent = null.
- Submitted map2b (24: S3,S4 ±0.15; S7,S9 ±0.03).
- LEADERBOARD: e's chiral-phase O{1,3,4,9}T1m (mirror-odd joint-orbit β, rms 0.06 rad, β=0.0245/entry) gain 1.5–2.4 on s21/r46/r56; ff86 (O3T1m) and 03b3 (O1T1m) STRONG. conv46 ≈ r46 to 5e-6 (qmax 8→10 negligible for LL0; hashes differ → overrides applied).
- New family `amp-x-chiral` (hyp 20261014T055116.348Z_swarm-a_hypothesis_41f9): α-even gradient around 5f81 (base block saved work/base_5f81.json; build.combine()).
  Submitted x5f81a (8: S1×T1/T3/T4 ±0.05, S3T1 ±0.05). x5f81b (S4T1 ±0.05, S12T4 ±0.02) pending in work/x5f81b.
- Mailed e to send its settled optimum.
- Next: submit x5f81b; post amp-map coverage when map2b lands; α around e's final optimum.

## 2026-10-14 06:10 — wakeup 4
- map2b done → amp-map CLOSED: 84 evals, 36 PASS / 48 FAIL, best 1.0002 (0244 = 20261014T054922.419Z_swarm-a_req_0244, S9T4 +0.03). Coverage posted: 20261014T060704.700Z_swarm-a_result_45fb.
- x5f81 (α around 5f81; 5f81 = s21 1.687 / r46 1.990 / r56 1.832):
  S1T1 m 1.717/2.023, p 1.606/1.944; S1T3 m 1.733/1.985, p 1.732/2.018; S1T4 m 1.658/1.982, p 1.679/1.974; S3T1 m 1.614/2.009, p 1.426/1.880 (s21/r46; r56 pending).
  x5f81b (S4T1 ±0.05, S12T4 ±0.02) submitted.
- OBSERVATION: s21 ceiling ~1.6–1.73 for all small-step β-odd points while r46 1.8–2.5 → s21 is the min-R bottleneck.
- b & d duplicate 12-shell odd-orbit map (identical R). Mailed both (herding critique).
- c's geometry note: w1c Ω very non-uniform (max/mean 15), parent R_staticM2 ≈ 0.12, β-odd shifts Ω_min at first order.
- e asks to wait ~1 h (till ~06:50) for line search to settle before α around new optimum.
- Next: collect x5f81 r56; when e mails leader, α map around it (S1T1−, S1T3±, S1T4, S4T1 best).

## 2026-10-14 06:30 — wakeup 5
- x5f81 final: 4aaa (S1T3 m) and 5a53 (S1T3 p) STRONG (s21 1.733/1.732, r46 1.985/2.018, r56 1.832/1.859) — contain α, not beyond-M2; no control requested (no gain over phase-only).
- c (8879): orbit-resolved α has big slopes (S4T1-SM− 1.37) that cancel in full-shell sum → my amp-map null is full-shell-scoped. Posted correction note f156.
- Agreed split with c: c = α-orbit around c's α point; me = α-orbit around e's β-odd point.
- d moved to ceiling-break (T3/T4 β-odd on 92e8); b holds 12-shell odd orbits; d requested Nk=27 C6v cluster, b requested sector-resolved low_energies.
- build.py now has joint_orbits(skey,pkey) (SM/PM classification, verified S1T1 SM = e's zero set), orbit_block, merge_blocks, write_block.
- e leader 29d3 = O1T1− rms 0.25 (β=0.10206 per entry on two PM orbits of S1T1), s21 1.7347, r46 2.27.
- Submitted: cd56 (diagnostic builder check, expect 1.7347) + 8 probes x29d3/ (α ±0.05 SM on S1/S3/S4 T1, PM-sum S1T1).
- Next: read results; if α-SM lifts s21 above ~1.75, line-search it; else close amp-x-chiral.

## 2026-10-14 06:44 — wakeup 6
- cd56 builder check reproduced 29d3 exactly (s21 1.7347) → orbit_block conventions OK.
- x29d3 (α ±0.05 on one T1 joint orbit, on 29d3): S4SM− b4d4 2.579/3.053; S3SM+ b547 2.227/2.741; S1SM− 0c18 2.099/2.555;
  S1PM+ ac63 1.814/2.382; S1PM− dc16 1.425/2.082; wrong signs FAIL (S4SM+ 0.007, S3SM− 0.68, S1SM+ 1.29F). → ceiling broken; α-SM and β-odd roughly additive.
- c: 87e3 = 7-orbit α combo (±0.025 on S1/S3/S4 × T1/T3/T4 orbits) + O1T1− 0.102 → s21 2.915. Converging on same joint space.
- Posted result 20261014T064323.496Z_swarm-a_result_17a5. Mailed c (proposal: c optimizes joint combo; I do 1-D lines + mechanism controls) and e.
- Submitted y29d3/ (14): S4SM− −0.10/−0.15; S4−S3+; S4−S1−; triple ×1/×2; S9/S12/S16 SM ±; S4SM−0.05 with β-odd rms 0.20/0.30.
- TODO: matched-density control for best α winner (request to human or --control); T3/T4 SM orbits on top of β-odd.

## 2026-10-14 07:00 — wakeup 7
- y29d3 results (s21/r46): tri×2 (S4SM−0.10,S3SM+0.10,S1SM−0.10 + β-odd 0.102) = 2fc4 4.596/5.316 PASS (sp/Δ 7e-5) ← LEADER;
  tri×1 0fd1 3.546/3.832; S4−S3+ 6247 3.297/3.571; S4m10 e1a8 2.919/3.669; S4−S1− 25f4 2.761/3.279; S9SM− 7bbd 2.668/3.361;
  b30+S4− 08da 2.697/3.331; b20+S4− 0e80 2.411/2.702; S16SM− e9ec 2.280/2.960; S12SM+ 23c1 2.174/2.828;
  FAIL: S4m15 (2.87 but sp/Δ .21), S12SM−, S16SM+, S9SM+. b4d4 r56 2.722 conv 3.053 STRONG.
- b: s21 ceiling = 4th level saturating. e: critique 4002 asks for controls; e's CMA fitness counts AMBIGUOUS as FAIL.
- Controls: work/control.py → ρ̄=<ρ_k>_BZ (C6-avg, |G|²≤49) and M2-matched. Submitted --control on s21,r46,r56:
  74b6 (2fc4 meanρ), 5fbd (2fc4 M2-match), 61bd (b4d4 meanρ). Posted request 20261014T070025.983Z_swarm-a_request_4af0.
- Submitted z2fc4/ (17): tri×3, ×2.5, +S9−/S16−/S12+, β 0.30/0.40, penta, T3/T4 SM ± on S1/S4.
- amp-x-chiral spend so far ~61 evals (> declared 50) → post budget update with next result (new cap 150).

## 2026-10-14 07:18 — wakeup 8
- Controls (s21/r46): 2fc4 meanρ 74b6 0.9951/0.9942; 2fc4 M2-match 5fbd 0.9961/0.9960; b4d4 meanρ 61bd 0.9995/0.9994 → beyond-M2 OK (r56 pending).
- z2fc4 1-D: best β-odd 0.163 5a25 5.954/6.312; +S4T3SM+ 2777 5.755/6.035; tri×1.5 4af1 5.085/6.710; outer SM raise r46, lower s21.
- c runs joint CMA (12-D) seeded at 2fc4: 429f 10.78/10.47 already. d: phase-only T3 β-odd lifts s21 (c821 min 1.812).
- Posted result 20261014T071735.514Z_swarm-a_result_e0bf. Submitted g2fc4/ (5 greedy combos: 7028, fb47, f335, 3554, b8d2).
- Roles: c = optimizer; me = 1-D lines + controls. TODO: control for c's best α+β point after r56 (use work/control.py).
- Budget 145+5 charged ≈ 150/500.

## 2026-10-14 07:45 — wakeup 9
- Controls final (s21/r46/r56): 2fc4 meanρ 74b6 0.9951/0.9942/0.9943; 2fc4 M2 5fbd 0.9961/0.9960/0.9958; b4d4 meanρ 61bd 0.9995/0.9994/0.9994. Beyond-M2 confirmed.
- Greedy combos (s21/r46): G1 7028 7.23/7.10; G2 fb47 7.39/7.21; G3 f335 7.94/7.95; G4 3554 7.78/7.51; G5 b8d2 (β 0.225 + S4T3SM+) 8.24/8.19.
- Board: c CMA leader 3b76 (ray t1.5) s21 12.71/r46 12.33, R_beyondM2 1.58; b lead12 (12-shell gradient at 429f); d robustness basin probe; e phase-only CMA ~1.66.
- New family lead6 (hyp 20261014T074226.798Z_swarm-a_hypothesis_0af0): 18 six-shell MT-even coords outside c's CMA at 3b76, ±. 37 inputs in work/lead6 (checks running in background).
- Next: submit lead6 (32-in-flight cap: split 30 + 7), collect slopes, hand to c.
- 07:43 submitted lead6: rebuild 4013 (diagnostic) + lead6a (30). lead6b (6: bOdd S16T1±, S1T3±, S12T1± etc.) pending in work/lead6b.

## 2026-10-14 08:06 — wakeup 10
- lead6 rebuild 4013 = 12.7060 ✓. Slopes at 3b76 (s21 12.706 / r46 12.327), gaining sides: aSM S16T1− 13.90/13.03; bOdd S3T3− 13.21/12.85; aPM S3T3+ 13.19/12.92;
  bOdd S12T1− 13.08/13.37; aSM S4T3+ 13.08/12.84; aSM S9T3+ 13.07/13.07; aPM S4T3+ 13.05/12.48; aSM S12T1+; bOdd S1T3−; aPM S1T3+; aSM S3T4−. T4 flat.
- Submitted lead6b (6 β-odd: S4T3, S9T3, S9T1 ±) and lead6c combined steps C1–C5 (93ca, d66d, 0da0, 582c, 74c3). Σ|α|≤2.5 binds (3b76 at 2.04; C4 2.494).
- Posted result 20261014T080609.051Z_swarm-a_result_04a7; mailed c the coords for v2 span.
- Board: b lead12 combined steps → abf0 15.77/14.61 (leader); c v2 20-D CMA; c claim f286 STRONG for 429f with control 0.989; d basin robustness ok.
- Budget ~191/500.

## 2026-10-14 08:25 — wakeup 11
- lead6b: bOdd S9T3− 13.53/11.90; S4T3− 13.33/12.56; S9T1− 12.39/12.56. lead6c combos: C1 β-only 93ca 14.58/14.14 (best min of mine);
  C3 0da0 15.86/13.52; C4 582c 15.32/13.31; C5 74c3 15.06/12.50; C2 d66d 14.27/13.49. α-SM steps buy s21 more than r46.
- c CMA v3 (30-D trust region in entry space incl. my lead6 deltas) based at 0da0. b abf0 15.77/14.61 (half-step 12-shell gradient).
- d: 3b76 α alone FAIL, β alone 4.47 AMBIGUOUS → synergistic.
- Posted critique 8a9b (s21 overfitting; rank by min(s21,r46)); mailed c (rebase on min; c owns headline control).
- Posted request 091f (Σ|α|≤2.5 binds; widen as diagnostic?).
- Submitted basin2 (6): β-odd O3/O4/O9 T1 at rms .25 alone and + tri(2) α-SM → is the recipe generic beyond O1T1? (5617 3a40 351c 5fb5 475b 8988)
- Budget ~197/500.

## 2026-10-14 08:48 — wakeup 12
- basin2: O3T1 β .25 + tri2 3a40 7.47/7.84 PASS; O4T1 + tri2 5fb5 8.34/8.67 PASS; β alone O3/O4 FAIL; O9 alone R 9.1 FAIL (other phase); O9+tri2 FAIL.
  → recipe generic; α widens Laughlin basin. Posted 20261014T084700.200Z_swarm-a_result_7151.
- 93ca conv46 14.13 (min 13.53 r56); 0da0 conv46 13.44 (min 13.44). conv46 departs from r46 by ≤0.6%.
- c: v3 fitness now min(s21,r46), owns headline control. d: min-es around abf0. Leader by min: c 262f 17.17/16.42/15.90.
- Building outer/ probe at 262f (S12,S16 × T3,T4 + S9T4; α-SM ±0.015, α-PM ±0.008 (Σ|α| boundary), β-odd ±0.015) = 30 + rebuild. Checks running in background (Monitor).
- 08:5x submitted outer probe at 262f: rebuild (diag) + 30 (outer_sub/).

## 2026-10-14 09:15 — wakeup 13
- outer probe at 262f: rebuild 9f84 = 17.1714 ✓. s21 slopes small (+1–3%): bOdd S16T3− 17.72, S12T3− 17.66; aSM S16T4− 17.49, S12T3+ 17.45, S16T3+ 17.43, S12T4− 17.36, S9T4− 17.33; β-odd T4 loses. r46 pending.
- Submitted outerc combined: eede (β S16T3−+S12T3− ×1), e6d9 (×2), 49c6 (+aSM S16T4−).
- Board: c controls for all α leaders 0.982–0.9995 (bacb); d min-es plateau around abf0; b 12-shell probe at 262f (17.87 s21); e MT-odd hessian at abf0.
- Leader by min: c 0bd5/262f 17.17/16.42/15.90 (conv 16.35).
- TODO: coverage posts for amp-x-chiral, lead6 (+outer), basin2. collect.py is slow (swarm show per pending req) — run in background.
- Budget 230/500.

## 2026-10-14 09:22 — wakeup 14 (session restarted; resumed from notebook)
- outer at 262f r46: no direction raises r46 (best 16.428 vs 16.418); β-odd S16T3−/S12T3− raise s21 +3% but r46 −13%; S12T4− r46 −24%. → overfit. Withdrew eede, e6d9, 49c6.
- Posted result 383e; coverage posts: amp-x-chiral b9a1, basin2 ae48, lead6 (just now). All my families closed.
- collect.py now prefilters by pattern (fast).
- Budget ~233/500 charged.
- Open: request 091f (Σ|α| widen?) awaiting human; request 4af0 (control definition) awaiting human.
- Next: decide whether to continue (low-marginal: optimizers b/c/d saturating) or go to low-cadence watch + verifier role.

## 2026-10-14 09:53 — wakeup 15
- All agents closed families; c claim a609: 0bd5 STRONG 17.17/16.42/15.90/conv 16.35 (Σ|α| boundary; control 0.995/0.992). e: abf0 local max in MT-odd directions.
- b critique 8c94: ladder clusters = selection set; r56/Nk=27 hold-out; frontier as band 15–16. Mailed agreement.
- Waiting on human replies (091f Σ|α|; 4af0 control definition; d's Nk=27 2225). Low cadence (1 h). If no reply after ~2 more checks → swarm done.

## 2026-10-14 10:54 — wakeup 16
- b, c, d, e are all `done`. No human reply to 091f, 4af0 or 2225.
- d c643: 262f robust ±0.3% at r56 (15.88–15.95); frontier band ≈15.9 (r56) to 16.4 (r46).
- My outer probe at 262f is laddering for free:
  - f4a1 STRONG 17.49/16.25/16.03/conv 16.14.
  - b659 STRONG 17.33/16.34/16.01/conv 16.21.
  - 15 more are pending at r56.
  - Both STRONG points are inside the band; they are perturbations of 262f, not new optima.
- Plan: wait for the r56 results (free), then post a lead6-outer coverage addendum and run `swarm done`. No new charged evals.

## 2026-10-14 11:55 — wakeup 17 (final)
- Outer probe at 262f, r56 hold-out:
  - α steps are flat at 15.61–16.03 (f4a1 16.03, b659 16.01 STRONG).
  - β-odd steps fall to 14.8–15.05.
  - Nine requests are pending at r56; r46 caps their min at ≤15.55.
- Posted addendum 20261014T115609.681Z_swarm-a_result_3b77. Ran `swarm done` with summary (work/done.md). Loop stopped.
