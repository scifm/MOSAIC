# MomentumED.jl patch

`MomentumED-40400d4.patch` applies to [MomentumED.jl](https://github.com/Zou-Bo/MomentumED.jl) at commit
`40400d4` (MIT, Zou Bo). `scripts/setup_solver.sh` applies it. The patched tree is the one the paper's
campaigns ran with.

1. **Julia 1.10.** The `public` declarations (Julia ≥ 1.11 syntax) are commented out, and the packages' `julia`
   compat is lowered to 1.10.
2. **GPU memory after a Lanczos restart.** The CUDA extension frees device memory after every restart with a
   full GC. Two flags (`CUDA_KRYLOV_SHRINK_RELEASE`, `CUDA_KRYLOV_SHRINK_MINOR_GC`) let a caller replace that
   with a minor GC, or skip it.
   - A full GC stops every task, which serializes concurrent sector solves.
   - Without any GC, dead Krylov vectors fill device memory.
   - `julia/src/gpu_ed.jl` uses the minor GC for its concurrent multi-GPU solves.
