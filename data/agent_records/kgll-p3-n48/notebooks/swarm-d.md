# swarm-d notebook

Started 2026-10-14T10:24:00+00:00.

## 2026-10-14 11:17 — wakeup 1
- Read docs (40, 46, theory §2,§6.4, ADR-0040), brief, reference. Parent w1c Δ(s21)=2.2586e-4, Δ(r56)=2.590e-4.
- Board: swarm-a (axis-map) and swarm-b (linmap) both doing the full 60-axis ±map (α±0.05, β±0.03). Avoid.
- **Symmetry insight**: Θ = M·K maps (α,β) on cluster C to (α,−β) on −MC for full shells (T1–T3 achiral).
  Checked clusters (work/cluster_sym2.py): s21 = C6 chiral (no mirror); r46/r56 only ±1. So full-shell β linear slopes are
  cluster-chirality artifacts. Chiral half-shells (|G|²=7,13,19,21 split into C6 orbits A=orbit(3,2),(4,3),(5,3),(5,4) = CW,
  B=orbit(3,1),(4,1),(5,2),(5,1) = CCW) carry the only physical first-order phase response; (A,β)≡(B,−β) on mirrored cluster.
- Posted hypothesis 20261014T111643.026Z_swarm-d_hypothesis_e679 (chiral-phase). Mailed swarm-a, swarm-b the caveat.
- Submitted stage 1: work/batch_s1 (48 = 4 shells × T1-3 × A/B × β=±0.05). Tools: work/gen.py (make()), work/stage1.py.
- Next: analyze slopes slope_A, slope_B per (shell,T); check slope_A ≈ −slope_B; then line search along chiral-odd gradient.

## 2026-10-14 11:35 — wakeup 2
- Board exploded (36 posts). Leader: swarm-c jorb, phase-only S2-pair×T1-pair joint orbit β=0.03 (req d698): s21 1.249, r46 1.404 PASS.
  swarm-f does chiral-odd joint-orbit β (covers 12-member shells as δ-orbits) — my half-shell family is a subset of it.
  swarm-h confirmed M·T on data: mirror-partner pairs agree to 0.04–2.4% at s21.
- My stage 1 (β=±0.05 on half-shells S13/S19/S21): ALL FAIL, gap collapses to ~1e-8–1e-7 (R ~ 0–0.002). A and B ≈ same.
  High-|G| phases destroy the near-zero-mode Laughlin state. S7 results pending.
- Submitted stage 2 (work/batch_s2, 30): A-only, β=±0.01 for S7/13/19/21×T1-3, β=±0.003 S7×T1-3. Goal: find whether linear window exists.
- Plan: if still collapse/negative → post result+coverage, abandon family; switch to a useful unclaimed role.

## 2026-10-14 12:10 — wakeup 3
- S7 half-shell β=±0.05 also FAIL (T1 R 0.05–0.07, T2 ~0, T3 0.07–0.19). All 48 stage-1 FAIL.
- KEY: (A,β) ≡ (B,β) on s21 to 4e-5 rel (hashes differ: 95dc vs a3a1 etc.), β sign changes R 30%. ⇒ half-shell separable β is TL-even;
  my hypothesis claim 3 was wrong. Likely reason: chiral response ∝ sin2δ (b's sin2d rule); for half-shell×full-T, δ set = {δ0,δ0+60,δ0+120}
  so Σ sin2δ = 0 (only l=6 harmonic survives, apparently negligible).
- Posted correction note 20261014T120944.401Z_swarm-d_note_ef39.
- Board: swarm-c STRONG phase-only claim (S2×T1 +60° chiral orbit β=0.03: 1.249/1.404/1.347). Heavy herding; outer chiral sector
  owned by swarm-a (90 reqs). ⊥ α line: r46 2.63 but s21 splitting gate binds.
- Next: wait for stage-2 small-β (A only), post result+coverage+abandon; then pick a hole (p's list: inner+outer direct optimizer,
  large-amp non-⊥ α orbits) or act as critic with low spend.

## 2026-10-14 12:35 — wakeup 4
- S13A×T1 β=±0.01: R 0.9315/0.9300 PASS — even, −7%. Rest of small-β batch still queued (broker congested, 29/32 in flight).
- Board: f STRONG claim S3×T1 chiral-odd β=0.05 (1.558/1.641/1.560, conv46 1.641); h outer α contrast S4×T1 c0+ 1.572/1.720/1.614.
  Leaders are MT-invariant by construction (mirror-even α, chiral-odd β) → MT-image verification adds little.
- Decision: close chiral-phase when data land (result+coverage+abandon). Then low-spend critic; consider `swarm done` early
  rather than adding a 6th optimizer to a herded region.

## 2026-10-14 13:05 — wakeup 5
- Small-β (A only, ±0.01) landed for S13/S19/S21×T1/T2 and S13/S19×T3: all PASS, ~even in β.
  T1: 0.909–0.932 (−7..−9%); T2: 0.979–0.988; T3: 1.012–1.025 (slight positive even curvature; ±asym ~0.9% = s21 chirality).
- Board: R_gap records ~5 (h claim c662: 4.76/5.23/4.67 STRONG; t 8c01 s21 4.82/r46 5.19). j STRONG ⊥ α. Mechanism: k density controls ≈1.
- Waiting on S21×T2/T3 and S7 tail, then post result+coverage+abandon; likely swarm done afterwards (region saturated, queue congested).

## 2026-10-14 13:37 — wakeup 6
- Tail landed: S21A T2 0.977, T3 1.010/1.017; S7A T1 0.96 (0.01), 0.997 (0.003); T2 ~1.000; T3 1.025/1.003. 47c6 pending.
- Best: 68d4 (S7A×T3 +0.01) s21 1.0250; da12 (S13A×T3 −0.01) s21 1.0249, r46 1.0461 PASS.
- Posted result+coverage 20261014T133633.879Z_swarm-d_result_28e5 and abandon. Board records ~5×; region saturated.
- Decision: swarm done (78/500 spent). Rationale: no unowned direction; queue congestion.
