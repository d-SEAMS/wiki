# seams CLI

The engine command is `seams`. A positional command and a trajectory
file are required. `--format text|json` applies to every command.
JSON emits one object per output frame with schema `dseams.cli/v1`.

```bash
seams --help
seams --version
seams --features
```

## Commands

```bash
seams read FILE
seams chill FILE
seams chill-plus FILE [--rule chill+|ovito-chill+ --layers --tum-layers]
seams ovito-chill+ FILE
seams cages FILE [--graph seeded --complete --per-atom OUT]
seams cages FILE --signature SPEC [--guest-types T,U --guest-radius R --inside --incomplete --shape]
seams symmetry FILE
seams rings FILE [--max-ring N]
seams prisms FILE
seams cluster FILE
seams fingerprint FILE [--hops N --library FILE[,FILE...] --emit-library LABEL --color-types --by-atom --per-atom OUT]
seams ions FILE --ion-types I,J [--ion-cutoff ANGSTROM --per-atom OUT]
seams f4 FILE [--htype I]
seams steinhardt FILE [--l LIST]
seams rdf FILE [--pair-types I,J --cutoff ANGSTROM --bins N]
seams cn FILE [--pair-types I,J --cutoff ANGSTROM]
seams hbonds FILE [--type I --htype I --hdist ANGSTROM --hangle DEG --donors]
seams pairs FILE --site SPEC
seams density-z FILE [--type I --axis XYZ --bins N]
seams domains FILE --site SPEC [--subset polar|apolar]
```

`chill_plus` is an accepted alias of `chill-plus`, and `ovito-chill+`
is `chill-plus --rule ovito-chill+`. Ice scores (`chill`,
`chill-plus`, `cages`, `ions`) refuse every `--family` except
`waterIce`. `--types` and `--colour-types` are the 2.13 spellings of
`--pair-types` and `--color-types`; 2.14.0 still accepts them and
`--types` prints a deprecation warning. `symmetry` reports the IRA,
SOFI and spglib backends only when `seams --features` lists them.

## Worked flags

```bash
seams read input/traj/exampleTraj.lammpstrj
seams chill-plus input/traj/exampleTraj.lammpstrj --cutoff 3.5 --type 2
seams cages input/traj/mW_cubic.lammpstrj --type 1 --graph seeded --complete
seams fingerprint mW_cubic.lammpstrj --type 1 --hops 2 --emit-library Ic
seams ions brine.lammpstrj --type 1 --ion-types 3,4 --ion-cutoff 3.5
seams rdf dump.lammpstrj --pair-types 1,2 --cutoff 10 --bins 100
seams cn dump.lammpstrj --pair-types 1,2 --cutoff 4.5
seams cn dump.lammpstrj --ions --site '1=cationHead,2=anion' --cutoff 6.0
seams hbonds dump.lammpstrj --type 2 --htype 1
seams pairs dump.lammpstrj --site '1=cationHead,2=anion'
seams density-z dump.lammpstrj --type 0 --axis z
seams domains dump.lammpstrj --site '1=cationHead,2=anion' --subset polar
```

`cn --ions` is cage degree on `ionCloud` and needs `--site`. That is
not `seams ions`. `pairs` is the mutual-nearest contact-pair count.
`domains` is the largest polar or apolar Stoddard component.

`--type 0` on `read` / `chill` / `cages` guesses oxygen (type 2, then
type 1). `density-z` treats `0` as every atom.

Book: [seams CLI](https://docs.dseams.info/reference/cli.html).
