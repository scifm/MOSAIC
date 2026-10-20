# swarm-ao notebook

Started 2026-10-08T04:37:08+00:00.

## 2026-10-08 wakeup 1 (05:14–05:25 UTC)
- Read board (35 posts), leaderboard, docs 46/40, ADR-0032, kdep_envelope.py.
- Leader: S1×T1 ⟂ (co-moving-matched, R_G=(-n,m)) achiral orbit, swarm-i fa76: α_orb 0.15 (entries 0.0866) → s21 1.1885, r46 1.156 PASS. 0.05 → 1.105 (e 56da).
- Heavy herding on low-shell w3 (i,e,ad,s,z,o,l,d,b,c,f,g) and z3-w2 (q,u,v,x).
- My insight: on LL0, ψ_k = χ_k ⊗ φ_k^LLL exactly, χ_k = Σ η_G c_G(k) e^{iG·X_k} e^{iG·η}|0⟩ (cyclotron orbital). Co-moving → k-indep χ (uniform band, anisotropic LL mixing).
- Posted hypothesis lll-mech (20261008T052140.644Z_swarm-ao_hypothesis_df34).
- Submitted 4 controls (uniform LL0 + S1⟂ orbit), --parent w3 --control, s21:
  a1fd: α_orb +0.05; 0ff3: +0.15; e0c9: +0.30; 9991: −0.15.
  Read gap/delta_lll (Δ_LLL s21 = 1.827e-4).
- Tools: work/build.py (pair-resolved builder, perp_orbit), work/table.py (tabulate all visible reqs; cache in work/cache).
- Next: read controls; decide search family (candidates: w2 transfer of gc-lock, β on top of leader, ...).

## wakeup 2 (05:38–05:42 UTC)
- LL0 controls landed: gap/Δ_LLL = 0.9355 (−0.15), 0.9874 (+0.05), 0.9633 (+0.15), 0.9402 (+0.30). No gain on LL0; the leader needs the parent.
  Interpretation: matches swarm-g offset rule. ⟂ orbit = ½(co L=0)+½(anti L=2G∈S3); w3 S3=3/5 provides the slope.
- Posted result 20261008T053856.088Z_swarm-ao_result_e907 (with coverage). Mailed swarm-as (duplicate cyc-mech) and swarm-g.
- Board: leader now plane-w3 (af c310) s21 1.52 at M2k 5.3; e c3f0 r46 1.41. Herding is huge (48 agents).
- Phase B (note 20261008T054014.463Z_swarm-ao_note_6aec): 9 controls, ids in work/ctl2_ids.txt:
  w3 with S3×0, S3×0.5, all×0.5; each static, α_orb=±0.05 S1⟂. Compare the odd slope with w3's (swarm-i ±0.05 points, find in table).
- Budget charged: 4 (+9 pending).

## wakeup 3 (06:01 UTC)
- Phase B results (s21 gap ratios vs each modified static; static R vs w3: S3×0 0.4477, S3×0.5 0.5856, all×0.5 0.5496):
  | parent | R(+0.05) | R(−0.05) | odd | even |
  | LL0 | (0.987 at +0.05; ±0.15 odd 0.014) | | ~0.005 | ~−0.017 |
  | S3×0 | 0.9911 | 0.9750 | 0.0080 | −0.017 |
  | S3×0.5 | 1.0371 | 0.9240 | 0.0565 | −0.019 |
  | all×0.5 | 1.0340 | 0.9276 | 0.0532 | −0.019 |
  | w3 (swarm-i b6a4/9f92) | 1.0597 | 0.8999 | 0.0799 | −0.020 |
  → odd slope comes from S3 (S6/S8 ≤6%); even cost ≈ parent-independent (~−0.02 per 0.05).
- swarm-g refuted their rule in general (w2 nulls), but this orbit's S3 dependence holds.
- S2×T1∥ also has L = G ± G_c(R) ∈ S3 (G⟂G_c, |L|²=4). Submitted 4 controls (S3×0, S3×0.5; ±0.05 on S2∥): 0d17 73df 01cf 7b43.
- Next: post combined phase-B result + coverage, close lll-mech. Then pick a role (board crowded; reserve/verifier: at, x).

## wakeup 4 (06:21 UTC)
- S2∥ S3-scan: S3×0 odd 0.006 (w3 0.075), S3×0.5 odd 0.048. Posted closing result 20261008T062133.839Z_swarm-ao_result_2aae (coverage, 17 evals).
- Board: s21 leaders 3.3 (swarm-t 4a76, chiral-β dressed, M2k/M2 1.7). r56 stage stalled for everyone (swarm-c request). Several agents in reserve (at, x, u, w).
- Phase C (note 8618): phase-only chiral β S4×T1 χ 0.03 (swarm-w 8ffd) on LL0 (±), S3×0 (±), and w3 −β diagnostic.
  ids: c92a (LL0 −), ac27 (LL0 +), ec39 (S3×0 −), 7802 (S3×0 +), 4552 (w3 −, diagnostic).
  Static refs: Δ_LLL (R 0.3997 vs w3), S3×0 static 0.4477 (995a).
- After phase C: probably reserve/verifier, or done.

## wakeup 5 (06:43 UTC) — closing
- Phase C: S4χ phase-only: w3 odd +0.090 (mirror 0.8725, 4552), S3×0 odd −0.082 (7802/ec39), LL0 odd 0.001 (ac27/c92a). Posted 20261008T064326.490Z_swarm-ao_result_f85a.
- lll-mech closed: 22 evals total, all PASS. The board has many reserve agents; no unique direction left for me → swarm done.
