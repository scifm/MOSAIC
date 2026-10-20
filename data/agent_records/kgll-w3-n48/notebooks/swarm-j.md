# swarm-j notebook

Started 2026-10-08T04:35:04+00:00.

## 2026-10-08 05:05 — wakeup 1: scope chosen, screen submitted
- Board at start: swarm-c atlas T1 (w3), swarm-f atlas T2/T3 (w3), swarm-b full w3 map (duplicates c+f), swarm-a atlas w2, swarm-e joint (G,R) pair orbits including the chiral joint direction for S1/S2/S3×T1.
- **Insight (my niche):** M·T selection rule. On C6v parents, full-star β → −β and chiral α → −α under M·T, so on a mirror-closed cluster only full-star α and **chiral β** have a linear response. None of the ED clusters is mirror-closed (`work/cluster_sym.py`: s21 is C6 but chiral, r46/r56 are C2 only), so any odd-in-β part on full stars is a cluster artifact.
- Family `chiral-beta-w3`, hypothesis 20261008T050331.748Z_swarm-j_hypothesis_8fb1, budget ≤ 200.
- Tools: `work/stars.py` (stars, sub-stars, joint orbits) and `work/gen_chiral.py` (inputs). Batch `work/batch1`: 18 directions (sub_S{4,7,9,10}_T{1,2,3}, jnt_S{1,2,3}_T{2,3}) × β = ±0.1, 36 requests. Ids are the first 36 in `swarm status`.
- MISTAKE: I ran submit-batch twice and got 36 duplicates (ids ≥ 20261008T050353.914Z). I withdrew them. Budget showed 20 charged, so check whether the duplicates were charged. Never re-run submit-batch to view its output.
- Mailed swarm-e (I skip their ×T1 joint blocks) and swarm-c (the β sub-stars are in my screen).
- Next: compute odd and even parts per direction from `swarm show`, then line searches on the best signed directions. Also compile the full-star ±β evenness test from the atlases (c, b) and post it as a note.

## 2026-10-08 05:25 — wakeup 2: batch1 back (all destructive), batch2 submitted
- Batch1 (36 evals charged; the duplicates were free): chiral β = ±0.1/term is very destructive. Best R is 0.70 (FAIL, sub S7×T1 −); best PASS is 0.50 (jnt S1×T3 +). T2/T3 and |G|² ≥ 13 close the gap outright. Phase curvature ≫ any slope at this step. Posted result 20261008T052234.472Z_swarm-j_result_6cce with a coverage block.
- Swarm-h's Z2×Z2 half-translation rule (w3 has only even harmonics): pair (G=(m,n), R=(R1,R2)) is invariant iff m≡R2, n≡R1 mod 2. TL-linear directions = M·T-even ∩ Z2-invariant. Only jnt S3×T3 among batch1 qualifies.
- Leaders (amplitude): swarm-i fb45/fa76, S1×T1 ⟂ + S2×T1 ∥ orbit, R ≈ 1.17–1.19 at s21, 1.156–1.171 at r46. Many agents are on it (af plane map, ac comoving, l numconv, ao/as/p/ab mechanism controls).
- Batch2 (`work/gen_chiral2.py`, ids in `work/batch2_ids.txt`): 7 doubly-allowed chiral-β directions, ci_S9/S10 × T1/T2 (invariant orbit − mirror) and ci_S3/S6/S8 × T3 (+θ − −θ), at β = ±0.02. Swarm-w covers S4/S7 × T1/T2 chiral β at ±0.03.
- Next: slope b = (R+ − R−)/(2β) and curvature c. If max gain b²/4c < 1 %, close the family with an abandon post and coverage, then pick a new role (verifier/critique, or the chiral-β dressing at the leader if swarm-am hasn't covered the doubly-allowed directions).
- TODO: the full-star ±β evenness test from the atlas data (no board-list command; I need the req ids from swarm-c/b posts).

## 2026-10-08 05:41 — wakeup 3
- Batch2 results (β = ±0.02, all PASS): S10×T1 + = 1.014 / − = 0.876; S9×T1 − = 1.027 (req_0215, promoted to r46) / + = 0.911; T2/T3 chiral are nulls (odd part ≤ 0.7 %, even part −6 to −35 %). Posted result 20261008T054039.856Z_swarm-j_result_6c11.
- **Sign rule:** gain with +β on the invariant orbit whose G→R angle is acute (ccw). It holds for S4, S7 (swarm-w), S9, S10 (mine), assuming swarm-w's angle convention matches; asked them in mail.
- swarm-w keeps the pure phase-only chiral-T1 line. S4×T1 χβ+0.03 gives s21 1.053, **r46 1.211**.
- Leaders: S2×T1∥ α orbit (swarm-af c310 α = 0.26, s21 1.518; swarm-e c3f0 α = 0.2, s21 1.452, r46 1.413).
- New family `chidress-w3`: `work/gen_dress.py` dresses c3f0 with χβ on S4/S7/S9/S10 × T1. 7 evals, ids in `work/batch3_ids.txt`: single orbits at +0.02, S4 at −0.02, all four at 0.015 and 0.03.
- Mailed swarm-al: their phase 3 is covered.
- Next: if the dressing adds (R > 1.452 at s21), run a line scan in the all-four amplitude and try it on af's c310 base (α = 0.26). Post a hypothesis before exceeding 10 requests.

## 2026-10-08 05:58 — wakeup 4: dressing works big at s21
- Dressing of c3f0 (S2×T1∥ α = 0.2, s21 1.452): χS4 ±0.02 → 1.649 / 1.264 (sign confirmed); S7 1.590, S9 1.690, S10 1.775; **all four at 0.015 → 2.031 (ba1f, PASS, ent gap 5.3, M2k unchanged)**; all four at 0.03 → 1.629. All promoted to r46. swarm-am has the same idea on c310 (2.05 at s21).
- My phase-only S9 χ (req_0215): s21 1.027, **r46 1.169**, r56 pending.
- swarm-k critique: chiral increments are r46 ≫ s21 and positive at both signs on r46, so possibly a cluster artifact. r56 decides. Accepted publicly.
- swarm-w convention confirmed: +β on the orbit with offset angle(R) − angle(G) = acute value. It matches mine.
- swarm-u is screening the remaining T2/T3 chiral-invariant orbits; I already did S3/S6/S8×T3 and S9/S10×T2. TODO: tell u.
- Batch4: line scan of all four at 0.0075/0.01/0.02 (`work/batch4_ids.txt`). Hypothesis 20261008T055720.518Z_swarm-j_hypothesis_59cc. Mailed swarm-am to split by base.
- Next: wait for r46/r56 of batch3/4. If r56 is positive, run the −0.015 sign-reversal control and a per-orbit quadratic.

## 2026-10-08 06:20 — wakeup 5
- r46 is in for all dressing points. Line scan s21/r46: 0.0075 1.80/1.82; 0.01 1.94/1.98; 0.015 2.03/2.23; 0.02 2.00/2.43; 0.03 1.63/2.63. Single orbits agree within 1 pt. min(s21, r46) peaks at ba1f (2.031). r56 is stalled for everyone (swarm-c request 20261008T061052.874Z).
- Posted interim result (β-profile). Submitted batch5: slope-weighted direction ×0.8/1.0/1.25 (`work/batch5_ids.txt`).
- Board: ap 2.92, t 2.81 at s21 (chiral dressing at higher α). Herd is on chiral dressing; reserve/verifier roles are taken by at, x, u, z (numconv of ba1f).
- Agreed with am: they keep the c310 and S1⟂ bases, I keep c3f0. e is running mixed bases with my pattern. b is dressing w2.
- Next: once batch5 and r56 land, post a coverage result for chidress-w3 and close it. Then decide whether to go reserve or find an untouched direction.

## 2026-10-08 06:47 — wakeup 6: families closed
- batch5 (weighted): s21 1.989/2.019/1.980, r46 2.106/2.241/2.402. No gain over ba1f.
- Posted the closing result with coverage for both families. I'm now in reserve/verifier mode with 437 evals unspent.
- Board: swarm-t leads at s21 3.50 (xfam-gp). r56 is stalled swarm-wide. Many agents are already in reserve (at, x, u, w, a, r, k, n).
- r56 audit targets: ba1f, c9bf, fe2e, 0215.
- Next: wake every ~30 min. When r56 lands, audit my candidates' sign agreement and post a critique of whichever leaders are relevant. If nothing new remains to try by the deadline, run `swarm done`.

## 2026-10-08 07:18 — wakeup 7
- r56 still stalled. Many agents are done (v, ak, g, i, x, o).
- Posted critique 1 (rule 11) of swarm-as fad2: the s21/r46 split is the β-even part, hidden only at β ≲ 0.01, +1.0 at β = 0.03 on c3f0. Mailed swarm-as.
- Next: keep waiting for r56 to audit ba1f/c9bf/fe2e/0215. If r56 is still stalled by about 09:00, consider `swarm done`, since the candidates stay on the ladder anyway.

## 2026-10-08 07:48 — done
- r56 is still stalled. The frontier is at s21 4.39 (swarm-ap 3a0e), and verifier agents remain in reserve. Ran `swarm done` with a summary (work/done.md). 63/500 evals used.
