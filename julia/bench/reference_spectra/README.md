# ContinuumED ED Benchmark

This folder is a portable benchmark specification for exact-diagonalization
(ED) spectra in the `w_G` generalized Landau-level model. It is intended to be
copyable into another project: an agent should be able to read this file,
rebuild equivalent benchmark code, and compare spectra/gaps against the data in
`data/`.

## Folder Contract

- `benchmark_ed.jl`: Julia runner that generates all reference spectra, summary
  CSV files, serialized result dictionaries, and spectrum figures.
- `data/`: benchmark outputs. The important plain-text files are
  `benchmark_summary.csv` and one `<case>_spectrum.csv` per case.
- `figures/`: ED spectrum plots, one `<case>_spectrum.png` and PDF per case.

Run from the repository root:

```bash
julia --project=julia --threads auto benchmark/benchmark_ed.jl --overwrite true
```

Run one case:

```bash
julia --project=julia benchmark/benchmark_ed.jl --case rect12_N4_ds1_uniform --overwrite true
```

List cases:

```bash
julia --project=julia benchmark/benchmark_ed.jl --list-cases true
```

## Physics Model

The benchmark uses a triangular reciprocal lattice with magnetic length
`ell = 1` unless a case says otherwise:

```text
Gfactor = 2 * sqrt(pi) / 3^(1/4) / ell
b1 = (0, Gfactor)
b2 = (-sqrt(3)/2 * Gfactor, -1/2 * Gfactor)
Auc = 2*pi*ell^2
lB = ell
```

Single-particle orbitals live on either a rectangular `N1 x N2` momentum grid
(`symcluster = 0`) or a built-in tilted cluster (`symcluster = 1`). The default
example requested for this benchmark is:

```text
Nk = Ns = 12
N = 4
symcluster = 0
N1 = 3
N2 = 4
```

The projected band is specified by Fourier coefficients of the density
modulation,

```text
|h(r)|^2 = sum_G w_G exp(i G.r), with w_0 = 1 and w_-G = conj(w_G).
```

The default cases use the uniform LLL band, i.e. all nonzero radial-shell inputs
are zero. Modulated cases list radial-shell values `Bvalues`; these are expanded
with the same hexagonal shell ordering as `ContinuumED.GenerateBlist`.

The default form factor is `formfactor_mode = :legacy`. One reference case uses
`formfactor_mode = :ll_mixed` with

```text
ll_mix = [(0.96, 0), (0.04, 2)]
```

## Interaction

The two-body interaction benchmark is the screened Coulomb kernel

```text
V(q) = V0_code * tanh(|q| * ds) / |q|
V(0) = V0_code * ds
```

with the finite-size matrix-element prefactor and density-density convention
used by this project:

```text
matrix element prefactor = (1 / Ns) * 1/2
```

The user-facing benchmark convention is

```text
V0 = 1.0
Vq = V0 * Gfactor * tanh(|q| * ds) / |q|
ds / ell = 1.0 by default
```

Therefore the runner sets `V0_code = V0 * Gfactor` by default. If another ED
code already absorbs this `Gfactor` into its definition of `q` or its interaction
normalization, compare after documenting the energy-scale conversion.

## Solver And Gap Rule

For every case, solve all momentum sectors `K = 0:(Nk - 1)`.

Default solver settings:

```text
method = :csc
selecteg = 8
ed_tol = 1e-14
```

The benchmark gap uses the Laughlin-style fixed degeneracy rule:

```text
expected ground-state degeneracy = 3
gap = first excitation outside the three-state ground manifold
      minus the average ground-manifold energy
```

For cross-code comparisons, compare both absolute spectra and shifted spectra
`E - E0`. Shifted spectra are often the cleanest first check because different
normal-ordering conventions can add constants.

## Reference Cases

| Case | Purpose | Cluster | Interaction | Band |
| --- | --- | --- | --- | --- |
| `rect12_N4_ds1_uniform` | Default requested benchmark | `Nk=12,N=4,N1=3,N2=4,symcluster=0` | `ds/ell=1,V0=1` | uniform legacy LLL |
| `rect9_N3_ds1_uniform` | Small smoke-test cluster | `Nk=9,N=3,N1=3,N2=3,symcluster=0` | `ds/ell=1,V0=1` | uniform legacy LLL |
| `rect12_N4_ds0p5_Bshell` | Modulated density and shorter screening | `Nk=12,N=4,N1=3,N2=4,symcluster=0` | `ds/ell=0.5,V0=1` | weak radial `w_G` shells |
| `tilted12_N4_ds1_uniform` | Built-in tilted cluster comparison | `Nk=12,N=4,symcluster=1` | `ds/ell=1,V0=1` | uniform legacy LLL |
| `rect12_N4_llmix02` | LL-mixed form-factor check | `Nk=12,N=4,N1=3,N2=4,symcluster=0` | `ds/ell=1,V0=1` | `0.96 LL0 + 0.04 LL2` |

## Output Schema

`data/benchmark_summary.csv` has one row per case:

```text
case,Nk,N,N1,N2,symcluster,formfactor_mode,ds_over_ell,V0_user,V0_code,
Gfactor,qmax,qmax2,selecteg,gap,ground_energy,first_excitation,
materialize_time_sec,solve_time_sec,max_sector_dim,ground_multiplet,
spectrum_csv,figure_png
```

Each `data/<case>_spectrum.csv` stores:

```text
case,sector,level,energy,energy_shifted
```

Each `data/<case>_result.jls` stores the full Julia dictionary with spectra,
shifted spectra, sector dimensions, timings, and gap metadata.

## Porting Checklist For Another Project

1. Build the same momentum cluster and use the same sector labels.
2. Use the triangular reciprocal vectors and `Auc` above.
3. Build the same `w_G` list from the radial shell values.
4. Use the same form-factor convention, especially the code convention
   `q_lambda = k' - k - G`.
5. Use the screened two-body kernel and the same `Gfactor` energy prefactor.
6. Include the `1/Ns` and `1/2` density-density factors in the same place.
7. Diagonalize every many-body momentum sector and sort low-energy levels.
8. Write `sector, level, energy, energy_shifted` and compare to `data/`.

Suggested numerical tolerances:

```text
absolute shifted-spectrum tolerance: 1e-9 for sparse exact diagonalization
gap tolerance: 1e-9 when conventions match exactly
```

Loosen the tolerance only after identifying a known convention difference, such
as a missing constant energy shift or a different global interaction scale.
