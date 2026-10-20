# swarm-c notebook

Started 2026-10-15T04:12:59+00:00.

## 2026-10-15 04:22 — wakeup 1
- Read brief, progress/40, 46, ADR-0040, kdep_envelope. Known Nk=21 (progress/46): w3 α[S1,T1]=+0.05 → +1.85 %, −0.05 → −9.0 %, β +0.05 → −4.4 %; w2 α+0.05 → −5.05 %, β+0.05 → −3.0 %.
- w3 lives on |G|²∈{4,12,16} (2G sublattice); w2 on {3,9,12}.
- Board: swarm-a = w3-atlas (30 separable dirs ±α0.10 ±β0.05); swarm-b = w3-joint (orientation classes, exactly what I had prepped in work/gen.py — verified class sum == isotropic to 8e-17). So I took **w2-atlas** (hypothesis 20261015T042019.050Z_swarm-c_hypothesis_410b).
- Tools: work/gen.py (orientation-class builder), work/atlas_w2.py (separable atlas; usage: OUT S2LIST R2LIST).
  FILENAME CONVENTION: `T{|R|²}` → T1=T1, T3=campaign T2, T4=campaign T3. `S{|G|²}`.
- Submitted batch A1 (32 reqs: S{1,3,4,7,9,12}×T1 and S{1,3}×T(|R|²=3)). Pending: work/A2 (40 reqs: rest of T2/T3) once in-flight frees.
- Next: collect A1, submit A2, analyse slopes/curvatures; compare with swarm-a's w3 atlas.

## 04:35 — wakeup 2
- A1 results (s21, w2; order α+0.10 / α−0.10 / β+0.05 / β−0.05):
  S1T1 0.877/**1.026**/0.979/0.981 ; S1T(R²3) 0.937/0.959/0.964/0.964 ; S3T1 0.990/0.975/0.986/0.987 ; S3T(R²3) 0.988/0.981/0.986/0.983
  S4T1 0.9955/0.797/0.930/0.929 ; S7T1 0.984/0.859/0.941/0.939 ; S9T1 0.807/0.887/0.848/0.847 ; S12T1 0.902/0.900/0.902/0.902 (flat!)
- req_5515 (w2 S1T1 α−0.10): s21 1.026, s21c 1.026, r46 1.080, r56 1.041 → SUGGESTIVE (ladder auto). 
- Board: G⟂R joint class is the mechanism on w3 (swarm-b f06f: s21 1.105 r46 1.088 r56 1.092; swarm-j matched-⟂ S1⊥ s21 1.369). swarm-j: e^{iG·r}e^{-iσk·R_G} with R_G=ẑ×G ℓ² acts on cyclotron coord = LL mixing emulation. Matched partner of G=(m,n) is R=(n,-m).
- swarm-f: s21 is chiral, only |R|²=1 faithfully sampled on all clusters; |R|²=3 two-valued on s21; |R|²=4 aliased on r46. swarm-g/h: M·T ⇒ β even on mirror-symmetric directions.
- w2 class decomposition taken by swarm-i and swarm-k. Mailed both proposing I take w2 line search/optimization along winning class.
- Submitted 32: S1T1 α line (−0.05,−0.15,−0.20,−0.30) + 28 of A2. Remaining 12 in work/A2b (S7T4, S9T3/T4 …).

## 04:48 — wakeup 3
- S1T1 separable α line (w2, s21): −0.05 1.018 | −0.10 1.026 (r46 1.080, r56 1.041) | −0.15 1.024 (r46 1.101, r56 pending) | −0.20 1.013 | −0.30 0.967.
- A2 (s21): S1T(R²4) 0.939/0.911/0.964/0.958 (ap/am/bp/bm); S3T(R²4) ~0.97; S4T(R²3) 0.76–0.79; S4T(R²4) 0.78–0.84; S7T(R²3) ~0.82; S12T(R²3) 0.64–0.69; S12T(R²4) ~0.76. Outer momentum stars hurt a lot on w2.
- w2 class decomposition (swarm-i/k): oblique c30/c150 α−0.05 → 1.035/1.038 (r46 1.045); ⟂ loses both signs. w3 gain is ⟂. 
- Sign rule (from swarm-p's guiding-centre bookkeeping, work/gc_harm.py): term (G,R) → harmonics G±G_R, G_R=(−q,p) for R=(p,q); gain when α·w_parent(G±G_R) > 0. S1T1 ⟂→{0,4} (w3 +0.6), oblique→{1,3} (w2 −1/3).
- Posted hypothesis w2-oblique (…044738.963Z_swarm-c_hypothesis_2372). Submitted O1 (29): achiral c30+c150 α line −0.08…−0.40, c150 line, sign-rule tests (gen S3=|G|²4 ×T1, S1×T3=|R|²4), and last 12 atlas dirs (mis-tagged family w2-oblique).
- Board: 8+ agents on mechanism controls for w3 S1⊥ (herding). swarm-b claimed robust_positive f06f (w3 ⟂ α0.05: 1.105/1.088/1.092/conv 1.088). w3 S1⊥ large α ~1.37 s21, r46 1.386.

## 05:03 — wakeup 4
- O1 results (w2): achiral oblique c30=c150=c: −0.08 s21 1.107 r46 1.130 (e346); −0.12 1.108 r46 1.149 (2aa0); −0.16 1.073 r46 1.095 (0a68); −0.20 1.000; −0.25 0.857; −0.30/−0.40 FAIL (manifold). c150 alone peaks ~1.05 (−0.08/−0.12). r56 pending for all.
- Sign-rule tests: gen 'S3'(|G|²=4)×T1 ⟂ α+0.05 → **1.059 s21, 1.141 r46 (b132)** — predicted ✓; its oblique α−0.05 0.942 ✗; S1×T(|R|²4) obl α−0.05 0.912 ✗, ⟂ α+0.05 0.964 ✗. Rule is 1/4 here; swarm-m/swarm-r critique it too (5/9, 5/8). Don't rely on it.
- swarm-g also runs w2-oblique (posted 45 s before me). Mailed swarm-g: they keep S1 oblique refinement; I take |G|²=4 ⟂×T1 (family w2-g4perp). Submitted O2 (13): G4perp line −0.05…+0.30, G4obl +0.05, combos obl(−0.08..−0.12)+G4perp(+0.05..+0.15).
- Posted w2-atlas coverage result (…050331.279Z_swarm-c_result_7544).
- Board: swarm-j claim STRONG w3 S1⊥ α0.2 (7d04: 1.369/1.386/1.306/1.386). Controls (m, q, a, r, l, o): gain not density, not uniform-LL0 cyclotron; parent interference.
- TODO: when r56 lands on e346/2aa0, check claim; mechanism control for w2 (α≠0) → ask the controls agents (swarm-p/m/l/q/r/n/d) or do matched ρ̄ control myself.

## 05:18 — wakeup 5
- **w2 STRONG (broker):** 2aa0 obl −0.12: 1.108/1.149/1.135/conv 1.149; e346 obl −0.08: 1.107/1.130/1.114/conv 1.130. swarm-g's 88e5/141f (obl −0.10 ±⟂S1) also strong — swarm-g to post claim.
- O2: G4perp (gen 'S3'=|G|²4 ×T1, 90°) alone: +0.03 1.041/r46 1.081; +0.08 1.061/1.190; +0.12 1.022/1.222; +0.16 0.935; +0.20 0.809; +0.30 0.44; −0.05 0.786. G4obl +0.05 0.834.
  Combos (obl, G4perp): (−0.10,+0.05) **1.162/r46 1.208 (df59)**; (−0.10,+0.10) 1.135/1.227; (−0.08,+0.10) 1.119/1.244; (−0.12,+0.10) 1.142/1.184; (−0.10,+0.15) 1.058/1.175. r56 pending.
- Split agreed with swarm-g: me |G|²=3,4 classes on top of B (obl −0.10); swarm-g S1×T2/T3 on B + S1⟂ refinement.
- Submitted O3 (12): grid around (−0.10,+0.05) and |G|²=3×T1 ∥ / oblique(60+120) ±0.05 on B.
- Mailed swarm-q for matched ρ̄ controls of 2aa0, df59.
- Others on w2: swarm-e Sobol+GP S1 class space (6D); swarm-m outer-shell × T1 classes; swarm-i (1,3),(3,1),(1,4),(4,1),(4,4) classes at parent.

## 05:36 — wakeup 6
- **df59 (obl −0.10 + G4perp +0.05): s21 1.162 / r46 1.208 / r56 1.189 / conv46 1.208 → STRONG.** Claim posted (…053421.024Z_swarm-c_claim_0638). swarm-g claimed B=obl −0.10 strong (141f).
- O3 grid (s21/r46): ridge flat at (c,p)≈(−0.10, +0.05…0.07); all of c∈[−0.14,−0.06], p∈[.03,.10] ≥1.11/1.15. |G|²=3×T1 classes on B lower s21 (1.03–1.08) → excluded.
- Controls: built matched ρ̄ (per-k normalized, BZ avg 36², FFT on 20 shells, ε=0.0015 positivity regularizer since w2 touches zero; work/rhobar2.py). M2(ρ̄)=2.497 (df59), 2.483 (2aa0); ‖ρ̄−ρ_p‖/‖ρ_p−1‖≈1.1%. Submitted --control s21,r46,r56: req_4239 (df59), req_7403 (2aa0).
- swarm-e takes w2 multi-class CMA seeded at df59 (mailed seed data). 
- New family w2-chiphase (hyp …053533.655Z_swarm-c_hypothesis_c722): swarm-h's chiral L−R phase on |G|²=7,13 × T1 pairs on top of df59; P1 9 evals (b ±0.02, ±0.05 + gc9 ref). Builder work/chiral.py (exact lattice vectors).
- Owe a critique post (0 so far).

## 05:50 — wakeup 7
- Controls (w2): df59 ρ̄ (4239): s21 0.9986, r46 0.9991 (r56 pending); 2aa0 ρ̄ (7403): 0.9951 / 0.9953. swarm-q df59 ρ̄ (01ce) 0.9999/1.0004; R-rotated copies 0.88–0.90 → w2 leaders beyond averaged density.
- P1 chiral on df59 (ref gc9 1.1623/1.2081): S7 b−0.02 **1.190 / r46 1.228**; S7 −0.05 1.065; S7 +0.02 1.088; +0.05 FAIL; S13 −0.02 1.168/1.209; −0.05 0.949; +0.02 1.098; +0.05 FAIL. Strong curvature; S7 b<0 (same sign as swarm-h on w3).
- Submitted P2 (9): S7 b −0.01…−0.035, S13 −0.01/−0.03, combos (S7 −0.02+S13 −0.01), (−0.015,−0.015).
- Critique posted (refutation …055023.158Z_swarm-c_refutation_c545): fe3d ρ̄ control negativity = 8-shell truncation; 16 shells positive (M2 3.798) → queued control 3ecc (w3, s21/r46/r56). Also PES ent gap falls monotonically with deformation (parent ~20 → leaders 4–5).
- w3 race: swarm-p fe3d S2∥ α0.25 + chiral S7: 1.695/1.687/1.688/1.686 strong; swarm-b 02f7 s21 2.38. swarm-e running w2-stack CMA (8-D) seeded at df59.

## 06:05 — wakeup 8
- P2 chiral S7 (full orbit L−R) on df59, s21/r46: −0.01 1.188/1.224; −0.015 **1.191/1.229**; −0.02 1.190/1.228 (r56 1.208); −0.025 1.184/1.221; −0.03 1.174/1.208; −0.035 1.157/1.189. S13 −0.01 1.176/1.219; −0.03 1.130. Combos ≤1.178. → +2.9 pts s21 over df59, small.
- fe3d 16-shell ρ̄ control (3ecc): s21 1.0279, r46 1.0279 (predicted ~1.03 ✓).
- swarm-p took class-resolved chiral β on df59 (w2-chiclass). I took **w2-phasestack**: same classes phase-only at the bare parent (hyp …060514.993Z_swarm-c_hypothesis_790f). Builder work/chiclass.py (class + mirror, m↔n both bases). PS1 12 evals: rows 7r10[3,13], 7r01[4,12], 7r1m1[7,9], 13r10[7,21 ctl], 13r01[9,19], 13r1m1[12,16] at b=±0.04.
- w3 leaders now s21 2.4 / r46 2.6–2.9 (02f7, c89a; resonant 7×T1 chiral on S2∥).
- TODO: post w2-chiphase result+coverage once r56 for chi7 −0.015 lands.

## 06:25 — wakeup 9
- PS1 (phase-only chiral classes at w2 parent, b ±0.04): all lose (0.33–0.94); odd parts largest on [9,19], [7,9] rows (b<0). swarm-l's w2-phaseonly duplicates → handed over; posted abandon (…062248.665Z_swarm-c_abandon_bb52) with coverage.
- Posted w2-oblique+g4perp result with coverage (…062233.668Z_swarm-c_result_19ad): 11/11 r56-reached grid points strong.
- P1/P2 chiral on df59: chi7 −0.02 conv46 1.2278, r56 1.2078; chi7 −0.01 r56 1.2071. (chiphase coverage post pending r56 of −0.015)
- Structural insight (work/double_res.py): "double-resonant" classes (both partners G±G_R on parent shells with same-sign weights): w3 has 9 (incl. (3,1) S2∥ and (1,3) sum 1.2); w2 has ONLY (|G|²=9,|R|²=3) ∥ → [12,12], sum −1/3. Explains why w2 gains cap at ~+20% while w3 gets ~+40%/class. Testing it: DR batch 4 evals (α −0.03, −0.06, −0.10, +0.06), family w2-dres. Caveat: |R|²=3 two-valued on s21.
- swarm-p: 13[9,19] chiral on df59 → s21 1.228 / r46 1.408 (new w2 leader).

## 06:41 — wakeup 10
- DR (|G|²9×|R|²3 ∥, w2, s21): +0.06 0.832, −0.03 0.9815, −0.06 0.874, −0.10 0.609 → odd part right sign, curvature wins. Posted note (…063936.563Z_swarm-c_note_726c): w3 has 9 double-resonant classes, w2 only (9,3).
- Posted w2-chiphase result+coverage (…064005.434Z_swarm-c_result_1898): best 271c (S7 −0.015 on df59) 1.191/1.229/1.210/1.229 strong.
- swarm-l w2-phaseonly: 13@43.9 β+0.02 phase-only 1.069/r46 1.216 (clean beyond-M2 on w2!).
- New family w2-kshape (hyp …064108.987Z_swarm-c_hypothesis_d19f): 24 T2/T3 class probes on df59 + gc8 ref. Builder work/mk_ks.py (gen.py names: S2=|G|²3, S3=|G|²4, T2=|R|²3, T3=|R|²4).
- Agents finishing early: i, d, m, g. Budget charged ~186.

## 06:58 — wakeup 11
- KS (T2/T3 classes on df59, ref gc8 1.1623/1.2081): none beats ref on s21 or r46. Best s21: G4R3 ∥ +0.05 1.159/1.149; G3R3 ⟂ −0.05 1.155/1.173; G1R3 obl −0.05 1.145/1.112. G4R4 obl −0.05 r46 0.873. → null; close after r56 lands.
- w2 leaders now: swarm-e chistack a9a7 1.307/1.316 (r56 pending); swarm-p c02a 1.262/1.383/1.362/1.384 strong. w3: swarm-a 713b 3.97/4.80/4.56/4.80.
- Plan: post kshape result+coverage, then `swarm done` (all live directions owned; my marginal value low).

## 07:20 — wakeup 12 (final)
- KS null; withdrew 25 kshape requests from r56 promotion (queue backed up). Posted result …071956.013Z_swarm-c_result_abe3 with coverage.
- Ran `swarm done` with summary. 211/500 charged. Controls 4239/7403/3ecc r56 still queued (store will record).
