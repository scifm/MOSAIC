# swarm-f notebook

Started 2026-10-15T04:13:09+00:00.

## 2026-10-15 wakeup 1 (04:20–04:27 UTC)
- Read charter, docs 40/46, kdep_envelope, board. Board: swarm-a w3-atlas (small α/β all 30 dirs), swarm-b w3-joint (joint (G,R) classes + chiral |G|²=7 at ±0.1),
  swarm-c w2-atlas, swarm-e w3-bigamp (large α ±0.3/0.6 + M2^(k)-law hypothesis — I had prepared the same idea; dropped it to avoid duplication; my unused batch in work/batchA).
- Budget is per-agent quota (500 each) as far as I can tell ("checks the agent's quota", ADR-0037 item 4).
- Free findings (work/alias.py, work/symcl.py): s21 = {(5j mod 21, j)/21} has C6 and NO mirror (chiral); r46/r56 only C2.
  F_T moments: |R|²=3 two-valued on s21 (⟨F³⟩=2.04 vs 0.816); |R|²=4 aliased on r46 (⟨F²⟩=1.333). |R|²=1 faithful everywhere.
  Linear response: full stars steepest at 1st order on C6 clusters; chiral pairs A/B (two C6 orbits of 12-member class) are M·T-equivalent
  in infinite system (amplitude: A,α ↔ B,α; phase: A,β ↔ B,−β); S00 check 1e-15 with k→Mk (swap m,n).
- Posted note 20261015T042542.993Z_swarm-f_note_f8ce, hypothesis 20261015T042640.924Z_swarm-f_hypothesis_4586 (family w3-fsfloor), mailed swarm-b.
- Submitted 25 requests (work/batchF; req ids 20261015T0426(45..55)Z_swarm-f_req_*): chiral pairs |G|²=7 (±0.3,±0.6), 13 (±0.3,+0.6), 19,21 (±0.3), phase |G|²=7 A+0.15/B−0.15/B+0.15, all ×T1.
- Tools: work/mk.py (build(parent, [(s2,t2,α,β)]), diag → M2k, S00 cond), work/mkF.py (chiral orbits).
- NEXT: when results land, tabulate |R(A)−R(B)| vs α, shell; post result with coverage block. Then pick a search family
  (ideas: use floor to set a meaningful s21 threshold; critique others' s21 positives against floor; T1-only robust designs).

## 2026-10-15 wakeup 2 (04:48–05:00 UTC)
- My 25 fsfloor evals: ALL FAIL (chiral |G|²≥7 orbits at |α|≥0.3/|β|=0.15 kill Laughlin). Pairs agree ≤2% mostly; S21+0.3 25%, S7 phase 13%.
  Posted result+coverage 20261015T045007.611Z_swarm-f_result_c45f (family closed). Laughlin-state floor ≲0.6% per b and g.
- BOARD: big positive found. S1⊥ joint class (G⟂R, |R|=ℓ²|G|, S1×T1) on w3:
  α/pair 0.05 f06f: s21 1.105 r46 1.088 r56 1.092 conv 1.088 (robust_positive);
  0.1 j_6139: 1.220/1.182; 0.2 j_7d04: 1.369/1.386/r56 1.306/conv46 1.386 (STRONG); 0.3 j_8e11 1.235/1.204.
  Leaders ~1.37-1.39 s21 (b combos, e nematic C2, h chiral β on top of S1⊥ α0.2). S2⊥/S3⊥ lose (~0.94-0.99).
  ~8 agents (d,l,m,n,o,p,q,r) on matched-density mechanism controls → herding on controls. j asked human whether LL-mixing emulation counts.
- Reconstructed S1⊥ in work/perp.py (perp_spec((a1,a2,a3))); M2_k and S00 ratio match j's 7d04 exactly (validated).
- Observation: r56 retention falls with α (0.05: r56/s21 −1.2%; 0.2: −4.6%). Claims bind on r56.
- NEXT: when many r56 results land (b/e/h leaders), tabulate r46 vs r56 vs s21; post analysis (rank by min(r46,r56), which features retain at r56).
  Possibly own a "r56-robust optimum" family: fine α line + second directions, 1 charged eval each, ladder free.

## 2026-10-15 wakeup 3 (05:17–05:20 UTC)
- Board: S1⊥ 7d04 claim STRONG (j). Mechanism controls: matched ρ̄ ≈1.00–1.02 (not density); M2-matched static 1.18–1.20 < 7d04;
  uniform-LL0 parent loses (parent interference). n: static sharpening (control) reaches 1.45 @ M2=8 on s21 — interpretation question to human.
  7d04 is local max vs nematic (e), chiral l=2 (q), matched-⟂ subspace (j), 9-class complement (b). Second linear class at parent: S2∥ (|G|²=3×T1, G∥R; b a90f).
  r: S1⊥+S2∥ combos up to s21 1.505 (7935) but r46 1.364; h: chiral β on S1⊥ to s21 1.427/r46 1.461. a: CMA 14-D. d: recentre atlas at B incl (3,4),(4,3) tied.
  p posted r56 orientation artefact critique (C6-breaking points). r56 stage is the bottleneck (most pending).
- Built work/joint.py: general pair-star C6 joint classes (classes(s2,t2), class_spec(s2,t2,{d:(α,β)})); validated vs 7d04 (cond 0.7792).
- Submitted w3-atlas34 (hyp 20261015T051856.685Z_swarm-f_hypothesis_5641): (3,4),(4,3) × θ classes × α±0.05, 12 req (051857–051903).
- Spent 37/500.
- NEXT: post atlas34 result+coverage. Critique candidate: s21→r46 drop for S2∥-containing combos (r_7935 1.505→1.364, 09f8 1.452→1.413) — wait for r56.

## 2026-10-15 wakeup 4 (05:45–05:50 UTC)
- atlas34 done: all 12 <1 (0.94–0.98), odd ≤0.6%; (4,3) three classes identical on s21 (|R|²=3 aliasing). Posted result 20261015T054753.945Z_swarm-f_result_54ec (closed).
- Board frontier: base amplitude (S1⊥ α0.2 or S2∥ α0.25) + M·T-symmetric resonant chiral β (7@49° L/R pair etc.):
  fe3d 1.69 all clusters (strong), 0672 1.43–1.46 strong, 02f7 s21 2.38/r46 2.59 (r56 pending), c89a s21 2.45. w2: df59 strong 1.16–1.21, g 141f strong.
  Static frontier (n, controls) peaks ≈1.56.
- Verification (free, work/mtinv.py): all top-25 w3 and top-10 w2 are exactly M·T-invariant → no cluster-chirality artefact. PES EG ≈4–5 flat
  from R 1.37 to 2.45 (parents ~20). Posted note 20261015T054754.715Z_swarm-f_note_916a.
  Reading another request's input: `swarm show` → 'ed_input' path → json.load (read-only).
- New family w3-phasestack (hyp 20261015T054943.193Z_swarm-f_hypothesis_0b2c): phase-only stack of M·T pairs of resonant chiral classes
  (b's 71ed/9d5f/3f32/0bda + M·T partner; work/phasestack.py, unit_pair(s), build_block). 13 submitted (054945–054956). Mailed b.
  Quadratic prediction: pairs +0.5–2.4%, stack ~+4% if additive.
- Spent 50/500.
- NEXT: fit per-pair quadratics (include b's P7 β≤0.02 data), stage-2 weighted stack; watch 02f7 r56/conv46.

## 2026-10-15 wakeup 5 (06:13–06:18 UTC)
- phasestack stage 1 (s21 / r46): P13 .01 f3d7 1.022/1.040; .02 9d9c 1.034/1.106; .03 de7e 1.035/1.163
  P19 .01 3be1 1.025/1.074; .02 059f 1.025/1.168; .03 ba09 0.989
  P21 .01 9cfd 1.029/1.103; .02 14d0 1.012; .03 0697 0.933
  P7 .03 bd8f 1.0535/1.211 (b runs P7 line 0.025–0.06; b 6826 @0.02 1.050/1.146)
  Pall .01 da6f 0.997; .015 b5e2 0.859; .02 1f10 0.663  → strong NEGATIVE cross terms.
  Note big s21→r46 increase for phase-only (r56 is the referee; o: r56<r46 in 43/45 leaders).
- Submitted 6 pairwise stacks (061646–061652): P13.02+P19.01 (0609), P13.02+P21.01 (b286), P19.01+P21.01 (ca4d),
  P7.03+P13.02 (5543), P7.03+P19.01 (034a), P7.03+P21.01 (410b).
- Board: w3 leaders now a-stack cc13 s21 3.60/r46 3.91; 02f7 strong 2.38/2.59/2.53/2.58. Convergence verified by n,i,m,q.
  Several agents finishing early (i, d) to avoid duplication.
- Spent 56/500.
- NEXT: pairwise cross terms → which pairs compatible; post phasestack result. If bd8f/de7e clear r56 ≥1.05 → phase-only robust claim (clean beyond-M2).

## 2026-10-15 wakeup 6 (06:43–06:47 UTC)
- Pairwise phase-only (s21/r46): P13.02+P19.01 0609 1.040/1.179; P13.02+P21.01 b286 1.024/1.207; P19.01+P21.01 ca4d 1.028/1.184;
  P7.03+P13.02 5543 1.010; P7.03+P19.01 034a 1.028/1.274; P7.03+P21.01 410b 1.009. → on s21 nothing beats P7 alone; P7 clashes with P13/P21.
- b's P7 line (phase-only): 0.02 6826 1.050/1.146; 0.025 225b 1.054/1.178; 0.03 f652 1.0535/1.211 (=my bd8f); 0.04 651c 1.037/1.270; 0.05+ <1.
  Phase-only s21 ceiling ≈ +5.4% at the parent; r46 grows monotonically with β (r46 inflation by chiral phases, cf. j, o).
- Board: w3 leaders s21 ~4–4.5 (a-stack, r-kshape); r56 close to r46 for leaders (s21 is low outlier). Many agents finishing early (d, g, i, m).
- NEXT: when r56/conv46 land for bd8f, de7e, 059f, 034a etc → post phasestack result (+coverage); then likely swarm done.

## 2026-10-15 wakeup 7 (07:14 UTC): no r56 yet for phasestack points (GPU queue busy). Frontier: o 90a9 s21 5.11/r46 6.04 (Σ|β| cap-limited, o asked human); a b4b8 strong 4.50/5.75/5.54/5.74. Agents p,n,m,g,d,i done. Waiting.

## 2026-10-15 wakeup 8 (07:45 UTC) — FINISHED
- r56 still queued after 1.5 h; withdrew 8 promotions incl. bd8f (≡ b's f652 to 1e-12). Kept de7e, 059f, 034a.
- Posted phasestack result 20261015T074546.515Z_swarm-f_result_c1bd (closed), mailed b. Ran `swarm done` (62/500 charged).
