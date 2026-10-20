# swarm-a notebook

Started 2026-10-02T03:51:00+00:00.

## 2026-10-02 wakeup 1 (first agent awake; board empty)
- Read docs 40, 46, ADR-0040, kdep_envelope. Key priors: doc 46 at Nk21 w3: α[S1,T1]=+0.05 → +1.85 %, −0.05 → −9.04 %,
  β[S1,T1]=+0.05 → −4.4 %, α[S3,T1]=+0.05 → −3.75 %. 024 pilot: 4×6 +0.5 % flipped to −0.9 % at 5×6 → never trust one cluster.
- Stars (solver 120° basis): S1..S8 = enumerate_shells(9)[1:] (|G|²=1,3,4,7,9,12,13,16; S4,S7 have 12 members).
  T1 (|R|²=1), T2 (3), T3 (4) defined in work/gen.py. Using n_mesh 48, g_cutoff 6.
- w3 occupies |G|² = 4 (S3), 12 (S6), 16 (S8). w2 occupies S2 (−1/3), S5 (1/3), S6 (−1/6).
- Posted hypothesis 20261002T035928.083Z_swarm-a_hypothesis_2dfa (family w3-atlas, ~260 req budget).
- Generated 96 atlas inputs in work/atlas_w3 (all pass swarm check). Split: work/b1 (amp T1/T2, 32), b2 (amp T3, 16), b3 (phase, 48).
- Submitted b1 (32). NEXT: when slots free, submit b2 then b3 (cap 32 in flight). Then fit slopes, post table.

## wakeup 2 (04:24)
- Board busy (18 agents). Symmetry consensus (d,i,k,l): β on star products is even in TD limit (MT/MK); s21 ± asymmetry = chirality artefact.
  Aliasing (o,p,r): on s21 T2≡T5≡T6, T4 = half T3; on r46 T3 self-aliased (norm² 4/3). Only T1/T2 clean everywhere.
  swarm-n: g_cutoff 6 truncates outer shells; human fixed conv46 to max(req, 10).
- Revised plan (note 20261002T042428.170Z_swarm-a_note_ef31): β only T1 (work/b3t1, 16), α all 48. Phase 2 at g_cutoff 10.
- Broker was slow; my 32 accepted at 04:19, still pending. NEXT: submit b2 (16 α T3) + b3t1 (16 β) when slots free.
- Others: c=w3 CMA wide, e/f/b=w2 atlas, g/h/k=joint orbits, d/i/l/j=chiral phase, m=K7, n=contrast pump, o=pooled surrogate,
  p=M2 breathe, q=geometry mechanism, r=w2 synth.

## wakeup 3 (04:40)
- Atlas α T1/T2 (32) done, all PASS. s21 star slopes per unit α (T1): S1 +1.15, S2 +1.04, S3 −0.05, S4 +0.50, S5 −0.17,
  S6 −0.21, S7 +0.34, S8 −0.25. Curvature (R++R−−2)/α² ≈ −25…−70 (strongly concave even at 0.02!). T2 slopes ≈ 0, concave.
  Results cache: work/results.json via work/collect.py.
- Board: k/h resolved the gradient onto ONE joint orbit: S1T1 G⟂R (+2.79/unit c) and S2T1 G∥R. h 6e88 (pure S1T1 ⟂ orbit,
  t=0.11, g10) s21 1.135, s21c 1.135, at r46. k fa1d s21 1.041 → r46 1.0345 PASS. Swarm herding on A orbits (h,k,o,c).
- Submitted b2 (α T3, 16) + b3t1 (β T1, 16).
- New family m2-control (hypothesis 20261002T044429.151Z_swarm-a_hypothesis_6427): work/control.py builds ρ_ctrl=<ρ_k>_k
  static control. h6e88: M2_k 3.7237 but k-averaged density M2 only 3.6367. Submitted control 20261002T044428.313Z_swarm-a_req_7101.
- INSIGHT: w3 is on positivity bound — scaling contrast to M2 3.72 makes |h|²<0. k-dependence evades static positivity bound.
- NEXT: post atlas result w/ coverage when T3/β land; read control result; request human r46/r56 controls if 6e88 survives r56.

## wakeup 4 (05:00)
- Atlas complete (64 PASS). Posted result 20261002T050112.146Z_swarm-a_result_ebe4 w/ coverage. β star odd ≤0.05/unit;
  only T1 has α slope; full stars strongly concave; best 1.0114.
- My avg control of h6e88 = 1.0015 (= n's 5b68). n corrected my positivity claim: ρ^p on 20 shells is positive → 1.019.
- Board leaders: o 968b (2A + 2 chiral-β C7(S4T1) + C13(S7T1)) s21 1.609 r46 1.710; c 776c (pure S2T1∥ t=0.45) s21 1.518 r46 1.409.
  α×β-chiral superadditive. LL-mixing critique (b, p, j, q): S1T1⟂ orbit is half static coherent LL mixing; S2T1∥ is clean.
- Split with n: I do avg controls, n does pow/frozen. Submitted avg controls 968b (…425b) and 776c (…a497), box 10.
- Posted request to human ceb4: controls on r46/r56.
- Budget: 64 + 3 controls = 67 charged.
- NEXT: read control results; watch r56 of leaders; critique role (finite size: β points grow on r46 — check r56).

## wakeup 5 (05:23)
- Avg controls s21: 968b 1.0096 (vs 1.609), 776c 1.0303 (vs 1.518). n: 968b M2-matched static 1.077; 776c frozen slices 0.61/0.92.
- Human added `--control --clusters r46,r56` (mail 3a38). control.py now takes --mesh s21|r46|r56|dense (cluster momentum avg).
- Leaders now LL-free S2T1∥ + chiral-β: p cc86 s21 2.399 / r46 2.470 (M2_k 6.203); o 48bf s21 2.62. r56 GPU bottleneck.
- Submitted for cc86 (p asked): avg ctrl s21 …065a, r46 …e85e, r56 …8ae5 (ctrl M2 3.912). r46 ctrls 968b …b637, 776c …63f2.
- Budget ≈ 67+3+3+2+... check `swarm digest`.
- NEXT: post a controls result table once r46/r56 land. Critique ideas: gain grows r46>s21 with β — wait r56.

## wakeup 6 (05:45)
- Controls: cc86 avg s21 1.0459 / r46 1.0467 (r56 …8ae5 pending); 968b r46 1.0097; 776c r46 1.0306. bd1a has same α as 776c
  → same avg density; submitted only r56 (…2133). Posted controls result 20261002T054614.256Z_swarm-a_result_3b06.
- n yardstick: R_static ≈ 1 + 0.193(M2−M2*) on s21 & r46; my controls agree.
- e: β-chiral alone LOSES (α=0) → gain is α×β interplay. bd1a r56 2.567 (s21 2.271, r46 2.627) → first w3 point with all 3 clusters.
- Human: new `--diagnostic`, `swarm withdraw`, priority queue. G⟂R-paired claims = provisional.
- Budget 72 + 1 = 73 charged. Role now: control provider + critique. Little need for own search.

## wakeup 7 (06:12)
- Claims: p cc86 STRONG (provisional; s21 2.399/r46 2.470/r56 2.456/conv46 2.469), o bd1a STRONG (provisional; 2.271/2.627/2.567/2.628),
  d 2400 robust_positive phase-only (1.036/1.080/1.056/1.076; q: marginal).
- New top: h fea3 (o base + S1T2∥ −0.05) s21 2.80 / r46 3.59, r56 pending. c: PES ent gap falls 21→~5 as R rises (all still PASS).
- n M2-matched mixture static: cc86 1.42/1.43 (~30% of gain is density-reachable statically).
- My r56 controls (cc86 …8ae5, bd1a …2133) still pending (GPU queue). Rule: don't read broker store files directly.
- NEXT: avg controls for new α blocks (fea3 family: S2T1∥ + S1T2∥) once they reach r56 with R≥1.05; w2 leader avg control (g 7f3e/e214).

## wakeup 9 (06:43)
- c claimed 776c STRONG (amp-only S2T1∥ t=0.45): 1.518/1.409/1.499/1.409. Mailed c my avg controls (1.030/1.031; r56 queued).
- k 435c s21 3.47 new top (confirm21). f: parents' 4x6 gap 4.1% low → r46 R inflated ~4%; r56 binding.
- My r56 controls still queued (controls = lowest GPU priority). m done (118 evals).
- Plan: idle-ish; controls for new claimed α blocks + w2 leader once at r56.

## wakeup 10 (07:14)
- New claims: h d49b STRONG (S2T1∥ t=0.11 amp-only 1.128/1.120/1.112/1.120); r e064 w2 phase-only STRONG; g w2 98ec/29a2 STRONG
  (amp-only, provisional); l w2 9fcb phase-only STRONG. c and m done.
- Human: controls with --builds-on now inherit candidate priority on r56 (my pending r56 controls should run now).
- Submitted avg controls s21/r46/r56: d49b (w3) …3189/…2340/…a3b5; 29a2 (w2) …2730/…6c80/…e771; 98ec (w2, box 14 —
  box 10 ringing made |h|²<0 at −3e-5 because w2 touches zero) …5594/…3bef/…3cbf.
- Budget ≈ 73 + 9 = 82.

## wakeup 11 (07:41)
- Controls s21/r46: d49b 1.0016/1.0016 (vs 1.128/1.120); w2 98ec 1.0011/1.0020 (vs 1.102/1.245); w2 29a2 0.9983/0.9983 (vs 1.108/1.131).
  All 5 r56 controls still pending (GPU). Human now ranks r56 queue per parent.
- o done (50 evals), claimed 84e4 phase-only strong. e: all claimed points exactly MT-invariant.
- NEXT: when r56 controls land, post a full control table (all claims, 3 clusters).

## wakeup 12 (07:59)
- 5 r56 controls still SUBMITTED (GPU saturated). New claims: d C7 phase-only strong (e25f, 3ea2); k 7966 3.727/3.832/3.785.
  e audit: top tier R>3 has split/Δ 4–9%; robust tier (split ≤1e-2) tops at cc86. Agents finishing: c, f, j, m, o.
- Plan: post final control table when r56 lands, then `swarm done`.

## wakeup 13 (08:31)
- r56 controls still queued (n's too; GPU bottleneck). Posted full control table 20261002T083152.366Z_swarm-a_result_20d3 (+fix note).
- New claims: k 7966 (3.727/3.832/3.785/3.787), p 9fc9/8bc7 (thin manifold sp/D ~0.09). i: static-free combos reach 1.40/1.51.
- Plan: one or two more wakeups for r56 controls, then a short update + swarm done.

## wakeup 14 (09:18) — DONE
- r56 controls still queued (GPU). Posted `swarm done` summary. 82/500 charged. Loop stopped.
