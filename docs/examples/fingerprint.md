# Topology fingerprint

A fingerprint is the label-independent key of a bonded graph: one
rooted neighbourhood class per atom, the histogram of those classes,
the primitive ring census, and a frame key over all of it. Relabelled
copies of the same bonded graph share the key.

## CLI

```bash
seams fingerprint mW_cubic.lammpstrj --type 1 --hops 2
seams fingerprint mW_cubic.lammpstrj --type 1 --hops 2 --colour-types
seams fingerprint mW_cubic.lammpstrj --type 1 --hops 2 --emit-library Ic > ic.keys
seams fingerprint hydrate.lammpstrj --type 2 --hops 3 --library ic.keys
```

`--hops` is the number of bonds from the centre in each local key
(default 2). `--colour-types` colours vertices by LAMMPS type so
species never match across types. `--emit-library LABEL` prints the
frame's distinct keys as library lines under `LABEL`. `--library FILE`
names atoms of a frame by that library.

The bond graph follows `--graph`. `seeded` is two graphs, so the
fingerprint falls back to the cutoff list. Use `--graph knn` or
`--graph knn-union` for a k-nearest graph.

## Python

```python
from pydseams import Frame
from pydseams import yoda

frame = Frame.from_file("mW_cubic.lammpstrj", atom_type=1)
fp = frame.fingerprint(hops=2, colour_types=False)
print(fp.key, fp.method, fp.classes)

lib = frame.topology_library("Ic", hops=2)
print(yoda.writeLibrary(lib))

named = frame.classify_topology(lib, hops=2)
print(named.matched, named.counts)
```

`fingerprint` returns a `FrameFingerprint`: `key`, `atomKeys`,
`classes`, `ringCensus`, and `method` (`"nauty"` when the engine links
nauty, else `"wl"`). `topology_library` adds this frame's keys under a
label. `classify_topology` names every analysed atom; unmatched atoms
carry `""`.

## Lua

`dseams.fingerprint` takes neighbour-list rows by index.

```lua
local dseams = require("dseams")
local cloud = dseams.read("mW_cubic.lammpstrj", {type = 1})
local rows = dseams.core.neighbourListByIndex(
    cloud, dseams.neighbors(cloud, {cutoff = 3.5, type = 1}))
local fp = dseams.fingerprint(rows, {hops = 2})
local lib = dseams.topology_library(rows, "Ic", {hops = 2})
local named = dseams.classify_topology(rows, lib, {hops = 2})
print(fp.key, named.matched)
```

`o.colours` is an optional list of one integer class per row.

Book: [seams CLI](https://docs.dseams.info/reference/cli.html).
