# Wiki Updates

Use the edit button on any page for small corrections, or clone
`d-SEAMS/wiki` when changing several pages or the site configuration.

## Local

Create an isolated Python environment and install the hashed dependency lock:

```bash
uv venv
. .venv/bin/activate
uv pip sync --require-hashes requirements.txt
mkdocs serve
```

Run the same checks as continuous integration before publishing a change:

```bash
mkdocs build --strict --site-dir site
python scripts/check-site-links.py site
```

The direct dependencies live in `pyproject.toml`. Regenerate the universal
lock after changing them:

```bash
uv pip compile pyproject.toml --universal --generate-hashes --upgrade -o requirements.txt
```

### Resources

- Official [MkDocs documentation](https://www.mkdocs.org/user-guide/writing-your-docs/)
- [Material for MkDocs documentation](https://squidfunk.github.io/mkdocs-material/)
