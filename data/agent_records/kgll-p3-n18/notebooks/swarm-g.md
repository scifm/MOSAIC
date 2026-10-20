# swarm-g notebook

Started 2026-10-14T05:20:06+00:00.

## Wakeup 1 — 2026-10-14 05:20–05:50 UTC

Read: brief, 40-kgll-pilot-024, 46-precision, theory §6.4/§7–8, notes §5.4–5.8.
Board at start: a=linmap (single product terms, small), b=jorbit, c=jointorb (joint orbits, small),
then e=sharpen, f=bigamp, h=bigstep (all three: large-amplitude single terms -> HERDING on big-α).

Tools I wrote (work/):
- geom.py: single-particle geometry of pure-LL0 k-dep band from the G=0 form factor
  (port of raw_formfactor_mn, m=n=0, with W_g(k,k')). Berry curvature from small plaquettes
  (N×N), tr g from short links (h=1e-3), T_viol=<tr g-|Ω|>. Tests: LLL C=1 (sign conv. gives -1;
  use |.|), Ω flat, tr g=1; static w1c ideal (T≈1e-5) as expected for k-indep h.
- stars.py, mk.py (input builder; swarm check passes), scan1.py, flatten.py, board_geom.py.

Findings (free, local):
- parent w1c: Ω very peaked: rel.std 2.07, Ω∈[0.10,14.8], hot spot at Γ (S00 min at Γ, S ratio 0.149).
- phase-only β: Ω almost unchanged (max|dΩ| 0.14 at β=0.3), only adds trace violation T≈18β² (S1,S3×T1,T3).
- amplitude α<0 on S×T1 flattens Ω (S1×T1 α=-0.3: rel.std 1.39, Ωmax 5.2, T 0.13); α>0 sharpens it.
- board s21 (58 reqs): R_gap 0.40–1.20 at |α|≤0.1 with near-identical BZ geometry -> s21 response
  is mesh-sampling dominated; big-α outer shells FAIL PES (R 1.4–1.9, "other phases").
Next: finish flatten designs; post hypothesis `geoflat`; submit rays.

### 06:00 UTC
- Board moved fast: joint-orbit winners survive r46 (comove P1 9de1: s21 1.88 / r46 2.65; chiphase 2678 phase-only r46 2.22;
  c5b8 suggestive through r56 1.19). 18 agents; many on joint orbits; surrogates (p, r); M2 controls (a, l, q).
- My geometry on board (work/board_geom.json, corr.py): comove P1 line gain is monotone in Ω flattening
  (relstd 2.07→1.17); Spearman(R_r46, relstd) = -0.50 (n=24), -0.68 on Ω-moving subset. T doesn't hurt.
  Phase-only winners leave Ω unchanged -> separate mechanism.
- Posted hypothesis geoflat (20261014T060012.843Z_swarm-g_hypothesis_bfc4): designed flatteners off P1,
  matched in Ω relstd to comove points, + sign-flipped controls + an Ω-neutral control. Budget ≤ 60.
  Small error in post: 9de1 entries are -0.5 (not "-0.35?"); d770 (-0.35) FAILs PES at s21 (relstd 1.31).
- Mailed swarm-i.
- Running work/flatjo.py (L-BFGS-B over 27 joint-orbit amplitude classes S1-S3×T1-T3) three variants
  (lam,L1cap) = (0,2.5),(0.5,2.5),(0.5,1.5) -> work/flatjo_*.json.

## Wakeup 2 — ~07:00 UTC
- Board: R up to ~11 (b55a strong claim through conv46; ac14 strong 4.4-4.9; swarm-b phase-only strong 1.15).
  swarm-a's qgeom duplicated my geometry (agrees): flattening explains the P1 family only, not ac14.
- flatjo L-BFGS too slow on the loaded node -> killed. (Lesson: `pkill -f <pattern>` matches my own shell; use ps|grep [p]ython.)
- graddesign.py: dσ_Ω/dc at the parent for 27 classes: P/A/B in a block ~equal (S1T1 2.36/2.37/2.37), all positive
  -> negative c flattens; flattening can't distinguish P1 from M1=A+B. Board counterexample: swarm-c d80f (M, σ 1.77) s21 0.776.
- Submitted 3 controls (s21,r46,r56): 7fee M1 c=-0.09 (σ 1.62 ≈ 2462), 6cc8 M1 c=-0.281 (σ 1.17 ≈ 9de1),
  e73f product S1T1 c=-0.0603 (σ 1.62). Note posted 20261014T070022.508Z_swarm-g_note_7ecd.
Next: read results; post geoflat result + coverage. Then pick next role (likely verification/critique of leaders).

## Wakeup 3 — ~07:20 UTC
- Controls (r46): 7fee M1 c=-0.09 -> 0.514 PASS (P1 partner 2462: 1.633); 6cc8 M1 c=-0.281 -> 0 FAIL, gap closed
  (9de1: 2.65); e73f product -> 0.909. s21 alike (0.596 / 0 / 0.910). => curvature flattening NOT causal; P1 orbit-specific.
- swarm-a found pair-channel mechanism: e2 (2nd two-body eigenvalue, 4x6) predicts R (R² 0.97 r46). Mailed swarm-a
  my 3 controls as out-of-sample test of e2.
- Waiting r56, then post geoflat result + coverage, close family.
- Next-role candidates: e2-guided search in an uncovered subspace (would need own implementation of pair proxy;
  independence forbids reading swarm-a's worktree) or direct ED on T2/T3 x inner-shell combos at incumbent.

## Wakeup 4 — ~08:00 UTC
- Posted geoflat result (…swarm-g_result_a948) + abandon (…abandon_a998). r56 legs of controls still pending.
- New role: independent reproduction of swarm-a's e2 pair-channel mechanism (verification; no budget).
  work/pair2.py = port of MoireSolver.TrialBandH2 (V = W0 tanh(0.1q)/q, V(0)=W0*D_l, qmax 8, Umklapp via Gdif,
  antisymmetrised pair matrix per sector on 4x6). Validated: LLL degenerate doublet e1=e2=0.0106, e3~1e-6;
  parent e1 0.290 / e2 0.0066 -> matches swarm-a ×W0 (2.69).
- Running work/board_pair.py over all r46-reaching requests -> work/board_pair.json. Then fit log R vs log e2.

## Wakeup 5 — ~08:00 UTC
- pair2 over 440 bands (work/board_pair.json, pairfit.py): log R vs log e2r: r46 R2 0.943 (n=435), 0.967 search-only (n=380),
  r56 0.960, conv46 0.971; slope 0.71-0.75. Harmonic mean H=1/(1/e1+1/e2) also fits substrate controls (0.960 all).
  Posted …swarm-g_result_7d1d (pairchk) + mailed swarm-a.
- eplus.py: chiral l=2 E+ builder (θ=∠R−∠G, α=2λcos2θ, β=λsin2θ; reproduces 3bd0 exactly).
  eplus_grad: proxy efficiency per Σ|α|: T1 2.5-3× T2/T3; outer shells ~10-12 vs S1 2.4. Posted note …note_7dc7.
- Budget: 9 charged. Not opening a search family (frontier owned by r, k, n, h). Role now: proxy service + critique.
- Open: r56 legs of 7fee/6cc8/e73f still pending -> append to geoflat result if they differ.

## Wakeup 6 — 08:28 UTC
- Board converging: many final summaries (c, e, f, i, j, m). Leader 2fb9 (n): strong, min R 14.27. k: all strong claims are
  one chiral E+ field. swarm-a: e3 (V3-like channel) separates PASS/FAIL (AUC 0.965); e2guide maximisation exits phase.
- My r56 control legs still pending (5x6 queue). Plan: wait one cycle, append r56 to geoflat, then swarm done.

## Wakeup 8 — ~09:00 UTC — DONE
- r56 legs of controls still queued after ~2 h; conclusion unaffected. Posted swarm done (summary work/done.md).
