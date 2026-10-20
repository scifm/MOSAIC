# swarm-m notebook

Started 2026-10-02T03:51:55+00:00.

## 2026-10-02 wakeup 1 (04:09–04:20 UTC)
- Read board: a=w3-atlas (S1-S8 x T1-T3 x α/β ±0.02), c=w3-wide CMA-ES (S1-S4 x T1-T2), e/f/b = w2 (b and f run the SAME w2 atlas design: herding), g/h = w3-orient (pair-star joint orbits, cos·cos only).
- Broker looked dead at 04:09 (last tick 419 s ago).
- Key finding (work/alias_map.py): s21 mesh is k_j = j(5,1)/21, so cos(k·R) depends on (5R1+R2) mod 21. Exactly 4 C6 momentum functions on s21: T1, T2, T3, K7 (chiral |R|²=7 orbit through (-3,1)). Everything higher aliases; (-5,4) |R|²=21 orbit is constant (zero mode) on s21. r46: 11 distinct, r56: 15 (through |R|²≤28).
- Posted hypothesis 20261002T041507.895Z_swarm-m_hypothesis_38db (family w3-k7).
- Submitted work/k7_phase1 (34): S1..S8 × K7 × {α,β} × ±0.02 (g_cutoff 6, n_mesh 48) + 2 alias controls (alias_S1_T16_ap must equal a's α[S1,T1]=+0.02 at s21; alias_S1_T21c_ap05 must give R=1).
- Next: read results; compare with a's T1–T3 slopes; phase 2 joint/CMA-ES in {T1,T2,T3,K7} basis if any slope.
- Critique idea pending: b and f duplicating w2 atlas.
- 04:17 all 34 submitted (ids in work/k7_phase1_submit.log). Broker "looks dead"; swarm-o already posted a request about it.
- CORRECTION posted (20261002T041656.161Z_swarm-m_note_466f): mesh-constant orbit (-5,4) is a STATIC density change on s21, not a zero mode. alias_S1_T21c_ap05 (req ee2b) is a static-density control, NOT a candidate.
- swarm-o (pooled-surrogate) has the same aliasing table; recommends staying on T1–T3 for s21 optimizers. K7 is the m=7 function = s21-specific; anything positive on K7 must be read as likely cluster-fitting unless r46/r56 agree.

## wakeup 2 (04:44–04:50 UTC)
- K7 phase 1 done, all 34 PASS: K7 null — |slope| ≤ 0.16/unit, κ −40..−1250 (β outer shells worst). Table work/k7_table.md. Posted result 20261002T044657.171Z_swarm-m_result_7718 (with coverage) + abandon 20261002T044703.543Z_swarm-m_abandon_76de.
- Alias control exact: req_72e2 (|R|²=16) = a's 6972 = g's 3bb4 to 1e-9. ee2b (static S1 tilt via mesh-constant orbit) = 0.925.
- Board: gradient lives on α S1T1⟂ (d=1), α S2T1∥ (d=2), β-chiral S4T1, S7T1. Leaders: o 968b s21 1.609 (R_beyondM2 1.001! parent's is 0.69), h d49b r46 1.120, h 7b23 r46 1.111. PES ent gap of 968b 5.8 vs parent ~21 — watch.
- New family w3-E (hyp 20261002T044831.385Z_swarm-m_hypothesis_5688): Z3 E-irrep (C6-breaking) directions of the 3 joint orbits of S1T1, S2T1. work/build_e.py. 36 submitted (work/e_phase1_submit.log): 24 at parent (α,β), 12 α at 7b23 (saddle test). t=±0.04, g_cutoff 10.
- Budget used: 34 + 36 = 70.
- Next: compute κ_E = (R+ + R- − 2R0)/t²; R0 = 1 (parent) or 7b23 s21 1.1294. If κ_E>0 anywhere → line search + rotated copies.

## wakeup 3 (05:10–05:13 UTC)
- E phase 1 done (36 PASS). Parent κ_E α −17..−28, β −25..−47; at 7b23 inactive orbits soften to −3..−6, active orbits −17..−25 with cubic asymmetry. r46 linear E term +0.10..0.13/unit on active orbits only = 4×6 orientation artifact (Eap points r46 1.118 > base 1.1105). Table work/e1_table.md. Posted result 20261002T051203.349Z_swarm-m_result_3d76.
- Board leaders now huge: p cc86 s21 2.399 / r46 2.470 (α S2T1∥ 0.3175/entry + β-chiral S4T1,S7T1 0.0367, g_cutoff 12), o bd1a 2.27. R_beyondM2 of leaders ≈ 0.95–1.10 vs parent 0.69 (R×2.502/M2k).
- Phase 2 submitted (24, work/e_phase2_submit.log, builder work/build_e_at.py): E α/β ±0.04 around cc86 on S1T1, S2T1 orbits. Saddle test at large deformation. base R0 s21 = 2.3989, r46 2.4695.
- Budget 94/500.
- Next: κ_E at cc86. If >0: line search along E from cc86 at t=0.08,0.16 + other E basis vector (0,1,-1)/√2 to confirm isotropy; check r46/r56 both signs.

## wakeup 4 (05:33–05:40 UTC)
- E phase 2 at cc86 (24 PASS): all 12 E dirs lower s21; κ/R0 −5..−36 (no softening continues). r46 E linear artifact up to +1.6% (bcc86_S2T1_d2_Eap r46 2.5088); bcc86_S1T1_d1_Ea± r46 2.4796/2.4514 but r56 2.4513/2.4517 → r56 shows no linear term. Table work/e2_table.md.
- Posted closing result + coverage 20261002T053402.654Z_swarm-m_result_29f3 (w3-E closed, 60 evals).
- Posted request f159: drop/deprioritize promotions of my E points (they jump strongest-first r56 queue), keep 4 diagnostics (b9b4, 5a1f, 501f, 75ec).
- Board: w3 leaders α S2T1∥ + chiral β S4T1/S7T1 (p cc86 2.40/2.47, o bd1a 2.27/2.63); c: α-only plane closed (ridge min ~1.41); PES fails t≥0.8. h adds S1T2∥ (α<0) to cc86. w2: r 509c 1.137/1.289; g P4⊥ rays; w3 orbits null on w2. qmax 8 truncation 1% at M2k~8 (h).
- Decision: herding + r56 bottleneck → hold budget (94/500 used), act as verifier/critic. Wait for r56 results; check sign agreement and orientation-artifact points.

## wakeup 5 (06:06–06:09 UTC)
- New tools: `swarm withdraw`, `--diagnostic` (first stage only), `--control --clusters`. Withdrew 32 w3-E probe requests; later also b9b4/5a1f (done through conv46). Kept 501f/75ec (S2T1 d2 Ea±; r46 2.4300/2.5088, r56 pending) as orientation diagnostic.
- Diagnostic pair result: 5a1f/b9b4 ±E split 1.1% at r46 & conv46, 0.02% at r56.
- Claims on board: p cc86 STRONG (2.399/2.470/2.456/2.469), o bd1a STRONG (2.271/2.627/2.567/2.628), d 2400 robust_positive (phase-only 1.036/1.080/1.056/1.076). Provisional pending LL-mixing ruling. M2-matched static controls reach only ~1.42.
- Posted verification note 20261002T060755.852Z_swarm-m_note_4e29 (cc86 robust to 24 E perturbations), mailed p.
- Submitted e_phase3 (24, --diagnostic): β E-irrep on S4/S7 (|G|²=7,13) × T1 orbits (both chiral triplets × d) at cc86, ±0.04. Builder work/build_e12.py. Budget 94+24=118.
- Next: κ_E for those; post result; then consider swarm done unless something new (r56 of 501f/75ec; q's 4th cluster).

## wakeup 6 (06:34 UTC) — DONE
- E phase 3 (24 diagnostic): β E-irrep on |G|²=7,13 orbits at cc86 all concave, κ/R0 −16..−44 (work/e3_table.md). Posted result 20261002T063434.866Z_swarm-m_result_7883 with full w3-E coverage (84 evals).
- Ran `swarm done` (summary work/done.md). Budget 118/500. Pending in store: r56 of 501f/75ec.
