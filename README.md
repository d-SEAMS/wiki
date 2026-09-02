# Wiki

MkDocs wiki for d-SEAMS, published at
[wiki.dseams.info](https://wiki.dseams.info).

- Product page: [dseams.info](https://dseams.info)
- Engine book: [docs.dseams.info](https://docs.dseams.info)
- Python book: [pydseams](https://d-seams.github.io/PydSEAMSlib/)
- Lua book: [yodaStruct](https://d-seams.github.io/yodaStruct/)
- Engine source: [d-SEAMS/seams-core](https://github.com/d-SEAMS/seams-core)

The wiki keeps process notes, the 2020 Software Quality Management
course artifact (history), and the 2.7.0 workflow examples (`seams` /
`pydseams` / `require("dseams")` / `DSEAMS_CAGES`).

Build the site from the pinned lock or from `requirements.txt`:

```bash
uv run --locked mkdocs build --strict
uvx --with-requirements requirements.txt mkdocs build --strict
```

## License

The software license is the Massachusetts Institute of Technology (MIT)
License. This wiki declares that license in `pyproject.toml`. The
original wiki document also carried the Free Software Foundation (GNU)
Free Documentation License 1.3; that text remains under
`docs/03_license.md` as history.
