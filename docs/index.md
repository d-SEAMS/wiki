# Wiki

Process, worked examples, and the 2020 Software Quality Management
notes. The product page is
[dseams.info](https://dseams.info). API books:

- Engine and `seams` CLI: [docs.dseams.info](https://docs.dseams.info)
- Python `Frame`: [pydseams](https://d-seams.github.io/PydSEAMSlib/)
- Lua `require("dseams")`: [yodaStruct](https://d-seams.github.io/yodaStruct/)
- PLUMED action: [dseams-plumed](https://github.com/HaoZeke/dseams-plumed)

Cite the 2020 paper (digital object identifier
[10.1021/acs.jcim.0c00031](https://doi.org/10.1021/acs.jcim.0c00031),
[arXiv:1909.09830](https://arxiv.org/abs/1909.09830)).

Trajectories: [figshare project 73545](https://figshare.com/projects/d-SEAMS_Datasets/73545).
Records: [Zenodo community](https://zenodo.org/communities/d-seams/).

## Examples

These pages use the 2.7.0 public API. `seams` covers `read`,
`chill`, `chill-plus`, `cages`, `fingerprint`, `ions`, `rdf`, `cn`,
`hbonds`, `pairs`, `density-z`, and `domains`. New Python examples
use `Frame.from_file`; `ds.read` remains a suffix-dispatch alias.
`Frame.find_prisms`, `Frame.monolayer_rings`, and `Frame.rdf_2d` are
the output-writing confined-ice helpers. The 2020 YAML /
`yodaStruct -c` driver is gone.

The four-neighbour ice classifier (CHILL) and CHILL+ label bulk ice.
Hexagonal cages (HC) and double-diamond cages (DDC) are the
topological ice score. In-plane radial distribution function (RDF)
pages stay on `Frame.rdf_2d`.

- [seams CLI](examples/cli.md)
- [CHILL+ on a cubic lattice](examples/chillPlus.md)
- [Bulk HC / DDC cages](examples/bulkTopologicalCriterion.md)
- [Ice nanotube prisms](examples/iceNanotube.md)
- [Monolayer square ice](examples/monolayer.md)
- [In-plane RDF](examples/rdf2d.md)
- [Topology fingerprints](examples/fingerprint.md)
- [Ions against the cage assignment](examples/ions.md)
- [Kinetic features](examples/features.md)
- [PLUMED DSEAMS_CAGES](examples/plumed.md)

## Python and Lua libraries

The Python distribution is `pydseamslib` and its import is `pydseams`.
The Lua module is `require("dseams")`; `require("yoda")` is a compatibility
alias. Both libraries call the native engine and expose trajectory reading,
CHILL/CHILL+, cages, fingerprints, ion environments, radial
distributions, coordination numbers, hydrogen bonds, density
profiles, ionic pairs, and domain statistics.

Use the generated books for the live names:

- [Python `Frame` and native API](https://d-seams.github.io/PydSEAMSlib/reference/python.html)
- [Lua helpers](https://d-seams.github.io/yodaStruct/reference/lua.html)
- [Lua compiled registrations](https://d-seams.github.io/yodaStruct/reference/lua-functions.html)

## Process

The [Software Quality Management plan](SQM%20Plan/index.md) is the
2020 course artifact. Keep it as history.

[Contributing](02_Contributing.md) ·
[Code of conduct](01_Code_of_Conduct.md) ·
[License](03_license.md)
