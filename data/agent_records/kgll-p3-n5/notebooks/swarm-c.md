# swarm-c notebook

Started 2026-10-14T05:16:52+00:00.

## 2026-10-14 05:25 — wakeup 1: scope + phase map launched
- Read brief, docs 40/46, theory §6.4, contract/validate. Key: star fn O_s = d^-1/2 Σ e^{iGr} (max √d), F_p same; γ = (α/2 + iβ) O F.
  Momentum stars metric R1²+R2²+R1R2 (T1,T3 = (±1,0)... ; T3=(±2,0)...). Spatial 120° basis m²+n²−mn. Parent M2 = 10.04; s21 Δ = 2.2586e-4, r46 2.4101e-4.
- swarm-a took `amp-map` (α ±0.15 on 30 (S,T) dirs). I took `phase-map` (β only = clean beyond-M2). Hypothesis 20261014T052202.922Z_swarm-c_hypothesis_ab6c, budget ≤180.
- Tool: work/build.py OUT 'SPEC' (terms [[s_g2,t_r2,alpha,beta],...]; chiral halves "7a"/"7b").
- Submitted map1 (β=+0.1, 30 dirs). map2 (β=−0.1) built in work/map2, submit when slots free (cap 32 in flight).
- Next: write work/collect.py to tabulate R_gap by label; submit map2; line search top directions.

## 2026-10-14 05:40–06:00 — wakeup 2
- My β=+0.1 full-shell map: 24/30 FAIL (outer shells and S3/S4 destroy Laughlin; R~0). Only S1×T3/T4 PASS (0.81, 0.89); S1T1 0.76 FAIL (splitting/Δ 0.11).
  S1 β=−0.1: T1 0.7636 FAIL, T3 0.8089, T4 0.8812 → odd part ≤ 0.003: full-shell β even, as swarm-d's MT argument predicts. Did NOT submit rest of map2 (wasteful).
- Board: swarm-e `chiral-phase` (mirror-odd joint-orbit β, b=0.0245/entry) gives huge gains: O4T1m s21 1.69 r46 1.99; O9T1m s21 1.52 r46 2.42; O3T1m 1.62/1.79. p-signs lose (0.24...). swarm-b duplicates phase-map (β ±0.15). swarm-d chiral halves of 12-shells: even, ~1.
- New tool work/geom.py: numpy port of solver pure-LL0 raw form factor + kernel → FHS Berry curvature + FS metric. Parent: C=−1, S range matches broker (0.2043/1.3750), Ω rel std 2.07, max/mean 15, min/mean 0.10, ideal (trace viol ~0).
  Hypothesis: parent gap (only 1.24× LLL despite M2=10) is limited by Berry-curvature concentration; mirror-odd phase redistributes Ω at first order → big gains. work/geomboard.py correlates with board.
- Geometry vs board: mirror-odd β winners ideal (T ≤ 0.015), Ω relstd unchanged (~2.06); Ω_min/mean tracks sign within ± pairs only. Full-shell α moves Ωstd a lot, no gain.
- Posted result b08e (odd part, β-scale, geometry), abandon 5ca6 (phase-map coverage: 33 evals, best 0.8862 cdd0), critique note 52a2 on e's STRONG claim eb7b (O3T1−: 1.62/1.79/1.67/conv 1.79). Mailed e.
- NEW family `orbit-amp` (hyp 87c1): α on joint orbits, SM (self-mirror δ=0/90) and PM (P+MP δ=±30/±60), S∈{1,3,4,9}×T∈{1,3,4}, α=±0.05/entry. 48 submitted (ids in work/oa1a.ids, oa1b.ids). Builder work/orbits.py (orbit_block terms [[g2,t2,delta,α,β]]), generator work/mk_oa.py.
  Note e's "O<g>T<t>−" = β(δ=+30°)=+b, β(−30°)=−b, b=0.0245.
- Next: tabulate oa map (antisym slope per dir), line search top 5, then joint α-orbit + e's β-odd 2-D scan (await e's reply).

## 2026-10-14 06:10 — wakeup 3
- orbit-amp map landed: big first-order α slopes when resolved by orbit. S4T1-SM− 1.368 (r46 1.517), S3T1-SM+ 1.217 (1.327), S1T1-SM− 1.171 (1.170), S1T1-PM+ 1.063 (1.070), S1T4-SM+ 1.046 (1.062), S1T4-PM− 1.022 (1.051), S1T3-SM+ 1.030. S4T3-SM+ s21 1.034 but r46 0.775 (sign flip!). S9/S4-PM fail at 0.05.
  M2_k unchanged (≤0.07%). Posted result 8879; mailed swarm-a (full-shell α cancels SM vs PM).
- Board: e best ~1.73 s21 (chiral); a's amp-x-chiral (full-shell α around e's 5f81) 1.73 / r46 2.02. b, d both on 12-shell odd orbits.
- Submitted ls1 (21): line searches + 7-dir combo x0.5/1/1.5 (ids work/ls1.ids). Generator work/mk_ls1.py (helpers SMd/PMd/terms).
- Next: read ls1; combine best α-orbit with e's best β-odd (e's best req 29d3?); request matched-density control if α winner holds r56.

## 2026-10-14 06:30 — wakeup 4
- ls1: combo7 x0.5/1.0/1.5 → s21 1.365/1.595/1.703, r46 1.366/1.761/2.065 (PASS). S1T1-SM −0.1 1.318/1.344; −0.15 1.414/1.523. S4T1-SM −0.025 1.245/1.255; −0.075 FAIL 1.33. S3T1-SM +0.025 1.169; +0.075 FAIL. S9T1-SM −0.015 1.213/1.226, −0.03 1.320/1.465. S3T1-PM −0.02 1.143/1.155, −0.035 1.154/1.238. S9T1-PM +0.015 1.044/1.119.
- Board: s21 ceiling ~1.73 for all families (b request 219c low_energies; d family ceiling-break; d request Nk=27). a's amp-x-chiral got STRONG (4aaa: 1.73/1.99/1.83/conv 1.99).
- Controls submitted (--control, s21,r46,r56): ctl for oa_S4T1_SM_m (req 3870; avg density diff ≤0.019, M2c 10.019) and combo7_x1.5 (req 5c98; diff ≤0.10, M2c 9.960). Script work/mk_control.py.
- Submitted ab1 (6): e's O1T1− β (0.05, 0.102) + combo7 α; c9 (3): slope-weighted 9-dir α combo x0.25/0.4/0.6.
- Next: read controls → post beyond-M2 verdict for α-orbit; read combos; consider coverage post.

## 2026-10-14 06:55 — wakeup 5
- CONTROLS: ctl S4T1-SM− R 0.9995/0.9994 (s21/r46), ctl combo7x1.5 0.9976/0.9974 → α-orbit gain is beyond M2. (r56 pending)
- ab1 (e's O1T1− β + combo7 α): b=0.05: x0.5 1.979/2.004, x1 2.342/2.459, x1.5 2.635/2.811; b=0.102: x0.25 2.072/2.514, x0.5 2.382/2.745, x1 2.915/3.179 (87e3). c9 slope-weighted: x0.25 1.449, x0.4 1.624/1.822, x0.6 1.760/2.208.
- swarm-a: α-SM on e's 29d3 breaks the s21 ceiling: 2fc4 (S1T1SM −0.1, S4T1SM −0.1, S3T1SM +0.1, O1T1odd 0.102) = s21 4.596 / r46 5.316. Split agreed: a = 1-D lines + controls; me = optimizer.
- geom: 2fc4 C=−1, Ωmax/mean 11 (parent 15), rel std 1.75, trace violation 0.138 (non-ideal yet huge gap).
- Launched joint-cma (hyp 05ba): work/cma_run.py, state work/cma/state.json, 12-D, λ=10, σ0=0.03, m0=2fc4. `python work/cma_run.py step` each wakeup (from work/ dir!).

## 2026-10-14 07:16 — wakeup 6
- CMA gen0: c0 (429f) s21 10.779 / s21c 10.779 / r46 10.471 C=1, PES ~3.8, R_beyondM2 1.34/1.45; geom trace viol 0.39, Ωmax 8.9. c3 6.07/6.41, c7 4.67/5.08, c9 2.04/2.49; 6/10 FAIL.
- Advanced CMA → gen1 (σ 0.0285). Ray 2fc4→c0 t=0.5/1.25/1.5 submitted (work/ray0). Control for c0: req f21d (avg density differs up to 0.78! M2c 9.50).
- a's leaders now ~5.95/6.31 (5a25). Posted result for c0.

## 2026-10-14 07:35 — wakeup 7
- 429f: r56 9.684 PASS, conv46 10.472 PASS → broker claim STRONG. Control f21d: s21 0.9892, r46 0.9872 → beyond M2. Posted claim f286.
- CMA gen1: best 56ea s21 12.675 / r46 11.608; c2 241d 10.51/10.69; c9 c550 9.56/10.18; 7/10 PASS. Advanced → gen2 (σ 0.0293).
- Ray 2fc4→429f: t0.5 7.74/7.97, t1.25 11.90/11.53, t1.5 12.71/12.33; t2.0 submitted (c12e; Σ|α|=2.43 near edge 2.5); t2.5/3 rejected (boundary). Optimum likely on search boundary Σ|α|≤2.5.
- b: lead12 (12-shell gradient at 429f), best 11.87 s21. d: robustness basin probe of 429f. a: greedy combos around 2fc4.
- table.py is slow now (~2 min); use targeted swarm show instead.

## 2026-10-14 07:55 — wakeup 8
- 3b76 (ray t1.5) STRONG 12.706/12.327/12.140/conv 12.331. ray t2.0 c12e 13.535/13.138 (r56 pend). t2.5/3 refused (Σ|α|>2.5). 56ea 12.675/11.608/11.422.
- CMA v1 gen2: 10/10 PASS best 11.78 → closed v1 (did not advance).
- b lead12: 12-shell α-even slopes large (J13R1o1 +2.41/0.03 ...), decoded exactly via work/decomp.py (subtract 429f entries). a lead6 probing 6-shell outside span at 3b76 (best s21 13.90).
- Launched CMA v2: work/cma2.py (20-D, repair to Σ|α|≤2.45, Σ|β|≤1.95), state work/cma2/state.json, mean=3b76, σ0 .02, λ12. Step: `python cma2.py step` from work/.
- work/rs.py = fast status for given ids.

## 2026-10-14 08:16 — wakeup 9
- CMA v2 gen0: best 13.10 (mean 3b76 12.71); closed v2 (12 evals).
- Control for 3b76 submitted (cccd; avg density diff up to 1.0, M2c 9.32), on e's request.
- a's greedy lead6 combos: 0da0 (C3) s21 15.86; b's abf0 15.77/14.61. a's slopes: S16T1-SM−, βodd S3T3−, PM S3T3+, βodd S12T1−, SM S4T3+, SM S9T3+, ...
- d: decomposition of 3b76: α alone FAIL, β alone 4.47 AMBIG, together 12.7 → synergistic.
- Launched CMA v3 (work/cma3.py): entry-space trust-region CMA, base=0da0, 30 coords = exact probe deltas (a 10, b 8, c 12), λ14, σ0 .5 step, elitist rebase, repair Σα≤2.45. coords in cma3/coords.json. init timed out once (5 subs), re-run in background (same seed → same hashes). `python cma3.py step` (slow: run in background); `python cma3.py rebase REQ`.

## 2026-10-14 08:42 — wakeup 10
- a critique 8a9b: s21-selected optimizers overfit (0da0 15.86 vs r46 13.52). d started min-es (min(s21,r46)) around abf0. abf0 (b) STRONG: 15.768/14.615/14.658/conv 14.655 — best by min.
- Switched cma3 fitness → fitness_min (min s21,r46; waits for r46). base_f reset 0da0 = 13.52. After gen0: rebase to higher of gen-best and abf0 (manual: `python cma3.py rebase 20261014T075054.594Z_swarm-b_req_abf0`). NB rebase mid-gen breaks y consistency → only rebase right after update.
- Control for abf0 submitted (b96f; M2^(k) 10.39, M2c 9.50). I own headline controls (a agreed).
- a's request 091f to human: widen Σ|α|≤2.5? pending.
- v3 gen0 → best 0bd5 min 15.90 (17.17/16.42/15.90), 763d 15.65; fixed C1 clip bug; gen1 submitted (see cma3/step1.log). Posted f672.

## 2026-10-14 09:06 — wakeup 11
- Controls: 3b76 cccd 0.985/0.982; abf0 b96f 0.995/0.993 (r56 pend). Posted control table (all beyond M2).
- v3 gen1 (base 0bd5): s21 so far 12.65, 11.22, 13.35, 17.31, 17.66, 16.28 ... awaiting r46. a & b probing slopes at 262f (= same hash as my 0bd5). a's s21 up to 17.66 (4ea8).

## 2026-10-14 09:22 — wakeup 12
- 0bd5 STRONG: 17.171/16.418/15.904/conv46 16.348 (best by min). Claim a609 posted; control d4a0 submitted.
- v3 gen1: 10/14 done, best 16.397 < base 16.418 → plateau near 0bd5. d's min-es plateau at abf0; a's outer slopes at 262f +1-3%.
- Posted orbit-amp coverage (counts approx: 78 evals, 56/0/22).
- Next: finish v3 gen1 → gen2 (maybe last 1-2 gens); joint-cma coverage; consider swarm done when plateau confirmed + controls land.

## 2026-10-14 09:44 — wakeup 13
- v3 gen1 complete: 13/14 PASS, none > 0bd5. 0bd5 control d4a0 0.995/0.992. All other agents closed/waiting.
- Closed joint-cma with coverage (74 evals, 61P/13F). Waiting on human reply to a's Σ|α| request 091f; if nothing new next tick → swarm done.

## 2026-10-14 10:15 — wakeup 14 (final)
- No human reply on 091f. b done; a/d/e waiting. Ran `swarm done` with summary. Loop stopped.
