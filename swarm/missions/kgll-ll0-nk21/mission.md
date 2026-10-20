# Mission: does momentum dependence improve the ν = 1/3 Laughlin gap of a static GLL?

*Campaign brief from [author] (three messages, 2026-10-01), adapted to the agent
swarm (ADR-0037, ADR-0040). Every agent reads this. No agent is assigned a role
or a region: the swarm decides together, on the board, who does what.
**[broker]** marks what the broker enforces or computes for you; **[you]**
marks the swarm's job.*

## The question

Take a static generalized-Landau-level band with a known Laughlin gap (the
**parent**) and let its envelope depend on momentum. Can that momentum
dependence raise the Laughlin gap above the parent's, robustly across cluster
sizes? If so, is the gain a genuinely new mechanism, or only the changed
density at work?

There are two separate claims, made in this order:

1. **Gap enhancement:** `R_gap = Δ_kdep / Δ_static(parent) > 1` while the state
   stays a Laughlin FCI. This is what you optimize.
2. **Beyond-M2 mechanism:** the enhancement cannot be explained by the changed
   diagonal density alone. This is checked after a candidate is found.
   - A winner that uses phase only (`β`, `α = 0`) leaves `|h_k|²` unchanged and
     is automatically a clean beyond-M2 result.
   - A winner with amplitude (`α ≠ 0`) needs a post-hoc matched-density static
     control before its mechanism can be called beyond M2. Ask the human for
     one with a `request` post.

If the answer is no, the deliverable is exactly how much of the space was
searched and the largest Laughlin-qualified `R_gap` found. A null in one
cutoff or parameterization is never a null for the full k-GLL space. Every
null you post states its scope (see "Coverage posts").

## Fixed setup — [broker], enforced by `swarm check`

- Pure LL0 (`a_n = (1, 0, 0)`), short-range interaction `d_s / l_B = 0.1`,
  flat bare dispersion, one interaction normalization throughout.
- Filling ν = 1/3. Screening on the symmetric `Nk = 21` cluster (N = 7).
- **Parents** (static densities on the solver's eight shells, ADR-0035; your
  requests name one):
  - **w3** = (0, 0, 3/5, 0, 0, 1/4, 0, 1/8), the primary benchmark;
  - **w2** = (0, −1/3, 0, 0, 1/3, −1/6, 0, 0), an independent secondary parent.
- The static density is pinned to the named parent; LL mixing and `d_s` are
  not search variables. **Only the momentum-dependent deformation is free.**

## What you search — [you]

`ψ_k(r) = N_k h_k(r) ψ^LL0_k(r)` with `h_k(r) = h_parent(r) exp γ(k, r)`, written
as the `form_factor.deformation` block. The solver builds the full
cross-momentum kernel `W_G(k,k') = F_G[h_k^* h_k']` from it. Never set
`W_G(k,k')` directly. Within that, everything is open:
- spatial shells and momentum harmonics;
- amplitude and phase, separately or together;
- many harmonics at once;
- joint `(G, R)` orbits;
- less symmetric choices;
- global or local methods (Sobol, CMA-ES, surrogates, refinement), as the
  swarm decides.

**Bounds.** No optimizer runs unbounded. Search inside an explicit box, stated
in your `hypothesis` post. When good candidates pile up at a boundary, widen
the box and search again. A boundary winner triggers an expanded search; it is
neither accepted nor rejected for being on the boundary.

## Admissibility — [broker] gate, [you] pre-check

There is no small-deformation bound: large deformations are allowed in
principle. Near-singular, numerically ill-conditioned envelopes do not count
as winners. An envelope is admissible when all three hold:

1. `γ(k, r)` is smooth and periodic within its harmonic representation (the
   deformation block guarantees this);
2. the norm `S(k) > 0` everywhere it is tested: the ED mesh, dense off-mesh
   samples, and the twist momenta used by the diagnostics;
3. conditioning: `min_k S(k) / max_k S(k) ≳ 1e-6` for pure LL0.

These are numerical criteria, not physical laws. Check them before
submitting (`physics.kdep_envelope`, `scripts/kgll_pilot_024_diag.jl`). The
broker refuses inadmissible requests. Promoted candidates are also re-run with
a finer real-space mesh, a larger kernel harmonic cutoff and a larger `qmax`
before they can count.

## Score and phase gates — [broker]

For every evaluation:
- `Δ` = the gap above the three-state ground manifold (`E₄ − E₃`), and the
  manifold splitting `E₃ − E₁`;
- `R_gap = Δ / Δ_static(parent)`, with the parent evaluated on the same
  cluster at the same accuracy.

Reported as diagnostics only, never as score or gate:
- `M2^(k) = ⟨⟨ρ_k²⟩_uc⟩_BZ`, `M2*` of the parent;
- `Δ_LLL` (uniform pure LL0);
- `R_beyondM2 = Δ / (M2^(k) Δ_LLL)`.

There is no M2 theorem for k-dependent envelopes.

**Laughlin phase gate**, on every cluster used. The PES is built from the
equal-weight density matrix of the three lowest states. Expected counts
follow the (1,3) admissible counting rule, momentum-resolved:

| cluster | N_φ | N_A = 2 | N_A = 3 | Chern |
|---|---|---|---|---|
| Nk = 21 (screen) | 21 | 168 | 637 (promoted candidates) | not evaluable there; not required |
| 4×6 (confirm) | 24 | 228 | 1088 (final candidate, if practical) | must equal the parent's |
| 5×6 (confirm) | 30 | 375 | 2530 (final candidate, if practical) | must equal the parent's |

The entanglement gap is measured at the expected count, and each evaluation
gets one of three verdicts:
- **PASS:** correct momentum-resolved counting and entanglement gap ≥ 0.5;
- **AMBIGUOUS:** correct counting but a smaller or poorly separated gap. Sent
  on to confirmation and human inspection, not rejected;
- **FAIL:** wrong counting, or no separation at the expected count.

The 0.5 is a confidence threshold, not a phase criterion. A clean
three-state manifold is required on every cluster. FAIL states with large gaps
are kept in a separate *other phases* table.

**Ladder [broker]:**
1. Screen on Nk = 21 (search accuracy, PES `N_A = 2`).
2. Promising PASS/AMBIGUOUS candidates are re-run on Nk = 21 at confirm
   accuracy with `N_A = 3`, then on 4×6, then on 5×6 (Chern + PES `N_A = 2`).
3. Convergence reruns (mesh, harmonic cutoff, `qmax`) for the strongest.

## What counts as an answer

| outcome | requirement |
|---|---|
| **robust positive** | Laughlin gate passed on every cluster used, `R_gap > 1` on all three clusters, and `R_gap ≥ 1.05` on both 4×6 and 5×6 |
| **strong** | the same, with `R_gap ≥ 1.10` on both 4×6 and 5×6 |
| **suggestive** | `R_gap > 1` on all three clusters but below 1.05 on a confirmation cluster (≈ +3 % is comparable to the finite-size variation already seen) |
| **not a result** | any sign change across clusters, or a gate failure |

Nk = 21 must agree in sign but does not set the threshold. w3 is the primary
benchmark. A robust w2-only enhancement counts as evidence that
momentum-dependent GLLs can beat their static parent, reported as
parent-dependent; it does not establish an improvement of w3. The 024 pilot
showed small gains reversing sign with cluster size, which is why nothing is
claimed from one cluster.

## Coverage posts — [you], required

When you finish (or abandon) a parameterization or cutoff, post a `result`
that ends with:

    coverage:
      parent: <w3 | w2>
      parameterization: <spatial × momentum harmonics, α/β, joint orbits, symmetry>
      bounds: <per parameter; widened? from what>
      method: <Sobol n=…, CMA-ES seeds …, …>
      evaluated: <requests / evaluations>
      best_R_gap: <value, request id, gate verdicts per cluster>
      pass / ambiguous / fail: <counts>

The final report states how much of the space was searched from these posts.
A null without its coverage block does not count.

## Not your job

Running ED, PES or plots yourself; changing the parents, LL mixing, `d_s` or
the interaction; editing `src/`, `julia/`, `configs/`, `docs/`. The final
report is assembled from the store, the leaderboards and your coverage posts.
