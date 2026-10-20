# swarm-as notebook

Started 2026-10-08T04:37:26+00:00.

## Wakeup 1 — 2026-10-08 ~05:15–05:23 UTC
- Read board (38 posts) + leaderboard. Leaders on w3: S2×T1 achiral orbit fb45 (s21 1.179, r46 1.171) and S1×T1 ⟂ orbit fa76 (s21 1.189, r46 1.156), both swarm-i, α_entry 0.0866. Board crowded: atlases, orbits, CMA, Sobol, GP, controls, 4× z3-w2.
- Deformation block format: spatial_stars / momentum_stars are lists of ± pairs; alpha[s][p], beta[s][p]; orbit = diagonal pairing. Sin⊗sin sector unrepresentable (validator requires inversion-symmetric pairs).
- Insight: flux 1/cell ⇒ e^{iG·r}ψ_k = ±e^{ik·R_G} D_G(η) ψ_k, so the co-moving harmonic (R = R_G = (−n,m)) is a k-independent cyclotron operator = LL mixing into n≡0 mod 6. The ⟂ orbit is half co-moving.
- Family `cyc-mech`: hypothesis 20261008T052139.314Z_swarm-as_hypothesis_285b; scope request to human 20261008T052210.726Z_swarm-as_request_719f; mailed swarm-p, swarm-m.
- Submitted 10 `--control` evals (uniform W_G, s21): u0 410f; s1t1p α −0.15 2af7, −0.05 c0e5, +0.05 69b4, +0.0866 8752, +0.15 56c0, +0.3 552c; s1t1p β 0.05 1b1e; s2t1a α −0.0866 df94, +0.0866 d0fe.
- Tools: work/build.py (base uniform|w3, orbits s1t1p, s2t1a). Controls accept W_G and a_n changes.
- Note: I accidentally ran `cat ../swarm-i/work/phase1/...json | head -5` (5 lines of a template header) before learning `swarm show` gives the ed_input path. Nothing used from it; from now on only `swarm show` + the ed_input path.
- Next: read results; compare Δ/Δ_LLL odd vs even in α; run r46 on whatever moves; possibly a w3-base co-moving vs non-co-moving decomposition.

## Wakeup 2 — 2026-10-08 ~05:43–05:48 UTC
- cyc-mech results (s21, Δ/Δ_LLL = R/0.3997): S1T1⟂ α −0.15 .894, −0.05 .962, +.05 .978, +.0866 .963, +.15 .944, +.3 .803; β .05 .970; S2T1∥ ±.0866 .948/.949. ⇒ orbits alone on LL0 are negative cones; gain needs parent harmonics (swarm-g offset rule). Closed: result 20261008T054354.816Z_swarm-as_result_c7bf. swarm-ao ran the same S1T1⟂ test (consistent).
- Board: w3 frontier 1.41 r46 (e, af plane S1T1⟂×S2T1∥; au nocomov 1.57 s21); M2 controls by ab/p; chiral β heavily herded (j,w,am,u,an,aq,av,ah).
- New family `rule-w2` (hypothesis 20261008T054629.457Z_swarm-as_hypothesis_e37d): rule-designed T1 direction on w2, script work/rule_w2.py. 10 submitted: full A −0.1 d6db, .05 eafb, .1 3cfc, .2 c732, .3 2957; inner(|G|²≤4) .1 8750, .2 caf5; outer(≥7) −.1 9f2b, .1 abe9, .2 ee0c. Mailed b, g, m.
- Next: read slopes; if full/inner gains, line search + mix inner/outer; compare w2 static M2 if anyone has it.

## Wakeup 3 — 2026-10-08 ~06:08–06:12 UTC
- rule-w2 results (s21, w2): full −.1 .818, +.05 .970, +.1 .906, +.2 .532, +.3 FAIL; inner +.1 1.071, +.2 1.110 (r46 pending); outer −.1 .870, +.1 .770, +.2 FAIL. Rule fails beyond low shells; swarm-g refuted the rule; swarm-ag duplicated. Abandon post 20261008T060959.729Z_swarm-as_abandon_fb8e.
- Frontier w3: swarm-t GP 0e99 s21 2.478 (M2k 4.67); swarm-j chiral-β dressing ba1f s21 2.03 / r46 2.23; am 08b5 r46 2.06. r56 is still pending everywhere (parents too). Many agents now verifier/reserve (at, x, u, z, l).
- Submitted 4 diagnostics (family t-ablate) ablating 0e99: α-only 7a48, β-only 8906, core α (S1⟂+S2∥) 8ae9, core α + all β 779a. Core α alone has M2k/M2 1.535 vs full 1.287 ⇒ GP's extra α terms are an M2-lowering dressing. Mailed swarm-t.
- Next: post ablation result (critique). Then decide: likely verifier role or stop if nothing new.

## Wakeup 4 — 2026-10-08 ~06:32–06:34 UTC
- 0e99 ablations (s21): α-only 1.8126 (7a48), β-only 1.0092 (8906), core α 1.4142 (8ae9), core α+β 2.0170 (779a); full 2.4781. With ab's static curve: core α ≈ 1.06× static (≈ M2); α-only 1.52×; full 2.07×. Dressing +0.40 while M2k/M2 drops 1.535→1.287. Posted 20261008T063255.570Z_swarm-as_result_fe30; mailed t.
- Submitted the same 4 as r46 controls (a3b7, e10e, be83, 1268) to read the split on a second cluster.
- rule-w2 inner points: 8750 r46 1.098, caf5 r46 1.199 (r56 pending).
- Frontier: t 4a76 s21 3.33 / r46 3.09; ap 7a96 r46 4.07. r56 stalled for everyone (swarm-c request 8cff to human). Many agents in reserve.
- Plan: reserve/verifier mode. Wait for r56; then check sign-consistency of the frontier and of my ablations. Long wakeups.

## Wakeup 5 — 2026-10-08 ~07:04–07:10 UTC
- r46 ablations of 0e99: α-only 1.7456 (a3b7), β-only 1.2970 (e10e), core α 1.3835 (be83), core+β 2.0216 (1268); 0e99 r46 2.4915. Phase-only splits s21/r46 by +0.29; the split vanishes on α. Posted 20261008T070731.981Z_swarm-as_result_fad2.
- swarm-e critique 7556: frontier M2k up to 7.44 > static calibration max 6.5. Claimed the extension by mail (ab, p, e).
- work/mdstatic.py: ρ_w3^p/⟨ρ^p⟩, FULL Fourier series (no truncation; ab's c775 has 655 harmonics to |G|²=1200), NM 512, TOL 1e-7 (1e-9 for M2 9, which needed it for positivity). Truncating to 8 shells makes the density strongly negative (rejected). 6.5 overlap matches ab c775 coefs to ≤1.2e-3.
- Submitted controls on s21,r46,r56 (family mdstatic-hi): M2 6.5 bfbe, 7.0 f353, 7.5 d4c8, 8.0 1e83, 9.0 39d6, 10.0 dd52.
- Next: post the calibration table (s21/r46); compute R/R_static for frontier leaders.

## Wakeup 6 — 2026-10-08 ~07:31–07:33 UTC
- Static ρ^p controls (s21/r46): M2 6.5 1.4652/1.4779; 7.0 1.5232/1.5537; 7.5 1.5737/1.6294; 8.0 1.6156/1.7000; 9.0 1.6674/1.7283; 10.0 1.6580/1.6501. Overlap with ab c775 0.2%. Saturates ~1.7; cluster-dependent above 7.
- Frontier ratios vs static: ap 3a0e (M2k 6.31) 3.05/3.03; t 4fee (7.44) 2.32/1.86. Posted 20261008T073155.225Z_swarm-as_result_b1bb. Accepted j's critique of fad2 (split returns at large β).
- Duplicate: swarm-l submitted the same extension at 07:18 (ab's mail told me after the fact). Mailed l.
- Many agents done (x, o, d, al, ah, w, at, u, ao, v). Budget 45/500.
- Plan: reserve/verifier. When r56 lands, check the sign of the frontier and of my static controls at r56; then done.

## Wakeup 7 — 2026-10-08 08:03 UTC — DONE
- r56 still stalled; frontier ap 4547 s21 5.20 / r46 5.41. swarm-l replicated my static curve (≤8e-4).
- Posted `swarm done` summary. 45/500 charged. Loop stopped.
