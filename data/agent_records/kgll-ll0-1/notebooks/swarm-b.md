# swarm-b notebook

Started 2026-10-02T03:51:05+00:00.

## 2026-10-02 04:08 UTC — wakeup 1: scope chosen
- Read: doc 40 (024 pilot: LL01 seed, α1 −0.05 → +0.51 % at 4×6, −0.92 % at 5×6, sign flip), doc 46 (Nk=21 precision; w3 a1p +1.85 %, a1m −9.0 %; w2 a1p −5.05 %, b1p −3.0 %), theory §2, §5, §6.4, §8.
- Representable family: γ = Σ (α/2 + iβ) O_s(r) F_p(k), where O_s and F_p are any inversion-symmetric sets (cos-type only, so no sine parts). Pair stars {±G} allow C3 breaking; the cos-cos part of joint (G,R) orbits uses pair stars × pair stars with a coefficient matrix.
- Parents in solver shells: w3 on S3 (|G|²=4), S6 (12), S8 (16); w2 on S2 (3, −1/3), S5 (9, +1/3), S6 (12, −1/6).
- swarm-a took the w3 atlas (S1–S8 × T1–T3 × α/β × ±0.02, g_cutoff 6, n_mesh 48) and asked for a w2 atlas. **I took w2-atlas**, same design. Hypothesis post 20261002T040628.912Z_swarm-b_hypothesis_b7a0.
- Script: work/make_atlas.py → work/atlas_w2/ (96 inputs, all `swarm check` ok). Batch 1 (first 32: S1T1..S3T2) submitted from work/batch1.
- Next: submit the remaining 64 as slots free up (32 in flight max), then fit slope/curvature per direction: R(±h) → g = (R+ − R−)/2h, c = (R+ + R− − 2)/2h².

## 2026-10-02 04:20 UTC — wakeup 2
- Board: 18 agents, heavy overlap. On w2: swarm-e (w2-map, ±0.03) and swarm-f (w2-atlas, an identical design). **Split with swarm-f: f = α, me = β.** Already submitted, and kept: 16 α + 16 β (S1T1..S3T2). Remaining 32 β staged in work/batch2 (S3T3, S4..S8 × T1..T3). Submit when slots free (32/32 in flight now).
- Key board physics:
  - swarm-i/l: MT (or MK) parity means β on star×star is odd (no linear term in the TD limit), β on chiral modes can be linear, α on star×star is linear-allowed. All ladder clusters are mirror-free (s21 C6 only; r46/r56 C2), so the odd-direction linear terms are cluster artefacts.
  - swarm-r: on s21, T2≡T5≡T6; T3 is ×1.15 on r46; only T1/T2 are clean on every mesh.
  - swarm-m/o: momentum orbits that are constant on the mesh act as a static density change there (a loophole past the pin).
  - swarm-n: g_cutoff 6 truncates 1e-3..1e-1 of the kernel weight for S4+ or large steps.
- Broker backlog: 253 requests queued at 04:15, none charged yet.
- Next: submit batch2; tabulate β even/odd parts; choose a follow-up family that is not herded (candidates: T1/T2-only cluster-robust w2 search; verification/critique; matched-density controls).

## 2026-10-02 04:50 UTC — wakeup 3
- β half of the w2 atlas done (47/48 PASS, S3T3 β+ pending): result post 20261002T044651.323Z_swarm-b_result_7eef (with coverage). The MT parity argument holds: β-U odd ≤ 0.115/unit vs α slopes 0.5–1.2. Phase is concave, steeply at large |G|. Two weakly convex directions: β[S2,T2] (c=+2.4; R(+0.02)=1.0021, req 1d15) and β[S1,T2] (+0.5).
- Line scan (work/scan1, ids in work/scan1_ids.txt): β[S2,T2] ∈ {±0.05, ±0.1, ±0.15, +0.25}, β[S1,T2] ∈ {±0.06, +0.12}, g_cutoff 6.
- Tools: work/tabulate.py (my requests → table + pair slopes, cache work/results_cache.json), work/make_scan.py.
- Board: the w3 leader is swarm-h req 6e88 (A orbit S1T1 G⟂R, α=0.0635 per entry): s21 1.135, r46 1.113, C=1, PASS; M2_k +2.6 %.
- **My critique (note e1e5 + human request 3942):** R = ẑ×G l² pairs S1 exactly with T1 in the A orbit. Since e^{iG·r}e^{ik·R}ψ_k = η_G e^{ik·(R−ẑ×G)} e^{iG·η}ψ_k, half of the cos·cos A orbit is a k-independent cyclotron operator, i.e. static coherent LL mixing (pinned by the brief). The S2 partner is T2 (suppressed by e^{-|G|²/4}, 0.0043 vs 0.163). This does not explain S2T1-∥. Mailed h, k, j, o, q.
  - Subtlety to remember: LL weights are NOT invariant under Quotient B (e^{iθ(r)}). The invariant statement is in the form factor ⟨χ|e^{iqη}|χ⟩. Every GLL Bloch state is |χ_k⟩_cyc ⊗ |k⟩_gc with χ_k = Σ_G c_G η_G e^{-ik·a(G)} D(G)|0⟩. The static space has no k-independent non-LL0 component; the A orbit's cyclotron half adds one.
- Budget: 32 + 32 + 10 = 74 charged or in flight.
- Next: read the scan; if β[S2,T2] convexity survives at 0.1–0.25 → phase-only w2 candidate (automatically beyond-M2, and S2T2 is not the cyclotron channel for β... check: S2's cyclotron partner IS T2⟂, but a star×star includes it only partially and is suppressed ×0.0043). Watch for human replies.

## 2026-10-02 05:17 UTC — wakeup 4
- The β[S2,T2]/β[S1,T2] scan is a clean null. The convexity was a flat spot: R(±0.05)=0.98, ±0.1→0.84, ±0.15→0.55, +0.25→0.04 (still PASS!). Abandon post 4938 (coverage: 58 evals, best 1.0021).
- Board: w3 leader p/cc86 (S2T1∥ α=0.32 + chiral β S4/S7): s21 2.40, r46 2.47, C=1. w2 leader r/e064 (chiral β): s21 1.077, r46 1.20.
  - My LL-mixing critique was confirmed and narrowed. swarm-p: Q = a_G + R, only S1T1⟂ has Q=0. swarm-q: the C6 static half feeds only LL0+LL6. S2T1∥ (LL-free) is as strong, so LL mixing is not the driver. h accepted it for 6e88.
  - n's controls: static density explains ≤1.9 % of 6e88's 13.5 %.
- Zero-cost check (work/kernel_check.py): the kernels of p/cc86, o/bd1a, r/e064 are converged (box loss ≤1.3e-6 L2, mesh alias ≤2e-12).
- The Q-frame (|Q|²=4) selection rule is falsified by the S1T2-∥ data; dropped.
- **New family w2-outer-orbit** (hyp 7554): orbit-resolved α by G–R angle class on w2's S3..S8 × T1, 14 classes × ±0.03, g_cutoff 10. 28 submitted (work/orb1, ids in work/orb1_ids.txt). Tool: work/make_orbits.py (also builds --combo inputs).
- Budget: 74 + 28 = 102.
- Next: tabulate the classes (slope per class); line-scan the live ones; build a joint ray; coordinate with r (w2-synth chiral β) for combos.

## 2026-10-02 05:36 UTC — wakeup 5
- orb1 done (28 PASS). Table in work/orb1_table.txt; result post f15c. Live w2 α classes (per-entry slope): S4-10.9 +3.29 (R 1.0537, b281), S3-90 +2.71, S4-70.9 +1.52, S4-49.1 −2.20, S7-43.9 −2.21, S7-76.1 −1.62, S8-90 −2.11, S8-30 −1.63. Dead: S5, S6, S7-16.1.
- Board: f's w2-far and e's w2-map are nulls for the w3 leader plane on w2 (the w3 mechanism is parent-specific). r's w2 best 509c (P4⊥ α + chiral β): s21 1.137, r46 1.289. i's selection rule: live iff a_{G+G_p} = −R for a parent harmonic G_p. The broker's r56 queue now serves the strongest first.
- orb2 submitted (18, ids work/orb2_ids.txt, cmds work/orb2_cmds.sh): S4-10.9 line t 0.06–0.30; gradient ray over 8 live classes (per-entry max 0.03–0.18); (S4-10.9, S3-90) plane; diagonal Newton ×0.5/1/1.5.
- Mailed r (offered an α base for chiral-β stacking; I stay out of α×β-chiral on w2 unless r asks) and i (table as a rule test).
- Budget: 120.

## 2026-10-02 05:55 UTC — wakeup 6
- orb2 results (all at s21 unless noted):
  - S4-10.9 line: 0.06 → 1.0555 (r46 1.153); 0.1 → 0.97; 0.15 → 0.76; ≥0.22 FAIL.
  - (S4-10.9, S3-90) plane: **c37c (0.05, 0.05): s21 1.0948, r46 1.238** (best α-only on w2 from me); d4a4 (0.05, 0.1): 1.053 / 1.265; cd26 (0.1, 0.05): 1.021 / 1.202.
  - Gradient ray and Newton: strongly sub-additive. Newton ×0.5 e10a 1.0575 / 1.195; ×1 0.93; large steps FAIL (non-Laughlin, R up to 2.1).
- Board: claims are up. p/cc86 STRONG on w3 (2.40 / 2.47 / 2.46 / conv 2.47), provisional on the LL-content ruling. d/2400 phase-only robust_positive on w3 (1.036 / 1.080 / 1.056 / 1.076). w2 leader g/7f3e: s21 1.209 / r46 1.368 (P4⊥ α + −P1pair α + r's chiral β). j: r46 has a generic +0.4..0.9 % even-order bias, so don't rank by r46. e: the leaders' β patterns lose at α=0.
- stk1: 6 requests on top of g/7f3e (--builds-on): S4-10.9 α ∈ {+0.02, +0.04, +0.06, −0.03}, S8-90 α ∈ {−0.02, −0.04}. Tool: work/stack_on.py (adds class α into the first T1 column block). ids: work/stk1_ids.txt.
- Budget: 144.

## 2026-10-02 06:12 UTC — wakeup 7
- stk1 on g/7f3e (base s21 1.2093 / r46 1.3679): S4-10.9 +0.02 → 1.2067/1.3713 (flat), +0.04 → 1.186, +0.06 → 1.141, −0.03 → 1.171. **S8-90 −0.02 → 1.2284/1.4003 (2134); −0.04 → 1.2307/1.4336 (bb0d), the new w2 best on min**, ent gap ~4.0, M2_k 2.657, r56 pending.
- S8-90 rows are collinear with P4⊥ (S3-90) rows: (4,4) = 2·(2,2), same T1 partner, so this is the second harmonic of the ⟂ orbit with the opposite sign.
- stk2 on bb0d (8 requests, ids work/stk2_ids.txt): S8-90 totals −0.06/−0.08/−0.10; S7-43.9 −0.02/−0.04; S4-49.1, S8-30, S7-76.1 at −0.03.
- Board: o's bd1a STRONG claim on w3 (provisional). c's critique: the ent gap falls from 21 to ~5 on the amplitude leaders. n: M2-matched static controls reach ~30 % of the leaders' gains. q: the r56 excess is about half of r46's.
- Budget: 152 (broker says 126 charged; promotions are free).

## 2026-10-02 06:31 UTC — wakeup 8
- stk2 on bb0d: nothing beats bb0d at s21 (1.2307). More S8-90, S7-43.9 and S4-49.1 raise r46 (to 1.50) but lower s21; S8-30 and S7-76.1 lose on both. Result post (class stacks) made; not ranking by r46 (f: the parent r46 gap is 4.1 % low; j: r46 even-order bias).
- stack_on.py now supports T2 classes ("S1T2:0.0=-0.04"), appending T2 columns when absent.
- stk3 on bb0d: S1T2-0° (∥) and S1T2-60° at ±0.04 (ids work/stk3_ids.txt). Tests whether h's w3 add-on S1T2∥ (fea3 s21 2.80) transfers.
- Board: p's w3-sobol global map; k: Q0-free T2 β-chiral live on cc86; n: the PES eg falls with M2 for static bands too.
- Budget: 156 incl. promotions (broker charged 134 + 4).

## 2026-10-02 06:52 UTC — wakeup 9
- stk3 on bb0d: **S1T2-∥ −0.04 → f0fd s21 1.3052 / r46 1.4736 (new w2 best on min)**; S1T2-60 −0.04 → 0985 1.2835/1.3943; the + signs lose (1.1065, 1.0669). Agrees with h's c178 (S1T2∥ live on w2 with w3's sign).
- g's new α optimum 0f4e (s21 1.2613 / r46 1.3379). r is re-tuning β on bb0d (6 requests).
- stk4 (ids work/stk4_ids.txt): bb0d + S1T2∥ −0.07/−0.10; f0fd + S1T2-60 −0.04; 0f4e + S8-90 −0.04, + S1T2∥ −0.04, + both.
- Mailed g/r/h/k a lane split: me α classes; r β on bb0d; g β on 0f4e; k T2 β; h gradients.
- Board: c's 776c claim STRONG (amplitude-only S2T1∥: 1.518/1.409/1.499/1.409; static M2-matched 1.28). m done.
- Budget: ~166 incl. promotions (broker charged 138 + 6).

## 2026-10-02 07:14 UTC — wakeup 10
- stk4 (s21 only so far):
  - **0f4e + S8-90 −0.04 + S1T2∥ −0.04 → fb0c 1.3938** (superadditive: +0.044 and +0.051 alone → +0.133);
  - f0fd + S1T2-60 −0.04 → 1.3535;
  - bb0d + S1T2∥ −0.07 → 1.3303, −0.10 → 1.3404 (still rising);
  - 0f4e + S1T2∥ −0.04 → 1.312; + S8-90 alone → 1.3048.
- Lanes agreed with g/r/h/k: α classes are mine. k handed over its α T2 classes on 0f4e (S5T2-60 −0.05, S6T2-90 +0.05, S6T2-30 +0.05, each ≈ +0.07).
- stk5 on fb0c (7; ids work/stk5_ids.txt): S1T2∥ further −0.03, S1T2-60 −0.04, S5T2-60 −0.05, S6T2-90 +0.05, S6T2-30 +0.05, S8-90 further −0.02, combo3.
- Asked h for a gradient at fb0c; told r about the fb0c base.
- Board claims: w2 r/e064 STRONG (phase-only), l/9fcb STRONG (phase-only), g/98ec and 29a2 STRONG (amplitude); w3 h/d49b, c/776c STRONG.
- Budget: 144 + 13 charged.

## 2026-10-02 07:36 UTC — wakeup 11
- stk5 on fb0c (fb0c is now s21 1.3938 / r46 1.4189):
  - **S8-90 further −0.02 (0e5e): s21 1.4401**, r46 pending;
  - S1T2∥ −0.07 total: 1.3652; S1T2-60 −0.04: 1.3440;
  - S6T2-90 +0.05: 1.3467; S6T2-30: 1.3245;
  - S5T2-60 −0.05: 1.3833 / **r46 1.1765**; combo3: 1.2154 / **r46 0.4070** (!).
- Lesson: outer-shell T2 α on w2 is s21-only (k agrees, abandon 8668). Posted a warning note. Only S1T2∥ holds on r46 so far.
- Posted a human request: the r56 queue ranks by R_gap_min across parents, so w2 is starved (bb0d/f0fd/fb0c at stage r56 since ~06:00).
- Board: p's 9fc9 w3 s21 3.514; o's 84e4 phase-only STRONG w3; e: all claimed points are exactly M·T-invariant; g opened w2-sobol (11-D global; includes my S16T1-90 = S8-90 and S1T3-par).
- Next: when 0e5e r46 lands, extend the S8-90 line (−0.08) on fb0c if r46 holds.

## 2026-10-02 07:58 UTC — wakeup 12
- **0e5e (fb0c + S8-90 to −0.06): s21 1.4401 / r46 1.4648, best w2 on min.** BUT at s21 split/Δ = 0.047 (gate 0.1) and eg 2.9 (s21c N_A=3: 2.18); r46 split/Δ 0.005, eg 3.06, C=1. M2_k 2.83, S ratio 0.70. Purity is falling: watch it.
- S8-90 line on fb0c at s21: −0.06 → 1.440, −0.08 → 1.434 (r46 1.506), −0.10 → 1.398 (r46 1.531).
- Other stk5 r46: S1T2∥ −0.07 (4202) 1.365/1.391; S1T2-60 (25d8) 1.344/1.299; S6T2-90 (be16) 1.347/1.342; S6T2-30 (527e) 1.325/1.233.
- Human: the r56 queue is now ranked per parent (my request 9ab0 answered).
- h gradient at fb0c (5532): S2T1∥ + (+0.037), S3T1⟂ − (+0.030) are the clean c0 steps; the oblique ones are likely s21-only.
- stk7 on 0e5e (ids work/stk7_ids.txt): S2T1∥ +0.04, +0.08; S3T1⟂ −0.04; both.
- Board: e's audit proposes a split/Δ ≤ 1e-2 robust tier; d's C7 phase-only STRONG; k's 7966 w3 3.73/3.83/3.79; f, j, c, o, m are done.

## 2026-10-02 08:01 UTC — wakeup 13 (early)
- stk7 on 0e5e at s21: S2T1∥ +0.04 → 1.4975, +0.08 → **1.5073**; S3T1⟂ −0.04 → 1.4598; both → 1.4736 (sub-additive). r46 pending.
- stk8: S2T1∥ +0.12, +0.16 on 0e5e (ids work/stk8_ids.txt). S2T1∥ was dead or negative at the w2 parent (e/f) and is live at this base.

## 2026-10-02 08:24 UTC — wakeup 14
- The S2T1∥ line on 0e5e (s21 / r46): +0.04 1.4975/1.4794; **+0.08 (879b) 1.5073/1.4895 = best w2 on min**; +0.12 1.4456/1.5038; +0.16 1.3253/1.5190. S3⟂ −0.04 1.4598/1.4822; both 1.4736/1.4911.
- 879b: M2_k 2.81, s21 split/Δ 0.045, eg 3.0 (N_A=3 1.96); r46 split/Δ 0.013, eg 3.2.
- r: β 2×e064 on fb0c → cb44 1.493/1.5045. Mailed r the 879b α base for its β (its lane).
- Posted an interim result (α line table). Pausing α pushes until the r56 legs land (none of mine has an r56 yet).
- Budget 165 charged (+promotions).

## 2026-10-02 08:56 UTC — wakeup 15
- No r56 yet for any of my points; the r56 queue holds dozens of w3/w2 points.
- g's w2-sobol 1909: s21 1.513 / r46 1.539, split/Δ 0.007. Cleaner and slightly higher than my 879b; it uses small P4⊥ + negative S16T1-90 (= my S8T1-90 class). My local α lane is now covered by g's global map plus local search.
- **Withdrew 41 dominated requests** from the ladder (reason given). Kept bb0d, f0fd, fb0c, 0e5e, 879b for r56: they trace the line.
- Decision: no new α steps on w2. Next: wait for the r56 legs → post the coverage block for w2-outer-orbit → decide between a verifier role and done.
- Open: human request 3942 (LL-mixing ruling) is unanswered; p/o/k claims stay "provisional" on it.

## 2026-10-02 09:27 UTC — wakeup 16
- Still no r56 for my 5 kept points. The GPU pool (job 27809046) is alive. NB: the pool logs use local time (EDT, −04:00), not UTC. ~175 s per r56 eval on 2 GPUs, so ~40/h, and the queue holds dozens.
- r: β on 879b α → bf94 s21 1.548 / r46 1.591 (split/Δ 0.06–0.08, purity-limited); r closed its β lane. g's 1909 (1.513/1.539, split 0.007) is the clean w2 point.
- Board: a, d, e, p, m, c, f, j, o, q have posted final summaries.
- Plan unchanged: wait for r56 → coverage post → verifier role or done.

## 2026-10-02 09:58 UTC — wakeup 17
- g's w2-sobol local: 1059 s21 1.764 / r46 1.793, split ≤ 0.006, so my w2 line is dominated.
- Withdrew bb0d, f0fd and fb0c too (44 withdrawn in total). 0e5e and 879b stay on r56 as the line's trace.
- **Posted the w2-outer-orbit coverage post 2883** (85 requests, 79 PASS / 0 AMB / 6 FAIL; best 879b 1.507/1.490, r56 pending).
- Next role: verifier/critic at a slow cadence. Check new claims (g's w2 1059 when it claims), post the r56 of 879b/0e5e, then `swarm done`. 341 evals unspent: no unexplored direction with a better expected value than the swarm's current lines.

## 2026-10-02 10:43 UTC — wakeup 18
- The w2 r56 lane was stalled by a broker bug (a failed request set w2's per-parent best); the human fixed it at 10:28 (c95197e). Waiting on r56 for 0e5e and 879b. r and l are done. Nothing else to act on.

## 2026-10-02 11:30 UTC — wakeup 19
- Still no r56 for 0e5e/879b (the human fixed a stale GPU-pass bug at 10:43).
- g claimed w2 0356 STRONG (1.857/1.865/1.789/1.862). Verified at zero cost: kernel converged, conv shift −0.1 %, eg flat ~3.7, r56 split/Δ 0.044. Posted the verification note (family verify).
- k, n and i are done. Remaining active: g (w2-sobol batch 2), h?

## 2026-10-02 12:05 UTC — DONE
- Posted the final summary via `swarm done` (work/done.md). 159/500 charged. 879b and 0e5e r56 still queued (they stay on the ladder; the broker will record them). Loop stopped.
