# CHILL+ on a cubic lattice

Figshare:
[CHILL LAMMPS Trajectory](https://figshare.com/articles/CHILL_LAMMPS_Trajectory/11448720)
(`nucleation.lammpstrj`, 4096 molecules of ice Ic). CHILL+ labels
every oxygen cubic on that lattice.

The 1.x driver (`yodaStruct -c`, `conf.yaml`, `lua_inputs/`) is gone.
Use `seams`, `pydseams`, or `require("dseams")`.

## CLI

```bash
seams chill-plus nucleation.lammpstrj --cutoff 3.5 --type 2
```

Counts print to stdout (cubic, hexagonal, interfacial, clathrate,
water).

## Python

```python
import pydseams as ds

frame = ds.read("nucleation.lammpstrj")
print(frame.chill_plus())
```

## Lua

```lua
local dseams = require("dseams")
local cloud = dseams.read("nucleation.lammpstrj", {type = 2})
print(dseams.chill_plus(cloud, {cutoff = 3.5}))
```

Books: [seams CLI](https://docs.dseams.info/tutorials/bulk-ice.html),
[pydseams](https://d-seams.github.io/PydSEAMSlib/tutorials/classify-ice.html),
[dseams](https://d-seams.github.io/yodaStruct/tutorials/read-and-classify.html).

## References

1. Nguyen, A. H.; Molinero, V. *J. Phys. Chem. B* **2015**, *119*, 9369.
   doi:[10.1021/jp510289t](https://doi.org/10.1021/jp510289t)
