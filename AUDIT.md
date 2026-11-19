# Audit of wiki.dseams.info at e8b4867

Checked against the seams-core 2.14.0 release binary (`seams --version` prints `seams 2.14.0`), the public CLI reference at https://docs.dseams.info/reference/cli.html, the language books that resolve, and the pinned packages `pydseamslib==2.14.0`, crates.io `dseams==2.14.0`, and Dseams.jl at `193ac43` (project version 2.14.0, loaded against `libseams_lang` from that same release).

`py.dseams.info`, `jl.dseams.info`, and `rs.dseams.info` do not resolve. The books that do resolve are https://docs.dseams.info (including the stable Python, Julia, Rust, Fortran, Lua, and R chapters), https://r.dseams.info, https://fortran.dseams.info, https://lua.dseams.info, https://plumed.dseams.info, and https://linkcell.dseams.info. The older GitHub Pages books https://d-seams.github.io/PydSEAMSlib/ and https://d-seams.github.io/yodaStruct/ still answer.

## What the site is

The published nav is a home page, eleven example notes, two Lua link pages, and a process section that still leads with the 2020 Software Quality Management course (the SQM plan and its style guide). The home page describes the site as process notes plus those examples. A reader who wants to analyse a trajectory is sent to command lists and to other books.

The logo file `docs/images/logo.png` is the d-SEAMS mark. The theme is generic Material blue-grey with Rubik, which is not the paper, cobalt, and abyss palette of https://dseams.info.

## Stale or wrong

- `docs/examples/iceNanotube.md` says the `seams` CLI has no prism command. The 2.14.0 binary and the CLI reference both have `seams prisms` (perfect and imperfect prisms of size 3 to 6). On the mixed TIP4P dump shipped with seams-core the command reports 51 perfect tetragonal prisms.
- The same page, and `docs/examples/monolayer.md`, tell the reader to use only `Frame.find_prisms` and `Frame.monolayer_rings`, and they point at figshare trajectories the wiki does not ship. There is no figure, and nothing in CI runs the snippets.
- `docs/examples/rdf2d.md` is right that `seams rdf` is the three-dimensional partial RDF. It does not show an in-plane result, and the in-plane call is not executed.
- The Lua pages (`docs/lua/functions.md`, `docs/lua/references.md`) are four links. They are not a worked analysis. The current `require("dseams")` helpers cover reading, CHILL+, seeded cages, signatures, fingerprints, ions, RDF, hydrogen bonds, density, pairs, and domains. They are not what a reader can learn from this wiki.
- The home page and the SQM pages still teach the site as a 2020 process archive. The SQM plan says to keep it as history, and the nav still presents it beside contributing.
- Several examples describe the 1.x `yodaStruct -c` driver as gone. That part matches the 2.14 books. The snippets around it were never run here, so the pages could not catch the prism mistake above.
- `docs/examples/features.md` and `docs/examples/visualise.md` depend on optional Python extras (deeptime, PyEMMA, OVITO, MDAnalysis) and on trajectories that are not in the tree. PyEMMA is described as unmaintained. None of that is a complete analysis with a figure.
- The only raster under `docs/images/` besides the logo and favicon is `cloc-2020-01-20_15-56.png`, a 2020 line-count screenshot. There is no structure gallery.
- linkcell is absent. It is an independent periodic neighbour library (https://linkcell.dseams.info), not a d-SEAMS language binding. The 2.14.0 CLI reports its linkcell pair backend as compiled out. The wiki never separates the library from the bindings.
- The citation block is only the 2020 JCIM paper. The d-SEAMS 2.0 paper is not named.
- Cross-links point at GitHub repositories and the older GitHub Pages books. They do not point at the books that now resolve under `dseams.info`, and they point at `py` / `jl` / `rs` hosts that do not resolve only by omission: those hostnames are simply not used. The product page https://dseams.info is linked.

## Missing for a scientist learning the 2.14 analyses

The command inventory on the home page and in `docs/examples/cli.md` does match the 2.14.0 help string (`read`, `chill`, `chill-plus`, `ovito-chill+`, `cages`, `symmetry`, `rings`, `prisms`, `cluster`, `fingerprint`, `ions`, `f4`, `steinhardt`, `rdf`, `cn`, `hbonds`, `pairs`, `density-z`, `domains`), including `--jobs`, `--cage-edge`, `--layers`, `--water-types`, and `--per-atom`. That inventory is not a path through a dataset.

There is no Diataxis split. In particular there is no worked path for:

- bulk ice Ih and ice Ic, and the sI, sII, and sH cage census, shown in more than one language
- ice-nanotube prisms on a small public input
- a quasi-2D sheet and its ring census
- CHILL+ next to q6 on the same frame
- an ice/water interface and the basal stack
- the largest ice cluster along a short trajectory
- a three-dimensional RDF and an in-plane RDF drawn from the run
- ions against the cage assignment, with the counts the CLI prints
- the PLUMED `DSEAMS_CAGES` action as something you run, rather than a keyword list
- choosing a cutoff, a triclinic cell, LAMMPS / XYZ / CON readers, frame threading, or an OVITO/VMD column
- how the reproduction package at https://github.com/d-SEAMS/dseams2_repro relates to the paper figures
- what a primitive ring is, what an HC or DDC cage is, how that criterion differs from CHILL+ and from q6, and how those ideas sit next to other ice tools
- a glossary, a gallery of real renders, and a citation page that includes the coming 2.0 paper

Nothing in `.github/workflows/docs.yml` executes a scientific sample. The workflow builds the site, checks pins, checks internal links, runs lychee, and checks DOI handles. Those checks should stay. They do not know whether a snippet still calls the engine.

## What already matches 2.14

On frames that were actually run while writing this audit, the 2.14.0 CLI, `pydseamslib` 2.14.0, `dseams` 2.14.0 (Rust, linked to the release library), and Dseams.jl agree:

- `input/traj/ice1h.lammpstrj` (128 oxygens): CHILL+ hexagonal 128, seeded cages hexagonal 128, 256 primitive six-rings, mean q6 0.625855, mean q6-bar 0.562449
- `input/traj/exampleTraj.lammpstrj` type 2: CHILL+ interClathrate 9 and water 241
- `input/traj/genice_sI.lammpstrj`: signature `512` is 2 cages and 40 atoms
- `input/traj/genice_sII.lammpstrj`: `512` is 16 cages and 136 atoms, `51264` is 8 cages and 128 atoms
- `input/traj/genice_sH.lammpstrj` is triclinic (`xy` about -6.21) and the signature census is 12, 8, and 4 cages for `512`, `sh`, and `51268`
- `input/traj/interface_f0.lammpstrj`: hexagonal 352, water 434, interfacial 49, interClathrate 25, clathrate 3, cubic 1, stack `HHHHHHHH....C.`
- `input/traj/nacl_front.lammpstrj`: 9 ions, 1 in ice, 0 on the front, 8 in liquid

The community pages (contributing, code of conduct, license) are still the right pages to keep. The GFDL text in the license page is marked as the historical documentation license. The contributing guide already points at the live repositories.
