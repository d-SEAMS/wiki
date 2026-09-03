# Wiki

Process, worked examples, and the 2020 SQM notes. The product page is
[dseams.info](https://dseams.info). API books:

- Engine and `seams` CLI: [docs.dseams.info](https://docs.dseams.info)
- Python `Frame`: [pydseams](https://d-seams.github.io/PydSEAMSlib/)
- Lua `require("dseams")`: [yodaStruct](https://d-seams.github.io/yodaStruct/)
- PLUMED action: [dseams-plumed](https://github.com/d-SEAMS/dseams-plumed)

Cite the 2020 paper (DOI
[10.1021/acs.jcim.0c00031](https://doi.org/10.1021/acs.jcim.0c00031),
[arXiv:1909.09830](https://arxiv.org/abs/1909.09830)).

Trajectories: [figshare project 73545](https://figshare.com/projects/d-SEAMS_Datasets/73545).
Records: [Zenodo community](https://zenodo.org/communities/d-seams/).

## Examples

These pages use the 2.7 public API. `seams` covers `read`, `chill`,
`chill-plus`, `cages --graph seeded --complete`, `fingerprint`,
`ions`, `rdf`, `cn`, `hbonds`, `pairs`, `density-z`, and `domains`.
`pydseams` adds `Frame.from_file` / `from_ase` / `from_arrays`,
`fingerprint`, `ion_environment`, and `IceFeaturizer`. Lua is
`require("dseams")`. Collective variables use `DSEAMS_CAGES`.
The 2020 YAML / `yodaStruct -c` driver is gone.

`ds.read` remains a documented suffix-dispatch alias; new examples
call `Frame.from_file` for LAMMPS dumps.

- [seams CLI](examples/cli.md)
- [CHILL+ on a cubic lattice](examples/chillPlus.md)
- [Bulk HC / DDC cages](examples/bulkTopologicalCriterion.md)
- [Topology fingerprint](examples/fingerprint.md)
- [Ions against cages](examples/ions.md)
- [Ice features](examples/features.md)
- [Visualise labels](examples/visualise.md)
- [PLUMED DSEAMS_CAGES](examples/plumed.md)
- [Ice nanotube prisms](examples/iceNanotube.md)
- [Monolayer square ice](examples/monolayer.md)
- [In-plane RDF](examples/rdf2d.md)

## Python and Lua libraries

The Python distribution is `pydseamslib` and its import is `pydseams`.
The Lua module is `require("dseams")`; `require("yoda")` is a compatibility
alias. Both libraries call the native engine and expose trajectory reading,
CHILL/CHILL+, cages, fingerprints, ion environments, radial distributions,
coordination numbers, hydrogen bonds, density profiles, ionic pairs, and
domain statistics.

Use the generated books for the live names:

- [Python `Frame` and native API](https://d-seams.github.io/PydSEAMSlib/reference/python.html)
- [Lua helpers](https://d-seams.github.io/yodaStruct/reference/lua.html)
- [Lua compiled registrations](https://d-seams.github.io/yodaStruct/reference/lua-functions.html)

## Process

The [SQM plan](SQM%20Plan/index.md) is the 2020 Software Quality
Management course artifact. Keep it as history.

[Contributing](02_Contributing.md) ·
[Code of conduct](01_Code_of_Conduct.md) ·
[License](03_license.md)
