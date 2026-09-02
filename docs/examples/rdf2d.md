# In-plane RDF

Figshare:
[In-plane 2D RDF LAMMPS Trajectory](https://figshare.com/articles/In_plane_2D_RDF_LAMMPS_Trajectory/11448711).
fMSI at 320 K. The pair histogram is normalized to an ideal gas.

`seams rdf` is the three-dimensional site-site `g_IJ(r)`, not this
in-plane calculation. The in-plane writer is `Frame.rdf_2d`.

## CLI (3D site-site)

```bash
seams rdf dump-320.lammpstrj --types 2,2 --cutoff 12 --bins 240
```

Stdout is `# r g count`, then a header with types, rmax, bins, and
volume, then one `r g count` row per bin.

## Python

```python
from pydseams import Frame

frame = Frame.from_file("dump-320.lammpstrj")
r, g = frame.rdf_2d(output_dir="output/", cutoff=12.0, binwidth=0.05)
```

`rdf_2d` returns bin centres and `g(r)`. The engine also writes
`topoMonolayer/rdf.dat` under `output_dir`.

The 3D counterpart on the same frame is `frame.rdf(2, 2, cutoff=12.0,
binwidth=0.05)`.

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
so `Frame.rdf_2d` is the supported library workflow for this page.

## References

1. The in-plane RDF page in the 2020 d-SEAMS paper,
   doi:[10.1021/acs.jcim.0c00031](https://doi.org/10.1021/acs.jcim.0c00031).
