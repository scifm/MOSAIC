# swarm-c notebook

Started 2026-10-13T18:08:48+00:00.

## 2026-10-13 18:18 — wakeup 1: scope + map batch b1
- Read brief, docs 40/46, theory §6.4, notes §5.6–5.7, §12. Board: swarm-a took `w3-map` (star products S1..S10×T1..T3, α/β ±0.05, single terms, g_cutoff 6).
- Key priors: doc46 Nk=21 w3: α[S1,T1]=+0.05 → +1.85 %, −0.05 → −9.0 %, β +0.05 → −4.4 %, α[S3,T1] → −3.75 %. Pilot 024: 4×6 gains flipped at 5×6. Odd part is cluster-specific; even part looks negative (ideality defect ∝ |α/2+iβ|²|R|²).
- w3 density lives on |G|²=4,12,16 (half-period); w2 on |G|²=3,9,12 (√3 sublattice).
- MY FAMILY `w3-joint` (hypothesis 20261013T181553.718Z_swarm-c_hypothesis_298a): joint-C6 orientation channels. Tool `work/kgen.py` (fixed dual-basis bug: A = inv([G1;G2]) columns). Per (6-mem G shell, 6-mem R star) 3 channels by angle Δ(G,R) mod 180. |G|²=1,4 × T1: Δ∈{30,90,150}; |G|²=3 × T1: {0,60,120}. Mirror: Δ↔180−Δ. Channel c → c/√3 per pair entry; star product = ΣC/√3.
- File naming: g{|G|²}T1_d{Δ}_{ap,am,bp,bm}, c_α=±0.08, c_β=±0.04, g_cutoff 6, n_mesh 48.
- Submitted b1 (36 reqs), mapping in work/reqs.tsv.
- NEXT: collect b1, compute odd/even parts per channel, compare channel sums with swarm-a star numbers; then line searches / CMA-ES.

## 2026-10-13 18:38 — wakeup 2: b1 results → robust_positive
- b1 (36 s21, all PASS). Winners: α on achiral channels **g1 Δ90 (G⊥R) c=+0.08 → req_3182** (s21 1.0966, r46 1.0810, r56 1.0849, conv46 1.0810) and **g3 Δ0 (G∥R) c=+0.08 → req_68f6** (s21 1.0916, r46 1.0843, r56 1.0818, conv46 1.0843). Both broker-labelled ROBUST_POSITIVE. −α side: 0.845/0.851. All β < 1. |G|²=4 all channels < 1. Mirror pairs 30/150, 60/120 agree ≤1% and lose.
- M2^(k)/M2 only 1.011–1.013; R_beyondM2 0.740 vs parent 0.690. Control needed (α≠0).
- Posted result f31b, claim 7999, request 6d34 (control construction + conv46 qmax question: parent conv46 Δ == r46 Δ to 7 digits).
- Board: swarm-a w3-map (whole stars; S1T1 α 0.08 r46 1.040), swarm-b w2-map-cma, swarm-d w2-orient (transfers my channels to w2; w2 s21 1.035), swarm-e w3-orient (duplicate of my map) → mailed split proposal: I keep amplitude optimization + analogues; e takes 12-member shells + β.
- b2 submitted (28, mapping reqs_b2.tsv): α lines c=0.12..0.40 for both winners; combo both (0.06,0.08,0.12) and (+,−); analogues g1T2Δ0, g3T2Δ90, g9T1Δ90, g12T1Δ0, g1T3Δ90, g3T3Δ0 at ±0.08.
- Collector: `uv run ... python work/collect.py work/reqs_b2.tsv` (run from work/).
- NEXT: read b2; find line optimum; combos; then CMA over achiral winners (maybe + small β); watch for human reply on control.

## 2026-10-13 18:57 — wakeup 3: b2 → STRONG
- b2: g3Δ0 line: c .12 1.140/1.133, .16 1.192/1.185, .20 1.247/1.242, .24 1.304/1.304, **.32 8617 s21 1.419 r46 1.401 r56 1.352 conv 1.403 STRONG**, **.40 3faf 1.495/1.419/1.467/1.420 STRONG** (M2k 1.218/1.356). g1Δ90 saturates ~0.32–0.40 (ab9c 1.368/1.360; d025 1.353/1.363).
- Combos equal c: .08 ddbc 1.193/1.164/1.166; .12 89a6 1.299/1.255/1.256 (additive). Opposite sign 4616: 1.010, M2k 0.999.
- Analogues on T2/T3, |G|²=9,12 all lose at ±0.08. Gain is specific to T1 × |G|²=1,3.
- Posted result 3eab, claim 6021 (STRONG; M2 caveat). Mails to a/d/e. swarm-d: R_beyondM2 peaks c~0.3, beyond tracks M2k (note 6ebe). swarm-e → mechanism (geometry proxy). swarm-a → surrogate (multi-channel; I said other channels are theirs). swarm-b → w3-hichan (S4–S10). swarm-d → w2-orient (w2 winner g4Δ90).
- b3 submitted (19, reqs_b3.tsv; gc 8): g3Δ0 c .48 .56 .64 .80 .88; .40 gc8 repeat; g1Δ90 .28 .36; 2D grid g3Δ0 × g1Δ90.
- Human has not answered request 6d34 yet.
- NEXT: b3 → locate the 2D optimum; if g3 line keeps rising, the M2k ≤ 3 boundary binds (c=0.96 rejected at 3.10).

## 2026-10-13 19:16 — wakeup 4: b3 → line optimum
- g3Δ0 gc8: .40 6f32 s21 1.500 r46 1.420 r56 1.456 conv 1.4195 (strong); .48 1.517/1.394; .56 1.477/1.321; .64 1.379/1.202; .80 FAIL(PES) 1.02; .88 FAIL 0.78. r46 optimum ~0.40–0.44.
- g1Δ90 .28 1.351/1.309, .36 1.368/1.383 (plateau ~1.37).
- 2D plane: adding g1Δ90 (either sign) near the optimum hurts; at equal M2k R differs by up to 15% → posted result+critique (R not a function of M2k).
- Controls by others: swarm-b static ρ̄/frozen-k all ≤1.024 at s21 (46cb); swarm-e matched-M2 statics 0.79–0.985 s21. Human not yet replied to 6d34.
- b4 submitted (16, reqs_b4.tsv): c .36/.44; β on top of .40 (same channel ±.04/±.08, g1Δ90 ±.04, g3Δ60/120 ±.04); α g3Δ60+120 ±.08; α g1Δ90 ±.04 on top.
- Budget ~118/500.
- IDEAS NEXT: if nothing on top helps → small CMA (6–8 dims: g3 3 channels α + β, g1Δ90 α, g4 channels) around c=.40 seeded; or check w3 at T1 with |G|²=3 Δ0 + |G|²=12 Δ0 (2G collinear: swarm-a's w3-profile does that—avoid).

## 2026-10-13 19:32 — wakeup 5: b4 flat → start CMA
- b4: everything on top of g3Δ0 .40 gives r46 1.37–1.42; max still 1.420 (6f32/1f7f/08ff). c .36 r46 1.416, .44 1.413.
- Posted b4 result with coverage block for w3-joint (99 reqs; best 6f32 R_min 1.4195 strong).
- swarm-a w3-profile: 3G (g9Δ90) at −0.12 on g1Δ90 c=.24 → r46 1.397 with M2k down (beyond-M2 handle).
- Started `w3-cma` (hyp 3147): work/cmarun.py, state work/cma_state.pkl, gens in work/cma/gNN. 8 dims: g3d0,g1d90,g9d90,g12d0,g3d60+120,g1d30+150,g4d90,g4d30+150. λ10 σ0 .06 seed 20261013. Objective min(s21,r46). `python cmarun.py step` each wakeup (tells when all fitness in, submits next gen). Budget 60.
- Gen 0 submitted.

## 2026-10-13 19:55 — wakeup 6: CMA gen0
- gen0 best **ece3 (20261013T193129.319Z_swarm-c_req_ece3)**: s21 1.696 r46 1.681 r56 1.653 conv 1.680 STRONG, M2k ratio 1.276. Coeffs g3d0 .475, g9d90 −.099, g4d30+150 −.071, others small.
- New mean g3 .457, g9 −.06; σ .056. Gen1 submitted.
- swarm-a: g1 square-wave (g1d90 .48 + g9d90 −.32) 7b81 r46 1.655 r56 1.660; b5 extends to .80 + g3 on top. Split: a=lines, c=CMA.
- swarm-b k-reassign: h'_k = h_{k+M} kills gain (6f32 1.50→0.60): gain is in k-assignment.
- swarm-d: STRONG on w2 R_min 1.161.
- NOTE: cma_state.pkl pickles __main__.CMA → only load via `python cmarun.py step`.

## 2026-10-13 20:17 — wakeup 7: CMA gen1
- gen1 best edef [g3 .521, g1 −.037, g9 −.125, ...] min(s21,r46) 1.710; 597a 1.649. Mean → g3 .465, g9 −.101; σ .054. Gen2 submitted.
- swarm-a: g1sq+g3: 0208 (g1 .40, g9 −.27, g3 .16) s21 1.901 r46 1.802; a76c (g1 .48 g9 −.32 g3 .16) s21 1.955 r46 1.787. b6 grid around 0208.
- Added `cmarun.py recenter '<json x>' sigma`. PLAN: after gen2 tell, recenter at best overall (likely 0208: [0.16,0.40,-0.27,0,0,0,0,0]) σ .08, fresh C.
- swarm-b mech table: static ≤1.02 at r46; k-reassignment collapses every winner. swarm-d w2-cma started (w2 best 1.178).
- Next wakeup: `python cmarun.py step --no-submit` → `recenter '[...]' 0.08` → `python cmarun.py submit`.

## 2026-10-13 20:40 — wakeup 8: CMA gen2 → 38fd R_min 1.986
- gen2 best **38fd (20261013T201600.506Z_swarm-c_req_38fd)**: s21 2.072 r46 1.988 r56 2.065 conv 1.986 STRONG; PES 3.6–4.3. x=[g3 .537, g1 .070, g9 −.229, g12 −.004, g3d60+120 −.003, g1d30+150 .001, g4d90 .096, g4d30+150 −.021]. M2k 1.377.
- Did NOT recenter (CMA beats swarm-a's 0208/b30d 1.80/1.82). Gen3 submitted (mean g3 .511 g9 −.187 σ .06).
- Claim posted. Mailed swarm-a: bridge line b30d ↔ 38fd.
- swarm-d critique 5a4a: PES ent gap falls with R (still ≫0.5).

## 2026-10-13 21:00 — wakeup 9: CMA gen3
- gen3 best 3dcc 1.965, a411 1.915; none beats 38fd 1.988. Mean [g3 .505, g1 .111, g9 −.218, ...] σ .066. Gen4 submitted (40/60 CMA budget).
- swarm-a: bridge line b30d→38fd queued (w3-profile); b7 higher harmonics null at 0208. swarm-b: chiral phase-only S4 lead r46 1.27 but s21 1.05 (artefact checks). swarm-e: 891b strong on w2 (1.202). r56 queue may be stuck (swarm-b request 12f0).

## 2026-10-13 21:23 — wakeup 10: CMA gen4 → 0fea R_min 2.145
- **0fea (20261013T205941.594Z_swarm-c_req_0fea)** x=[g3 .580, g1 .144, g9 −.357, g12 .045, g3d60+120 .048, g1d30+150 −.027, g4d90 −.023, g4d30+150 −.006]: s21 2.222 r46 2.148 r56 2.355 conv 2.145 STRONG; Σ|α| 2.185 (box 2.5!), M2k 1.402. 7012 2.043.
- Gen5 submitted (mean g3 .553 g1 .122 g9 −.304, σ .072). Extended CMA budget 60→120 (claim post says so). Charged 149/500.
- Σ|α| ≤ 2.5 will bind: repair loop pulls toward mean; if mean itself violates, need projection. Watch.
- swarm-a: bridge b30d→38fd is one ridge; now off-T1 add-ons on 38fd (w3-offT1). swarm-b: chiral phase-only S4 lead β-odd robust.

## 2026-10-13 21:45 — wakeup 11: CMA gen5
- gen5 best 3944 [g3 .679 g1 .127 g9 −.36 ...] s21 2.182 r46 2.170 (Σ|α| 2.317, M2k 1.546). Gen6 submitted; its samples at Σ|α| 2.45–2.49 → box binds.
- Side test `rad/` (5, reqs_rad.tsv): 0fea projected on (g3,g1,g9) only, scaled ×1.0,1.1,1.2,1.3,1.33 (Σ|α| 1.87→2.49). Asks: do minor coords matter; does R keep rising along the ridge to the box.
- swarm-a off-T1 (T2/T3 add-ons on 38fd) mostly null. w2: swarm-e 044c R_min 1.220; swarm-d ffc2 1.226.
- Charged ~174/500.

## 2026-10-13 22:08 — wakeup 12: radial line; close w3-cma; start w3-cma2
- Radial (0fea → g3/g1/g9 only, scaled): ×1.0 r46 2.174 (> 0fea); ×1.33 bbe1 s21 2.825 r46 2.313 at Σ|α| 2.49. α ridge is boundary-limited.
- CMA gen6 told (best 1079 2.089); w3-cma CLOSED (75 evals), result c71c with coverage.
- swarm-a ae41: chiral |G|²=7 phase (+C130.9 −C49.1)/√2 at β .06 on 0fea → s21 2.740 r46 2.843; their β line to .20 + symmetric-combo artefact control queued.
- Started **w3-cma2** (hyp cdfa): work/cmarun2.py, state cma2_state.pkl, dirs cma2/gNN. Dims [α g3d0, α g1d90, α g9d90, α g12d0, β g7 131−49, β g13 164−16]. x0 [.696,.173,−.428,0,.06,0] σ .05 seed 20261014. Run `python cmarun2.py step`.
- Charged ~189/500.

## 2026-10-13 22:30 — wakeup 13: cma2 gen0 pending
- All 10 gen0 still pending (queue). swarm-a 51de: chiral |G|²=7 β line on 0fea still rising at β=.20 (s21 3.43 r46 3.89 r56 3.77); mirror control passes; swarm-a request 3420 asks human for gauge-covariance sanity check before claiming R≈3–4. My cma2 x0 β=.06 is far below → expect CMA to push β up; consider recentering β≈.2 after gen0.

## 2026-10-13 22:38 — wakeup 14: cma2 gen0 → recenter
- cma2 gen0 best a809 [α .705,.126,−.48,.066; β7 .127, β13 .009] min(s21,r46) 3.313; 46f5 3.214; 906a 3.107.
- swarm-a b12: β7 line on 0fea: s21 peaks β≈.40 (3.919), r46 peaks ~.50 (5.16); d48b (.40) r46 5.013 r56 4.882. β13 +.04 adds a little.
- Recentered cma2 at [.697,.165,−.432,.026,.40,.04] σ .07, fresh C; gen1 submitted.
- swarm-b critique 926f: expose low_energies to separate gap from energy-scale increase (relevant to R≈3–5 claims). swarm-a asked human sanity check (3420).
- swarm-d w2 best 1017 R_min 1.264.

## 2026-10-13 22:59 — wakeup 15: cma2 gen1 → 4462 R_min 4.18
- **4462 (20261013T223617.093Z_swarm-c_req_4462)** [α .652,.109,−.481,.046; β7 .401, β13 .016]: s21 4.182 r46 5.462 r56 5.344 conv46 5.564 STRONG. conv46−r46 +1.9% (convergence degrading at large β). 777a 4.175/5.418/5.330.
- Gen2 submitted (mean [.684,.119,−.472,.029,.407,−.008] σ .064). Claim posted with caveats (sanity 3420, low_energies 926f, convergence).
- swarm-a closed w3-profile & w3-offT1; now w3-convcheck (gc/n_mesh at large β). If gc8 biased → switch cma2 to gc10.

## 2026-10-13 23:21 — wakeup 16: cma2 gen2
- gen2 best **9d3e (20261013T225815.256Z_swarm-c_req_9d3e)** [α .733,.069,−.628,.004; β7 .356, β13 −.012]: s21 4.823 r46 5.709 r56 5.586 (conv46 pending). Σ|α| 2.483 (BOUNDARY), M2k ratio 1.198 (lower than 0fea!). a6ff 4.735.
- Gen3 submitted (mean [.711,.095,−.568,.02,.383,−.041] σ .070).
- swarm-a convcheck: s21 converged 0.15% at gc8; conv46−r46 drift likely qmax-10 on candidate only (my 6d34 item 2) → quote r46 not conv46.
- TODO: claim 9d3e when conv46 lands; mention boundary + M2k falling.

## 2026-10-13 23:45 — wakeup 17: cma2 gen3 (flat)
- gen3 best a9bc 4.743 (<4.82). 9d3e ladder done: s21 4.823 r46 5.709 r56 5.586 conv46 5.766 STRONG; claimed (boundary). a6ff strong 4.735.
- Gen4 submitted (mean [.646,.079,−.546,.008,.375,−.05] σ .069). cma2 budget: 50/60 after gen4.
- swarm-e mapping 6-shell chiral phase combos on d48b (w3-phasemap); offers coords for my CMA.
- Charged ~239/500.
- PLAN: after gen4: if no gain, stop cma2; maybe a cma3 adding swarm-e's best 6-shell phase coords; or finish with coverage + confirm runs.

## 2026-10-14 00:06 — wakeup 18: cma2 gen4 → 5.34
- **bb15 (20261013T234306.736Z_swarm-c_req_bb15)** [α .636,.125,−.526,−.016; β7 .535, β13 −.187]: s21 5.345 r46 5.975 r56 5.819 (conv46 pending). Σ|β| 1.77 (box 2.0), Σ|α| 2.26. 1844 s21 5.341 r46 6.009.
- Gen5 submitted (mean [.646,.13,−.547,−.017,.494,−.14] σ .081). Budget extended 60→100 (note posted). Charged 224/500 (broker count).
- swarm-a DONE (214 evals). swarm-e closed w3 families (6-shell chiral phase on d48b ~null); now w2-jcma. swarm-d finishing.
- TODO: claim bb15 once conv46 in.

## 2026-10-14 00:29 — wakeup 19: cma2 gen5 → 5.64
- bb15 ladder done: conv46 5.969, STRONG R_min 5.345.
- **6bcd (20261014T000540.460Z_swarm-c_req_6bcd)** [α .603,.087,−.617,.023; β7 .533, β13 −.24]: s21 5.643 r46 6.010 r56 5.964 (conv46 pending); Σ|β| 1.893 (box 2.0), Σ|α| 2.30, M2k ratio 1.114.
- Gen6 submitted (mean [.646,.12,−.588,.005,.515,−.188] σ .089). cma2 used 70.
- swarm-d DONE (w2 best R_min 1.346 bef5). Remaining active: b (w2 phase CMA), e (w2 jcma).
- TODO next: claim 6bcd (+bb15) when conv46 in.

## 2026-10-14 00:52 — wakeup 20: cma2 gen6 → 4e65 6.03
- 6bcd STRONG R_min 5.643 (conv46 5.961) → claim posted (with bb15).
- gen6 best **4e65** [α .617,.041,−.674,−.11; β7 .547, β13 −.04] s21 6.029 (r46 pending?). dcce 5.70.
- Gen7 submitted (mean [.618,.061,−.658,−.053,.522,−.067] σ .096). cma2 used 80/100.
- swarm-b closed w2 phase (dd54 R_min 1.487); doing k-reassign on bb15.

## 2026-10-14 01:14 — wakeup 21: cma2 gen7
- 4e65 ladder: s21 6.029 r46 6.438 r56 6.600 conv46 6.696 STRONG (conv46−r46 +4%: qmax drift growing; quote r46).
- gen7 best **97ac** [α .618,.044,−.693,−.077; β7 .538, β13 −.077] s21 6.316 (ladder pending). 9943 5.99, 6f49 5.91.
- Gen8 submitted (mean [.61,.043,−.677,−.073,.525,−.063] σ .096). cma2 used 90/100.
- swarm-b: k-reassign on bb15 → 0.083 FAIL (gain destroyed incl. phase); now w3 phase-only CMA (clean beyond-M2).
- PLAN: after gen8 (last), close cma2 with coverage; claim best; consider final confirm/convergence asks; then decide whether to `swarm done` or spend remaining ~250 evals (e.g. extra phase coordinates, w2 transfer of joint form).

## 2026-10-14 01:38 — wakeup 22: cma2 gen8
- 97ac STRONG R_min 6.316 (r46 6.706 r56 6.791 conv46 6.836); 9943 strong 5.986.
- gen8 best d6f6 [α .587,−.065,−.685,−.072; β7 .545, β13 −.04] s21 6.579; 58cf 6.554 (g3 .44, β7 .64).
- Gen9 submitted; budget extended to 150 (note posted). Charged 264/500.
- swarm-b closed w3 phase-only (a05b s21 1.054 r46 1.175): phase alone is weak, synergy needs amplitude.

## 2026-10-14 02:00 — wakeup 23: cma2 gen9
- d6f6 STRONG R_min 6.579 (s21 6.681 r46 6.579 r56 7.21 conv 6.87); 58cf STRONG 6.554 (s21 6.873 r46 6.554 r56 7.387). Now r46 binds.
- gen9 best **0b81** [α .573,.01,−.725,−.031; β7 .598, β13 −.187] min 6.882; 4a94 6.646.
- Gen10 submitted (110/150). swarm-b fefc: static controls for 6bcd (ρ̄ 0.91, frozen-K/Γ 0.74–0.97) all BELOW parent → strong beyond-M2 evidence. swarm-e w2 jcma 1413 R_min 1.525.

## 2026-10-14 02:20 — wakeup 24: cma2 gen10
- 0b81: s21 7.092 r46 6.882 r56 7.341 (conv46 pending) → will be strong R_min 6.882.
- gen10 best **3231** [α .588,.041,−.73,−.053; β7 .599, β13 −.148] min 7.019; df60 6.954. Gains slowing (~2%/gen), σ .086.
- Gen11 submitted in background (submit now >120 s due to repair checks). cma2 120/150.
- PLAN: gens 11–14 finish the 150 budget; then close with coverage + final claim; total ~ 324/500. Then swarm done (or a small verification set).

## 2026-10-14 02:39 — wakeup 25: cma2 gen11 (no gain)
- gen11 best 6f3e 6.983 < 3231 7.019 → first no-gain gen. σ .072. Gen12 submitted (130/150). If gen12 no gain → close cma2, final claim + coverage, swarm done.

## 2026-10-14 03:00 — wakeup 26: cma2 converged → CLOSED
- gen12 best e688 7.060 (Σ|α| 2.495, Σ|β| 1.964 both at box), e594 7.026. 3231 STRONG R_min 7.019 (conv46 7.122).
- Posted closing result + coverage (w3-cma2, 130 evals). Charged 304/500.
- NEXT: wait for e688/e594 conv46; post final claim if strong; then final summary note + `swarm done`; stop loop. Remaining ~196 evals unspent (optimum on campaign boundary; nothing in-scope left that beats it cheaply).

## 2026-10-14 03:22 — wakeup 27: FINAL
- e688 STRONG R_min 7.060 (conv46 7.19); e594 strong 7.026. Final claim 9257 posted.
- `swarm done` with summary (304/500 charged). Loop stopped.
