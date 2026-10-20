# swarm-g notebook

Started 2026-10-08T04:34:53+00:00.

## 2026-10-08 05:00 — wakeup 1
- Read docs 40, 46, swarm reference. Parents: w3 Δ s21 4.5714e-4 (density on |G|²=4,12,16 → a/2 superlattice); w2 on |G|²=3,9,12 (√3 superlattice).
- Doc 46 at Nk=21: w3 α[S1,T1]=+0.05 → +1.85 %, −0.05 → −9.0 %, β +0.05 → −4.4 %, α[S3,T1]+0.05 → −3.75 %.
- swarm-c claimed atlas-T1-w3 (10 stars × T1, α {−.1,−.03,.03,.1,.3}, β {±.03,±.1}).
- I took **atlas-T23-w3**: 10 stars × {T2,T3}, α ±0.1, β ±0.05, n_mesh 48, g_cutoff 8. 80 evals submitted (hyp post 20261008T050034.255Z_swarm-g_hypothesis_ff74). Inputs work/atlas23/, generator work/gen.py (make(terms) helper).
- Limitation noted on board: block only gives even×even cos·cos products; no odd×odd (k-dependent translation).
- Next: collect atlas (swarm show → request.source gives label), post slope table, then extend positive directions; coordinate with swarm-c on CMA-ES in positive subspace.

## 2026-10-08 05:22–05:35 — wakeup 2
- atlas-T23-w3: 77/80 landed, all < 1 (best 0.969 S1T3 α−0.1). Posted result + coverage 20261008T052426.396Z_swarm-g_result_41df. Family closed. (swarm-f duplicated T2 α, agrees to 4 digits.)
- Board state: leaders are the S1T1⟂ (co-moving) + S2T1∥ invariant orbits on w3; s21 up to 1.50 (swarm-e plane), r46 1.17 (swarm-i). Heavy herding on co-moving w3.
- Key facts: swarm-h Z2 rule (w3 half-translations; invariant pairs m≡R2, n≡R1 mod 2); w2 has Z3 (m+n≡0 mod 3); s21 closed under Z3 but not Z2; breaking directions give a linear cone at s21.
- MY INSIGHT (note 20261008T053040.757Z_swarm-g_note_8a81): pair term = 2 halves with offsets L = G ∓ G_c(R), G_c(R)=(R2,−R1). Half is invariant iff L is in the parent lattice. Empirical rule: slope ≈ Σ κ w_L; L=0 (pure co-moving) ≈ 0 (w2 S1T1⟂ 0.954/0.968). All measured orbits fit in sign. Predictions listed. Tools: work/umklapp.py (table), work/gen_orbit.py (pairs(par,s,t,tag), make(par,[(pairs,a,b)])).
- Submitted umk-w2 (12 evals, w2, ±0.1 orbit): null tests S3T3_L0, S7T1_21, S8T1_21, S9T1_21, S9T1_27 (predict ≈0), and S8T1_9 (predict gain at α>0).
- Mailed ad, ac, p, as, h, ar, m.
- Next: score the predictions against umk-w2 and others' data (w3 S1T2 invariant orbit, S4/S5×T1, S3T3; w2 S1T3, S4T1 from swarm-ar). If the rule holds, a design rule follows: target the highest-|w_L| offsets with sign(α) = sign(w_L).

## 2026-10-08 05:48 — wakeup 3
- umk-w2 results: the zero-weight null tests have odd parts of 4–8 %/0.1; S8T1_9 has the wrong sign (gain at α<0: 1.0099, req …161d); the S3T3 co-moving orbit on w2 has odd −0.043/0.1.
- The rule is refuted by me, by swarm-b (w3 S1T2∥ flat) and by swarm-z (S3T3 flat). The L=0 part is confirmed on uniform LLL (ao, as). Posted refutation 20261008T054914.168Z_swarm-g_refutation_d405 (with coverage). b's e^{-|R|²/4} amendment also fails (w2 T3 co-moving slope −0.43/unit A).
- Board: e's plane S1T1⊥×S2T1∥ reaches r46 1.41; chiral β S4/S7/S9/S10×T1 gives r46 up to 1.54 but r46≫s21 (k critique). Parent r56 still pending → no r56 R yet.
- Next: data-driven gradient for w2 from all measured w2 orbit slopes (work/w2slopes.py → work/w2_rows.json), then a line search. Check n (w2-opt) and as (rule-w2) for overlap.

## 2026-10-08 06:05 — wakeup 4
- w2 frontier: m (s21 1.16), ar (S3T1⟂ ⊕ S4T1 gradient), as and ag (rule-designed, from my refuted rule), a (hiorb-w2). Saturated, so I did not open my planned w2 Newton combination. Per-orbit Newton numbers (s21, unit A): S3T1d1 s=+1.57, e=−9.5; S1T1 d0 −0.74/−3.6; d2 −0.78/−3.7; S8T1_9 −1.15/−10.5.
- w3 leaders are now about 2× (am 08b5 s21 2.05 / r46 2.06; j ba1f 2.03 / 2.23; j fe2e 1.63 / 2.63, which is clean: PES and Chern pass at r46). Chiral-β dressing on the S2T1∥ / S1T1⟂ amplitude leaders. r56 is still pending for everyone, parents included.
- s21 momenta: k = (5j mod 21 /21, j/21), j = 0..20 (julia/src/geometry.jl).
- ED-free test (work/meshm2.py → meshm2_w3.txt): cluster-sampled M2 is identical across s21/r46/r56 to < 0.5 %, so mesh sampling of the density does NOT explain the s21→r46 drifts. Post as a null once the run finishes.
- Role going forward: verifier/reserve (≈408 evals). The compute queue (r56) is the bottleneck, so I am not adding screening load.

## 2026-10-08 06:31 — wakeup 5
- r56 is stalled for everyone (swarm-c filed a request to the human). Many agents are in reserve (at, x, u, w).
- Posted the ED-free mesh-M2 null (199 w3 entries; M2 ratios ≤1.8 %; corr 0.17 with the R drift).
- Board highlights: w3 leaders reach about 2.0–2.5 at s21 (t 0e99 2.478) with chiral-β dressing. Chiral dressing transfers to w2 (b: d43f 1.16→1.30). My offset rule is dead (b, ag, as all closed rule designs).
- Holding budget (408). Next: watch for r56; offer targeted verification.

## 2026-10-08 07:02 — wakeup 6: DONE
- Swarm converged: more than 10 reserve agents, r56 stalled, all directions covered. Closing with `swarm done` (92/500 used). The atlas final count is 62 PASS / 18 FAIL (S9T3 last 3 FAIL).
