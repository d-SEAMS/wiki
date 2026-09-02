# PLUMED action DSEAMS_CAGES

`DSEAMS_CAGES` is the d-SEAMS topological ice score as a PLUMED
colvar. It reports integer counts with no derivatives. Those counts
drive `PRINT`, `COMMITTOR` basins, and analysis. They do not bias.

The four-neighbour ice classifier (CHILL) plus variant, CHILL+, is
reported next to the cage score.

Build `libdseams_plumed.so` from
[dseams-plumed](https://github.com/HaoZeke/dseams-plumed). `LOAD`
takes that path.

## Keywords

- `ATOMS`: oxygen atoms of the water molecules (required)
- `CUTOFF`: neighbour cutoff in A for the CHILL+ graph (default 3.5)
- `CANDIDATE`: candidate shell in A for the four-nearest walk (default 5.5)
- `K`: neighbours per molecule in the bonded graph (default 4)
- `LENGTH_SCALE`: factor from the PLUMED length unit to A (default 10)
- `COMPLETE`: fill the last vertex of six-rings whose other vertices carry a label
- `IONS`: ions read against the water assignment; not part of the graph
- `ION_CUTOFF`: radius in A of an ion's first water shell (default 3.5)
- `HOPS`: bonds from the centre in each local topology key (default 3)
- `LIBRARY`: topology key library from `seams fingerprint --emit-library`

Omit `LIBRARY` or `IONS` when unused. A library built at a different
`HOPS` is an error.

## Ice score

```text
LOAD FILE=libdseams_plumed.so
ice: DSEAMS_CAGES ATOMS=1-4096 CUTOFF=3.5 COMPLETE
PRINT ARG=ice.nice,ice.nmax,ice.nic,ice.nih,ice.chillice,ice.chillmax STRIDE=100 FILE=ICE
COMMITTOR ARG=ice.nmax STRIDE=100 BASIN_LL1=0 BASIN_UL1=20 BASIN_LL2=800 BASIN_UL2=100000
```

## Brine

```text
LOAD FILE=libdseams_plumed.so
brine: DSEAMS_CAGES ATOMS=1-3000 IONS=3001-3060 ION_CUTOFF=3.5 COMPLETE
PRINT ARG=brine.nice,brine.nmax,brine.nionice,brine.nionfront,brine.nionliq STRIDE=500 FILE=BRINE
```

## Key library

```text
LOAD FILE=libdseams_plumed.so
hyd: DSEAMS_CAGES ATOMS=1-2944 LIBRARY=sI_sII.keys HOPS=3
PRINT ARG=hyd.nnamed,hyd.nclasses STRIDE=500 FILE=HYDRATE
```

`LENGTH_SCALE` is 10 for the PLUMED default (nm to A) and 1 after
`UNITS LENGTH=A`.
