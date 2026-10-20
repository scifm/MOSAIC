# swarm-b notebook

Started 2026-10-14T05:16:49+00:00.

## 2026-10-14 05:25 — wakeup 1: scope chosen, phase map submitted
- Read brief, docs 40/46, ADR-0032 deformation schema, src/swarm/validate.py.
- Board: swarm-a took `amp-map` (α ±0.15 over 30 (S,T)), suggested phase-only map to others.
- Posted hypothesis 20261014T052146.442Z_swarm-b_hypothesis_368c: family `phase-map`, ≤220 evals:
  map β=±0.15 over 30 (S,T) → line search ±0.05/±0.3 on ≤6 best → cos·cos joint-orbit phase terms
  (diagonal β over pair stars, 3 relative orientations) → CMA-ES σ0 0.08 in best span.
- Facts: phase-only ⇒ m2k ratio exactly 1, admissibility = parent. Amplitude α=±0.6 on S1T1 gives
  m2k ratio 0.95 (<1!) — amplitude does NOT trivially raise M2^(k) for this sharp parent.
- Block schema can only express products of real cosines; true joint orbits need sin·sin too (flagged in post).
- C6 maps: G (m,n)→(m−n,m); R (R1,R2)→(−R2,R1+R2).
- Tools: work/gen.py (S(i), T(p), make, write). Inputs under work/inputs/map.
- Submitted 60 map requests (b_S{s}T{p}{p|m}), ids 052316..052353.
- Next: collect map, post result, choose line-search directions; build joint-orbit inputs.

## 2026-10-14 05:55 — wakeup 2: map dead, pivot to odd-orbit12
- Map: all 60 full-shell β=±0.15 FAIL (table work/map_table.txt). R(+)≈R(−) where gap survives → MT evenness
  (swarm-d/e argument) confirmed. Posted result 20261014T054840.951Z_swarm-b_result_2ea2 with coverage.
- Board: swarm-e's mirror-odd joint-orbit β (P−MP orbits of 6-member shells, rms 0.06) gives R 1.3–2.4 and
  a STRONG claim already (ff86: s21 1.62, r46 1.79, r56 1.67, conv46 1.79; 03b3 strong at 1.26–1.28).
  swarm-c duplicates phase-map at ±0.10 (mailed). swarm-a: S1 α concave, outer α ≥ 0.15 destroys Laughlin.
- conv46 ≈ r46 to 5e-6 relative (qmax 10 / mesh 64 / cutoff 10) — different hashes, so genuinely converged.
- New family odd-orbit12 (hyp 20261014T055248.990Z_swarm-b_hypothesis_6199): 12-member shells have 6 joint
  orbits per T → 3 odd directions; chiral halves (d/e) = their sum. 72 inputs J{g}R{r}o{idx}{p|m}, rms 0.06,
  submitted. Tools: work/orbits.py (odd_input(g,r,idx,rms)), work/table.py <pattern>.
- My (1,T1) odd dir = −1 × e's O1T1m (so my "p" ≈ e's winning "m" sign convention there).
- Next: tabulate J*, slopes; line search top ≤6 at rms 0.12/0.2/0.3; consider joint CMA-ES with e's O-dirs.

## 2026-10-14 06:22 — wakeup 3: 12-shell map done, line search + cross combos
- 12-shell map (work/h12_table.txt): T1 winners J7o0m 1.612 (r46 2.475), J7o2p 1.631 (r46 1.986), J7o1p 1.492,
  J13o1p 1.420 (r46 2.00), J13o2p 1.432, J19o1p 1.270. T3/T4 never gain. 15 P / 57 F total. Strongly
  nonlinear: losing side ≪ 2−R. Posted result 482d (+ two count corrections 3987, 75b9 — be careful counting!).
- swarm-d ran identical map (free by hash). Proposed split by mail: b = 12-shell line search + 6×12 cross combos.
- Board: s21 ceiling ~1.73 (e's O1T1− rms 0.25 = 29d3; 0.20 = 92e8 1.711). a: amp-x-chiral (α on top of e's).
  c: orbit-amp (orientation-resolved α, S4T1-SM− 1.37). Posted request for sector-resolved low_energies.
- e's O1T1m(rms) == my odd_entries(1,1,0,−rms) (verified vs 92e8 input).
- Submitted ls1 (26): {6 winners}×rms{0.03,0.12,0.2} + E20(=e O1T1− 0.20)+winner@0.06 (6) + E20+J7o0m/J7o2p@0.12.
- Budget after: 158/500.

## 2026-10-14 06:48 — wakeup 4: ls1 results; ceiling diagnosis
- ls1 (work/ls1_table.txt): 12-shell dirs steep (J7o0m 1.598 at 0.03); all cap ≤1.63 s21 then manifold breaks.
  0.20 points → AMBIGUOUS 4.3–5.7 with PES gap ~0.2, s21c FAIL = other phase.
  6×12 combos on 92e8: only +J7o1p (1.644, r46 2.53) and +J19o1p (1.544) keep manifold; none beat 92e8 on s21.
- Diagnostic (work/e4e1.py): (E4−E1)/Δp on s21 saturates ≈1.80 while r46 tracks to 2.5 → ceiling is 4th level
  (plus splitting). Posted result 20261014T064652.842Z_swarm-b_result_5f99.
- Roster: d=ceiling-break (T3/T4 β-odd around 92e8, Nk=27 request), a=α-SM around 29d3, c=α×β-odd combos,
  e=CMA 5-D 6-shell T1-odd. Everyone on the ceiling → I'm holding spend; family odd-orbit12 nearly closed.
- Next: once r56 lands on promoted 12-shell points, post coverage block; check human response to 219c.

## 2026-10-14 07:25 — wakeup 5: frontier moved to α-orbit ⊕ β-odd; lead12 probe
- Board: a found α self-mirror-orbit + β-odd breaks s21 ceiling (b4d4 2.58/3.05/2.72; 2fc4 4.6/5.3);
  c's joint CMA 429f: s21 10.78 / r46 10.47 / r56 9.68, PES ≈ 3.8, C=1, admissibility 0.079.
  Matched-density controls (a, c) give R≈0.995 → beyond-M2. AMBIGUOUS high-R points (PES ~0.2) = other phase.
  d: phase-only frontier c821 min 1.81 (T3 β-odd on 92e8).
- My contribution: lead12 = 12-shell α-even (P+MP) orbits (|G|²=7,13 × T1,T3 × 3, ±0.03/entry) and 12-shell
  β-odd T1 (J7 o0-2, J13 o1-2, ±rms 0.03) on top of 429f + exact rebuild. 35 inputs work/inputs/lead1.
  orbits.py: parse_block, even_entries, ab_input (g_cutoff 8), add. Mailed c.

## 2026-10-14 07:52 — wakeup 6: lead12 slopes landed
- All 35 PASS (work/lead1_table.txt); rebuild a74b == 429f exactly. Big 12-shell α-even slopes at 429f
  (J13R1o1 +2.41/0.03, J7R1o1 +1.79, J13R1o2 −1.52, J7R3o0 +1.49, J13R3o0 +1.47, J7R1o2 −1.45) and β J7o0 −0.97.
  Best: b115 (α J7R3o0 +0.03) 11.87/11.83/11.37; c282 11.72/11.66/10.90. Posted result f861, mailed c coords.
- c's gen-1 best 56ea 12.67/11.61; Σ|α| ≤ 2.5 is c's binding constraint.
- Submitted lead2 (7): combined gradient steps G429f_{B1,A06,A06B1,A03B05}, G56ea_{B1,A06B1,A03B05}
  (BETA 5 coords @0.03×sb, ALPHA 6 coords @0.03×sa; see work/mk_lead2.py).
- Budget ≈ 200/500.

## 2026-10-14 08:22 — wakeup 7: combined steps work
- lead2: 56ea+A03B05 abf0 15.77/14.61 (best on board s21/r46), 429f+A03B05 453c 14.37/13.79; A06B1 FAIL (split);
  B1 alone ≈ no gain; A06 alone 12.92 (sp/Δ 0.08). Posted result 85b3, mailed c.
- c: 3b76 STRONG 12.71/12.33/12.14 (Σ|α| 2.04), c12e 13.54; c v2 20-D CMA includes my 6 α + β J7o0.
  a: lead6 at 3b76 (S16T1 α-SM− 13.90). d: robustness 429f basin ±4%.
- lead3 (8) in flight: 56ea t=0.3/0.4/0.6 (sa=0.6t, sb=t), A03, B05; 3b76 t=0.3/0.4/0.5.

## 2026-10-14 08:56 — wakeup 8: abf0 STRONG; probe at 262f
- abf0: 15.77/14.61/14.66/conv 14.65 all PASS C=1 → strong (min 14.61). 453c 14.37/13.79/13.51/13.80 strong.
  Ray on 56ea t=.3/.4/.5/.6: s21 14.64/15.23/15.77/16.25; r46 13.80/14.36/14.61/14.30 → abf0 is ray optimum for min.
  3b76 ray t=.3/.4/.5: 14.25/14.61/14.88; r46 13.84/13.98/13.72.
- Leader now c's 262f 17.17/16.42/15.90/conv16.35 (Σ|α|=2.45 boundary). d runs min-es on abf0's orbit groups
  (0889 16.1 s21). a: overfitting critique 8a9b (rank by min(s21,r46)); request to widen Σ|α|.
- lead4 (36) at 262f: α-even J19/J21 T1, J7/J13 |R|²=4, ±0.008/entry; β-odd J19/J21 T1 ±rms 0.03.
  Hypothesis 23db. Budget ~244/500 after.

## 2026-10-14 09:25 — wakeup 9: lead12 closed
- lead4 at 262f (36, all PASS; work/lead4_table.txt): small slopes; best 4437 (α J19R1o1+) 17.82/16.56/r56 15.96.
  Outer β-odd moves s21/r46 oppositely. Posted closing result e75c with lead12 coverage (86 evals, 84P/2F).
- Posted critique 8c94 (ladder clusters = selection set; r56 + Nk=27 as hold-out; quote band). Mailed a, c, d.
- c: matched-density controls for all α leaders R 0.982–0.9995 (bacb). 262f/0bd5 STRONG min 15.90.
- Budget 244/500. My sectors (phase-map, odd-orbit12, lead12) closed. Remaining options: verifier role
  (hold-out once Nk=27 available), or swarm done if nothing distinct remains.

## 2026-10-14 09:58 — wakeup 10: done
- All agents closed families. Posted odd-orbit12 final coverage a9b1 (+ correction 57ba: ls1 counts 9/3/14).
- Ran `swarm done` with summary. Budget 244/500. Open: request 219c (low_energies).
- Lesson: always compute pass/fail counts with grep on the table BEFORE writing a coverage block (3 corrections posted).
