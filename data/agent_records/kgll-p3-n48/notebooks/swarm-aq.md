# swarm-aq notebook

Started 2026-10-14T10:26:23+00:00.

## 2026-10-14 ~11:45 UTC — wakeup 1: scope chosen = `outer-odd`
- Read board (≈35 hypotheses). Board state: chiral-odd phase β on inner shells is the master direction
  (f e5d5 |G|²=4×T1 b=.0167 → s21 1.558; c d698 S2×T1 +60° β=.03 → s21 1.249, r46 1.404). Separable β
  axes are even (M·T, confirmed by h). Inner S1–S3 is heavily herded (c,f,g,j,q,r,x,z,ag,n,ae,s...).
  Outer shells: only first-order α_even (v,w) and half-shell separable β (d). Outer chiral-odd β = unmeasured.
- Tools: work/orbits.py (joint orbits, δ labels, chiral-odd pairs, block builder), work/gen_outer.py,
  work/dump2.py (board summariser; `swarm show` + read ed_input). NB: subprocess needs stdin=DEVNULL.
  Don't `pkill -f` patterns matching own shell.
- Convention: +b on orbit δ<90, −b on 180−δ, per pair-entry (same as f). Diagonal pair-star blocks.
- Posted hypothesis 20261014T114215.484Z_swarm-aq_hypothesis_b960; mailed f proposing split (f: S1–S3, me: S4–S10).
- Submitted b1_t1: 30 evals (15 outer dirs × ±0.01) on T1. b2_t2/b3_t3 generated + checked (60), submit when slots free.
- Next: read b1 results → slopes table; submit T2/T3; then lines on strongest outer dirs and add to inner leader.

## 2026-10-14 ~12:10 UTC — wakeup 2: outer-odd ceded, new family `perp-prof`
- outer chiral-odd β was claimed 5× (a, ap, ac, as, me). a's 45×± at 0.002 already charged → I ceded (note 722a),
  kept my 30 T1 points (b=0.01) as a curvature check vs a's slopes. Did NOT submit b2_t2/b3_t3.
- Board leader: j's S1×T1 ⊥ α line (ea28, α⊥=−0.45: s21 1.639 / r46 2.632 / r56 2.445). s21 splitting gate binds.
  c's claim STRONG (d698 phase-only 1.249/1.404/1.347). l: conv46 ≡ r46 for pure LL0.
- New family perp-prof (hyp b95f): c12 = (G,2R) S1×T3⊥ harmonic (no Q=0 content), c21 = (2G,R) S3×T1 δ90, at c11 ∈ {−.2,−.3,−.45}.
  work/gen_perp.py; build(c11) reproduces j's blocks exactly. Batch p1 = 16 evals submitted. Mailed j, r.
- Next: read p1 → best sign of c12 → 2-D (c11,c12) grid; post outer-odd T1 table + coverage.

## 2026-10-14 ~12:40 UTC — wakeup 3
- No results yet (broker queue deep). Withdrew all 30 outer-odd reqs (they still run, at the back) so perp-prof gets slots.
- Board: j STRONG claim ea28 (⊥ α −0.45, conv46 2.632); f STRONG claim e5d5 (S3×T1 odd β, 1.558/1.641/1.560);
  k: density controls lower the gap (leader not density). h: outer α orbit S4T1 c0+ 1.572/1.720/1.614.
  e: PES entanglement gap drops 13.4→2.5 at ⊥ leader (gates still pass). m: perpchi (⊥ × phase leaders) claimed.

## 2026-10-14 ~13:10 UTC — wakeup 4: records at ~4.8×; new family rec-T3
- Records: h c662 (4.760/5.226/4.674, conv46 5.226, STRONG), t 8c01 (4.816/5.186/4.551). Multi-orbit α+β, superadditive.
  c: leaders restore the M2 law (R_beyondM2 0.12 → 0.6–0.72); test = does it go beyond 1. k: density controls ≈ 1 → not density.
- Decomposed records (work/gen_rec.py record_entries): S1×T1 {30,90,150}, S1×T2, S2×T1 + small S2×T2/T3, S3×T1/T2. NO S1×T3.
- Posted hyp rec-T3 (5a3a). Submitted r1: 13 evals = c662 rebuilt base + S1×T3 orbits δ30/90/150 × α±0.03, β±0.02.
- perp-prof (16) still queued; only 3 running. Withdrawn outer-odd still hold in-flight slots (withdraw doesn't free slots).
- Charged so far 33 (charge at acceptance). Next: gradient from r1 → line; post perp-prof + outer-odd tables.

## 2026-10-14 ~13:45 UTC — wakeup 5
- outer-odd T1 interim (16/30 done, b=±0.01 per entry, + = smaller δ): EVERY + direction gains, − loses.
  g12 1.497/0.527, g13p0 1.326/0.704, g13p1 1.534/0.482, g13p2 1.298/0.730, g16 1.449/0.607,
  g19p0 1.117/0.890, g19p1 1.415/0.630, g19p2 1.354/0.702. Splitting/Δ ≤ 0.034 on + side. Strongly linear.
- LESSON: withdrawing blocks promotion — the + points never climb. Resubmitting identical input should be free
  (existing evals) → do it for the + points once the queue drains (to get r46/r56 per direction).
- Board: lanes reported stuck (o, j requests). Claims: v STRONG S7×T1 α cos2δ 1.56/1.93/1.79; s noQ0 STRONG;
  f phase-only s21 ceiling ≈1.72; ap: records' γ on uniform LL0 lowers gap (γ×ρ* cooperation); aj: T1+T3 shaping of
  S2×T1 α leaders does not help (concave, optimum≈0) — relevant prior for rec-T3.

## 2026-10-14 ~14:20 UTC — wakeup 6
- outer-odd all 30 landed; posted result+coverage 848e. Purely odd (even ≤3.4%), sign sin2δ>0 gains,
  slope/sin2δ ≈ 0.5 per 0.01 entry on all shells 7–21 (falls ~25% at 19/21). Best 23dd 1.5335 (not promoted).
- perp-prof partial: T3⊥ alone −0.1 → 0.839, −0.2 FAIL; on ⊥ line c12=+0.05@−0.2, +0.03@−0.3, c21=−0.02@−0.3 all FAIL.
  "failed" status = gate FAIL (not infra).
- Board: av cos2δ+i·sin2δ rule S1–S3×T1 → s21 10.39 (e0a8), 9.67/r46 10.49; s c325 9.87/10.15; o f5f1 6.28/8.33/8.12 STRONG.
  Caps (Σ|α| 2.5, Σ|β| 2.0) bind; representation-dependent (t request 789e). Swarm converging on e^{2iδ} rule.
- My remaining: rec-T3 (13 at c662) + perp (~10) queued. Then likely wind down (marginal value of extra budget low)
  unless rec-T3 shows a non-trivial S1×T3 gradient worth a line at the av/f5f1 records.

## 2026-10-14 ~14:50 UTC — wakeup 7
- perp-prof: more gate FAILs (8a89, ee60, 6372 = c12 at −0.3/−0.45 lines). T3⊥ harmonic destructive throughout so far.
- rec-T3 13 all running (pending). Board: av STRONG e0a8 10.39/9.87/10.50/conv46 9.96; inner T2/T3 null (ar, av, i, ao);
  T3 "anti-rule". u: qmax-8 interaction non-PSD at R≈10 (conv46 qmax 10 fixes; ~1% effect). x: outer α adds at record.
  Many agents finishing (c, ac, ae, q, p, g, d, ak, aj done).

## 2026-10-14 ~16:45 UTC — wakeup 8
- rec-T3 13 + perp 9 still pending (3.5 h; slow lanes). Board records now 11–14 (h 5063 11.65/12.30/11.97 STRONG;
  w 407a 13.93 but qmax unconverged r46→conv46 +5%; y: conv46/r46 shift up to +20% above R≈9). o/h: S1T3 & T2/T3 at
  records = ballast → my rec-T3 now redundant (answers itself). Plan: let charged runs land, post coverage, swarm done.

## 2026-10-14 ~17:35 UTC — wakeup 9
- "pending" status = s21 done, ladder still climbing (my mytab.py only printed "done" before — fixed).
- rec-T3 at c662 (base reproduces 4.7599/5.2257): −α on all S1×T3 orbits +3–4%/orbit (s21 & r46), β anti-rule on r46;
  cap-inefficient (~1.7 R/Σ). perp-prof: c12=−0.03 at α⊥=−0.45 → s21 1.761 (split 0.013) but r46 2.383; trade.
- Posted result 8aa7 (both families, coverage). Submitted r2: S1×T3 direction on z e327 (t=.5,1,2) and x 06bb (t=1).
- Board: s21 records ~15 (w a8eb, z e327 unconfirmed); class-A confirmed ≈11.7–13.0 (av 55f9 12.51/12.71/12.79/13.00).
- Next: read r2 (4 evals); then swarm done (≈63/500 charged).

## 2026-10-14 ~18:10 UTC — wakeup 10: finished
- r2: e327 + S1×T3 dir: t=0.5 min 14.372, t=1 (4792) 14.85/14.52/14.37/conv 14.92 (broker STRONG), t=2 r56 drops.
  06bb + dir: 11.98/11.78 (≈0). Increment +1% over e327 — within finite-size spread. Posted claim c67b (credit z),
  request 0333 (density control), mailed z. Then swarm done.
