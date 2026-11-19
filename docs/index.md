# Analyse water and ice with d-SEAMS

d-SEAMS reads a molecular-dynamics frame and names the ice in it. One engine does the work. You can call it from Python, Julia, Rust, or the `seams` command, and the same frame gives the same census.

The product page is [dseams.info](https://dseams.info). The engine book is [docs.dseams.info](https://docs.dseams.info). Language books:

- [Python](https://docs.dseams.info/stable/python.html) and the [Frame book](https://d-seams.github.io/PydSEAMSlib/)
- [Julia](https://docs.dseams.info/stable/julia.html)
- [Rust](https://docs.dseams.info/stable/rust.html)
- [R](https://r.dseams.info/)
- [Fortran](https://fortran.dseams.info/)
- [Lua and Fennel](https://lua.dseams.info/)
- [PLUMED](https://plumed.dseams.info/)

[linkcell](https://linkcell.dseams.info/) is a separate library for periodic neighbour search. d-SEAMS builds cutoff lists and mutual k-nearest lists of that kind. It is not a language binding.

## Start here

Each tutorial starts from a small file under `examples/inputs` and ends with a figure drawn from the run.

1. [Bulk ice and hydrate cages](tutorials/bulk-ice.md): ice Ih, ice Ic, and the sI, sII, and sH cages.
2. [Ice nanotubes](tutorials/nanotubes.md): tetragonal prism blocks.
3. [Monolayer rings](tutorials/monolayer.md): a square sheet.
4. [CHILL+ and q6](tutorials/order-parameters.md): a local label and a bond-order number on the same oxygens.
5. [Ice/water interface](tutorials/interface.md): the basal stack and the front.
6. [Nucleation](tutorials/nucleation.md): the largest ice cluster over three frames.
7. [Radial distributions](tutorials/rdf.md): g(r) and the in-plane histogram.
8. [Ions](tutorials/ions.md): a brine front.
9. [On the fly with PLUMED](tutorials/plumed.md): the `DSEAMS_CAGES` counts a run can print and commit on.

The command reference for `seams` is the [CLI page](https://docs.dseams.info/reference/cli.html).

## Cite

Goswami, Goswami, and Singh, J. Chem. Inf. Model. 2020, doi [10.1021/acs.jcim.0c00031](https://doi.org/10.1021/acs.jcim.0c00031). The citation page also lists the coming d-SEAMS 2.0 paper. See [Publications](reference/publications.md).
