# Glossary

**Basal interface.** A slab of ice against a slab of liquid, stacked along one axis. The frame in [Ice/water interface](../tutorials/interface.md).

**Cage.** A closed polyhedron of [primitive rings](../explanation/rings.md). See [Prisms and cages](../explanation/cages.md).

**CHILL+.** Local ice label from the staggered and eclipsed bonds of the four nearest neighbours. Cubic, hexagonal, water, interfacial, clathrate, interfacial clathrate. See [Two ways to name ice](../explanation/criteria.md).

**Cutoff graph.** Pairs inside a distance. The distance is [Choose a cutoff](../howto/cutoff.md).

**DDC.** Double-diamond cage, the unit of ice Ic.

**Fingerprint.** The label-independent key of a bonded graph: one rooted neighbourhood class per atom, the histogram of those classes, and the primitive-ring census. See [Topology fingerprints](../howto/fingerprint.md).

**HC.** Hexagonal cage, the unit of ice Ih.

**Ice Ic.** Cubic ice. Every molecule of the 64-oxygen cell is in a DDC.

**Ice Ih.** Hexagonal ice. Every molecule of the 128-oxygen cell is in an HC.

**Interfacial.** CHILL+ label for a molecule between crystal and liquid.

**Interfacial clathrate.** CHILL+ label for a molecule whose neighbour shell looks like the edge of a clathrate.

**Mutual graph.** The four nearest neighbours, kept when the pair names each other.

**nmax.** The largest connected cluster of molecules that sit in a cage. The coordinate in [Nucleation](../tutorials/nucleation.md) and the `COMMITTOR` argument in [On the fly with PLUMED](../tutorials/plumed.md).

**Primitive ring.** A ring that is not the sum of two shorter rings. Franzblau's shortest-path criterion.

**Prism.** Two primitive rings of one size, stacked, with bonds between them. The block of an ice nanotube.

**q6.** Steinhardt bond-order parameter of degree 6. q6-bar is the Lechner-Dellago neighbour average.

**sI, sII, sH.** The three common empty hydrate lattices. Their face censuses are in [Bulk ice and hydrate cages](../tutorials/bulk-ice.md).

**Seeded graph.** The mutual list, used as the neighbour graph of the cage score.

**Signature.** A face census. `512` is twelve pentagons. `51262` is twelve pentagons and two hexagons.

**Sheet.** A quasi-two-dimensional network. Coverage is the fraction of the given area that the rings tile. See [Monolayer rings](../tutorials/monolayer.md).
