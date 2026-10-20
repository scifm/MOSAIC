# swarm-ae notebook

Started 2026-10-14T10:25:37+00:00.

## 2026-10-14 ~11:30 — wakeup 1: survey + s2phase batch 1
- Board: ~25 agents active. Separable full-star maps (a, b), joint-orbit maps (c jorb, g joint-orbit,
  f chiral-odd β, d chiral half-shells), ⊥ amplitude (j, r, q), combos/surrogates (h, x, o), high shells (v, w),
  finite size (y fsmatch, q), mech (k), big amplitude (e), kpow (i), phase Hessian (l, m).
- Facts: chiral-orbit phase responses are huge. S2×T1 o±60 β=0.03 → s21 1.249/1.240; S1×T1 +30 β=0.03 → s21 1.1595,
  **r46 1.1586** (transfers!). ⊥ S1×T1 α=−0.05 → 1.171. The separable axes give only ~1 %.
- Tools: work/geom.py (pair-star orbits, δ=∠R−∠G mod 180, block builder, write_input from the swarm template).
- Chose family `s2phase`: β line scans of the S2×T1 o60 orbit (single, odd, even). Hypothesis 20261014T113002.525Z_swarm-ae_hypothesis_1154.
- Submitted batch 1: 16 evals (work/b1). Mailed swarm-c about the δ convention.
- Next: read the R(β) line plus promotions. Then batch 2, the T2/T3 profile at the best β (chiral-odd signs), then S3×T1 ±30.

## 2026-10-14 ~11:50 — wakeup 2
- Batch 1 still queued (broker congested; 48 agents).
- Key news: d698 (S2×T1 o60 β 0.03) r46 = **1.4041**, but s21 split/Δ = 0.048 (gate 0.1), per u's audit cb13. f 5098 (S1×T1 chiral-odd β ±0.067) s21 1.3806, clean split. Full-star β breaks Laughlin near 0.12 (e, l).
  k: matched-density control for α⊥ explains none of the gain. l: conv46 == r46 for pure LL0.
- c confirms my o60 = their o+60 (same matching and δ sign).
- Ceded the T2/T3 β profile to ao (T1+T3 mixtures), e and au. Note 20261014T115130.495Z. Keeping the line, the finite-size table (R and split/Δ) and possibly the S2-best + f5098 line.
- Next: tabulate batch 1 when it lands; watch for an s21 split FAIL on the line.

## 2026-10-14 ~12:17 — wakeup 3
- All 16 of my requests are still pending (about 50 min in the queue); other agents' results are landing.
- Board leaders (claims): c STRONG d698 S2×T1 o60 β 0.03: 1.249/1.404/1.347 (s21/r46/r56). f STRONG S3×T1 chiral-odd β 0.05:
  1.558/1.641/1.560 (conv46 1.641). j ⊥α −0.45: 1.64/2.63/2.44 (an ak critique says s21 changed branch). h S4×T1 α c0+: 1.57/1.72/1.61.
  k: density controls lower the gap, so the gains are not density. q/u: s21 manifold splitting is the binding gate on the leader lines.
- T2/T3 β of the S2 orbit now sits with au (harmladder). ao dropped stage 2.
- Plan: wait for the batch 1 lines. Hold any new submissions until they land; the queue is the bottleneck.

## 2026-10-14 ~12:45 — wakeup 4: batch 1 landed
- S2×T1 odd(b) = o60(+b)+o120(−b): b=0.015 → 1.436/1.451 (s21/r46); **b=0.03 → 1.687/1.989** (0df7, r56 running); 0.06 → 1.48 FAIL (split 0.157).
  odd −0.03 → 0.219. even +0.03 → 0.365 FAIL. Single o60 peaks at 0.03 (1.249/1.404) and FAILs from 0.045 on.
  o60 at 0.12/0.18 gives R ~2.4 but FAILs (eg 0.25): another phase.
- Posted result 20261014T124429.912Z_swarm-ae_result_ee09.
- Submitted b2: odd b ∈ {0.0225, 0.035, 0.04, 0.045, 0.05} (5 evals). Charged so far ~21.
- Board top is now multi-orbit α+β combos: t 8c01 s21 4.82 / r46 5.19; h c662 4.76 / 5.23. Phase-only is much lower.
- Tool: work/tab.py <ids> prints R, sp/Δ and eg per cluster.
- Next: locate the s21 gate edge on odd. Then maybe take the phase-only direction further: odd S2 + odd S3 (f) + odd S1. Check aa's chi3map first.

## 2026-10-14 ~13:12 — wakeup 5
- Refinement b2 (5 pts) still queued; 0df7 r56 still running. No spectrum detail in result.json (only gap and splitting).
- Board: c662 STRONG α+β 4.76/5.23/4.67 (h claim). s noQ0 C 2.51/2.61/2.40. Phase-only β D1+D2 (S1 odd + S2 odd at 0.03): 1.725/2.322/2.142 (bfbb).
  s finds the α and β pieces split the s21 manifold in opposite senses, so combos relieve the gate. av: records follow α~cos2δ, β~sin2δ.
  am: random phase-only directions all FAIL (the gains are directional).
- The phase-only S1–S3×T1 subspace is saturated (aa map, s, f, ag CMA, b/ab coherent). Mailed aa the line overlap.
- Plan: finish s2phase (refinement + r56), post the coverage, then switch to verifier/critic or an untaken niche. Keep spending low.

## 2026-10-14 ~13:45 — wakeup 6: s2phase closed
- 0df7 full ladder: 1.6869/1.9892/1.8242/conv 1.9892, broker claim = strong (phase-only).
- ai's mtodd line duplicates mine (b=0.045: 1.7008/2.4095/2.2250; 0.06 FAIL). aa's S2 axis also. f: phase-only s21 ceiling ≈1.72.
- Withdrew the 5 refinement requests (redundant; lanes congested). Posted closing result + coverage 20261014T134256.979Z_swarm-ae_result_dbff.
- Charged: 16 completed (+5 withdrawn, possibly charged). Posts so far: hyp, note, 2 results. **The next post should be a critique** (rule 11).
- Checked v's STRONG S7×T1 α claim (0268): conv46 ≈ r46, S ratio = parent's; nothing wrong. t's 8c01 is waiting on its own density control (t asked the human).
- Next: look for an untaken niche or a substantive critique. Keep load low; other agents report stuck lanes.

## 2026-10-14 ~14:17 — wakeup 7: audit + done
- Records now reach s21 R ≈ 10 (av cos2d) and are Σ|α| cap-bound. Many agents are closing.
- Posted gate-margin audit 20261014T141536.881Z_swarm-ae_note_0302: top 40 rows have eg 2.3–4.3 and s21 split/Δ ≤ 0.07, so they are cap-limited.
- Ran `swarm done` (21 charged). Rationale: every subspace has multiple owners, lanes are congested, records are cap-bound.
