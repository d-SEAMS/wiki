# Export labels

A per-atom label file is what a viewer colours. `seams chill-plus --per-atom FILE` writes a LAMMPS dump whose atom table carries a `label` column, and prints the histogram on standard output. The codes are the CHILL+ order: 0 cubic, 1 hexagonal, 2 water, 3 interfacial, 4 clathrate, 5 interfacial clathrate.

In OVITO, colour the particles by that column. In VMD, the column is a user field on the dump. The interface frame is a useful first file because the slab and the liquid are both in it.

```bash
# example
set -euo pipefail
mkdir -p examples/output
seams chill-plus examples/inputs/interface_f0.lammpstrj --type 1 --cutoff 3.5 --per-atom examples/output/interface-labels.lammpstrj | tee /tmp/export.txt
grep -q "hexagonal 352" /tmp/export.txt
grep -q "label" examples/output/interface-labels.lammpstrj
```

The printed histogram reports 352 hexagonal molecules. The dump header names `label`. The coloured render of this frame is in the [gallery](../reference/gallery.md). The meaning of each label is in [Two ways to name ice](../explanation/criteria.md).
