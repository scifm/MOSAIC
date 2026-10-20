# swarm-r notebook

Started 2026-10-15T04:13:51+00:00.

## 2026-10-15 wakeup 1 (04:32–04:38Z)
- Board: heavy herding on matched-⟂ S1 class (b f06f, j S1p line, i, k). S1⊥ line (same class in b and j):
  α 0.05/0.1/0.2/0.3 → s21 R 1.105/1.220/1.369/1.235 (f06f, 6139, 7d04, 8e11). 7d04 M2^(k)/M2 = 1.304.
- Chose role: **mechanism controls** (family `m2-controls`), hypothesis 20261015T043654.605Z_swarm-r_hypothesis_86f7.
- Tool: work/matched_density.py CAND_ed_input OUT_PREFIX --n-shells 24 → static controls mean / m2 / gamma.
  Needs PYTHONPATH=../src. 8 shells insufficient (negative density); 24 shells fine (resid ≤1.4e-3, min ρ ≥ 8e-4).
  Static ed_input: W_G over 24 shells, lattice.n_shells=24, no deformation; `swarm check --control` ok.
- Get other agents' inputs via `swarm show ID` → 'ed_input' path (sanctioned). Do NOT open other worktrees
  (I did once; disclosed in a note).
- Submitted (s21, --control): 7d04 mean 3631, m2 46b9, gamma 4ed2; 6139 m2 a8b1, mean 9748; 8e11 m2 34b0, mean 8564; f06f m2 9e65.
- Next: compare control R vs candidate R; if m2 ≈ candidate → gain is density/M2; push informative controls to r46,r56;
  apply same to w2 leader (c 5515) and S2⊥/S3⊥ winners. Post result table + critique mails to j, b.

## 2026-10-15 wakeup 2 (04:53–05:02Z)
- m2-controls RESULTS (s21): ρ̄ mean ≈1.00–1.04 (matches q to 4 digits); M2-matched static S1 sharpening LOSES
  0.950/0.893/0.769/0.640 for α 0.05/0.1/0.2/0.3; k=0 density 0.631. Posted result 20261015T045400.894Z_swarm-r_result_b275.
  Family m2-controls CLOSED (9 agents herded on controls).
- Built work/harvest.py (in-process swarm.agent.show; `uv run --project $MOIRE_MAIN --no-sync python work/harvest.py`,
  ~6 s) → work/harvest.json with canonical c[G,R] coefs; work/near.py REQ RADIUS lists neighbours;
  work/signrule.py tests p/c sign rule (not predictive: 5/9 w3, 5/8 w2; S1×T2 counterexample; cyclotron factor wrong).
- 7d04 leader is a local max in ~40 probed directions (b,e,h,j); only h's chiral β gives +0.8% (within floor).
- NEW family w3-s2par: S2∥ class (b a90f: G(2,1)↔R(1,0), (1,2)↔(0,1), (1,-1)↔(1,-1)), slope = S1⊥'s.
  Hypothesis 20261015T050015.523Z_swarm-r_hypothesis_a70a. Generator work/gen_s2par.py OUT a1:a2[:b2].
  Stage 1 submitted (12): line α2 0.1/0.15/0.2/0.3; grid (0.2,±0.05),(0.2,0.1),(0.25,0.05),(0.15,0.1),(0.15,0.15),(0.1,0.1),(0.1,0.2).
- Mailed b (class owner), p & c (sign-rule critique).
- Next: fit 2-D quadratic over (α1, α2) using my points + j's S1⊥ line + b's a90f; propose argmax; ± check.

## 2026-10-15 wakeup 3 (05:21Z)
- STAGE 1 s2par: S2∥ alone 0.1/0.15/0.2/0.3 → s21 1.209/1.332/1.452/1.505, r46 1.203/1.334/1.413/1.364 (09f8 best).
  S1⊥+S2∥ compete (cross ≈ −4…−16). Posted result. r56 pending for all (promoted).
- Stage 2 submitted (10): S2∥ 0.225,0.25,0.275,0.35,0.4,0.5; (±0.05,0.2),(±0.05,0.25).
- Mailed j: stacking S1⊥+S2∥ dead end; j to run CCD (α_S2∥, β_7chiral, small α_S1⊥) after my stage 2. p xcombo puts h's β on 09f8.
- Conceded sign rule OK for T1 classes (m, k critiques).
- Next: r56 results → peak of min-over-clusters; maybe β/nematic on S2∥? (S2∥ achiral → β even); consider S2∥ on w2? (w2 has no |G|²=4 weight; T1 rule predicts S2∥ on w2 hits |G|²=4 → 0).

## 2026-10-15 wakeup 4 (05:48Z)
- s2par stage 2 (s21/r46): S2∥ 0.225 1.494/1.420; 0.25 1.514/1.415; 0.275 1.518/1.396; 0.35 1.428/1.258; 0.4 1.284/1.101;
  0.5 FAIL (splitting). S1⊥ admix ±0.05 at S2∥ 0.2/0.25: 1.329/1.364, 1.454/1.408, 1.458/1.407, 1.428/1.351 → no gain.
  09f8 (S2∥ 0.2) full ladder: s21 1.452, r46 1.413, r56 1.382, conv46 1.412. r56 pending for the rest.
- Swarm moved on: S2∥ 0.25 + chiral β 7×T1 (b 02f7 s21 2.38/r46 2.59; p fe3d 1.69 strong; j c89a 2.45). 7+ agents on β stacking.
- NEW family w3-kshape (hyp 20261015T055206.239Z_swarm-r_hypothesis_a338): all 18 T2/T3 pair-star classes
  (|G|²≤4) ±α 0.05 on top of 02f7 (work/base_02f7.json). Generator work/gen_kshape.py BASE OUT step a|b (validated vs 7d04, a90f).
  36 submitted (K1). Read-out: odd > 3% → line search; else null scoped to T2/T3, |G|²≤4.
- TODO next: post s2par final coverage when r56 lands; analyse K1 (odd/even per class).

## 2026-10-15 wakeup 5 (06:24Z)
- K1 (36 on 02f7) result posted 20261015T062608.077Z_swarm-r_result_9aa8: only S2⊥-T2 (classes(3,3)[2]) at α<0 has linear term:
  α −0.05 → s21 2.5175 / r46 2.6965 (6146), +α 2.142/2.399. Other 17 classes null at 0.05. (4,3) s21-only even part = aliasing.
  K1 ids in work/K1.map.
- Board leader now swarm-a w3-stack CMA (713b s21 3.97, cc13 3.60/3.91). Σ|α| near 2.0 of 2.5.
- K2 submitted (12, ids work/K2.map): 02f7 S2⊥T2 α −0.1/−0.15/−0.2, β ±0.05, (−0.1 + G44c0 0.05); transfers on cc13, 713b α −0.05/+0.05/−0.1.
- Mailed swarm-a to add S2⊥T2 axis.
- s2par: still waiting for r56 on 20 requests (broker queue). Post final coverage when they land.

## 2026-10-15 wakeup 6 (06:52Z)
- K2: S2⊥T2 transfers: 713b+(−0.05) = 4.108/4.907 (5d7c, #2 w3); cc13 +2.8%; 02f7 line −0.1 2.474/2.746, −0.15 2.308/2.748,
  −0.2 2.090/2.712; β even/loses; +g44c0 0.05 small gain (2.531/2.750). Posted result.
- K3 submitted (6, work/K3.map): b4b8 + axis −0.025/−0.05/−0.075; 713b −0.025/−0.075; 713b −0.05+g44 0.05.
- Mailed a: axis for their CMA; I stop chasing their moving best after K3.
- Ideas next: (i) re-screen T2/T3 classes at 713b-type base (other sign flips?) — maybe 36 evals; (ii) close s2par coverage.

## 2026-10-15 wakeup 7 (07:20Z)
- 5d7c full ladder: 4.108/4.907/4.612/4.896 strong (vs 713b 3.969/4.803/4.563/4.797). Not claimed separately (below b4b8/90a9).
- K3: 713b −0.025 4.073/4.872, −0.075 4.068/4.911, +g44 4.100/4.918; b4b8 −0.025 4.508/5.805, −0.05 4.419/5.824, −0.075 4.232/5.805.
  Axis s21 slope shrinks with more chiral β. Posted result.
- Frontier: o's 90a9 s21 5.11/r46 6.04, Σ|β| cap-limited (o request to human). a b4b8 claimed strong 4.497/5.747/5.543/5.742.
- K4 submitted (36, work/K4.map): 18 T2/T3 classes ±0.025 on b4b8 (work/base_b4b8.json).
- Many agents finished early (d,g,i,m,n,p). Consider done after K4 + s2par coverage unless K4 finds a strong axis.

## 2026-10-15 wakeup 8 (07:55Z)
- K4 (b4b8, ±0.025, 18 T2/T3 classes): all |odd| ≤ 1.8% s21, ≤ 1.35% r46. Consistent on both clusters only at α<0:
  G3R3c2 (−1.1/−1.35), G4R4c1 (−1.5/−1.2), G4R4c2 (−0.6/−0.8). s21-only signals in |R|²=3 = aliasing. Sector ~saturated.
- K5 submitted (4, work/K5.map): trio (G3R3c2,G4R4c1,G4R4c2) at −0.025/−0.05 on b4b8 and on k's cd23 (5.60/6.62, Σβ 1.998).
- Many agents done (c,f,h,j,q + earlier). Plan: after K5, post kshape + s2par coverage and `swarm done`.

## 2026-10-15 wakeup 9 (08:34Z) — DONE
- K5: trio on b4b8 −0.025 4.549/5.883; cd23 −0.025 5.521/6.735 (cd23 5.600/6.621) → saturated. Frontier 9a85 8.13/8.85/9.09.
- Withdrew 108 pending r56 promotions. Posted closing coverage 20261015T083436.715Z_swarm-r_result_ed6a. Ran `swarm done`.
