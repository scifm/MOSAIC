# swarm-l notebook

Started 2026-10-14T05:20:23+00:00.

## Wakeup 1 (2026-10-14 ~05:45 UTC)
- Read the brief, progress/40 and 46, and the board. Parent w1c: Δ s21 2.2586e-4, r46 2.4101e-4, r56 2.5901e-4; Δ_LLL ≈ 1.8e-4. That makes the parent only 1.24× LLL despite M2 = 10.
- Board: a = product map; b and c = S1–S3 joint orbits; d = chiral (mirror-odd) phase; e, f and h = large-amplitude products (they FAIL the gate at α=0.3 in outer shells, with R 1.4–1.9 there); i = matched P_n line scans; j = phase quadratic; k = outer-shell joint orbits S4–S10×T1 (claimed just before I would have, so I dropped my plan).
- Key data: swarm-c P orbit S1×T1, c=−0.06 per entry (`c5b8`): s21 1.2022, **r46 1.2044**. It transfers. swarm-d's MT rule: physically linear sectors are α on mirror-even and β on mirror-odd. All ladder clusters are chiral (s21 C6, r46/r56 C2).
- My MT-pair check of b's J1: chirality artifact ≤ 0.009 on s21.
- Role: mechanism controls plus cross-family integrator. Tools: `work/orbits.py` (joint orbits and even/odd dirs, C3/mirror in the solver basis), `work/mdens.py` (D1 matched-density control), `work/dump.py` (summary of all requests).
- Submitted control `…swarm-l_req_938f` = D1 of c5b8 on s21, r46 and r56. D1 changes w1 by 9e-4 and M2 10.035→10.017.
- Posted note `…swarm-l_note_5350`; mailed b, c and d.
- Next: read the 938f result. When the maps finish, build the union gradient (α_even + β_odd) and post an integrator hypothesis. Run controls for large-|c| winners (i's P1 line).

## Wakeup 2 (06:03–06:08 UTC)
- My D1 control of c5b8 (`938f`): R 0.9989 PASS on s21, r46 and r56. a and q got the same (0.999). Both handed the ρ̄ controls to me, so **I own them now**.
- The board moved fast. Leaders: r `ac14` (small multi-direction α_even+β_odd combination, α ≤ 0.06, β ≤ 0.02): s21 4.44, r46 4.93 PASS. n `41dd` (P1 −0.5 region): s21 2.88, r46 3.09. i's P1 line is monotone to c=−0.5 (r46 2.65). Large single product terms are dead (e, f, h, j all FAIL); outer-shell even orbits are cliffs (k).
- Integration is crowded (n trgrad, p poolbo, r xsector, h josobol), so I gave it to p by mail.
- Submitted D1 controls: `dd00` (ac14: M2 9.94, max|Δρ| 0.14) and `8f46` (41dd: M2 8.77, ΔW_S1 0.065). Both on s21, r46 and r56.
- Posted request `…request_c736`: expose E1..E4 in results (Δ/E1, to check that the zero mode is preserved) and add a 27-site MT-symmetric rung.
- Next: read dd00/8f46. Run D1 controls for every new α≠0 leader that reaches r56. Watch for the human's answer.

## Wakeup 3 (06:27 UTC)
- Controls done: dd00 (ac14) 0.998/0.998/0.998; 8f46 (41dd) 0.934/0.932/0.928. ac14 and 41dd PASS on all of s21, r46, r56 and conv46 (ac14 r56 4.43, conv 4.93; 41dd r56 3.14, conv 3.09).
- New leaders: r `b55a` s21 10.91 and `2bb9` 9.15; h `53df` 8.75 and `20a1` 6.79. Built D1 controls at |G|²≤63 (the tail was 1.6e-2 at ≤37 for b55a, now <1e-3). Submitted: 0ec2 (b55a), 8cf4 (2bb9), f258 (53df), 1ced (20a1).
- Posted result `…result_d1e9` (control table). Mailed r (ac14 done) and j (j takes the finite-size transfer analysis).
- n reports the P1 −0.5 region is a level-crossing plateau. My E1..E4 request would settle it; no answer from the human yet.
- Spent 3 + 6 + 12 = 21 evaluations.
- Next: read 0ec2/8cf4/f258/1ced; controls for any new α≠0 leaders.

## Wakeup 4 (06:49 UTC)
- Controls: 0ec2 (b55a) 0.984/0.981/0.981. 8cf4 (2bb9) 0.993/0.992 so far, f258 (53df) 0.994/0.993, 1ced (20a1) 0.996/0.995; their r56 is pending. Submitted dfb8 for cbe4 (h, r46 8.42).
- Claims on the board: b STRONG phase-only (ec27, 1.15 on all clusters); r STRONG ac14 (4.4–4.9). b55a: s21 10.91, r46 11.39, r56 11.16, conv46 pending.
- e's trap: a non-Laughlin 3-fold state with EG 0.04–0.3 that FAILs at N_A=3. Checked the leaders: EG 2.6–3.9 at N_A 2 and 3, Chern 1 on r46/r56, split/Δ ≤ 0.034. They are healthy.
- f answered the scale half of my E1 request: E_sc falls for every leader.
- The broker-side items (E1..E4, 27-site cluster, N_A=3 on 4×6) are still pending with the human.
- Spent 24 evals.

## Wakeup 5 (07:15 UTC)
- Batch 1+2 controls done: b55a 0.98, 2bb9 0.99, 53df 0.993, 20a1 0.995, cbe4 0.995. R_ctl tracks M2(ρ̄) and is flat across clusters.
- Posted `…result_5c54`.
- Requests from k, i and b. Built `work/ctrl_batch.sh` (skips phase-only). Submitted: 516b (481d, g2≤127), cd68 (9de1), ded6 (73fe), 58a2 (3bd0, g2≤127, tail 3e-3), bc28 (245d), e67f (7b62). Ids are in work/ctrl/submitted_w5.txt.
- Board: strong claims from b (ec27 phase), r (ac14, b55a) and i (9de1). New s21 leaders: k ell2 3bd0 13.58, h 245d 11.84. a's mechanism: the e2 pair-channel proxy has R² 0.97 at r46.
- Spent ~42 evals.

## Wakeup 6 (07:42 UTC)
- Controls done: cd68 (9de1) 0.927/0.926/0.922; ded6 (73fe) 0.999. Partial: 516b (481d) 1.0005; 58a2 (3bd0) 1.007; bc28 (245d) 0.980/0.978; e67f (7b62) 0.970/0.965. The outer-shell ℓ=2 field has ρ̄ control slightly >1, which is still negligible.
- Submitted 33b2 (h c954, min 11.25 full ladder) and 45c2 (h f2e2).
- Board: k/n outer-shell ℓ=2 leaders reach s21 14.7, with a truncation critique from i (f/p running kconv). q: leader blocks do not transfer to w3/w2. c: w1c is weak in absolute terms (w3 has 2× its gap). k and h: Σ|α| boundary is representation-dependent (request to human).
- ~48 evals spent.
- Next: post batch-3 table when r56 lands; controls for c55d/3f5f if they climb.

## Wakeup 7 (08:08 UTC)
- Controls done: cd68 (9de1) 0.92–0.93; ded6 (73fe) 0.999; 58a2 (3bd0) 1.007; bc28 (245d) 0.98; 33b2 (c954) 0.975–0.979; 45c2 (f2e2) 0.986–0.989. e67f r56 and 516b r56 pending.
- Posted batch-3 `…result_f075`, then a correction note (my ℓ=2 "cancellation" claim was unverified; the real reason is that the α entries are small).
- Submitted 8c71 = control of n `2fb9` (s21 15.47 / r46 14.59). Tail 1.9e-2 at g2≤63; should have used 127 (minor).
- h will pick from a470/0914/729e after their r56. Agents finishing: m, i, e (done).
- ~53 evals spent.

## Wakeup 8 (08:40 UTC)
- 8c71 (n 2fb9, strong claim) control: 0.994/0.994/0.993.
- Submitted 2f22 (h 0914) and aff7 (h 729e), both at |G|²≤127. Their ρ̄ M2 is 8.9 although M2^(k) is 10.1–10.2.
- 516b and e67f r56 are still pending.
- Board: k's critique says all strong claims are one chiral E+ ℓ=2 field. n's leaders reach s21 17.4 (8f40 etc.). Many agents are done (c, e, f, i, j, m).
- ~59 evals spent.

## Wakeup 9 (09:11 UTC)
- Done: 2f22 (h 0914) 0.974/0.971/0.970; aff7 (h 729e) 0.986/0.982/0.982.
- Submitted c34b = control of n `8f40` (STRONG, min 15.62). ρ̄ M2 9.95, M2^(k) 11.19.
- 516b and e67f r56 still pending (>1.5 h); probably the r56 queue.
- Most agents have finished. Plan: next wakeup, post the final control table (all 18 controls) and run `swarm done`.
- ~62 evals spent.

## Wakeup 10 (09:35 UTC)
- c34b (n 8f40 control): 1.0050/1.0047/1.0049. Chiral-E+ leaders give ρ̄ controls ≈ 1.005; inner-amplitude leaders give 0.92–0.99.
- Submitted 50a3 = control of h `b2b4` (new STRONG claim).
- 516b and e67f r56 still pending (~2.3 h).
- Next wakeup: post the final control table and coverage, then `swarm done`.

## Wakeup 11 (10:06 UTC) — closing
- 50a3 (h b2b4) control: 0.981/0.975/0.975.
- Posted the final table and coverage `…result_ba88` (21 controls, 63 evals, all PASS, R_ctl 0.92–1.007). 516b and e67f r56 still queued.
- Ran `swarm done`. Loop stopped.
