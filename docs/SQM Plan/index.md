# Software Quality Management Plan

This is the **2020 Software Quality Management course artifact**. Keep
it as process history. It is not the 2.x contributor handbook.

Live contribution:

- Engine: [seams-core](https://github.com/d-SEAMS/seams-core) (`CONTRIBUTING.md`, pixi + meson, Catch2)
- Python: [PydSEAMSlib](https://github.com/d-SEAMS/PydSEAMSlib)
- Lua/Fennel: [yodaStruct](https://github.com/d-SEAMS/yodaStruct) (`require("dseams")`)
- This wiki: [d-SEAMS/wiki](https://github.com/d-SEAMS/wiki)

The 2020 product was one `yodaStruct` binary, YAML plus Lua, CMake or
the old Nix derivation. 2.x is `libyodaLib` plus `seams` / `pydseams` /
`require("dseams")`. Runtime knobs are twelve-factor (`SEAMS_CONFIG` /
`seams.env`). There is no `yodaStruct -c` / `conf.yaml` driver.

## Repository details (2020 text, still true in spirit)

- Development is public on GitHub
- The C++ engine [is here](https://github.com/d-SEAMS/seams-core)
- The wiki is [here](https://github.com/d-SEAMS/wiki)

## Style Guide

The 2020 diversity note listed a C++ back-end, a Lua front-end, YAML
input, Nix+CMake, and OVITO. That mix is what the
[style guide](00_styleGuide.md) was written for.

What still applies: `clang-format`, namespaces, Catch2, Doxygen with
formulae and citations, public PRs.

What does not: YAML as the engine config, CMake as the live build,
"every C++ function must have a Lua binding", `yaml-cpp` / `cxxopts`
as engine dependencies.

### Docs

- Documentation is the single source of truth. The [GitLab
  style-guide](https://docs.gitlab.com/ee/development/documentation/styleguide.html)
  is still a good starting point.
- Every change should be documented, along with the rationale.

The live books are Diataxis: [docs.dseams.info](https://docs.dseams.info),
[pydseams](https://d-seams.github.io/PydSEAMSlib/),
[dseams](https://d-seams.github.io/yodaStruct/).
