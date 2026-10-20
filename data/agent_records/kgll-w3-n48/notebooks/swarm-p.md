# swarm-p notebook

Started 2026-10-08T04:35:28+00:00.

## 2026-10-08 05:15 — wakeup 1 (setup, role choice)
- Read brief, docs 40/46, ADR-0040, board. Board herded: w3 atlases (b,c,f,g), Hessian (d), joint orbits (e,i), z2-w3 (h),
  chiral-beta (j), global sobol (o), nematic/ps (k), c3break (r), w2: atlas (a), orbit-w2 (m), z3-w2 (q).
- I derived the w2 Z3 symmetry (work/z3check.py: tau=(1/3,1/3) <-> delta=K=(2/3,1/3), S00 match 2e-15; Nk=21 contains K)
  but swarm-q posted it first -> dropped. Phase-1 w2 orbit inputs exist in work/inputs/p1 (unused; swarm-m covers).
- Leader: S1xT1 perp orbit (G.R=0 pairs). e 56da: s21 1.105, r46 1.088 (alpha 0.05/entry); i fa76 s21 1.1885 (0.0866/entry).
  Gain ~linear in amplitude. M2^(k) only +1.6%/+5%.
- ROLE: family `m2-control` = matched-density static controls (beyond-M2). Hypothesis 20261008T051322.137Z_swarm-p_hypothesis_9033,
  human request 20261008T051345.766Z_swarm-p_request_7bf2, note on co-moving interpretation 20261008T051407.373Z_swarm-p_note_c84d.
  Controls (--control, s21,r46,r56): 070b fa76_kavg, f836 fa76_m2, 170d 56da_kavg, 526a 56da_m2, d317 be47_m2. 15 evals.
  Control A kavg: BZ-avg of rho_k (work/control_build.py) ~ parent to 1e-3. Control B m2: (1-t)rho*+t rho*^2/M2* (work/control_m2sq.py);
  linear rescale and rho^p projections fail positivity (w3 near zero).
- Insight: co-moving harmonic e^{i(G.r - R.k)} with R_G=(-n,m) is invariant under all magnetic translations (delta=(-t2,t1)).
  perp orbit = half co-moving + half anti-moving; pure co-moving needs sin x sin (swarm-m's request).
- Next: collect control results; post result w/ coverage. Consider follow-up controls for new amplitude winners; maybe a
  co-moving-motivated search (S2xT2, S3xT3 perp orbits combined with S1xT1) if not covered by h/e/i.

## 05:31 — wakeup 2
- Control results (s21 = r46 to 4 digits; r56 pending): fa76 A 1.0030 / B 1.0336 (cand s21 1.1885, r46 ~1.16);
  56da A 1.0010 / B 1.0107 (cand 1.105/1.088); be47 B 1.0091 (cand 1.0995). => S1T1-perp & S2T1-par at small amp are beyond
  k-avg density and beyond M2 law by ~+8-15%.
- swarm-ab (mdctl-w3) duplicates; agreed split: ab = static Δ(M2) curve via rho^p (slope ~0.19/unit M2 at s21), me = per-candidate A+B.
- swarm-e now leads with S2xT1-par at large amp: a7c2 (0.3/entry, M2k 5.91, s21 1.505), c3f0 (0.2, M2k 4.57, 1.452).
  M2 law could explain much of that. Submitted A (work/control_kavg2.py, 25 shells to |G|^2<=64, needed for positivity) and
  B (control_m2sq.py) for both: b71a a7c2_kavg, 21ef a7c2_m2, 35f1 c3f0_kavg, cefd c3f0_m2. 27/500 charged.
- swarm-as/ao: co-moving part = k-independent cyclotron operator (LL mixing); uniform-LL0 controls running there; scope Q to human.
- Next: on r56 landing, post result (with coverage block) for m2-control. Then controls for further leaders as needed.

## 05:53 — wakeup 3
- s21/r46 control results (r56 pending everywhere incl. parents). E = R_cand/R_B:
  56da 1.093/1.076; fa76 1.150/1.118; be47 1.090/1.082; c3f0 (S2T1par 0.2, M2k 4.57) 1.247/1.211; a7c2 (0.3, M2k 5.91) 1.096/0.985
  -> a7c2 fully M2-explained on r46 (1.364 < static 1.385). Control A (k-avg) always 1.00-1.04.
- Posted interim result 20261008T055156.058Z_swarm-p_result_16fe; mailed swarm-e.
- New s21 leaders: swarm-j chidress (c3f0 + chiral beta) up to 2.03 at M2k 4.571 (B=1.164) -> biggest beyond-M2 if holds.
- Submitted shape-B static curve at M2 4.4/5.0/5.5/6.5 (b087, 68ee, 7ca9, af82) to compare with swarm-ab rho^p curve (shape spread).
- 51/500 charged.
- Next: r56 values; final result + coverage; shape spread; check ba1f etc on r46.

## 06:20 — wakeup 4
- Shape-B static curve (M2 4.4/5.0/5.5/6.5): s21 1.1359/1.2335/1.3109/1.4586, r46 1.1377/1.2386/1.3200/1.4772.
  vs swarm-ab rho^p: B lower by 0.3-1.2% -> shape spread ~1%. Posted 20261008T06xxxx result (shape-independence).
- r56 stalled campaign-wide (~95 min, swarm-c asked human). All my 13 controls await r56.
- s21 leaders now 2.5-2.9 (swarm-ap tl-grad, swarm-t xfam; M2k 4.1-5.1; amplitude+chiral beta). Many agents in verifier/reserve.
- 51/500 charged. My family essentially complete pending r56. Next: when r56 lands, final result with coverage; consider
  verifier role / budget offers; or a beyond-M2-efficiency search if a gap emerges.

## 06:50 — wakeup 5
- r56 still stalled campaign-wide. Leaders: swarm-t xfam (6107 s21 3.39/r46 3.71; b863 r46 4.21; M2k 6.227, 36 S-stars x 9 T,
  sum|a| 1.97, sum|b| 0.72-0.96). swarm-ab did ef7f control (aj request). Many agents in reserve/verifier mode.
- Submitted control A for 6107 (covers b863): f50e (s21,r46,r56). rbar truncation residual 3.4e-2 at |G|^2<=64 (tails irrelevant).
  B not needed (curve: R_static(6.23) ~1.42-1.43). 54/500 charged.
- Next: when r56 lands, final m2-control result with coverage block. Then likely reserve/verifier or done.

## 07:22 — wakeup 6
- 6107 control A: s21 1.0146 / r46 1.0227. Posted closing result with coverage: 20261008T072144.124Z_swarm-p_result_4fa1.
- Static M2 extension to 7-10 claimed by swarm-l (m2hi-ctl) and offered by as/av; told as/av to coordinate (not me).
- r56 still stalled (>2h). Many agents done. Plan: wait (1h cadence) for r56 on my 14 controls, append r56 column, then `swarm done`.
  54/500 charged.

## 08:24 — wakeup 7 (done)
- r56 still stalled campaign-wide (>3 h). Frontier now swarm-ap R~5.4 (s21/r46). My family closed with coverage (4fa1).
- Ran `swarm done` with summary. 54/500 charged; r56 legs of 14 controls will land in the store automatically.
