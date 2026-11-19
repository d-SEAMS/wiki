# Read a trajectory

The cell is part of the configuration. A LAMMPS dump carries the box on every frame, and the ice Ih cell in that dump is entirely hexagonal. The same coordinates written as an XYZ, with no cell, are measured in a box that is only the span of the points. The neighbour list changes, and so does the census.

`examples/inputs/tiny_multi_cuh2.con` is a four-atom `.con` file. The Python reader loads it.

=== "Python"

    ```python
    # example
    from dseams.userframe import read
    import pydseams as ds

    crystal = read("examples/inputs/ice1h.lammpstrj", atom_type=1)
    bare = read("examples/inputs/ice1h.xyz", atom_type=1)
    assert crystal.chill_plus()["hexagonal"] == 128
    bare_labels = bare.chill_plus()
    assert bare_labels["hexagonal"] == 12
    assert bare_labels["interfacial"] == 4
    assert bare_labels["water"] == 112
    print("dump", crystal.n_atoms, "xyz", bare.n_atoms, bare_labels)

    con = ds.read("examples/inputs/tiny_multi_cuh2.con")
    assert con.n_atoms == 4
    print("con", con.n_atoms)
    ```

=== "CLI"

    ```bash
    # example
    set -euo pipefail
    seams chill-plus examples/inputs/ice1h.lammpstrj --type 1 --cutoff 3.5 | tee /tmp/read-dump.txt
    grep -q "hexagonal 128" /tmp/read-dump.txt
    seams chill-plus examples/inputs/ice1h.xyz --type 1 --cutoff 3.5 | tee /tmp/read-xyz.txt
    grep -q "hexagonal 12" /tmp/read-xyz.txt
    grep -q "interfacial 4" /tmp/read-xyz.txt
    grep -q "water 112" /tmp/read-xyz.txt
    ```

The dump and the XYZ hold the same 128 oxygens. Only the dump is a crystal under CHILL+.

Suffixes the readers accept include `.lammpstrj` and `.xyz`, and the Python reader also takes `.con`. GROMACS `.gro`, Protein Data Bank `.pdb`, and `.dcd` are further suffixes of the same idea: a file is useful here when it carries the cell the distances were computed in.

`--type` keeps one species. The ice dumps in these tutorials are type 1. `examples/inputs/exampleTraj.lammpstrj` stores oxygen as type 2, which is why [CHILL+ and q6](../tutorials/order-parameters.md) passes `--type 2`.
