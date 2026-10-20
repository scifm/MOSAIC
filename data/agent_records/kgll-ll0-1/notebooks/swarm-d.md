# swarm-d notebook

Started 2026-10-02T03:51:14+00:00.

## 2026-10-02 04:13 — wakeup 1: scope chosen, phase 1 submitted

**Board when I arrived:** a = w3 star atlas (S1-S8×T1-T3, α/β ±0.02); c = w3-wide CMA-ES (stars S1-S4×T1-T2);
e, f, b = w2 atlases/CMA; h = w3-orient (joint-orbit A/B modes on S1-S3×T1-T2).

**Key insight (posted, hyp 20261002T041056.492Z_swarm-d_hypothesis_6816):** the symmetry is M·T, not M.
γ → conj γ(Mk,Mr). Mirror-even X (all star products, h's A): R even in β → β slope = 0 in the TL.
Mirror-odd X (chiral, h's B): R even in α, β slope allowed. So first-order phase-only gains (beyond-M2) only
on mirror-odd X. No ladder cluster is mirror-symmetric (checked: Nk=21 C6 chiral; 4×6, 5×6 C2 only), so
"forbidden" slopes show up as finite-size artifacts. Mailed h (their B prediction was inverted), a and c.

**Tools:** `work/chiral.py` (pair-star representation, C3 orbits, mirror partners, chiral_dirs(qg,qr),
even_orbit_dirs, to_spec, combine, check_symmetry, write_input). Naming S_i by |G|² index (1,3,4,7,9,12,13,16),
T_i by |R|² (1,3,4,7). Directions unit Frobenius = unit mean square.

**Phase 1 submitted (36 req, family w3-chiral-phase, parent w3):** β = ±0.03 along chiral modes
S1-3×T3, S4×T1/T2 (3 each), S5/S6/S8×T1/T2, S1×T4 (3). Files work/p1/*.json, req ids in work/p1_ids.txt.

**Next:** collect slopes (odd part) and curvatures; get swarm-h's B-β slopes; build chiral-β gradient;
line search |β| ≤ 0.15; then CMA-ES on top ~6 modes.

## 2026-10-02 04:41 — wakeup 2: phase 1 back; S4T1c2 live
- Board herded on chiral phase (h, i, j(w2), k, l all on it; i, l, k posted the same M·T rule independently). swarm-h's
  table: s21 artifact floor for MT-odd slopes ≈ 0.18/unit; A-α (orientation amplitude) S1T1 ⟂ orbit and S2T1 ∥ orbit
  slopes ≈ +1.4–1.5 → swarm-h leaderboard s21 ~1.135 (amplitude).
- My phase 1 (tab in work/tab1.md, result post 20261002T044104.989Z_swarm-d_result_a27d): all chiral-β inside
  floor EXCEPT **S4T1c2: slope +1.32, curv −0.006**; req 2400 s21 1.0364, s21c 1.0365, r46 1.0798 → r56 pending.
  Other curvatures −0.02..−0.09, growing with |G|.
- Phase 2a submitted (work/p2_map.tsv): S4T1c2 at g_cutoff 10, β ∈ {±0.03, .06, .10, .15, .20, .30}; S7T1 c0-2 ±0.03 g10.
- Next: if g10 confirms, find the line optimum, then a small CMA/coordinate search in {S4T1c2, S4T2c2, S7T1 best, S1T3c0}
  around the optimum; then w2 transfer (check swarm-j/l for w2 S4 coverage). Check the r56 for 2400.

## 2026-10-02 05:03 — wakeup 3
- Board moved fast: α on joint orbits (S1T1⟂, S2T1∥) + β-chiral (my S4T1c2 = "C7", i's |G|²=13 c0 = "C13") are
  strongly superadditive (o 968b: s21 1.61 / r46 1.71; p cc86 s21 2.40). LL-mixing caveat on S1T1⟂ (b, p, j).
  Amplitude needs M2 controls (a, n). Phase-only is my clean niche.
- S4T1c2 g10 line (p2_map): +0.03 1.0367 (g6 1.0364 → truncation fine), 0.06 s21 1.0539/r46 1.1746, 0.10 s21 1.0344/
  r46 1.2744, 0.15 0.940, 0.20 0.790, 0.30 0.423; −0.03 0.9575. r46 >> s21 response. r56 pending on 0.03/0.06/0.10.
- S7T1 (=|G|²13) c0: −0.03 → 1.0253 (r46 1.0527), same as swarm-i's live mode; c1,c2 dead.
- Submitted p3 (p3_map.tsv): S4T1c2 β=0.07, 0.08; chiral |G|²=19, 21 × T1 (3 modes each, ±0.03, g10) — unique.
- Posted request 20261002T050336.783Z_swarm-d_request_d36a: converge gate min includes s21 (≥1.05) vs brief.
- Next: r56 of e25f/3ea2/2400/7d5d; if r56 ≥ 1.05 → phase-only robust candidate. Then phase-only 2-3D refine
  with any new live modes (G19/G21).

## 2026-10-02 05:27 — wakeup 4
- Human fixed converge gate (r46/r56 only) per my request; r56 now served strongest-first.
- **2400 (S4T1c2 β=0.03 g6): r56 1.0560 PASS → conv46 pending. If ≥1.05 → robust-positive phase-only.**
- S4T1c2 g10 line: s21 peak ~0.065 (1.054); r46 0.07 1.201, 0.08 1.228, 0.10 1.274. r56 pending all.
- New live chiral modes: |G|²=19 c1 (slope −1.22, 38eb at −0.03: s21 1.0276 r46 1.1005), |G|²=21 c2 (+1.51, 9818
  s21 1.0299 r46 1.1324). Matches swarm-i's pre-registered live/dead pattern 6/6 (blind), but size scaling fails.
- Posted result 20261002T052641.481Z_swarm-d_result_9e9d. Handed phase-only CMA to swarm-e (mail); live modes
  (q,c) = (7,2),(13,0),(19,1),(21,2), signs +,−,−,+.
- p4 submitted (p4_map.tsv): G19c1 −0.06/−0.10, G21c2 +0.06/+0.10, P4grad t=.04/.07/.10/.14, P4eq .07.
- Board: big leaders are α(S2T1∥)+β-chiral (p cc86 s21 2.40/r46 2.47). Swarm-i: live modes all have "static via
  parent harmonic" content → LL-mixing-type debate (human request 3942). w2: w3 amplitude plane null.
- Next: r56/conv46 results; if phase-only robust → post claim. Consider next unique lane (not CMA).

## 2026-10-02 05:52 — wakeup 5: CLAIM
- **2400 robust_positive** (phase-only, M2(k)=M2*): s21 1.0364 / s21c 1.0365 / r46 1.0798 / r56 1.0560 / conv46 1.0761,
  all PASS, C=1. Claim post 20261002T054938.487Z_swarm-d_claim_c0eb (with i's static-content caveat; asked for
  an extra cluster).
- Phase-only combos destructive: 4-mode grad t .04 s21 1.021 (r46 1.242), .07 0.867, .10 0.616, .14 0.305;
  eq .07 0.883; C19 −.06 1.013, −.10 0.909; C21 +.06 0.984, +.10 0.790. Phase-only optimum is single-mode C7 ~0.06.
- Withdrew redundant promotions 7d5d, f59d, 7e0b, 0f55 (r56 queue is bottleneck). Kept e25f (0.06), 3ea2 (0.10),
  38eb, 9818, 16f7.
- Board leaders: α S2T1∥ + β-chiral, s21 up to 2.8 (h), strong claims cc86 (p), w3-E (m). Leaders have
  R_beyondM2 ≈ 0.9–1.0 vs parent 0.69 (M2^(k)-law efficiency restored) — possible note later.
- p5 submitted: cc86 + C19/C21 at ±0.03/±0.06 + exact rebuild of cc86 (ed42 should give s21 2.3989).
- Next: p5 results; r56 of e25f/3ea2 (possible strong phase-only).

## 2026-10-02 06:16 — wakeup 6
- cc86 rebuild exact (ed42 → identical hashes, all stages). Conversion code in gen_p5.py is trustworthy.
- cc86 + C19 c1 −0.06 (75e7→resubmitted as 3a86): s21 2.644 / r46 2.849; −0.03 2.528/2.685. cc86 + C21 c2 +0.03
  2.478/2.724, +0.06 2.465/2.908. Wrong signs lose. Phase increments at fixed M2(k).
- MISTAKE: withdrew 7bb7/75e7 (the winners) instead of a156/4c8c; fixed by resubmitting (7201, 3a86) and withdrawing
  a156, 4c8c, 5756, df16. Lesson: grep the map file before withdrawing.
- Critiques from q (margin marginal, non-monotone N) and c (eg 21 → 9.5) answered in note df4e; eg drop explained
  as vortexability loss.
- p6 in flight (p6_map.tsv): cc86 + C19 −0.09/−0.12, C21 +0.09, C19−0.06+C21+0.03/+0.06.
- Next: p6 results; r56 of the cc86+C19/C21 points and of my phase-only line (e25f, 3ea2).

## 2026-10-02 06:39 — wakeup 7
- cc86 + C19 line (s21 / r46): −0.06 2.644/2.849, −0.09 2.719/3.014, −0.12 2.747/3.177; C21 +0.09 2.361/3.063;
  C19−.06+C21+.03 2.638/3.043, +.06 2.525/3.212. s21 saturating near −0.12..−0.15. r46 >> s21 (and f: r46 has
  +4.3% parent-denominator boost; 2400's own gap is size-flat, so its r46 1.080 is mostly the parent dip).
- p7 submitted: C19 −0.15, −0.20, C19−.12+C21+.03 on cc86. Withdrew 7201 (dup).
- Board: p's 8/8 grid STRONG; c's amplitude-only 776c STRONG; p static-free null (genuinely k-dep orbits don't win
  alone); p started w3-sobol over 10 live classes incl. my C19/C21; m done.
- Plan: wait for r56 (bottleneck); then post a final coverage result + decide whether anything unique remains.

## 2026-10-02 07:10 — wakeup 8
- **e25f (phase-only C7 β=0.06, g10): r56 1.1194 PASS → converge.** If conv46 ≥ 1.10 → STRONG phase-only on w3
  (s21 1.054 / r46 1.175 / r56 1.119). Post claim upgrade when it lands.
- cc86 + C19 line: −0.15 s21 2.730 / r46 3.338; −0.20 2.638 / 3.601 (s21 peaks ~−0.12..−0.15). C19−.12+C21+.03
  2.631/3.357. All waiting on r56.
- Board: w2 phase-only STRONG claims by r (e064) and l (9fcb); h d49b strong small amplitude; k fea3+T2 s21 3.47.
- Nothing new submitted; waiting on r56/conv46.

## 2026-10-02 07:43 — wakeup 9: STRONG phase-only
- e25f (C7 β .06): 1.054/1.175/1.119/1.175 STRONG; 3ea2 (β .10): 1.034/1.274/1.200/1.274 STRONG; 38eb (C19) and
  9818 (C21) robust_positive. Own gaps grow with N (s21 < r56 < r46-ish). eg 5–7.5.
- Claim posted 20261002T074141.560Z_swarm-d_claim_61e7 (supersedes c0eb headline).
- Controls (r46,r56 only) on C7 line β .15 (46ee), .20 (68c4): does the phase optimum move with N? Note posted.
- e closed phase-only CMA (single C7 is s21 optimum); o finished (84e4 C7+C13 strong phase-only).
- Next: control results; cc86+C19 r56s; then likely wrap up with final coverage + `swarm done` unless a new idea.

## 2026-10-02 08:03 — wakeup 10
- Controls on C7 line: r46 β .15 → 1.3475, .20 → 1.334 (r46 peak ~0.15–0.17 vs s21 peak 0.065); r56 pending.
  l and r see the same outward shift of the phase optimum with N on w2.
- j: r56 generic even-order bias at 0.03 ≈ 0/−0.4%, so 2400's r56 margin is not bias-inflated.
- Several agents finished (c, f, j, m, o). Plan: when control r56 lands, post final coverage result + swarm done.
- 08:28 wakeup 11: no new results (r56 queue); waiting on 46ee/68c4 r56 and cc86+C19 r56.

## 2026-10-02 09:00 — DONE
- Withdrew superseded cc86+C19/C21 and 16f7 promotions. Final coverage result 20261002T090006.231Z_swarm-d_result_afb8.
- `swarm done` with 92/500 charged. Controls 46ee/68c4 r56 legs still pending (results will land in the store).
