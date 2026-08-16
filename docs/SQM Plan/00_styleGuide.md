# Style Guide

This page is the 2020 SQM style note. Read it as history of how the
single-binary product was formatted. It is not the 2.x contributor
handbook. Live commit style is Conventional Commits in seams-core
`CONTRIBUTING.md`. The live build is pixi + meson (or the Nix
flake). The live languages are C++ in seams-core, Python in
PydSEAMSlib, and Lua/Fennel in yodaStruct.

## Code formatting (still current)

- Formatting should be consistent
- Use the repo's automated formatters (`clang-format` on the engine,
  ruff on pydseams)
- Formatters stay IDE-independent

### Clang Format

The engine ships a `clang-format` file at the seams-core root.

- [Emacs](https://github.com/lassik/emacs-format-all-the-code)
- [Sublime Text](https://packagecontrol.io/packages/Clang%20Format)
- [Vim](https://github.com/rhysd/vim-clang-format)

## C++ (engine)

- `clang-format` on seams-core
- Prefer clang / LLVM tooling
- The live language standard is C++20 (`meson.build`)
- Prefer comments that carry science over verbose code

!!! warning "Use namespaces"
    Namespaces are still required. No file-scope `using namespace`.

- Doxygen generates the [engine API](https://docs.dseams.info)

!!! note "Annotate scientific details"
    Formulae (LaTeX) and citations on every method that implements one

- Catch2 for C++ tests
- Lua bindings live in yodaStruct. They are not required for every
  new engine function. Register what the `dseams` library exposes.

Libraries the 2020 note listed. Several are gone from the default
engine graph:

| Then | Now |
| --- | --- |
| Catch2 | yes |
| cxxopts | Catch2 harness only; `seams` uses Argum |
| rang | yes (CLI colors; `NO_COLOR`) |
| sol2 | yodaStruct, not seams-core |
| yaml-cpp | gone; twelve-factor knobs |
| LAPACK / BLAS | yes |
| Spectra / Boost Geometry / Boost Math | not the default 2.x path |
| vesin / linkcell | cutoff list and periodic k-NN |

!!! note "Use included libraries"
    Do not add a dependency unless the algorithm needs it and it is
    on the pixi / meson / flake graph.

### Resources

- [LLVM coding standards](https://llvm.org/docs/CodingStandards.html)
- Match the file you are in. Do not restyle the tree.

## Lua (yodaStruct)

- Scripts carry comments and name the trajectory they need
- Compiled registrations are Doxygen of `lua_api.hpp` on the
  [yodaStruct book](https://d-seams.github.io/yodaStruct/reference/lua-functions.html)
- Helpers stay in `lua/dseams.lua` (`require("dseams")`)

There is no project-wide YAML input. `example_lua/*/config.yml` files
are 1.x script descriptors, not deploy config.

## Nix (engine flake)

The CMake-era `yodaStruct` derivation and `shell.nix` are gone. The
flake builds `libyodaLib` and `seams` with meson.

- Do not check in a laptop-built binary
- CI is the purity gate

### Resources

- [Nix pills](https://nixos.org/guides/nix-pills/)
- The `flake.nix` in seams-core, PydSEAMSlib, and yodaStruct
