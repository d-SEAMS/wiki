# CHILL+ on a cubic lattice

Figshare:
[CHILL LAMMPS Trajectory](https://figshare.com/articles/CHILL_LAMMPS_Trajectory/11448720)
(`mW_cubic.lammpstrj`, 4096 type-1 mW sites of ice Ic). CHILL+
labels every site cubic on that lattice. `nucleation.lammpstrj` is
a different figshare deposit.

The 1.x driver (`yodaStruct -c`, `conf.yaml`, `lua_inputs/`) is gone.
Use `seams`, `pydseams`, or `require("dseams")`.

## CLI

```bash
seams read mW_cubic.lammpstrj --type 1
seams chill mW_cubic.lammpstrj --cutoff 3.5 --type 1
seams chill-plus mW_cubic.lammpstrj --cutoff 3.5 --type 1
```

Counts print to stdout (`cubic`, `hexagonal`, `water`,
`interfacial`, `clathrate`, `interClathrate`, `reCubic`, `reHex`,
`unclassified`). `chill_plus` is an accepted alias of `chill-plus`.

## Python

`ds.read` is a suffix-dispatch alias of `Frame.from_file` for LAMMPS
dumps. New examples use the constructor.

```python
from pydseams import Frame

frame = Frame.from_file("mW_cubic.lammpstrj", atom_type=1)
print(frame.chill_plus())
```

ASE and raw arrays use the other constructors:

```python
from pydseams import Frame

frame = Frame.from_ase(atoms)                 # default select="O"
frame = Frame.from_arrays(positions, cell, numbers=[1, 1, 1, 1])
```

## Lua

```lua
local dseams = require("dseams")
local cloud = dseams.read("mW_cubic.lammpstrj", {type = 1})
print(dseams.chill_plus(cloud, {cutoff = 3.5}))
```

Books: [seams CLI](https://docs.dseams.info/tutorials/bulk-ice.html),
[pydseams](https://d-seams.github.io/PydSEAMSlib/tutorials/classify-ice.html),
[dseams](https://d-seams.github.io/yodaStruct/tutorials/read-and-classify.html).

## References

1. Nguyen, A. H.; Molinero, V. *J. Phys. Chem. B* **2015**, *119*, 9369.
   doi:[10.1021/jp510289t](https://doi.org/10.1021/jp510289t)
