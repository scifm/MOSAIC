# swarm-f notebook

Started 2026-10-02T03:51:23+00:00.

## 2026-10-02 04:07 — wakeup 1
- Read docs (46, ADR-0040, 40 pilot, kdep_envelope). Deformation block = separable even×even:
  γ = Σ (α/2 + iβ) O_s(r) F_p(k), cos-stars only. No odd-odd joint (G,R) terms representable.
- Board: swarm-a = w3-atlas (single dirs ±0.02, 96 req); swarm-c = w3-wide (CMA-ES 8D/16D, box |α|≤0.6).
- My family: **w2-atlas** (hypothesis 20261002T040423.778Z_swarm-f_hypothesis_c3ba). Same design as a's w3 atlas.
  Generator work/gen_atlas.py; inputs in work/atlas_w2/{b1,b2,b3} (b1=α×T1,T2; b2=α×T3 + β×T1; b3=β×T2,T3).
- Submitted b1 (32 req, 040457..040636). Next: submit b2, b3 as slots free; fit slopes/curvatures; line search.
- Prior (doc 46): w2 α[S1T1]+0.05 → −5.05%, β[S1T1]+0.05 → −3.01%.
- Note for critiques: Nk=21 aliasing of momentum harmonics beyond |R|²≈4.

## 2026-10-02 04:20 — wakeup 2
- Broker looks dead (last tick ~15 min; swarm-o already posted a request to human). Nothing accepted; my 32 queued.
- HERDING: swarm-b posted an identical w2-atlas 2 min after me; swarm-e does w2-map (±0.03, T1 + αS1-3T2).
  Mailed b: split — I keep α half (S1-8×T1-3, ±0.02; αT1,T2 queued; αT3 = 16 in b2 unsubmitted), b takes β half.
  Mailed e: our steps give 3-point curvature; suggested e skip αS1-3×T2.
  -> HOLD my β inputs (b2 β×T1, b3) until b answers. Do not submit them unless b declines.
- Key board physics: MK symmetry (swarm-l): physical linear terms = α on mirror-even (star×star) modes, β on chiral modes.
  All clusters mirror-free (s21 C6, r46/r56 C2) → β-linear on star×star is finite-size artefact. Expect my α atlas to carry the real slopes.
- Aliasing (swarm-o/m): only T1-T3 clean on s21; |R|²≥9 exact aliases; R=(4,1)-type orbits constant on mesh = static-density loophole.
- Many families on chiral/orbit (d,g,h,i,j,k,l), pooled surrogate (o). My spare role: verification/critique.

## 2026-10-02 04:37 — wakeup 3
- Broker alive (was slow). Split agreed with swarm-b (I α, b β). β inputs moved to work/atlas_w2/held_beta (do NOT submit).
- α T1/T2 atlas results (32 PASS) → work/atlas_w2_alpha_T12.txt; posted note 20261002T043645.875Z_swarm-f_note_02ef.
  T1 slopes: S1 −0.70, S3 +0.89, S4 +0.54, S5 −0.19, S7 −0.94, S8 −1.24; T2 slopes ≈ 0. curv −7..−73.
  Best single: αS3T1+0.02 1.0109; αS7T1−0.02 1.0103; αS8T1−0.02 1.0102.
- Submitted α T3 (16, b2) and line search work/line1 (diag-Newton t=0.25..1.5, gradient r=0.01..0.03; g_cutoff 10).
  Tool: work/gen_combo.py write(parent, {shell: alpha}, path), work/atlas_table.py.
- Leaderboard: w3 best s21 1.041 (swarm-k joint-orbit) at r46; w2 best 1.0186 (l, j chiral).
- Next: read line results; if t-optimum interior, refine 2-D (pairs) / fit Hessian in T1 subspace; ladder promotes ≥1.02 automatically.

## 2026-10-02 04:57 — wakeup 4
- α T3 atlas done (T3 slopes small except S7/S8 ~+0.3, big neg curvature). Full table: run work/atlas_table.py.
- Line search (work/line1) sub-additive: Newton t=0.75 s21 1.0230 → r46 1.0914; t=0.5 s21 1.022/r46 1.0625; grad r=0.03 s21 1.021/r46 1.075.
  r56 pending for all three. (Predicted diag-sum +5%; got +2.3% at s21.) r46 > s21 like w3 leaders.
- BOARD: w3 leaders s21 ~1.5–1.6 (o 968b r46 1.71; c 776c pure S2T1∥ α=0.26 per entry s21 1.52), all via joint A orbits
  S1T1⊥ (R = ẑ×G l_B², cyclotron/LL-mixing half per swarm-b note e1e5) and S2T1∥ (no cyclotron half).
  Verified geometry myself: ẑ×G l_B² for S1 ∈ T1, for S2 ∈ T2.
- NEW family **w2-far** (hyp 20261002T045631.544Z_swarm-f_hypothesis_21b2): polar grid in (u=S1T1⊥, v=S2T1∥) on w2,
  r 0.06/0.13/0.26/0.40 × 8 angles, g_cutoff 12; generator work/gen_far.py write(parent,u,v,path). 32 submitted.
  Mailed g (w2-orient) and c (w3-far).
- w2-atlas still owes a coverage `result` post (α half) once r56 of line points land.

## 2026-10-02 05:18 — wakeup 5
- w2-far: NULL. All 32 < 1 (best 0.9877 r=0.06 th315); 10 FAIL (manifold) at large r. g_u=+0.24, g_v≈0, curv −21/entry².
  Verified my pair-star generator reproduces c's 776c block exactly (so plane is right; parent-dependence is real).
  Posted result 20261002T051602.031Z_swarm-f_result_c59c + abandon. Occupied-shell pattern noted (live α orbit = low shell parent leaves empty).
- Board: w3 leaders R≈2.4 (p ll-free-combo cc86: S2T1∥ α 0.3175/entry + chiral β 0.0367 on S4/S7; M2_k 6.2; R_beyondM2 0.97–1.0;
  ent gap 4.7 vs parent 21). w2 leaders: r's chiral-β phase-only combos s21 1.137.
  Checked solver q-grid: qmax is integer-label hexagon (|Q| up to ~21 l_B⁻¹) → truncation not a concern; conv46 re-checks at qmax 10 anyway.
- Submitted equivalence control 0daa: αS1T1 star +0.02 rewritten as 9 pair entries 0.02/3 → must equal 45e5 (0.9805).
  Validates the star↔pair mapping all pooled surrogates (o, r) rely on.
- Pending: r56 for line pts (newt t050/t075, grad r030). Then post w2-atlas α coverage result.

## 2026-10-02 05:42 — wakeup 6
- Equivalence control 0daa = 0.9805325 vs 45e5 0.9805334 (9e-7 rel). Star↔pair mapping confirmed.
- Posted w2-atlas α-half coverage result 20261002T054116.701Z_swarm-f_result_6ceb (105 PASS, best 580e s21 1.023 / r46 1.091, r56 pending).
- Critique posted 20261002T054001.424Z_swarm-f_note_2c0b + mailed k: w3 #1 13f5 = cc86 + S2T2⊥ orbit (R=ẑ×G l_B², half Q=0) → provisional;
  S2 cyclotron LL1 weight tiny (0.014 vs 0.31 for S1) so a big S2T2⊥ gain argues against b's LL1 mechanism; consistent with i's rule.
- Board state: i's selection rule (f044): live first-order T1 orbits all have k-independent kernel content via parent harmonics
  (a_{G+Gp} = ∓R); explains w2/w3 differences (supersedes my occupied-shell pattern). Human added: --control --clusters, --diagnostic, withdraw; queue strongest-first.
  w3 leaders s21 ~2.6 (13f5, 48bf); w2 leaders g 7f3e s21 1.209/r46 1.368. r56 is bottleneck; no leader r56 yet.
- My families: w2-atlas α (done, coverage posted), w2-far (null, abandoned). Budget used 73/500.
- Next: verifier role — watch r56/conv46 of leaders for sign changes; critique; consider a new family only if an uncovered direction appears.

## 2026-10-02 06:14 — wakeup 7
- Withdrew my 3 w2 line points (31f6, 1e6d, 580e) from r56 queue (weak, ~1.02 s21; relieves bottleneck).
- Claims now: p cc86 STRONG (s21 2.399 / r46 2.470 / r56 2.456 / conv46 2.469; LL-free; M2-matched static 1.42), o bd1a STRONG,
  d 2400 robust_positive phase-only (s21 1.036 / r46 1.080 / r56 1.056 / conv46 1.076).
- Critique posted 20261002T061349.899Z_swarm-f_note_48a8 (mailed q, d): parent Δ r46/s21 = 0.9586 (w3), 0.9592 (w2) → every r46 R
  has +4.3% denominator boost; 2400's own gap is size-flat (4.74/4.73/4.81e-4) so its r46 excess = parent dip; q's 0.04 intercept = this.
  Tool: work/absgap.py REQ... (absolute gaps per cluster).
- k replied: at cc86 only S2T2⊥ is live; pre-registered Q0-free T2 classes add +0.24 (5c77) → i's rule holds.
- Next: continue verifier role; consider swarm done soon if nothing uncovered remains. Budget 73/500 used.

## 2026-10-02 06:47 — wakeup 8
- q accepted 48a8 (refit own-gap law: r46/s21 own − 1 = 4.8·dT, intercept 0). n replied: static controls show R(r46)/R(s21)≈1.00–1.015
  → static bands share the dip; agreed on facts, mailed n the reading (4×6 is outlier for static bands; parent r56/s21 = 0.996).
- New claims: c 776c STRONG (amplitude-only S2T1∥ t=0.45). p static-free null supports i's rule. w3 s21 up to 3.47 (k), w2 1.33 (k, h).
- m done. My remaining distinct options are few; keep verifier role at 1 h cadence, then `swarm done`.

## 2026-10-02 07:50 — wakeup 9: DONE
- Phase-only strong claims own gaps grow 5–7% s21→r46/r56 (84e4, e064, 9fcb, 509c); r56 ratios genuine; included in done summary.
- Ran `swarm done` with final summary (73/500 charged). Loop stopped.
