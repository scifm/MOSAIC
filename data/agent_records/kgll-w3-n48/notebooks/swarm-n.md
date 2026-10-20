# swarm-n notebook

Started 2026-10-08T04:35:20+00:00.

## 2026-10-08 05:13 — wakeup 1: orientation, scope, w2-opt phase 1
- Read brief, docs 40/46, theory §6.4, notes §5.7/§12. Tools: work/harvest.py (all visible requests ->
  label + R per cluster, cache in work/cache), work/evenodd.py (even/odd parts of atlas axis pairs),
  work/gen.py (template + deformation block; stars S1..S4, T1..T3), work/cluster_sym.py.
- Labels in harvest: G<|G|²>/<n> x R<|R|²>/<n>: G1=S1, G3=S2, G4=S3; R1=T1, R3=T2, R4=T3.
- Findings: β response ~even (M·T rule; swarm-j posted it). No ED cluster is mirror-closed (s21 C6 chiral,
  r46/r56 only C2). w3 even part along S1/S2 α is LINEAR in |x| (cone/kink: degenerate excitation split by
  half-translation breaking, cf swarm-h); S3 β quadratic. Posted critique to swarm-d (note 599d + mail).
- w3 board is crowded (~12 agents). Took **w2-opt** (hypothesis 4821): 6-D α (S1-S3 x T1-T2),
  24 Sobol dirs (seed 21) x ±0.06 = 48 evals submitted (meta: work/inputs/w2p1_meta.json).
- Next: when phase 1 lands, fit grad + Hessian (+ swarm-a axis ±0.1 points); check smoothness (even part vs r);
  line search along ascent/Newton direction; CMA-ES later. Budget plan ≤130.

## 2026-10-08 06:18 — wakeup 2: w2-opt closed; M.T audit
- Board exploded: joint (G,R) orbits (S1T1⟂, S2T1∥) + chiral-β dressing give w3 R up to ~2.5 (s21/r46);
  w2 leaders ~1.16 (m orbit) to 1.30 (b chidress). r56 has produced NO results yet (stalled; c asked human).
- w2-opt phase 1 fit (60 pts incl. swarm-a): smooth, no cone; grad −α[S1T1] + α[S3T1]; dominated by m's orbits.
  Closed with coverage (result a308). Best 8f0f s21 1.027 / r46 1.080.
- harvest.py: fixed import side-effect (main() at import). Full-board harvest is slow (~1000 reqs, ~1 s/show);
  filter by section/agent.
- New tool work/mtpartner.py: M.T partner (mirror G=(m,n)->(m-n,-n), R->(R1,-R1-R2), beta->-beta), classifier.
  Top-30 of both parents are M.T-even except 4 of swarm-t's (tiny chiral α). Submitted their partners
  (family mt-partner: f8c4, 655a, a4af, 02a2). Note 2d08 + mail to t.
- Budget: 52/500 used. Role now: verifier. Next: (1) partner results vs originals; (2) when r56 lands,
  cross-cluster consistency analysis of leaders (what predicts s21/r46/r56 drift); look for an unexplored direction.

## 2026-10-08 06:45 — wakeup 3: partner test closed; reserve
- Partners vs originals (s21/r46): a4af 2.4785/2.4902 vs 0e99 2.4781/2.4915; f8c4 vs f7a7, 02a2 vs 847e, 655a vs 23af
  all ≤0.05 %. Posted result fe74 (coverage). r56 still stalled board-wide.
- w3 s21 frontier now 3.5 (swarm-t GP); w2 1.30 (b chidress). Many agents in reserve. Phase-only TL-linear
  sector saturates at s21 1.053 (swarm-w). I switched to reserve/verifier (note posted).
- Next: when r56 lands, check partner pairs on r56; look for real gaps; don't burn budget on crowded targets.

## 2026-10-08 07:25 — wakeup 4: quiet hold
- r56 still stalled. Many agents posting 'done'. Frontier w3 min(s21,r46) 3.52/3.92 (t 4020); w2 s21 1.32 (ai step).
- Nothing new for me to run; staying reserve until r56 lands (partner-pair check on r56).

## 2026-10-08 08:30 — wakeup 5: done
- r56 still stalled; most agents done. Withdrew 3 redundant partner promotions (f8c4, 655a, 02a2) to free r56
  capacity; kept a4af (partner of t 0e99). Posted `swarm done` summary (work/done.md). Loop stopped.
