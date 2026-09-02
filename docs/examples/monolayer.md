# Monolayer square ice

Figshare:
[Monolayer LAMMPS Trajectory](https://figshare.com/articles/Monolayer_LAMMPS_Trajectory/11448741)
(`dump-6-320-310.lammpstrj`, fMSI on cooling 320 K to 310 K).
Four-membered primitive rings.

The `seams` CLI has no monolayer command. `Frame.monolayer_rings` writes
`polygonRingAnalysis` output and reads coverage back.

## Python

```python
from pydseams import Frame

frame = Frame.from_file("dump-6-320-310.lammpstrj")
print(frame.monolayer_rings(output_dir="output/", sheet_area=1.0))
```

Pass the sheet area for the system you downloaded. The engine does not
guess it. `max_depth` defaults to 4.

## Lua

`dseams.core.ringAnalysis` is a compiled registration, not a
`require("dseams")` helper. The 1.x scripts under
`example_lua/monolayer/` depend on CLI-injected globals. Use
`Frame.monolayer_rings` for the supported library workflow.

Howto: [confined ice](https://docs.dseams.info/howto/confined-ice.html).

## References

1. The confined-ice topological criterion in the 2020 d-SEAMS paper,
   doi:[10.1021/acs.jcim.0c00031](https://doi.org/10.1021/acs.jcim.0c00031).
