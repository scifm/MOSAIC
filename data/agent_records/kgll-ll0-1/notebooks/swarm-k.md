# swarm-k notebook

Started 2026-10-02T03:51:46+00:00.

## 2026-10-02 wakeup 1 (04:07–04:17 UTC)
- Board: a=w3-atlas (star×star ±0.02), c=w3-wide (CMA-ES S1-S4×T1-T2), e=w2-map, b+f both w2-atlas (duplicate; their problem).
- Niche chosen: **joint-orbit** — split each full-star product O_S F_T (6×6 shells) into 3 C6 orbits by signed G→R angle:
  A (0/90°), P (+30/+60), M (−30/−60). Built with pair-stars {±G_j},{±R_l} and a 3×3 α/β matrix. Code: work/orbits.py
  (C6 + mirror pairing verified, work/check_c3.py).
- Symmetry argument (mirror×TR, parents real & mirror-symmetric): odd directions α_P−α_M, β_A, β_P+β_M → zero linear slope in TL;
  even: α_A, α_P+α_M, **β_chiral=β_P−β_M (phase only → beyond-M2 automatically)**. s21 is chiral (√21) → artefact allowed there.
  S00(Mk)=S00(k) checked analytically from ll0_norm formula (no k-shift under mirror).
- Cross-check: full-star α (swarm-a) ≡ 3 orbits each at c=α/3; slope_star = (sum orbit slopes)/3.
- Posted hypothesis 20261002T041316.315Z_swarm-k_hypothesis_0236; mailed c (correction: joint orbits representable) and a.
- Submitted batch1: work/batch1_w3/ 56 req, combos S1T1,S1T2,S2T1,S3T1 × {aA,aP,aM,bA,bP,bM,bCH} × ±0.02. g_cutoff 6, n_mesh 48.
- Next: when results land, tabulate slopes/curvatures per orbit (work/analyze1.py todo); test predicted zero-slope dirs; line-search β_chiral.

## wakeup 2 (04:37 UTC)
- Batch1 done, 56 PASS. Map: work/names1.txt ↔ work/status1.txt (sorted order). Key: S1T1 αA +0.02 → 1.0413 (fa1d; r46 1.0345),
  S2T1 αA → 1.0393 (3a63; r46 1.0346). P/M flat; S1T2, S3T1 dead. β_chiral concave everywhere on S1-S3 (my prediction FAILS there);
  βA (MT-odd) artefact slopes up to 0.4/unit on s21.
- Board heavily herded into orbits/chiral (g,h,d,i,j,l). d's S4T1 β-chiral phase-only: s21 1.036, r46 1.0798 (!).
- Accepted h's split: h = S1-S3 α orbit line/CMA + matched-density control. I declined β_chiral (crowded).
- Batch2 submitted: mirror-even α orbit classes on S4-S8 × T1 (|angle| classes), Frobenius 0.035, g_cutoff 10, 24 req.
  Files work/batch2_w3/, ids work/submit2.txt. Code work/orbits2.py.
- Posted result 20261002T043919.213Z_swarm-k_result_ab32 (with coverage block).
- Next: analyse batch2; if an outer-shell class has slope, combine with S1T1 αA (coordinate w/ h) and/or d's S4T1 βCH (joint α+β).

## wakeup 3 (04:59 UTC)
- Board exploded: w3 leaders s21 1.6 / r46 1.71 (o 968b: α S1T1⟂+S2T1∥ + chiral β S4/S7/S13, large amp). c 776c pure S2T1∥ Frob 0.45: s21 1.5175, r46 1.409, M2_k 5.30 vs 3.63.
  b's critique: S1T1⟂ (R=ẑ×G l²) is half static coherent LL mixing; S2T1∥ is LL-free. n: matched-density controls for h/6e88 explain ≤1.9% of 13.5%.
- Batch2 (outer α classes, ids work/submit2.txt) → live: S4T1 49.1° (+0.75/Frob), S7T1 16.1° (+0.92/Frob). Others concave. Posted 20261002T050201.955Z_swarm-k_result_69cb, mailed o.
  CAUTION: earlier paste-based mapping was wrong; always join on req id (work/status_all.txt).
- Batch3 (14 req, work/submit3.txt): far lines S4a49/S7a16 Frob 0.10–0.45 + stacks on c/776c (F 0.10, 0.20, single & both). merge util: work/merge.py (pair stars only).
- fa1d/3a63 at r56 stage (r46 1.0345/1.0346).
- Next: read batch3; if stacking helps, refine (2-D scan on top of 776c / o's LL-free leader); consider w2 transfer of outer α classes.

## wakeup 4 (05:23 UTC)
- Batch3 result: outer α classes concave beyond F~0.05; stacking on 776c subtracts (1.52→1.23/1.31; both → FAIL). S4a49 F0.45: R 2.18 PES FAIL (other phase).
  Posted abandon 20261002T052545.130Z_swarm-k_abandon_42f4 (coverage). Mailed o (they stacked my α49/α16 in b3).
- Board leaders: o 48bf s21 2.62 (confirm21), p cc86 s21 2.40 / r46 2.47 (LL-free: α S2T1∥ 0.3175/entry + chiral β |G|²=13×T1 0.0367). r56 is the bottleneck (2 lanes).
  i: selection rule a_{G+Gp} = −R → live orbits carry k-indep (LL-mixing-type) content; b requested human ruling on LL mixing.
- Herding: everyone on α S2T1∥ + chiral β. My orthogonal probe: T2 harmonic (S2×T2 α classes 30°, 90°) on top of cc86, F ±0.1, ±0.2 (8) + cc86 re-merged sanity (061b). ids work/submit4.txt.
- Budget: 94 + 9 = 103 charged.
- Next: if T2 helps at the leader → refine; else post null and consider verifier role (conserve budget).

## wakeup 5 (05:46 UTC)
- Batch4 (T2 on cc86): S2T2 90° (⟂, Q=0 half) live: F −0.2 → 13f5 s21 2.6375 / r46 2.709 (PROVISIONAL per human dee8 & f's critique 2c0b). 30° class dead.
  Remerged cc86 (061b) reproduces p exactly (r56 2.4564, conv46 2.4692) → merge.py OK.
- work/qrule.py: i-rule (a_{G+Gp}=±R, Gp ∈ parent support ∪ {0}) fits ALL my measured live/dead classes. Predicts Q0-free T2 live: S4T2 40.9, S5T2 ∥, S7T2 73.9.
- Batch5 (10 req, work/submit5.txt): those α classes F ±0.1 + chiral β S4T2/S7T2 ±0.05 on cc86. Pre-registered in result 20261002T054819.071Z_swarm-k_result_a1b7.
- Human: new tools --diagnostic (no promotion), --control --clusters, withdraw. r56 queue by priority.
- e: chiral-β alone (α=0) loses → β gain is α×β interplay. o: bd1a r56 2.567.
- Budget ~122 charged.
- Next: evaluate batch5 vs prediction; if live, combine best Q0-free T2 classes on cc86 (LL-free improvement); posts to keep provisional label on 13f5.

## wakeup 6 (06:09 UTC)
- Batch5 pre-registered test PASSED 4/5: β-chiral S4T2 40.9 (+.05: 5e11 2.642/2.666) and S7T2 73.9 (+.05: e4b0 2.644/2.660) at identical M2_k; α S7T2 −0.1 (990b 2.639/2.542, M2 down). S5T2 weak. eg rises with gain.
- Posted 20261002T061100.855Z_swarm-k_result_5c77. Mailed i, p. Withdrew 15 dominated requests from the ladder (incl. 92be, f96f).
- Claims on board: p cc86 STRONG (provisional), o bd1a STRONG (prov), d 2400 robust_positive (phase-only!). New top: h fea3 s21 2.80 / r46 3.59.
- Batch6 (8 req, work/submit6.txt; lib work/t2lib.py): combos on cc86 of βCH S4T2/S7T2 (0.05, 0.10), +α S7T2 (−.05, −.1, −.2), +α S4T2.
- Next: if combos add, port the best T2 increment onto current top leader (h fea3 / o b7cb) and check r56.

## wakeup 7 (06:32 UTC)
- Batch6: T2 combos subadditive; single βCH T2 0.05 optimal (e4b0). Posted 20261002T063450.692Z_swarm-k_result_3529. Withdrew 9 dominated.
  Kept T2 candidates: 5e11, e4b0, 3a06, 13f5 (prov).
- Board: top w3 h fea3 2.80/3.59 (cc86-type + S1T2∥); p w3-sobol global map incl. my T2 betas; f: parents' r46 gap 4.1% low → r46 R inflated 4%.
- Batch7 (18, work/submit7.txt): w2 Q0-free T2 classes (rule w/ w2 support: S2T2 30, S5T2 0/60, S6T2 30/90; work/qrule_w2.py) on g/0f4e (α ±0.05, βCH ±0.03);
  + fea3 + βCH S4T2/S7T2 0.05. Hypothesis 20261002T063344.943Z_swarm-k_hypothesis_d453.
- Budget ~146 charged.

## wakeup 8 (06:56 UTC)
- fea3 + βCH S4T2 0.05 → **435c s21 3.472 / r46 3.835** (fea3 2.80/3.59), 1684 (S7T2) 3.325/3.785. Same M2_k 7.57. Likely w3 #1.
- w2 T2 on 0f4e (s21 1.261): c6a8 S5T2a60 −.05 1.333, 8292 S6T2a90 +.05 1.332, bd8e S6T2a30 +.05 1.329; several up at both signs. Withdrew 10 weak.
- Lanes on w2 (b's proposal, accepted): b = α classes, r/g = β retune, h = gradients, **k = Q0-free T2 β**.
- Batch8 (7, work/submit8.txt): fea3 S4T2 βCH 0.03/0.08/0.12 + (0.05 + S7T2 0.03); w2 0f4e βCH S5T2 60 ±0.06, S2T2 30 +0.06.
- Posted 20261002T065757.526Z_swarm-k_result_d4ff. Mailed b, h. Claims on board: c 776c STRONG, h d49b STRONG, p cc86, o bd1a (prov), d 2400 robust.
- Budget ~163.

## wakeup 9 (07:19 UTC)
- fea3 S4T2 βCH scan s21: 0.03 3.247, 0.05 3.472 (r46 3.835), 0.08 3.727, 0.12 3.817 (eg 3.8), 0.05+S7T2 0.03 3.622. Still rising → batch9 widening: 0.16, 0.22, 0.08+S7T2 0.05 (work/submit9.txt).
- w2 T2 gains s21-only (r46 below base 1.338) → abandoned (20261002T071958.869Z_swarm-k_abandon_8668), withdrew 9. Mailed b.
- New claims: r e064 (w2 phase-only STRONG), l 9fcb (w2 phase-only STRONG), g 98ec (w2 prov). c and m done.
- Budget ~148.
- Next: r46 of 7966/cd46 and the widening; pick the best min(s21,r46) and let it climb to r56/conv46. Owe a critique post.

## wakeup 10 (07:41 UTC)
- fea3 S4T2 β scan: optimum 0.08 → **7966 s21 3.727 / r46 3.832 / r56 3.785** (conv46 pending → STRONG if ≥1.10). 0.12 overshoots on s21 only.
  Posted 20261002T074? result (res7). Withdrew 435c, 1684, 941e, cd46, 60b1, 6e20, 9438, 13f5. Kept 7966, 35d0, 5e11, e4b0.
- Batch10: 7966 + α S7T2 −0.05/−0.10 (work/submit10.txt).
- h asked: post conv46−r46 shift for 7966 (qmax check).
- o, c, m done. p sobol f9e2 s21 3.81.
- Budget ~150.

## wakeup 11 (08:09 UTC)
- **7966 STRONG** (s21 3.727 / r46 3.832 / r56 3.785 / conv46 3.787, C=1, split/Δ ~4e-2, eg ~4.5); 35d0 STRONG too. Posted claim 20261002T081029.559Z_swarm-k_claim_3d10 (provisional, parent-harmonic static content like cc86).
- 7966 + α S7T2 −0.05 → b2d5 3.792/4.030; −0.10 → 3d90 3.903/4.222 (split/Δ r46 0.024). Batch11 widening −0.15/−0.20/−0.30 (work/submit11.txt).
- Lanes with h: h re-tunes T1 α at 7966 (181c s21 4.007!), me T2 α. Mailed h.
- e audit: top tier R>3 split/Δ 4–9%; robust tier (≤1e-2) best cc86.
- Budget ~155.

## wakeup 12 (08:36 UTC)
- α S7T2 line on 7966: −0.15 ac08 3.994/4.404; **−0.20 feba 4.120/4.556 (split/Δ r46 0.010)**; −0.30 3.658/3.845. Withdrew b2d5, 3d90, 9948.
- Batch12 (work/submit12.txt): −0.25; β S4T2 re-tune 0.05 / 0.11 at α −0.20.
- h stacks T1 α (S1T2∥ +0.03, S2T1∥ +0.05) on my bases; told h feba is new base.
- Posted critique of p's afbb (split 0.094 at conv46, conv shift −2.8% ∝ M2): 20261002T083702.424Z_swarm-k_refutation_a439. Mailed p.
- q, f, j, o, c, m done. Budget ~158.

## wakeup 13 (09:03 UTC)
- Batch12: 459c (α S7T2 −0.20, β S4T2 0.05) s21 4.111 / r46 4.603, split 5e-3, eg 4.7 — best min. feba 4.120/4.556. −0.25 and β 0.11 worse.
  Withdrew ac08, 0e27, 2b32. Posted result (res8). h's a965 (3d90 + T1 α) 4.336/4.327; h re-stacking on feba (9ad3 s21 4.37).
- d, e, p done (p accepted my critique a439). Remaining active: a, b, g, h, i, k, l?, n, r.
- Waiting: r56/conv46 for feba, 459c → claim if strong. Budget ~158.
- batch13 (8, work/submit13.txt): phase-only T2 βCH on d/e25f (S4T2 ±.03/±.05, S7T2 ±.03) + parent+S4T2 ±.03. Phase-only = beyond-M2 by construction.

## wakeup 14 (09:30 UTC)
- Phase-only T2 on d/e25f: null on r46 (c5fe 1.065/1.136 vs e25f 1.054/1.175); parent+T2 β concave → abandon 20261002T093054.617Z_swarm-k_abandon_2c79. T2 β gain = α×β cross term.
- h: 9ad3 = feba + S1T2∥ +0.03 → 4.370/4.626 (w3 #1); S2T1∥ hurts r46 on feba. h also stacked on 459c (edc0).
- Batch14: β S4T2 re-tune on 9ad3 → 0.05 (5687), 0.065 (686f).
- a done. Still waiting r56/conv46 for feba, 459c (r56 queue slow per n's request 2dbb).
- Budget ~174. Plan: after batch14 + r56 of 459c/feba → claim if strong, final coverage, swarm done.

## wakeup 15 (10:02 UTC)
- 686f (9ad3, β S4T2 0.065) 4.3945/4.6121 — best min on board, marginal. Withdrew 5687, feba. Waiting r56 for 686f, 459c (and 9ad3 is h's).
- Posted result (res9). Recipe converged. Nothing left in my lane worth budget → after r56/conv46: claim (if strong), final coverage, swarm done.
- 10:33 quiet: r56 still pending for 686f, 459c, 5e11, e4b0. r, l done.

## wakeup 17 (11:24 UTC) — DONE
- 686f STRONG 4.3945/4.6121/4.4115/4.6106 (best min on w3); 459c STRONG 4.111/4.603/4.325/4.618. 5e11/e4b0 r56 2.58/2.56 > cc86 2.456.
- Posted claim 20261002T112442.461Z_swarm-k_claim_e5ed. Ran `swarm done` with final summary + coverage. Stopping loop. 165/500 charged.
