# swarm-d notebook

Started 2026-10-15T04:13:03+00:00.

## 2026-10-15 ~04:40 — wakeup 1: scope = mechanism controls (family `m2-controls`)
- Board: a=w3-atlas, b=w3-joint, c=w2-atlas, e=w3-bigamp, f=fsfloor, g/h=phase/chiral, i/j/k=G⟂R matched classes.
  My first idea (w2 atlas) was taken by swarm-c a minute earlier → dropped.
- KEY board fact: S1×T1 joint class G⟂R (R_G=(n,-m) for G=(m,n)) is a big winner: b req_f06f α=0.05 robust_positive
  (min 1.088 incl conv46); j req_7d04 α=0.2 s21 1.369/r46 1.386 (M2k 4.733); j 8e11 α=0.3 1.235 (M2k 6.18).
- Tools written (work/): gen.py (inputs; atlas/randdirs), geom.py (single-particle tr g, Berry F, M2k; validated:
  static tr g = F = 1+½∇²logS to 1e-7 with + sign of real exponent), ctrl.py/mk_ctrl.py (static controls).
- Geometry facts: parents' Berry curvature already flat (std .015 w3, .038 w2). The three S1×T1 classes have identical
  M2k and near-identical defect (⟂ .019 vs .022 at α=.05) → class dependence is NOT M2k/ideality.
- w3 ρ* min = 0.005 → can't scale parent shape up. Controls = ρ*·exp(a O_S1) M2-matched (±a) + BZ-avg ρ̄; C6-closed cutoff |G|²≤49.
- Submitted 25 control evals (s21,r46,r56): bar 37b0(7d04?) … see `swarm status`; identity fb47 (s21).
  Posted hypothesis c14d, request 18ef (definition of matched control), mailed b, j, e.
- Unused: rd_w3/ (16 random α directions ±0.1 for an additivity test) — parked; atlas_w2/, atlas_w3/ descriptors in desc_atlas.txt.
- NEXT: read control results; compare R_ctrl vs R_kdep per cluster; post `result` with coverage; extend controls to w2 S1⊥ leaders.

## 2026-10-15 ~05:00 — wakeup 2
- Herding: 8 agents ran matched-density controls (a,d,l,m,n,o,p,q,r). Consensus: ρ̄ control ≈1.00–1.04, M2-matched
  statics lose (S1 exp) or reach ~1.2 (a's shape) vs 7d04 1.31–1.39 → S1⊥ gain beyond M2; uniform LL0 loses → parent interference.
- My controls (s21/r46; r56 pending): bar f06f c5e9 1.001/1.001; bar 7d04 37b0 1.017/1.017; bar 8e11 380f 1.038/1.038;
  expS1- 7d04 303b 0.947/1.031(!); expS1- f06f 76e3 0.940/1.002; expS1+ 7d04 b9f8 0.769/0.827; expS1+ 8e11 b0c6 0.640/0.689;
  expS1+ f06f f02f 0.950/0.999; identity fb47 1.0000. NOTE large s21→r46 spread (~6–8%) for static S1-modulated bands.
- Descriptor test vs swarm-a atlas (120 pts): defect corr(logR) −0.30, band distance −0.28 (and anti-ordered: S1 has
  largest distance yet least damage), M2k −0.03. Single-particle descriptors do NOT predict ED damage. (work/fit_atlas.py, dist.py)
- New family `w3-recentre` (hyp e6b3): joint classes S{1,3,4}×T{1,3,4} (achiral + mirror-tied chiral) ±0.05 on top of
  S1⊥ α=0.2 base (work/joint.py, mk_recentre.py, rc_w3/). Submitted base + 22; 12 left in work/rc_pending.txt.
- NEXT: submit rc_pending; post m2-controls result when r56 lands (short, cite duplication); analyse recentre odd parts.

## 2026-10-15 ~05:25 — wakeup 3
- Recentre (base 8254 = 7d04 exactly; status list earlier was truncated by `head` — map ids via `swarm show`).
  22 probes S1×T3/T4, S3×T1/T3/T4 classes ±0.05 at B: ALL below B (s21 1.24–1.36, r46 1.23–1.37 vs B 1.369/1.386).
  Notably S2∥ (=my S3T1_ach0) at B: 1.3318/1.3570 s21 → odd part −0.013 → S1⊥ and S2∥ do NOT add (both feed |G|²=4 image).
  b (result 81d6) did S1×T1/T2 complement at B: all below. → B is a local max over all low-shell classes.
  Submitted last 12 (S4×T classes). 
- Posted m2-controls result 0615 (closing family; r56 pending, update later).
- Board leaders: w3 p xcombo fe3d = S2∥ c=0.25 alone + chiral β S7/S13 → s21 1.69 (M2k 5.16); h 0672 suggestive 1.43;
  w2 c w2-g4perp (|G|²=4×T1 ⊥) 1.16 s21/1.21 r46; g w2-oblique STRONG 1.11.
- Static front (n): sharpened w3 reaches 1.45 at M2=8 (s21) — matched-M2 statics shape-dependent.
- NEXT: recentre result post (with coverage); consider re-centred T1-class atlas at the S2∥ leader (w3) and at the w2
  g4perp leader — check with p/r/c first to avoid overlap.

## 2026-10-15 ~05:50 — wakeup 4
- Leaders: w3 02f7 (b) S2∥ α.25 + L−R chiral β .08 on |G|²=7 resonant classes: s21 2.38 r46 2.59; j c89a s21 2.45.
  w2: c df59 strong 1.16–1.21; g 141f strong 1.11–1.15.
- Recentre stage 1 done (rc_table.txt). Posted result 19df: 30/34 lose at B; S2∥ doesn't add to S1⊥;
  |G|²=4×T1 (ach90 & chi30-tied) beat B in both signs on s21 & r46 (+0.2…1.8%) → positive even part (curvature sign flip).
- Stage 2 submitted (16): s4/L_S4T1_{ach90,chi30}_{±.05,±.10} on 02f7, s4/B_S4T1_{..}_{±.10,±.20} on 7d04.
  New helper joint.add_classes(blk, [(s,t,d,c)]) adds classes to any block.
- Critique: built exact M·T partner of 02f7 (work/mt.py) — identical entry set → 02f7 M·T-even, no artefact. Note dce0.
- NEXT: read stage 2; if L+S4T1 gains, line-search & post; consider S4T1 on other leaders (c89a, h's 4927).

## 2026-10-15 ~06:12 — wakeup 5: closing
- Stage 2: |G|²=4×T1 on B ach90 ±0.1 → s21 1.40/1.39, r46 1.396/1.397 (≤+1–4%/+0.8%); ±0.2 saturates, chi30 ±0.2 FAIL.
  On 02f7 every probe loses (s21 2.01–2.32, r46 2.15–2.56 vs 2.38/2.59). Posted result 8ac9 + abandon 92c3.
- Board: f verified all top leaders M·T-invariant; n/i/q kernel convergence of 02f7 (−0.55% at g_cutoff 10/64);
  o: no sign changes across 45 multi-cluster gains. Herding on chiral β / w2 phase families.
- Decision: swarm done (91/500 charged). Control r56 runs (8) still queued; ρ̄ r56 covered by m/l.
