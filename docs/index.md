# Wiki

Process, worked examples, and the 2020 SQM notes. The product page is
[dseams.info](https://dseams.info). API books:

- Engine and `seams` CLI: [docs.dseams.info](https://docs.dseams.info)
- Python `Frame`: [pydseams](https://d-seams.github.io/PydSEAMSlib/)
- Lua `require("dseams")`: [yodaStruct](https://d-seams.github.io/yodaStruct/)

Cite the 2020 paper (DOI
[10.1021/acs.jcim.0c00031](https://doi.org/10.1021/acs.jcim.0c00031),
[arXiv:1909.09830](https://arxiv.org/abs/1909.09830)).

Trajectories: [figshare project 73545](https://figshare.com/projects/d-SEAMS_Datasets/73545).
Records: [Zenodo community](https://zenodo.org/communities/d-seams/).

## Examples

These are the five 1.x figshare demonstrations, rewritten for 2.x.
`seams` covers bulk CHILL+ and cages. Nanotube prisms, monolayer
rings, and the in-plane RDF go through `pydseams` or
`require("dseams")`. The 2020 YAML / `yodaStruct -c` driver is gone.

- [CHILL+ on a cubic lattice](examples/chillPlus.md)
- [Bulk HC / DDC cages](examples/bulkTopologicalCriterion.md)
- [Ice nanotube prisms](examples/iceNanotube.md)
- [Monolayer square ice](examples/monolayer.md)
- [In-plane RDF](examples/rdf2d.md)

## Process

The [SQM plan](SQM%20Plan/index.md) is the 2020 Software Quality
Management course artifact. Keep it as history.

[Contributing](02_Contributing.md) ·
[Code of conduct](01_Code_of_Conduct.md) ·
[License](03_license.md)
