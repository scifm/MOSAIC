# swarm-n notebook

Started 2026-10-02T03:52:00+00:00.

## 2026-10-02 04:20 — wakeup 1: scope chosen = `contrast-pump`
- Board: a (w3 atlas), b+f (duplicate w2 atlas), e (w2 map), c (w3 CMA S1-S4×T1-T2, |α|≤0.6), d/g/h/i/j/k (orientation/chiral joint orbits — heavy herding). Broker "looks dead" (no tick ~12 min) but not halted.
- My family: parent-aligned amplitude γ=(α/2)c(r)F_T(k), c unit-RMS from parent shells. Rationale: the α² static-like contrast gain (M2 pumping) vs the α² ideality loss; ±0.02 atlases can't see it.
  - w3 `log` profile: S3/S6/S8 weights (0.9247, 0.2812, -0.2566) [projection of log rho_*]; `lin`: (0.9065,0.3777,0.1888). w2 lin: S2/S5/S6 (-0.667,0.667,-0.333).
  - g_cutoff 10, n_mesh 48 (truncation out-of-box weight ≤5e-4 for my batch).
- Found: at g_cutoff 6, S4+/large steps lose 1e-3..1e-1 kernel weight; conv46 rung fixes g_cutoff 6. Posted note 20261002T041732.897Z_swarm-n_note_9624 + human request 20261002T041733.619Z_swarm-n_request_8c47.
- Hypothesis post: 20261002T041712.460Z_swarm-n_hypothesis_294c (~100 evals budget).
- Batch 1: work/b1_w3 (24) + work/b1_w2 (6). Builder: work/build_contrast.py (`parent:profile:T:kind:value`).
- Next: read results; R(α) even/odd shape per T; refine up-bending rays; matched-density control for any amplitude winner.
- 04:18 submitted batch 1: 24 w3 (req_186b..req_86fe) + 6 w2 (req_3bf9..req_a5e2). Map file→req id: `swarm status`.

## 04:38–04:42 — wakeup 2: contrast-pump null; switched role to matched-density controls
- Batch 1 results (s21): w3 log T1 R ≈ 1 − 0.19α − 6.2α² (best 0.957 at α=−0.1); T2/T3 curvature ~14/12; phase β log T1 ~22; |α|=0.4 breaks the manifold. lin profile worse. w2 lin T1 best 0.885.
  → posted result 20261002T043919.176Z_swarm-n_result_5055 (with coverage) + abandon 2dae.
- Human fixed conv46: overrides only tighten (g_cutoff max(req,10), n_mesh ≥64, qmax 10).
- Board leaders: w3 swarm-h c0-orbit (S1T1 G⟂R, S2T1 G∥R) amplitude, s21 up to 1.135 (req_6e88, t=0.11, M2^(k)=3.724). w2 swarm-f ~1.02.
- New role: matched-density static controls (`--control`, s21 only, never ranked).
  - tools: work/matched_control.py REQ OUTDIR (avg density control), work/pow_control_wide.py SRC M2 NSHELLS OUT (rho_*^p, M2-matched; needs 20 shells for w3 positivity — 8-shell rescale goes negative).
  - submitted for 6e88: avg req_5b68 (M2 3.6367), pow req_2741 (M2 3.7237), parent20 sanity req_b36b. Note 20261002T044122.714Z_swarm-n_note_941c; mailed swarm-h.
- Budget used: 33.
- Next: read controls; if avg≈1, pow≈1.02 → 6e88's gain is not static density. Track 6e88 on r46/r56. Offer controls for w2 leaders.

## 04:57–05:00 — wakeup 3: control results; more controls
- 6e88 controls: avg 1.0015 (5b68), pow M2-matched 1.0191 (2741), parent20 1.0000 (b36b). Candidate 1.135 → density ≤1.9 of 13.5 %. Posted result e62b (with critique of swarm-a's "no static can match M2^(k)" — false beyond 8 shells).
- swarm-a opened `m2-control` (avg controls) — overlap. Mailed a proposing split: a = avg controls, me = M2-matched pow + frozen-slice. Built avg20 for 968b/776c in work/ctrl2 (held, not submitted).
- Leaders now: w3 o_968b (s21 1.609, r46 1.710; α S1T1⟂/S2T1∥ + β chiral), c_776c (pure S2T1∥ α, t≈0.26, M2^(k)=5.30, s21 1.518, r46 1.409). w2 r_e064 (phase-only chiral β, 1.077).
- Submitted: pow60_968b req_ce28 (ρ_*^1.115, 60 shells, M2 4.0207); 776c frozen slices Γ (M2 7.815, 40 shells) req_28af, K (M2 4.025, 20 shells) req_a0b2. Pow for 776c impossible (p≈1.51 negative even on 90 shells).
- Tools: work/avg_control_wide.py, work/pow_control_wide.py (hi=4), work/slice_control.py (k0 option).
- LL-mixing critique (b e1e5, p f9b6, j, q): S1T1⟂ orbit has a static coherent-LL-mixing half; S2T1∥ (776c) is free of it.
- Budget: 36 charged.

## 05:15 — wakeup 4
- swarm-a agreed split: a = avg controls (968b req …425b, 776c …a497); me = pow (M2-matched) + frozen-slice.
- Results: 968b pow (ce28) 1.077 vs 1.609; 776c slices Γ 0.610 (M2 7.8), K 0.915 (M2 4.0). Posted e65f (critique of swarm-e's R·M2*/M2(k) ratio); mailed e.
- Human: `--control --clusters r46,r56` now possible (charged per eval; r56 GPU bottleneck). Converge gate now on r46/r56 only.
- New w3 leaders: p cc86 (S2T1∥ α 0.3175/pair + chiral β, M2^(k) 6.20, s21 2.399 r46 2.470), m w3-E ~2.39. w2 r w2-synth 1.137 (phase-only).
- Positivity of rho_*^p: max p≈1.18 on 90 shells (M2 4.235).
- Submitted (s21,r46): pow p1.10 324e, p1.179 9c51, cc86 sliceΓ 1769 (M2 10.1), sliceK 1cfc (M2 4.165); r46 only: 6e88 pow b502, 968b pow 7c54. Files in work/ctrl3.
- Budget ~48 charged.
- Next: compile static R(M2) curve s21/r46; cc86 slices; wait r56 for leaders before r56 controls.

## 05:38 — wakeup 5
- Static curve (pow, w3 pattern): M2 3.724→1.0191, 3.970→1.0673, 4.021→1.0770, 4.235→1.1172 (s21) — r46 identical to 3e-4. R_static ≈ 1+0.193ΔM2. cc86 slices Γ 0.543/0.604, K 0.919/0.994 (s21/r46). Posted 1c34 (yardstick). Mailed p (cc86) and a (avg cc86 is theirs).
- r56 controls queued: p118 edge 7a7d, cc86 K slice ff06.
- NEW family for positivity: mixture (1-s)ρ*+sρ*^2/<ρ*^2>, exact on 40 shells (work/mix_control.py TEMPLATE M2 N NSH OUT). w3 n=2 reaches M2 6.78, w2 n=2 4.28.
- Submitted s21+r46: mix 4.235 ba8e (cross-check), mix 5.30 (776c) 0bbf, mix 6.20 (cc86) e067; w2 7f3e: mix 2.664 5ab2, slice Γ 5f20 (80 sh), K 1f06. Mailed g.
- Human: --diagnostic and `swarm withdraw` exist; r56 2 H100 lanes, priority by R_gap_min. G⟂R claims provisional.
- Budget ≈ 64.

## 06:00 — wakeup 6
- Mixture family (exactly positive): ba8e M2 4.235 → 1.108/1.109 (pow agrees 1.117); 0bbf M2 5.30 → 1.280/1.288 (776c 1.52/1.41); e067 M2 6.20 → 1.4155/1.4312 (cc86 2.399/2.470 → ~30 % density).
- w2 7f3e: mix 5ab2 1.039/1.040; slices Γ 0.972/1.024, K 0.987/1.005 (7f3e 1.209/1.368; α-only twin 98ec 1.102/1.245).
- Posted fde8. Claims on the board: p cc86 STRONG (provisional, cites my 1.42/1.43), o bd1a STRONG (provisional), d req_2400 robust_positive phase-only.
- Submitted s21+r46: mix2 s=1 M2 6.776 385c; n=3 at 6.2032 2678 (family test); n=3 7.5706 (h fea3) ae54; n=3 7.8641 (o b7cb) 53cb; w2 n=2 2.7716 (g e214/61ca) 3624; r56 mix2 6.2032 (cc86) e00d. Pending r56: 7a7d, ff06.
- bd1a not visible to me; mailed o for its M2^(k).
- Budget ≈ 85.

## 06:24 — wakeup 7
- Results: 385c ρ²(s=1) M2 6.776 → 1.498/1.520; 2678 n=3 M2 6.203 → 1.349/1.424 (family dependence ~5% vs n=2 e067); ae54 (fea3 M2 7.571) 1.487/1.545; 53cb (b7cb M2 7.864) 1.515/1.565; w2 3624 (e214 M2 2.77) 1.064/1.065.
- PES eg falls with M2 for static too: 21→15(4.2)→11(6.2,n2)→6(n3)→5.6–5.9 (M2 7.6–7.9). Leaders eg 4.2–5.0. → c's purity critique mostly density.
- Static r46/s21 ≤1.015 (n2) / ≤1.06 (n3) vs fea3/b7cb 1.28–1.30 → f's denominator critique doesn't explain.
- Posted 262d; mailed c, f.
- Pending r56: 7a7d, ff06, e00d. Next: r56 controls for fea3/b7cb once they reach r56 (files work/ctrl5/mix3_w3_7.5706.json, 7.8641).
- Budget ≈ 98.

## 06:50 — wakeup 8 (no new evals)
- r56 controls 7a7d/ff06/e00d still pending: controls get first-stage priority 900000 (broker.py _priority_for) → starve behind promotions. Posted human request 2b0a (inherit builds-on candidate priority).
- bd1a M2^(k) = 5.2995 (same α as 776c) → covered by 0bbf (1.280/1.288) vs bd1a 2.271/2.627/2.567: β lifts at identical density. k 435c/1684 M2 7.5706 = fea3 → ae54. w2 f0fd ≈ 7f3e density → 5ab2.
- Posted coverage note 3e60; mailed c (776c static explains 55–70 %).
- Claims: p cc86 STRONG, o bd1a STRONG, c 776c STRONG, d 2400 robust_positive (phase-only).
- Budget ≈ 101.

## 07:20 — wakeup 9
- Human: controls inherit priority of --builds-on candidate (my e00d/ff06/7a7d all built on cc86 → should run).
- New claims: h d49b STRONG (small S2T1∥ α t=0.11, M2 3.709), r e064 STRONG phase-only (w2), l 9fcb STRONG phase-only (w2), g 98ec/29a2 STRONG (w2 α-only).
- Submitted: d49b mix2 M2 3.7088 s21,r46,r56 → req_2645; g 29a2 mix2 w2 M2 2.5550 s21,r46,r56 → 3a51; r56: 5ab2 input (98ec) 9c49, 0bbf (776c/bd1a) 0a53, ae54 (435c/fea3) dbf4.
- Mistake: req_9a3f submitted with placeholder builds-on → withdrawn.
- Budget ≈ 109.

## 07:48 — wakeup 10
- 2645 (d49b) 1.0148/1.0149; 3a51 (29a2) 1.0134/1.0135; dbf4 r56 (n=3 M2 7.57) 1.518. Posted 2a24.
- k 7966 r56 3.785, 435c r56 3.774 (M2 7.5706) → density ~19 % on r56.
- Human: r56 queue now ranked per parent.
- Caveat for final summary: w2/w3 are paper benchmarks (doc 25, arXiv 2606.07323), not pure-LL0 static optima; "best static at matched M2" is a different (static-search) question, out of brief's scope.
- Pending r56: e00d, ff06, 7a7d, 0a53, 9c49 + r56 legs of 2645, 3a51. When in: post final control table + coverage, then `swarm done`.
- Budget ≈ 113.

## 08:12 — wakeup 11
- r56 controls still pending (e00d, ff06, 7a7d, 0a53, 9c49, 2645-r56, 3a51-r56) after ~2.5h; queue busy.
- /tmp templates vanished → regenerated in work/templates/ (build_contrast.py path updated; pass work/templates/*.json to mix/pow scripts).
- i 618c (static-free, M2 4.8909): control mix n=2 s21,r46,r56 → req_4eaa. Mailed i.
- k claim 3d10 cites my r56 static 1.518.
- Budget ≈ 116.

## 08:40 — wakeup 12
- 4eaa (618c control): 1.2163/1.2205 vs 1.404/1.511; mailed i.
- swarm-a posted avg-density controls for all amplitude claims (20d3): ≤1.047.
- r56 legs still pending (7 of mine) ~3h; per-parent ranking puts cc86/776c/98ec below new leaders. Waiting.
- 09:30 r56 legs still pending; posted human request (claim-level priority). Charged budget per digest: 83.
- 10:05 human moved my r56 legs to priority 1 (221a820); still pending. Waiting.
- 10:36 r56 legs stuck SUBMITTED (no updates since queued); posted human request. Submitted 9ad3 control 24bb (n=3, M2 6.8879, s21,r46,r56). Mailed h.
- 11:05 human fixed stale GPU pass (15a35aa); r56 legs done: 7a7d 1.1174, ff06 0.9449, e00d 1.4238, 2645 1.0149, 3a51 1.0134, 9c49 1.0394, 0a53 1.2845. 24bb (9ad3) 1.4209/1.4924. Pending r56: 4eaa, 24bb. Final table drafted (density share per candidate). Next: post final result + coverage, swarm done.

## 11:24 — final
- 24bb (9ad3) r56 1.4663 vs 9ad3 r56 4.375. Posted FINAL control table 0138 (+ coverage fix 2d87: 34 control requests / 57 legs).
- 4eaa r56 still pending (618c unclaimed, low priority) — left as pending in the table.
- swarm done. Charged 86/500.
