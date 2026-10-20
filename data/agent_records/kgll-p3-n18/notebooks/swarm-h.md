# swarm-h notebook

Started 2026-10-14T05:20:09+00:00.

## 2026-10-14 05:35 — wakeup 1: orientation, family `bigstep`, Stage L submitted
- Board: swarm-a `linmap` (single product terms |α|≤0.1, |β|≤0.05, all 30 S×T pairs);
  swarm-b `jorbit` + swarm-c `jointorb` (joint (G,R) orbits; overlapping each other).
- Parent w1c: Δ s21 2.2586e-4; R_beyondM2 of parent-ish ≈ 0.12 → far off static M2 law (Δ ≈ 1.24 Δ_LLL at M2=10).
- swarm-a req_7106 (α[S1,T1] = −0.1): s21 R = 0.9918 PASS.
- swarm check M2^(k)/M2 at α=±0.6 single term: S1×T* 0.95; S2 1.06-1.08; S3 1.13; S4 1.53-1.59; S5 1.36-1.42. All admissible.
- My niche: large-amplitude regime. Hypothesis post 20261014T053130.922Z_swarm-h_hypothesis_cdb7 (~300 evals).
- Tool: work/build.py OUT.json '{"a":{"S1T1":0.2},"b":{...}}' (product stars, solver basis; spatial S1..S10, T1..T3).
- Stage L submitted: work/waves/L1 (44 reqs, 05:33): α ±0.3/±0.6 S1-5×T1; α ±0.6 S1-3×T2,T3; β ±0.15/±0.3 S1-3×T1.
- Next: collect L1 results, build table (merge with swarm-a's ±0.1 points), choose Sobol box → Stage G.

## 2026-10-14 06:00 — wakeup 2: Stage L null; pivot to joint-orbit linear sector
- Stage L: 44/44 FAIL (25 charged; dedup with swarm-e/f). Posted result 20261014T055750.117Z_swarm-h_result_bf4a + abandon …_8965.
- Board state: leaders are joint-orbit directions. c5b8 (S1T1 P c=-0.06 entry) = claim *strong* (min 1.19).
  swarm-r ac14 s21 4.44 PASS (small multi-lever combo, max|α| 0.06, max|β| 0.02, EG 3.97) -> climbing.
  swarm-i P1 line: c=-0.5 entry s21 1.88 / r46 2.65.  swarm-d 2678 (β S5T1g3_X) phase-only s21 1.61 / r46 2.22.
- MT rule (swarm-d): physically linear sector = α on mirror-even orbits (P, M) ⊕ β on mirror-odd (X).
- Many optimizers already (r xsector surrogate, n trgrad, p poolbo). Mapping: b,c,d,e,k,m,o. Controls: a,l,q. Verifier: f.
- Built work/jo.py (cells {±G}x{±R}, 72 even + 54 odd coords; same convention as swarm-r's post) —
  project(block) and build_block(acoord,bcoord); validated vs product stars (resid 1e-16) and kdep_envelope normalization.
- work/scrape.py pools leaderboard requests -> work/pool_cache.json (coords + R + verdicts).
- Idea for next family: space-filling (Sobol) design in the good orthant of the top ~10 linear-sector levers —
  global check of basins + data for the surrogate agents. Also note: R_beyondM2=1 ↔ R≈8.1 (M2·Δ_LLL/Δ_parent).

## 2026-10-14 06:10 — family `josobol` launched
- Pooled 317 requests (work/pool_cache.json). Key: ac14 (xsector) s21 4.44 / r46 4.94 PASS = 5 levers at small step
  (α S1T1g0_P −0.104, S2T1g2_P +0.104, S3T1g0_P −0.104; β S2T1g1_X −0.05, S5T1g3_X −0.05) — strongly super-additive.
- Controls (a, q): c5b8/f721 R_ctl = 0.999 → gains not averaged-density.
- Hypothesis 20261014T060407.071Z_swarm-h_hypothesis_1627: Sobol (seed 20261014) over 12-D good orthant, core box [0, 2× ac14 step],
  secondary α [0,0.1], β [−0.05,0]. Generator work/sobol_gen.py WAVE START N; coords in work/waves/S1_coords.json.
- Wave S1 (sob000–063) submitted ~06:10; ids in work/waves/S1_ids.txt.
- Next: fit quadratic + gate classifier on S1 (+ pool); wave S2 (64–127); post result.
- S1: all 64 passed check and were accepted (06:10-06:16).

## 2026-10-14 06:35 — S1 interim (42/64 back)
- s21 PASS up to 8.75 (sob040 req_53df), 6.79 (sob016), 6.74 (sob014), 6.53 (sob000), 6.50 (sob021). 18/42 FAIL (mostly split; some R 5-7 FAIL).
- Board leader: swarm-r b55a s21 10.9 (X2 line along ac14 beyond my box). ac14 r46 4.93.
- Linear log-R fit (work/fit.py S1; uses work/sobol_gen_dims.py): R²=0.96 on 24 PASS. slopes (full box): S3T1g0_P +0.77, S2T1g2_P +0.47,
  S2T1g1_X +0.24, S1T1g0_P +0.21, S8T1g4_X +0.20; NEGATIVE in combination: S1T3g0_P −0.29, S1T1g1_X −0.16.
  FAIL correlates with large S5T1g3_X, S8T1g4_X (u≈0.65-0.69 among FAIL).
- Mechanism context: swarm-q LLL-substrate: leader blocks on uniform LLL lower gap → gains need w1c density;
  swarm-f statctl / swarm-c statfront: is w1c a soft static point (Δ/Δ_LLL = 1.24 at M2 10)?
- Next: wait for all 64; decide S2 — probably shift box (drop/neg S1T3g0_P, S1T1g1_X; extend S3T1g0_P, S2T1g2_P beyond 2×), keep FAIL-prone β small.

## 2026-10-14 07:00 — S1 complete, S2 submitted
- S1 final s21: 37 P / 1 A / 26 F. Best sob040 (req_53df) s21 8.754 / r46 9.420 P (r56 pending), sob052 7.35/8.42, sob016 6.79/7.62 ...
- High-R FAILs = s21 split/Δ 0.10-0.17 (sob012 7.44 at 0.1007). S3T1g0_P small → FAIL; large β S5/S8 → FAIL.
- Linear log-R fit R² 0.90: P3 +0.81, P2 +0.50, P1 +0.31; S1T3g0_P, S1T1g1_X(β), S1T1g1_M ≤ 0 in combination.
- Posted result 20261014T070059.078Z_swarm-h_result_414a (coverage block included).
- Board: b55a (r) 10.9 suggestive→conv; swarm-i oddamp 10.76 (A−B α convex); claims strong: ac14 (r), ec27 (b, phase-only).
- S2: box2 (work/box2.py, seed 20261015): P1,P3 ∈[−.42,−.10], P2 ∈[.05,.42], βX2 [−.15,0], βX5 [−.1,0], αS1T1g1_X [−.15,.15], αS1T2g2_P [0,.1], βS8T1g4_X [−.05,0].
  63 submitted (sob034 excluded: Σ|α| 2.56 > 2.5). ids work/waves/S2_ids.txt. Charged so far ~153.
- sobol_gen.py now: python sobol_gen.py WAVE START N [boxmodule]  (run from work/); coords → work/waves/WAVE_coords.json

## 2026-10-14 07:30 — S2 results: new board-best min
- S2: 62/63 PASS s21. c954 (sob006) full ladder 11.33/11.61/11.25/11.63 (min 11.25 > b55a 10.91). f2e2 10.99/10.89/10.27/10.89.
  245d (sob059) s21 11.84 / r46 11.51 (r56 pending; swarm-l doing D1 on it). 0fb7, 24ab, dba6 ~10.5-10.9.
- Fit S2 (R² .85): βX5 +.53, βX2 +.49, P3 +.32, P2 +.17, P1 +.12 per box unit; αS1T1g1_X concave; others ~0.
  Large P3 protects s21 manifold; β drives gain. Top points at edge in βX2, βX5, P3.
- Posted 20261014T073041.785Z_swarm-h_result_aef0. Mailed swarm-l for D1 on c954, f2e2.
- Board context: swarm-a e2 pair-channel proxy predicts R (R² .97 r46); swarm-c statfront: static w3 has 2.0×/1.8× w1c gap → quote Δ/Δ_w3 too.
  swarm-b orthant factorial (second basin check). swarm-r b55a strong claim.
- S3: box3 (seed 20261016) 5-D: P1[−.35,−.05], P2[.05,.35], P3[−.70,−.20], βX2[−.35,−.08], βX5[−.25,−.05]; α shrink if Σ|α|>2.45.
  check+submit running in background → work/waves/S3_ids.txt.
- TODO: critique post (none yet, ~1 in 5 required); coverage block at family close; consider claim for c954 once controls in.

## 2026-10-14 07:35 — chiral E+ link; C1; boundary request
- swarm-k ell2 (…result_e370): gain lives in E+ = e^{+2iθ_GR} only. work/chiral.py projects per-shell E+ onto jo coords:
  S1: P −3.46λ, M(g1) +2.45λ, βX −2.12λ; S2: P(g2) +3.46λ, M(g1) −2.45λ, βX −2.12λ; S3, S5 like S1. All my good signs are E+.
  c954 ≈ E+ with λ ≈ (S1 .093, S2 .080, S3 .111, S5 .037) but missing M partners (E− admixture).
- Wave C1 (family chishell, 10 reqs, ids work/waves/C1_ids.txt; generator work/gen_c1.py): completion of c954/245d with M partners
  (+M2, +M5P5, +All; shrunk to Σ|α| 2.45 where needed) and pure per-shell E+ reconstructions at 0.5×, 0.6× (1.0× violates Σ|α|).
- Request to human 20261014T073445.184Z_swarm-h_request_8eba: Σ|α| boundary is representation-dependent (pair cells = 3× product).
- Mailed swarm-k proposing split (I take per-shell λ on inner shells).
- S3 check/submit still running in background (task by742hole).

## 2026-10-14 08:05 — S3 + C1 results; V1 submitted
- Budget 226 charged before V1 (+5 now). Remaining ~269.
- S3: 51/64 PASS. a470 (sob006) s21 13.91 / r46 12.97; 0914 (sob034) 13.54/13.06; 5c3e 13.11; 34dd 12.84/12.37 ...
  Quadratic fit (R² .78) → interior vertices (u from good end): P1 .61, P2 .88, P3 .81, X2 .46, X5 .22 → josobol optimum located (~13.5-14 s21).
- C1 (chishell): all 10 PASS. E+ completion helps: 245d+M5P5 (729e) 13.50/13.29 (from 11.84/11.51); c954+All shrunk (c5e8) 13.27/12.99;
  c954+M5P5 12.96/12.67; +M2 alone small; pure inner E+ 0.6× ~11.4 (Σ|α|-limited).
- Board: swarm-k strong claim 3bd0 outer chiral field 13.58/13.11/13.10/13.30; swarm-n chiral projection b55a−E− 12.9; l0+inner+outer s21 14.70;
  swarm-r took per-shell E+ profile (xsector/profile) — don't duplicate. swarm-k also posted Σ|α| representation request (same as mine).
- V1 (5 reqs, work/waves/V1_ids.txt): S3 vertex, vertex+M5P5, vertex+M2+M5P5 (shrunk), sob006/sob034 + M5P5.
- Plan: after V1 + ladder, close josobol with coverage; claim best min if r56/conv46 PASS (with D1 from swarm-l).

## 2026-10-14 08:35 — josobol closed
- Full ladder: 0914 (S3 sob034) 13.54/13.06/13.23/13.08 min 13.06 (broker: strong). 729e (C1 245d+S5 partners) 13.50/13.29/12.88/13.30.
  a470 13.91/12.97/13.29/… ; b2b4 (V1) 14.06/13.38/…; 1032 (V1) s21 15.00 but r46 12.33 (EG 1.87) → s21>14 overstates.
- 9 r46 FAILs (S3) = r46 splitting, low r46 EG; at small P3 / large X5.
- C1 result: removing E− on S5 orbit = +14% on all clusters → supports swarm-k's relabelling critique (all strong claims = one chiral E+ field).
- Posted closing result + coverage 20261014T083422.805Z_swarm-h_result_bb1b. Mailed swarm-l (D1 on 0914, 729e) and swarm-k (agree).
- Board frontier: swarm-n 2fb9 strong min 14.27 (E+ + negative l0 breathing), 6c70 s21 15.7 / r56 14.47. Many agents done.
- Budget: 231 charged. Remaining ideas are low-value (same mechanism). Waiting on: human answer to Σ|α| request; D1 for 0914; then claim post; then done.

## 2026-10-14 09:05 — waiting on D1
- b2b4 (V1: S3 sob034 + S5 E+ partners) full ladder 14.06/13.38/13.16/13.51 → broker STRONG, my best min 13.16.
- swarm-l D1 submitted: 0914 → swarm-l_req_2f22, 729e → swarm-l_req_aff7 (s21/r46/r56).
- Board top: swarm-n 8f40 min 15.62 strong (17.43/15.62/16.02/15.98). Most agents have posted final summaries.
- No human answer yet on Σ|α| request. Next: when D1 lands, post claim for b2b4 (+0914), then swarm done.

## 2026-10-14 09:35 — claim posted
- D1 (swarm-l): 0914 → 0.974/0.971/0.970; 729e → 0.986/0.982/0.982 (s21/r46/r56). b2b4 itself not controlled (stated in claim).
- b2b4 diagnostics: M2k/M2 1.034, S min/max .076, R_beyondM2 1.68-1.81, EG ≥ 2.39, split/Δ ≤ .037, C=1.
- Claim posted: 20261014T093133.516Z_swarm-h_claim_3ead (strong, mixed; variant of k's chiral E+).
- Only open item: human answer on Σ|α| request (…request_8eba) → would allow full-strength E+ completion test. Waiting one cycle; else swarm done.

## 2026-10-14 10:33 — done
- b2b4 D1 (swarm-l req_50a3): 0.981/0.975/0.975 all PASS, M2(ρ̄) 8.68 → claim 3ead caveat closed; posted note 20261014T103224.681Z_swarm-h_note_18fe.
- Still no human answer to the Σ|α| request (8eba) after a full cycle. Nothing left in my scope that is not the same E+ mechanism → swarm done.
- Final: 231/500 charged. Families bigstep (abandoned, bf4a/8965), josobol (414a, aef0, bb1b), chishell (in bb1b). Claim 3ead.
