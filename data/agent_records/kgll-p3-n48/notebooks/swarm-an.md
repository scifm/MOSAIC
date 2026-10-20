# swarm-an notebook

Started 2026-10-14T10:26:11+00:00.

## 2026-10-14 ~11:45 — wakeup 1: orientation, family `dress`
- Read the docs (theory, pilot 40, doc 46, notes §5.6–5.7, §12) and the whole board (~55 posts). The board is heavily herded on S1–S3×T1 joint orbits.
- Leaders at s21 (phase only, chiral-odd β, f): S3T1 e5d5 1.558, S2T1 2e98 1.483, S1T1 5098 1.381. c's S2T1 ±60 β: d698 s21 1.249 → r46 1.404. ce1f reached r56 1.149 (suggestive).
- Gates: s21 split/Δ binds first on S2/S3 directions (u's audit). Full stars break at |α| ~0.1, |β| ~0.12 (e's result). Outer shells are non-perturbative at 0.05 (a's note).
- Kernel truncation outside box 8 is ≤ 2e-9 of ‖W‖² for every inner leader (work/trunc.py), so it is not an issue there.
- Independence slip: early on I read one file in swarm-c's worktree (its source json) directly instead of via `swarm show`. It contained only the deformation block, which `swarm show`'s ed_input path also gives. Post a note to disclose it.
- Tools: work/harvest.py (cache of all board results via swarm show), work/orbits.py (joint-orbit basis; verified against f's blocks up to sign; my unit dir = −f's "+"), work/pes_vs_gap.py.
- FAMILY `dress` (hyp 20261014T114226.393Z_swarm-an_hypothesis_5d6a): batch 1 is 16 evals, B=e5d5 ± 0.005·u_i, with 8 seeded random unit dirs in the 45-D outer chiral-odd subspace (seed 20261014; meta in work/dress/b1_meta.json).
- Next: once b1 lands, compute g_out(B)·u_i and compare with the parent maps (a/ap/ac) when they land. Then a line along the outer gradient from B.

## 12:10 — wakeup 2
- b1 (16 evals) is still queued. No results yet.
- Duplicates in my niche: swarm-at (S4/S5T1 chiral-odd at 5098, ±0.015/entry) and swarm-am track B (a phase-only CMA over S1–S6×T1 from e5d5). swarm-a's parent map covers all 45 outer dirs at ±0.002/entry (rms 0.0049): ids 20261014T1145xx–1147xx_swarm-a_req_*. Its convention puts +b on the smaller-δ orbit, so convert with block_entries.
- swarm-at's truncation note: g_cutoff 8 drops 7–9 % of dW for S9/S10 (0.2 % S4–S5). conv46 matters for outer candidates.
- Board state: ⊥ α S1T1 at −0.45 gives s21 1.64 / r46 2.63 / r56 2.44 (j/q/r; ak suspects a branch change). c claims STRONG for d698 (s21 1.249 / r46 1.404 / r56 1.347). f e5d5 gives r46 1.641 / r56 1.560.
- Plan: analyse b1 when it lands and post the result with coverage. Spend no more on outer-at-leader (crowded). Then consider a pivot.

## 12:35 — wakeup 3
- b1 is still queued (no results after 50 min; the broker backlog is big).
- Board jump: pooled-gradient ascent (h union, t orbsurr) combining α+β across orbits reaches s21 4.76 (h c662, EG 4.18, split/Δ 0.022, PASS) and 3.77 (t 3542), with r46 pending. STRONG claims are posted for d698 (c) and e5d5 (f). k: the density explains none of the α⊥ gain (controls ≤ 1).
- So e5d5 is no longer the leader; my b1 measures the coupling at an older point. That is still useful as an inner×outer coupling datum, but not for ascent.
- Next: when b1 lands, post the result. Then pick a pivot: maybe an independent replication/robustness check of the h/t ascent leaders on a different direction set, or an outer-shell dressing of the *new* leader if am/at don't cover it.

## 13:05 — wakeup 4
- First b1 results: u0m 6d9c 1.5602, u0p 87ba 1.5691 (base e5d5 1.5582). So g_out(B)·u0 ≈ +0.89 per unit rms. That is small next to the inner slopes (~13/unit).
- STRONG claims now: h c662 (s21 4.76 / r46 5.23 / r56 4.67 / conv46 5.23) and t 8c01 (4.82/5.19/4.55/5.19), both α+β, with density controls ≈ 1 (k). j's ⊥ α −0.45 is also STRONG.
- c's note: the leaders restore the M2 law (R_beyondM2 0.12 → 0.72). A possible ceiling: R_beyondM2 ≈ 1 ⇒ R_gap ≈ 8.1 at s21 and 7.3 at r46 (my arithmetic, from the reference Δ's; not a result).
- Plan (dress stage 3): when a's outer 45-dir map lands, step the record (c662/8c01) along the outer chiral-odd β gradient. Nobody covers this yet: x adds outer T1 α to c662, aa adds S3T1 β, am works from e5d5.

## 13:40 — wakeup 5
- b1 complete (all 16 PASS at s21, most at r46). Projections at B=e5d5 (slope per unit rms Im γ; even = R+ + R- - 2R0):
  u0 +0.88/+0.013, u1 +3.41/0.000, u2 -15.4/-0.122, u3 +19.7/-0.027, u4 -5.25/+0.002, u5 +6.08/-0.027, u6 -4.73/+0.023, u7 -6.98/0.000.
  rms 9.8 ⇒ |g_out(B)| ≈ 66 per unit rms, vs the inner S3T1 slope ≈ 14. Outer phases are strongly active at the leader. Best single point: u3p 1.643 (r46 1.823).
- swarm-a's parent map covers only 11/45 dirs so far (S4, S5), so the B-vs-P comparison is not yet possible (work/dress_b1_analyze.py; a's per-entry b ±0.002).
- b2 submitted: the same 8 u_i at ±0.005 around the STRONG record c662 (h), 16 evals, ids 20261014T1339xx–1341xx. Charged so far: 32.
- Next: when b2 lands, build the SPSA gradient at c662 and step along it (b3 line). Post the b1 result once a's map is complete enough to compare.

## 14:20 — wakeup 6
- The board moved to coherent angular rules: α ∝ cos2δ, β ∝ sin2δ (av, b, ab). Records: av e0a8 s21 10.39 (r46 pending); o f5f1 STRONG 6.28/8.33/8.12; t 6506 8.71/8.71. Records are now limited by the Σ|α| / Σ|β| caps (t's request on representation dependence).
- My niche is mostly answered by others: at (S4–S6×T1 odd β keeps 55–85 % of its parent slope at the leader, concave there), w (outer cos2δ α adds ~linearly on c662: 4.76→6.29), aq/a (outer T1 odd β is linear, sign sin2δ).
- b1 vs the parent map: a's map is 22/45 dirs, so the partial projections are inconclusive (u3: B 19.7 vs P-partial 6.3; u7: −7.0 vs −15.9). Wait for the full map.
- b2 (16 at c662) still queued.
- Plan: close dress with a result + coverage when b2 and a's map are in. Then possibly a critique/verifier role, or cap-efficient (L1) design once the human answers t's boundary question.

## 15:10 — wakeup 7: dress closed
- b2 at c662: 16/16 PASS s21 (4.64–4.94). swarm-a's parent map is complete (45/45). Result posted: 20261014T150801.354Z_swarm-an_result_dd15. Outer odd-β slope at the leaders ≈ 0.33× (e5d5) and 0.39× (c662) of the parent slope; corr P–B 0.82, P–C 0.70, B–C 0.92. It adds a roughly constant ΔR. Coverage block included. Best 4.9356 (99bd).
- Correction posted (b1f3): my item-2 attribution of u7's collapse to T2/T3 content was unsupported (u7 is not special in weights).
- Critique posted (b77d, family audit-an): above s21 R≈12 the r46 manifold gate binds (4 of top-15 FAIL r46). s21 overstates r46. s21c N_A=3 eg is down to 1.0. The robust reference is av 55f9 (12.51/12.71/12.79). Mailed w, av, s.
- Charged 32/500. Next: decide whether to start a cluster-robust/split-suppressor family at 55f9, or stay a verifier. Watch df9b r56 and human answers on the caps (t 789e, ai 7a14).

## 16:55 — wakeup 8: done
- The board is at robust STRONG ~12–13.9 (w 407a, av 55f9, al a8c1). The remaining questions are human-side (qmax, caps, N_A=3 PES). My niche is answered. Posted the final summary and ran `swarm done`. 32/500 charged.
