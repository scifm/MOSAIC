# swarm-at notebook

Started 2026-10-14T10:26:35+00:00.

## 2026-10-14 ~11:40 UTC — wakeup 1: scope chosen
- Board: ~35 agents active, nearly all in S1–S3×T1–T3 joint orbits (maps a/b/c/g/f, lines q/ae/j/r, CMA z/ag/n, pooled h/o/t/u/x).
  Leaders are phase-only chiral: c d698 (S2T1 δ60 orbit β=.03: s21 1.249, r46 1.404), f 5098 (S1T1 chiral-odd β=1/30: s21 1.381).
- Key facts: M·T symmetry, (α_δ,β_δ)->(α_−δ,−β_−δ); chiral-odd β is the only phase direction with linear TL term. s21 chirality artefact ~1-2.5%.
  Response is very nonlinear (rms|γ|≈.05 moves R .42→1.25). Geometry does not predict R (swarm-k).
  Σ|β| bound counts pair entries (pair-star form uses it 3x faster).
- My family `outer-at`: 45 outer (S4–S10×T1–T3) chiral-odd β directions, ±0.015/entry at base f-5098. Hypothesis 20261014T113952.734Z_swarm-at_hypothesis_11ad.
- Tools: work/orbits.py (orbits, chiral-odd dirs, block_from / coefs_from_block, write_input), work/gen_s1.py; inputs work/s1{a,b,c}/ (30 each), manifest work/s1_manifest.json.
- Submitted s1a (30: S4×T1-3, S5, S6) → ids in work/s1a_ids.txt. s1b, s1c pending (in-flight cap 32).
- Next: submit s1b/s1c as slots free; analyse slopes (work/analyse_s1.py to write); stage 2 line search along outer gradient.

## 2026-10-14 ~12:05 UTC — wakeup 2: deduped, cutoff note
- Outer chiral-odd β sector claimed 7× (a, ap, ac, aq, as at parent; an + me at leader; c herding round 2).
  Withdrew my 11 queued (S5T2..S6). Kept 20 accepted: S4×T1–T3 all 9 chiral-odd dirs ±0.015 + S5T1 ±, around f-5098. Mailed an (they own the rest at-leader).
- Note posted 20261014T120408.787Z_swarm-at_note_8343: g_cutoff 8 (screen/r46/r56) drops 7–9% of first-order dW for S9/S10 deformations; S1–S5 ≤0.2%. conv46 (box 10) is not a duplicate of r46 for outer-shell candidates. Script work/cutoff_check.py.
- Board state: c claims STRONG (d698 phase-only, 1.249/1.404/1.347, conv46=r46). Leaders: α⊥ −0.45 s21 1.64 r46 2.63 (ak: suspected branch change); f e5d5 S3T1 odd β .05/3 per entry s21 1.558 r46 1.641.
- Result summaries only expose gap, splitting, PES eg (no per-momentum spectrum) → branch-resolved modelling not possible.
- Next: analyse S4 at-leader table when in (work/analyse_s1.py, manifest covers all 90; only 20 will have ids), post result + coverage; look for a genuinely unclaimed niche or act as critic.

## 2026-10-14 ~12:30 UTC — wakeup 3
- Withdrawn requests still run ("queued runs go to the back") and were charged: 30/500 charged. All 30 (S4×T1–3, S5×T1–3, S6×T1–3 at 5098) will land → full S4–S6 at-leader map.
- an agreed split (they: random outer projections at e5d5; me: S4–S6 coordinates at 5098). am track B CMA S1–S6×T1 from e5d5 overlaps.
- l corrected their conv46 request citing my cutoff note. Leaders now: t f0fb s21 3.51 (orbsurr combos), x d524 1.92/2.15 r46. f STRONG claim S3T1 odd β 1.558/1.641/1.560.
- No results for me yet. Next: analyse when landed.

## 2026-10-14 ~13:10 UTC — wakeup 4
- First at-leader results (base f-5098 s21 1.3806): S4T1odd49 ±0.015 → 1.7011 / 0.5888 (half-diff .556, curv −.24); S4T1odd11 → 1.6130 / 1.0792. Phase-only, so the +0.015 point (1.70) is level with the board's best phase-only (ae S2T1 odd 1.687 s21).
- Board: records c662/8c01 (h, t) α+β unions s21 ~4.8 / r46 ~5.2, STRONG; R_beyondM2 ~0.6–0.72 (c note: restoring M2 law, not beating it). Many verifiers (p, g, u, k, i, as, ap).
- analyse_s1.py parallelised. Next: full S4–S6 table → result post with coverage; consider a phase-only line S1T1odd(5098) + t·S4T1odd49 since it's a clean beyond-M2 / no-Q0 direction.

## 2026-10-14 ~13:45 UTC — wakeup 5: S4 at-leader map complete
- S4 (|G|²=7) chiral-odd β ±0.015 at f-5098 (base 1.3806): T1 all strongly + (δ49: 1.701/0.589; δ71: 1.681/0.873; δ11: 1.613/1.079); T2 weak (δ19 1.309/1.014, δ79 1.394/1.200, δ41 0.660/0.566 FAIL−); T3 negative (δ71 .974/1.219, δ11 1.148/1.356, δ49 .498/.701 FAIL both).
- beff (S4T1odd49 +) = broker claim 'strong': s21 1.701 / r46 2.330 / r56 2.156 / conv46 2.330, Chern 1, PES pass; split/Δ s21 0.054. e0b9 (δ71+) r46 2.025; dc51 (δ11+) r46 1.769 r56 1.658.
- Phase-only board ceiling ~1.73 at s21 (b d586, t 452c, s bfbb, aa, f ...) — s21 manifold splitting binds; beff is level with it, not a record.
- analyse_s1.py bug fixed (ids now in columns 6,7). Waiting on S5/S6 (12 points) → then result post w/ coverage.

## 2026-10-14 ~14:15 UTC — wakeup 6: S4–S6 map done, result posted, stage 2 submitted
- Result post 20261014T140757.988Z_swarm-at_result_e1f5 (coverage incl.). NB the post's pass/fail count says 22/0/8; correct is 21/0/9 — fix in next coverage.
- At leader, outer T1 slopes = 0.57–0.87 × parent slopes (a's a70f, per unit rms), concave; T2/T3 destructive.
- Gain per s21 split/Δ increase: S4T1 d11 ≈24, d71 ≈13, d49 ≈6.4, S5 5.7, S6 2.6. Phase-only s21 ceiling ~1.72 (f ff14) is set by s21 splitting.
- Stage 2 (8 evals, work/s2, ids work/s2_ids.txt): base f-5098 × inner scale {1,1.5,2} + S4T1 odd d11/d71 combos. Test: can low-splitting directions push phase-only past 1.72 at s21?
- Records elsewhere: o f5f1 s21 6.28 / r46 8.33 (Σ|β| near cap), h un2 6.59.

## 2026-10-14 ~14:45 UTC — wakeup 7
- Stage 2 (8) still pending. Board: record e0a8 (av, cos2δ+i sin2δ S1–S3×T1) 10.39/9.87/10.50/conv 9.96 STRONG, cap-limited (Σ|α|). b: no shell profile lifts phase-only s21 ceiling ~1.73. aq: outer odd slope ∝ sin2δ ≈0.5/0.01 every shell. u: qmax-8 non-PSD pair interaction at R≈10 records. Many agents posting `done`.
- Plan: if stage 2 can't beat ~1.73 at s21, post short closing result (phase-only ceiling is not lifted by low-splitting directions either) + corrected coverage, then `swarm done`.

## 2026-10-14 ~16:55 UTC — closed
- Stage 2: best phase-only s21 1.699 (c4a2); d11+d71 combos split superadditively (FAIL ≥ .025 each); r46 up to 2.482 (858f). Posted 20261014T165147.526Z_swarm-at_result_09ab (closing coverage, corrected counts).
- `swarm done` posted (38/500 charged). Loop stopped.
