# swarm-g notebook

Started 2026-10-02T03:51:28+00:00.

## 2026-10-02 04:10 — wakeup 1: chose family `w3-orient`
- Board at start: swarm-a w3-atlas (U-mode star×star single directions ±0.02, 96 req), swarm-c w3-wide (CMA-ES star×star S1-S4×T1-T2), swarm-e w2-map.
- My niche: orientation-resolved (G,R) couplings via inversion pair-stars ({G,-G},{R,-R}) + full J×P alpha/beta matrix.
  C6 joint orbits (cos·cos part). Modes per block: U (=star×star, verified γ identical 1e-17), X (achiral contrast), C (chiral).
  Normalization: Frobenius norm of pair matrix == star coefficient.
- NAMING in my files: S{|G|²}T{|R|²}. So my S3 = swarm-a S2, my S4 = swarm-a S3, my T3 = swarm-a T2. Basis: G metric m²+n²−mn, R metric m²+n²+mn.
- Scripts: work/orient.py (generator), work/gen_p1.py (phase 1), work/relabel_check.py.
- Submitted phase 1: 33 requests (S1T1,S3T1,S4T1,S1T3 × X,C × α,β × ±0.04, + U α S1T1 +0.02 relabel control vs swarm-a). g_cutoff 6, n_mesh 48.
- Hypothesis post 20261002T040810.113Z_swarm-g_hypothesis_0dfa. Mailed swarm-c re representability.
- Next: read results; fit slopes; phase 2 = combine best X/C with U α[S1,T1]≈+0.04, then CMA in orientation subspace.

## 2026-10-02 04:27 — wakeup 2: herding; pivot planned
- swarm-h posted identical w3-orient (pair-star U/A/B, ±0.03, S1-S3×T1-T2) 30 s before me; swarm-k joint-orbit (A/P/M, ±0.02); d/i/l/j chiral-β variants.
- Symmetry (i, l): MT/MK → α-C even (no linear), β-C linear allowed; β-U, β-X odd. No ladder cluster has a mirror (s21 C6 chiral; r46/r56 C2).
- s21 momentum aliasing (p, r, o): only T1, T2(|R|²=3) clean everywhere; T3 self-aliases on r46.
- Human: conv46 now uses g_cutoff max(request,10). Broker was slow, fixed.
- Decision: let phase 1 run (33 req; ±0.04 complements h/k steps); no phase 2 in w3 orientation space.
  Posted note 20261002T042701.509Z_swarm-g_note_c42b; mailed h, i.
- NEXT: post phase-1 table (+ MT test, relabel control vs swarm-a). Then hypothesis `w2-orient`: α-X modes on w2
  S1,S3,S4 × T1,T3 ±0.03 (~12) then line search combined with w2 best U from e/b/f. Check w2 admissibility.

## 2026-10-02 04:55 — wakeup 3: phase 1 done; w2-orient submitted
- Phase-1 result posted 20261002T044909.158Z_swarm-g_result_e19a (coverage block incl.). α-X S1T1 slope +1.50 curv −28; α-X S3T1 +1.36/−23;
  all others (S4T1, S1T3 X; all C; all β) inside floor & concave. e549 (S1T1 α-X +.04): s21 1.0371, r46 1.0317; 2fb3 (S3T1 α-X +.04): r46 1.0326; r56 pending.
- Low-shell chiral β slopes ≤0.07: no evidence of MT-allowed linear term on S1–S4 (live chiral β is on 12-member shells: d |G|²=7, i |G|²=13, l).
- BOARD LEADER: o req_968b = h's α(S1T1⊥+S2T1∥) + chiral β (d S4T1, i S7T1), g_cut 10: s21 1.609, r46 1.710 PASS C=1, PES ent gap ~6.
  c w3-far polar grid gives s21 up to 1.52. 1-D quadratic vertices (~1.04) badly underestimate far-field → response not quadratic.
- My truncation check (work/trunc.py, n_mesh 128): 968b & 776c weight beyond their g_cutoff ≤1e-6. Not an issue.
- Submitted w2-orient phase A: 10 req α-X ±0.03 on (1,1),(3,1),(4,1),(1,3),(3,3) — ids in work/w2x_ids.txt.
- NEXT: w2 analogue of o's winner: w2 best α (X orbits + f's star slopes: S3,S4 up; S1,S7,S8 down on T1) + l's w2 chiral β (C4T1 +3.7, C7T1 +3.3). Coordinate with e, r, l.

## 2026-10-02 05:08 — wakeup 4: w2 α-X results; phase B rays
- w2 α-X (±0.03): S1T1 +0.71/−29; |G|²=3 +0.03; |G|²=4 +1.23/−43; S1T3 0; (3,3) +0.12. With f's U slopes →
  orbit slopes: |G|²=4×T1 ⊥ +1.32 (LIVE, LL-free), S1T1 ±30° pair −0.98 (live on − side, LL-free), S1T1⊥ +0.17, S2T1∥ dead.
  Posted 20261002T050726.311Z_swarm-g_result_b3f8.
- Board: LL-mixing critique (b, p, q, j): S1T1⊥ orbit (R = ẑ×G l_B²) has a static coherent LL-mixing half; p: Q=a_G+R criterion.
  o: α × chiral-β superadditive on w3 (968b r46 1.71). n: matched density explains ≤1.9% of h 6e88's 13.5%.
  Human: converge gate now thresholds on r46/r56 only; --control --clusters available.
- w2 coverage by others: f w2-far (S1T1⊥, S2T1∥ plane), r w2-synth (chiral β combos), j w2 chiral, l chiral, e w3-orbit transfer to w2.
- Submitted phase B (13, g_cutoff 10): B1 P4⊥ t=.05–.30, B2 −P1pair t=.05–.30, B3 combo t=.1,.2,.3. ids work/w2B_ids.txt. Mailed f the split.
- NEXT: read rays; if a far-field peak, combine with w2 chiral β (j S3×T1 +1.60; l C4T1/C7T1) as o did on w3. Budget used 43+13=56.

## 2026-10-02 05:25 — wakeup 5: w2 rays live; phase C (α × chiral β)
- Phase B (w2, g_cut 10, all PASS):
  P4⊥ t=.05..0.30: s21 1.040/1.062/1.058/1.029/0.896; r46 1.078/1.159/1.197/1.220/—
  −P1pair t=.05..0.30: s21 1.038/1.070/1.094/1.108/1.107; r46 1.038/1.073/1.105/1.131/1.148   ← s21-robust
  combo(0.80 P4⊥, −0.60 P1pair) t=.1/.2/.3: s21 1.092/1.102/1.049; r46 1.168/1.245/1.234
  All promoted to r56 (pending; r56 is the bottleneck: 2 GPU lanes).
- Board: w3 leaders now LL-free S2T1∥ α + chiral β: p cc86 s21 2.40 / r46 2.47; o bd1a 2.27/2.63. w2: r's phase-only chiral β e064 1.077/1.205.
  f: w3 plane null on w2 (confirms my result). r batch 2 uses my P4⊥ α with its β (r keeps P4⊥-alone base).
- Phase C submitted (8, ids work/w2C_ids.txt): C1 −P1pair t.40; C2 tilt(0.40 P4,0.92 pair) t.2,.3; C3 −P1pair t.2 + e064×1,×2;
  C4 combo t.2 + e064×1,×2; C5 e064×2 alone (β reference). Mailed r the split.
- NEXT: β increments at fixed M2; r56 values; amplitude winner → matched-density control (ask n/a or --control myself);
  post phase B/C result with coverage. Budget used 56+8=64.

## 2026-10-02 05:47 — wakeup 6: w2 leader 7f3e; phase D refinement
- Phase C: C4 combo20+e064×1 (7f3e) s21 1.209 / r46 1.368 = w2 #1 (n running controls). C2 tilt(23.5°) t.3 α-only 1.165/1.206 (s21-robust).
  β×2 alone (badb) 0.996 but +6.6% on combo base → α×β interplay (matches e's w3 finding).
- Posted 20261002T054635.699Z_swarm-g_result_7348. Mailed n: α-only twin of 7f3e is 98ec.
- Board: o bd1a r56 2.567 (w3 first r56 PASS >2.5). m: no C6-breaking instability. h: qmax 8 truncation ~1% at M2(k)~8.
  b: w2 outer orbits live S4T1-10.9° (a's S4=|G|²=7) +3.29/entry. Human: queue strongest-first; withdraw tool; controls on named clusters.
- Phase D submitted (8, work/w2D_ids.txt): θ∈{23.5,38,53.4}, t∈[.15,.30], b∈[.5,1.5]. Generators importable (gen_w2C.alpha_input).
- NEXT: fit (θ,t,b) quadratic; maybe add b's |G|²=7 10.9° orbit; wait for r56 of 7f3e/98ec/C2. Budget 72/500.

## 2026-10-02 06:09 — wakeup 7: phase D done, box widened (phase E)
- Phase D: best D_th23_t30_b10 s21 1.248 / r46 1.349 (on t=0.30 wall); D_th23_t30_b15 1.241/1.401; D_th38_t25 1.233/1.368. All PASS.
  PES ent gaps of leaders ~3–4 (parent ~20).
- n: 7f3e M2-matched static = 1.039 (vs 1.21/1.37) → beyond density.
- Board: claims — p cc86 STRONG (provisional, LL-mixing ruling), o bd1a STRONG (prov.), d 2400 robust_positive phase-only (q: marginal).
- Withdrew 20 redundant r56 promotions (kept B2 t20, 98ec, C2 t30, 7f3e, D th23 t25/t30b10/t30b15, D th38).
- Phase E submitted (7, work/w2E_ids.txt): θ∈{12,23.5,30}, t∈{.30,.35,.40}, b∈{1,1.25}.
- Posted reconciliation note 20261002T060830.193Z_swarm-g_note_6219 (critique count: 2).
- NEXT: fit; if peak interior, stop refining, wait r56; then final coverage post; consider b's |G|²=7 10.9° orbit stack. Budget 79/500.

## 2026-10-02 06:30 — wakeup 8: phase E interior peak; β re-tune (phase F)
- Phase E: best min(s21,r46) = E_th23_t35_b125 (0f4e) s21 1.2613 / r46 1.3379; ec22 (b=1) 1.2589/1.3099. s21 plateau 1.23–1.26;
  r46 falls past t≈0.25 (θ23 t.40: 1.247/1.247). θ=12° and 30° slightly worse. α-plane refinement DONE.
- No r56 for any w2 point yet (queue strongest-first; w3 points ~2.4 ahead). Withdrew E th12×2, th23_t40, th30.
- Board: b stacks S8T1-90° (2nd harmonic of P4⊥, −0.04/entry) on 7f3e → bb0d 1.231/1.434; h probing gradients at e214 (family w2-orient-grad).
  f: parents' r46 gap 4.1% low → every r46 R has +4.3% boost; r56 binding. n: PES eg falls with M2 for static too.
  p: cc86 & 8 grid pts STRONG; static-free null. o: β-chiral gain sign-locked to α.
- Phase F submitted (3, work/w2F_ids.txt): 0f4e α base (θ23.5,t.35) + r's N5 β pattern c665 ×1, ×1.5, ×2.
- NEXT: compare N5 vs e064; wait r56 on reps (7f3e, 98ec, C2 t30, B2 t20, D th23 t25/t30/t30b15, D th38, 0f4e, ec22);
  then final coverage post. Budget 82/500. Critiques so far: 2 notes.

## 2026-10-02 06:58 — wakeup 9: STRONG claim on w2; β re-tune lane
- r56 landed: 29a2 (B2 −P1pair t.20, α-only) s21 1.108 / r46 1.131 / r56 1.116 / conv46 1.131 → broker STRONG.
  98ec (combo t.20, α-only) 1.102 / 1.245 / 1.200 / 1.245 → STRONG. conv46 == r46 to 5e-9 (converged, not a bug: different hashes).
- Posted CLAIM 20261002T065715.745Z_swarm-g_claim_108d (provisional like cc86/bd1a pending ruling on static-content; w2-only = parent-dependent).
  Control: n 5ab2 (M2-matched static to 98ec) 1.039/1.040. Asked n for 29a2 control (+r56) via builds-on.
- Phase F: N5 (c665) on 0f4e worse than e064 (1.244/1.224/1.174 for ×1/1.5/2). Withdrew ×1.5, ×2.
- Lanes (b's proposal, accepted): b α classes; r β on bb0d; g β on 0f4e; k Q0-free T2 β; h diagnostics. b's f0fd s21 1.305/r46 1.474.
- Phase G submitted (5, work/w2G_ids.txt): chiral β C-modes on 0f4e. SIGN: j's θ = argG−argR = opposite of my label,
  so j's live S3(|G|²=4)×T1 +b(j) = my −b. Points: c4 −.04, −.08, +.04(sign check); c1 +.04; c4 −.06 + c1 +.03.
- Budget 90/500.

## 2026-10-02 07:45 — wakeup 10: w2-orient closed; w2-sobol launched
- Phase G (chiral β on 0f4e): c4 −.04 1.2633 (flat), −.08 1.228, +.04 1.196 (sign: j's + = my −), c1 +.04 1.227 → β saturated.
- Posted w2-orient final result w/ coverage 20261002T072353.031Z_swarm-g_result_2cec (54 w2 + 33 w3 req).
- Board: r claim e064 STRONG (w2 phase-only, r56 1.141); l claim 9fcb STRONG (w2 phase-only); k w2 T2 classes on 0f4e: c6a8 1.333,
  8292 1.332, bd8e 1.329; b f0fd 1.305; e: all claims MT-invariant; c, m done.
- w2-sobol hypothesis 20261002T072402.582Z_swarm-g_hypothesis_2bb7; 32 scrambled Sobol (seed 20261002) over 11 dims,
  g_cut 12; generator work/gen_w2S.py, coords work/w2S/coords.json.txt, ids work/w2S_ids.txt. NOTE: swarm check/submit slow (~5 s each) → run in background.
- NEXT: fit log R (linear+diag), local search around best if off-path (~20). Budget ~122/500.

## 2026-10-02 07:48 — wakeup 11
- b & k: w2 α T2 classes are s21-ONLY (combo3 on fb0c s21 1.215 / r46 0.407; k abandoned w2-T2: s21 +, r46 −). My Sobol includes
  3 α T2 dims (S9T3_60, S12T3_30/90) + S9T3 chiral β → judge Sobol by min(s21, r46), not s21.
- Human: r56 queue now ranked per parent (w2 candidates no longer starved).
- n submitted controls: 3a51 (M2-matched static to 29a2, s21/r46/r56), 9c49 (r56 of 5ab2, builds-on 98ec).
- r takes β re-tune on fb0c (mailed). h: S2T1∥ now live on w2 at fb0c.
- Sobol: 7 done, 7 FAIL (manifold), 18 pending.

## 2026-10-02 08:09 — wakeup 12 (quiet)
- n 2a24: 29a2 M2-matched static (3a51) 1.0134/1.0135 vs 1.108/1.131 → density ~12%; r56 legs (3a51, 9c49) pending → then claim update note.
- e: claims audit; robust tier split/Δ≤1e-2. j, f, o, c, m done. Sobol: 8 done, 7 FAIL, 17 pending (queue slow).

## 2026-10-02 08:33 — wakeup 13: Sobol map → off-path w2 point S09
- Sobol (32): 25 PASS / 7 manifold FAIL. S09 (req 20261002T072742.._1909? see w2S_ids) s21 1.513 / r46 1.539, sp/D .007, eg 4.4, M2k 2.603.
  Others: S14 1.399/1.397, S17 1.443/1.384, S25 1.519/1.356, S02 1.332/1.392, S21 1.592/1.298. S05 s21-only (1.347/0.921).
  Clean top points: small P4⊥, negative S16T1-90, e064 0.7–1.05.
- Linear fit (box units) R² .55 (s21) / .70 (r46): agree S16T1_90 −, S9T3_60 α +, e064 +, C4 −, S9T3 chiral −.
- Posted 20261002T083252.806Z_swarm-g_result_7515 (typo: S09 full id placeholder; real id in work/w2S_ids.txt).
- Withdrew 12 weaker Sobol promotions. Submitted 13 local points around S09 (work/w2L, ids work/w2L_ids.txt, builds-on 1909):
  3 grad steps, 7 pushes, 3 ablations (S12T3_90→0, S7T1→0, all α T2→0).
- r56 for S09 pending → then request control (n). Budget ~132/500.

## 2026-10-02 09:00 — wakeup 14: local search around S09
- Wins (s21/r46): S16→−.15 1.575/1.608; e064→1.4 1.570/1.599; C4→−.08 1.561/1.595; S9a60→.06 1.550/1.566; grad .05/.10/.15 rising to 1.573/1.598.
- Losses: P4⊥→0 1.448/1.447; S12a30 −.06 1.481/1.483; S7→0 1.510/1.493; S9ch −.03 flat.
- ABLATION: all T2 α → 0 (a99e): s21 1.282 / r46 1.579 → T2 α mostly an s21 boost; S12a90→0: 1.415/1.629.
- Round 2 submitted (work/w2M, 6): C1 = S09+{C4 −.08, S16 −.15, e064 1.4, S9a60 .06}; C1+e064 1.8; C1+S16 −.20; C1+C4 −.12; noT2 (C1 w/o T2 α); grad .25.
- Withdrew 5 losing local points. Budget ~151/500.

## 2026-10-02 09:26 — wakeup 15: S09 line climbing
- Round 2: C1 055f 1.725/1.734; C1+S16 −.20 1059 1.764/1.793; C1+e064 1.8 da48 1.785/1.773; noT2 af40 1.262/1.686. sp/D ≤.006 (af40 .015).
- Moves additive. Posted 20261002T092601.440Z_swarm-g_result_b2f0 (includes S09 full id correction).
- Round 3 submitted (work/w2N, ids work/w2N_ids.txt): D1 = C1+S16 −.20+e064 1.8; D1+S16 −.25; D1+e064 2.2; D1+C4 −.12; D1+S9a60 .09; D1+P4 .10.
- Withdrew superseded L_* and S17, M_grad25, M_C1_C4m12. On ladder: S09, S14, C1, 1059, da48, af40, a99e?(withdrawn), round 3.
- NO r56 yet for any Sobol-line point (queue). r's bf94 1.548/1.591 was best w2 before. Budget ~163/500.

## 2026-10-02 09:52 — wakeup 16: round 3; pause for r56
- Round 3: D1 3ab0 1.789/1.836; D1+S9a .09 0356 1.857/1.865 (best, sp/D .003); S16 −.25 5dfe 1.715/1.864; e064 2.2 dbbc 1.776/1.864;
  C4 −.12 f386 1.713/1.840; P4 .10 6b7d 1.759/1.843. s21 saturating, r46 still rising → r56 must arbitrate.
- Withdrew 7; reps on ladder: S09 1909, 1059, 3ab0, 0356, af40 (noT2). Plus 98ec/29a2 claimed, 7f3e/0f4e etc waiting r56.
- Human: r56 controls on claimed candidates now priority 1. i: static-free-w2 null.
- PLAN: no more climbing until r56 lands on the S09 line. Then: claim + request matched-static control (n) for best robust point.
  Budget ~169/500.

## 2026-10-02 10:24 — wakeup 17: w2 r56 stalled → request posted
- No w2 r56 since ~06:50 for anyone (r bf94/9857, b 879b, my 0356/3ab0/1059/1909/af40 all at stage r56).
- Posted request to human re w2 r56 starvation. b closed w2-outer-orbit (cites my 1059 as superseding); r done.
- Holding: no new submissions until r56 lands. Budget ~169/500.

## 2026-10-02 10:55 — wakeup 18
- Human fixed w2 r56 stall (FAIL request 42bd had set w2 parent-best → 0356 scored 0.78). 0356 now priority 1; also a GPU lane bug fixed (n).
- Control note: n's 5ab2 (static mix, M2 2.664) = 1.039/1.040 upper-bounds static at 0356's M2k 2.654 (monotone yardstick).
- l, r, b, j, f, a, c, d, e, m, o, p, q done or closing. Waiting r56.

## 2026-10-02 11:27 — wakeup 19: CLAIM 0356; Sobol batch 2
- r56 landed: 0356 s21 1.857 / r46 1.865 / r56 1.789 / conv46 1.862 STRONG (sp/D r56 .044, eg 3.6); 3ab0 1.789/1.836/1.785/1.834 STRONG.
- Posted CLAIM 20261002T112551.624Z_swarm-g_claim_b6f8. Control: n 5ab2/9c49 (M2 2.664) 1.039/1.040/1.039 upper-bounds static.
- n, k, i done. Sobol batch 2 (seed 20261003, widened S16/e064/C4/S9a60) submitted: work/w2T, ids work/w2T_ids.txt. Budget ~201/500.

## 2026-10-02 11:59 — wakeup 20: Sobol batch 2 = no second basin; mechanism ablations
- Batch 2 (wider box): 21 PASS/11 FAIL. Best min: T30 5c74 1.611/1.602, T13 3774 1.570/1.608, T09 1.420/1.643, T29 1.414/1.546.
  T08 s21-only (1.722/1.219). → S09 line (0356) remains the w2 optimum. Withdrew all but T30, T13, T09, T29.
- b verified claim b6f8 (kernel converged, r56 sp/D .044 the only thin margin). h offered gradient diagnostics at 0356 → accepted.
- Submitted ablations of 0356 (work/w2X): α-only ee21 (β=0), β-only 0b1c (α=0).
- NEXT: post batch-2 + ablation result with final w2-sobol coverage; then consider swarm done. Budget ~235/500.

## 2026-10-02 12:25 — wakeup 21: 0356 ablations
- α-only ee21 s21 1.147 (M2k 2.654); β-only 0b1c 0.870 (M2*); full 1.857 → cross-term +84% at fixed density: α×β interplay (cf. o 7147 on w3).
- Submitted sign-lock test: 0356 with β→−β (work/w2Y). Then: final w2-sobol result w/ coverage, then swarm done.

## 2026-10-02 12:30 — DONE
- Sign lock: 0356 with −β → s21 0.108 FAIL. α-only ee21 r46 1.266.
- Posted final w2-sobol result 20261002T122942.954Z_swarm-g_result_5af0 and `swarm done` summary. 179/500 charged.
