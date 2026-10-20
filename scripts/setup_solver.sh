#!/bin/bash
# Set up the Julia ED solver: fetch MomentumED.jl at the commit the solver was built on, apply the local
# patch (Julia 1.10 compatibility and two GPU memory flags; see julia/patches/README.md), and instantiate
# the julia/ environment against it.
#
#   scripts/setup_solver.sh                 # uses `julia` on PATH
#   JULIA=/path/to/julia scripts/setup_solver.sh
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
JULIA="${JULIA:-julia}"
URL="https://github.com/Zou-Bo/MomentumED.jl"
REV="40400d4ebc6eea5456276f3fcd1c6637736ea2dd"
PATCH="$ROOT/julia/patches/MomentumED-40400d4.patch"
DEPS="$ROOT/julia/deps/MomentumED.jl"

if [ ! -d "$DEPS/.git" ]; then
  git clone --quiet "$URL" "$DEPS"
fi
if git -C "$DEPS" apply --reverse --check "$PATCH" 2>/dev/null; then
  echo "MomentumED.jl already at $REV with the patch applied"
else
  git -C "$DEPS" checkout --quiet "$REV"
  git -C "$DEPS" apply "$PATCH"
  echo "MomentumED.jl checked out at $REV and patched"
fi

# julia/Manifest.toml pins every package at the version the campaigns ran with and finds EDCore and
# MomentumED under julia/deps/ by relative path.
"$JULIA" --project="$ROOT/julia" -e 'using Pkg; Pkg.instantiate(); Pkg.precompile()'
