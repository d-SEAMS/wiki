# PLUMED DSEAMS_CAGES

The PLUMED action `DSEAMS_CAGES` is the seeded cage score on a group
of oxygen atoms. Counts have no derivatives: they serve `PRINT`,
`COMMITTOR` basins, and analysis, not biasing.

Keywords: `ATOMS`, `CUTOFF` (default 3.5 Angstrom), `CANDIDATE`
(default 5.5), `K` (default 4), `LENGTH_SCALE` (default 10.0, PLUMED
length unit to Angstrom), `COMPLETE`, `IONS`, `ION_CUTOFF` (default
3.5), `HOPS` (default 3), `LIBRARY`.

```text
LOAD FILE=libdseams_plumed.so
ice: DSEAMS_CAGES ATOMS=1-4096 CUTOFF=3.5 COMPLETE
PRINT ARG=ice.nice,ice.nmax,ice.nic,ice.nih,ice.chillice,ice.chillmax STRIDE=100 FILE=ICE
COMMITTOR ARG=ice.nmax STRIDE=100 BASIN_LL1=0 BASIN_UL1=20 BASIN_LL2=800 BASIN_UL2=100000
brine: DSEAMS_CAGES ATOMS=1-3000 IONS=3001-3060 ION_CUTOFF=3.5 COMPLETE
PRINT ARG=brine.nice,brine.nmax,brine.nionice,brine.nionfront,brine.nionliq STRIDE=500 FILE=BRINE
hyd: DSEAMS_CAGES ATOMS=1-2944 LIBRARY=sI_sII.keys HOPS=3
PRINT ARG=hyd.nnamed,hyd.nclasses STRIDE=500 FILE=HYDRATE
```

`ATOMS` names the oxygen atoms. `IONS` are read against the water
assignment and are not part of the graph. `LIBRARY` is a topology key
library from `seams fingerprint --emit-library`; `HOPS` must match the
library. `COMPLETE` fills the last vertex of six-rings whose other
vertices carry a label.

Components include `nice`, `nmax`, `nclus`, `nic`, `nih`, `nmixed`,
`chillice`, `chillmax`, `chillinterfacial`, `sixrings`, `nionice`,
`nionfront`, `nionliq`, `nclasses`, and `nnamed`.

Source: [dseams-plumed](https://github.com/HaoZeke/dseams-plumed).
