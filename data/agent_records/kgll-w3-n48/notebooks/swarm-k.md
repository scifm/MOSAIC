# swarm-k notebook

Started 2026-10-08T04:35:08+00:00.

## 2026-10-08 05:05 — wakeup 1
- Read brief, doc 40 (024 pilot), doc 46, kdep_envelope. Board: atlases claimed by c (T1), f (T2/T3), b (all, ±0.05), a (w2 all). e: joint-pair non-separable.
- w3 density: min 5.0e-3, max 6.85; only even stars (S4,S12,S16): parent lives on a half-period sublattice. log rho projects on S4:S12:S16 = 1:0.300:-0.271.
- Families posted & submitted:
  - `ps-w3` (hyp 20261008T050417.145Z_swarm-k_hypothesis_519f): gamma=(a/2+ib) Σ c_s O_s F_T, T1/T2/T3, a∈{-0.1,0.1,0.3}, b=±0.05. 15 reqs (work/ps_batch1). M2k ratio ≤1.013.
  - `nem-w3` (hyp ..._11f4): pure E2 nematic, Nr (spatial nematic S1 pairs × T1) and Nk (S1 × momentum-nematic T1 pairs), α/β ±0.1. 8 reqs (work/nem_batch1).
- Posted herding note (b/c/f overlap), mailed b,c,f.
- Scripts: work/common.py (stars, template, with_block, check), work/build_ps.py, work/build_nem.py.
- Next: read results; expect nem symmetric-ish negative; if ps a<0 positive, line-search; then move to multi-term optimizer using atlas data.

## 2026-10-08 05:30 — wakeup 2
- Results: ps-w3 all negative (best 0.948 T1 a=-0.1; a=+0.3 breaks manifold); nem-w3 all negative (best 0.957). Posted result+coverage for both (…result_f70c, …result_b1b0). nem left to swarm-r.
- Board: leading direction = S1×T1 ⟂ joint orbit (G ⟂ R; = guiding-centre lock cos(G·r)cos(G·X_k), R(G)=(−n,m)) and S2×T1 ∥; Z2 half-translation selection rule (swarm-h) explains which orbits have linear slope. s21 leaders 1.50 (swarm-e a7c2, M2k 5.9); r46 holds ~1.17 (fb45). r56 pending. am: chiral β S4T1 on top of α S1T1⊥ raises 1.19 → 1.35 at fixed M2k.
- PES entanglement gap erodes with R: parent ~21, 56da 9.1, fb45 8.2, d746 5.4, a7c2 3.95. Scanning all (work/pes_scan.py).
- Swarm extremely crowded on the plane; I'm looking for a verifier/critique niche.

## 2026-10-08 05:41 — wakeup 2b (PES scan done)
- PES scan (work/pes_scan.py over 835 leaderboard ids): ent. gap ~21 only for static/matched-density controls; any k-dep deformation 3–10 regardless of R → generic non-ideality. Posted in critique note …note_5523.
- Chiral-β dressed points (am a15_chi_*, w *_chi_bp): r46 increments +13..+34% at BOTH signs vs s21 −13..+13%; invariant α leaders agree s21/r46 ≤3%. Posted critique; mailed am, w, aa, h.
- Checked: all those chiral β pair terms are Z2 half-translation invariant (m≡R2, n≡R1) → twist test trivial. Posted correction (…note_d387) and fix (…note_51ab: mirror image of chiral = −β, already measured; r56 only test). Lesson: check invariance before suggesting tests.
- Budget used 23/500. No new submissions. Next: watch r56 of fa76/fb45/6790/2ea0/8ffd; look for an unclaimed niche.

## 2026-10-08 06:09 — wakeup 3
- Board: s21 leaders now 2.0–2.5 (xfam-gp t 0e99 2.48; am 08b5 2.05/r46 2.06; j ba1f 2.03/r46 2.23) via chiral-β dressing of amplitude leaders. r56 still pending everywhere (even parent r56!).
- swarm-ae refuted my note_5523 §1 partially: at β≈0.02/entry chiral increments are odd & cluster-consistent; the both-sign r46 bump is β=0.04/entry curvature. Accepted (…note_3268).
- Submitted perpchi-w3 (7 reqs, work/perpchi_batch1, builder work/build_perpchi.py): j's chiral T1 orbits S4/S7/S9/S10 ±0.02/entry on fa76 base (S1T1⊥ α 0.0866). Note sign map: am "m" = j "+" for S4.
- Budget 30/500.

## 2026-10-08 06:35 — wakeup 4
- perpchi results (fa76 base, ±0.02 chiral): odd parts agree s21/r46 (S10 .054/.063, S9 .048/.063, S7 .033/.045); even part large and ~2x on r46 (S10 .096/.212). Posted result+coverage …result_886e. ae independently got the same (mail).
- Board: w3 leaders r46 3–4 (t 4a76 s21 3.33/r46 3.09; ap 7a96 2.81/4.07). r56 stalled ~95+ min incl. parents (swarm-c request to human). Many agents → reserve.
- Me: reserve/verifier (note posted). 30/500 used. Next: audit when r56 lands.

## 2026-10-08 07:05 — wakeup 5
- r56 still stalled (parents too). w3 s21 frontier 3.6 (t 4fee, M2k 7.44 > static calibration). Several agents done/reserve. Quiet hold; my 7 perpchi at stage r56.

## 2026-10-08 07:37 — done
- r56 still stalled; >12 agents in reserve to audit it. My families closed with coverage. Ran `swarm done` (summary in scratchpad done.md, same as board). 30/500 used.
