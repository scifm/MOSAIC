# swarm-k notebook

Started 2026-10-15T04:13:27+00:00.

## 2026-10-15 04:33 — wakeup 1: scope chosen, stage A submitted
- Board at start: swarm-a w3 separable atlas, swarm-b w3 joint (G,R) classes, swarm-c w2 separable atlas, swarm-e w3 big amplitudes, swarm-g MT-symmetry note (β-odd = cluster-shape artefact on achiral directions; all clusters mirror-asymmetric).
- Store pattern: gains only α on |G|²=1×|R|²=1. b's θ=90° class (G⟂R) c=+0.05: s21 1.105, r46 1.088 (req f06f). w2 S1×T1 gain at α<0 (c req 5515: s21 1.026, r46 1.080). Everything else < 1; big amplitudes (e) strongly negative (0.15–0.67).
- Idea: e^{iG·r}ψ_k = e^{ik·R'_G}(cyclotron op)ψ_k with R'_G = l² ẑ×G (lattice vector at 1 flux/cell; |R'|=|G| in campaign units). Matched perpendicular pairs (|R|²=|G|², θ=90°) carry a k-independent cyclotron (scalar coherent LL mixing) piece at half weight (cos⊗cos locks R and −R). Block cannot express sin⊗sin, so pure f(r−X) is not representable.
- Tools: work/classes.py (class builder; verified = b's d1), work/board_table.py (store table), work/gen_stageA.py.
- Posted hypothesis kgll-cyclo (…_75cb). Submitted 30: w3 (1,4),(3,3),(4,4) × {30,90,150} × ±0.05; w2 (1,1),(3,3) × same. Mailed b and c.
- Next: read results; if 90° matched classes respond, line-search them and combine across harmonics; request matched-density control for any α winner.

## 2026-10-15 05:05 — wakeup 2: stage A posted; pivot to critique/check
- Stage A (30) result posted (…_result_1feb): matched-⟂ gain S1-only on w3; (3,3)⟂ odd +0.015, (4,4)⟂ none; w2 ⟂ loses, oblique 30/150 at α<0 wins (580c: s21 1.038 r46 1.044 r56 1.043). |R|²=3 M·T mirror-pair split 2.3% on s21 (w2 (3,3)). Duplicated 6 of swarm-i's w2 runs — ALWAYS swarm show before submitting.
- Board state: S1⊥ α=0.2 (j 7d04) claimed `strong` (s21 1.369, r46 1.386, r56 1.306, conv46 1.386). Mechanism controls (a,l,m,q,r): matched ρ̄ ≈ 1.00; M2-matched static 1.18–1.20 < 7d04 → beyond M2; uniform-parent S1⊥ loses (o, m) → parent-dressed, not pure LL mixing.
- Guiding-centre resonance rule (G±G_R on parent shell, sign = parent weight): fits S1⊥, S2∥=(3,1)θ0 (b a90f 1.0995), w2 oblique, w2 (4,1). swarm-r says not predictive; counterexample S1×T(3) θ0 — but that is s21-only, where |R|²=3 is two-valued.
- Taken by others: S2∥×S1⊥ grid (r), w2 (1,3),(3,1),(1,4),(4,1),(4,4) (i), outer-shell resonance (o, l), re-centred atlas (d), CMA 14-D (a), chiral l=2 (q).
- Submitted 4 controls (family kgll-t3fs, --control --clusters r46,r56): b's S1×T(3) θ0 ±0.05 (0888 +, 84b7 −), θ60 ±0.05 (34be +, dee0 −). Posted note …_note_5db3, mailed r.
- Charged so far: 30 (+8 control evals pending).
- Next: read the controls; post the outcome. Consider whether any uncovered direction remains (w2 is less covered than w3).

## 2026-10-15 05:25 — wakeup 3
- Controls r46 (r56 pending): S1×T(3) θ0 (resonant) +0.05 0.9801 (0888), −0.05 0.9948 (84b7) → odd −0.007, wrong sign for rule. θ60 +0.05 1.0182 (34be), −0.05 0.9940 (dee0) → odd +0.012; s21 had 0.9594/0.9603 → 6% s21–r46 discrepancy on a T(3) direction.
- So far: swarm-r's counterexample survives on r46; consistent with swarm-m's "rule works on T1 only" (T2/T3 suppressed by |R|).
- Board: w3 leaders h 0672 (S1⊥ + chiral β S7/S13: s21 1.427 r46 1.461 r56 1.440); r S2∥ α=0.2 alone s21 1.452 r46 1.413; n static sharpened w3 reaches 1.45 at M2=8 (control) → parent-relative headline caveat. w2: g strong 141f (1.114/1.149/1.131/1.147); i (4,1)⊥ r46 1.141; c combining.
- Everything I'd do next is covered (p xcombo, a CMA, c w2-g4perp, o/l/m resonance). Plan: post control outcome, then slow cadence; consider swarm done if nothing uncovered.

## 2026-10-15 05:45 — wakeup 4
- My r56 controls still queued. Leaders: p fe3d (S2∥ 0.25 + chiral β 7×T1) 1.69 on all 4 clusters (claim strong); b 02f7 (same α, β up to 0.08) s21 2.38, r46 2.59, r56/conv46 pending — diagnostics clean (adm 0.82, M2k/M2 1.42, split/gap <0.7%, PES gap ~5). conv46 (g_cutoff 10, n_mesh 64, qmax 10) will test truncation for free.
- w2: c df59 strong 1.162/1.208/1.189/1.208. a's 14-D CMA all below 7d04; a now 8-D stack CMA.
- No uncovered direction for me. Plan: post control outcome once r56 lands, then swarm done.

## 2026-10-15 06:08 — wakeup 5
- Posted kgll-t3fs result (…_result_a512): S1×T(3) resonant θ0 class odd −0.007 on r46 → swarm-r's counterexample stands, my objection withdrawn; T2 s21→r46 shift up to +5.9% (θ60: s21 0.959, r46 1.018) → T2/T3 s21 nulls are weak.
- Board: leaders 02f7 (s21 2.38, r46 2.59, r56 2.53, converged −0.55% at n_mesh 64/g_cutoff 10), c89a/h 19@67° s21 2.44–2.45 / r46 2.82–2.94. Static frontier ~1.58 (n). Verification done by f, n, o, q, d. Heavy herding on chiral-phase stacking (g's note).
- Decision: no uncovered direction for me; don't add to herding. Go to waiting with ~1 h cadence, in case human answers (j's sin·sin chart extension, n's sharpened-parent + k-dependence) open a new niche. If none after 2 checks → swarm done.

## wakeup 6 (2026-10-15 ~07:10Z)
- Board moved: w3 frontier now o's 90a9 (713b with β×1.45) s21 5.114 / r46 6.036 (r56 pending); a's b4b8 strong (min 4.50); r's kshape S2⊥-T2 axis transfers (db79). w2 leader e's a9a7 1.307. Many agents done (d, g, i, m, n).
- Found: 90a9 has Σ|β| = 1.943 (cap 2.0), so the radial β line is blocked by the campaign boundary. PES ent. gap drops 20 → ~4.5–5 at the frontier (still ≫ 0.5).
- New family w3-bcap (hyp 4dcf): 9 s21 screens at Σ|β|=1.998, ±0.025 per-entry shifts per class (7/13/19/21 × T1), others rescaled proportionally; α = 90a9. Inputs in work/bcap/in, generator work/gen_bcap.py (reads 90a9 ed_input). Mailed a, o.
- Reqs: ae17 g13dn, 4431 g13up, bb06 g19dn, cd23 g19up, 01d8 g21dn, 55b2 g21up, 328c g7dn, e6f2 g7up, cc64 p0.
- Next: read results vs 90a9 s21 5.114; if a direction gains ≥3%, take a second step (≤10 more); post result + coverage.

## wakeup 7 (~07:40Z)
- bcap step 1 is done (s21/r46): 19up cd23 5.600/6.621 (#1 s21), 21dn 01d8 5.501/6.793, 13dn ae17 5.456/6.205, uniform cc64 5.217/6.142. Gradient (7, 13, 19, 21): s21 (+6.2, −6.7, +16.6, −16.1), r46 (+8.5, +1.3, +17.4, −27.2). The PES gap is anticorrelated with R (4.1–4.7).
- Step 2 is in work/bcap/in2 (gen_bcap2.py): avg-grad steps 0.025/0.04/0.055/0.07 (62a1, 2026, 1d7d, 5dad), s21-grad 0.05 (fec3), sparse no-21 (0039). Posted interim result. o said go ahead (mail 8213); o asked the human whether the Σ|β| cap is physics or box (request 752c).
- Next: read step 2. If it's still rising at the β21 → 0 end, the remaining direction is 13 → 0, then α reallocation? Keep the family ≤ 20, then close with coverage.

## wakeup 8 (~08:05Z)
- Step 2: fec3 (s21-grad 0.05: .1525/.0175/.1400/.0229) s21 5.943 / r46 7.204 is the best. avg steps 62a1 5.66/6.88, 2026 5.72/7.02, 1d7d 5.57/6.92, then a cliff: 5dad (β21 .002) 4.23/6.52, 0039 (β21 = 0) 3.29/6.46. So β21 must stay at ~.02–.035; s21 is sharply sensitive there while r46 isn't.
- Ladder finished: 01d8 s21 5.501 / r46 6.793 / r56 6.782 / conv46 6.885; cd23 5.600/6.621/6.438/6.519; ae17 5.456/6.205/5.980/6.114. All PASS.
- Step 3 (in3, gen_bcap3.py), 5 local moves at fec3: 13 → .008 into 19 or into 7, 7↔19 ±.015, β21 +.007. Family total 20 = the hypothesis budget.
- Then: wait for fec3's ladder, post the claim and close-out with coverage.

## wakeup 9 (~08:28Z)
- Step 3: e5e5 (13 → 19: .1525/.008/.1495/.0229) 6.175 / 7.393 is the best; 6b3a 6.091/7.275; 6a6d (7 → 19) 6.071/7.389; e849 (19 → 7) 5.765/6.995; 4808 (β21 + .007) 5.973/7.201.
- Note 3eab: family budget extended to ≤35. Step 4 (in4): 7a0f comb (.1375/.008/.1645/.0229), c824 β19 .18, 43fc β13 = 0, 2673 β21 .030, 6eb3 β21 .016.
- Withdrew the weak points (55b2, bb06, 4431, 328c, e849) to free the r56 queue. Kept 0039 and 5dad for the s21-cliff finite-size check.
- Next: continue along 19 if it is still rising; consider per-class α reallocation, since α is still uniform at 90a9's; claim the best point once its ladder completes; close out with coverage.

## wakeup 10 (~08:55Z) — closing
- Step 4: 43fc (β13 = 0) 6.418/7.691, c824 6.315/7.701, 7a0f 6.268/7.559. fec3 ladder done: 5.943/7.204/7.320/7.282. e5e5 r56 7.509.
- a's 9a85 (8.13/8.85/9.09/9.04, strong) has the same β allocation (.108/.027/.176/.021) and also reallocates α at the Σ|α| cap. My family is dominated and covered, so I closed it (result b372, with coverage) and withdrew the dominated promotions.
- Ran swarm done with summary work/done.md and stopped the loop.
