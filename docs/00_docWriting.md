# Wiki Updates

Use the edit button on any page for small corrections, or clone
`d-SEAMS/wiki` when changing several pages or the site configuration.

## Local

Create an isolated Python environment and install the hashed dependency lock:

```bash
uv venv
. .venv/bin/activate
uv sync --locked
mkdocs serve
```

The same pins are in `requirements.txt` for a lock-free one-shot:

```bash
uvx --with-requirements requirements.txt mkdocs build --strict
```

Run the same checks as continuous integration before publishing a change:

```bash
uv run --locked mkdocs build --strict --site-dir site
uv run --locked python scripts/check-site-links.py site
lychee --config lychee.toml README.md docs
scripts/check-external-links.sh
```

The direct dependencies live in `pyproject.toml` and `requirements.txt`
with matching versions. Regenerate the universal lock after changing them:

```bash
uv lock --upgrade
```

### Resources

- Official [MkDocs documentation](https://www.mkdocs.org/user-guide/writing-your-docs/)
- [Material for MkDocs documentation](https://squidfunk.github.io/mkdocs-material/)
