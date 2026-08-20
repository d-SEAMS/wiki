# Ice nanotube prisms

Figshare:
[Quasi-1D Nanotube LAMMPS Trajectory](https://figshare.com/articles/Quasi-1D_Nanotube_LAMMPS_Trajectory/11448768)
(`dump-240-square.lammpstrj`, 750 TIP4P/2005 waters in a smooth (13,0)
tube at 240 K). Tetragonal prism blocks.

The `seams` CLI has no prism command. Use a front end.

## Python

```python
import pydseams as ds

frame = ds.read("dump-240-square.lammpstrj")
frame.find_prisms(output_dir="output/")
```

## Lua

`require("dseams")` does not expose the output-writing prism analysis as a
stable helper. The 1.x scripts under `example_lua/iceNanotube/` depend on
CLI-injected globals. Use `Frame.find_prisms` for the supported library
workflow; low-level Lua registrations are documented in the
[yodaStruct book](https://d-seams.github.io/yodaStruct/reference/lua-functions.html).

Howto: [confined ice](https://docs.dseams.info/howto/confined-ice.html).

## References

1. The confined-ice topological criterion in the 2020 d-SEAMS paper,
   doi:[10.1021/acs.jcim.0c00031](https://doi.org/10.1021/acs.jcim.0c00031).
