# Ions against the cage assignment

Ions sit outside the hydrogen-bond network. The cage assignment runs
on the water. Each ion is then classed by the ice content of its
first water shell: ice when every neighbour carries a cage label,
liquid when none does, and front otherwise.

`seams ions` loads every LAMMPS type. `--type` still names the water.

## CLI

```bash
seams ions brine.lammpstrj --type 1 --ion-types 3,4 --ion-cutoff 3.5 --complete
```

`--ion-types` is required (`I,J` LAMMPS types). `--ion-cutoff` is the
first-shell radius and defaults to `--cutoff`. `--complete` is the
same ring completion as `seams cages --complete`.

## Python

```python
from pydseams import Frame

frame = Frame.from_file("brine.lammpstrj", all_atoms=True, atom_type=1)
env = frame.ion_environment((3, 4), ring_adjacent=True)
print(env.nIce, env.nFront, env.nLiquid)
```

`all_atoms=True` keeps every species in the cloud. `atom_type` is the
analysed water. `ion_types` are `c_type` codes (LAMMPS types, or
atomic numbers for frames built through ASE).

An ASE `Atoms` mix of water and salt keeps the listed species. The
first entry is the analysed water:

```python
import pydseams as ds

frame = ds.Frame.from_ase(atoms, select=("O", "Na", "Cl"), bonded="cutoff")
env = frame.ion_environment((11, 17))
```

Sodium and chlorine keep their atomic numbers as `c_type`.

## Lua

`PointCloud` does not expose per-atom types. Pass the 0-based ion
indices yourself, as `example_lua/library/topology.lua` does:

```lua
local dseams = require("dseams")
local cloud = dseams.read("brine.lammpstrj", {all = true})
local aff = dseams.cages(cloud, {type = 1, complete = true})
local ice = {}
for i = 1, cloud.nop do
  ice[i] = (aff.hc[i] or aff.ddc[i]) and true or false
end
print(dseams.ion_environment(cloud, ice, { 0 }, {type = 1, cutoff = 3.5}))
```

`dseams.read(..., {all = true})` keeps every LAMMPS type.
`ion_environment` takes the cloud, a 1-based ice-flag list of
length `cloud.nop`, and 0-based ion indices.

See also [kinetic features](features.md) for `pydseams.features.ion_environment`.
