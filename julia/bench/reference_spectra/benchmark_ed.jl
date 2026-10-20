#!/usr/bin/env julia
#
# Reproducible ED benchmark runner for this repository's Julia solver.
#
# Run from the repository root:
#   julia --project=julia --threads auto benchmark/benchmark_ed.jl --overwrite true
#   julia --project=julia benchmark/benchmark_ed.jl --case rect12_N4_ds1_uniform --overwrite true
#
# Outputs:
#   benchmark/data/benchmark_summary.csv
#   benchmark/data/<case>_spectrum.csv
#   benchmark/data/<case>_metadata.md
#   benchmark/data/<case>_result.jls
#   benchmark/figures/<case>_spectrum.png
#   benchmark/figures/<case>_spectrum.pdf
#   benchmark/figures/<case>_spectrum.svg

using LinearAlgebra
using Printf
using Serialization

const REPO_ROOT = normpath(joinpath(@__DIR__, ".."))
const JULIA_DIR = joinpath(REPO_ROOT, "julia")

include(joinpath(JULIA_DIR, "src", "MoireSolver.jl"))
using .MoireSolver
using MomentumED

const TRI12_KLIST = Int64[
    0 3 2 5 1 4 0 3 2 5 1 4;
    0 0 1 1 2 2 3 3 4 4 5 5
]
const TRI12_GK = (6, 6)

Base.@kwdef struct BenchmarkCase
    name::String
    description::String
    Nk::Int
    N::Int
    N1::Int
    N2::Int
    symcluster::Int = 0
    k_list::Union{Nothing,Matrix{Int64}} = nothing
    Gk::Union{Nothing,NTuple{2,Int64}} = nothing
    qmax::Int = 6
    selecteg::Int = 8
    gsdeg_expect::Int = 3
    ell::Float64 = 1.0
    ds_over_ell::Float64 = 1.0
    V0::Float64 = 1.0
    include_gfactor_prefactor::Bool = true
    n_shells::Int = 0
    shell_values::Vector{Float64} = Float64[]
    formfactor_mode::Symbol = :orth_ll
    level_mix::Vector{Tuple{Float64,Int64}} = Tuple{Float64,Int64}[(1.0, 0)]
    ll_reg::Float64 = 0.0
end

parse_bool(opts, key, default=false) =
    lowercase(get(opts, key, string(default))) in ("1", "true", "yes", "y")

function parse_kv_args(argv)
    opts = Dict{String,String}()
    i = 1
    while i <= length(argv)
        arg = argv[i]
        if startswith(arg, "--")
            key = arg[3:end]
            if i == length(argv) || startswith(argv[i + 1], "--")
                opts[key] = "true"
                i += 1
            else
                opts[key] = argv[i + 1]
                i += 2
            end
        else
            i += 1
        end
    end
    return opts
end

portable_path(path::AbstractString) =
    replace(relpath(normpath(path), @__DIR__), '\\' => '/')

gfactor_for_ell(ell::Real) = 2 * sqrt(pi) / 3^(1 / 4) / Float64(ell)
auc_for_ell(ell::Real) = 2 * pi * Float64(ell)^2

function benchmark_cases()
    BenchmarkCase[
        BenchmarkCase(
            name = "rect12_N4_ds1_uniform",
            description = "Default rectangular 3x4 cluster: Nk=12, N=4, ds/ell=1, uniform LLL band.",
            Nk = 12,
            N = 4,
            N1 = 3,
            N2 = 4,
            symcluster = 0,
            qmax = 6,
            selecteg = 8,
        ),
        BenchmarkCase(
            name = "rect9_N3_ds1_uniform",
            description = "Small rectangular 3x3 cluster for quick cross-code smoke checks.",
            Nk = 9,
            N = 3,
            N1 = 3,
            N2 = 3,
            symcluster = 0,
            qmax = 5,
            selecteg = 8,
        ),
        BenchmarkCase(
            name = "rect12_N4_ds0p5_Bshell",
            description = "Same 3x4 cluster with shorter screening length and weak real shell modulation.",
            Nk = 12,
            N = 4,
            N1 = 3,
            N2 = 4,
            symcluster = 0,
            qmax = 5,
            selecteg = 8,
            ds_over_ell = 0.5,
            n_shells = 3,
            shell_values = [0.08, -0.025, 0.015],
        ),
        BenchmarkCase(
            name = "tilted12_N4_ds1_uniform",
            description = "Tilted 12-orbital cluster with uniform LLL and ds/ell=1.",
            Nk = 12,
            N = 4,
            N1 = 6,
            N2 = 6,
            symcluster = 1,
            k_list = TRI12_KLIST,
            Gk = TRI12_GK,
            qmax = 6,
            selecteg = 8,
        ),
        BenchmarkCase(
            name = "rect12_N4_llmix02",
            description = "Rectangular 3x4 cluster with 0.96 LL0 + 0.04 LL2 trial-band weight.",
            Nk = 12,
            N = 4,
            N1 = 3,
            N2 = 4,
            symcluster = 0,
            qmax = 5,
            selecteg = 8,
            formfactor_mode = :ll_mixed,
            level_mix = [(0.96, 0), (0.04, 2)],
        ),
    ]
end

hex_q(m::Int, n::Int) = m * m + m * n + n * n

function enumerate_hex_shells(n_shells::Int)
    n_shells < 0 && throw(ArgumentError("n_shells must be >= 0"))
    qmax = max(1, 4 * n_shells)
    groups = Dict{Int,Vector{Tuple{Int,Int}}}()
    while true
        empty!(groups)
        for m in -qmax:qmax, n in -qmax:qmax
            q = hex_q(m, n)
            q <= qmax * qmax || continue
            push!(get!(groups, q, Tuple{Int,Int}[]), (m, n))
        end
        nonzero_qs = sort([q for q in keys(groups) if q > 0])
        length(nonzero_qs) >= n_shells && break
        qmax *= 2
    end

    shells = Vector{Vector{Tuple{Int,Int}}}()
    push!(shells, sort(groups[0]))
    for q in sort([q for q in keys(groups) if q > 0])[1:n_shells]
        push!(shells, sort(groups[q]))
    end
    return shells
end

function shell_values(case::BenchmarkCase)
    values = copy(case.shell_values)
    if length(values) < case.n_shells
        append!(values, zeros(case.n_shells - length(values)))
    elseif length(values) > case.n_shells
        values = values[1:case.n_shells]
    end
    return values
end

function build_wg(case::BenchmarkCase)
    shells = enumerate_hex_shells(case.n_shells)
    values = shell_values(case)
    glist = Tuple{Int,Int}[]
    w = ComplexF64[]
    for (ishell, shell) in enumerate(shells)
        coef = ishell == 1 ? 1.0 : values[ishell - 1]
        for g in shell
            push!(glist, g)
            push!(w, ComplexF64(coef, 0.0))
        end
    end
    return glist, w, shells
end

function build_cluster(case::BenchmarkCase)
    if case.k_list !== nothing
        case.Gk === nothing && error("case $(case.name) has k_list but no Gk")
        size(case.k_list, 2) == case.Nk ||
            error("case $(case.name) has Nk=$(case.Nk) but k_list has $(size(case.k_list, 2)) columns")
        return copy(case.k_list), case.Gk
    end

    case.N1 * case.N2 == case.Nk ||
        error("rectangular case $(case.name) needs N1*N2 == Nk")
    k_list, Gk = MoireSolver.build_kmesh(
        Dict{String,Any}("nk1" => case.N1, "nk2" => case.N2),
        case.Nk,
    )
    return k_list, Gk
end

function case_to_dict(case::BenchmarkCase)
    Dict{String,Any}(
        "name" => case.name,
        "description" => case.description,
        "Nk" => case.Nk,
        "Ns" => case.Nk,
        "N" => case.N,
        "N1" => case.N1,
        "N2" => case.N2,
        "symcluster" => case.symcluster,
        "qmax" => case.qmax,
        "selecteg" => case.selecteg,
        "gsdeg_expect" => case.gsdeg_expect,
        "ell" => case.ell,
        "ds_over_ell" => case.ds_over_ell,
        "V0" => case.V0,
        "include_gfactor_prefactor" => case.include_gfactor_prefactor,
        "n_shells" => case.n_shells,
        "shell_values" => shell_values(case),
        "formfactor_mode" => String(case.formfactor_mode),
        "level_mix" => case.level_mix,
        "ll_reg" => case.ll_reg,
    )
end

function materialize_case(case::BenchmarkCase)
    if case.ell != 1.0
        error("MoireSolver currently fixes magnetic length lB=1; benchmark cases must use ell=1")
    end

    k_list, Gk = build_cluster(case)
    glist, w, shells = build_wg(case)
    lattice = MoireSolver.triangular_lattice()
    tff = MoireSolver.TrialFormFactor(
        glist,
        w,
        lattice,
        case.level_mix;
        reg = case.ll_reg,
    )

    ds = case.ds_over_ell * case.ell
    v0_code = case.include_gfactor_prefactor ? case.V0 * gfactor_for_ell(case.ell) : case.V0
    qlist = MoireSolver.build_qgrid(case.qmax)
    h2 = MoireSolver.TrialBandH2(tff, lattice, Gk, qlist, case.qmax, v0_code, 0.0, ds)
    para = EDPara(; k_list = k_list, Gk = Gk, H_two = h2)
    scat = ED_scatterlist_twobody(para)
    subspaces, sector_momenta = ED_momentum_subspaces(para, (case.N,))

    sector_labels = [sector_label(k, Gk) for k in sector_momenta]
    order = sortperm(sector_labels)
    return (
        para = para,
        scat = scat,
        subspaces = subspaces[order],
        sector_momenta = sector_momenta[order],
        sector_labels = sector_labels[order],
        k_list = k_list,
        Gk = Gk,
        glist = glist,
        w = w,
        shells = shells,
        ds = ds,
        V0_code = v0_code,
        Gfactor = gfactor_for_ell(case.ell),
        Auc = auc_for_ell(case.ell),
    )
end

sector_label(k::NTuple{2,Int64}, Gk::NTuple{2,Int64}) = Int(k[1] + Gk[1] * k[2])

function method_symbol(raw::AbstractString)
    s = lowercase(raw)
    s in ("csc", "sparse") && return :sparse
    s == "dense" && return :dense
    error("Unknown --method '$raw'. Use sparse, csc, or dense.")
end

function solve_sector_spectrum(subspace, scat, nlevels::Integer; method::Symbol, tol::Real)
    dim = length(subspace)
    nreq = min(Int(nlevels), dim)
    nreq == 0 && return Float64[], dim
    vals, _ = EDsolve(
        subspace,
        scat;
        N = nreq,
        showtime = false,
        ishermitian = true,
        method = method,
        method_info = false,
        tol = tol,
    )
    return sort!(Float64.(real.(vals))), dim
end

function shifted_spectra(spectra)
    finite = [e for levels in spectra for e in levels if isfinite(e)]
    isempty(finite) && error("no finite energies in spectra")
    e0 = minimum(finite)
    return [levels .- e0 for levels in spectra], e0
end

function gap_from_spectra(spectra; gsdeg_expect::Int)
    tagged = Tuple{Float64,Int,Int}[]
    for (isector, levels) in enumerate(spectra)
        for (ilevel, energy) in enumerate(levels)
            isfinite(energy) && push!(tagged, (energy, isector, ilevel))
        end
    end
    sort!(tagged, by = x -> x[1])
    length(tagged) >= gsdeg_expect + 1 ||
        error("too few eigenvalues: have $(length(tagged)), need $(gsdeg_expect + 1)")
    ground = tagged[1:gsdeg_expect]
    ground_energy = sum(row[1] for row in ground) / gsdeg_expect
    first_excitation = tagged[gsdeg_expect + 1][1]
    return (
        gap = first_excitation - ground_energy,
        ground_energy = ground_energy,
        first_excitation = first_excitation,
        ground_multiplet = ground,
    )
end

function ground_descriptor(gapinfo, sector_momenta, sector_labels)
    rows = String[]
    for (energy, sector_index, level_index) in gapinfo.ground_multiplet
        k = sector_momenta[sector_index]
        label = sector_labels[sector_index]
        push!(rows, @sprintf("K%d(%d,%d):L%d:%.16g", label, k[1], k[2], level_index, energy))
    end
    return join(rows, ";")
end

function csv_cell(x)
    s = string(x)
    if occursin(",", s) || occursin("\"", s) || occursin("\n", s) || occursin(";", s)
        return "\"" * replace(s, "\"" => "\"\"") * "\""
    end
    return s
end

function write_spectrum_csv(path, case, sector_momenta, sector_labels, spectra, shifted)
    open(path, "w") do io
        println(io, "case,sector,sector_k1,sector_k2,level,energy,energy_shifted")
        for i in eachindex(sector_labels)
            k = sector_momenta[i]
            for (level, energy) in enumerate(spectra[i])
                @printf(io, "%s,%d,%d,%d,%d,%.17g,%.17g\n",
                    csv_cell(case.name), sector_labels[i], k[1], k[2],
                    level, energy, shifted[i][level])
            end
        end
    end
    return path
end

function level_mix_string(level_mix)
    join([@sprintf("%.12g:LL%d", weight, n) for (weight, n) in level_mix], ";")
end

function write_metadata_md(path, case, model, result)
    settings = result["settings"]
    open(path, "w") do io
        println(io, "# ", case.name)
        println(io)
        println(io, case.description)
        println(io)
        println(io, "## Physics Settings")
        println(io)
        println(io, "- Nk = $(case.Nk), Ns = $(case.Nk), N = $(case.N)")
        println(io, "- Cluster = symcluster $(case.symcluster), Gk = $(model.Gk), N1 = $(case.N1), N2 = $(case.N2)")
        println(io, "- ell = $(settings["ell"]), Gfactor = $(settings["Gfactor"]), Auc = $(settings["Auc"])")
        println(io, "- qmax = $(case.qmax), n_shells = $(case.n_shells)")
        println(io, "- shell_values = $(settings["shell_values"])")
        println(io, "- formfactor_mode = $(case.formfactor_mode), level_mix = $(level_mix_string(case.level_mix))")
        println(io, "- Interaction: V(q) = V0_code * tanh(|q| * ds) / |q|, q=0 limit V0_code * ds")
        println(io, "- User V0 = $(case.V0), include_gfactor_prefactor = $(case.include_gfactor_prefactor), V0_code = $(settings["V0_code"])")
        println(io, "- ds/ell = $(case.ds_over_ell), ds = $(settings["ds"])")
        println(io, "- Solver method = $(result["method"]), selecteg = $(case.selecteg), expected GS degeneracy = $(case.gsdeg_expect)")
        println(io)
        println(io, "## Results")
        println(io)
        println(io, "- Gap = $(result["gap"])")
        println(io, "- Ground energy average = $(result["ground_energy"])")
        println(io, "- First excitation = $(result["first_excitation"])")
        println(io, "- Ground multiplet = $(result["ground_multiplet"])")
        println(io, "- Materialization time seconds = $(result["materialize_time_sec"])")
        println(io, "- ED solve time seconds = $(result["solve_time_sec"])")
    end
    return path
end

function write_summary_csv(path, results)
    open(path, "w") do io
        println(io, join([
            "case",
            "Nk",
            "N",
            "N1",
            "N2",
            "symcluster",
            "Gk",
            "sector_count",
            "formfactor_mode",
            "n_shells",
            "ds_over_ell",
            "V0_user",
            "V0_code",
            "Gfactor",
            "qmax",
            "selecteg",
            "gap",
            "ground_energy",
            "first_excitation",
            "materialize_time_sec",
            "solve_time_sec",
            "max_sector_dim",
            "ground_multiplet",
            "spectrum_csv",
            "figure_png",
            "figure_pdf",
            "figure_svg",
        ], ","))
        for result in results
            case = result["case"]
            settings = result["settings"]
            row = Any[
                case["name"],
                case["Nk"],
                case["N"],
                case["N1"],
                case["N2"],
                case["symcluster"],
                result["Gk"],
                length(result["sector_labels"]),
                case["formfactor_mode"],
                case["n_shells"],
                case["ds_over_ell"],
                case["V0"],
                settings["V0_code"],
                settings["Gfactor"],
                case["qmax"],
                case["selecteg"],
                result["gap"],
                result["ground_energy"],
                result["first_excitation"],
                result["materialize_time_sec"],
                result["solve_time_sec"],
                maximum(result["sector_dims"]),
                ground_descriptor(result["gapinfo"], result["sector_momenta"], result["sector_labels"]),
                result["spectrum_csv"],
                result["figure_png"],
                result["figure_pdf"],
                result["figure_svg"],
            ]
            println(io, join(csv_cell.(row), ","))
        end
    end
    return path
end

function xml_escape(s::AbstractString)
    s = replace(s, "&" => "&amp;")
    s = replace(s, "<" => "&lt;")
    s = replace(s, ">" => "&gt;")
    s = replace(s, "\"" => "&quot;")
    return s
end

function plot_coordinates(sector_labels, shifted)
    width = 900
    height = 560
    left = 96.0
    right = 48.0
    top = 72.0
    bottom = 122.0
    plot_w = width - left - right
    plot_h = height - top - bottom
    all_y = [e for levels in shifted for e in levels if isfinite(e)]
    ymax_data = isempty(all_y) ? 1.0 : maximum(all_y)
    ymax = max(1.08 * ymax_data, 1e-9)
    ymin = -0.03 * max(ymax_data, 1e-9)
    n = length(sector_labels)
    sx(i) = n <= 1 ? left + plot_w / 2 : left + (i - 1) * plot_w / (n - 1)
    sy(y) = top + plot_h - (y - ymin) * plot_h / (ymax - ymin)
    return (
        width = width,
        height = height,
        left = left,
        right = right,
        top = top,
        bottom = bottom,
        plot_w = plot_w,
        plot_h = plot_h,
        ymin = ymin,
        ymax = ymax,
        sx = sx,
        sy = sy,
    )
end

function tick_indices(n::Int)
    n <= 12 && return collect(1:n)
    step = ceil(Int, n / 12)
    ticks = collect(1:step:n)
    ticks[end] == n || push!(ticks, n)
    return ticks
end

function ytick_values(geom)
    [geom.ymin + t * (geom.ymax - geom.ymin) for t in (0.0, 0.25, 0.5, 0.75, 1.0)]
end

sector_k_text(k::NTuple{2,Int64}) = @sprintf("(%d,%d)", k[1], k[2])
sector_label_text(label) = "K" * string(label)

function first_excitation_shifted(gapinfo)
    e0 = minimum(row[1] for row in gapinfo.ground_multiplet)
    return gapinfo.first_excitation - e0
end

function ground_label_groups(gapinfo)
    by_sector = Dict{Int,Vector{Int}}()
    for (_, sector_index, level_index) in gapinfo.ground_multiplet
        push!(get!(by_sector, sector_index, Int[]), level_index)
    end
    return sort([(sector, levels) for (sector, levels) in by_sector], by = x -> x[1])
end

ground_group_label(levels::Vector{Int}) = length(levels) == 1 ? "GS" : "GSx$(length(levels))"

function write_spectrum_svg(path, case, sector_labels, sector_momenta, shifted, gapinfo)
    geom = plot_coordinates(sector_labels, shifted)
    open(path, "w") do io
        println(io, """<svg xmlns="http://www.w3.org/2000/svg" width="$(geom.width)" height="$(geom.height)" viewBox="0 0 $(geom.width) $(geom.height)">""")
        println(io, """<rect x="0" y="0" width="$(geom.width)" height="$(geom.height)" fill="white"/>""")
        println(io, """<text x="$(geom.width / 2)" y="26" text-anchor="middle" font-family="Arial, sans-serif" font-size="16" fill="#111">$(xml_escape(case.name))</text>""")
        println(io, @sprintf("""<text x="%.2f" y="50" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="#333">gap = %.6g,  red circles = expected %d-state ground manifold</text>""",
            geom.width / 2, gapinfo.gap, case.gsdeg_expect))

        for frac in 0.0:0.25:1.0
            y = geom.top + frac * geom.plot_h
            println(io, @sprintf("""<line x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f" stroke="#e1e5ea" stroke-width="1"/>""",
                geom.left, y, geom.left + geom.plot_w, y))
        end
        ticks = tick_indices(length(sector_labels))
        for i in ticks
            x = geom.sx(i)
            println(io, @sprintf("""<line x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f" stroke="#e1e5ea" stroke-width="1"/>""",
                x, geom.top, x, geom.top + geom.plot_h))
        end
        println(io, @sprintf("""<line x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f" stroke="#111" stroke-width="1.2"/>""",
            geom.left, geom.top + geom.plot_h, geom.left + geom.plot_w, geom.top + geom.plot_h))
        println(io, @sprintf("""<line x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f" stroke="#111" stroke-width="1.2"/>""",
            geom.left, geom.top, geom.left, geom.top + geom.plot_h))

        for i in ticks
            x = geom.sx(i)
            println(io, @sprintf("""<text x="%.2f" y="%.2f" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="#333">%d</text>""",
                x, geom.top + geom.plot_h + 18, sector_labels[i]))
            println(io, @sprintf("""<text x="%.2f" y="%.2f" text-anchor="middle" font-family="Arial, sans-serif" font-size="9" fill="#555">%s</text>""",
                x, geom.top + geom.plot_h + 34, xml_escape(sector_k_text(sector_momenta[i]))))
        end
        for yval in ytick_values(geom)
            y = geom.sy(yval)
            println(io, @sprintf("""<text x="%.2f" y="%.2f" text-anchor="end" dominant-baseline="middle" font-family="Arial, sans-serif" font-size="10" fill="#333">%.3g</text>""",
                geom.left - 8, y, yval))
        end
        println(io, @sprintf("""<text x="%.2f" y="%.2f" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" fill="#111">Momentum sector K and coordinates (k1,k2)</text>""",
            geom.left + geom.plot_w / 2, geom.height - 28))
        println(io, @sprintf("""<text x="18" y="%.2f" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" fill="#111" transform="rotate(-90 18 %.2f)">E - E0</text>""",
            geom.top + geom.plot_h / 2, geom.top + geom.plot_h / 2))

        yfirst = geom.sy(first_excitation_shifted(gapinfo))
        println(io, @sprintf("""<line x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f" stroke="#b23a48" stroke-width="1" stroke-dasharray="5 4"/>""",
            geom.left, yfirst, geom.left + geom.plot_w, yfirst))
        println(io, @sprintf("""<text x="%.2f" y="%.2f" text-anchor="end" font-family="Arial, sans-serif" font-size="10" fill="#8a2532">first excitation</text>""",
            geom.left + geom.plot_w - 4, yfirst - 5))

        for (i, levels) in enumerate(shifted)
            x = geom.sx(i)
            for yval in levels
                y = geom.sy(yval)
                println(io, @sprintf("""<line x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f" stroke="#2f5d7c" stroke-width="2" stroke-linecap="round"/>""",
                    x - 7, y, x + 7, y))
            end
        end
        for (_, sector_index, level_index) in gapinfo.ground_multiplet
            x = geom.sx(sector_index)
            y = geom.sy(shifted[sector_index][level_index])
            println(io, @sprintf("""<circle cx="%.2f" cy="%.2f" r="4.2" fill="#b23a48" stroke="#111" stroke-width="0.7"/>""", x, y))
        end
        for (sector_index, levels) in ground_label_groups(gapinfo)
            x = geom.sx(sector_index)
            y = minimum(geom.sy(shifted[sector_index][level_index]) for level_index in levels)
            println(io, @sprintf("""<text x="%.2f" y="%.2f" text-anchor="middle" font-family="Arial, sans-serif" font-size="9" fill="#8a2532">%s</text>""",
                x, y - 7, xml_escape(ground_group_label(levels))))
        end
        println(io, "</svg>")
    end
    return path
end

pdf_escape(s::AbstractString) = replace(replace(replace(s, "\\" => "\\\\"), "(" => "\\("), ")" => "\\)")

function pdf_line(x1, y1, x2, y2)
    @sprintf("%.3f %.3f m %.3f %.3f l S\n", x1, y1, x2, y2)
end

function pdf_text(x, y, text; size=10, align=:left)
    safe = pdf_escape(text)
    prefix = align == :center ? @sprintf("(%s) dup stringwidth pop 2 div neg 0 rmoveto ", safe) :
             align == :right ? @sprintf("(%s) dup stringwidth pop neg 0 rmoveto ", safe) :
             @sprintf("(%s) ", safe)
    return @sprintf("BT /F1 %d Tf %.3f %.3f Td %sTj ET\n", size, x, y, prefix)
end

function write_pdf(path, width::Int, height::Int, content::String)
    objects = String[
        "<< /Type /Catalog /Pages 2 0 R >>",
        "<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        "<< /Type /Page /Parent 2 0 R /MediaBox [0 0 $width $height] /Resources << /Font << /F1 4 0 R >> >> /Contents 5 0 R >>",
        "<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
        "<< /Length $(ncodeunits(content)) >>\nstream\n$content\nendstream",
    ]
    open(path, "w") do io
        write(io, "%PDF-1.4\n")
        offsets = Int[]
        for (i, obj) in enumerate(objects)
            push!(offsets, position(io))
            write(io, "$i 0 obj\n$obj\nendobj\n")
        end
        xref_pos = position(io)
        write(io, "xref\n0 $(length(objects) + 1)\n")
        write(io, "0000000000 65535 f \n")
        for off in offsets
            write(io, @sprintf("%010d 00000 n \n", off))
        end
        write(io, "trailer\n<< /Size $(length(objects) + 1) /Root 1 0 R >>\n")
        write(io, "startxref\n$xref_pos\n%%EOF\n")
    end
    return path
end

function write_spectrum_pdf(path, case, sector_labels, sector_momenta, shifted, gapinfo)
    geom = plot_coordinates(sector_labels, shifted)
    py(y) = geom.height - y
    content = IOBuffer()
    write(content, "1 1 1 rg 0 0 $(geom.width) $(geom.height) re f\n")
    write(content, "0.88 0.90 0.92 RG 1 w\n")
    for frac in 0.0:0.25:1.0
        y = geom.top + frac * geom.plot_h
        write(content, pdf_line(geom.left, py(y), geom.left + geom.plot_w, py(y)))
    end
    ticks = tick_indices(length(sector_labels))
    for i in ticks
        x = geom.sx(i)
        write(content, pdf_line(x, py(geom.top), x, py(geom.top + geom.plot_h)))
    end
    write(content, "0 0 0 RG 1.2 w\n")
    write(content, pdf_line(geom.left, py(geom.top + geom.plot_h), geom.left + geom.plot_w, py(geom.top + geom.plot_h)))
    write(content, pdf_line(geom.left, py(geom.top), geom.left, py(geom.top + geom.plot_h)))
    write(content, "0 0 0 rg\n")
    write(content, pdf_text(geom.width / 2, geom.height - 26, case.name; size = 16, align = :center))
    write(content, pdf_text(geom.width / 2, geom.height - 50, @sprintf("gap = %.6g, red circles = expected %d-state ground manifold", gapinfo.gap, case.gsdeg_expect); size = 10, align = :center))
    write(content, pdf_text(geom.left + geom.plot_w / 2, 28, "Momentum sector K and coordinates (k1,k2)"; size = 12, align = :center))
    write(content, pdf_text(18, geom.height / 2, "E - E0"; size = 12, align = :center))
    for i in ticks
        write(content, pdf_text(geom.sx(i), py(geom.top + geom.plot_h + 18), sector_label_text(sector_labels[i]); size = 9, align = :center))
        write(content, pdf_text(geom.sx(i), py(geom.top + geom.plot_h + 34), sector_k_text(sector_momenta[i]); size = 8, align = :center))
    end
    for yval in ytick_values(geom)
        y = geom.sy(yval)
        write(content, pdf_text(geom.left - 8, py(y) - 3, @sprintf("%.3g", yval); size = 9, align = :right))
    end
    yfirst = py(geom.sy(first_excitation_shifted(gapinfo)))
    write(content, "0.698 0.227 0.282 RG 1 w [5 4] 0 d\n")
    write(content, pdf_line(geom.left, yfirst, geom.left + geom.plot_w, yfirst))
    write(content, "[] 0 d\n")
    write(content, "0.698 0.227 0.282 rg\n")
    write(content, pdf_text(geom.left + geom.plot_w - 4, yfirst + 5, "first excitation"; size = 9, align = :right))
    write(content, "0.184 0.365 0.486 RG 2 w\n")
    for (i, levels) in enumerate(shifted)
        x = geom.sx(i)
        for yval in levels
            y = py(geom.sy(yval))
            write(content, pdf_line(x - 7, y, x + 7, y))
        end
    end
    write(content, "0.698 0.227 0.282 rg 0 0 0 RG 0.7 w\n")
    for (_, sector_index, level_index) in gapinfo.ground_multiplet
        x = geom.sx(sector_index)
        y = py(geom.sy(shifted[sector_index][level_index]))
        write(content, @sprintf("%.3f %.3f 4.2 0 360 arc B\n", x, y))
    end
    for (sector_index, levels) in ground_label_groups(gapinfo)
        x = geom.sx(sector_index)
        y = maximum(py(geom.sy(shifted[sector_index][level_index])) for level_index in levels)
        write(content, pdf_text(x, y + 8, ground_group_label(levels); size = 8, align = :center))
    end
    return write_pdf(path, geom.width, geom.height, String(take!(content)))
end

function set_pixel!(img, x::Int, y::Int, color::NTuple{3,UInt8})
    h, w, _ = size(img)
    (1 <= x <= w && 1 <= y <= h) || return nothing
    img[y, x, 1] = color[1]
    img[y, x, 2] = color[2]
    img[y, x, 3] = color[3]
    return nothing
end

function draw_line!(img, x1, y1, x2, y2, color::NTuple{3,UInt8}; thickness::Int=1)
    x1 = round(Int, x1); y1 = round(Int, y1)
    x2 = round(Int, x2); y2 = round(Int, y2)
    dx = abs(x2 - x1)
    sx = x1 < x2 ? 1 : -1
    dy = -abs(y2 - y1)
    sy = y1 < y2 ? 1 : -1
    err = dx + dy
    x = x1
    y = y1
    radius = max(0, div(thickness, 2))
    while true
        for yy in y - radius:y + radius, xx in x - radius:x + radius
            set_pixel!(img, xx, yy, color)
        end
        x == x2 && y == y2 && break
        e2 = 2 * err
        if e2 >= dy
            err += dy
            x += sx
        end
        if e2 <= dx
            err += dx
            y += sy
        end
    end
    return img
end

function draw_circle!(img, cx, cy, r, color::NTuple{3,UInt8})
    cx = round(Int, cx); cy = round(Int, cy); r = round(Int, r)
    for y in cy - r:cy + r, x in cx - r:cx + r
        (x - cx)^2 + (y - cy)^2 <= r^2 && set_pixel!(img, x, y, color)
    end
    return img
end

const FONT5X7 = Dict{Char,Vector{String}}(
    ' ' => ["00000","00000","00000","00000","00000","00000","00000"],
    '0' => ["01110","10001","10011","10101","11001","10001","01110"],
    '1' => ["00100","01100","00100","00100","00100","00100","01110"],
    '2' => ["01110","10001","00001","00010","00100","01000","11111"],
    '3' => ["11110","00001","00001","01110","00001","00001","11110"],
    '4' => ["00010","00110","01010","10010","11111","00010","00010"],
    '5' => ["11111","10000","10000","11110","00001","00001","11110"],
    '6' => ["01110","10000","10000","11110","10001","10001","01110"],
    '7' => ["11111","00001","00010","00100","01000","01000","01000"],
    '8' => ["01110","10001","10001","01110","10001","10001","01110"],
    '9' => ["01110","10001","10001","01111","00001","00001","01110"],
    'A' => ["01110","10001","10001","11111","10001","10001","10001"],
    'B' => ["11110","10001","10001","11110","10001","10001","11110"],
    'C' => ["01110","10001","10000","10000","10000","10001","01110"],
    'D' => ["11110","10001","10001","10001","10001","10001","11110"],
    'E' => ["11111","10000","10000","11110","10000","10000","11111"],
    'F' => ["11111","10000","10000","11110","10000","10000","10000"],
    'G' => ["01110","10001","10000","10111","10001","10001","01110"],
    'H' => ["10001","10001","10001","11111","10001","10001","10001"],
    'I' => ["01110","00100","00100","00100","00100","00100","01110"],
    'J' => ["00111","00010","00010","00010","00010","10010","01100"],
    'K' => ["10001","10010","10100","11000","10100","10010","10001"],
    'L' => ["10000","10000","10000","10000","10000","10000","11111"],
    'M' => ["10001","11011","10101","10101","10001","10001","10001"],
    'N' => ["10001","11001","10101","10011","10001","10001","10001"],
    'O' => ["01110","10001","10001","10001","10001","10001","01110"],
    'P' => ["11110","10001","10001","11110","10000","10000","10000"],
    'Q' => ["01110","10001","10001","10001","10101","10010","01101"],
    'R' => ["11110","10001","10001","11110","10100","10010","10001"],
    'S' => ["01111","10000","10000","01110","00001","00001","11110"],
    'T' => ["11111","00100","00100","00100","00100","00100","00100"],
    'U' => ["10001","10001","10001","10001","10001","10001","01110"],
    'V' => ["10001","10001","10001","10001","10001","01010","00100"],
    'W' => ["10001","10001","10001","10101","10101","10101","01010"],
    'X' => ["10001","10001","01010","00100","01010","10001","10001"],
    'Y' => ["10001","10001","01010","00100","00100","00100","00100"],
    'Z' => ["11111","00001","00010","00100","01000","10000","11111"],
    '.' => ["00000","00000","00000","00000","00000","01100","01100"],
    ',' => ["00000","00000","00000","00000","00000","01100","01000"],
    ':' => ["00000","01100","01100","00000","01100","01100","00000"],
    ';' => ["00000","01100","01100","00000","01100","01000","10000"],
    '=' => ["00000","00000","11111","00000","11111","00000","00000"],
    '-' => ["00000","00000","00000","11111","00000","00000","00000"],
    '_' => ["00000","00000","00000","00000","00000","00000","11111"],
    '+' => ["00000","00100","00100","11111","00100","00100","00000"],
    '/' => ["00001","00010","00010","00100","01000","01000","10000"],
    '(' => ["00010","00100","01000","01000","01000","00100","00010"],
    ')' => ["01000","00100","00010","00010","00010","00100","01000"],
    '?' => ["01110","10001","00001","00010","00100","00000","00100"],
)

function glyph_rows(ch::Char)
    return get(FONT5X7, ch, FONT5X7['?'])
end

function text_width_px(text::AbstractString; scale::Int=1)
    isempty(text) && return 0
    return length(collect(text)) * 6 * scale - scale
end

function draw_text!(img, x, y, text::AbstractString, color::NTuple{3,UInt8}; scale::Int=1)
    x0 = round(Int, x)
    y0 = round(Int, y)
    cursor = x0
    for ch in uppercase(text)
        rows = glyph_rows(ch)
        for (row, bits) in enumerate(rows)
            for (col, bit) in enumerate(bits)
                bit == '1' || continue
                px0 = cursor + (col - 1) * scale
                py0 = y0 + (row - 1) * scale
                for yy in py0:py0 + scale - 1, xx in px0:px0 + scale - 1
                    set_pixel!(img, xx, yy, color)
                end
            end
        end
        cursor += 6 * scale
    end
    return img
end

function draw_text_center!(img, x, y, text::AbstractString, color::NTuple{3,UInt8}; scale::Int=1)
    draw_text!(img, x - text_width_px(uppercase(text); scale = scale) / 2, y, text, color; scale = scale)
end

function draw_text_right!(img, x, y, text::AbstractString, color::NTuple{3,UInt8}; scale::Int=1)
    draw_text!(img, x - text_width_px(uppercase(text); scale = scale), y, text, color; scale = scale)
end

function adler32(data::Vector{UInt8})
    a = UInt32(1)
    b = UInt32(0)
    mod_adler = UInt32(65521)
    for byte in data
        a = (a + UInt32(byte)) % mod_adler
        b = (b + a) % mod_adler
    end
    return (b << 16) | a
end

function crc32(data::Vector{UInt8})
    crc = UInt32(0xffffffff)
    for byte in data
        crc = xor(crc, UInt32(byte))
        for _ in 1:8
            mask = (crc & UInt32(1)) == UInt32(1) ? UInt32(0xffffffff) : UInt32(0)
            crc = xor(crc >> 1, UInt32(0xedb88320) & mask)
        end
    end
    return xor(crc, UInt32(0xffffffff))
end

function push_be32!(v::Vector{UInt8}, x::Integer)
    ux = UInt32(x)
    push!(v, UInt8((ux >> 24) & 0xff))
    push!(v, UInt8((ux >> 16) & 0xff))
    push!(v, UInt8((ux >> 8) & 0xff))
    push!(v, UInt8(ux & 0xff))
    return v
end

function push_le16!(v::Vector{UInt8}, x::Integer)
    ux = UInt16(x)
    push!(v, UInt8(ux & 0xff))
    push!(v, UInt8((ux >> 8) & 0xff))
    return v
end

function zlib_store(data::Vector{UInt8})
    out = UInt8[0x78, 0x01]
    i = 1
    while i <= length(data)
        n = min(65535, length(data) - i + 1)
        final = i + n - 1 == length(data)
        push!(out, final ? 0x01 : 0x00)
        push_le16!(out, n)
        push_le16!(out, xor(UInt16(0xffff), UInt16(n)))
        append!(out, @view data[i:i+n-1])
        i += n
    end
    push_be32!(out, adler32(data))
    return out
end

function png_chunk(kind::String, data::Vector{UInt8})
    out = UInt8[]
    push_be32!(out, length(data))
    kind_bytes = Vector{UInt8}(codeunits(kind))
    append!(out, kind_bytes)
    append!(out, data)
    push_be32!(out, crc32(vcat(kind_bytes, data)))
    return out
end

function write_png(path, img)
    h, w, _ = size(img)
    ihdr = UInt8[]
    push_be32!(ihdr, w)
    push_be32!(ihdr, h)
    append!(ihdr, UInt8[8, 2, 0, 0, 0])

    raw = UInt8[]
    sizehint!(raw, h * (1 + 3w))
    for y in 1:h
        push!(raw, 0x00)
        for x in 1:w
            push!(raw, img[y, x, 1])
            push!(raw, img[y, x, 2])
            push!(raw, img[y, x, 3])
        end
    end

    bytes = UInt8[0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]
    append!(bytes, png_chunk("IHDR", ihdr))
    append!(bytes, png_chunk("IDAT", zlib_store(raw)))
    append!(bytes, png_chunk("IEND", UInt8[]))
    open(path, "w") do io
        write(io, bytes)
    end
    return path
end

function write_spectrum_png(path, case, sector_labels, sector_momenta, shifted, gapinfo)
    geom = plot_coordinates(sector_labels, shifted)
    img = fill(UInt8(255), geom.height, geom.width, 3)
    grid = (UInt8(225), UInt8(229), UInt8(234))
    axis = (UInt8(17), UInt8(17), UInt8(17))
    text = (UInt8(17), UInt8(17), UInt8(17))
    muted = (UInt8(85), UInt8(85), UInt8(85))
    blue = (UInt8(47), UInt8(93), UInt8(124))
    red = (UInt8(178), UInt8(58), UInt8(72))
    draw_text_center!(img, geom.width / 2, 16, case.name, text; scale = 2)
    draw_text_center!(
        img,
        geom.width / 2,
        44,
        @sprintf("GAP=%.6g  RED=EXPECTED %d-STATE GS", gapinfo.gap, case.gsdeg_expect),
        muted;
        scale = 1,
    )
    for frac in 0.0:0.25:1.0
        y = geom.top + frac * geom.plot_h
        draw_line!(img, geom.left, y, geom.left + geom.plot_w, y, grid)
    end
    ticks = tick_indices(length(sector_labels))
    for i in ticks
        x = geom.sx(i)
        draw_line!(img, x, geom.top, x, geom.top + geom.plot_h, grid)
    end
    draw_line!(img, geom.left, geom.top + geom.plot_h, geom.left + geom.plot_w, geom.top + geom.plot_h, axis; thickness = 2)
    draw_line!(img, geom.left, geom.top, geom.left, geom.top + geom.plot_h, axis; thickness = 2)
    for i in ticks
        x = geom.sx(i)
        draw_text_center!(img, x, geom.top + geom.plot_h + 14, sector_label_text(sector_labels[i]), text; scale = 1)
        draw_text_center!(img, x, geom.top + geom.plot_h + 30, sector_k_text(sector_momenta[i]), muted; scale = 1)
    end
    for yval in ytick_values(geom)
        y = geom.sy(yval)
        draw_text_right!(img, geom.left - 10, y - 3, @sprintf("%.3g", yval), text; scale = 1)
    end
    draw_text_center!(img, geom.left + geom.plot_w / 2, geom.height - 34, "MOMENTUM SECTOR K AND COORDINATES (K1,K2)", text; scale = 1)
    draw_text!(img, 16, geom.top + geom.plot_h / 2 - 4, "E-E0", text; scale = 1)
    yfirst = geom.sy(first_excitation_shifted(gapinfo))
    draw_line!(img, geom.left, yfirst, geom.left + geom.plot_w, yfirst, red; thickness = 1)
    draw_text_right!(img, geom.left + geom.plot_w - 4, yfirst - 13, "FIRST EXCITATION", red; scale = 1)
    for (i, levels) in enumerate(shifted)
        x = geom.sx(i)
        for yval in levels
            y = geom.sy(yval)
            draw_line!(img, x - 7, y, x + 7, y, blue; thickness = 2)
        end
    end
    for (_, sector_index, level_index) in gapinfo.ground_multiplet
        x = geom.sx(sector_index)
        y = geom.sy(shifted[sector_index][level_index])
        draw_circle!(img, x, y, 5, red)
    end
    for (sector_index, levels) in ground_label_groups(gapinfo)
        x = geom.sx(sector_index)
        y = minimum(geom.sy(shifted[sector_index][level_index]) for level_index in levels)
        draw_text_center!(img, x, y - 17, ground_group_label(levels), red; scale = 1)
    end
    return write_png(path, img)
end

function plot_spectrum(path_png, path_pdf, path_svg, case, sector_labels, sector_momenta, shifted, gapinfo)
    write_spectrum_png(path_png, case, sector_labels, sector_momenta, shifted, gapinfo)
    write_spectrum_pdf(path_pdf, case, sector_labels, sector_momenta, shifted, gapinfo)
    write_spectrum_svg(path_svg, case, sector_labels, sector_momenta, shifted, gapinfo)
    return path_png, path_pdf, path_svg
end

function run_case(case::BenchmarkCase; data_dir, fig_dir, method::Symbol, overwrite::Bool, make_figures::Bool)
    stem = case.name
    spectrum_csv = joinpath(data_dir, stem * "_spectrum.csv")
    metadata_md = joinpath(data_dir, stem * "_metadata.md")
    result_jls = joinpath(data_dir, stem * "_result.jls")
    figure_png = joinpath(fig_dir, stem * "_spectrum.png")
    figure_pdf = joinpath(fig_dir, stem * "_spectrum.pdf")
    figure_svg = joinpath(fig_dir, stem * "_spectrum.svg")

    if isfile(result_jls) && !overwrite
        result = open(deserialize, result_jls)
        result["spectrum_csv"] = portable_path(spectrum_csv)
        result["metadata_md"] = portable_path(metadata_md)
        result["figure_png"] = make_figures ? portable_path(figure_png) : ""
        result["figure_pdf"] = make_figures ? portable_path(figure_pdf) : ""
        result["figure_svg"] = make_figures ? portable_path(figure_svg) : ""
        return result
    end

    @printf("Running %-28s Nk=%d N=%d method=%s\n", case.name, case.Nk, case.N, string(method))
    model_ref = Ref{Any}()
    materialize_time = @elapsed model_ref[] = materialize_case(case)
    model = model_ref[]

    sector_dims = Int[]
    sector_times = Float64[]
    spectra = Vector{Vector{Float64}}(undef, length(model.subspaces))
    solve_time = @elapsed begin
        for (i, subspace) in enumerate(model.subspaces)
            dim_ref = Ref(0)
            t = @elapsed begin
                vals, dim = solve_sector_spectrum(
                    subspace,
                    model.scat,
                    case.selecteg;
                    method = method,
                    tol = 1e-14,
                )
                spectra[i] = vals
                dim_ref[] = dim
            end
            push!(sector_dims, dim_ref[])
            push!(sector_times, t)
            k = model.sector_momenta[i]
            @printf("  sector %3d k=(%d,%d) dim=%4d levels=%2d time=%.3f s\n",
                model.sector_labels[i], k[1], k[2], dim_ref[], length(spectra[i]), t)
        end
    end

    shifted, e0 = shifted_spectra(spectra)
    gapinfo = gap_from_spectra(spectra; gsdeg_expect = case.gsdeg_expect)

    mkpath(data_dir)
    mkpath(fig_dir)
    write_spectrum_csv(spectrum_csv, case, model.sector_momenta, model.sector_labels, spectra, shifted)

    settings = Dict{String,Any}(
        "ell" => case.ell,
        "Gfactor" => model.Gfactor,
        "Auc" => model.Auc,
        "ds" => model.ds,
        "ds_over_ell" => case.ds_over_ell,
        "V0_user" => case.V0,
        "V0_code" => model.V0_code,
        "include_gfactor_prefactor" => case.include_gfactor_prefactor,
        "n_shells" => case.n_shells,
        "shell_values" => shell_values(case),
        "interaction_kernel" => "V(q)=V0_code*tanh(|q|*ds)/|q| with q=0 limit V0_code*ds",
    )

    result = Dict{String,Any}(
        "case" => case_to_dict(case),
        "settings" => settings,
        "method" => String(method),
        "Gk" => model.Gk,
        "sector_momenta" => model.sector_momenta,
        "sector_labels" => model.sector_labels,
        "spectra_by_sector" => spectra,
        "shifted_spectra" => shifted,
        "energy_zero" => e0,
        "gap" => gapinfo.gap,
        "ground_energy" => gapinfo.ground_energy,
        "first_excitation" => gapinfo.first_excitation,
        "ground_multiplet" => gapinfo.ground_multiplet,
        "gapinfo" => gapinfo,
        "sector_dims" => sector_dims,
        "sector_times_sec" => sector_times,
        "materialize_time_sec" => materialize_time,
        "solve_time_sec" => solve_time,
        "spectrum_csv" => portable_path(spectrum_csv),
        "metadata_md" => portable_path(metadata_md),
        "figure_png" => make_figures ? portable_path(figure_png) : "",
        "figure_pdf" => make_figures ? portable_path(figure_pdf) : "",
        "figure_svg" => make_figures ? portable_path(figure_svg) : "",
    )

    write_metadata_md(metadata_md, case, model, result)
    if make_figures
        plot_spectrum(figure_png, figure_pdf, figure_svg, case, model.sector_labels, model.sector_momenta, shifted, gapinfo)
    end

    open(result_jls, "w") do io
        serialize(io, result)
    end

    @printf("  gap=%.12g, materialize=%.3f s, solve=%.3f s\n",
        Float64(result["gap"]), materialize_time, solve_time)
    return result
end

function selected_cases(all_cases, selector::String)
    selector in ("all", "") && return all_cases
    names = split(selector, ",")
    chosen = BenchmarkCase[]
    by_name = Dict(c.name => c for c in all_cases)
    for name in names
        haskey(by_name, name) || error("Unknown benchmark case '$name'. Use --list-cases true to inspect names.")
        push!(chosen, by_name[name])
    end
    return chosen
end

function main(argv = ARGS)
    opts = parse_kv_args(argv)
    all_cases = benchmark_cases()

    if parse_bool(opts, "list-cases", false)
        for case in all_cases
            println(case.name, " -- ", case.description)
        end
        return nothing
    end

    data_dir = get(opts, "data-dir", joinpath(@__DIR__, "data"))
    fig_dir = get(opts, "fig-dir", joinpath(@__DIR__, "figures"))
    method = method_symbol(get(opts, "method", "sparse"))
    overwrite = parse_bool(opts, "overwrite", false)
    make_figures = !parse_bool(opts, "no-figures", false)
    cases = selected_cases(all_cases, get(opts, "case", "all"))

    mkpath(data_dir)
    mkpath(fig_dir)
    results = Dict{String,Any}[]
    for case in cases
        push!(results, run_case(case; data_dir, fig_dir, method, overwrite, make_figures))
    end

    summary_csv = joinpath(data_dir, "benchmark_summary.csv")
    write_summary_csv(summary_csv, results)
    println("Wrote summary: ", summary_csv)
    return results
end

if abspath(PROGRAM_FILE) == @__FILE__
    main()
end
