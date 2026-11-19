# Two ways to name ice

CHILL+ and the cage score look at the same oxygens and answer different questions.

CHILL+ (Nguyen and Molinero, J. Phys. Chem. B 2015, doi [10.1021/jp510289t](https://doi.org/10.1021/jp510289t)) looks at the staggered and eclipsed bonds among the four nearest neighbours. The published rule used here labels a molecule cubic, hexagonal, water, interfacial, clathrate, or interfacial clathrate. It is a local label. It does not ask whether those neighbours close a polyhedron.

The topological criterion asks that question. Membership in a hexagonal cage or a double-diamond cage, built from [primitive rings](rings.md), is the ice label. A molecule in neither is water, for this criterion. Hydrate identity is a face census, not a CHILL+ label. The comparison on one crystal and one mixed frame is [CHILL+ and q6](../tutorials/order-parameters.md): ice Ih is hexagonal by both, and the mixed frame is mostly water by CHILL+ with a q6 distribution below the crystal.

q6 is a third number, not a third structure. The Steinhardt parameter measures how directional the neighbour shell is. The Lechner-Dellago average q6-bar (J. Chem. Phys. 129, 114707, 2008, doi [10.1063/1.2977970](https://doi.org/10.1063/1.2977970)) mixes a molecule with its neighbours. A growing nucleus moves the largest cage cluster long before it moves the mean q6-bar of a large liquid cell. That is why [Nucleation](../tutorials/nucleation.md) plots the cluster.

The codes written by `--per-atom` follow the CHILL+ order: 0 cubic, 1 hexagonal, 2 water, 3 interfacial, 4 clathrate, 5 interfacial clathrate. How to load that column is [Export labels](../howto/export.md).
