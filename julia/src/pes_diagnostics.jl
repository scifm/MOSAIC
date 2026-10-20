# Opt-in PES integration. Included into MoireSolver; no extra ED for normal runs.

function pes_from_ed_spectrum(para, subspaces, momenta, energies, vectors, scat, ed,
    settings::AbstractDict, m::Int; stats=nothing)
    allowed = Set(["NA","holes","parents","nparents","threaded","memory_budget_bytes",
        "verbose","zero_tol","level_floor","threshold_mode","threshold","given_count",
        "expected_counts","gap_min","auto_min_gap"])
    unknown = setdiff(Set(string.(keys(settings))),allowed)
    isempty(unknown) || throw(ArgumentError("Unknown PES settings: $(sort(collect(unknown)))."))
    haskey(settings,"NA") || throw(ArgumentError("extra.pes.NA is required."))
    settings["NA"] isa Integer && !(settings["NA"] isa Bool) ||
        throw(ArgumentError("extra.pes.NA must be an integer."))
    for key in ("nparents","given_count","memory_budget_bytes")
        value=get(settings,key,nothing)
        value === nothing || (value isa Integer && !(value isa Bool)) ||
            throw(ArgumentError("extra.pes.$(key) must be an integer or null."))
    end
    for key in ("holes","threaded","verbose")
        haskey(settings,key) && !(settings[key] isa Bool) &&
            throw(ArgumentError("extra.pes.$(key) must be boolean."))
    end
    for key in ("zero_tol","level_floor","gap_min","auto_min_gap","threshold")
        value=get(settings,key,nothing)
        value === nothing && (!haskey(settings,key) || key=="threshold") && continue
        value isa Real && !(value isa Bool) && isfinite(value) ||
            throw(ArgumentError("extra.pes.$(key) must be a finite number."))
    end
    get(settings,"threshold_mode","none") isa AbstractString ||
        throw(ArgumentError("extra.pes.threshold_mode must be a string."))
    haskey(settings,"parents") && haskey(settings,"nparents") &&
        throw(ArgumentError("Specify PES parents or nparents, not both."))
    picks = if haskey(settings,"parents")
        settings["parents"] isa AbstractVector || throw(ArgumentError("PES parents must be an array."))
        # Explicit momenta, rather than this project's basis-array indices.
        [(begin
            pick isa AbstractDict && haskey(pick,"momentum") && haskey(pick,"state") ||
                throw(ArgumentError("Each PES parent needs momentum and a one-based state index."))
            momentum=pick["momentum"]
            momentum isa AbstractVector && length(momentum)==2 &&
                all(x -> x isa Integer && !(x isa Bool),momentum) ||
                throw(ArgumentError("PES parent momentum must contain two integers."))
            pick["state"] isa Integer && !(pick["state"] isa Bool) ||
                throw(ArgumentError("PES parent state must be an integer."))
            k = Tuple(Int.(pick["momentum"]))
            b = findfirst(==(k),momenta)
            b === nothing && throw(ArgumentError("Unknown PES parent momentum $(k)."))
            (b,Int(pick["state"]))
        end) for pick in settings["parents"]]
    else
        n = Int(something(get(settings,"nparents",nothing),m))
        1 <= n <= sum(length,energies) || throw(ArgumentError("Invalid PES nparents."))
        all(length(energies[b]) >= min(n,length(subspaces[b])) for b in eachindex(subspaces)) ||
            throw(ArgumentError("PES nparents=$(n) requires extra.neigen_per_block >= $(n)."))
        lowest_states(energies,n)
    end
    isempty(picks) && throw(ArgumentError("PES needs at least one parent."))
    length(unique(picks)) == length(picks) || throw(ArgumentError("Duplicate PES parent selection."))
    for (b,st) in picks
        1 <= st <= length(energies[b]) || throw(ArgumentError("PES parent state is outside the computed spectrum."))
    end
    needed = Dict(b => maximum(st for (bb,st) in picks if bb==b) for (b,_) in picks)
    missing = [b for b in sort(collect(keys(needed))) if vectors[b] === nothing || length(vectors[b]) < needed[b]]
    gpu = isempty(missing) || ed.backend != :gpu ? nothing : gpu_solve_batch(
        Tuple{Int,Any}[(b,:pes) for b in missing],subspaces,_ -> scat,get_bits(first(subspaces));
        Neigen=ed.nlevels,keep=maximum(values(needed)),krylov_kw(ed)...)
    for b in missing
        n = min(ed.nlevels,length(subspaces[b]))
        vals,vecs,st = gpu === nothing ? cpu_solve(ed,subspaces[b],scat; N=n,keep=needed[b]) : gpu[(b,:pes)]
        stats === nothing || record!(stats,st,n)
        isapprox(real.(vals),energies[b]; atol=1e-8,rtol=1e-8) ||
            error("PES explicit parent-sector solve disagrees at momentum $(momenta[b]).")
        vectors[b] = vecs
    end
    parents = MBS64Vector[vectors[b][st] for (b,st) in picks]
    result = pes_spectrum(para,parents,Int(settings["NA"]);
        holes=Bool(get(settings,"holes",false)), threaded=Bool(get(settings,"threaded",true)),
        memory_budget_bytes=get(settings,"memory_budget_bytes",nothing),
        verbose=Bool(get(settings,"verbose",false)), zero_tol=Float64(get(settings,"zero_tol",1e-14)),
        level_floor=Float64(get(settings,"level_floor",1e-15)),
        threshold_mode=Symbol(get(settings,"threshold_mode","none")), threshold=get(settings,"threshold",nothing),
        given_count=get(settings,"given_count",nothing), expected_counts=get(settings,"expected_counts",nothing),
        gap_min=Float64(get(settings,"gap_min",0.5)), auto_min_gap=Float64(get(settings,"auto_min_gap",0.0)))
    out = Dict{Symbol,Any}(pairs(result))
    out[:levels] = [[isfinite(x) ? x : nothing for x in es] for es in result.levels]
    out[:parents] = [Dict(:momentum=>momenta[b],:state=>st,:energy=>energies[b][st]) for (b,st) in picks]
    out[:mixture] = "equal_incoherent"
    return out
end
