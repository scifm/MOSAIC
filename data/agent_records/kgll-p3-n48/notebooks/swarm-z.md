# swarm-z notebook

Started 2026-10-14T10:25:18+00:00.

## 2026-10-14 11:31 — wakeup 1: orientation, family `rcma` chosen
- Board at arrival: a/b separable maps, c/g S1–S3 joint orbits, d chiral half-shell β, e bigamp, f all chiral-odd β,
  h union quadratic model + S4–S6 α contrasts, i kpow, j/r/q ⊥ channel line scans, k mech verifier, l/m phase curvature,
  s noQ0 (⊥ = half static LL mixing), x combos of orbit leaders.
- Key s21 facts (swarm-c jorb, per-entry α 0.05/β 0.03): S2×T1 ∥ α+ 1.2166 / α− 0.5223; S2×T1 +60 β+ 1.2494;
  S1×T1 ⊥ α− 1.1709; S1×T1 +30 β+ 1.1595 → **r46 1.1586** (transfers!). MT symmetry (α_θ≡α_−θ, β_θ≡−β_−θ) holds to <1 %.
- My niche: CMA-ES on the ROBUST objective min-over-clusters (s21 + free s21c/r46/r56 promotions) in 18-D
  S1–S3×T1 orbit α/β space. Hypothesis 20261014T113026.903Z_swarm-z_hypothesis_5a83. Mailed c, x.
- Code: work/rcma.py (CMA core, state in work/rcma/state.json, per-gen manifest), work/orbits.py (orbit + mirror
  enumerator), work/pool.py (pools board requests into canonical pair coefficients).
- gen0 submitted (12, σ0=0.4, mean=parent). Next: `uv run ... python work/rcma.py step` each wakeup.

## 2026-10-14 12:20 — wakeup 2
- Board exploded: ⊥ S1×T1 α line (j/q/r): α −0.15 s21 1.41/r46 1.52 … −0.45 s21 1.64/r46 2.63 (ak: suspected branch change, gate splitting FAIL at −0.35).
  q 5b9e: β=0.3 per entry on S1×T1 +30 → s21 2.75 (at boundary). c CLAIM STRONG: S2×T1 +60 β 0.03 → 1.249/1.404/1.347 (d698).
  f e5d5 (S3×T1 chiral-odd β) s21 1.558 r46 1.641. r46 generally ≥ s21 → s21 usually binds the min.
- Gen0 (σ 0.4 at parent) too timid → restarted CMA at gen1: warm mean x = α⊥S1 −2; β chiral-odd S1 ±2, S2 ±1, S3 ±1; σ=1;
  box widened to campaign boundary (x_α ≤ 12, x_β ≤ 10) with L1 repair (Σ|α| ≤ 2.45, Σ|β| ≤ 1.95). gen0 kept as archive.
- NB pool.py analysis bug: summing 3 orbit entries → x displayed ×3. Divide by 3.
- Split agreed with ag (β-only 24-D fsmin) and n (27-D minmax). Mine: 18-D α+β T1.

## 2026-10-14 12:40 — wakeup 3
- Leaders now s21 4.8 (t 8c01, h c662: multi-orbit S1–S2×T1 α+β combos; in my x coords
  8c01 ≈ α[1,1,−2.7,−0.3,1.3,−1.6,0,0,0] β[−2.3,2.6,0,−0.7,0,0.8,0,0,0] + 9 pairs outside my space). r46 pending.
- Claims STRONG: c d698 (S2 +60 β), f e5d5 (S3 chiral-odd β 1.558/1.641/1.560), j ea28 (⊥ α −0.45 1.64/2.63/2.45).
- s21 splitting gate binds (q). k/u: gains not density nor interaction scale.
- my gen0 (archive): 9e31 s21 1.508, 48ce 1.386; two FAIL (splitting). gen1 queued. work/xof.py maps any req to my x.

## 2026-10-14 13:15 — wakeup 4
- Records: h c662 STRONG 4.76/5.23/4.67(r56)/5.23(conv46); t 8c01 4.82/5.19/4.55. Direction = av's angular rule
  (α ∝ cos2δ, β ∝ sin2δ) on S1/S2×T1 + S1×T2 content (8c01 has S1×T2 α≈0.1/β≈0.03 per entry — OUTSIDE my 18-D space).
- Density controls (k) ~1.0 for all records → not density. Broker queue slow (~1 h to first result); gen1 still queued.
- gen0 archive: 9e31 s21 1.508 r46 1.697; 48ce 1.386/1.672. 3 FAILs (splitting).
- Decision pending gen1: consider extending space to S1/S2×T2 orbits (records use them) or restarting mean at 8c01 projection.

## 2026-10-14 13:55 — wakeup 6
- New record o f5f1: s21 6.28 / r46 8.33 / r56 8.12 (ray along cos2δ α / sin2δ β, incl. S1×T2/T3 pairs). Uses Σ|β| 1.88/2.0.
- gen1 stuck in broker (no s21 since 12:07; others report stuck lanes). Restarted at gen2: mean = f5f1 projection,
  background (rcma/background.json = f5f1 outside-pairs, block entries) fixed, σ 0.5. rcma.py block() merges background;
  clip() L1 caps subtract background. Verified reproduction (rcma/f5f1_repro.json) to 5e-5, swarm check ok.
- gen0/gen1 manifests are archives (not told to CMA). Posted note + mailed o.

## 2026-10-14 14:20 — wakeup 7
- gen1 (σ=1 around warm start): 8/12 FAIL (PES/splitting), FAIL R up to 6.03 (3c2e), 5.19 (d215): the Laughlin window
  transverse to the ray is narrow. BUG fixed: FAIL used R−0.5 → now f = −1 − min(1, split/Δ) (below every PASS).
- New record av e0a8 s21 10.39 (cos2δ+i sin2δ rule on S1–S3×T1) is INSIDE my 18-D space; at Σ|α| 2.34/2.5, Σ|β| 1.64/2.0.
  x = α μ(1,1,−2 | −1,2,−1 | 1,1,−2)·1.3, β (−1,1,0 | −1,0,1 | −1,1,0)·3.03.
- Restarted gen3 at e0a8, σ 0.3, caps 2.49/1.99 (no background; f5f1 background moved to rcma/background_f5f1_active_gen2.json).
  gen2 (around f5f1) still queued → archive. Mailed av.

## 2026-10-14 14:50 — wakeup 8
- gen3 (σ 0.3 around e0a8): 12/12 PASS at s21, 9.76–11.87; best 2734 11.87, dcb1 11.36 (board #3/#4). Awaiting r46/r56.
- gen2 (around f5f1+bg): s21 4.2–8.3 PASS (460b 8.30), one FAIL — archive.
- e0a8 full ladder 10.39/9.87/10.50/conv46 9.96 (av claim). av 55f9 s21 12.51 (rule extended). u: qmax-8 non-PSD at R≈10 → watch conv46.
- Everything is cap-limited (ae audit): records at Σ|α| 2.3–2.5. Chart-dependence of the cap raised by t, ai (human's call).

## 2026-10-14 16:50 — wakeup 9
- gen3 closed: 11/12 STRONG; best 2734 min 10.88 (11.87/10.88/11.47/conv 10.95), baab 10.61, dcb1 10.52. r46 binds.
  Correlations: phase budget S1→S2 chiral, α budget → S3⊥ & S2 −60. Posted result. CMA told; gen4 proposed (σ 0.28).
- Board: h 5063 STRONG 11.65/12.30/11.97; w 407a 13.93/13.26/13.79 (qmax not converged); av 55f9 12.51/12.71/12.79;
  s 1c48 noQ0 11.21/11.67/11.60; e c577 11.42/11.59/11.38. u: qmax ≥12 rerun requested for R≥13.
- gen2 (f5f1+bg) still promoting — archive.

## 2026-10-14 17:20 — wakeup 10
- gen4 (rcma 18-D) landing: all PASS r46, best ddde 11.25, 39fe 11.20 (r56 pending).
- Frontier: av 023e 13.69/13.46 (inner 0.5×rule + outer y_a 1.25, y_b 0.89; Σ|α| 1.68, Σ|β| 0.90 → NOT cap-limited),
  w 4133 13.93/13.63, ai d702 13.96/13.17. Outer content = exact angular rule per shell (work/rulefit.py).
- NEW rcma2.py (32-D: 18 inner + y_a,y_b per outer shell S4..S10×T1), DIR work/rcma2, λ 14, C0 diag(0.5 inner, 1 outer), σ 0.3,
  clip uses actual block L1. gen1 submitted at 023e. Hypothesis …_hypothesis_6378. Run step for BOTH each wakeup:
  `uv run ... python work/rcma.py step` and `... work/rcma2.py step`. Plan: rcma 18-D 2–4 more gens then stop (coverage).

## 2026-10-14 17:55 — wakeup 11
- rcma gen4 told (best ddde min 11.25 at r46 (r56 pending), 39fe 11.20); gen5 proposed (12) = LAST 18-D gen: work/rcma/STOP
  created (propose() now skips if DIR/STOP exists). n closed the inner-only question (27-D CMA min 11.50; capped max ≈11.5–11.7).
- rcma2 gen1: 14/14 PASS r46; **e327 s21 14.69 / r46 14.23 / r56 14.35** (conv46 pending) — above the board frontier (~13.5).
  e327 z: inner ~0.6×023e-ish, outer y_a ↑ on 13/16/19/21 (1.66–1.82), y_b 0.6–1.2.
- Board audits: u class A/B qmax (outer-heavy R>12 → conv46 +2…+20%); v: N_A=2 match ≠ Laughlin, quote s21c N_A=3 EG;
  ai: s21-steered optimizers drift off the V+ plane (my min objective guards against that); aa: EG<1.6 flags r46 FAILs.

## 2026-10-14 18:25 — wakeup 12
- e327 full ladder 14.69/14.23/14.35/conv46 14.66 all PASS → board's top min. CLAIM posted …swarm-z_claim_200a.
- Density control: NEW work/control.py (⟨ρ_k⟩_BZ, 24² k grid, 48² mesh, truncated to 15 shells, renormalised w0=1).
  e327 → ctrl_e327.json (M2 trunc 9.83, ρmin 0.015); M2-matched rescaling goes negative → skipped. Submitted ea0d (--control s21,r46,r56).
- aq dressed e327 with S1×T3 → 4792 (min 14.37, +1%). rcma2 gen1 told; gen2 (14) proposed. rcma 18-D gen5 = last (STOP file).
- Many agents now done (k, s, t, n, ...). Budget 100+14 used.

## 2026-10-14 19:00 — wakeup 13
- Control ea0d for e327: 1.0117/1.0097/1.0109 PASS → density excluded (beyond-M2 by brief def; Q=0 share open).
- rcma 18-D closed: best 3ecc min 11.82 (12.46/11.82/12.36/conv 11.88). Coverage posted (72 req, 50 P / 22 F).
- Frontier: w 256c 16.11/15.23/15.09/conv 15.54 (min 15.09), ai 18fa s21 15.72 pending, av fd2d 15.48. rcma2 gen2 waiting.

## 2026-10-14 19:35 — wakeup 14
- rcma2 gen2: 14/14 PASS all rungs; best 427d 14.78/14.37/14.46/conv 14.78 (min 14.37), 6682 14.34, 811f 14.33. gen3 proposed.
- Frontier w 256c min 15.09 (inner 1.39×rule-ish, outer only S7–S10 y_a 1.78 y_b 0.66, + 9 S1×T2 pairs, Σ|α| 2.42 cap-limited).
- NEW rcma3.py (= rcma2 chart, DIR rcma3, seed 20261016, background = 256c's S1×T2 pairs in rcma3/background.json),
  restart at 256c σ 0.3. Mailed w. Each wakeup: step rcma2 AND rcma3 (rcma has STOP).

## 2026-10-14 20:00 — wakeup 15
- rcma2 gen3 (promotions running): 677f 15.59/14.75/14.85 (min 14.75); all PASS so far.
- rcma3 gen1 (at 256c): r46 15.15–15.53, s21 15.9–16.4; 69ec 16.39/15.53/15.31; r56 pending for most. No FAILs.
- Board: w claim 256c (16.11/15.23/15.09/conv 15.54); av fd2d (15.48/14.58/14.16). Many agents done.

## 2026-10-14 20:50 — wakeup 16 (after an interrupted step)
- The previous step was interrupted mid-propose for rcma3: gen002 c00–c12 submitted, c13 not, no manifest, state unsaved.
  RECOVERED: re-ran collect(gen1) → told (state gen 2, σ 0.28); regenerated the gen-2 draws (rng SEED+2) and matched each
  c*.json block to a draw; rids mapped from `swarm show` request.source (rcma3/gen002_rids.json); submitted c13 (769e).
  LESSON: propose() should write the manifest incrementally. (rcma2 gen4 was fine.)
- rcma2 gen3 closed: 677f 15.59/14.75/14.85/conv 15.35 (min 14.75). gen4 in flight.
- rcma3 gen1 closed: 69ec 16.39/15.53/15.31/conv 15.74 (min 15.31 > w 256c 15.09); 6e0e 15.21, 9b37 15.12. 14/14 PASS.

## 2026-10-14 21:20 — wakeup 17
- rcma3 gen2: d7f2 17.71/16.36/15.99/conv 16.60 (min 15.99, board top, +6% over 256c); 9/14 min ≥15. CLAIM …_claim_2d74.
  Density control 596d submitted (work/ctrl_d7f2.json; trunc M2 9.76, ρmin 0.036). Mailed w.
- rcma2 stagnant (gen4 best e1cb 14.79) → work/rcma2/STOP; budget goes to rcma3. rcma3 stepped (see output).

## 2026-10-14 21:45 — wakeup 18
- d7f2 control 596d: 1.0046/1.0028/1.0036 PASS → beyond M2 (note posted). rcma3 stepping (gen2 → gen3).

## 2026-10-14 22:15 — wakeup 19
- rcma3 gen3 (σ 0.27, mean ~d7f2): 14/14 PASS s21 16.0–17.6, r46 15.0–16.3; r56 pending. Looks like a plateau near min ~16
  (Σ|α| cap-limited). Budget 176/500. If gen3–4 don't beat 15.99 by >1%, consider final convergence + coverage and done.

## 2026-10-14 22:50 — wakeup 20
- rcma3 gen3 closed: best f19b 17.58/16.26/15.97/conv 16.55 (min 15.97); median 15.73 (gen2 15.19) → converging on
  a cap-limited plateau ~16. gen4 proposed (14).
- Withdrew 4 stale pending requests (r56 backlog per ag/a notes).
- Cap probe on d7f2 (work/probe_t2/, builds-on d7f2): p1 remove S1×T2 α background (6075); p2 + fill Σ|α| to 2.49 with T1
  (ce2b); p3 keep bg, fill T1 α to cap (0114); p4 = p2 + fill Σ|β| to 1.99 (45a4). Question: are T2 α pairs worth their cap share?

## 2026-10-14 23:20 — wakeup 21
- Cap probes on d7f2 (15.99): p1 6075 no T2α 17.01/15.88/15.71 (−2%); p2 ce2b no T2α + refill T1 17.12/15.87/…;
  p3 0114 fill T1α to cap 17.81/16.38/16.00 (= d7f2); p4 (…224127 45a4) +β to cap r46 15.20 (worse).
  → d7f2 sits at an INTERIOR optimum in overall α scale; cap not binding in gradient sense; more β hurts.
- rcma3 gen4: r46 15.6–16.41 (e92a 16.41, f596 16.33), r56 pending — converged plateau.
- Q=0 ablation of d7f2 (only S1×T1 ⊥ α carries Q=0; S3×T1 90° orbit does not, R ≠ ẑ×G): e167 (⊥ α removed), ae65 (removed + α refilled).
- Plan: close rcma3 after gen4 + ablations → coverage post → swarm done (budget ~196/500; leftover unused is fine).

## 2026-10-14 23:50 — wakeup 22
- rcma3 gen4: best e92a 17.65/16.41/16.05/conv 16.66 (+0.4% over d7f2); median 15.67 → converged. work/rcma3/STOP created.
- Q=0 ablation: e167 (S1⊥ α removed) 17.53/16.21/… (≈99%); ae65 (removed+refill) 17.69/16.26/16.01 (= d7f2). Q=0 ≲1%.
- Coverage counts: rcma2 56 req all PASS (best e1cb min 14.79); rcma3 56 req all PASS (best e92a 16.05).
- Next: wait e167 r56, post final coverage result (rcma2+rcma3+probes), then swarm done.

## 2026-10-15 00:15 — DONE
- e167 no-Q0 ablation 17.53/16.21/15.91/conv 16.41 (99.5% of d7f2). Final coverage posted …_result_58ef. `swarm done` run.
- Final: best min e92a 16.05; claims d7f2 (15.99, ctrl 1.004) and e327 (14.23, ctrl 1.01). 196/500 charged.
