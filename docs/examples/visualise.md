# See the labels in OVITO or VMD

Counts tell you how much ice there is. Colouring each molecule by what
the engine decided shows where it is. Three routes, from no Python at
all to a live OVITO pipeline.

## CLI: a dump with one extra column

```bash
seams cages traj.lammpstrj --frame 1 --last 200 --per-atom cages.lammpstrj
seams fingerprint traj.lammpstrj --hops 3 --library ic.keys --per-atom labels.lammpstrj
seams ions brine.lammpstrj --ion-types 3,4 --per-atom ions.lammpstrj
```

`--per-atom FILE` appends one LAMMPS dump frame per analysed frame with
the columns `id type x y z` and one more: `cage` (0 water, 1 hexagonal
cage, 2 double-diamond cage, 3 both) for `cages`, `class` (rank of the
topology class by population, 1 the largest) or `label` (index into the
library labels the summary line prints) for `fingerprint`, `state` (0
liquid water, 1 ice water, 2 liquid ion, 3 front ion, 4 ice ion) for
`ions`. OVITO reads the extra column as a particle property; in VMD
load it with the LAMMPS dump plugin and colour by `user`.

## OVITO: a modifier function

```python
from functools import partial
from ovito.io import import_file
from pydseams.adapters import ice_states

pipeline = import_file("traj.lammpstrj")
pipeline.modifiers.append(partial(ice_states, oxygen_type=1, cutoff=3.5))
data = pipeline.compute(10)
print(data.particles["Ice state"][...])
```

`ice_states` adds the `Ice state` particle property (0 water, 1 cubic,
2 hexagonal, 3 mixed, -1 outside the oxygen type) from the seeded cage
assignment. Add a Color coding modifier on it and step through the
trajectory.

## MDAnalysis: an analysis class

```python
import MDAnalysis as mda
from pydseams.adapters import IceStates

u = mda.Universe("brine.gro", "brine.xtc")
an = IceStates(u.select_atoms("name OW"), ions=u.select_atoms("name NA CL")).run()
an.results.states       # frames x oxygens
an.results.ion_states   # frames x ions
```

`pip install pydseamslib[mdanalysis]` pulls MDAnalysis. Boxes must be
orthorhombic.

Book: [MDAnalysis, OVITO and notebooks](https://d-seams.github.io/PydSEAMSlib/howto/tools.html).
