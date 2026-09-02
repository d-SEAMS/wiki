# Bulk hexagonal and double-diamond cages

Figshare:
[Nucleation LAMMPS Trajectory](https://figshare.com/articles/Nucleation_LAMMPS_Trajectory/11448702)
(4096 mW waters after crystallization). Hexagonal cages (HC),
double-diamond cages (DDC), and mixed rings sit on the ice cluster.

`seams cages` is the 2.x replacement for the 1.x
`bulkTopologicalCriterion` Lua script.

## CLI

```bash
seams cages nucleation.lammpstrj --type 2 --graph seeded --complete
```

`--graph` is `seeded` (default), `cutoff`, `knn`, or `knn-union`.
`--complete` fills the last vertex of a six-ring whose other
vertices already carry a cage label. That flag applies to the
seeded assignment.

## Python

```python
from pydseams import Frame

frame = Frame.from_file("nucleation.lammpstrj")
print(frame.cages(ring_adjacent=True))
print(frame.seeded_affiliation(ring_adjacent=True))
```

`Frame.cages(seeded=True)` is the hysteresis construction.
`ring_adjacent=True` is the same completion as `seams cages --complete`.
`Frame.cages` and `Frame.seeded_affiliation` leave that flag off
unless you pass it.

## Lua

```lua
local dseams = require("dseams")
local cloud = dseams.read("nucleation.lammpstrj", {type = 2})
print(dseams.cages(cloud, {complete = true}))
```

Books: [seams cages](https://docs.dseams.info/tutorials/bulk-ice.html),
[pydseams](https://d-seams.github.io/PydSEAMSlib/tutorials/classify-ice.html).

## References

1. Haji-Akbari, A.; Debenedetti, P. G. *Proc. Natl. Acad. Sci.* **2015**,
   *112*, 10582. doi:[10.1073/pnas.1509267112](https://doi.org/10.1073/pnas.1509267112)
