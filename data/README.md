# Data

The band parameters, spectra and agent records that support the paper. All files are JSON or Markdown.

## Models and campaigns

- **Model 1** is the γ=0 band `w3`, and **model 2** is the γ=0 band `w1c`. Campaign names use `w3` for
  model 1 and `p3` for model 2.
- Every campaign ran a swarm and two isolated agents with the same brief, quota (500 evaluations) and tools.
  The isolated agents (`ctrl-a`, `ctrl-b`) had no board, mail or view of other agents' requests.

| Campaign | Model | Swarm agents | Search boundary |
|---|---|---|---|
| `kgll-w3-n5` | 1 | 5 | yes |
| `kgll-w3-n18` | 1 | 18 | yes |
| `kgll-w3-n48` | 1 | 48 | yes |
| `kgll-p3-n5` | 2 | 5 | yes |
| `kgll-p3-n18` | 2 | 18 | yes |
| `kgll-p3-n48` | 2 | 48 | yes |
| `kgll-ll0-1` | 1 | 18 | no (run before the boundary was set) |
| `kgll-p3-n20` | 2 | 20 | no (run before the boundary was set) |

The campaigns' configs are in `../configs/` and their briefs in `../swarm/missions/`. The bounded campaigns use
`kgll-w3` (model 1) and `kgll-p3-boundary` (model 2). `kgll-ll0-1` uses `kgll-ll0-nk21` and `kgll-p3-n20` uses
`kgll-p3`.

## `bands/`

Complete solver inputs (`EDInput` v1) for the 27-site cluster. They can be passed to `julia/ed_solver.jl`
as they are.

| File | Band |
|---|---|
| `lll.json` | uniform lowest Landau level (reference Δ_LLL) |
| `model1_gamma0_w3.json`, `model2_gamma0_w1c.json` | the two γ=0 bands with ideal quantum geometry |
| `model1_optimized_5eda.json` | best band of model 1 (`kgll-w3-n48`, R_min = 10.76) |
| `model2_optimized_8a68.json` | best band of model 2 (`kgll-p3-n5`, R_min = 16.29) |
| `candidate_{686f,077d}.json`, `candidate_{a321,5608}.json` | other strong bands of models 1 and 2 |

The best strong band of every arm of the bounded campaigns is under `agent_records/<campaign>/bands/`.

## `spectra/`

- **`sym27/<band>/`:** input and output of the 27-site ED (N = 9 electrons, d_s = 0.1 ℓ_B) for each band above.
- **`screening_scan/`:** the screening-length scans of Fig. 3e,f.
  - Run names give the band and d_s/ℓ_B.
  - Runs with a `_q10`, `_q12` or `_q14` suffix repeat a scan point at a larger interaction cutoff q_max, as a
    convergence check.

## `source_data/`

The values plotted in each figure and table.

| File | Used in |
|---|---|
| `spectra27.json` | Fig. 1d, Fig. 3a–d (gaps and sector spectra of the 27-site runs) |
| `spectra27_ds.json` | Fig. 3e,f |
| `kgll_geometry.json` | Fig. 1d (filled-band densities, envelope moments), Fig. 2e,f, Fig. 3g,h, Supplementary Fig. S2 |
| `fig2_space.json`, `fig3_parents.json` | Fig. 1b, Fig. 2 (Fourier modes, coefficient partial sums, densities) |
| `shear_lll.json`, `shear_gap_scan.json` | Fig. 5 |
| `fig3_speedup.json` | Supplementary Fig. S1 |
| `swarm_analysis.json` | Fig. 4b, Supplementary Tables S1–S2 |
| `boundary.json` | Fig. 4, Supplementary Fig. S5d and the table on the effect of the search boundary |
| `figS3_interactions.json` | Supplementary Figs. S3 and S4 |
| `events/events_<campaign>.json` | board posts, requests and citations over time: Fig. 4a, Supplementary Figs. S3, S5, S6 |

Tables 1 and 2 of the paper (search boundary, evaluation protocol) are the `gates.boundary`, `clusters` and
`stages` blocks of the bounded campaigns' configs.

## `agent_records/<campaign>/`

**`requests.json`:** one row per request, with these fields:
- who made it: `arm`, `agent`;
- the request: `req_id`, `kind` (search or diagnostic), `family`, `parent`, `builds_on`, `note`, `terms` (the
  α_sp, β_sp of each (G, R) term);
- what came back: the stage reached, the claim, `R_min`, and per-cluster results (gap, R = Δ/Δ⁽⁰⁾, ground-state
  splitting, entanglement gap and counting).

**Board, mail and notebooks** (`{swarm,control}/board/`, `swarm/mail/`, `notebooks/`) are released verbatim as
the agents wrote them:
- every post with its YAML header (kind, references, request identifiers);
- direct messages between swarm agents;
- each agent's working notebook.

The posts cite the project notes and decision records the agents could read, which are not part of this
repository. Names of people are replaced by `[author]`, and file-system paths by `<worktrees>/`.

**`parents.json`:** the parent bands of each arm, where the campaign recorded them.

**Token usage**, counted from the agents' Claude Code transcripts:
- `tokens.json` gives per-agent totals of input, cache-creation, cache-read and output tokens;
- `kgll-w3-n48/tokens_by_message.json` is per message;
- `kgll-p3-n20/tokens_usage.json` is a per-agent summary.

The transcripts themselves are not released.
