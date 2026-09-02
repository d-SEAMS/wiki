# Bulk HC / DDC cages

Figshare:
[Nucleation LAMMPS Trajectory](https://figshare.com/articles/Nucleation_LAMMPS_Trajectory/11448702)
(4096 mW waters after crystallization). Hexagonal cages (HC),
double-diamond cages (DDC), and mixed rings sit on the ice cluster.

`seams cages` is the 2.x replacement for the 1.x
`bulkTopologicalCriterion` Lua script.

## CLI

`--graph` defaults to `seeded`. `--complete` turns on ring-adjacent
completion of that seeded assignment.

```bash
seams cages nucleation.lammpstrj --type 2 --graph seeded --complete
```

Other bond graphs: `--graph cutoff`, `--graph knn`, `--graph knn-union`.
`-k` (default 4) applies to `knn`, `knn-union`, and `seeded`.

Stdout is `nop N graph KIND hexagonal IH cubic IC water W`. Hexagonal
is HC (Ih), cubic is DDC (Ic), water is neither.

## Python

`Frame.cages` defaults to the seeded construction. `ring_adjacent=True`
is the same completion as `--complete`.

```python
from pydseams import Frame

frame = Frame.from_file("nucleation.lammpstrj", atom_type=2)
print(frame.cages(ring_adjacent=True))
print(frame.seeded_affiliation(ring_adjacent=True))
```

`cages(seeded=False)` is cutoff-graph affiliation on this frame's
six-rings. `IceFeaturizer` turns ring-adjacent completion on by default.

## Lua

```lua
local dseams = require("dseams")
local cloud = dseams.read("nucleation.lammpstrj", {type = 2})
print(dseams.cages(cloud, {complete = true}))
```

`dseams.cages` always uses the seeded pair of k-nearest graphs.
`complete` fills the last vertex of a six-ring whose other vertices
carry a label.

Books: [seams cages](https://docs.dseams.info/tutorials/bulk-ice.html),
[pydseams](https://d-seams.github.io/PydSEAMSlib/tutorials/classify-ice.html).

## References

1. Haji-Akbari, A.; Debenedetti, P. G. *Proc. Natl. Acad. Sci.* **2015**,
   *112*, 10582. doi:[10.1073/pnas.1509267112](https://doi.org/10.1073/pnas.1509267112)
