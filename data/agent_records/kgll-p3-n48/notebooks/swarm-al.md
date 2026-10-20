# swarm-al notebook

Started 2026-10-14T10:26:04+00:00.

## 2026-10-14 11:33 — wakeup 1: scope chosen = `lowsym`
- Board: ~20 C6-invariant families (axis maps a/b, joint orbits c/g/f/d, ⊥ amp j/r, big amp e, phase hess m/l, combos x/h/o, mech k, fsmatch y, noQ0 s, high shells v/w).
  Leaders (s21): jorb d698 (S2xT1 δ60 β+0.03) 1.2494; ce1f (S1xT1 δ30 β+0.03) 1.1595 → r46 1.1586; 7133 (⊥ α −0.05) 1.1709.
- Nobody covers symmetry breaking. Block is always C2-even ⇒ only E2 (C3-breaking) representable. On s21 (C6) linear E2 term = 0; R = R(L)+cε²+dε³.
- Hypothesis posted 20261014T113213.641Z_swarm-al_hypothesis_7999 (budget ≤ 60).
- Stage 1: 18 s21 evals submitted (work/s1, gen in work/gen_s1.py, orbit tools work/lowsym.py). Per orbit o30/o60/o90: pure E2 ± at parent, leader+E2 at fixed orbit sum with members (3b,0,0),(2b,b/2,b/2),(0,1.5b,1.5b),(−b,2b,2b).
- Prediction: c<0 (concentration hurts).
- Note: I read ed_input.json of other agents' requests via the path `swarm show` prints (that's the documented way to see inputs).
- Next: fit c,d per orbit; then stage 2 = E2 stability at large-amplitude C6 leaders (watch fs-scan q, bigamp e, phasehess m, union h).

## 2026-10-14 11:56 — wakeup 2
- Stage-1 18 requests still all pending (queue backed up across 40+ agents).
- Overlap: swarm-ad `nem` (11:28) and swarm-ah `nematic` (11:32) posted the same E sector. Agreed split (mail 115537): ad = pure E at parent; **al = leader + E2 at fixed orbit sum (concentration)**; ah = leader+εE via the ladder + r46/r56 orientation. My 6 pure-E points stay (third amplitude for ad/ah's profile); I won't extend pure E at the parent.
- Board facts: swarm-e: full stars break the manifold at |α|~0.1–0.2, |β|~0.12 → my o90 (3b,0,0) at α=−0.15 on one member may fail. swarm-u: response is a min over branches (cusp), so expect R ≈ R(L) − κ|ε| on s21 if the lowest excitation is a C6 multiplet. ce1f transfers: r46 1.1586, r56 1.1492. d698 r46 1.4041. f_5098 (chiral-odd S1×T1 ±30 at 0.067) s21 1.3806.
- Gotcha: a bare `cat > file` with no heredoc hangs on stdin; use heredocs only.
- Next: when results land, fit κ/c per orbit, post a result to ad/ah, then decide on stage 2 (concentration at larger-amplitude leaders like f_5098) or a switch.

## 2026-10-14 12:22 — wakeup 3
- Still 18/18 pending (charged 18). Queue slow.
- Board: STRONG claims already exist: c d698 (S2×T1 +60 β 0.03: 1.249/1.404/1.347); f 728b (S3×T1 chiral-odd β 0.05: 1.558/1.641/1.560, conv46 1.641); α⊥=−0.45 line (j ea28 = r e99d = q c027): 1.64/2.63/2.44, conv 2.63, s21 splitting is binding. h: S4×T1 α contrast 1.57/1.72/1.61. x d524 s21 1.92.
- k: density controls show leader gains are not density.
- Stage-2 idea: concentration at the large α⊥ leader is limited by per-entry |α|≤0.6 → ε ≤ 0.075 around b=−0.45. Decide after stage 1.

## 2026-10-14 12:55 — wakeup 4
- Stage-1 results (12/18 done). o30: s21 all below leader. Quadratic c≈−36 (in ε units, consistent at 0.015 and 0.03), cubic ratio 6.7 vs 8 → smooth, NO cusp. r46: big linear (orientation) term, 34da (0,.045,.045) r46 1.2026 > leader 1.1586. o60: concentration loses at s21; (−.03,.06,.06) and both pure-E2 at parent FAIL the manifold (S2 in-orbit E splits the s21 manifold fast). o90 pending.
- ad's result b6bf: k-nematic (full S1 × E-weighted T1) gains +5% for both signs at s21 → positive E curvature off-diagonal. ah's small-ε points also say no cusp.
- Records now ~4.8 (t 8c01, h c662, multi-orbit S1–S3×T1–T3 α+β, C6-circulant).
- Stage 2 submitted (16): multiplicative nematic strain of 8c01 and c662, (1+εw), w=(2,−1,−1) by the orientation class of G ("r") or R ("k"), ε ±0.15, ±0.3. work/gen_s2.py, verified pure E2 with work/check_e2.py. Class bins are offset 15° (S1 members sit at 0/60/120°).
- Mailed ad/ah the interim. Charged 34/500.
- Next: post the stage-1 result with coverage once o90 and r56 land; read stage 2 (s21 quadratic → is the record a max in E2?).

## 2026-10-14 13:27 — wakeup 5
- o90 (⊥ α leader 7133: 1.1709/1.1699) concentration: (−.15,0,0) s21 1.1595 r46 1.1924; (−.1,−.025,−.025) 1.1683/1.1853; (0,−.075,−.075) 1.1688/1.1489; (.05,−.1,−.1) 1.1634/1.1396. Pure E2 ± at the parent: 0.9771 / 0.9847.
  ⊥ is very flat in E2 at s21 (c≈−3.8, consistent at both |ε|), against o30 c≈−36. r46 again shows a linear orientation term of ±2%.
- Stage-1 r56 still pending for all promoted points; stage 2 (16) queued, not started.
- Board: STRONG claims for c662 (h) and 8c01 (t). g retracted the 1/d² critique. ap lllref: the records' γ on a uniform LL0 parent lowers the gap, so the gain needs γ×ρ* cooperation.

## 2026-10-14 13:59 — wakeup 6
- STAGE 2 RESULT (s21): records are saddles in E2. The r-strain (G orientation class) has positive curvature: 8c01 4.8159 → 5.0160 at ε=−0.3 (c≈+2.0), c662 4.7599 → 4.8682 (c≈+1.0). The k-strain has negative curvature (c −6 / −5). Quadratic is consistent at 0.15 and 0.3. Posted result 20261014T135913.077Z_swarm-al_result_0184.
- Stage 3 submitted (11): 8c01 r −0.45, −0.6, +0.45; 8c01 r −0.3 orientations o1, o2 (s21 must equal ad5e); f5f1 r ±0.3, k −0.3; 6506 r ±0.3; c662 r −0.45. Generator work/gen_s3.py (spec TAG:REQ:MODE:EPS:ROT), lib work/gen_s2_lib.py.
- Charged 45/500. Board records now: 6506 (t) s21 8.71; f5f1 (o) 6.28/8.33/8.12 STRONG.
- Next: watch the r46/r56 orientation dependence of the stage-2 promotions; is the r-strain gain larger than the orientation artifact? If the s21 gain persists at the 8.7 record, consider an E2-direction line at the newest record + all 3 orientations.

## 2026-10-14 14:30 — wakeup 7
- Stage-2 r46 (8c01 base r46 5.1860): r −0.3 ad5e **5.3291** (+2.8%), −0.15 5.2117, +0.15 5.1636, +0.3 5.2015. k: +0.15 5.2209, +0.3 4.7797, −0.15 4.6568, −0.3 3.8675 (big linear orientation term).
  c662 (r46 5.2257): r −0.3 9048 5.2775, −0.15 5.2286, +0.15 5.2221, +0.3 5.0491. k: +0.15 5.2389, +0.3 4.9450, −0.15 5.0072, −0.3 4.5182.
  → ad5e beats 8c01 on both s21 and r46. Its r56 is pending (8c01's r56 4.5509 is its min).
- Stage 3 (11) all still pending. Board s21 records now ~10.4 (av cos2d), f5f1 8.33/8.12 STRONG. A nematic +3–4% is small; its value is as a structural statement (C6 optima are saddles).

## 2026-10-14 15:03 — wakeup 8
- Stage-3 s21:
  - 8c01 r line: −0.6 **5.5914** (+16%), −0.45 5.2651, −0.3 5.0160, +0.45 5.1205. Still rising at −0.6, where coefficients of class w=2 flip sign (Σ|α| 1.37 → 1.55).
  - C6 check: 8c01 r −0.3 orientations o1/o2 = 5.0158/5.0161 vs o0 5.0160 ✓ (3e-5).
  - c662 r −0.45: 5.0065 (+5.2%).
  - f5f1 (6.2767): r +0.3 **6.6425** (+5.8%), r −0.3 5.9171, k −0.3 5.0688. Quadratic ≈0, cubic-dominated.
  - 6506 (8.7058): r +0.3 8.4714, r −0.3 8.8378 (+1.5%). Quadratic slightly negative, c≈−0.6.
- Reading: the r-strain direction is not uniformly positive-curvature. The cubic E2 invariant matters at the newer records. Useful property: multiplicative strain with |ε|<0.5 leaves Σ|α|, Σ|β| unchanged, so it is "free" at the cap-limited records.
- Stage 4 submitted (10): 55f9 (av, full ladder 12.51/12.71/12.79) r±0.3, k±0.3; df9b (w, s21 14.52; outer S7–S10 shells, verified pure E2) r±0.3, k±0.3; e0a8 (STRONG 10.39/9.87/10.50) r±0.3. Charged 66/500 after this batch.
- Caveat from u: R≈13–14.5 records have qmax-8 non-PSD pair spectra; trust the conv46 (qmax 10) rung.

## 2026-10-14 16:48 — wakeup 9
- Stage 4 (top records), full results:
  - 55f9 (12.51/12.71/12.79/conv 13.00): k ±0.3 FAIL (s21 split 0.31/0.16). r+0.3 a8c1 12.44/12.69/12.57/conv 13.14, about neutral. r−0.3 6f22 12.35/12.24/12.70/12.73, slightly worse.
  - df9b (14.52/11.60/13.56/13.21): k ±0.3 FAIL. r+0.3 44ee s21 15.04 but r46 FAIL (split 0.105). r−0.3 15d0 14.88/9.33/12.89/11.18, worse.
  - e0a8 (10.39/9.87/10.50/9.96): r+0.3 a78d s21 9.80 then r46 FAIL. r−0.3 24e4 10.08/9.02/10.54/9.13, worse.
- Stage 3 ladder: 6506 r−0.3 64f2 8.84/8.73/7.96/conv 8.73; r+0.3 d1d7 8.47/8.53/7.85. Need 6506's own ladder to compare (m says min 7.73).
  8c01 r −0.6 cef6 r46 5.77 (vs 5.19); f5f1 r−0.3 57ea r46 8.05; f5f1 r+0.3 4046 r46 6.26 (vs 8.33): big orientation swings on 4×6.
- CONCLUSION forming: at the frontier (R≥10) the nematic strain is neutral to harmful. The k strain breaks the s21 manifold. The r strain shifts s21 by ±1–4% and destabilises the r46 manifold gate. 4×6 swings ±20–30% with orientation. Gains exist only at the old records 8c01/c662.
- Plan: once the r56 rungs land, post the closing result with coverage and abandon lowsym. Then pick a new role (55/500 charged).

## 2026-10-14 17:23 — wakeup 10
- Closed lowsym: result 20261014T171948.125Z_swarm-al_result_9540 (full table + coverage), abandon …171948.892Z_swarm-al_abandon_8438.
- Critique/diagnostic note …172057.105Z_swarm-al_note_bfb7: χ = odd r46 response to a Σ-neutral E2 r-strain, normalised. It ranks the records' s21/r46 disagreement (Spearman 0.89, 7 records). f5f1 χ −0.36, df9b +0.28, inner angular-rule records ~0.05. This supports l's 4th-cluster (27-site C3) request.
- New family audit-al: χ probes on frontier records 407a, 4133, 023e, d702 (r ±0.3, 8 evals, work/s5). Mailed w, o, av, ai, l. Charged 63/500.
- Next: when the r46 rungs land, compute χ (base r46: 407a 13.2594; 4133 13.6299; 023e 13.4582; d702 13.1659) and post. Then likely `swarm done` unless a gap appears.

## 2026-10-14 17:55 — wakeup 11: DONE
- χ probes landed (r46): 407a +0.128, 4133 −0.010, 023e +0.084, d702 +0.150. Spearman over 11 records = 0.65 (p 0.03). At the frontier s21 rewards strain that r46 punishes. Posted note …175444.889Z_swarm-al_note_fa5f; replied to ai.
- Nothing compelling left in my scope; most agents are closing. Called `swarm done` with summary work/done.md.
