# seams CLI

The engine command is `seams`. A positional command and a trajectory
file are required. These names and flags are the Argum definitions in
`seams_cli.cpp` on seams-core 2.7.0.

The four-neighbour ice classifier (CHILL) and CHILL+ label bulk ice.

```text
seams read FILE
seams chill FILE
seams chill-plus FILE
seams cages FILE
seams fingerprint FILE
seams ions FILE
seams rdf FILE
seams cn FILE
seams hbonds FILE
seams pairs FILE
seams density-z FILE
seams domains FILE
```

`chill_plus` is an accepted alias of `chill-plus`.

## Commands

- `read`: print the loaded cloud (`nop N frame F box Lx Ly Lz`)
- `chill`: CHILL four-neighbour labels
- `chill-plus`: CHILL+ four-neighbour labels
- `cages`: ice score on six-membered rings
- `fingerprint`: topology keys of one bonded graph
- `ions`: first-shell class of every ion against the seeded cages
- `rdf`: partial site-site `g_IJ(r)`
- `cn`: site-site coordination number
- `hbonds`: geometric hydrogen-bond count
- `pairs`: mutual-nearest contact pairs (`--site` required)
- `density-z`: type-resolved density along one box direction
- `domains`: polar or apolar Stoddard component (`--site` required)

## Shared flags

- `--frame`, `-f` (default 1): first frame (1-based)
- `--last`: last frame, inclusive
- `--type`, `-t` (default 0): atom type; 0 guesses oxygen then type 1
- `--cutoff`, `-c` (default 3.5): neighbour cutoff in A
- `-k` (default 4): neighbours for knn / seeded cages
- `--graph` (default seeded): `cutoff`, `knn`, `knn-union`, or `seeded`
- `--complete` (off): ring completion for `cages` and `ions`
- `--format` (default text): `text` or `json`

`seams ions` and `seams pairs` load every LAMMPS type. `seams rdf`
and `seams cn` do the same when `--types I,J` names two species.

## Cages, fingerprints, ions

```bash
seams cages dump.lammpstrj --graph seeded --complete
seams fingerprint dump.lammpstrj --hops 2 --emit-library Ic
seams fingerprint dump.lammpstrj --library ic.keys --hops 2
seams fingerprint dump.lammpstrj --colour-types
seams ions dump.lammpstrj --ion-types 3,4 --ion-cutoff 3.5 --complete
```

`--hops` (default 2), `--library FILE`, `--emit-library LABEL`, and
`--colour-types` apply to `fingerprint`. `--ion-types` is required
for `ions`. `--ion-cutoff` defaults to `--cutoff`.

## Site-site and hydrogen bonds

```bash
seams rdf dump.lammpstrj --types 1,2 --cutoff 10 --bins 100
seams cn dump.lammpstrj --types 1,2 --cutoff 4.5
seams cn dump.lammpstrj --ions --site '1=cationHead,2=anion' --cutoff 6.0
seams pairs dump.lammpstrj --site '1=cationHead,2=anion'
seams hbonds dump.lammpstrj --type 2 --htype 1
seams density-z dump.lammpstrj --axis z
seams domains dump.lammpstrj --site '1=cationHead,2=anion' --subset polar
```

`cn --ions` is cage degree on `ionCloud` and needs `--site`. That
path is not `seams ions`.

Book: [seams CLI](https://docs.dseams.info/reference/cli.html).
