# Triclinic cells

A hydrate cell is often triclinic. Distances, rings, and cages use the full cell, including the tilt. Dropping the tilt changes neighbour lists and the census.

`examples/inputs/genice_sH.lammpstrj` is one sH cell. The box is about 31.05 by 10.76 by 20.13 angstrom, with an xy tilt near -6.21 angstrom. The face census of that cell is the one in [Bulk ice and hydrate cages](../tutorials/bulk-ice.md): 12 dodecahedra, 8 medium cages, and 4 large cages.

=== "Python"

    ```python
    # example
    from dseams.userframe import read

    frame = read("examples/inputs/genice_sH.lammpstrj", atom_type=1)
    box = frame.box
    assert len(box) == 9
    assert abs(float(box[6]) - (-6.21061)) < 1e-3
    small = frame.cages_by_signature("512", edge="none")
    medium = frame.cages_by_signature("sh", edge="none")
    large = frame.cages_by_signature("51268", edge="none")
    assert (len(small), small.n_atoms) == (12, 136)
    assert (len(medium), medium.n_atoms) == (8, 112)
    assert (len(large), large.n_atoms) == (4, 120)
    print("xy", float(box[6]))
    print(len(small), len(medium), len(large))
    ```

=== "CLI"

    ```bash
    # example
    set -euo pipefail
    seams read examples/inputs/genice_sH.lammpstrj --type 1 | tee /tmp/sh-box.txt
    grep -q "xy -6.21061" /tmp/sh-box.txt
    seams cages examples/inputs/genice_sH.lammpstrj --type 1 --graph cutoff --signature 512+sh+51268 --cage-edge none | tee /tmp/sh-cages.txt
    grep -q "signature 5:12 cages 12 atoms 136" /tmp/sh-cages.txt
    grep -q "signature 4:3,5:6,6:3 cages 8 atoms 112" /tmp/sh-cages.txt
    grep -q "signature 5:12,6:8 cages 4 atoms 120" /tmp/sh-cages.txt
    ```

The nine box numbers are the origin, the three lengths, and the three tilts `xy`, `xz`, `yz`. An orthorhombic frame reports the three lengths only. The sH frame reports all nine, and index 6 is `xy`.

LAMMPS writes the tilt on the `ITEM: BOX BOUNDS` lines (`xy xz yz` when any tilt is nonzero). Keep that header. A coordinate-only file has no cell, which is the case the [reader guide](readers.md) shows with an XYZ of ice Ih.
