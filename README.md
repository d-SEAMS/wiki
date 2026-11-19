# Wiki

MkDocs wiki for d-SEAMS, published at
[wiki.dseams.info](https://wiki.dseams.info).

- Product page: [dseams.info](https://dseams.info)
- Engine book: [docs.dseams.info](https://docs.dseams.info)
- Python book: [PydSEAMSlib](https://d-seams.github.io/PydSEAMSlib/)
- Julia, Rust, Fortran, and R chapters: [docs.dseams.info](https://docs.dseams.info)
- R book: [r.dseams.info](https://r.dseams.info/)
- Fortran book: [fortran.dseams.info](https://fortran.dseams.info/)
- Lua and Fennel book: [lua.dseams.info](https://lua.dseams.info/)
- PLUMED book: [plumed.dseams.info](https://plumed.dseams.info/)
- linkcell, a separate neighbour-search library: [linkcell.dseams.info](https://linkcell.dseams.info/)
- Engine source: [d-SEAMS/seams-core](https://github.com/d-SEAMS/seams-core)

The pages are tutorials, how-to guides, explanation, and reference for
analysing water and ice. Community notes stay under `docs/community`.

## Build

Pinned versions live in both `pyproject.toml` and `requirements.txt`.
The lock is `uv.lock`.

```bash
uv run --locked mkdocs build --strict
uvx --with-requirements requirements.txt mkdocs build --strict
uv run --locked python scripts/check-site-links.py site
lychee --config lychee.toml README.md docs
scripts/check-external-links.sh
uv run --locked python scripts/check-dois.py README.md docs
```

The worked examples are a separate environment. `requirements-examples.txt`
pins that environment. `SEAMS_HOME` is an extracted libseams 2.14.0 tree,
and `DSEAMS_JL` is a Dseams.jl checkout prepared with `dev/develop_jll.jl`.

```bash
python scripts/run-examples.py
```

## License

The software is MIT. This wiki declares MIT in `pyproject.toml`.
The original wiki document also carried GNU Free Documentation
License 1.3; that text remains under `docs/community/license.md`.
