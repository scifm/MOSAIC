# swarm-j notebook

Started 2026-10-15T04:13:23+00:00.

## 2026-10-15 wakeup 1 (04:24–04:31 UTC)
- Read board: a w3-atlas (separable), b w3-joint (joint (G,R) classes), c w2-atlas, e w3-bigamp,
  f w3-fsfloor (cluster aliasing: T2 skewed on s21, T3 aliased on r46; s21 chiral), g w3-chiral-phase
  (MT symmetry: β-response even on achiral directions in TL).
- swarm-b req f06f: S1×T1 G⊥R class α=0.05 → s21 R=1.105 PASS (heading to r46).
- My idea: R_G = ℓ²ẑ×G is a lattice vector (one flux/cell; ℓ²|G1| = a). e^{iG·X} on Bloch ψ_k = e^{iσk·R_G}.
  So e^{iG·r}e^{-iσk·R_G} = cyclotron op e^{iG·η}: effective LL mixing. Solver labels: G=(m,n) ↔ R_G=(n,-m).
  Chart is even-even (cos·cos) → contains co-moving + counter-moving halves equally; sin·sin unreachable.
- Posted hypothesis w3-perp (c495), request to human (9d01: odd-odd sector + does LL-mixing emulation count),
  mailed swarm-b.
- Submitted stage A (31): work/A/*.json, generator work/gen_perp.py. S1⊥ α∈{-.1,-.05,.1,.2,.3,.45,.55}, β±.05,±.1;
  S2⊥,S3⊥ α∈{±.05,±.1,.2}, β±.025,±.05; control S1×2R_G α .05,.1.
  Boundary: S1⊥ α=0.6 → M2k ratio 3.175 (>3), binding. S3⊥ barely changes M2k (1.003 at α .2).
- Next: read results; stage B joint search over (α_S1⊥, α_S2⊥, α_S3⊥) within M2k≤3.

## wakeup 2 (04:51 UTC)
- Stage A results: S1⊥ α=0.2 (7d04) STRONG: s21 1.369, r46 1.386, r56 1.306, conv46 1.386, all PASS, C=1.
  α=0.1 1.22 (r46 1.18), 0.3 1.235 (r46 1.20), 0.45 AMBIG 0.77, 0.55 FAIL; α<0 loses; β both signs lose.
  S2⊥, S3⊥ lose at all signs (prediction 1 falsified). Mismatched S1×2R_G α=.1 → 0.856 at same M2k (1.068) as S1⊥ .1 → 1.22.
- swarm-o: C6 co-moving part admixes LL6 only (not LL1). swarm-p: counter-moving half → guiding-centre harmonic at 2G.
- Many agents (a,d,l,m,n,p,q,r,o) run mechanism controls on 7d04/f06f; I won't duplicate.
- Posted claim 551d (strong, claim 1 only) and result 729b (stage A + partial coverage).
- Submitted B1 (14): S1⊥ α .15/.175/.225/.25; at S1⊥ .2: S2⊥ ±.03 ±.06, S3⊥ ±.03 ±.06, X2 (S1×2R_G) ±.05. Dir work/B1.
- Mailed i (split: I keep w3 stage B, they take w2), e (nematic theirs), l (optimum 7d04).
- Next: read B1, fit local quadratic, maybe a combined step; watch controls (matched-density) for claim 2.

## wakeup 3 (05:14 UTC)
- B1 results: S1⊥ line peaks at 0.2 (s21 .15 1.333, .175 1.363, .2 1.369, .225 1.358, .25 1.331; r46 similar).
  S2⊥/S3⊥/X2 at 7d04: all ≤ 7d04 on s21 (best 7095 S3⊥+.03 1.367, r46 1.375). 7d04 local max of matched-⊥ subspace.
- Mechanism: uniform-parent S1⊥ loses (o) → my cyclotron reading refuted; gain is parent interference (2G on |G|²=4).
  Controls: matched ρ̄ ~1.00–1.02, M2-matched static ≤1.20 → beyond M2 (a, l, m, q, r).
- Posted result ce29 (stage B1 + coverage + self-refutation). w3-perp C6 matched subspace closed.
- Leaders: swarm-h 0672 = 7d04 + chiral β on |G|²=7 orbits×T1 (A −0.035, B +0.035) s21 1.427, r46 1.461 (MT-self-partner, fine).
  swarm-r: S2∥ (|G|²=3×T1, G∥R) slope ≈ S1⊥'s; r running S1⊥+S2∥ grid. swarm-a CMA 14-D around 7d04.
- Mailed r, h, a: proposal to do a central-composite stacking design (S1⊥, S2∥, β7chiral). Waiting for replies.
- Budget used 45/500.

## wakeup 4 (05:37 UTC)
- Board: S1⊥+S2∥ compete (r). S2∥ alone 09f8 s21 1.452/r46 1.413. fe3d (p: S2∥ .25 + full-orbit chiral β) 1.69 all clusters, strong.
  b's 02f7 = S2∥ .25 + 7×T1 resonant class only (49.1° +.08, 130.9° −.08): s21 2.38 (r46 pending).
  Static sharpening (n) reaches 1.56 max; fe3d beats it. a closed 14-D CMA (7d04 local max), now w3-stack 8-D CMA.
- New family w3-chistack (hyp 02ec): on 02f7, add MT-symmetric class pairs ±0.02: 13res(16.1/163.9), 19res(66.6/113.4),
  21res(40.9/139.1), non-res 13 (43.9/136.1); base re-encoded at g_cutoff 9 (8d3b). Dir work/C1, gen work/gen_c1.py,
  class builder work/classes.py (angle convention verified vs 02f7). Sign rule: θ<90 → +β, mirror −β.
- Next: read C1; then RSM in (α_S2∥, β_7res, best extra class) after r's stage 2 + b's β line land.

## wakeup 5 (06:00 UTC)
- C1 (on 02f7 gc9 base 8d3b s21 2.367/r46 2.583): r19 +.02 c89a 2.451/2.824 (both up); r13 +.02 2.320/2.719,
  r21 +.02 2.278/2.849 (r46 up, s21 down); −β all lose; non-res 13@44 loses both. Posted result 4930.
- Board: a 10-D CMA seeded at c89a → b3f2 s21 2.881. h did same classes (d901). fe3d/0672 claims strong.
  02f7: r46 2.59, r56 2.53 (b). Converged (q, n). Huge herding on 02f7 chiral stacking — I keep only structured probes.
- C2 (8): all three resonant pairs at common x .01–.04, pairwise at .02, r19 .04. Dir work/C2.

## wakeup 6 (06:22 UTC)
- C1 ladders: c89a min 2.451 (s21 2.451/r46 2.824/r56 2.774/conv46 2.821) all PASS; 908b r56 2.659; base 8d3b r56 2.526.
- C2: s21 falls with outer chiral 13/21 (triple x .01 2.32, .02 2.01, .03 1.48, .04 FAIL) while r46 ~2.9–3.05.
  19@.04 2.384/3.062. Pairs at .02: 19+13 2.359/2.950, 19+21 2.213/3.049, 13+21 2.119/2.903.
- Posted result a7a3 (finite-size warning, coverage). Mailed a. a's CMA now s21 3.97 (713b) → my probes are superseded.
- No new submissions. Next: post r56 column when it lands; decide whether to finish (done) or find an uncovered niche.

## wakeup 7 (06:48 UTC)
- C2 r56 still pending (queue). Board: a's CMA b4b8 s21 4.50/r46 5.75; 713b strong min 3.97. a switched objective to
  min(s21, r46) after my warning. h claimed 4927 (02f7+19@67°) strong. i, d, m, g finished early.
- No new evals. Plan: post r56 verdict for C2 (which cluster is outlier), then `swarm done` unless a niche appears.

## wakeup 8 (07:19 UTC)
- r56 still queued 90 min. Frontier: a 9419 s21 5.77; k w3-bcap; o: frontier linear in λβ up to Σ|β|≤2 cap (request 752c).
  p, n, l finished. Withdrew 9 low-value pending r56 promotions (cec0 394c d90b 4a9c 8844 2ea3 13d8 685a dbcd);
  kept 7b56 and 0606 for the s21-vs-r46 verdict. Next: post verdict when they land, then final summary + swarm done.

## wakeup 9 (07:50 UTC) — DONE
- 7b56/0606 r56 still queued; they will land in the store. Most agents finished.
- Posted final summary note 7112 (coverage for both families) and ran `swarm done`. Loop stopped.
