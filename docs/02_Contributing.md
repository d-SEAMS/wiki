# Contributing

!!! note
    Engine patches go to [seams-core](https://github.com/d-SEAMS/seams-core).
    Python is [PydSEAMSlib](https://github.com/d-SEAMS/PydSEAMSlib).
    Lua/Fennel is [yodaStruct](https://github.com/d-SEAMS/yodaStruct).
    This wiki is [d-SEAMS/wiki](https://github.com/d-SEAMS/wiki).
    Doc prose in a book: see **Writing Docs**.

We love pull requests from everyone. By participating in this project, you
agree to abide by the [code of conduct].

[code of conduct]: https://github.com/d-SEAMS/seams-core/blob/main/CODE_OF_CONDUCT.md

Run the affected repository's tests and documentation checks. Explain the
scientific or user-facing invariant that the change preserves.

Push to your fork and open a pull request against the repository that owns the
change.

For this wiki, run:

```bash
uv run --locked mkdocs build --strict --site-dir site
uv run --locked python scripts/check-site-links.py site
```

Include:

- a focused change with its test or executable documentation;
- the commands used to verify it;
- any changed file format, unit, tolerance, or public API contract.

## Commit Style

Use [Conventional Commits](https://www.conventionalcommits.org/), with a short
imperative subject. Examples:

```text
docs: clarify the Lua RDF contract
fix(io): reject empty selected frames
test(package): exercise the installed Python API
```

Add a body when the rationale, compatibility impact, or scientific contract
does not fit in the subject. Credit co-authors with Git trailers when
applicable.
