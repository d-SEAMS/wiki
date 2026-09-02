# In-plane radial distribution

Figshare:
[In-plane 2D RDF LAMMPS Trajectory](https://figshare.com/articles/In_plane_2D_RDF_LAMMPS_Trajectory/11448711).
fMSI at 320 K. The pair histogram is normalized against a gas of
the same density.

`seams rdf` is the three-dimensional site-site radial distribution
function (RDF) `g_IJ(r)`. The in-plane page uses `Frame.rdf_2d`.

## CLI (3D site-site)

```bash
seams rdf dump-320.lammpstrj --types 2,2 --cutoff 12 --bins 240
```

`--types I,J` selects the pair. Omit it to use `--type` on both sides.

## Python (in-plane)

```python
from pydseams import Frame

frame = Frame.from_file("dump-320.lammpstrj")
r, g = frame.rdf_2d(output_dir="output/", cutoff=12.0, binwidth=0.05)
```

`rdf_2d` returns bin centres and `g(r)`. The engine also writes
`topoMonolayer/rdf.dat` under `output_dir`. `Frame.rdf(type_i, type_j)`
is the three-dimensional partial pair histogram that matches
`seams rdf`.

## Lua

`dseams.rdf` returns a partial three-dimensional pair histogram and
is not the in-plane calculation shown here:

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

1. The in-plane pair histogram in the 2020 d-SEAMS paper,
   doi:[10.1021/acs.jcim.0c00031](https://doi.org/10.1021/acs.jcim.0c00031).
