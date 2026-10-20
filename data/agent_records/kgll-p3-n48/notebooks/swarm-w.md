# swarm-w notebook

Started 2026-10-14T10:25:07+00:00.

## 2026-10-14 11:30 — wakeup 1: scope chosen
- Board: c's single joint orbits give big linear s21 responses (S1T1 ⊥ α−0.05 → 1.171; S2T1 δ0 α+0.05 → 1.217; β on ±30° chiral orbits ±16%). Separable stars ~1%.
  Herd on S1–S3 orbits: c, g, f, j, r, q, x, h. d = chiral half-shell β; h = S4–S6 even-α contrasts + union model; k = mechanism verifier; s = ⊥ channel = static LL mixing note.
- My family `hs-orbit`: mirror-even α orbit directions on S7–S10 × T1–T3 (33 dirs, ±0.05/entry, 66 evals). Hypothesis 20261014T112755.487Z_swarm-w_hypothesis_eec3. Mailed swarm-h.
- Tools: work/hs_gen.py (orbits, even_dirs; geometry G1 0°, G2 120°, a1 30°, a2 90°), work/tab.py (tabulate ids files).
- Submitted q1 (T1, 22 reqs) → work/hs/q1_ids.txt. Next: q2 (T2), q3 (T3) as slots free (32 max in flight).

## 2026-10-14 11:52 — wakeup 2
- Collision: swarm-v (hi-orb) claimed the same S7–S10 even α 5 s after me (orthonormal contrasts, rms 0.025). swarm-a note: outer shells (|G|²≥7) at ±0.05 are already in the collapse regime (FAIL, R 0–0.5); step ≲0.01 needed.
  → STOPPED my batch at the 32 in flight (q1 + q2a); NOT submitting q2b/q3. Mailed v (linear map is yours) and h.
  My 32 = Laughlin-window boundary data (rms Re γ ≈ 0.06 on 12-member shells). Post them as a result when they land.
- Board state: leaders at s21 1.64 (⊥ channel, large amplitude: j/r/q). Chiral phase orbits transfer (r46 > s21, per swarm-p). conv46 ≡ r46 for pure LL0 (swarm-l).
  Holes (swarm-p): verification package (p took it); inner+outer combos; large-amplitude non-⊥ α orbits (s, x partly).
- Pivot candidates: (a) outer even-α gradient at small step measured AT the inner leader (complements at/an who do outer β there); (b) critique/audit.

## 2026-10-14 12:20 — wakeup 3
- swarm-v ceded S7–S10 α to me (their 32 at rms 0.025 contrasts S7/S8/S10 × T1–T3 still land; S9 withdrawn).
- KEY: swarm-h result 282d: outer α contrasts at T1 (S4–S6, rms 0.025) give +50 % PASS that transfers (S4T1 c0+ 353f: 1.572/1.720/1.614). T2/T3 copies are flat/negative. So outer T1 is live, not dead.
- Board: STRONG claims: c d698 (S2×T1 +60 β 0.03: 1.249/1.404/1.347), f e5d5 (S3×T1 chiral-odd β 0.05: 1.558/1.641/1.560, conv46 1.641). ⊥ α −0.45: 1.64/2.63/2.44 (j). density controls (k) say gains not density.
- My S10×T1 at 0.05/entry: FAIL (R 0.07–2.74, other phases).
- Plan: when my + v's data are in, run S7–S10 × T1 even directions at a step inside the window (rms ≈ 0.0125–0.025), then line scans on the live ones; S9 blocks too.
- Submitted r1: S7–S10 × T1 even dirs at rms 0.0125 (22 reqs) → work/hs/r1_ids.txt. Charged now 54.

## 2026-10-14 12:50 — wakeup 4
- q1/q2a (0.05/entry) all landed: all FAIL (window edge). T2 S7/S8 collapse to R≈0. T1 FAIL with big gaps (other phases): S9T1 e007 ap bf75 4.36 (A at s21, F at s21c), S7T1 e016 ap 2.93, S10T1 e019 ap 2.74.
- Crossed mails with v: v owns linear-regime S7–S10 map (rms 0.005, 66 evals). My r1 (T1, rms 0.0125) = second amplitude. No more parent-point maps from me.
- Board: superadditive combos (x 4-orbit sum 1.92/2.15/1.99 STRONG; h union α+β s21 4.76 PASS). STRONG claims: c d698, f e5d5, j ⊥α−0.45 (2.63 r46). s21 splitting is binding gate. EG drops 13→4 (e).
- Next: pivot to "outer α at the leader": add live S7–S10×T1 directions (from r1) on top of the best inner combo leader, small steps. Post hypothesis when r1 lands.

## 2026-10-14 13:12 — wakeup 5: pivot to rec-out
- r1 (S7–S10×T1 rms 0.0125) still queued.
- v result 2d87: outer T1 α slope ≈ 4×cos2δ projection, uniform across S7–S10; v now runs coherent outer cos2δ at the parent. x stage 2 runs S4–S6 at record c662. av: records = cos2δ α / sin2δ β on S1/S2×T1(+T2).
- h claim 0069: c662 STRONG 4.76/5.23/4.67, conv46 5.23. Density controls (k) ~0.995.
- NEW family rec-out (hyp 20261014T130956.392Z_swarm-w_hypothesis_77b0): c662 + c·u_out (cos2δ on S7–S10×T1, unit norm). 9 reqs → work/ro1_ids.txt. Builder work/recout.py; c662 block at work/c662_block.json (from swarm show ed_input path).
- Charged: 63.

## 2026-10-14 13:40 — wakeup 6
- Nothing of mine landed: r1 (submitted 12:19) still SUBMITTED after 78 min; o and j report stuck lanes to operator. Waiting.
- Board: v CLAIM 0268 STRONG single outer S7×T1 cos2δ α contrast 1.561/1.933/1.787/conv 1.932 (supports rec-out premise). t claim 8c01 STRONG 4.82/5.19/4.55/5.19. f: phase-only s21 ceiling ≈1.72. ap: records' γ on uniform LL0 lower the gap (γ×ρ* cooperation). g retracted 1/d² critique.

## 2026-10-14 14:12 — wakeup 7
- Queue unstuck (o's lane resolved: slow, not lost).
- rec-out b1 landed: c662+c·u_out: −0.02 3.52, 0.01 5.27, 0.02 5.70, 0.04 6.29 (fbe0, e002 → r46). S7/S8-only 5.44/6.00. 0.75 track 4.56/4.92/0.08 FAIL. Posted result.
- r1 small-step: all 11 dirs gain on α·cos2δ>0 (+5…+23 %). 8 PASS gainers promoting.
- Board record: o f5f1 6.28/8.33/8.12 (Σ|β| 1.88, near cap). 
- Submitted ro2 (9): c662 c 0.06/0.08; f5f1 + c 0.01/0.02/0.04/0.06; c662+0.04u + d·sin2δ β outer d ±. Builder work/recout2.py (general record merge). Charged 72.

## 2026-10-14 14:45 — wakeup 8
- ro1 ladder: e002 (c662+0.04u) r46 7.38; fbe0 r46 6.28; all ro1 PASS points promoting. r1 small-step gainers r46 1.09–1.28.
- Board records: av e0a8 STRONG 10.39/9.87/10.50 conv 9.96 (S1–S3×T1 complex cos2δ+i sin2δ, Σ|α| cap-limited). s c325 9.87/10.15/9.53. av 55f9 s21 12.51 = all shells S1–S10 at outer weight 0.25 (Σ|α| 1.35, cap-cheap).
- x does S4–S6 outer α at e0a8/c325; a does outer sin2δ β at e0a8/c325.
- Submitted ro3 (4): 55f9 + u_out c 0.04/0.08, and complex (d = 0.8c). Mailed av. Charged 76.

## 2026-10-14 15:10 — wakeup 9
- e002 (c662+0.04u) full ladder: 6.29/7.38/6.59, conv46 7.367 → STRONG-level, converged. Mailed k for density control.
- Outer sin2δ β sign confirmed (+d gains): 5dd9 c662+0.04u+0.02v 9.23/9.42.
- f5f1+u: 0.06 → 11.19/11.99 (rising). 55f9+u: 13.93/13.26 (407a), 14.52/11.60 (df9b); +β → r46 FAIL.
- swarm-u: R>11 outer-heavy points have qmax-8 pair spectra far below physical floor (df9b −1.1e-2 vs gap 3.3e-3) → unconverged in qmax. Mailed u to pre-screen 79df/e90a/5dd9/2fdc/5ad9/e002. HOLDING amplitude pushes.
- Posted result 05b8.

## 2026-10-14 16:45 — wakeup 10
- 407a (55f9+0.04u) full ladder 13.93/13.26/13.79/conv46 13.93 — #1 on leaderboard, broker "strong". BUT qmax: r46→conv46 shift +2.3 % (55f9), +5.0 % (407a), +13.9 % (df9b) → grows with outer content. Posted CLAIM 34a0 with caveats; seconded u's qmax≥12 request.
- Clean companions: e90a (f5f1+0.06u) 11.19/11.99/11.61/conv 12.01 (+0.2 %); e002 7.37 conv. k queued controls e002 (f16b), 407a (09e9).
- an: above R≈12, r46 splitting gate binds; rank by min(r46,r56).
- ro4 submitted (8): 1c48+u (noQ0), 06bb+u, 5063 cap-trade+u — aim: qmax-clean R>12. Mailed s, x, h. Charged 84.

## 2026-10-14 17:16 — wakeup 11
- u 91dd: qmax 8 UNDERSTATES R>12 gaps (shifts positive); 407a reaches physical floor at qmax 12; all my rec-out points clean at qmax 10. k: 407a density ctrl 1.010 → beyond-M2. Posted note a04e updating claim 34a0.
- ro4: 5063 cap-trade s0.85 c0.055 (4133) 13.93/13.63; s0.9 c0.04 (39cd) 13.59/13.26; 1c48 c0.06 (a643) 13.32/12.85 (noQ0); 06bb c0.02 12.14/12.07 (peak low).
- ro5 submitted (6): 5063 s0.80 c0.07, s0.75 c0.085, s0.85 c0.055 + d 0.02/0.04 (outer β); 1c48 c 0.08/0.10. Charged 98.
- Many agents closing (c,h,o,r,j,m,an,at,af,...). 

## 2026-10-14 17:50 — wakeup 12
- ro4 ladder: 4133 (0.85·5063+0.055u) 13.93/13.63/13.09/conv 13.58; a643 (1c48 noQ0+0.06u) 13.32/12.85/13.10/conv 13.04; 1c48 c0.04 12.64 min.
- ro5: a8eb (0.85·5063+0.055u+0.02v) 15.33/14.68/14.56 (conv46 pending) — best min so far. d0.04 worse (14.13 min). c79a s0.8 c0.07 14.08/13.83.
- s21c N_A=3 eg: 407a 2.21, a8eb 2.63, 4133 2.79, a643 2.27 (answered v's critique 5b45). u: "reduced, not resolved" — agreed.
- k: 5063 control 0.989, 1c48 1.000.
- ro6 (5): grid around a8eb in (s, c, d). Charged 95.

## 2026-10-14 18:21 — wakeup 13
- ro5/ro6 ladder: fae8 (0.75·5063+0.085u+0.02v) 15.90/14.97/14.83/conv 15.12 BEST; a8eb 15.33/14.68/14.56/conv 14.75; cf95 (0.8,0.07,0.02) 15.80/14.87/14.74; d326 (0.85,0.055,0.03) 15.20/14.79/14.57; d=0.02–0.03 best; lower s + more c better.
- Competitors: aq 4792 14.85/14.52/14.37/14.92; av 023e 13.69/13.46/13.61; x 236b noQ0 12.22 min; s 2f3f noQ0 11.89.
- ro7 (5): s 0.70/0.65/0.60 with c 0.10/0.115/0.13, d 0.02–0.03. Charged 105.
- Many agents done. k closed mech (36 controls 0.935–1.010).

## 2026-10-14 18:53 — wakeup 14
- ro7: 256c (0.70,0.10,0.03) 16.11/15.23/15.09; 4b84 (0.75,0.085,0.03) 16.12/15.21/15.02; f12d (0.70,0.10,0.02) 14.82 min; s0.65/0.60 at d0.02 slightly lower. Plateau ≈15.
- u: fae8/cf95/a8eb class A′ (conv46 shift ≤1 %, art10 ≤5e-5) — qmax-robust. z/aq/av frontier class B.
- Competitors: z e327 14.69/14.23/14.35/14.66.
- ro8 (4): d 0.04/0.05 at (0.70,0.10), d0.04 at (0.75,0.085), (0.65,0.115,0.035). Then claim best + coverage.

## 2026-10-14 19:25 — wakeup 15
- ro8: plateau confirmed. 256c (0.70,0.10,0.03) 16.11/15.23/15.09/conv 15.54 = BEST (broker strong). b022 15.10 min, e477 15.04, 2d9b 14.90, c870 (d0.05) r46 14.43.
- ai certified fae8/256c against V− shift (optimum respects MT). z e327 control 1.01.
- Wrote work/control.py (⟨ρ_k⟩_BZ control, k's recipe); submitted control 9bea for 256c (s21,r46,r56).
- Posted CLAIM for 256c.
- Next: when control lands, post it; then final coverage result + done? Budget used ~107/500 — consider whether anything else worth doing (e.g. outer S4–S6 into the trade? x showed S4–S6 add at record).
- ro9 (3): cap trade with outer over S4–S10 (s0.70 c0.085 d0.03; s0.65 c0.10 d0.035/0.045). Charged ~110 + control.

## 2026-10-14 20:00 — wakeup 16: CLOSED
- Control 9bea for 256c: 1.006/1.004/1.005 → beyond-M2.
- ro9 (S4–S10 outer): r46 14.57–14.83 < 256c's 15.23 → S7–S10 is the better outer set in the trade.
- z's CMA (rcma3) now centred at 256c — local refinement covered.
- Posted final coverage result 55bd. Calling swarm done (110/500 charged).
