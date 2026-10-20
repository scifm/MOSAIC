# swarm-p notebook

Started 2026-10-02T03:52:09+00:00.

## Wakeup 1 — 2026-10-02 ~04:12–04:22 UTC
- Read the board: a (w3 atlas), b/e/f (w2 atlas, triplicated), c (w3 CMA-ES on S1-S4×T1-T2),
  and d/g/h/i/j/k (chiral/joint-orbit phase modes, heavily herded). Broker showed "looks dead"
  (last tick 604 s) at first digest; requests queue anyway.
- Chose an unclaimed family, **m2-breathe**: multi-shell amplitude rays along the directions where
  ⟨M2^(k)⟩_BZ grows fastest (X_M2 = top eigvec of the analytic Hessian H) or fastest relative to a
  heuristic ideality cost (X_eff, generalized eigvec vs Cov_rho), × T1. Code: work/breathe.py,
  work/gen.py, work/gen_p1.py; directions saved in work/dirs_p1.json.
  Predicted ⟨M2^(k)⟩ gains: w3 X_M2 +9 % at α=0.1; w2 much smaller (+2 %).
- Hypothesis post 20261002T041948.865Z_swarm-p_hypothesis_4319. Budget ~60.
- Submitted phase 1: 20 requests (10 per parent), ids ...req_5dc9 … req_de10 (see swarm status).
- Finding (critique note 20261002T042053.339Z_swarm-p_note_c157): momentum harmonics alias on the
  ladder meshes. s21: T5,T6 ≡ T2 on mesh; T4 half T3. 4×6: T3 mesh norm² = 4/3. Only T1, T2
  clean on all clusters. Mailed a, d, i. Script work/alias.py.
- Next: when phase 1 lands, compare R_gap with broker's M2^(k) along each ray; decide phase 2.
  Also do a critique of another agent's result once results exist (rule 11).

## Wakeup 2 — 2026-10-02 ~04:47–04:57 UTC
- Phase 1 m2-breathe landed: clean null (best 1.0108 w2 4e01; w3 ≤ 0.95; M2^(k) up 8–86 % while
  R_gap falls). Posted result 20261002T044817.664Z_swarm-p_result_95c0 + abandon (coverage block in result).
  Lesson: outer-shell (S4/S5/S7) amplitude curvature ≈ −52/unit², ~3.5× S1; ρ-weighted ideality
  heuristic useless as curvature model.
- Board: w3 leaders are amplitude on S1T1⊥ / S2T1∥ orbits (h, k, g) and o's α+β-chiral combo
  968b (s21 1.609, r46 1.710). c's pure S2T1∥ far-field 776c: s21 1.52.
- Dumped board via work/board.py (copy of swarm-o's, read-only swarm.agent API) → work/board.json.
  R_beyondM2 ≡ η = Δ/(M2^(k)Δ_LLL); η* = 0.69 (w3), 0.71 (w2); 968b has η = 1.001 (only one point; no ceiling claim).
- Derived and posted the per-term LL-mixing criterion (note 20261002T045438.980Z_swarm-p_note_f9b6):
  e^{iG·r}e^{ik·R} → e^{iG·η} × k-harmonic Q = a_G + R, a_G = l_B² ẑ×G. Q = 0 ⇔ static coherent LL
  mixing (closed under exp). S1T1⊥ is exactly half Q=0; S2T1∥ and chiral-β S4T1/S7T1 are Q≠0.
  968b is 19 % LL-mix by weight. Scripts work/qclass.py, work/qboard.py. Mailed b, c, o, h.
- New family **ll-free-combo** (hyp 20261002T045620.703Z_swarm-p_hypothesis_a6c2): ablations of 968b
  (noperp 7341, nopar 89d7, perp2par f13c) + grid α S2T1∥ t∈{.22,.35,.45,.55} × β m·(2C7+2C13),
  m∈{1,1.5}. g_cutoff 12. Builder work/combo.py, work/gen_p2.py. 11 requests submitted.
- Budget used: 20 (+11 pending).
- Next: read p2 results; refine; w2 transfer (S2T1∥ ± and i ffbc β); watch r46/r56 of LL-free points.

## Wakeup 3 — 2026-10-02 ~05:17–05:20 UTC
- p2 landed, all PASS s21/s21c/r46 (C=+1): cc86 (t∥=0.55, m=1.5) s21 2.399 / r46 2.470 = w3 #1.
  Grid and ablations in result 20261002T051857.140Z_swarm-p_result_8b6e. β increment at fixed M2^(k)
  vs c's α-only ray (67ed/776c/cd5a): ×1.39–1.62 (s21), ×1.58–1.85 (r46). Ablations: the ⊥ (LL-mix) half not needed.
- o's batch 3 brackets my box edge (t .45/.55/.70 × β to 6P) — not duplicating. m does E-sector saddle
  probes at cc86 (s21 ~2.33–2.39). h does gradient probes at 776c.
- Asked n and a (mail) for matched-density static controls on cc86 (s21/r46/r56).
- Budget 31/500.
- Next: r56 of cc86/e591/10ec; if PASS and ≥1.05, conv46 runs automatically. Consider w2 analogue
  only if someone hasn't (r covers w2 α×β). Do a critique post (rule 11) — candidates: i's selection
  rule note f044, e's rho note 3494.

## Wakeup 4 — 2026-10-02 ~05:45–05:50 UTC
- cc86 reached STRONG: s21 2.399 / r46 2.470 / r56 2.456 / conv46 2.469, all PASS. e591, 948f, 1a7b STRONG too.
  10ec suggestive → converge pending.
- Controls on cc86: a avg-density 1.046 (s21, 065a) / 1.047 (r46, e85e); n M2-matched static (M2 6.20)
  1.415/1.431 (e067); frozen slices Γ 0.54/0.60, K 0.92/0.99. e: β of cc86 alone = 0.885 (α×β interplay).
- i's rule (f044): first-order slopes need Q_tot = a_{G+Gp} + R = 0 via parent harmonics → S2T1∥ and
  chiral β carry static LL-mixing-type content. Accepted at first order. Human: G⟂R claims provisional.
- Posted CLAIM 20261002T054702.331Z_swarm-p_claim_cd9d (provisional; full caveats).
- New family static-free (hyp 20261002T054905.820Z_swarm-p_hypothesis_9ed1): 12 req (2bd5…387e),
  cc86 analogue from first-order static-free orbits (S2T1 ±60, S1T1 ±30, dead chiral classes |G|²=7,13).
  Builder work/orbits.py, work/gen_p3.py. Prediction (i's rule): all < 1.
- Budget ~43/500.
- Next: static-free results → result + coverage; ll-free-combo coverage block once r56 for grid lands.

## Wakeup 5 — 2026-10-02 ~06:15–06:22 UTC
- static-free (12) null: best 0.746 (2bd5); β anti-synergistic; manifold breaks t≥0.35. Posted result
  c8c4 (coverage) + abandon 8b12. i runs a CMA-ES static-free family (fb7e) — overlap acknowledged.
- ll-free-combo final: 8/8 grid STRONG; posted result 8c50 (coverage, eg table, cluster trend:
  r56/r46 ∈ [0.96, 1.02] across all 42 w3 r56-PASS points). Withdrew ablations 89d7, 7341, f13c from ladder.
- Board: k's Q0-free T2 β add +0.2 on cc86; h's S1T2∥ −0.05 add-on (fea3 s21 2.80/r46 3.59); m verified
  cc86 stable vs 24 C6-breaking perturbations; b has w2 at s21 2.10 (|a| 0.78).
- New family w3-sobol (hyp 884a): 32 scrambled-Sobol points (seed 20261002) over 10 live orbit dims,
  builder work/gen_sobol.py, points in work/sobol/points.json (index ↔ sobNN.json). Plan: fit quadratic + cross terms,
  maybe +32 more.
- Budget ~55 + 32 = 87/500.

## Wakeup 6 — 2026-10-02 ~06:49–06:52 UTC
- Sobol b1 (32): #6 df8f s21 2.740 / r46 3.458 PASS (α49 +.099, α16 +.096, βS4T2 −.079, βC21 −.108);
  #19 0d4c 2.385/2.952. 8 FAIL, 20/32 > 1. Crude linear log-R fit (R² 0.62): βS4T2 − strongest; α49, βC7, βC19 +.
  Results: work/sobol/results.json (work/collect_sobol.py). Posted result 7f73.
- Local search around #6: 11 req (work/gen_local6.py → work/local6/), ids d96b 968a 8dea b623 327d 58a8 0752 61dd 8bc7 9fc9 26ee.
- Board: m done (summary c589); c claims 776c STRONG; k: T2 combos on cc86 subadditive; o: β-chiral gain sign-locked to α∥.
- Budget 75 + 11 = 86/500.
- Next: local6 results → refine, r56 of df8f.

## Wakeup 7 — 2026-10-02 ~07:18–07:21 UTC
- local6: gradient step 0.35 from #6 → 9fc9 s21 3.514 (board top s21); par55 26ee 3.097; S4T2→−.10 327d 3.032;
  other pushes worse (α49, α16, C7, C21→0, S1T2 −.10 all lower). Note 91ac.
- Withdrew 23 non-candidate Sobol/push points from ladder (kept df8f 0d4c 3086 4f15 9fc9 8bc7 61dd 26ee 327d).
- local9 (8 req; work/gen_local9.py → work/local9/): g0.50 f9e2, g0.70 b082, from 9fc9: par60 60a3,
  S4T2m16 a74c, par60+S4T2m16 8967, C21m15 38c1, S1T2p08 77ab, a16p06 507a.
- Board: claims r (w2 e064 phase-only STRONG), l (w2 9fcb), g (w2 98ec), h (w3 d49b small); c and m done.
  i: static-free CMA point f8d6 s21 1.076/r46 1.187 (contradicts expected null; cc86 local max vs static-free dirs).
- Budget ~94/500.

## Wakeup 8 — 2026-10-02 ~07:46 UTC
- 9fc9: s21 3.514 / r46 3.484 / r56 3.481 PASS (conv46 pending), r46 sp/D 0.087 (gate 0.1), M2(k) ×2.93, eg 3.5–4.
  8bc7: 3.136/3.500/3.480 (conv pending). local9: steps beyond 9fc9 FAIL r46 manifold (f9e2, b082, a74c, 507a);
  60a3 (par .60) 3.42/3.59 sp/D .038 (r56 pending); 77ab 3.44/3.44; 38c1 3.29/3.96; 8967 3.30/3.39.
- Posted note on manifold-gate ridge. Push stopped. Owe h the conv46−r46 shift for 9fc9/8bc7.
- Next: when conv46 lands for 9fc9/8bc7 → claim (provisional) with caveats; check 60a3 r56.

## Wakeup 9 — 2026-10-02 ~08:15 UTC
- conv46: 9fc9 3.388 (sp/D 0.094), 8bc7 3.418 (sp/D 0.070); both broker STRONG. Claim afbb (provisional),
  mailed h the conv46−r46 shifts (−2.8/−2.3 %). w3-sobol final coverage 6f84 (+ count corrections dc8d, 4df6:
  first stage 43/0/8, 5 r46 manifold FAILs).
- All my families closed with coverage: m2-breathe (95c0), ll-free-combo (8c50), static-free (c8c4), w3-sobol (6f84).
  Claims: cd9d (cc86), afbb (9fc9, 8bc7).
- Many agents done (c, f, j, m, o). Budget 94/500.
- Plan: one more watch cycle (critiques of my claims, human ruling, r56 of 60a3), then swarm done.

## Wakeup 10 — 2026-10-02 ~08:47 UTC — DONE
- k critique a439 of afbb accepted (note be77): 9fc9 marginal at the gate; 8bc7 defensible; "ridge at gate" box-specific
  (k feba 4.12/4.56 at split 0.010). Withdrew 9 unclaimed ridge points from r56.
- swarm done posted (summary in work/done.md). 94/500 charged.
