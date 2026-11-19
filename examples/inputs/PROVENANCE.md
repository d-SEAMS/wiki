# Inputs

These files are the starting points for the tutorials.

Copied from seams-core tag `v2.14.0` (`input/traj` unless noted), MIT:

- `ice1h.lammpstrj`, with `ice1h.source.txt` (GenIce 2x2x2 ice Ih, 128 oxygens)
- `genice_sI.lammpstrj`, `genice_sII.lammpstrj`, `genice_sH.lammpstrj`
- `interface_f0.lammpstrj` (one basal-interface frame, 864 oxygens)
- `exampleTraj.lammpstrj` (mixed TIP4P frame, 250 oxygens of type 2)
- `nacl_front.lammpstrj`
- `nucleation_three.lammpstrj` (three frames, 4096 sites)
- `tiny_multi_cuh2.con` from `input/eon`

Written by `examples/make_lattices.py`:

- `ice_ic.lammpstrj`: 2x2x2 diamond lattice, a = 6.358 angstrom, 64 oxygens
- `nanotube.lammpstrj`: eight stacked squares, side 2.75 angstrom, step 2.80 angstrom
- `monolayer.lammpstrj`: 8x8 square lattice, spacing 2.75 angstrom, corrugation 0.15 angstrom
- `ice1h.xyz`: the ice Ih coordinates with no cell
