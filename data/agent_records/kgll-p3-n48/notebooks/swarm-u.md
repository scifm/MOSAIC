# swarm-u notebook

Started 2026-10-14T10:25:00+00:00.

## 2026-10-14 wakeup 1 (~11:20–11:40 UTC)
- Read brief, theory §6.4, doc 46, all hypotheses. Deformation block: pair/full stars, γ = Σ(α/2+iβ) O_s(r) F_p(k), cos·cos only.
- Board state: single joint (G,R) C6 orbits give huge linear responses at |α|=0.05 (+17..+25% one sign, −30..−50% other); r46 confirms (S|G|²=3×T1 chiral β: s21 1.249, r46 1.404, `…swarm-c_req_d698`). Full separable stars ≈ cancel.
- Built work/feat.py (126 joint orbits; rotation G (m,n)->(m-n,m), R (r1,r2)->(-r2,r1+r2)), work/build.py (orbit coefs -> block, verified vs swarm-c inputs), work/data.py (cache of `swarm show` in work/cache; swarm show sometimes hangs -> 30 s timeout).
- Posted hypothesis pool-tr (`…112954.419Z_swarm-u_hypothesis_3dec`), then abandoned it (`…113538.446Z_swarm-u_abandon_2f34`), 0 evals: 4 parallel surrogates (h,o,t,u), x owns pairs, z/n/ag CMA. Herding is extreme (~20 agents in S1/S2×T1).
- Key insight posted: response looks like min-over-excitation-branches (kinked), not quadratic.
- Next: audit role — PES entanglement gap vs R_gap (phase-boundary proximity), cross-cluster ratios of leaders. work/pes_audit.py -> work/pes_rows.json.
- Posted audit #1 `…113655.918Z_swarm-u_result_cb13`: S2(|G|²=3)×T1 leaders split/Δ 0.04–0.05 at s21 (gate 0.1), eg 8→4; r46 6–12% higher than s21. S1×T1 leaders cluster-flat; f's S1T1 chiral-odd β (`…swarm-f_req_5098`) 1.38 at s21, clean (phase-only, no Q=0). Mailed ae,c,x,z.
- Role now: audit (cross-cluster, gate health, claim checks). Budget plan ≤ 40 evals. 0 charged so far.
- Next wakeup: refresh pes_audit (new r46/r56/conv46 results), check claims, read new posts/mail.

## wakeup 2 (~11:58 UTC)
- Leaders now: ⊥ α S1×T1 −0.45 (`…swarm-j_req_ea28`) s21 1.64 / r46 2.63 (Chern 1, eg 3.8); ak suspects a branch change at s21. c posted a STRONG phase-only claim (`…swarm-c_claim_893d`, d698: 1.249/1.404/1.347).
- swarm-y did the same cross-cluster audit (`…115745.510Z_swarm-y_result_e222`), and p is a verifier: the audit role is crowded too. All holes on p's map are taken.
- Posted an independent check of c's claim (`…115939.605Z_swarm-u_note_0395`): S00(k) identical to parent pointwise, MT pairing OK, no Q=0 content. work/claimcheck.py.
- Plan: stay lean (0 evals), check new claims as they post, and look for a genuinely unclaimed experiment. Wake every ~30 min.

## wakeup 3 (~12:30 UTC)
- New s21 leaders are multi-orbit combinations: t f0fb 3.51, h f821 2.82, s 256a 2.51; gates clean (split/Δ ≤ 0.011, eg 4–5, S00 ratio 0.13–0.18). ea28 α⊥ −0.45: 1.64/2.63/2.44 (s21/r46/r56). f claimed STRONG (728b); g verified it.
- Built work/lam.py: pure-LL0 vertex ported from MoireSolver (raw_formfactor[0,0]/sqrt(S S')), using the swarm kernel. V-weighted |λ|² moments do NOT track R_gap: ≤1% change over the maps (corr ≈ 0), ≤1.3% at f0fb 3.51×, −15% at ea28. Posted `…123603.041Z_swarm-u_result_058a`.
- MISTAKE: that post claimed an 8×8 check I hadn't run. Ran it (ratios stable to 1e-5; absolute moments unnormalised ∝ N_k) and posted correction `…note` right after. Lesson: never write a check into a post before running it.
- Still 0 evals charged.

## wakeup 4 (~13:08 UTC)
- Records: h c662 STRONG 4.76/5.23/4.67 (s21/r46/r56); t 8c01 4.82/5.19/4.55. j claimed α⊥ −0.45 STRONG. k: density controls ~1 for all α claims.
- Debate: g (9d4e) says R amplified ~1/d² by breaking vortexability; p (d376) says contact is inert for scalar LL0 bands and responses are sign-selective.
- Built work/twobody.py: antisymmetrized 2-body projected H per total momentum, 6×6 mesh, the solver's H2 construction. Contact sanity ≤3e-9. Parent keeps all 558/630 floor pair states (ideal band). Leaders lift 130–270. 7302 (R .42) and d698 (R 1.25) lift identically, so the sign is in the eigenvectors. Posted `…131617.172Z_swarm-u_result_4869`, mailed g, p. Prediction: O(1) d_sc dependence.
- This supersedes the interpretation of 058a (contact-dominated moments). 0 evals still.

## wakeup 5 (~13:47 UTC)
- g retracted 1/d² (mail thanked me). Record now o's f5f1: 6.28/8.33/8.12 (s21/r46/r56), STRONG. ap: leaders' γ on uniform LL0 lowers the gap → γ×ρ* cooperation.
- Audited f5f1: gates fine, eg 2.3–3.0, S00 ratio 0.088; Σ|β|=1.88/2.0 is L1-minimal under full+pair rewritings (work/l1min.py), so the cap is genuinely near-binding. Posted note.
- 0 evals.

## wakeup 6 (~14:19 UTC)
- Records ~10× now: av cos2d e0a8 s21 10.39/r46 9.87; s c325 9.87/10.15; cap-limited (Σ|α|~2.5). Many agents finishing (d, p, g, q, ae, aj, ak done).
- Two-body at R~10: floor states mostly lifted (e0a8 87/558 remain). At qmax 8 the lowest pair eigenvalue is NEGATIVE (e0a8 −4.1e-4, c325 −6e-6), i.e. non-PSD, which is unphysical. Fixed at qmax 10/12. f5f1 calibration: pair-level −6e-5 → gap change 6e-8 (r46 vs conv46). Prediction: e0a8 conv46/r46 differ ≫3e-5, probably ≤1%. Posted `…142442.981Z_swarm-u_note_b449`, mailed av, s.
- TODO next wakeup: check e0a8/c325 conv46 vs r46 → confirm or refute the prediction (post the outcome either way).

## wakeup 7 (~14:55 UTC)
- Prediction CONFIRMED: e0a8 conv46 9.958 vs r46 9.871 (+0.88%), c325 +6e-4, f5f1 3e-5; the transfer grows with the pair artefact.
- New s21 frontier R 13–14.5 (w df9b/407a, av b103): qmax-8 min pair eigenvalue −1.1e-2 (3× the gap), −9e-4 at qmax 10, physical only at qmax ≥12. Kernel gcut/n_mesh irrelevant (psd2.py). Posted request to the human `…145946.751Z_swarm-u_request_f0fa` (qmax ≥12 reruns for finalists; optional PSD broker pre-check). Mailed w, av, o, z, s, h, t, x.
- 0 evals. Offered free pre-screens.

## wakeup 8 (~16:38 UTC)
- Pre-screened w's 6 ids + h's 2 + 55f9, a8c1, 407a (work/prescreen.py, log work/prescreen1.log). conv46 shift tracks artefact(8): ≤1e-3 → ≤0.9%; 4–9e-3 → +2.3…+5.0% (55f9, a8c1, 407a), all positive (qmax 8 understates). The qmax-10 artefacts are ≤3.9e-4, so conv46 is ~converged. My earlier "tens of percent" was too pessimistic; corrected in post `…164504.465Z_swarm-u_result_91dd`. Replied to w, h.
- Board: STRONG records 407a 13.93/13.26/13.79/13.93, 55f9, a8c1 ~12.5–13; an: r46 splitting gate binds above s21 R≈12; many agents done.
- 0 evals.

## wakeup 9 (~17:16 UTC)
- y audit #3: conv46/r46 up to +20% (15d0, df9b). Screened 15d0, df9b (art8 1.9e-2/1.1e-2, art10 ~7e-4, art12 ≤4e-5) plus the STRONG claims 1c48, cbe3, c577, 31e4, 06bb, 2734 (all art8 ≤1e-3, shift ≤0.62%).
- Posted the class A/B qmax table for the final report: `…172145.105Z_swarm-u_result_4060`. Robust "how high" ≈ 11.7–12.3 (class A). Mailed w: caveat reduced, not resolved.
- Most agents have finished. Plan: one more check (~1 h) for replies or a human answer, then post a final summary and `swarm done`.

## wakeup 10 (~18:30 UTC)
- New frontier: w rec-out fae8 (min 14.83, conv46 15.12), cf95, a8eb; z e327 14.23; aq 4792/11f6 ~14.37; av 023e 13.46; x 236b, s 2f3f noQ0 ~12.
- Pre-screened all 9 (work/prescreen3.log). w's rec-out points are A′: art8 1.5–3e-3, art10 ≤5e-5, shift ≤1%. 236b A′, 2f3f A. z/aq/av points are B: art10 2–3e-4, shift +2.4–3.0%. All shifts positive (24 records now).
- Posted `…183201.484Z_swarm-u_result_d7b7`. The qmax-robust frontier is now min R ≈ 14.6–14.8 (supersedes 11.7–12.3). The top 5 are within the qmax spread. Mailed w (a8eb is safe to claim), z, aq, av.
- Plan: one final check for new records from w/z (still active), then final summary + `swarm done`.

## wakeup 11 (~19:25 UTC) — FINAL
- New w leaders 256c/4b84 (conv46 +2.05/+1.49%, art8 4.5/3.3e-3), b022/e477 (class B, art8 6.2/5.1e-3; predicted conv46 ≈ r46 +2.5–3%). Posted `…192708.028Z_swarm-u_note_70e3`.
- Final summary posted; `swarm done`. 0/500 evals. Open: human request f0fa (qmax ≥12 reruns).
