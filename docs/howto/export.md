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

`seams cages --per-atom` writes `cage`: 0 water, 1 hexagonal cage, 2 double-diamond cage, 3 both. The ice Ih cell is all 1. The ice Ic cell is all 2. On the first frame of the short nucleation trajectory the four codes are all present: 3816 water, 141 hexagonal, 98 double-diamond, and 41 molecules that sit in both cages.

`seams fingerprint --per-atom` writes `class`, the rank of the topology class by population, with 1 the largest. On the ice Ih cell there is one class, so every atom is 1. Pass `--library` and the column is `label`, the index of the library name. An atom the library does not name is 0. The keys those columns come from are in [Topology fingerprints](fingerprint.md).

`seams ions --per-atom` writes `state`: 0 liquid water, 1 ice water, 2 liquid ion, 3 front ion, 4 ice ion. The brine front has 8 liquid ions and 1 ice ion, and no front ion.

```bash
# example
set -euo pipefail
mkdir -p examples/output
seams cages examples/inputs/ice1h.lammpstrj --type 1 --cutoff 3.5 --per-atom examples/output/ih-cages.lammpstrj | tee /tmp/export-cages.txt
grep -q "hexagonal 128" /tmp/export-cages.txt
grep -q "ITEM: ATOMS id type x y z cage" examples/output/ih-cages.lammpstrj
awk 'f && $NF==1 {c++} /ITEM: ATOMS/{f=1} END{exit !(c==128)}' examples/output/ih-cages.lammpstrj
seams cages examples/inputs/ice_ic.lammpstrj --type 1 --cutoff 3.5 --per-atom examples/output/ic-cages.lammpstrj >/dev/null
awk 'f && $NF==2 {c++} /ITEM: ATOMS/{f=1} END{exit !(c==64)}' examples/output/ic-cages.lammpstrj
seams cages examples/inputs/nucleation_three.lammpstrj --type 1 --frame 1 --per-atom examples/output/nuc-cages.lammpstrj >/dev/null
awk 'f {n[$NF]++} /ITEM: ATOMS/{f=1} END{exit !(n[0]==3816 && n[1]==141 && n[2]==98 && n[3]==41)}' examples/output/nuc-cages.lammpstrj
seams fingerprint examples/inputs/ice1h.lammpstrj --type 1 --cutoff 3.5 --hops 2 --per-atom examples/output/ih-class.lammpstrj >/dev/null
grep -q "ITEM: ATOMS id type x y z class" examples/output/ih-class.lammpstrj
seams fingerprint examples/inputs/ice1h.lammpstrj --type 1 --cutoff 3.5 --hops 3 --emit-library Ih > /tmp/export-ih3.keys
seams fingerprint examples/inputs/ice_ic.lammpstrj --type 1 --cutoff 3.5 --hops 3 --library /tmp/export-ih3.keys --per-atom examples/output/ic-label.lammpstrj >/dev/null
grep -q "ITEM: ATOMS id type x y z label" examples/output/ic-label.lammpstrj
awk 'f && $NF==0 {c++} /ITEM: ATOMS/{f=1} END{exit !(c==64)}' examples/output/ic-label.lammpstrj
seams ions examples/inputs/nacl_front.lammpstrj --type 1 --ion-types 3,4 --ion-cutoff 3.5 --complete --per-atom examples/output/ions-state.lammpstrj | tee /tmp/export-ions.txt
grep -q "in-ice 1" /tmp/export-ions.txt
grep -q "liquid 8" /tmp/export-ions.txt
grep -q "ITEM: ATOMS id type x y z state" examples/output/ions-state.lammpstrj
awk 'f {n[$NF]++} /ITEM: ATOMS/{f=1} END{exit !(n[2]==8 && n[4]==1 && n[3]+0==0)}' examples/output/ions-state.lammpstrj
```
