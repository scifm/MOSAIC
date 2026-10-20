# swarm-p notebook

Started 2026-10-15T04:13:44+00:00.

## Wakeup 1 — 2026-10-15 ~04:30–04:40 UTC
- Board: atlases (a: w3, c: w2), joint classes (b), bigamp (e), fs floor (f), chiral phase (g), phase by mirror parity (h),
  matched ⟂ classes (i: w3+w2, j: w3 S1⊥ line + β). Lead: swarm-b f06f (S1×T1 G⟂R class, α=0.05): s21 1.105, r46 1.088, r56 1.092 PASS → converge stage.
  w2 lead: swarm-c 5515 separable α[S1,T1]=−0.1 (r46 1.080, r56 1.041, s21 1.026).
- Herding on ⟂ (b, i, j). I chose role **mech-control**: matched-density static controls for α≠0 candidates (claim 2).
  - Definition: static W_G = Fourier of ⟨ρ_* e^{2Reγ_k}/⟨·⟩_uc⟩_BZ (24² k grid, n_mesh 96), truncated to 8 solver shells.
    Script work/matched_control.py (input ed_input.json path from `swarm show`). uc vs 1/S00 weighting agree to 5 digits.
  - f06f control ≈ parent: (0.60044,0.25036,0.12543), M2 3.6336 (parent 3.6288; M2^(k) 3.6863). Expect control R≈1.00.
  - M2-matched control (ρ_*^p, p=1.017) is inadmissible for w3 (min |h|² −0.0099) — w3 nearly touches zero. Dropped.
- Submitted control req 20261015T043501.810Z_swarm-p_req_4657 (--control --clusters s21,r46,r56).
- Posted hypothesis 20261015T043458.028Z_swarm-p_hypothesis_2ed2, note 20261015T043608.647Z_swarm-p_note_0064
  (guiding-centre bookkeeping: chart term (G,R) ↔ cyclotron e^{∓iG_R·η} × static harmonic G' = G ± G_R; matched ⟂ → {0, 2G};
  2G of S1/S2/S3 all on w3 shells; on w2 only S2's. Prediction: on w2, S2⊥ strongest matched class). Mailed swarm-b.
- work/classes.py enumerates all 126 joint pair-classes with partner shells |G±G_R|².
- Insight: cyclotron vector is set by R alone (G_R ∈ S1/S2/S3); e^{-|q|²ℓ²/4}: T1 0.16, T2 ~0.004, T3 ~7e-4 → T1 dominates LL-mixing channel.
- Next: read control result; watch swarm-j S1⊥ β (phase-only ⟂ curvature — if positive, phase-only ⟂ at large β is a clean beyond-M2 route);
  watch swarm-i w2 matched classes vs my prediction; then pick a search family (candidates: phase-only ⟂ large β; w2 matched large-α).

## Wakeup 2 — 2026-10-15 ~05:00–05:20 UTC
- Control req_4657: R=1.0010 on s21/r46/r56 (same as m, l). 8 agents ran controls → role saturated; closed mech-control
  with result 20261015T051749.962Z_swarm-p_result_38a3. My w2 S2⊥ prediction falsified (k, i).
- Tools built: work/harvest.py (swarm show → work/cache/*.json, ~1 s/request, incremental), work/canon.py
  (canonical pair coefficients C(G,R) = (α/2+iβ)/√(|s||p|); joint C6 class features), work/build.py (compose/emit pair-star
  blocks; α=4ReC, β=2ImC; verified γ reproduction 1e-16), work/near.py (list points near S1⊥ base).
- Critique posted 20261015T051237.236Z_swarm-p_refutation_6e01: e's 813f/18be are mirror images (TL-identical), r56 1.342 vs 1.260
  → r56 orientation artefact 6.5%; 813f's min>7d04 is alignment. Mailed e.
- Board: w3 S1⊥ α=0.2 (7d04) local max in ⟂/nematic/chiral-l2 spaces; h chiral β (S7/S13 × T1 orbits) adds ~+4% (0672 s21 1.427 r46 1.461);
  r's S2∥T1 class (G=(1,-1),R=(1,-1); partners [4,4], my table) alone: C=0.05 s21 1.4516 r46 1.4125; C=0.075 s21 1.5047 r46 1.364.
  w2: c's g4perp 1.16 s21 / 1.21 r46; g's oblique strong (88e5 min 1.1136).
- New family w3-xcombo (hyp 20261015T051715.611Z_swarm-p_hypothesis_d062): X1 = S2∥(C .05) + h chiral β, 6 evals:
  f291 (s13m) ddad (s13p) 51c7 (s7m = 0672 sign) f356 (s7m+s13p ×2/3) 8a2c (s7p) fe3d (S2∥ .0625 + s7m). Mailed r, h.
- Next: read X1; if additive, line in chiral β amplitude on S2∥ base and add S1⊥ small; watch r56 of S2∥ points.

## Wakeup 3 — 2026-10-15 ~05:39–05:50 UTC
- X1 results: fe3d (S2∥ C .0625 + S7 chiral β, h's sign) STRONG: s21 1.6946 r46 1.6870 r56 1.6879 conv46 1.6864 (0.5% spread!).
  51c7 1.595/1.633; f356 1.597/1.648/1.616; ddad 1.557/1.578; wrong chirality 8a2c 1.269/1.227, f291 1.331/1.288.
  Posted claim 20261015T054023.883Z_swarm-p_claim_98b3. Control (ρ̄ trunc negative → uniform mix δ=0.041, M2 3.58 weak) req e7ac.
- b built on fe3d: resonant-class-only chiral β (|G|²=7 class (1,-2)x(0,1), partners [4,12]) on S2∥ .25: C=.04i → 02f7 s21 2.38 r46 2.585.
  Line still rising (0.01 1.73, 0.02 2.03, 0.03 2.27, 0.04 2.38). b, j (chistack), a (stack CMA) all on that — herded.
- n: static sharpening frontier peaks ~1.56 (s21); fe3d beats all statics.
- New family w2-chiclass (hyp 20261015T054816.034Z_swarm-p_hypothesis_ed04): class-resolved chiral β on w2 df59,
  C=±0.02i on single T1 class + mirror; work/chiral_classes.py (mirror M(m,n)=(m-n,-n), partner table). 14 reqs in W1/
  (ec1a e4ae 9195 34d8 8a0d 3fe8 906e fcf0 c1fb 2aa6 bce8 079a dfaf 4f47). Mailed c (full-orbit P1 owner).
- Tools: work/top.py PAR THR N (top compositions), work/build.py from_req/combine/select/write.
- Next: read W1; line search best w2 class; check 02f7 r56/convergence (q queued cbd0); consider critique on g_cutoff for large β.

## Wakeup 4 — 2026-10-15 ~06:05–06:12 UTC
- X1 all ladder-complete: ddad min 1.5517 STRONG, 51c7 1.5951 STRONG, f356 1.5972 STRONG, fe3d 1.6864 STRONG. e7ac ctrl 0.979 (weak;
  c's critique: 8-shell truncation artefact; c's 16-shell ρ̄ control req 3ecc supersedes mine).
- W1 (w2 df59 + class-resolved chiral β C=0.02): shell-9-hitting classes win with m sign: 13[9,19] 8a0d s21 1.228 r46 1.408 (w2 leader);
  7[7,9] dfaf 1.064/1.352; 7[4,12] bce8 1.048/1.124; rest lose; non-resonant 13[7,21] concave (0.54/0.77).
  Result posted 20261015T061018.909Z_swarm-p_result_ce29. Told c/l (w2 phase-only at parent) to expect [9,19],[7,9] to dominate.
- W2 submitted (8): 13[9,19] m C .01/.03/.04 (8eb3 b925 47e4); 7[7,9] m .01/.03 (85d5 60c8); stacks (13,7)=(.01,.01) 1a80,
  (.02,.01) cf93, (.02,.02) 8ecf.
- w3 now: a's stack CMA s21 3.60 (cc13, many classes incl |G|²=21, g_cutoff 9) — others verifying (n, q, f, o). b 02f7 r56 2.53.
- o: r56<r46 in 43/45; r46 over s21 by 4–15% for leaders.

## Wakeup 5 — 2026-10-15 ~06:28 UTC
- 8a0d STRONG: s21 1.2278 r46 1.4084 r56 1.3805 conv46 1.4109 (w2). 8eb3 (13[9,19] C .01): 1.255/1.356/1.339 min 1.255, conv46 pending.
- C ≥ .03 on 13[9,19] FAILs (manifold). 7[7,9]: .01 85d5 1.197/1.337; .03 0.82. Stacks: 1a80 1.171/1.413, cf93 1.058/1.445, 8ecf .774.
  Pattern: more β → s21 down, r46 up; min binds at s21.
- W3 fine line submitted: 13[9,19] C .005 c828, .0075 2b53, .0125 c02a, .015 bcd9; stack(.0075,.005) 2a47.
- e takes w2 joint α+β CMA (w2-chistack) seeded near 8a0d; mailed seeding advice (8eb3, b≤.01 σ). I won't run joint optimizer on w2.
- w3 frontier ~4 (s21)/4.8 (r46) via a's stack, r's kshape. n: w2 static sharpening hits 1.59 s21 at M2 6.5 (> any w2 k-GLL) — caveat.
- Next: when W3 lands, post claim for best w2-chiclass point (8eb3 or better), close family with coverage; then consider done or a verifier role.

## Wakeup 6 — 2026-10-15 ~06:53 UTC
- W3 line 13[9,19] on df59 (s21/r46/r56): .005 1.221/1.281; .0075 1.241/1.319; .01 8eb3 1.255/1.356/1.339 conv 1.357;
  .0125 c02a 1.262/1.383/1.362; .015 bcd9 1.261/1.401/1.377; .02 8a0d 1.228/1.408/1.381. s21 optimum C≈.0125–.015.
  stack(.0075 13, .005 7) 2a47 1.235/1.382. 85d5 (7[7,9] .01) conv done min 1.197.
- e restarted w2 CMA at 8eb3 with σ0 .008 (my advice). c: w2 caps ~+20% (few double-resonant classes). Many agents finishing early (d,g,i,m).
- Plan: wait for c02a/bcd9 conv46 → claim best, close w2-chiclass with coverage, then swarm done (all directions owned).

## Wakeup 7 — 2026-10-15 ~07:10 UTC — DONE
- c02a ladder complete: s21 1.2618 r46 1.3828 r56 1.3621 conv46 1.3838 STRONG → claim 20261015T070932.237Z_swarm-p_claim_1e95.
- Closed w2-chiclass (result 20261015T071006.645Z_swarm-p_result_71a6) and w3-xcombo (20261015T071007.473Z_swarm-p_result_0b72) with coverage.
- swarm done posted. 39/500 evals charged. Stopping loop.
