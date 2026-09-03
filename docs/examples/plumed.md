# PLUMED DSEAMS_CAGES

The PLUMED action `DSEAMS_CAGES` is the seeded cage score on a group
of oxygen atoms. Counts have no derivatives: they serve `PRINT`,
`COMMITTOR` basins, and analysis, not biasing.

Keywords: `ATOMS`, `CUTOFF` (default 3.5 Angstrom), `CANDIDATE`
(default 5.5), `K` (default 4), `LENGTH_SCALE` (default 10.0, PLUMED
length unit to Angstrom), `COMPLETE`, `IONS`, `ION_CUTOFF` (default
3.5), `HOPS` (default 3), `LIBRARY`, `SIGNATURE`, `GUESTS`,
`GUEST_RADIUS` (default 4.0).

```text
LOAD FILE=libdseams_plumed.so
ice: DSEAMS_CAGES ATOMS=1-4096 CUTOFF=3.5 COMPLETE
PRINT ARG=ice.nice,ice.nmax,ice.nic,ice.nih,ice.chillice,ice.chillmax STRIDE=100 FILE=ICE
COMMITTOR ARG=ice.nmax STRIDE=100 BASIN_LL1=0 BASIN_UL1=20 BASIN_LL2=800 BASIN_UL2=100000
brine: DSEAMS_CAGES ATOMS=1-3000 IONS=3001-3060 ION_CUTOFF=3.5 COMPLETE
PRINT ARG=brine.nice,brine.nmax,brine.nionice,brine.nionfront,brine.nionliq STRIDE=500 FILE=BRINE
hyd: DSEAMS_CAGES ATOMS=1-2944 LIBRARY=sI_sII.keys,sI_sII_h2.keys HOPS=3
PRINT ARG=hyd.nnamed,hyd.nclasses STRIDE=500 FILE=HYDRATE
fill: DSEAMS_CAGES ATOMS=1-2944 SIGNATURE=512 GUESTS=2945-3200 GUEST_RADIUS=4.0
PRINT ARG=fill.ncages,fill.noccupied,fill.nmultiple,fill.nfreeguest STRIDE=500 FILE=FILL
```

That `DSEAMS_CAGES` block names oxygen with `ATOMS`. `IONS` stay off
the graph and are read against the water assignment. `LIBRARY` is one
topology key library from `seams fingerprint --emit-library`, or two
or more files, comma separated, built at different hop counts; each
molecule takes the deepest library that names its key. The deepest
file must match `HOPS`. `COMPLETE` fills the last vertex of six-rings
whose other vertices carry a label. `SIGNATURE` names a ring-size
census (`4:6,6:8`) or a table entry (`sodalite`, `alpha`, `512`,
`51262`, `hc`, `ddc`) and `ncages` counts the closed polyhedra that
match it on the union graph. `GUESTS` lists one atom per guest
molecule (methane carbon, THF oxygen, an ion); each guest goes to the
nearest cage centre within `GUEST_RADIUS`, and `noccupied`,
`nmultiple` and `nfreeguest` are the filled-cage counts a hydrate
nucleation run biases and commits on.

Components include `nice`, `nmax`, `nclus`, `nic`, `nih`, `nmixed`,
`chillice`, `chillmax`, `chillinterfacial`, `sixrings`, `nionice`,
`nionfront`, `nionliq`, `nclasses`, and `nnamed`.

Source: [dseams-plumed](https://github.com/d-SEAMS/dseams-plumed).
