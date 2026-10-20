# swarm-ae notebook

Started 2026-10-08T04:36:28+00:00.

## Wakeup 1 — 2026-10-08 ~05:27Z
- Read board (≈60 posts) + leaderboard. Swarm is heavily herded on w3: atlases (b,c,f,g), joint orbits (e,i,z,w,ah,ai),
  Z2-invariant (h, ap tl-grad 31 orbits), plane map (af), comov/gc-lock (ac,ad), CMA/GP (s,t,o), controls (ab,p,as,ao),
  numerics verifier (l), phase (j,am,aa), w2 (a,m,n,q,u,v,x,ar).
- Deformation block: gamma = sum (alpha/2 + i beta) O_s(r) F_p(k), stars = any inversion-symmetric set (pairs {±G} allowed).
  Only cos⊗cos sector representable (swarm-m).
- Key physics (swarm-h): w3 has exact half-cell magnetic translation Z2xZ2; TL gradient lies in invariant pair terms
  (m≡R2, n≡R1 mod 2). Parent sits on a cone (|x| cost) for breaking dirs.
- Leaders (w3): S1T1⟂ |c|=0.15 fa76 s21 1.1885 / r46 1.1560; |G|²=3 x T1 (S2T1∥) |c|=0.15 fb45 1.1785/1.1712. Both invariant.
- My tools: work/harvest.py (cache all swarm show + ed_input deformation), work/summ.py, work/z2decomp.py, work/invparts.py.
- Posted note 20261008T052638.074Z_swarm-ae_note_5be8: breaking content costs ~3x more at s21 than r46; mixed cands
  r46>s21 is from breaking content, not robustness.
- Decision: no family yet; every direction I considered is claimed. Spent 0 evals. Next: watch for gaps (e.g. r56 results,
  claims to critique, w2 under-coverage), act as verifier/critic.

## Wakeup 2 — 2026-10-08 ~06:06Z
- Frontier moved: S2T1∥ α=0.2 (c3f0, s21 1.45/r46 1.41) + chiral β on S4/S7/S9/S10×T1 (swarm-j chidress): ba1f s21 2.03 / r46 2.23;
  fe2e (β 0.03) s21 1.63 / r46 2.63. All waiting on r56 (parent r56 still pending).
- Found: single-orbit chiral dressings at β=0.02 are s21≈r46 within 1pt, odd and sign-reversing; divergence only at large total
  chiral amplitude (fe2e, ent gap 3.2, split/Δ 1e-2). Posted refutation 20261008T060531.909Z_swarm-ae_refutation_4aee
  (vs swarm-k note_5523 §1); mailed k and j.
- Submitted 4 evals family chicheck-w3: fa76 (S1T1⊥ α 0.0866/pair) + χS4 or χS10 at ±0.02 (signs copied from ba1f rows =
  acute+ convention). reqs 0870 (S4+), cad2 (S4−), 018b (S10+), 059f (S10−). Goal: base-independence of the small-β
  cluster consistency. Inputs: work/b1/, builder work/mk_b1.py.
- w2 α+chiral dressing: swarm-an assigned to aq/av, so I didn't claim it.
- Budget 4/500.

## Wakeup 3 — 2026-10-08 ~06:33Z
- My chicheck results (fa76 S1T1⊥ base + χ at ±0.02): S4+ 1.2305/1.3053, S4− 1.3377/1.4306, S10+ 1.1750/1.1645,
  S10− 1.2760/1.2979 (s21/r46). The odd part is consistent across clusters but has the opposite sign to the c3f0 base. The even
  part is positive and 2x on r46, so it's cluster-specific even at small β on this base. Posted result 20261008T063231.806Z_swarm-ae_result_1497
  narrowing my refutation; mailed swarm-k (who accepted the first refutation and runs perpchi-w3, 7 overlapping reqs).
- Frontier: swarm-t 4a76 s21 3.33/r46 3.09, ap 2848/7a96 r46 3.7-4.1 vs s21 2.8-2.9. w2: swarm-b chidress-w2 8c39 1.30/1.34.
- r56 stalled ~95+ min for everyone (swarm-c request to human). Many agents have switched to reserve/verifier (at,x,u,w,a,r).
- Plan: hold budget (4/500 spent). When r56 lands: audit the s21/r46/r56 ordering vs the even/odd chiral decomposition, especially
  whether r56 follows s21 (C6-closed) or r46.

## Wakeup 4 — 2026-10-08 ~07:03Z
- r56 still stalled for everyone (parents included). swarm-k perpchi-w3 reproduced my fa76-base finding (odd part consistent, even part ~2x on r46).
- Frontier: w3 swarm-t s21 3.63 (4fee), ap ~3.45; w2 swarm-q 1.306 s21. Many agents in reserve/done.
- No action; holding 496 evals. Next: r56 audit.

## Wakeup 5 — 2026-10-08 ~07:45Z — DONE
- r56 still stalled (~2.5 h). Many agents done or in reserve; the r56 audit is covered by reserve verifiers.
- Ran `swarm done` with a summary (4/500 evals). Loop stopped.
