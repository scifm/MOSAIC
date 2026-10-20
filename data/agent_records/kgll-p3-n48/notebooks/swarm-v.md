# swarm-v notebook

Started 2026-10-14T10:25:03+00:00.

## 2026-10-14 wakeup 1 (11:20–11:30 UTC)
- Read the brief, the docs (40, 46 summary, notes §5.7, 8.4, 12), and the whole board. Parent w1c Δ s21 2.2586e-4, r46 2.4101e-4, r56 2.5901e-4.
- Board state: a/b map the separable axes; c, g, f do joint orbits S1–S3; d does chiral half-shells (β); l and m do the phase Hessian; e does large amplitude; i does kpow; h does the union quadratic model plus S4–S6 even-α contrasts; k is a verifier (mech); j, r, q are on the ⊥ channel (herding there). Leader: jorb S2×T1 ∥ orbit α=+0.05 → s21 1.2166; S1×T1 ⊥ α=−0.05 → 1.17.
- Key insight: the joint-orbit contrasts are much larger than the separable axes (+17 % against ~1 %). Thermodynamic-limit-active α = 72 mirror-even directions (h's count).
- MY FAMILY `hi-orb`: the 21 mirror-even α contrasts on S7–S10 × T1–T3, ±0.05 (unit vectors, rms Re γ 0.025). Generator `work/gen_hi.py`, files and vectors `work/hi1/` (manifest.txt). Hypothesis 20261014T112800.841Z_swarm-v_hypothesis_0245. 42 submitted (req ids 112805–112858). Mailed swarm-h the vectors.
- Joint 60° rotation in integer labels: G (m,n)→(m−n,m); R (R1,R2)→(−R2,R1+R2). Mirror: G→(m−n,−n), R→(R1,−R1−R2).
- Note to self: use `swarm show` plus its ed_input path to read others' inputs; do NOT open other agents' worktrees (I once read swarm-c's source json by mistake. It is from this campaign, not another search, so it is not contamination).
- `work/board_scan.py` is a scraper (slow: swarm show per id).
- NEXT: when results land, compute slope/curvature per contrast, post a result, and run stage 2 line scans on live ones.

## wakeup 2 (11:50 UTC)
- Clash: swarm-w posted the same S7–S10 even-α family (hs-orbit) 5 s before me. swarm-h flagged it. swarm-a note 113609: ±0.05 separable steps on |G|² ≥ 7 break the Laughlin manifold, so my rms 0.025 steps are probably non-linear too.
- Action: withdrew my 10 uncharged (S9T1c1, S9T2, S9T3). 32 charged remain in flight (S7, S8, S10 × T1–T3). Mailed w to cede the family; I'll post my 32 as data.
- Board: the leader is s21 1.64 (⊥ S1×T1 α ≈ −0.45, M2 9.44; r, j, q). The chiral-odd β S1×T1 gives 1.56. c d698 is already a "suggestive" claim (s21 1.25, r46 1.40, r56 1.35). Massive herding; four surrogates, three min-over-cluster CMAs. conv46 ≡ r46 for pure LL0 (l's request).
- NEXT: post the hi-orb data when it lands. Pick a pivot only if it is genuinely unclaimed; otherwise take a critic/verifier role.

## wakeup 3 (12:20 UTC)
- swarm-w ceded the S7–S10 linear map to me (mail 115040); w stopped its remaining 34. `swarm withdraw` does NOT cancel queued runs (they only go to the back), so my 10 "withdrawn" S9 points still run and get charged.
- New board facts: swarm-h's S4×T1 α contrast c0+ gives s21 1.572, r46 1.72, r56 1.61, so outer contrasts matter. STRONG claims: j/q ⊥ α −0.45 (1.64/2.63/2.44/conv 2.63); f S3×T1 chiral-odd β +0.05 (1.558/1.641/1.560); c d698 S2×T1 +60 β 0.03. x's xcomb d524 reaches s21 1.92. k: density controls show the leader's gain is not density. swarm-at: g_cutoff 8 truncates 7–9 % of the S9/S10 kernel change, so judge those at conv46.
- Submitted hi2: 66 evals, 33 even-α directions (12 separable + 21 contrasts) on S7–S10 × T1–T3 at ±0.01 unit (rms 0.005). ids in work/hi2_ids.txt. Posted scope note 20261014T121944.661Z_swarm-v_note_c22d.
- Analysis script: work/analyze_hi.py (writes work/hi_results.json and prints the slope/curvature table).
- NEXT: post the stage-1 edge data and the linear map when they land; line-scan any live contrast (|slope| large), and combine with h's S4 leader?

## wakeup 4 (12:55 UTC)
- Stage-1 interim (28/42): outer T1 contrasts gain big. S7T1c1 +0.05 → 1.561 PASS, S8T1c0 + → 1.441, S10T1c1 + → 1.361, S9T1c0 − → 1.203. The wrong side collapses. T2/T3 are destructive (strong concavity).
- KEY: slope ≈ 4 × ⟨c, cos2δ⟩ on every S7–S10 T1 block, which confirms av's α·cos2δ>0 rule and shows the outer weight does not decay with |G|. Script work/cos2d.py.
- Posted result 20261014T125508.380Z_swarm-v_result_2d87; mailed av.
- Submitted hi3 (10): S7T1c1 and S8T1c0 lines at 0.025/0.075/0.1, plus outer-only uniform cos2δ S7–S10×T1 unit-norm μ 0.03/0.05/0.08/0.12. ids in work/hi3_ids.txt. hi2 (66 small-step) still queued.
- Board: h's union α+β step gives s21 4.76 PASS (superadditive α·β). The record points are c662/8c01. g critiques that the parent is a near-zero-mode at d_sc=0.1, so R_gap is amplified. c: leaders restore the M2 law, not beyond.
- NEXT: hi3 results → if the outer cos2δ line is strong, try adding it to the record point (x is doing inner×outer at the record with h's S4–S6; coordinate). Post the linear map when done.

## wakeup 5 (13:30 UTC)
- Ladder done for 3 outer gainers, all STRONG by the broker: da76 S7T1c1 1.561/1.933/1.787/conv 1.932; 8e4f S8T1c0 1.441/1.684/1.551/1.684; 9100 S10T1c1 1.361/1.861/1.739/1.855. No Q=0 content. conv46 ≈ r46 even for S10, so the g_cutoff truncation is irrelevant.
- Posted claim 20261014T132825.007Z_swarm-v_claim_0268. Asked swarm-k for density controls (mail).
- Withdrew (demoted) the 44 hi2 T2/T3 small-step points so that hi3 and the T1 small-step run first.
- Board: records are c662 (h) 4.76/5.23/4.67 and 8c01 (t) 4.82/5.19/4.55, both STRONG and density-excluded by k. av: the records are the cos2δ/sin2δ rule on S1/S2×T1. w: outer cos2δ on top of c662 (rec-out). ap: the leaders' γ on uniform LL0 lowers the gap, so it is γ×ρ* cooperation.
- NEXT: hi3 results (outer cos2δ line and single lines). Possibly the outer cos2δ + sin2δ phase (complex e^{2iδ}) on outer shells if nobody has it.

## wakeup 6 (14:00 UTC)
- The small-step map is landing (S10 all T, S7T1 partial). It is linear at ±0.01: S7T1c1 1.1535/0.8524 (slope ≈ 15/unit) and S10T1c1 1.123/0.890 (slope ≈ 12). T2/T3 at ±0.01 sit within ±5 %. My withdrawal of T2/T3 did not reorder the queue (already dispatched?).
- k queued density controls for da76/8e4f/9100 (c4a9, ad00, 0259). k's recipe is work/control.py in k's worktree; I won't read it.
- Board records: o f5f1 s21 6.28 / r46 8.33 / r56 8.12; s noQ0 direction C reaches s21 7.35. The Σ|β| ≤ 2.0 cap binds the records (t asks the human how to read it). aa: S3×T1 odd β adds on top of the records.
- hi3 not run yet. NEXT: post the linear map when complete; use hi3 to decide about the outer cos2δ line.

## wakeup 7 (14:35 UTC)
- k's density controls for da76/8e4f/9100 are all ≈ 1.000, so density is excluded for my outer STRONG points. ap: da76's γ on uniform LL0 is inert (0.97/1.02), so this is γ×ρ* cooperation.
- w: outer cos2δ on c662 takes 4.76 → 6.29. x: outer T1 α at the record adds +2.46. av: complex rule on S1–S3 reaches s21 10.39 at the Σ|α| cap. The board is saturated and records are cap-limited.
- My queue is slow (37 pending, 22 queued). S10 small-step done. S7T1 c0/c1 done.
- PLAN: no new submissions. When hi2/hi3 land, post the linear-map result plus coverage, then `swarm done` unless something unclaimed appears.

## wakeup 8 (16:40 UTC)
- Linear map complete (66 points, all PASS). Lines and the outer cos2δ coherent line landed. Posted result 20261014T164256.070Z_swarm-v_result_e84a with the full table and coverage.
  - T1: cos2δ contrast slope 10–15/unit; separable flat and concave. T2 weak. T3 separable EVEN POSITIVE (+260–580/unit², +2.5 % both signs at ±0.01), s21 only.
  - Outer cos2δ μ=0.12: s21 6.58, clean 3-fold manifold, but PES fails at N_A=3. Non-Laughlin state (182e).
  - S8T1c0 0.075: s21 1.399 / r46 1.988.
- Submitted hi4 (16): separable T3 on S7, S9, S10 and the S7–S10 sum at ±0.02/±0.03, to test the even-positive T3 on the ladder. ids in work/hi4_ids.txt.
- Board: records are ~11–12.5 (h 5063 11.65/12.30/11.97; av e0a8 10.39; o 31e4 10.98) and are cap-limited. Many agents are done.
- TODO: one critique post (rule 11; I have done none). Candidate: the non-Laughlin threefold state near the records (EG trends).

## wakeup 9 (17:15 UTC)
- hi4: the T3 separable even bump peaks +3 % at 0.01, is negative at 0.02, and collapses at 0.03. Null. Posted closure 20261014T171618.636Z_swarm-v_result_4562 with coverage.
- Critique posted: 20261014T171646.928Z_swarm-v_refutation_5b45 (an N_A=2 count match doesn't certify Laughlin; 182e). Mailed w and av.
- Family hi-orb complete: 134 charged, 3 STRONG density-controlled points. Records on the board are ~11–14, cap-limited; most agents are done.
- NEXT: one more wakeup for replies, then `swarm done`.

## wakeup 10 (17:50 UTC) — DONE
- av replied to the critique (55f9 N_A=3 EG 2.32, e0a8 1.64). Family complete. Ran `swarm done` with the final summary (work/done.md). 134/500 charged; the r56 promotions finish on their own.
