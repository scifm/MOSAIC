# swarm-o notebook

Started 2026-10-15T04:13:40+00:00.

## 2026-10-15 wakeup 1 (04:29–04:37)
- Read board: a (w3 separable atlas), b (w3 joint orbits), c (w2 atlas), e (big amp), f (fs floor), g/h (phase, MT), i/j/k (matched G⟂R).
- Top: swarm-b req_f06f S1⟂ class α=0.05: s21 1.105, r46 1.088 PASS. Heavy herding on matched ⟂.
- Physics: band = |χ_k>_cyc ⊗ |k>_gc. Co-moving terms (R=R_G=(n,-m) for G=(m,n)) closed algebra → exact k-indep cyclotron op;
  C6-invariant → admixes only LL n≡0 mod 6. Static parent = k-dependent cyclotron mixing.
- Built work/mk.py (matched pair-star inputs; parent=w3|w2|uniform). Uniform = W_G zero except G=0 (control only).
- Submitted (family uniform-ctrl): controls u α=+.05 (8c05), −.05 (5dbe), +.2 (3bf8), β=.1 (3160), β=.3 (de0f); diag w3 α=.05 gc6 (0d93).
- Posted note 20261015T043606.560Z_swarm-o_note_9fe7.
- Next: read results; compute Δ/Δ_LLL; decide stage 2 (avoid ⟂ optimizer herd; candidate niches: non-co-moving subspace search
  if human rules ⟂=LL mixing; w2; verification/critique).

## 2026-10-15 wakeup 2 (04:52–04:57)
- Uniform-parent controls (s21, Δ/Δ_LLL with Δ_LLL=1.8272e-4): α+.05 0.978, α−.05 0.963, α+.2 0.935, β.1 0.952, β.3 FAIL (manifold broken).
  w3 diag α.05 gc6 = 1.1050 (matches f06f). → ⟂ gain is parent-dressed, NOT LL mixing. Posted result 20261015T045327.926Z_swarm-o_result_4b50 (retracted LL-mixing implication).
- Board: j claims strong S1⟂ α=0.2 (7d04: s21 1.369/r46 1.386/r56 1.306/conv46 1.386). h phase on top 1.38 s21. w2 gain in oblique S1×T1 classes α<0 (c,g).
  7 agents doing matched-density controls (d,l,m,n,p,q,r) — herding on controls.
- Rule (p, c): term (G,R=R_{G_R}) → guiding harmonics G'=G±G_R; gain if α·w(G')>0. b's S1×T2 G∥R (both G' on |G|²=4) is even → my refinement: only T1 classes active (overlap e^{-ℓ²|G_R|²/4}).
- work/enum_res.py enumerates resonant classes; work/mk_class.py builds one joint class (G, GR) pair-star.
- Submitted batch A (family w3-resonance, 36 evals): outer shells 7..21 × T1 classes, α=±0.1; 5 resonant (7:(3,1)/(1,1), 9:(3,3)/(1,1), 13:(4,1)/(0,1), 19:(5,2)/(1,0), 21:(5,1)/(1,1)), 13 controls.
  Hypothesis 20261015T045622.166Z_swarm-o_hypothesis_dc8d. Analyse odd part ½[R(+)−R(−)] per class.
- Budget: 42 charged.

## 2026-10-15 wakeup 3 (05:17–05:21)
- Stage A results (odd part at α=0.1): 7(49°)+0.132 [7ad6: s21 1.027, r46 1.109, r56 pending], 13(16°)+0.088, 19(67°)−0.093, 21(41°)−0.038, 9(90°)+0.007;
  non-resonant on 7,9,13,19,21 ≤0.015; all T1 classes on |G|²=12,16 −0.044 (class-blind, own-shell term).
  → rule: activity 4/5, sign 2/4. Posted result 20261015T051942.800Z_swarm-o_result_d06e.
- Board: S2∥ (|G|²=3×T1, G∥R) second linear class (b a90f). n: static sharpened w3 reaches 1.45 at M2=8 (control!) — k-GLL leaders ~1.37-1.39.
  d does classes |G|²≤4 at B; l does outer ±0.05 (overlap; mailed l).
- Stage B submitted (13): B0 = S1⊥ 0.2 gc8 (55a1); B+7ach c .03/.06/.1/−.06; B+7a .06/.1; B+13ach ±.05/.1; B+7ach.06+13ach.05; 7ach alone .1/.15.
  Builder work/mk_multi.py ('G:GR:a' tokens). Mirror orbit rep: (m,n)->(n,m) for G and GR.
- Budget: 55 charged.

## 2026-10-15 wakeup 4 (05:41–05:45)
- Leader w3 now b's 02f7: S2∥ (|G|²=3×T1 G∥R) α=0.25 + 7×T1 resonant chiral β pair (orbit a +0.08, b −0.08): s21 2.38 / r46 2.59.
  w2 leaders ~1.19-1.22 (c). Many agents stacking (a CMA w3-stack, j chistack, p xcombo, l gcres stage B).
- My stage B on S1⊥ 0.2: outer classes flip sign. 13ach −0.05 → 1.480/1.433 (57fd), 7ach −0.06 1.386/1.393; +α loses/FAILs. Posted result.
- Submitted batch C on 02f7 base (work/add_to_base.py appends classes to an existing input): ff30 (base gc8), 13ach −.03/−.05/−.08/+.03 (02f2, ff60, 9767, 3595), 7ach −.05 (52a9).
- Mailed l (coordination: I take 02f7 + 7/13 amplitude).
- Budget: 74 charged.

## 2026-10-15 wakeup 5 (06:04–06:08)
- Batch C on 02f7 (base gc8 ff30 2.367/2.583): 13ach −.03/−.05/−.08 lose; +.03 s21 2.314 r46 2.664; 7ach −.05 2.302/2.619. Null on s21 → closed w3-resonance
  (result 20261015T060538.584Z_swarm-o_result_8f68 with coverage).
- Finite-size note (free): 45 multi-cluster gains, no sign change, r56 keeps 0.90–0.96 of r46 excess, r56<r46 43/45 (correction posted).
- Leaders: a's b3f2 s21 2.88 / r46 3.08 (10-D CMA, resonant chiral frame); b 8e7d 2.79/3.05. Broker queue slow (r56 promotions lag ~1h).
- Budget: 61 charged. Next: find an uncovered direction; candidates: w2 analogue of uniform/mechanism? low-|G| β at leader (MT-even only curvature).
- 06:07 Submitted w3-radial (6): scaled b3f2 (a's CMA top, s21 2.88): all×1.1 a33f, all×1.2 07a0, α×1.1 7bff, α×1.2 e373, β×1.2 dcf4, β×1.4 4c60. Mailed a.
- Structural note (unposted): no T1 class has both G' on w2 shells (w2 ⊂ √3 sublattice) → explains weaker w2 gains; w3 S2∥ hits |G|²=4 twice.

## 2026-10-15 wakeup 6 (06:28–06:30)
- Radial on b3f2: all×1.2 07a0 3.106/3.386; β×1.4 4c60 3.094/3.633; α×1.2 flat/loses. Posted result e715, mailed a.
- a's CMA leader now 713b s21 3.97 (cc13 3.60/3.91). i, d have finished (done).
- Submitted w3-ablate (4): 713b ampOnly 1e53 / phaseOnly b7cd; cc13 ampOnly 91ff / phaseOnly a604. Purpose: claim-2 decomposition.
- Budget 71.

## 2026-10-15 wakeup 7 (06:50–06:53)
- Ablation: 713b α-only 1.816/1.774, β-only 0.416; cc13 α-only 2.027/1.830, β-only 0.554 → strong synergy. Posted result.
- My radial 4c60 strong (3.094/3.633/3.686/3.650), 07a0 strong — superseded by a's 713b (3.97/4.80/4.56/4.80). Leader now a's b4b8 s21 4.50 / r46 5.75.
- Submitted 713b (λα,λβ) grid (8): 3ebe(0.5,1) 91a2(0.8,1.25) 7d52(0.8,1.45) 0374(1,.5) 7078(1,.75) e9d7(1,1.25) 90a9(1,1.45) c4c6(1.2,1.25). Σ|β|≤2 binds at λβ≈1.49.
- m, g, i, d finished early. Budget 83.

## 2026-10-15 wakeup 8 (07:12–07:14)
- Grid at 713b: λβ line (λα=1): 0→1.82, .5→2.87, .75→3.39, 1→3.97, 1.25→4.60, 1.45→5.11 (90a9, r46 6.04, w3 #1). λα 0.8/1.2 lose. Σ|β|≤2 binds at λβ≈1.49.
- Posted result 1ef8; request to human 752c (Σ|β| cap: physics or box? ask ≤6 beyond-boundary diagnostics). k runs w3-bcap (β reallocation at cap), told go ahead.
- Many agents done (d,g,i,m,n,p). Budget 79 (+8 =87?). Next: await human answer; consider in-box options only if new info.

## 2026-10-15 wakeup 9 (07:44)
- 90a9 ladder complete: 5.114/6.036/5.817/5.992 strong (superseded: a's 37c9 s21 6.21/r46 7.57; k bcap 5.94+).
- No human answer yet on request 752c. c, q, l, n, p, m, g, d, i finished. Nothing new to run in-box that a/k/r aren't doing.
- Plan: wait for the human answer; if none by next 1-2 wakeups and nothing new, post final summary + swarm done.

## 2026-10-15 wakeup 10 (08:31) — DONE
- No human answer yet; a's headline 9a85 8.13/8.85/9.09/9.04 (boundary-limited Σ|α|/Σ|β|). Most agents done.
- Replied to h (my λβ line rose on s21 too). Posted final summary via `swarm done`. Loop stopped.
