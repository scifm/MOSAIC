# swarm-ai notebook

Started 2026-10-14T10:25:52+00:00.

## 2026-10-14 11:36 — wakeup 1: scope chosen = `mtodd`
- Board: ~25 families; low-shell joint orbits saturated (c,f,g,j,q,r,x,s,ae,z); pooled surrogates (h,o,t,u);
  S7–S10 even-α taken by v AND w (I had generated `work/hev/` for it — dropped, not submitted).
- Leader d698 (c, S2×T1 +60° β 0.03 single orbit): s21 1.2494, r46 1.4041. Chiral β real (MT partner check by k).
- My family `mtodd` (hyp 20261014T113601.472Z_swarm-ai_hypothesis_1e20): V+ = {α mirror-even, β mirror-odd},
  V− = {α mirror-odd, β mirror-even}. TL: R even in x− at every x+. Q: does V− curvature turn positive at V+ optimum?
- Tools: work/orbits.py (pairs, C6/C6v orbits, δ labels), work/gen_mtodd.py (sector_dirs, combine),
  work/make_stage1.py (1a line; `1b <b> <outdir>` V− set at base b), work/myres.py (my results table).
- Submitted 1a: chiral-odd β S2×T1 b=0.015/0.03/0.045/0.06 per entry (e2b1 4149 4461 ee23).
  1b: V− at parent, 18 evals (S1T1,S1T2,S2T1: aodd ±0.10, beven_pair ±0.05; S2T2 also beven_self).
- Next: when 1a lands, choose base b, run `make_stage1.py 1b <b> work/s1c` (all 24 incl beven_self) and submit.

## 11:58 — wakeup 2
- All 22 mine still queued (broker busy). Board: c claimed STRONG for d698 (1.249/1.404/1.347).
  f: chiral-odd β per-entry b/3: S3×T1 +0.05 → s21 1.558 r46 1.641; S2×T1 1.483; S1×T1 linear to ±0.10.
  f's ascent in S1–S3×T1 odd subspace in flight → likely better base for my stage 1c than S2×T1 alone.
- Plan unchanged; choose 1c base = best pure-V+ point available when 1a lands (maybe f's ascent point).

## 12:24 — wakeup 3: still all 22 pending (broker backlog). Leader now x d524 s21 1.923 r46 2.149; ⊥-α ea28 strong (r46 2.63). No action.

## 12:55 — wakeup 4: first results
- 1a chiral-odd β S2×T1 line (per entry b): 0.015 → s21 1.4358 P (e2b1); 0.03 → 1.6869 P (4149, split/Δ .023);
  0.045 → 1.7008 P (4461, split/Δ .062); 0.06 → 1.4838 FAIL (ee23, split/Δ 0.157). Line max ~0.04, gate-limited.
- KEY: d698 (single +60 orbit 0.03 = V+ 0.015 + equal-norm V− β_even pair) s21 1.2494 vs pure V+ 0.015 → 1.4358.
  V− part costs −0.19 → effective curvature ≈ −0.19/0.0367² ≈ −140 /|β|² there. MT plane = max so far.
- 1b parent partial: S1T1 aodd −/+ 1.0118/1.0000 (curv +1.2/|α|², odd artefact 0.6%); beven_pair − 0.9626.
- Submitted 1c base b=0.03 (16 of 24; rest in work/s1c_b: S2T1 beven_self ±, S2T2 all 6 → submit next).

## 13:22 — wakeup 5
- 1a promoted: b=0.045 (4461) r46 2.4095 r56 2.2250 (conv46 pending); b=0.03 r46 1.9892; b=0.015 r46 1.4506.
- Parent V− curvature table (see result post): β_even strongly negative; α_odd S2T1 POSITIVE (+9.1, 1.035/1.056),
  S1T1 α_odd +1.2; S2T2 β_even pair odd artefact 0.145 (big).
- Posted interim result. Submitted s1c_b (8) + parent S2T1 aodd line ±0.2, ±0.3 (work/s2a; 4c77 4799 95c5 61df).
- Fixed bug: make_stage1.py ran its main body on import (created stray ./2 dir; deleted). gen_one.py = generic builder.
- Next: 1c results → V− curvature at base; if S2T1 aodd stays positive at base, line it at base (MT-broken optimum).

## 13:50 — wakeup 6
- Board leaders now R 6–8 (o f5f1 strong: 6.28/8.33/8.12; s 9a30 s21 7.35). All ≈ pure V+ (work/mtproj.py; validated
  expand vs gamma_on_mesh 3e-15 incl. full stars). aa e3a7 has α_odd 0.079.
- 1a promoted: b=0.03 conv46 1.989 r56 1.824; b=0.045 conv46 2.4095 r56 2.225 (phase-only S2T1 odd line → strong-level).
- Parent S2T1 aodd ±0.10 promoted: r46 1.1484 / 1.1442 (positive curvature holds at r46 too).
- Submitted: aa e3a7 V+ proj (fb87) & MT partner (341b); 9a30 + S2T1 aodd ±0.10 (502f/ac54). Tool: work/gen_on_base.py.
- Posted note on leaders' MT decomposition.
- Next: full α_odd set (9 blocks S1–S3×T1–T3) at 9a30 if S2T1 shows interesting curvature; then β_even self/pair.

## 14:19 — wakeup 7
- 1c (base b=0.03 chiral-odd S2T1 β, R0=1.6869, ε α .10 / β .05) V− curvature, s21:
  S1T1 aodd −2.6 (parent +1.2); S1T1 βe pair −60, self −33; S1T2 aodd **+15** (parent −6); S1T2 βe pair **+108**
  (odd .13), self **+75** (odd −.19); S2T1 aodd −17 (parent +9); S2T1 βe pair FAIL both. Curvature signs flip with x+!
  Big odd parts → wait for r46 (all promoted).
- Leaders now ~10 (av e0a8 10.39/9.87, s c325 9.87/10.15), all pure V+; t 6506 has α_odd 0.143 → submitted its V+ proj
  (13d7) and MT partner (3203).
- e0a8 α_odd probes: S1T1/S2T1/S3T1 ±0.10 (2e8b d97c 2601 7d50 133e 3100); S1T2/S2T2/S1T3/S3T3 ±0.06 (s2d) since
  Σ|α| boundary (pair-star chart) rejects 0.10. Posted request on chart-dependence of Σ|α| boundary.

## 14:48 — wakeup 8
- KEY: r46 of 1c probes (base r46 1.9892): V− curvatures at r46: S1T1 aodd +1.2, βe pair −14.5, self −3;
  S1T2 aodd −2.2, βe pair −7.9, self −12.6; S2T1 aodd **+8.8**. The big s21 positives on S1T2 (+15/+108/+75) are
  s21 ARTEFACTS. s21 unreliable for V− curvature; use r46/r56.
- Parent S2T1 aodd at r46: 1.1484/1.1442 → curv +29. Parent s21 line: +0.2 1.009, −0.2 0.906F, ±0.3 F → local only.
- Leaders: aa e3a7 V+ proj 6.3875 vs e3a7 6.3181 (+1.1%); MT partner 6.3187 (artefact 6e-4!).
  9a30 + S2T1 aodd ±0.1: 7.3566 / 7.4186 vs 7.3454 → +8.4 (consistent sign: S2T1 α_odd positive everywhere except s21 base).
  e0a8 S1T1 aodd −0.1: 10.3912 ≈ base.
- Submitted 9a30 S2T1 aodd line ±0.2, ±0.3 and S1T1/S3T1 aodd ±0.1 (work/s2e).

## 16:46 — wakeup 9 (late; ~2 h gap)
- e0a8 α_odd: 28/28 curvatures negative on all clusters (table in result post). 9a30 S2T1 aodd ≈ flat/neg at r46.
- S2T1 α_odd curvature (r46) along V+: parent +29 → b=.03 +8.8 → 9a30 −0.2 → e0a8 −11.4. Sign flip.
- e3a7 V+ proj neutral; t6506 V+ proj LOSES ~1% (its α_odd 0.143 helps at its point). Partners match (MT map OK).
- Leaders now ~13–14 (w 407a 13.93/13.26/13.79/13.93 strong; av 55f9; al lowsym). All-shell "complex angular rule"
  c ∝ e^{2iδ}-like on T1 (pure V+).
- Submitted 22: w407a c→c+itc t=±.15,±.3,±.6; e0a8 same ±.15,±.3; e0a8 β_even self/pair ±0.03 S1–S3×T1.
  Tools: work/vmshift.py (pure-V− shift), work/phirot.py (unused), work/curv.py (curvature tables).
- Posted stage-2 result. Budget 100/500.

## 17:24 — wakeup 10
- Coherent V− shift (c→c+itc): w407a s21 13.93→13.96/14.01/14.42 (t=.15/.3/.6) but r46 13.26→13.15/12.73/10.33F.
  e0a8: s21 up to 10.61, r46 down to 9.32. ⇒ s21 has POSITIVE even V− response; r46 strongly negative. Posted
  refutation 20261014T172435.951Z_swarm-ai_refutation_4fde (warning to s21-steered optimizers).
- β_even ±0.03 at e0a8 r46: S1T1 pair −5, self −1, S2T1 pair +8 (odd .06), self −61, S3T1 pair −42, self +3 (mixed; r56 pending).
- Submitted V+ projections of al a8c1 (609b), 6f22 (9d99); mailed swarm-al.
- Next: r56 for shifts/β_even → coverage/closing post for mtodd; then pick a new role (budget 102/500).

## 17:57 — wakeup 11
- w407a V− shift r56/conv46 negative (confirms r46). al V+ projections: not meaningful for nematic (MT ∘ rotation needed).
- Posted closing result + coverage: 20261014T175735.296Z_swarm-ai_result_e0ac. mtodd CLOSED. 102 requests, 94P/8F.
- Board: w rec-out leads (fae8 s21 15.90; a8eb strong min 14.56). Most agents done.
- Plan: wait for w's final leader, then certify it with coherent V− shift ±0.15 (2 evals, r46/r56 via promotion), then swarm done.

## 18:44 — wakeup 12
- w leaders fae8 (strong, min 14.83) and 256c (s21 16.11, r46 15.23) sit AT Σ|α| = 2.5 (pair chart) → c+itc probe rejected.
  Used β-only half of the V− shift (β += tα/2, work/vmshift_b.py), t=±0.3 → β_even norm ~0.055. Submitted 4 (work/s4).
- After these land (+r46/r56): final note, then swarm done.

## 19:18 — wakeup 13 — DONE
- β_even V− shift ±0.3 at w fae8 / 256c: below base on s21, r46, r56 (posted note cc61). Optimum respects MT.
- swarm done posted (106/500 charged). Loop stopped.
