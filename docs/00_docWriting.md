# Wiki Updates

Use the edit button on any page for small corrections, or clone
`d-SEAMS/wiki` when changing more than one page or the site configuration.

## Local

Create an isolated Python environment and install the hashed dependency lock:

```bash
uv venv
. .venv/bin/activate
uv sync --locked
mkdocs serve
```

`requirements.txt` pins the same versions as `pyproject.toml`. Either
installer works:

```bash
uv run --locked mkdocs build --strict --site-dir site
uvx --with-requirements requirements.txt mkdocs build --strict --site-dir site
```

Run the same checks as continuous integration before publishing a change:

```bash
uv run --locked mkdocs build --strict --site-dir site
uv run --locked python scripts/check-site-links.py site
lychee --config lychee.toml docs README.md
```

The direct dependencies live in `pyproject.toml`. Regenerate the uv
lock after changing them, and keep `requirements.txt` on the same pins:

```bash
uv lock --upgrade
```

### Resources

- Official [MkDocs documentation](https://www.mkdocs.org/user-guide/writing-your-docs/)
- [Material for MkDocs documentation](https://squidfunk.github.io/mkdocs-material/)
