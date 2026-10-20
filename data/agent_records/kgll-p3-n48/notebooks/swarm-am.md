# swarm-am notebook

Started 2026-10-14T10:26:08+00:00.

## 2026-10-14 11:35 — wakeup 1: orientation, family cmaorb, gen 0
- Read brief, docs 46, theory §6.4, kdep_envelope.py; board (30 posts), leaderboard.
- Board state: swarm-c jorb leaders at s21: S2xT1 +60° β=+0.03 → 1.2494 (`_req_d698`), −60° β−0.03 → 1.2403;
  S1xT1 ⊥ α−0.05 → 1.1709 s21 / 1.1699 r46 (r46 tracks s21 within 0.3 % for 3 leaders). Chiral-odd β gives linear gains (swarm-f MT argument).
- Crowded: mappers a,b,c,d,f,g,j,l,m,q,r,v,w,ae,af,ad; optimizers e,h,o,u,x; verifiers k,y; theory s (noQ0: ⊥ channels carry Q=0 static-LL-mixing content).
- My family `cmaorb` (hyp `20261014T113459.820Z_swarm-am_hypothesis_f13c`): CMA-ES, track A phase-only over 18 joint orbits S1–S3×T1–T2,
  λ=12, σ0=0.03, seed 1701, box |β_orbit|≤0.15, L1 3Σ|c|≤1.9 (repair by rescaling). Fitness −R(s21), FAIL→0.5.
- Code: work/orbits.py (orbit table; matches swarm-c +60 orbit), work/cmaes.py, work/drive.py (init/ask/tell/table TRACK; state in work/cma_A/).
- Observation posted: broker L1 Σ|β| is representation-dependent (pair-entry repr costs 3× full-star).
- Gen 0 submitted (12 reqs, ids in work/cma_A/gen000/pending.json).
- Next: `drive.py tell A` once gen0 done → `ask A`. Every 4 gens re-rank elites by cluster min.

## 2026-10-14 11:53 — wakeup 2: herding, switch to track B
- Missed at wakeup 1: z (rcma), ag (fsmin: phase-only 24-D CMA S1–S3×T1–T3 no-Q0, cluster-min), n (minmax) — three CMAs before me. Track A = dup of ag → stop after gen0 (gen0 still queued; broker slow, >20 min latency).
- Leaders now: ⊥ α S1T1 −0.45 → 1.6386 s21 (j/q/r); f_req_e5d5 S3×T1 chiral-odd β ±1/60 → s21 1.558, r46 1.641; h S4×T1 α contrast → 1.572.
  r46 ≥ s21 for chiral phase orbits (p's note). Outer shells non-perturbative above ~0.01-0.05 (swarm-a).
- Track B (note `20261014T115256.060Z_swarm-am_note_e401`): phase-only 21 orbits S1–S6×T1, mean at f's leader (idx6=−1/60, idx7=+1/60), σ0=0.01, outer scale 0.4, seed 2701. gen0 submitted.
- Next: tell A gen0 (then post data, don't ask again), tell/ask B each wakeup.

## 2026-10-14 12:15 — wakeup 3: waiting on queue
- All 24 of my reqs still pending (broker congested, >40 min). No action.
- Board: c STRONG claim (phase-only S2×T1 +60 β0.03: 1.249/1.404/1.347). ⊥ α −0.45: 1.64/2.63/2.44 (j); ak critiques branch change at −0.35;
  k: density controls lower gap (density not the mechanism). at: g_cutoff 8 truncation 7–9 % for S9/S10, 0.2 % S4–S5 → my S1–S6 track OK.

## 2026-10-14 12:40 — wakeup 4
- First 3 track-A results: c00 R=3.23 FAIL(PES), c01 0.0006 FAIL, c02 0.33 FAIL(splitting) → random 18-orbit β at σ0.03 (L1~1.4) is outside the Laughlin window. Expected; A is stopped anyway.
- Board: h union α+β step s21 R up to 4.76 PASS (superadditive α·β); f STRONG claim S3×T1 odd β 1.558/1.641/1.560 conv 1.641; j STRONG α⊥ −0.45 2.63 r46.
  e: PES entanglement gap drops 13→4–5 for leaders (still pass). Mechanism (k,u): not density, not projected-interaction scale.
- Waiting for B gen0.

## 2026-10-14 13:07 — wakeup 5
- Track A gen0: 12/12 FAIL (7 manifold destroyed R≈0, 4 broken R<0.8, f449 R 3.23 PES-FAIL). Posted abandon+coverage `20261014T130635.176Z_swarm-am_abandon_5b1e`.
- Board records: h c662 STRONG 4.76/5.23/4.67 (α+β union, has Q=0 ⊥ content); t 8c01 4.82/5.19. av: records follow α∝cos2δ, β∝sin2δ on S1/S2×T1(+T2); S3 & outer unused.
  Phase-only best: s noQ0 phase-only 1.73/2.32/2.14; ae S2×T1 odd β 0.03: 1.687/1.989.
- Track B (phase-only S1–S6×T1 from f's S3 leader) gen0 still in queue. Its niche: S3 + outer shells phase, which the records don't use.

## 2026-10-14 13:33 — wakeup 6
- Track B gen0 partial: c00 cbeb 1.594 PASS (→r46), c01 1.071, c02 0.926, c03 1.395 FAIL(split 0.18), c04 0.74 FAIL; 7 pending.
- f: phase-only s21 ceiling ≈1.72 across 4 directions (s21 splitting gate binds; r46/r56 keep rising). y: min over clusters is s21 or r56.
  → Track B's real question: can S3/outer phase relieve the s21 splitting ceiling for phase-only? s21 fitness is the binding objective, keep.
- Claims: h c662 4.76/5.23/4.67; t 8c01 4.82/5.19/4.55; s noQ0 phase-only bfbb 1.725/2.322/2.142; v outer S7×T1 α 1.561/1.933/1.787.

## 2026-10-14 13:55 — wakeup 7
- Track B gen0 told: best c00 cbeb 1.594 PASS (beats start 1.558), c11 1.542, c05 1.404; 6/12 FAIL (manifold). median 0.71, σ→0.0093. Gen1 submitted.
- Board record: o f5f1 s21 6.28 / r46 8.33 / r56 8.12 (α+β, Σ|β|=1.88 near cap). t asks human about representation-dependent L1 caps.
  Phase-only ceiling at s21 ≈1.72–1.73 (t 452c 1.727/2.221/2.035; s bfbb). p verifier done.

## 2026-10-14 14:25 — wakeup 8
- B gen0 best cbeb: s21 1.594 / r46 2.517 PASS (phase-only; r46 above at's beff 2.33); 2e70 1.542/2.342. Gen1 in queue.
- Board: phase-only s21 ceiling ~1.73 is robust (b: no shell profile lifts; at: outer adds concavely). α+β records cap-limited: av cos2d rule s21 up to 10.39 at Σ|α| cap;
  x outer α at c662 7.22/8.20; aa S3 odd β on 8c01 6.32. u: qmax-8 non-PSD for R≈10 records — conv46 matters.
- Plan: run B gen1–2, then close B with coverage (likely confirms the ceiling). Then consider done or a small verifier task.

## 2026-10-14 14:57 — wakeup 9: close B, done
- B gen1: best 2470 s21 1.606, 79f3 1.602; 7/12 FAIL. Mean drifts to S3×T1 odd (−0.020/+0.034), outer small. Posted close+coverage `20261014T145656.492Z_swarm-am_abandon_7481`.
- Board endgame: STRONG claims ~10 (av e0a8 10.39/9.87/10.50/9.96; s c325 noQ0 9.87/10.15/9.54/10.15), cap-limited; phase-only ceiling 1.73 (s21 gate).
- Nothing distinctive left for me (optimizers/verifiers saturated). 36/500 charged. Running `swarm done`.
