"""Fail when requirements.txt and pyproject.toml pin different versions."""

from __future__ import annotations

import sys
import tomllib
from pathlib import Path

root = Path(__file__).resolve().parent.parent
project = tomllib.loads((root / "pyproject.toml").read_text(encoding="utf-8"))
declared = {line.strip() for line in project["project"]["dependencies"]}
required = {
    line.strip()
    for line in (root / "requirements.txt").read_text(encoding="utf-8").splitlines()
    if line.strip() and not line.lstrip().startswith("#")
}
if declared != required:
    for pin in sorted(declared - required):
        print(f"pyproject.toml only: {pin}")
    for pin in sorted(required - declared):
        print(f"requirements.txt only: {pin}")
    sys.exit(1)
print("\n".join(sorted(declared)))
