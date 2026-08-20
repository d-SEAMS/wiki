# In-plane RDF

Figshare:
[In-plane 2D RDF LAMMPS Trajectory](https://figshare.com/articles/In_plane_2D_RDF_LAMMPS_Trajectory/11448711).
fMSI at 320 K. The pair histogram is normalized to an ideal gas.

The `seams` CLI has no RDF command.

## Python

```python
import pydseams as ds

frame = ds.read("dump-320.lammpstrj")
r, g = frame.rdf_2d(output_dir="output/", cutoff=12.0, binwidth=0.05)
```

`rdf_2d` returns bin centres and `g(r)`. The engine also writes
`topoMonolayer/rdf.dat` under `output_dir`.

## Lua

`dseams.rdf` returns a partial three-dimensional RDF and is not the
in-plane calculation shown here:

```lua
local dseams = require("dseams")
local cloud = dseams.read("dump-320.lammpstrj", {type = 2})
local result = dseams.rdf(cloud, {type_i = 2, type_j = 2,
                                  cutoff = 12.0, bins = 240})
print(result.r[1], result.g[1])
```

The in-plane output writer is the low-level registration
`dseams.core.calcRDF`. Its 1.x script depends on a CLI-injected accumulator,
so `Frame.rdf_2d` is the supported library workflow for this demonstration.

## References

1. The in-plane RDF demonstration in the 2020 d-SEAMS paper,
   doi:[10.1021/acs.jcim.0c00031](https://doi.org/10.1021/acs.jcim.0c00031).
