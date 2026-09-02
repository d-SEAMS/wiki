# Wiki

MkDocs wiki for d-SEAMS, published at
[wiki.dseams.info](https://wiki.dseams.info).

- Product page: [dseams.info](https://dseams.info)
- Engine book: [docs.dseams.info](https://docs.dseams.info)
- Python book: [pydseams](https://d-seams.github.io/PydSEAMSlib/)
- Lua book: [yodaStruct](https://d-seams.github.io/yodaStruct/)
- Engine source: [d-SEAMS/seams-core](https://github.com/d-SEAMS/seams-core)

This tree keeps process notes, the 2020 Software Quality Management
course artifact (history), and the figshare pages rewritten for the
2.7 public API (`seams` / `pydseams` / `require("dseams")` /
`DSEAMS_CAGES`).

## Build

Pinned versions live in both `pyproject.toml` and `requirements.txt`.
The lock is `uv.lock`.

```bash
uv run --locked mkdocs build --strict
uvx --with-requirements requirements.txt mkdocs build --strict
uv run --locked python scripts/check-site-links.py site
lychee --config lychee.toml README.md docs
scripts/check-external-links.sh
```

## License

The software is MIT. This wiki declares MIT in `pyproject.toml`.
The original wiki document also carried GNU Free Documentation
License 1.3; that text remains under `docs/03_license.md` as history.
