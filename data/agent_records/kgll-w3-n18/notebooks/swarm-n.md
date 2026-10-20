# swarm-n notebook

Started 2026-10-15T04:13:37+00:00.

## 2026-10-15 04:38 — wakeup 1: scope chosen = mechanism controls (w3-m2ctrl)
- Board at start: atlas (a, c=w2), joint (b), bigamp (e), fsfloor (f), chiral phase (g, h),
  and matched-perp G⟂R, R=ℓ²ẑ×G, on w3 (b, i, j, k). That is heavy herding, so I stayed out of perp.
- Top results: j S1⊥ α=0.1/0.2/0.3 → s21 1.220/1.369/1.235, r46 1.182/1.386/1.204;
  M2k 3.877/4.733/6.184. b_f06f (S1⊥ α=0.05) is robust_positive (1.088 at conv46).
- My single-particle fact (work/ctrl.py): both parents sit ON the positivity boundary along their
  own shape (w3 min ρ/mean 0.005, w2 exactly 0), so no static density of the parent's shape has a higher M2.
  The BZ-averaged ρ_k of S1⊥ has M2 of only 3.65–3.71.
- Posted hypothesis 20261015T043719.157Z_swarm-n_hypothesis_c2e9 and request ..._request_76c0; mailed j.
- Submitted 6 controls × {s21,r46,r56} = 18 evals (work/controls/, generator work/make_controls.py):
  avg_7d04 e272, frzp_7d04 05fc, frzm_7d04 e5d4, avg_6139 5b86, frzp_6139 a059, frzm_6139 97a9.
- Next: read the controls. If frz± ≈ the candidate, the gain is a static-shape/M2 effect; if frz± ≲ 1, it is beyond M2.
  Possible follow-ups: 8e11, b_f06f, the best S2⊥/S3⊥ points, and a static-frontier c-scan.

## 2026-10-15 05:00 — wakeup 2
- Controls are herded: a, d, l, m, o, p, q, r and I all ran ρ̄ / M2-matched controls on the S1⊥ line. Consensus:
  ρ̄ gives ≈1.00–1.04, S1-direction M2-matched statics lose (mine: frzp 7d04 s21 0.769, r46 0.827; frzm s21 0.947, r46 1.031;
  6139: avg 1.004, frzp 0.893/0.966, frzm 0.904/0.976). Gain is beyond M2 under those definitions. Closing w3-m2ctrl (r56 still pending).
- BUT swarm-a a6e6: STATIC ρ_w3·e^{κρ_w3} at M2=4.733 → 1.184/1.196/1.191. So statics can beat w3 by ~19%.
  New family w3-staticfront (hyp ..._hypothesis_84f3): static frontier along exp(κρ_w3) at M2 4.2/5.5/6.5/8.0 and exp(c O_S3) at 4.733/6.0, s21 only.
  reqs: 3937 af4c 5856 cd1c 5072 3b67. Generator work/make_static.py (cut 24). The power family was dropped (non-smooth).
- Other board facts: the S1⊥ gain is S1-only (S2⊥, S3⊥ lose); on w2 the oblique classes at α<0 win (~1.11–1.15); the uniform-LL0 S1⊥ loses
  (parent interference). Sign rule: α·w_parent(G±G_R)>0 (c, p); swarm-m found a counterexample (S1×T2 ∥).
- Cyclotron factor e^{-|G|²ℓ²/4}: S1 0.16, S2 0.004, S3 7e-4, so only S1 harmonics matter for cyclotron dressing.
- Next: read the frontier. If static reaches ≥1.3, post that k-GLL beats the parent but not statics, and run r46/r56 on the best.

## 2026-10-15 05:17 — wakeup 3: STATIC FRONTIER RESULT
- s21 static ρ_w3 e^{κρ_w3}: M2 4.2 → 1.101 (3937), 5.5 → 1.286 (af4c), 6.5 → 1.386 (5856), 8.0 → 1.453 (cd1c);
  expS3: 4.733 → 1.199 (5072), 6.0 → 1.382 (3b67). All PASS. Smooth, concave, rising curve.
- k-GLL leaders: j 7d04 1.369; h 0672 (S1⊥ 0.2 + chiral β S7) 1.427 s21 / 1.461 r46, M2k 4.733.
  So at matched M2 the k-GLL wins (≈1.4 vs 1.19), but statics at M2 8 match it absolutely.
- Posted result ..._result_7477, request to the human ..._request_b267 (headline wording; OK to try sharpened parent + k-dep?), mailed j, h, a, b.
- In flight: r46/r56 for M6.5 (fcb1), M8 (616a), S3 M6 (6ee7); s21 extension M10/12/15 (5612, 67c0, 1b98), S3 M8/10 (34cf, db71).
- Old m2ctrl r56 pending for 6139 controls.
- Charged: ~35/500.
- Next: find the peak; if the human OKs it, run controls "sharpened static + S1⊥ deformation" to test whether the gains stack.

## 2026-10-15 05:35 — wakeup 4
- Frontier: exprho M10 1.359, M12 1.050, M15 FAIL 0.43 (peak ≈1.45 near M2 8); expS3 M8 1.559, M10 1.537.
  r46: exprho M6.5 1.461, M8 1.450; expS3 M6 1.409.
- k-GLL leaders: p fe3d (S2∥ + chiral β S7; M2k 5.165) 1.695/1.687/1.688 on s21/r46/r56, which beats my best static (1.56).
  Posted correction note. Stage 2 submitted: expS3 M9 (c571), mix ρ+O4 at M8/M6.5 (eca4, d15d), O4+½O12 at M8 (f4fa), expS3 M8 r46/r56 (f88c).
- Other: swarm-m is testing "quasistatic" chart imitation of static sharpening (3 evals).
- Charged ≈ 52/500. Next: close staticfront with a coverage block once stage 2 lands. Then consider a role: verify the fe3d/xcombo leaders
  (MT partner of the chiral β, r56 orientation artefact per swarm-p's refutation) or help with sharpened-parent tests if the human OKs them.

## 2026-10-15 05:55 — wakeup 5
- Static stage 2: expS3 M9 1.580 (c571), mix ρ+O4 M8 1.498 / M6.5 1.409, O4+½O12 M8 1.483; expS3 M8 r46 1.624 (f88c).
  Static frontier ≈1.58 (s21) / 1.62 (r46).
- Leaders are now 2.38–2.59 (b 02f7 = S2∥ α0.25 + class-resolved chiral β 0.08 on |G|²=7×T1; j c89a, h 4927 at s21 2.44–2.45), far above statics.
- Posted: close-out result _result_2d24 (with coverage), abandon w3-m2ctrl _abandon_9592, and kernel-truncation note _note_f9dd
  (leaders: |W|² outside the g_cutoff box ≤2e-4, outside 10 ≤6e-5).
- New: w2-staticfront (8 controls on s21; exp(κρ_w2) and exp(c L3) at M2 3.2/4.0/5.0/6.5, floor 2e-4). Hypothesis posted.
- Charged ≈ 65/500. Pending r56 for some w3 statics.
- Next: read w2 statics and compare with the w2 leaders (1.16–1.23). Then decide whether I can add search value (crowded) or should stay in the
  verifier role; possibly finish early with `swarm done` if nothing distinct is left.

## 2026-10-15 06:11 — wakeup 6
- w2 statics s21: exprho M3.2 1.142, M4 1.237, M5 1.274, M6.5 1.175; expL3 (ρ_w2's |G|²=3 component) M3.2 1.172, M4 1.328,
  M5 1.469, M6.5 1.588, still rising. swarm-g: M2 2.58/2.68 exprho → 1.020/1.043.
- w2 k-GLL leaders: 1.19–1.23 s21 (p 8a0d r46 1.41). So on w2, statics beat k-GLL in absolute terms on s21; at matched M2 k-GLL wins.
- Posted _result_41f7 and mailed c, g, p, e. Submitted expL3 M8/10/12 s21 (34ac, 7bb4, 649d; cut 36 for M10/12) and r46/r56 for M5/M6.5 (58a6, c51c).
- w3 leaderboard is now 3.6 on s21 (swarm-a stack, cc13), far above the w3 static frontier of 1.6.
- swarm-m: convergence replicates of the leaders; swarm-q: 02f7 converged (−0.55% at n_mesh 64 / g_cutoff 10).
- Charged ≈ 80/500.

## 2026-10-15 06:32 — wakeup 7
- w2 statics: expL3 M8 1.626 (34ac, peak), M10 1.507 (7bb4), M12 FAIL 0.457 (649d). r46: M5 1.536 (58a6), M6.5 1.684 (c51c). r56 pending.
- w2 leaders: p 8eb3 1.255/1.356/1.339; 8a0d 1.228/1.408/1.381 (strong). So the w2 static frontier (1.63 s21 / 1.68 r46) beats them.
- w3 leaders: r 5d7c s21 4.11, a 713b 3.97/4.80 (r46). The w3 static frontier (~1.6) is far below.
- swarm-d and swarm-i finished early (done) to avoid duplication.
- Plan: once r56 lands, post a consolidated "claims vs static frontier" result with coverage for w2-staticfront, then `swarm done`.
  My roles (controls, static frontier, kernel check) are complete, and the search directions are all owned.

## 2026-10-15 06:58 — wakeup 8: DONE
- Posted close-out _result_3c3a (static frontiers vs every claim). w3 leaders now 4.5–5.1 s21 (o 90a9, a b4b8). w2 leaders ~1.31 s21.
- r56 confirmations are still queued; they will land in the store.
- Ran `swarm done`; loop stopped.
