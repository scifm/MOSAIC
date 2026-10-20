using Test
using MomentumED

include(joinpath(@__DIR__, "..", "src", "MoireSolver.jl"))
using .MoireSolver

include("test_geometry.jl")
include("test_symmetry_reduced_ed.jl")
include("test_normalization.jl")
include("test_glued_chern.jl")
include("test_kdep_kernel.jl")
include("test_output_spectrum.jl")
include("test_c3_symmetry.jl")
include("test_formfactor_fast.jl")
include("test_ground_manifold.jl")
include("test_parallel_scatter.jl")
include("test_gpu_ed.jl")
include("test_pes_donor.jl")
include("test_pes.jl")
