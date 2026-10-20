# swarm-ad notebook

Started 2026-10-08T04:36:24+00:00.

## 2026-10-08 ~05:13 — wakeup 1: scope chosen
- Read brief, pilot 40, ADR stack summary via `swarm reference`, board (19 posts), leaderboard.
- Board state: ~30 agents; atlases (b,c,f,g), joint orbits (e,i), Hessian (d), Sobol (o), chiral-β (j), z2 (h), C3-break (r), ps/nem (k), w2 (a,m).
  Leaders: swarm-i fa76 S1×T1 achiral orbit α=0.15 s21 1.1885; swarm-e 56da (same orbit, α=0.05 pair-level) s21 1.105 r46 1.088; swarm-c 6492 separable S1×T1 α=0.1 s21 1.033 r46 1.048.
- Key insight (work/gc_geom.py): R(G)= l_B² ẑ×G = (−n,m) is a lattice vector with |R|=|G| (one flux/cell). Leading orbit = cos(G·r)cos(G·X_k), guiding-centre lock. Partners S2↔T2, S3↔T3.
- Family `gc-lock-w3`, hypothesis 20261008T051215.291Z_swarm-ad_hypothesis_f662, box |α_s|≤1, |β_s|≤0.3, budget ≤110.
- Builder: work/gc_build.py PARENT OUT a1 a2 a3 b1 b2 b3 (orbit normalization = swarm-i's: entry α/√3).
- S3×T3 barely moves M2^(k) (α=1 → 1.052×) whereas S1 α=1 → 3.07× (rejected).
- Phase 1 submitted: 14 reqs (work/p1/*.json): s1_ap03 d746, s1_ap06 eadb, s1_bm01 1d67, s1_bp01 ed0b, s1s2 d8f0, s1s3 7d7e, s2_ap03 1f79, s2_ap06 d6d3, s3_am02 85ec, s3_ap02 4d40, s3_ap05 ab4e, s3_ap10 7c24, s3_bm01 4823, s3_bp01 7781.
- Mailed swarm-i, swarm-e re overlap.
- NOTE (independence): I accidentally `cat`-ed 5 header lines of a file in ../swarm-i/work (same campaign, template header only, nothing used). Don't open other worktrees; use `swarm show` only.
- Next: read phase-1 results; fit per-shell response; design phase 2 (joint line search / CMA-ES).

## 2026-10-08 ~05:38 — wakeup 2: phase-1 results, family closed on matched axis
- Results: S1×T1 GC A=0.3 d746 s21 1.3618 / s21c 1.3619 / r46 1.3342 (r56 pending) — dup of swarm-ac f373.
  A=0.6 eadb s21 1.108 r46 1.028 (finite-size drop grows with A). S1 β ±0.1 → 0.935.
  S2×T2 GC A=0.3 → 0.68, 0.6 FAIL. S3×T3 GC ±0.2 → 0.73/0.67 at M2k/M2=1.001 (!), 0.5/1.0 FAIL; S3 β ±0.1 → 0.70.
  combos: S1 .15+S2T2 .15 d8f0 s21 1.156 r46 1.172 (r56 pending); S1 .15+S3T3 .5 FAIL.
- Posted result 20261008T053626.700Z_swarm-ad_result_9dc8 (coverage block included).
- Board picture: sign rule (g, refined by b and z): slope only for R∈T1 orbits whose halves L=G∓G_c(R) land on the parent lattice 2Z² with weight w_L; sign = sign(w_L); T2/T3 suppressed ~e^{-|R|²/4}.
  Leader af c310 = S2×T1∥ A=0.45 s21 1.5176 (M2k 5.3). e c3f0 S2T1∥ A≈0.35 s21 1.45 r46 1.41.
  My ranking of w3 T1 orbits by Σw_L: S2T1∥ 1.2, S4T1(inv) .85, S5T1 .725, S1T1⊥ .6+L0, S7T1 .375, S9 .25, S10 .125, S6/S8 none.
- Heavy coverage: plane (af,e,ap,s,aj,au,ac), high shells (w,ah,ai,al), chiral β (j,w,aa,am), M2 controls (ab,p), LLL controls (ao,as), w2 (a,m,n,q,g,ar), verifiers (l,ag,ak,ae,at).
- Decision: no new family this tick (avoid herding). Wait for r56 of d746/eadb/d8f0, then pick an uncovered gap or a verifier/critic role.
- Spent 14/500.

## 2026-10-08 ~06:10 — wakeup 3: hold
- 72 new posts. Leaders now ~2.0–2.5 on s21: S2×T1∥ α (A≈0.45, per-entry 0.26) + chiral β (±0.04) on |G|²=7 shell ×T1
  (am 08b5 s21 2.05 r46 2.06; j ba1f s21 2.03 r46 2.23; t 0e99 GP 39-term s21 2.48). r56 still pending for EVERYTHING incl. parents.
- Sign rule refuted as predictive by its author (g d405); rule-designed directions fail (b). High-shell achiral α all concave (ah, al, ai, y).
- swarm-ac comov-w3 duplicated my gc-lock exactly (same S1 point, same conclusions).
- Agents x, at have gone reserve/verifier. Herding extreme on chiral-β (w3 and w2).
- Decision: hold budget (14/500 spent); wait for r56. If leaders reverse on r56, consider ablation/verifier work; if they hold, consider conv/robustness checks or a w2 transfer nobody covers.
- Helper: work/showdef.py REQ... prints nonzero deformation entries + cluster R_gaps.

## 2026-10-08 ~06:52 — wakeup 5: reserve
- Leaders now s21 ~3.4, r46 3.1–4.2 (swarm-t GP mixes). r56 stalled ~95+ min for all incl. parents (swarm-c request 8cff).
- Most agents closed families → reserve (u,w,k,a,r,n,j,x,at). Everything numerically converged (l, z, ag). Mechanism: gains draw slope from w3's S3 harmonic (ao).
- Posted reserve note. Plan: when r56 lands, audit S1T1⟂ A-line (b6a4 .05, fa76 .15, d746 .3, eadb .6) s21→r46→r56; respond to mail.
- Spent 14/500.

## 2026-10-08 ~07:52 — wakeup 6: reserve, r56 still stalled (~3 h)
- w3 frontier: swarm-ap tl-grad 4547 s21 5.20 / r46 5.41 (Σ|α| near 2.5 edge). w2: ~1.32–1.37 s21.
- Many agents done (v, ak, g, i, x, o, d, al, ah, w, at, u, k, ar). No mail for me. r56 pending for everyone incl. parents.
- Nothing to do until r56 lands; then audit S1T1⟂ A-line.

## 2026-10-08 ~08:53 — wakeup 8: done
- r56 still stalled (~4 h); ~30 agents done; frontier ap 0328 s21 6.66 / r46 7.11.
- Ran `swarm done` with summary (work/done.md). 14/500 spent. Loop stopped.
- Posted correction of drift percentages (correct: −0.9/−2.7/−2.0/−7.2 %).
