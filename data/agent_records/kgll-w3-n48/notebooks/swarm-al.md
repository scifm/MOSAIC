# swarm-al notebook

Started 2026-10-08T04:36:55+00:00.

## 2026-10-08 05:30 — wakeup 1: scope chosen, phase 1 submitted
- Board: ~30 hypotheses. Leader w3: swarm-i fa76 (S1×T1 ⟂ joint orbit, orbit α=0.15) s21 1.1885, r46 1.156 P.
  Crowded: S1–S3 joint orbits (e, i, z, ad, s), atlases (b, c, f, g), z3-w2 (q,u,v,x), M2 controls (ab, p).
- Key rules from board: swarm-h Z2×Z2 rule — TL gradient only on pair terms with m≡R2, n≡R1 (mod 2)
  (G 120° basis, R 60° basis). swarm-j M·T rule — linear α only on achiral, linear β only on chiral.
- My family `hishell-inv-w3` (hypothesis 20261008T052944.924Z_swarm-al_hypothesis_fb20): 14 achiral invariant
  joint-orbit directions on S4–S10, unit mean-square, α=±0.1 → 28 reqs submitted (work/p1, ids in submit log).
  Code: work/orbits.py (orbits, invariance), work/gen_p1.py (block builder; DIRS dict).
- Posted note 20261008T053044.556Z_swarm-al_note_1f0d: matched ⟂ orbit = ½ cyclotron-only (LL6 mixing) + ½ doubled
  displacement; mailed i, ad. Mailed h (overlap), j (phase-3 chiral β on invariant pairs).
- work/harvest.py: caches `swarm show` of leaderboard requests (slow, ~3 s each) → work/harvest.json.
- Next: read phase-1 slopes; line-search positive ones; stack on fa76 incumbent.

## 2026-10-08 05:50 — wakeup 2: phase 1 landed, family closed
- All 14 high-shell invariant achiral dirs concave (best S4T1 +0.1 → 1.0063, 4d9e). Table in result
  20261008T054811.721Z_swarm-al_result_9e38 (coverage block included). Duplicate of swarm-w/ah/ai/y (herding; I missed
  w's hypothesis by ~1 min — lesson: re-run digest right before posting a hypothesis).
- My LL-mixing note tested by swarm-as/ao (LL0 controls): cyclotron half ≲8% of leader slope; gain needs w3's S3
  harmonic (offset rule, swarm-g/b). Withdrawn in my result post.
- Board state: frontier = S1T1⟂ × S2T1∥ invariant plane (+chiral β dressings), s21 up to 1.57 (au a61f), r46 ~1.41
  (e c3f0, af 72e1). NO r56 results yet, parent r56 pending too. w3 frontier heavily crowded (e, af, ap, s, o, t, au, d, am, aa, j, w).
- Budget 28/500. Next: wait for r56; look for an uncovered niche (sign reversals at r56? M2-matched controls?).

## 2026-10-08 06:20 — wakeup 3: holding as reserve
- Leaders now: swarm-t 0e99 (⟂+∥ α + negative high-shell achiral α dressing + chiral β S4/S7×T1, ×1.25):
  s21 2.478, r46 2.4915 PASS, M2k/M2 1.29, adm ratio 0.72, PES gap 5.6. e 80c7 s21 2.15; am 08b5 r46 2.06.
- r56: ZERO results after ~95 min (parents too); swarm-c requested human. All claims blocked on r56.
- Many agents in reserve/verifier (at, x, u). Frontier crowded (t, e, am, j, s, au, ap, af).
- Decision: don't add s21 queue load; wait for r56, then critique sign changes / transfer. Budget 28/500.

## 2026-10-08 06:50 — wakeup 4: still reserve
- r56 still pending for everyone (parents included). ~12 agents now reserve/verifier; numerics of R~2 leaders converged
  (l, z, ag); M·T partners fine (n); mechanism = α·β_chiral cross term coupled to w3's S3 harmonic (j, ao).
- No uncovered niche worth budget. Holding (28/500). Next: audit r56 vs s21/r46 when it lands.

## 2026-10-08 07:20 — DONE
- Called `swarm done` (28/500 used). Reason: no distinctive niche left; ample reserve verifiers for r56 audits.
