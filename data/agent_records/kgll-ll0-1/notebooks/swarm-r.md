# swarm-r notebook

Started 2026-10-02T03:52:18+00:00.

## 2026-10-02 04:14–04:22 UTC — wakeup 1 (cold start)
- Read charter, docs 40/46, theory §6.4, kdep_envelope.py, board (14+11 posts). Broker "looks dead" (no ticks); 0 charged anywhere; ~430 requests queued by a–n.
- Parent gaps (swarm reference): w3 s21 4.5716e-4, r46 4.3823e-4; w2 s21 3.2271e-4, r46 3.0955e-4. Doc 46 s21: w3 α[S1,T1]=+0.05 → +1.85 %, −0.05 → −9.0 %.
- Posted hypothesis w3-synth (pooled cross-family model) 20261002T041720.015Z — then found swarm-o posted the same (pooled-surrogate) 1.5 min earlier → WITHDREW, switched to **w2-synth** (note 20261002T042121.615Z). Mailed o to confirm split.
- Posted aliasing note 20261002T041737.441Z (work/alias.py): s21 mesh k=j(5,1)/21; T2≡T5≡T6 on s21; T3 ⟨F²⟩=4/3 on r46; only T1/T2 clean everywhere. (o and m posted the same s21 facts.)
- Built work/pool.py: enumerates every request read-only (swarm.agent ctx.L.inbox), maps block → c(G,R) → s21 fold m=5R1+R2 mod 21 → C6×inversion orbits. Queue audit: w3 315 req / 292 distinct; w2 122 / 110 distinct. b≡f (12 identical w2), d≡i (22 identical w3). Mailed b, f, d, i.
- Geometry for later (MT partner test): mirror G:(m,n)→(m−n,−n); R:(R1,R2)→(R1,−R1−R2); C6 G:(m,n)→(m−n,m); R:(R1,R2)→(−R2,R1+R2); on s21 m→17m. MT image of block: α[o]→α[Mo], β[o]→−β[Mo].
- Ideas not taken: nematic/C6-breaking (symmetry ⇒ linear loss on s21 from splitting C6-degenerate excitations; cheap closure of "less symmetric" item, maybe 6–8 evals later); MT-partner verification of chiral/β candidates.
- NEXT: wait for o's reply + w2 data (b/e/f/j). Then fit w2 orbit model (need result.json format: first completed result). Budget used: 0.

## 04:47–04:52 UTC — wakeup 2
- Broker alive now (human fixed slowness). o agreed: o=w3, r=w2. e: r local Newton |c|≤0.15, e wide α CMA.
- Board highlights: w3 α joint orbits S1T1⟂ / S2T1∥ give big s21 gains (o best 1.609 s21). Chiral β live on T1 (d S4T1 1.036/r46 1.080; i |G|²13). w2: f α-T1 Newton line 1.023 s21 / 1.091 r46 (580e). b: β-U odd parts ≤0.12 (MT parity holds); β[S2,T2] weakly convex. l: w2 chiral β 4× w3.
- Fixed pool.py orbit label collision; wrote work/fitw2.py (pooled per-direction slopes → lstsq gradient) and work/build.py (orbit coords → pair-star block, round-trip verified vs i's ffbc).
- w2 chiral-β mirror-pair modes (2-pt fits at ±0.042): m13a s=−2.44 c=−21; m7a −2.35/−29; m13b −1.33/−23; m3 −1.13/−16; m7b −0.72/−19. Diag model +16 % but sub-additive (l's C7 mix: pred 4.1 %, meas 2.65 %).
- Posted hypothesis 20261002T045105.944Z; submitted batch b1 (10 req, w2, g10, phase-only): N5 λ .3–.9 (4deb.. ids: N2 4deb/e064/8331, N5 16c9/5541/c665/7f96/636e, grad 043d/e3ff). Mailed l, i: they keep single modes.
- NEXT: refit with b1; if N5 sub-additive, fit 5×5 H from line data; consider adding α (f's T1 Newton vector, a different subspace) on top of best β point = cross-subspace test on w2 (o did that on w3).

## 05:07–05:09 UTC — wakeup 3
- b1 landed: all PASS; top-10 w2. e064 (N2 λ.75) s21 1.0768 / r46 1.2045; N5 λ.9 (636e) s21 1.042 / r46 1.2495; s21 optimum ~λ .5 (+7.5 %), r46 unsaturated. r56 pending for all. Posted result 20261002T050857.194Z.
- Board: w3 α×β-chiral superadditive (o 968b s21 1.61 / r46 1.71; p LL-free combos s21 to 2.40). b/p/j/q: S1T1⟂ orbit = half static coherent LL mixing (R = ẑ×G l_B²); S2T1∥ and chiral β are LL-free. Human: converge gate now on r46/r56 only; controls can run on r46/r56.
- w2: w3 α orbits (S1T1⟂, S2T1∥) LOSE on w2 at all radii (f/e far data). w2 best α orbit: |G|²=4 T1 ⟂ ('a:G4:-2,-2|m4|n6'), pooled slope +2.05.
- Submitted b2 (10): aP alone t .03/.05/.08 (a312,a6ab,d572); c665+aP .03/.06 (a3bd,509c); e064+aP .03/.06 (764d,afea); 1.33e064+aP.06 (18ee); 2e064+aP.06 (2882); 2e064+aP.10 (aa4a). Budget used 20.
- NEXT: read b2 cross term; watch r56 of b1 (sign!). If β r56 holds → this is the w2 candidate (phase-only, beyond-M2, no control needed). Do a critique post (rule 11) — candidate: o's/p's huge s21 2.4 points: check entanglement gap/PES and splitting, and conditioning.

## 05:29–05:31 UTC — wakeup 4
- b2 landed (all PASS, r56 pending): best 509c (c665 + aP 0.06) s21 1.137 / r46 1.289. aP alone .03/.05/.08: s21 1.034/1.053/1.063. α×β additive on w2 at s21 (cross ≈ 0), slightly negative at r46 — unlike w3 superadditivity. β increment at fixed M2(k): +7–8 % s21, +18 % r46. r46 keeps rising with β (2e064+a.10: r46 1.39, s21 1.064). Posted result 20261002T053049.769Z.
- Board: w3 LL-free leaders p cc86 s21 2.40 / r46 2.47; o bd1a 2.27/2.63. r56 queue now strongest-first (human). q: r46−s21 = 0.04 + 5 dT (ideality loss) on both parents. i: selection rule (a_{G+Gp} = −R) says chiral β leaders carry static-like content (contested). f, e abandoned w2 α far (w3 plane null on w2). g owns w2 α bases −P1pair (s21-robust: t=.2 s21 1.108/r46 1.131) and combos with e064; l owns single orbits; I keep P4⊥ + β.
- Unit note: my orbit coord a ≈ g's unit-Frobenius / √2.
- Submitted b3 (6): c665×{1,1.25,0.8} + aP {.06,.08,.10} (6be3, 026d, 0b05, 2b27, a8a5, 753b). Budget used 26.
- NEXT: r56 of 509c/e064/c665 is the decision. If positive, ask control? (α part needs matched-density control; β increment doesn't). Owe a critique post (rule 11).

## 05:55–05:58 UTC — wakeup 5
- b3 landed: s21 plateau 1.133–1.139 (best 6be3 = c665+aP.08: 1.1393 / r46 1.3084). r46 rises with α,β. No r56 yet on any of mine (w3 leaders first in queue).
- Withdrew 19 redundant requests from ladder (kept e064, c665, 636e, d572, 6be3, 509c, aa4a for r56).
- Board: claims: p cc86 STRONG w3 (2.40/2.47/2.46/2.47, provisional); d 2400 robust_positive w3 phase-only (1.036/1.080/1.056/1.076). g w2 leader 7f3e (P4⊥ + −P1pair + my e064 β) s21 1.209 / r46 1.368. b: w2 α S4T1-10.9° class +3.29/entry (better than P4⊥). e: w3 leader β patterns lose at α=0. q: r56 keeps ~half the r46 excess for phase-only.
- New tools: --diagnostic (no promotion), --control --clusters, withdraw.
- Posted critique note 20261002T055814.933Z (phase-only gain parent-specific; w2 has it). Mailed e.
- NEXT: wait for r56 of e064/c665 (phase-only w2 claim candidate). If e064 r56 ≥ 1.05 and conv46 ok → robust_positive phase-only w2 claim. Otherwise: consider phase-only optimization targeting min(s21,r46,r56). Budget 26 used.

## 06:27–06:30 UTC — wakeup 6
- Still no r56 on my 7 reps (queue: w3 claims first). Parents' r56: w2 Δ 3.2164e-4 (r46 parent 4 % low per f → r46 R inflated ~4 %).
- Board: claims o bd1a STRONG, p cc86 STRONG (w3, provisional); h fea3 s21 2.80/r46 3.59. c/q: PES ent. gap drops 21 → ~4–5 on amplitude leaders (purity loss tracks ideality loss dT; n: static bands same). g/e reconciled my critique (e agreed scope). b: w2 α leader bb0d (7f3e + S8T1-90° −0.04) s21 1.231 / r46 1.434; b invited me to re-tune β.
- Submitted b4 (6) on bb0d α part: f177 (α-only), 685d (+0.5 e064), 56bf (+1.5 e064), 7e51 (−e064 sign), 8efe (+c665), 3909 (+1.5 c665). Budget 32.

## 06:56–07:00 UTC — wakeup 7
- **e064 (phase-only) broker STRONG**: s21 1.0768 / r46 1.2045 / r56 1.1412 / conv46 1.2043, all PASS, C=1, eg ≈ 6.5. **509c strong**: 1.137/1.289/1.219/1.289. c665 r56 1.1487 (conv pending). Posted CLAIM 20261002T065646.773Z.
- b4 (bb0d α base): α-only f177 1.0456; +0.5e064 1.157; +1.5e064 1.2525; +c665 1.2283; +1.5c665 3909 1.2586 (best); −e064 0.718 (sign lock). β superadditive on strong α base. Posted result.
- Lanes (b's proposal, agreed): b α classes on bb0d/f0fd/0f4e; r β re-tune on b's bases; g β on 0f4e; k Q0-free T2 β; h gradient diagnostics.
- Submitted b5 (5) on f0fd α: c665 ×1.5/2/2.5 (95cb, a5e9, 0c97), e064 ×1.5/2 (71e6, 858e). Budget 37.

## 07:21–07:24 UTC — wakeup 8
- aa4a (2e064 + aP .10) broker STRONG: s21 1.064 / r46 1.393 / r56 1.306 / conv46 1.393, eg ~3.7–4.0, M2k 2.554. → larger β raises the binding clusters (r46/r56) while s21 falls; claim metric favours bigger β than the s21 optimum (s21 only needs sign).
- b5 on f0fd α: c665×1.5 (95cb) s21 1.3331 best; ×2 1.3266; ×2.5 1.3007; e064×1.5 1.3187; ×2 1.3083 (f0fd itself 1.305). b4 r46s: 3909 1.487, 56bf 1.491.
- Board: l claim 9fcb (w2 single orbit m13a β .04: 1.071/1.187/1.128/1.187). g claim 98ec/29a2 (w2 α-only LL-free). e: all claimed points exactly MT-invariant. c, m done.
- b offered fb0c (s21 1.394, base g's 0f4e) — mailed g asking who re-tunes β; not touching until reply.
- Submitted b6 (4) large-β frontier on P4⊥: c665×2+aP.10 (d9ed), c665×2.5+aP.12 (8923), e064×2+aP.14 (f603), e064×2.5+aP.12 (c495). Budget 46.
- Pending r56: 636e (phase-only large β), 6be3, d572, b4/b5 promotions.

## 07:48–07:52 UTC — wakeup 9
- r56 in: 636e phase-only STRONG 1.042/1.2495/1.1845/1.2496 (best phase-only w2 by binding min); c665 strong (r56 1.149); d572 α-only strong 1.063/1.170/1.111/1.170.
- b6: frontier saturates r46 ~1.39 on P4⊥; c495 s21 0.9865 (sign fail). b5 r46 to 1.574 (0c97), r56 pending.
- Human: r56 queue now ranked per parent (w2 no longer starved). g closed β lane on 0f4e → fb0c is mine. e audit: robust tier (split/Δ ≤ 1e-2) top w2 = my 509c.
- Submitted b7 (4) on fb0c α: c665×1.5 a88b, ×2 1f9c, ×2.5 a634, e064×2 cb44. Budget 54. Posted result update.
- Many agents finishing (c, f, m, o done). Plan: after b7 + r56 of b5/b7, write coverage post and consider `swarm done` (w2 β lane will be saturated).

## 08:16–08:18 UTC — wakeup 10
- b7 (fb0c α): cb44 e064×2 s21 1.4932 / r46 1.5045 (w2 s21 best); 1f9c c665×2 1.457/1.501; a634 c665×2.5 1.433/1.500; a88b c665×1.5 1.431/1.463. r56 pending for all b4–b7.
- Board: many finals (j, p, q). q: s21 is the low outlier, r56 ≈ 80 % of r46 slope. i starting static-free-w2 CMA.
- Submitted b8 (3) on fb0c: e064×2.5 (5292), ×3 (3e43), c665×3 (b421). Budget 57. Mailed b.

## 08:47–08:49 UTC — wakeup 11
- b8 (fb0c α): e064×2.5 (5292) 1.482/1.539; ×3 (3e43) 1.444/1.535; c665×3 (b421) FAIL manifold split/Δ 0.127. β optimum on fb0c ≈ 2–2.5× e064.
- Board: b 879b α (s21 1.507/r46 1.490, purity thin split/Δ 0.045, eg 3.0); g Sobol 1909 1.513/1.539 clean (sp/D .007). k refuted p's 9fc9 (near manifold gate). Many agents final (o, p, q, j, c, f, m).
- Submitted b9 (3) on 879b α: e064×1.75 (7fc5), ×2 (bf94), ×2.5 (9857). Budget 63.
- Still no r56 on any b4–b8 point. Plan: one or two more wakeups for r56, then coverage + done.

## 09:17–09:20 UTC — wakeup 12
- b9 (879b α): bf94 e064×2 s21 1.5478 / r46 1.5911; 9857 ×2.5 1.5444 / 1.6437; 7fc5 ×1.75 1.540/1.560. Purity thin: s21 split/Δ .06–.08, eg ~2.8 (N_A=3 ~1.7).
- Withdrew 14 more redundant points. r56 reps: 6be3 3909 95cb 0c97 cb44 5292 bf94 9857 f177.
- Posted result+coverage 20261002T092004.293Z; closing β lane. Mailed b.
- NEXT: one long wait for r56 of bf94/9857/cb44 etc.; if strong, post claim note (with split/eg caveat); then `swarm done`. Budget 63 (no more submissions planned).

## 10:06 UTC — wakeup 13: DONE
- r56 legs still pending (g's sobol leaders 1.76 ahead in queue). Lane saturated; posted `swarm done` summary. 63/500 charged.
