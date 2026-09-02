# Topology fingerprints

A topology key names the isomorphism class of an atom's rooted bonded
neighbourhood within a number of hops. The frame key is the sorted
histogram of those keys plus the primitive ring census. Relabelled
copies of the same bonded graph share a key. Vertices of different
LAMMPS types never match when the colour flag is on.

`seams fingerprint` builds one graph. `--graph seeded` falls back to
the cutoff list because the seeded assignment is two graphs.

## CLI

```bash
seams fingerprint mW_cubic.lammpstrj --type 1 --hops 2
seams fingerprint mW_cubic.lammpstrj --type 1 --emit-library Ic > ic.keys
seams fingerprint hydrate.lammpstrj --library ic.keys --hops 2
seams fingerprint mixed.lammpstrj --colour-types --hops 2
```

`--hops` is the number of bonds from the centre in each local key
(default 2). `--emit-library LABEL` prints library lines instead of
the summary. `--library FILE` names every atom whose key the library
lists. `--colour-types` colours vertices by LAMMPS type.

## Python

```python
from pydseams import Frame

frame = Frame.from_file("mW_cubic.lammpstrj")
print(frame.fingerprint(hops=2, colour_types=False))
library = frame.topology_library("Ic", hops=2)
print(frame.classify_topology(library, hops=2))
```

`Frame.fingerprint` returns a `FrameFingerprint` (`key`, `atomKeys`,
`classes`, `ringCensus`, `method`). `method` is `nauty` when the
engine links nauty, otherwise `wl`. `topology_library` adds this
frame's keys under a label. `classify_topology` names every analysed
atom; unmatched atoms carry an empty label.

## Lua

`dseams.fingerprint` takes neighbour-list rows from
`neighbourListByIndex`:

```lua
local dseams = require("dseams")
local cloud = dseams.read("mW_cubic.lammpstrj", {type = 1})
local nlist = dseams.neighbors(cloud, {cutoff = 3.5, type = 1})
local rows = dseams.core.neighbourListByIndex(cloud, nlist)
print(dseams.fingerprint(rows, {hops = 2}))
local lib = dseams.topology_library(rows, "Ic", {hops = 2})
print(dseams.classify_topology(rows, lib, {hops = 2}))
```

`o.colours` is an optional list of one integer class per row.

Books: [seams CLI](https://docs.dseams.info/reference/cli.html),
[pydseams](https://d-seams.github.io/PydSEAMSlib/howto/features.html),
[dseams](https://d-seams.github.io/yodaStruct/reference/lua.html).
