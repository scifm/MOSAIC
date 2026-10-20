# swarm-a notebook

Started 2026-10-08T04:34:31+00:00.

## 2026-10-08 wakeup 1 (04:55 UTC)
- Read brief, docs 40/46, kdep_envelope, validate. Parents s21 Δ: w3 4.5714e-4, w2 3.2271e-4.
- Board at start: empty; within minutes swarm-c (atlas-T1-w3), swarm-f (atlas-T23-w3), swarm-e (joint-pair-w3) claimed the w3 atlas.
- My family: **atlas-w2** (hypothesis 20261008T045944.883Z_swarm-a_hypothesis_5b7e): S1–S10 × T1–T3, α=±0.1, β=±0.1, one term at a time, n_mesh 48 / g_cutoff 8 (same as w3 atlas). 120 requests.
- Tools: work/gen.py (map / spec / shells), inputs in work/map_w2, chunks of 30 in work/batch_w2/b0..b3 (ordered T1α, T1β, T2α, ...).
- Submitted b0 (T1 α all S + T1 β S1–S5). b1..b3 still to submit when in-flight < 32.
- Next: collect, compute slope/curvature table, post result; then line scans on positive directions; cross-check w3 winners on w2.

## 2026-10-08 05:20 UTC
- All 120 atlas-w2 submitted (logs work/submit_b0..b3.log, merged work/all_submits.log). Charging is at ACCEPT (broker _accept_one); "queued (waiting for a slot)" = not yet accepted. Withdraw does NOT cancel (still accepted & charged), only deprioritizes runs.
- Withdrew 40 β requests on S4–S10 (work/withdraw1.txt) to deprioritize them.
- Board state: w3 leader = S1×T1 ⟂ joint orbit (swarm-i fb45: s21 1.1785, r46 1.1712); swarm-e: S1T1⊥ & S2T1∥ only linear directions (half-translation selection rule, swarm-h). w2: exact Z3 magnetic-translation symmetry (swarm-u/v/x/q) → separable slopes zero on most blocks on s21; I promised to test it with atlas odd parts. w2 crowded: m (orbit-w2, 1.06 s21), n (w2-opt), z3 x4.
- First data: S10T1 α−0.1 → 0.757, α+0.1 → 0.814 (big negative cone).
- work/collect.py: `python3 work/collect.py work/all_submits.log` → table + work/results.json.
- Next: when atlas lands, post result with odd/even per block vs Z3 rule. Then pick a new uncovered niche (candidate: transfer of the w3 ⟂-orbit mechanism to w2 is m's; maybe finite-size/ cluster-sampling checks or higher-T joint orbits on w2).

## 2026-10-08 05:50 UTC
- atlas-w2 interim (66/120 done): everything < 1 on s21. Separable β on S5–S10 ×T1 FAILs the gate; ×T2 collapses with |G|. Largest odd parts on S3,S4,S7,S8,S9 ×T1 (table in hyp2). Best separable 0.9955 (S3T1 α+0.1, dc98).
- Offset rule (work/rule.py: w(G±Gc(R)), Gc = ẑ×R): predicts wrong sign for separable S7/S8/S9 T1 odd parts on w2. Possibly missing a magnetic-translation sign η_L or per-orbit weight; not resolved.
- New family **hiorb-w2** (hyp 20261008T055103.743Z_swarm-a_hypothesis_ac71): achiral α orbits S7–S10×T1 on w2, A=±0.1, g_cutoff 12, 22 evals (work/hiorb_w2, work/submit_hiorb1.log). Builder work/orbgen.py (validated: orbit sum == separable, M2k identical).
- Board: w3 top s21 1.57 (au nocomov), e/af ridge S1T1⊥+S2T1∥ r46 1.41. w2 leader swarm-m S3T1⊥ (r46 1.159).

## 2026-10-08 06:25 UTC
- atlas-w2 CLOSED, result posted 20261008T062524.466Z_swarm-a_result_679d (coverage incl.). Only α[S1,T1]=−0.1 gains: 8df7 s21 1.0258, r46 1.0803, r56 pending. Z3 rule holds; β even & destructive.
- hiorb-w2 CLOSED (abandon 20261008T062551.136Z_swarm-a_abandon_54a8): duplicate of swarm-ar's orbit-w2-ext phase 2(i) (I missed their announcement). Agreement 48/12 vs 64/10 ≤5e-4 = numerics check. Lesson: read full hypothesis text of overlapping families before submitting.
- Budget 142/500 charged.
- Board: w3 s21 up to 3.33 (swarm-t 4a76, M2k 6.23, PES NA2 4.28 vs parent ~21); r56 stalled for everyone (swarm-c request). Many agents switched to reserve/verifier (at, x, u, w).
- Running: work/pesfetch.py on 45 w3 PASS entries sampled across R → work/pes_sample.json, to test whether R gains trade off against PES entanglement gap (critique candidate).

## 06:30 UTC
- Posted PES audit note 20261008T062741.999Z_swarm-a_note_ffda (PES gap uncorrelated with R, ρ=0.02, n=45; lowest N_A=3 gaps: j fe2e, af ed2b/1fd3); mailed j, af.
- Switched to reserve/verifier (note posted). Plan: when r56 lands, audit sign/ordering s21→r46→r56 for top-30 of both parents (ED-free, from swarm show); answer mail requests for checks.

## 07:15 UTC
- r56 still 0 results board-wide. w3 top: ap 3a0e s21 4.39 / r46 4.39. Many agents done (ao, v, ak, g, i, x).
- swarm-e critique 7556: frontier M2k (6.2–7.4) beyond static calibration (ab/p ≤ 6.5). Offered to swarm-ab (mail dead) to extend: ρ_w3^p/<ρ^p> with 0.3% floor, M2 ∈ {7, 7.5, 8, 9, 10.5}, --control on s21,r46,r56 = 15 evals. Builder work/staticpow.py reproduces ab's 816c coefficient w(-2,-2)=0.742650 exactly. Inputs in work/ctl_ext/. Waiting ~20 min for ab reply, then submit (family mdctl-ext).

## 07:36 UTC
- Stood down from mdctl-ext: swarm-l (m2hi-ctl, 6 controls M2 7–10) and swarm-as (mdstatic-hi: static saturates ≈1.67 s21 / 1.73 r46, turns over by 10; ap 3a0e ≈3.0× equal-M2 static) cover it. Nothing submitted. Lesson again: check board right before submitting.
- w3 top now ap 4547 s21 5.20. r56 still stalled. Many agents done.
- Remaining role: r56 ordering audit when r56 lands. Budget 142/500.

## 08:37 UTC
- Quiet hold. r56 still 0 results board-wide (incl. parents); no human reply to swarm-c's request. ~30 agents done. w3 top ap e2f1 s21 5.43 / r46 5.56; w2 top q 0d4c s21 1.41. Static band caps ~1.75 (ab, as, l). Plan: poll hourly; if r56 still stalled after a few hours, post final summary + swarm done.

## 09:15 UTC — DONE
- Posted final summary via swarm done (work/done.md). 142/500 charged. r56 still stalled; audit left to f, t, ab, af, aj, aq (all holding for r56).
