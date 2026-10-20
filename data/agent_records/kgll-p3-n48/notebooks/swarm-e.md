# swarm-e notebook

Started 2026-10-14T10:24:03+00:00.

## 2026-10-14 wakeup 1 (11:12–)
- Read brief, docs 40/46, key-facts, kdep_envelope. Parent w1c Δ(s21)=2.2586e-4, r56 2.5901e-4.
- Board: swarm-a (axis-map) and swarm-b (linmap) both doing the 60-axis ±0.05/±0.03 map; swarm-c chiral joint orbits (jorb).
- Chose family `bigamp`: large-amplitude 1-D scans to boundary (5 α axes ±0.1..0.6, 3 β axes ±0.06..0.3), then 18-D Sobol on S1–S3×T1–T3, then CMA-ES. Hypothesis post 20261014T111415.911Z_swarm-e_hypothesis_567f.
- Tools: work/gen.py OUT.json 'S1T1a=0.1,...' (stars in solver 120° basis, T in 60° direct basis; chiral halves S4+/S4- etc. available).
- swarm check on S1T1a=0.1: ok, m2k_max_ratio 0.998.
- 11:17 submitted batch s1a (32: α S1T1,S2T1,S3T1 ±0.1/0.2/0.35/0.6; β S1T1 ±0.06/0.12/0.2/0.3). Batch s1b (α S1T2,S1T3; β S2T1,S1T2) waiting in work/inp/s1b for slots.
- Note: swarm check is ~30 s/input (slow); submit-batch accepts quickly and broker validates.
- Admissibility at α[S1T1]=−0.1: S min/max ratio 0.093 (fine).

## 2026-10-14 wakeup 2 (11:33)
- bigamp stage 1 result: full-star axes break manifold at |α|≈0.1–0.2 (S1), 0.1 (S2,S3), |β|≈0.12; best PASS 0.992. Posted 20261014T113443.355Z_swarm-e_result_703a with coverage. Dropped batch s1b (work/inp/s1b_dropped).
- Board: leader swarm-c jorb S2×T1 +60 β=+0.03 per entry (phase only) R s21 1.249, r46 1.404. Joint orbits are where the signal is; full stars cancel. MT symmetry: (θ,α)≡(−θ,α), (θ,β)≡(−θ,−β). ~20 agents in S1/S2×T1.
- New family orbmap2: first-order orbit map of S2×T2, S2×T3, S1×T3, S3×T1–T3 (self-dual + one chiral orbit). Hypothesis 20261014T113651.566Z_swarm-e_hypothesis_ef1d. Tool work/orbit.py ('S2T2@30:b=0.03'). Batch A (30, S3* + S2T2⊥) submitted 11:37; batch B (20) in work/inp/om2b.
- Charged so far: 32 + 30 = 62.

## 2026-10-14 wakeup 3 (11:53)
- Broker slow: none of orbmap2 batch A finished after 15 min (queued behind 48 agents).
- Heavy herding on T2/T3 orbit profiles (ar kharm, i hiT-orb, ao/av kprof, aj s2kprof). Dropped batch B (work/inp/om2b_dropped); mailed ar/i/ao/av that I own the S3 combos + S2×T2⊥ only. Replied to swarm-m.
- Leaders: ⊥ α channel (j/r/q) R s21 1.639 (M2k 9.44); chiral-odd β f e5d5 s21 1.558 r46 1.641. c d698 is "suggestive" (s21 1.249, r46 1.404, r56 1.347).
- swarm-l: conv46 ≡ r46 for pure LL0 (5e-8), so it is not independent evidence.
- Open holes (p): final verification package (p took it); inner+outer (at, an, am); large-amp non-⊥ α orbits (s, x partly).

## 2026-10-14 wakeup 4 (12:20)
- orbmap2 batch A: all 30 still pending at broker after 43 min.
- av, ar keep S3 at α ±0.05 (complementary step → curvature); i withdrew S3. OK.
- Claims: STRONG c d698 (S2×T1 +60 β .03: 1.249/1.404/1.347) and f 728b (S3×T1 odd β .05: 1.558/1.641/1.560). ⊥ α −0.45 (j ea28) 1.64/2.63/2.44.
- Critique note 20261014T122233.587Z_swarm-e_note_91cc: PES EG static control 13.4 vs leaders 4–5 vs ⊥α 2.5–3.8; flat in N. Mailed c,f,j,p. Tool work/pes.py RID... prints R/EG/split per cluster.

## 2026-10-14 wakeup 5 (12:48)
- Only 1/30 orbmap2 done after 70 min (S2T2⊥ α− 0.989). Broker congested.
- Records: t 8c01 s21 4.816 / r46 5.186; h c662 4.760/5.226/4.674 (multi-orbit α+β, S1–S3 × T1–T3, per-entry ≤0.058). EG of records 3.3–4.4, same as R~1.25 leaders → EG does not degrade with R (good). j claims STRONG α⊥ −0.45.
- c note: parent far below static M2 law (R_beyondM2 0.12); leaders restore toward it (0.72). M2-law ceiling ≈ R 8 at s21.
- Decision: do not add load; wait for orbmap2 to finish, post result with coverage. Remaining budget ~438.

## 2026-10-14 wakeup 6 (13:20)
- orbmap2 19/30 done. S3×T1 strong and follows av's angular rule (α∝cos2δ, β∝sin2δ): ⊥ α−0.03 1.287 (r46 1.307), +30 β+0.02 1.247, −30 β−0.02 1.250 (r46 1.325; MT ok 0.3%), +30 α+ 1.087. Wrong signs lose 38–44%. S3 ~3× steeper per unit than S1. S3T2 ∥ α+ 1.045. S2T2⊥ weak (α− 0.989), β asym 6%.
- Mailed av (cos2d E1 adds S3 at uniform weight) to down-weight S3.
- STRONG claims now: c d698, f 728b, j 3d0f (α⊥), h 0069 (c662 4.76/5.23/4.67), t 4fb4 (8c01). Records = cos2δ+i sin2δ rule on S1/S2×T1(+T2) (av).
- Waiting for remaining 11 (S3T2 +60 β/α+, S3T3 all) then post orbmap2 result + coverage.

## 2026-10-14 wakeup 7 (13:53)
- orbmap2 complete (30/30): posted result 20261014T135437.386Z_swarm-e_result_37a0 with coverage. (Typo: wrote ca5e prefix as 113745; real 20261014T113707.627Z_swarm-e_req_ca5e.)
- S3×T3 anti-rule (T3 opposite sign), 11% β asym on self-dual ⊥ at s21; S3T2 +60 β flips sign s21→r46.
- Records: s 9a30 s21 7.35, x d2de 7.22, o f5f1 6.28/8.33/8.12/8.33 STRONG. f5f1 has S3×T1 β but no S3×T1 α; Σ|β| 1.88/2.0 near cap; Σ|α| 1.59.
- Submitted 4 probes f5f1 + S3T1 cos2δ α (a=0.015,0.03,0.045, −0.03 ctrl): 8710 d7da 6438 9991. Tool work/addto.py BASE_REQ OUT spec.
- Charged: 62 + 4 = 66.
- p, d, ak have called done.

## 2026-10-14 wakeup 8 (14:27)
- Probes on f5f1 still pending.
- Board: records ~10 at s21 (av cos2d μ .13: 10.39; e0a8 #1), cap-limited (Σ|α| 2.3–2.5), chart-dependent caps → requests to human (t 789e, ai 7a14). u: qmax 8 non-PSD pair interaction at R≈10 (fixed at qmax 10) → conv46 will tell. ap: f5f1 γ on uniform LL0 kills Laughlin → gain is γ×ρ* cooperation. ar confirms S3×T1 ⊥ α−0.05 1.368/1.517. Many agents done (d, ak, p, g, aj, q, ae, ac).
- Plan: collect probes, post short result; then likely done unless a gap appears (don't exploit cap loophole before human answers).

## 2026-10-14 wakeup 9 (14:58)
- f5f1 + S3T1 cos2δ α: a=.015 7.224 (r46 8.895), .03 7.954, .045 8.633; split/Δ 0.027→0.003; −.03 control 3.26 FAIL. Posted result. Extending a=.06/.08/.10/.13 (f2e8 c663 5fd6 c577). Charged 74.
- Records: av e0a8 STRONG 10.39/9.87/10.50/9.96; s c325 noQ0 STRONG 9.87/10.15/9.54; h un3_B s21 11.07. Many agents done (c, au, am...).

## 2026-10-14 wakeup 10 (16:31)
- Line done: a=.06 9.26/10.26/10.03; .08 10.02/10.72/10.51; .10 10.70/11.12/10.91; .13 (c577) 11.42/11.59/11.38 all PASS. Submitted cap point a=.15 (b7a3). Posted result with coverage. Charged 79.
- Board best min R: w 407a 13.26 (STRONG), av 55f9 12.51. Above s21 R≈12 r46 gate starts binding (an). qmax caveat at R>11 (u, n).
- Next: collect b7a3 + conv46 of c577; then post final summary and swarm done (swarm saturated at cap; nothing distinct left for me).

## 2026-10-14 wakeup 11 (17:13) — DONE
- c577 STRONG (conv46 11.595, +0.04%); b7a3 (cap) 11.68/11.83/11.62, conv46 pending. Claim 20261014T171343.466Z_swarm-e_claim_ed6f. Asked swarm-k for density controls.
- Budget actually charged: 71 (earlier notebook counts 74/79 were miscounts).
- Posted final summary; ran swarm done.
