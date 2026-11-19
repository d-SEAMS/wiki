# Prisms and cages

A prism is two primitive rings of the same size, stacked on a common axis, with bonds between matching vertices. It is the repeated block of a quasi-one-dimensional ice. Squares give a tetragonal prism, the block inside a square ice nanotube. The eight stacked squares in [Ice nanotubes](../tutorials/nanotubes.md) contain five perfect prisms of size 4 and none of any other size. An imperfect prism is the same stack with a missing or extra bond. That file has none.

A cage is a closed polyhedron of primitive rings.

- A double-diamond cage (DDC) is the unit of ice Ic. A molecule that sits in one is cubic ice.
- A hexagonal cage (HC) is the unit of ice Ih. A molecule that sits in one is hexagonal ice.
- A hydrate cage is named by its faces. `512` is twelve pentagons, the dodecahedron common to sI, sII, and sH. `51262` is the larger sI cage. `51264` is the larger sII cage. `sh` and `51268` are the medium and large sH cages.

The seeded assignment used in the tutorials asks, for each molecule, whether it belongs to an HC, a DDC, both, or neither. On the 128-oxygen ice Ih cell the answer is HC for every molecule. On the 64-oxygen ice Ic cell it is DDC for every molecule. The hydrate cells are not ice Ih or ice Ic. Their census is the face list, which [Bulk ice and hydrate cages](../tutorials/bulk-ice.md) prints in full for one cell of each phase.

A molecule can sit in a cage and still be a small cluster. The largest connected set of cage molecules is the nucleus tracked in [Nucleation](../tutorials/nucleation.md). The largest connected set of every atom is a different number: on that file it is almost the whole box, because the liquid is one network.
