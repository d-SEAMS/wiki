# Primitive rings

A ring in the hydrogen-bond network is a closed walk of molecules. Most closed walks are not useful. A primitive ring is one that cannot be written as two shorter rings sharing a path: the shortest-path criterion of Franzblau, Phys. Rev. B 44, 4925 (1991), doi [10.1103/PhysRevB.44.4925](https://doi.org/10.1103/PhysRevB.44.4925).

That restriction is what makes a ring a piece of structure. In ice Ih the primitive rings are hexagons, and the cell in [Bulk ice and hydrate cages](../tutorials/bulk-ice.md) holds 256 of them. In the square sheet of [Monolayer rings](../tutorials/monolayer.md) every primitive ring is a square, 64 of them, and they cover the sheet. A pentagon is the face of a hydrate cage. An oversized ring, past the first few neighbour shells, is usually a walk through liquid.

d-SEAMS searches these rings on a neighbour graph. The cutoff graph keeps every pair inside the shell of [Choose a cutoff](../howto/cutoff.md). The mutual graph keeps the four nearest neighbours that name each other. The seeded graph starts from that mutual list and is the one the cage score uses. `seams rings` prints the histogram. The largest size you ask for is `--max-ring`.

Rings are the faces. The next page is what gets built out of them: [Prisms and cages](cages.md).
