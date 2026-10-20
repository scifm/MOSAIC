# swarm-ar notebook

Started 2026-10-14T10:26:27+00:00.

## 2026-10-14 11:40 — wakeup 1 (scope chosen)
- Read board (33+9 posts). Leader: swarm-c jorb S2×T1 +60 β+0.03 phase-only: s21 1.2494, r46 1.4041 (d698). c's map (bc24): MT symmetry holds; separable stars cancel orbit signals; s21≈r46.
- Heavy herding on S1/S2×T1 orbits, 4 surrogates (h,o,t,u), CMA (z, ag, n, am, c, f). My first idea (27-D phase CMA) was taken by ag/n/am within minutes -> dropped.
- Chose family `kharm`: α map of the 18 inner T2/T3 orbits (S1×T3, S2×T2, S2×T3, S3×T1, S3×T2, S3×T3), ±0.05 per entry (c's convention, verified pair matchings match bc24). Hypothesis 20261014T113936.260Z_swarm-ar_hypothesis_f977. Mailed c (take their stage 2) and ae (β on S2×T2/T3 is theirs).
- Tool: work/orb.py (126-orbit basis, block builder, write_input from cached template). Delta labels: p30=+30, m30=150, p60=+60, m60=120, p0=0/180, p90=90.
- Submitted b1: 36 α probes + repro of d698 (S2T1 p60 bp03) — req ids 8ba0 … 5873, aeba.
- Next: when results land, table the slopes; stage 2 = profile lines adding T2/T3 copies to the S2×T1 ∥ α+, ±60 α−, S1×T1 ⊥ α− leaders.

## 12:07 — wakeup 2
- 21/500 charged. Board: huge gains. α⊥ S1×T1 −0.45 1.64/2.63/2.44 (j ea28); f's S3×T1 chiral-odd β +0.05 1.558/1.641 (e5d5); c's STRONG claim d698 (1.249/1.404/1.347).
- Herding: 6 agents on my inner T2/T3 map (e, ao, av, aj, i, me). Mine is the full 36 set, so I kept it and posted dedupe note 4394 with the ids (work/b1_map.tsv). i withdrew its α points; e keeps S3 at ±0.03 (curvature).
- Next: table my map, post result + coverage; then choose stage 2. Candidates: p's hole 2 (inner+outer joint) or hole 3 (large-amplitude non-⊥ α); mechanism controls for α leaders (only k does them).
- 12:40: only 2/37 done (S2T2 p90 ⊥: α−0.05 0.989, α+0.05 0.822; EG ~3.0). Broker queue slow. Waiting.

## 13:15 — wakeup 4
- 28/500 charged. 7/36 map points in; T2/T3 weak or negative so far (best S2T2 p30 α+ 1.012). Repro of d698 hashed identically → free, generator validated (orbit conventions = c's).
- Board: records now c662 union α+β step R 4.76/5.23/4.67 (h claim 0069), 8c01 (t) 4.82/5.19. Records = cos2δ α + sin2δ β on S1/S2×T1(+T2) (av ddbc); T3 opposite sign. Density controls exclude density (k). g vs p debate on d_sc=0.1 vortexability amplification.
- Plan after map: T2/T3-copy gradient at the record for S2/S3 (aq has S1×T3 at record). Decide when map is in.

## 13:45 — wakeup 5
- 17/36 map points in. Inner T2/T3 α is a null: best 1.0118 (S2T2 p30 α+), most points lose; S2×T3 strongly destructive (two FAIL with split/Δ>0.1: p0 α+, p60 α−). S1×T3 ≤ 1.0. aj independently: T3 opposite to T1, concave.
- 19 still SUBMITTED since 11:40 (stuck-lane reports from o, j, m on the board — likely same issue).
- Board: STRONG claims: h c662 4.76/5.23/4.67, t 8c01 4.82/5.19/4.55, v S7T1 single outer α 1.56/1.93/1.79, s noQ0 phase-only 1.725/2.32/2.14, f phase-only S1T1 odd b=.25 1.715/2.07/1.90. Phase-only s21 ceiling ≈1.72 (s21 splitting gate). g retracted the 1/d² critique. ap: γ on uniform LL0 lowers gap → gain is γ×ρ* cooperation.

## 14:17 — wakeup 6
- kharm map done → result 20261014T141409.570Z_swarm-ar_result_6707 (with coverage). T2/T3 α null; S3×T1 ⊥ α−0.05 1.368/1.517 (1bbf); s21 MT artefact 5–20% for T2/T3.
- Board records: av cos2d e0a8 s21 10.39 (T1-only); s c325 9.87/10.15 (T1-only); o f5f1 6.28/8.33/8.12 STRONG claim (29% of Σβ in T2/T3, Σβ cap-bound).
- New family t1proj (hyp 9aab): T1 projection ablations. b2 ids: 017f_t1 3643, 6506_t1 8f04, d2de_t1 db3e, f5f1_t1 ec88, x1.2 2e46, x1.4 e0a7, x1.5 47d5, f5f1_t23 238d. Mailed o,t,h,x.
- Tools: work/rec_content.py (shell×T-star content of any request), work/t1proj.py.

## 14:50 — wakeup 7
- t1proj s21: 017f_t1 8.21 (full 8.28), 6506_t1 7.85 (8.71), d2de_t1 6.17 (7.22), f5f1_t1 4.18 FAIL split/Δ 0.118 (scales 1.2–1.5 FAIL too), f5f1 T2/T3-only Δ→0 FAIL.
- o's own ablation: f5f1's T2/T3 β is ballast (7.01 w/o it). → T2/T3 α in f5f1 suppresses s21 splitting.
- Submitted 2 control runs (r46,r56) of f5f1_t1 ×1.0 (691d), ×1.4 (c2a5) — mechanism ablation, said so on board (note posted).
- Waiting: r46 promotions of 6506_t1/d2de_t1/017f_t1.

## 16:52 — wakeup 8
- t1proj r46: 017f_t1 8.83 (full 9.08), 6506_t1 8.07 (8.71), d2de_t1 7.23 (8.20); f5f1_t1 ctrl r46 7.42 (full 8.33), ×1.4 ctrl 8.01 (split 0.072). → T2/T3 at records is REAL (+3–12% on r46), my artefact hypothesis was wrong; but cap-inefficient (0.2–1.8 R/unit Σ vs 5–9 for T1 α).
- Posted result 20261014T165124.249Z_swarm-ar_result_2ce1 with coverage. 40/500 charged.
- Board: records ~11–14 (w 407a 13.93 qmax-unconverged; h 5063 11.65/12.30/11.97; s 1c48; x 06bb noQ0 11.80). Many agents done. Open items need the human (qmax ≥12, 4th cluster, cap reading).
- Plan: wait one cycle for r56 of 6506_t1/d2de_t1/controls; post a note only if sign changes; then swarm done.

## 17:23 — wakeup 9 (closing)
- r56: 6506_t1 7.33 (full 7.73) and 017f_t1 8.33 (full 8.54): same sign as r46, so the t1proj conclusion stands. 017f_t1 conv46 8.834 = r46. Remaining r56 (d2de_t1, controls) pending; no sign change expected.
- Board converging: STRONG records ~11–13 (av 55f9 12.51/12.71/12.79/13.00 at half the caps; w 407a; h 5063; t cbe3; e c577), all density-controlled. Most agents done. Open items are the human's (N_A=3 on rectangles, per v's critique; 4th cluster).
- Done: 40/500 charged. Running swarm done.
