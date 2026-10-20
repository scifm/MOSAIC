# swarm-ag notebook

Started 2026-10-08T04:36:35+00:00.

## 2026-10-08 ~05:35 UTC — wakeup 1: survey + role choice
- Read brief, theory §1–3, §6.4, key-facts, decisions ADR-0032. Deformation block = sum over (pair/full) stars of
  (α/2+iβ) O_s(r) F_p(k), cos⊗cos only (sin⊗sin unrepresentable; swarm-m asked human).
- Board state: ~40 agents; leaders are the Z2-invariant achiral T1 orbits S1T1⊥ and S2T1∥ (swarm-h's half-translation
  rule: pair (m,n)x(R1,R2) invariant iff m≡R2, n≡R1 mod 2). fa76 (S1T1⊥, orbit A=0.15) s21 1.1885 r46 1.156;
  fb45 (S2T1∥) s21 1.1785 r46 1.171; ad d746 (S1T1⊥ A≈0.3) s21 1.362. Everything else concave at parent (cone at s21).
  Static M2-matched controls (ab, p) give only ~+3.5% at M2 ratio 1.05 → leaders are beyond-M2 by ~15%.
- Herding is extreme on leader directions (i, e, h, ad, ac, af, ap, b, s, t, am, aa, au, aj ...). Chose verifier role.
- Tools: work/dump.py (caches swarm show into work/cache/, slow ~1s/req, run in background), work/meta.py,
  work/perp.py (⟂-orbit builder), work/tail.py/tail2.py (kernel L1 weight outside g_cutoff box), work/reconv.py.
- Finding: low-shell orbits truncate <1e-4 at gc 8 even at A=1.0; high-shell atlas points (S6–S10 α=0.1) truncate
  1–7% at gc 8 → their collapse (R 0.1–0.3) might be numerics.
- Posted hyp `20261008T053220.260Z_swarm-ag_hypothesis_bb27` (hishell-conv-w3, ≤20 evals). Submitted 6 diagnostics:
  ac44/9955/eb6e at (64,12) and (96,16): req 8958 296d 31df 73e0 a62b 518b. Mailed swarm-l, swarm-f.
- Next: read results; if ΔR large → extend to al/w/ah/ai points + request to human about g_cutoff policy; else post
  scoped "high-shell nulls are numerically sound" result with coverage block. Then pick next gap (critique duty).

## 2026-10-08 ~05:52 UTC — wakeup 2
- hishell-conv-w3 DONE: gc12/gc16 reruns match gc8 (ΔR ≤ 6.5e-4, worst S10). Posted result 20261008T054834.059Z_swarm-ag_result_aee8
  with coverage. Collapse is physical; the out-of-box L1 fraction overstates the error by >10×.
- Tail check of top-40 w3 leaders (R 1.33–1.57): out-of-box(8) ≤ 1.2e-2 (au a61f, e0f4 worst), mostly ≤1e-3 → safe at s21.
  (Not posted separately; l covers leaders' numconv.)
- Board: w3 leaders now R≈1.4–1.57 at s21, r46 ≈1.41 (e/af plane S1T1⊥+S2T1∥); chiral β high shells r46 up to 1.54
  but r46≫s21 (k critique). Rule (swarm-g): slope ∝ Σ parent weight at offsets L = G ∓ Gc(R), Gc(R)=(R2,−R1).
- Opened rule-t1-w2 (hyp 20261008T055138.996Z_swarm-ag_hypothesis_4f7a): 10 reqs af8d 1d26 5912 46f3 c4b4 (full A −.05..0.25),
  7210 cc7f (inner .05,.15), 6a4a 0f5e 1eda (outer −.05,.05,.15). Builder work/rule_w2.py. Mailed b, g, m.
- Next: read slopes; if positive, line search along full / combine with m's best; compare to b's w3 numbers.

## 2026-10-08 ~06:10 UTC — wakeup 3
- rule-t1-w2 CLOSED (abandon 20261008T060834.518Z_swarm-ag_abandon_f92a): outer part negative slope; full loses; inner
  S1/S3×T1 gains 1.037 (A=.05, 7210), 1.095 (A=.15, cc7f) ≈ m's orbits. Duplicate of swarm-as rule-w2 (b's mail).
  Inner reqs climbing ladder free — report r46/r56 later.
- Leaders jumped to s21 R ≈ 2.0–2.5 (t xfam-gp 0e99 2.48; j chidress ba1f r46 2.23; am 08b5 r46 2.06). No r56 anywhere yet.
- Tails at gc8 for top-20 now 1.2–5%. Submitted 10 diagnostics (gc12/gc16) for e80c7, e321d, j ba1f, j c9bf, t0e99:
  e7d4 0745 8c07 6b39 4ea7 39ee 4c2a d49c 64a6 065f. Mailed swarm-l.
- Next: compare to originals; post a result (converged or not). Watch r56 for robust claims; critique duty.

## 2026-10-08 ~06:30 UTC — wakeup 4
- Leader convergence batch done: gc12==gc16; gc8 bias upward ≤0.5% ≈ 0.1×tail. Posted 20261008T062950.445Z_swarm-ag_result_be6a.
  Split with swarm-l: I check |G|²≥12-content candidates, l the low-shell ones.
- My w2 inner points: 7210 r46 1.047, cc7f r46 1.152 (r56 pending).
- r56 stalled for everyone (~95 min, swarm-c request to human). Many agents now reserve/verifier (u, w, a, l, z).
  w2 now: chidress-w2 (b) s21 1.299/r46 1.343; q runs cma-w2; ai w2-fgrad.
- Plan: low activity until r56 lands; then audit r56 vs s21/r46 for candidates with |G|²≥12 content + my own.

## 2026-10-08 ~07:01 UTC — wakeup 5
- r56 still pending for all (parents included). Swarm largely closed families → reserve (u,w,a,k,n,r,ad,ar,j) or done (ao,v).
- Notable: l/z confirm R~2 leaders converged on s21 and r46; s21↔r46 spreads are even-part (curvature) cluster effects
  (aq, an, v self-refutation). am: S2T1∥ + one chiral S4×T1 β → s21 2.41 / r46 2.63.
- Decision: hold budget (submitting more just lengthens the queue that r56 waits on). Audit r56 vs s21/r46 for
  |G|²≥12-content leaders and my w2 inner points when it lands.

## 2026-10-08 ~07:43 UTC — wakeup 6: DONE
- Posted correction note b480 (gc8 bias either sign, per swarm-z). Frontier now s21/r46 ≈ 4.39 (ap 3a0e); r56 still none.
- Ran `swarm done` (26 evals charged). Verifier niche and w2 rule-design closed; remaining work (r56 audit) is covered
  by many reserve agents.
