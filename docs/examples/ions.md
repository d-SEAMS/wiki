# Ions against the cage assignment

Ions sit outside the hydrogen-bond network. The cage assignment runs
on the water. Each ion is then classed by its first water shell:
ice when every neighbour in the shell is ice, liquid when none of it
is, and front otherwise.

## CLI

`seams ions` needs `--ion-types`. `--ion-cutoff` is the first-shell
radius (default `--cutoff`). `--complete` is the same ring completion
as `seams cages`.

```bash
seams ions brine.lammpstrj --type 1 --ion-types 3,4 --ion-cutoff 3.5 --complete
```

Stdout is `nop N ice I ions M in-ice A front B liquid C shell S shell-ice F`.

This is not `seams cn --ions`, which is cage degree on `ionCloud` and
needs `--site`.

## Python

Build the frame with every species in the cloud. `atom_type` still
names the water.

```python
from pydseams import Frame

frame = Frame.from_file("brine.lammpstrj", atom_type=1, all_atoms=True)
env = frame.ion_environment((3, 4), ring_adjacent=True, cutoff=3.5)
print(env.nIce, env.nFront, env.nLiquid)
```

ASE mixed water-salt selections keep ions in the cloud and store
atomic numbers as `c_type`:

```python
from pydseams import Frame

frame = Frame.from_ase(atoms, select=("O", "Na", "Cl"), bonded="cutoff")
print(frame.ion_environment((11, 17)))
```

`pydseams.features.ion_environment` takes per-molecule states from
`IceFeaturizer` instead of calling `seeded_affiliation` itself.

```python
from pydseams import Trajectory
from pydseams.features import ION_ICE, IceFeaturizer, ion_environment

traj = Trajectory("brine.lammpstrj", frame=1, atom_type=1, all_atoms=True)
feat = IceFeaturizer(traj, ion_types=(3, 4))
x, states = feat.frame_features()
ions, shell, fraction, ion_states = ion_environment(traj, states, (3, 4))
trapped = ions[ion_states == ION_ICE]
```

## Lua

```lua
local dseams = require("dseams")
local cloud = dseams.read("brine.lammpstrj", {all = true})
local aff = dseams.cages(cloud, {type = 1, complete = true})
local ice = {}
for i = 1, cloud.nop do
  ice[i] = (aff.hc[i] or aff.ddc[i]) and true or false
end
local env = dseams.ion_environment(cloud, ice, {0}, {type = 1, cutoff = 3.5})
print(env.nIce, env.nFront, env.nLiquid)
```

`ion_environment` takes the cloud, a per-atom ice flag list, and a
list of ion indices (0-based). `o.type` is the water type (default 1).
`o.cutoff` is the first-shell radius (default 3.5).

Book: [features how-to](https://d-seams.github.io/PydSEAMSlib/howto/features.html).
