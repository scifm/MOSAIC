# swarm-c notebook

Started 2026-10-02T03:51:09+00:00.

## 2026-10-02 wakeup 1 (≈04:00–04:15 UTC)
- Read charter, docs 40/46, theory §2/§6.4/§8, notes §8.4/§12, ADR-0040, config. Budget 500 evals/agent; Nk=21 evals are seconds.
- Board: swarm-a took `w3-atlas` (single-direction ±0.02 slopes, S1–S8 × T1–T3 × α/β, 96 req; then line search + CMA in top subspace).
- My family: **`w3-wide`** (hypothesis 20261002T040250.574Z_swarm-c_hypothesis_6b9d): joint multi-direction CMA-ES, S1,S2,S3,S4(|G|²=1,3,4,7) × T1,T2(|R|²=1,3); stream A = 8-D α (box |α|≤0.6), stream B = 16-D α+β (|β|≤0.3); g_cutoff 6, n_mesh 48.
- Physics notes: deformation block only represents cos(G·r)cos(k·R) products (γ even in r and k separately). Any k-dependence breaks ideality (tr g − F = ε²σ²|∇f|² for phase). w3 density lives on even G only (S3, 2S2, 4S1). doc46: α[S1,T1]=±0.05 → +1.85/−9.04 % → 1-D quadratic vertex ≈ α 0.038, ≈ +2 %.
- Submitted 24-request radial calibration (work/batches/calib, log calib_log.json, ids calib_ids.tsv): 4 random dirs per stream × r = 0.05/0.15/0.4.
- Tools: work/gen.py (template+block), work/stars.py, work/space.py, work/cma.py (resumable ask/tell CMA; `uv run ... python work/cma.py A 1`).
- Next: read calibration → set σ0 → launch CMA A1, A2, B1 (B2 later).

## wakeup 2 (04:20 UTC)
- Board exploded: 18 agents, many on chiral/orientation phase modes (d,g,h,i,j,k,l), atlases (a w3; b,e,f w2), pooled surrogates (o,r), contrast-pump (n), m2-breathe (p), geom-mech (q), K7 (m).
- Corrections received: cos·cos joint orbits representable via pair-stars (g,k) — I was wrong; β on star products MT-odd → no physical linear slope (d,i,l); g_cutoff 6 truncation bad for S4/large α (n); only T1/T2 clean on all meshes (r).
- Action: dropped stream B; space.py G_CUTOFF → 10; launched CMA A1 (from parent) and A2 (from α[S1,T1]=0.035), σ0 0.04, λ 12, budget 144 each. Background driver work/drive.sh → work/drive.log. Note posted 20261002T042057.415Z_swarm-c_note_4ddb.
- Calibration (24, g_cutoff 6) still queued; broker queue is long (~250+).

## wakeup 3 (04:42 UTC)
- Calibration (g_cutoff 6, star space): r=0.05 → 0.95–1.01; r=0.15 → 0.54–0.96; r=0.4 → ALL FAIL (splitting/Δ 1e4–1e5, broken manifold = other phase). Strongly concave in random directions.
- CMA star space: A2 best b460 s21 1.0386 / s21c 1.0387 / r46 1.0403 (r56 pending); A1 best efdf 1.0280. Stopped CMA after gen 2 queued (72 evals). Star products dilute the orbit gradient by 1/√3 → pivot.
- Board: gradient lives on S1T1 ⟂ orbit ((1,0)|(0,1),(0,1)|(1,0),(1,1)|(1,−1)) and S2T1 ∥ orbit ((1,−1)|(1,−1),(2,1)|(1,0),(1,2)|(0,1)); h 6e88 t=0.11 ⟂ → s21 1.135, still near-linear. β-chiral S4T1/S7T1 live (d, i). n running matched-density controls for 6e88.
- New family **w3-far** (hyp 20261002T044402.873Z_swarm-c_hypothesis_a06e): 25-pt polar grid θ∈{0,30,45,60,90}°, t∈{.15,.2,.27,.35,.45}, g_cutoff 12; work/far.py, ids work/batches/far1_ids.tsv. Mailed h, o.
- TODO: tell CMA gen2 results (manual run of cma.py once, it will then submit gen 3 — DON'T; just read results instead) ; post w3-wide coverage result after gen2 lands.

## wakeup 4 (05:00 UTC)
- far1 grid: ALL 25 PASS (s21,s21c,r46). Peak mixed θ30–60 at t≈0.27 (~1.39–1.41 both clusters; e426 θ60 t.27 = 1.410/1.409). θ=90 (pure S2T1∥, LL-mixing-free) still rising: 776c t.45 s21 1.518 / r46 1.409; 67ed t.35 1.456/1.414. M2k up to 5.3–7.5.
- w3-wide best bc9e s21 1.066 / r46 1.068.
- Leaderboard w3: o 968b (2A+2C7+2C13, α+chiral β) s21 1.609 / r46 1.710.
- Posted result 20261002T050111.811Z_swarm-c_result_176d (with coverage for w3-wide and far1).
- far2 (16) submitted: θ90 t .55/.65/.8/1.0 (g14 for .8/1.0), θ80 .35–.65, θ70 .30–.45, θ100 .35–.55, θ270 .27/.45. ids work/batches/far2_ids.tsv. table: `uv run ... python work/table.py work/batches/far*_ids.tsv`.
- Others on my points: o adds chiral β on cc20/776c; h gradient probes at 776c; p S2T1∥ + chiral β at t .22–.55; f does w2-far. n/a do matched controls.
- Next: read far2; if ∥ ray peaks, refine; request matched-density control for the best pure-∥ point (ask a/n). Watch r56 for 776c/67ed.

## wakeup 5 (05:17 UTC)
- far2: ∥ ray s21 peak t≈0.45 (776c 1.518); t .55 1.485/1.333; .65 1.363/1.185; .8 FAIL (other phase, 857f s21 1.02), 1.0 FAIL. θ100 t.55 8f68 s21 1.563/r46 1.404 (M2k lower). −∥ destructive. min-over-clusters plateau ~1.41 ridge; best b3f3 (θ80 t.35) 1.466/1.417.
- Posted result afb4 (with coverage) — α-only plane closed. Posted request 8457 to human: r56 bottleneck (FIFO 2 GPU lanes, no w3 r56 yet).
- Board: o/p α∥+β-chiral reach s21 2.40 / r46 2.47 (p cc86), o bd1a 2.27/2.63; m's E-sector points ~2.39. n: frozen-slice controls show static M2 doesn't predict R. f: w3 plane null on w2.
- Decision: no new points while r56 is backlogged. Next: when r56 lands, do a zero-budget finite-size synthesis across the board (s21 vs r46 vs r56) as critique.

## wakeup 6 (05:45 UTC)
- Human implemented my request 8457: pools served by R_gap_min priority. New tools: `--diagnostic` (s21 only, no ladder), `--control --clusters`, `swarm withdraw`.
- Withdrew 124 redundant requests (far grid + w3-wide), keeping ∥ ray (dfc8 8960 cc20 67ed 776c cd5a) + ridge (b3f3 e426 8f68 48dd 045a) + bc9e/b460 for r56.
- Board: r56 lands: o bd1a s21 2.271/r46 2.627/r56 2.567; p cc86 2.399/2.470/2.456 (LL-free α∥ t.55 + chiral β). e: β patterns alone LOSE on parent → α×β interplay. h: S1T2∥ (α<0) live at 776c. n: static yardstick R=1+0.19(M2−M2*).
- New diagnostic (8, s21 only): S2T3∥ (2nd k-harmonic of the ∥ orbit: (1,−1)|(2,−2),(2,1)|(2,0),(1,2)|(0,2)) ±0.05/±0.10 at cc86 and 776c. Tool work/addorb.py. ids work/batches/h3_ids.tsv. Note T3 self-aliased ×1.15 on r46.

## wakeup 7 (06:03 UTC)
- S2T3∥ diagnostics: concave at 776c and cc86 (best +0.05: 1.511 / 2.364 vs base 1.518 / 2.399) → null.
- Claims posted: p cc86 STRONG (2.399/2.470/2.456/conv 2.469), o bd1a STRONG (2.271/2.627/2.567/2.628), d 2400 robust_positive phase-only (1.036/1.080/1.056/1.076). n: M2-matched static reaches cc86 1.42 → ~30% density; 776c static 1.28/1.29 vs 1.52/1.41.
- Critique posted 20261002T060400.109Z_swarm-c_note_241d: PES ent gap 21 → ~5 on amplitude leaders; R peaks at eg≈4.5–5; manifold breaks at eg≲1.5. Mailed p, o, d. work/pes.py.
- Budget 145/500. Ideas left: static-free (i, p doing). Consider whether anything uncovered remains; otherwise wind down.

## wakeup 8 (06:35 UTC)
- r56 landed for my ray: 776c r56 1.499 (conv46 1.409) → broker STRONG; 8f68 1.489, b3f3 1.448, 045a 1.416 also STRONG (provisional, ⟂ content); e426 1.386; 67ed 1.387; 48dd 1.307.
- Posted CLAIM 20261002T063542.545Z_swarm-c_claim_cff6 (776c, α-only S2T1∥, matched static 1.28/1.29 → amplitude claim; partial beyond-density).
- n: purity loss mostly density (static bands also eg 21→6 as M2 4.2→7.9). f: parents' r46 gap 4.1% low → r56 binding. h: S1T2∥ add-on lifts leaders (fea3 2.80/3.59).
- Plan: one more cycle to answer critiques of my claim, then `swarm done` unless a gap appears.

## wakeup 9 (07:06 UTC) — DONE
- a: 776c avg-density control 1.030/1.031; n: M2-matched 1.280/1.288 (55–70%) — already in claim.
- Ran `swarm done` with final summary. Loop stopped.
