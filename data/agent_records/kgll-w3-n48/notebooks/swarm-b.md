# swarm-b notebook

Started 2026-10-08T04:34:35+00:00.

## 2026-10-08 wakeup 1 (first on board; no posts yet)
- Read brief, progress/40, 46, theory §6.4/§8, notes §12. Key priors: w3 at Nk=21: α[S1,T1]=+0.05 → +1.85 %,
  −0.05 → −9.0 %, β[S1,T1]=+0.05 → −4.4 %, α[S3,T1]=+0.05 → −3.75 % (progress/46, not in this store).
  Quadratic through ±0.05 on α[S1,T1]: vertex ≈ +0.038, max ≈ +2 %. 024 pilot: 4×6 gains flipped at 5×6.
- Tooling: work/mk.py builds inputs (template + DeformationSpec block). Star classes S1..S10 (|G|²=1,3,4,7,9,12,13,16,19,21),
  T1..T3 (|R|²=1,3,4), checked vs progress/46 lists. swarm check ~1 s each.
- Posted hypothesis 20261008T045925.954Z_swarm-b_hypothesis_94d3: family w3-linmap, 120 evals, ±0.05 single-pair map.
- Next: submit map in ≤32 batches, then quadratic model / line search in top subspace.

## wakeup 1 cont. (05:20Z)
- Map S1–S5 × T1–T3 done (60 evals); result post 20261008T052032.517Z_swarm-b_result_5319. All concave; β even (achiral);
  only α S1T1 (g 1.09, c −28.8), α S2T1 (g 0.90, c −26.3), α S4T1 (g 0.27, c −44) gain. Separable vertices +2.1 %, +1.5 %.
- Herding mails (d, k): dropped S6–S10 (c/f/g cover them). Unsubmitted inputs in work/inputs/linmap/q3,q4.
- New family w3-t1prof (hypothesis 20261008T052052.749Z_swarm-b_hypothesis_fb1d): 3×3 grid S1T1×S2T1 α ∈ {.02,.035,.05}² submitted.
- work/collect.py prints my requests (cache in work/reqcache.json). Queue is now shared: ~15 min per 30 requests.
- Next: fit a quadratic on the grid, then a line search with S3/S4/S5 T1 added.

## wakeup 2 (05:35Z)
- Grid S1T1×S2T1 α: peak 1.0196 (febf); vertex ≈ (0.039, 0.015), R ≈ 1.020; negative cross term. Closed: abandon 20261008T053447.419Z_swarm-b_abandon_6f5b.
- Board learned: joint (G,R) orbits matter. S1×T1⟂ and S2×T1∥ have slope ≈ 1.5/unit A (swarm-i, e); leaders reach s21 1.5 (af, e) at
  M2^(k) ~5–6. swarm-ab static M2 curve: R_static ≈ 1 + 0.19(M2 − 3.63) (s21, small M2).
- Critique posted (20261008T053426.708Z_swarm-b_note_805d): swarm-g's sign rule predicts S1×T2∥ gains, but it is flat (swarm-i 005d/c501).
  Proposed factor e^{−|R|²/4 l_B²} (T1/T2 = 38). Mailed swarm-g.
- New family rule-t1-w3 (hyp 20261008T053641.025Z_swarm-b_hypothesis_5f70): 33-term T1 direction weighted by parent w at
  invariant offsets (work/rule_dir.py, work/mk_rule.py, g_cutoff 10). 8 reqs in work/sub_r1.txt. Prediction: slope ≈ 3.3× single orbit.
  Watch M2^(k): ratio 1.31 at A = 0.15, 2.09 at A = 0.25.

## wakeup 3 (06:05Z)
- rule-t1-w3 closed (abandon 20261008T060349.259Z_swarm-b_abandon_056c). Full slope 2.1 (pred ~5), outer 0.83; best 3f5e s21 1.048 / r46 1.052;
  A=0.25 → 1.73 PES FAIL (other phase), outer A=0.15 manifold broken. swarm-g refuted their own rule. Mailed as/ag (duplicate w2 transfers).
- Board: chiral phase-only β dressing of w3 amplitude leaders → s21 ~2.0–2.5 (j ba1f, am 08b5, t xfam-gp 0e99). r56 is pending for everything,
  including the parents' r56. Several agents are now verifier/reserve (at, x).
- New: chidress-w2 (hyp 20261008T060559.686Z_swarm-b_hypothesis_405b). w2 bases m d43f (s21 1.161) and ff48 (r46 1.22) + ah d734 S7 chiral β × t.
  7 reqs (work/sub_c1.txt). Tool: work/merge.py (ed_input(agent, rid), merge, write).
- 06:14Z chidress-w2 batch 1: d43f + S7χ t=1 → s21 1.2991 (8c39); t=1.5 1.262; t=−0.5 1.013; ff48 + t=0.5 → 1.209. Interim result 20261008T061403.908Z_swarm-b_result_6d66.
  Mailed aq/av/an (an had proposed aq/av for this cross term). Batch 2 (work/sub_c2.txt): t 0.75/1.25; + S4(11°)− (an 3938) or S3(30°)− (an 1e14)
  at u=0.5/1.0; ar 4413 base + S7 t=0.5/1.
- 06:40Z batch 2: S7 t-scan on d43f flat top (0.75: 1.282, 1.0: 1.299, 1.25: 1.296, 1.5: 1.262). S3m u0.5 1.289, u1 1.213; S4m hurts (1.228, 1.072).
  4413 + S7 t=0.5/1: 1.168/1.171 (base 1.061). Batch 3 (work/sub_c3.txt): d43f α ×0.75/1.25/1.5 + S7 t1; d43f+4413 + S7 t1/1.5.
  Batch-1 points are at r46 (pending). r56 not yet landed anywhere.
- 06:29Z batch 3: d43f α×0.75 1.258, ×1.25 1.265, ×1.5 FAIL; d43f+4413+S7 1.225/1.228. Closed chidress-w2 (result 20261008T062853.736Z_swarm-b_result_16c3).
  Best: 8c39 s21 1.2991 / r46 1.3434. Mailed swarm-q (cma-w2) to start from 8c39.
- Budget ~97/500 charged. State: waiting for r56 (stalled for everyone, swarm-c asked the human). Next: when r56 lands, check the sign of my
  promoted points (975f, 3f5e, 8c39, a6c7..., 1aed, e23d, ...) and do a finite-size critique of the board leaders. Otherwise reserve.
- 07:00Z: no r56 results anywhere; 0 in flight. Holding. NOTE: use 'swarm digest --no-mark' when previewing (lost a backlog view once).
- 07:31Z: many agents done (ak,g,i,x,o,d,al,ah,w,at,u). w3 frontier s21 4.39 (ap 3a0e, Σ|α| 2.39). ai stepped 8c39 → 1.3248 (0e27). r56 still stalled. Holding in reserve; final summary once r56 reads my promoted points.
- 08:25Z: swarm done posted (work/posts/done.md). Loop stopped.
