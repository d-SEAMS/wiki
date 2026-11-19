"""Run every worked example in the wiki.

Fences under docs/ in python, bash, julia, or rust are examples. Each one
starts with `# example` or `// example`. The process fails if a fence of
those languages has no marker, or if an example exits non-zero.

SEAMS_HOME is the extracted libseams 2.14.0 tree (bin/seams, lib/, include/).
DSEAMS_JL is a Dseams.jl checkout prepared with dev/develop_jll.jl.
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
import tempfile
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
# Contributor command lists live under docs/community and are not analyses.
SECTIONS = ("tutorials", "howto", "explanation", "reference")
FENCE = re.compile(
    r"^(?P<indent>[ ]*)```(?P<lang>python|bash|rust|julia)\n(?P<body>.*?)^[ ]*```[ ]*$",
    re.M | re.S,
)


def seams_home() -> Path:
    raw = os.environ.get("SEAMS_HOME", "")
    if not raw:
        sys.exit("SEAMS_HOME is not set")
    home = Path(raw)
    if not (home / "bin" / "seams").is_file():
        sys.exit(f"no seams binary under {home}")
    return home


def environment(home: Path) -> dict[str, str]:
    env = os.environ.copy()
    lib = str(home / "lib")
    env["SEAMS_HOME"] = str(home)
    env["SEAMS_LIBDIR"] = lib
    env["SEAMS_INCLUDE"] = str(home / "include")
    env["SEAMS_LANG_LIB"] = str(home / "lib" / "libseams_lang.so")
    env["LD_LIBRARY_PATH"] = lib + (
        ":" + env["LD_LIBRARY_PATH"] if env.get("LD_LIBRARY_PATH") else ""
    )
    env["PATH"] = str(home / "bin") + os.pathsep + env.get("PATH", "")
    env["PYTHONPATH"] = str(ROOT) + (
        os.pathsep + env["PYTHONPATH"] if env.get("PYTHONPATH") else ""
    )
    return env


def examples() -> list[tuple[Path, str, str]]:
    found = []
    pages = [DOCS / "index.md"]
    for section in SECTIONS:
        pages.extend(sorted((DOCS / section).rglob("*.md")))
    for path in pages:
        text = path.read_text(encoding="utf-8")
        for match in FENCE.finditer(text):
            lang = match.group("lang")
            body = textwrap.dedent(match.group("body"))
            marker = "// example" if lang == "rust" else "# example"
            first = next((line for line in body.splitlines() if line.strip()), "")
            if first.strip() != marker:
                sys.exit(f"{path}: {lang} fence does not start with {marker}")
            found.append((path, lang, body))
    if not found:
        sys.exit("no examples found")
    return found


def run(cmd: list[str], env: dict[str, str], cwd: Path | None = None) -> None:
    print("+", " ".join(cmd), flush=True)
    subprocess.run(cmd, cwd=cwd or ROOT, env=env, check=True)


def main() -> int:
    home = seams_home()
    env = environment(home)
    run([sys.executable, str(ROOT / "examples" / "make_lattices.py")], env)
    target = ROOT / "examples" / "rust" / "target"
    target.mkdir(parents=True, exist_ok=True)
    env["CARGO_TARGET_DIR"] = str(target)
    julia_project = os.environ.get("DSEAMS_JL", "")
    for path, lang, body in examples():
        print(f"\n== {path.relative_to(ROOT)} ({lang})", flush=True)
        if lang == "python":
            script = Path(tempfile.mkstemp(suffix=".py")[1])
            script.write_text(body, encoding="utf-8")
            run([sys.executable, str(script)], env)
        elif lang == "bash":
            script = Path(tempfile.mkstemp(suffix=".sh")[1])
            script.write_text(body, encoding="utf-8")
            run(["bash", str(script)], env)
        elif lang == "julia":
            if not julia_project:
                sys.exit("DSEAMS_JL is not set")
            script = Path(tempfile.mkstemp(suffix=".jl")[1])
            script.write_text(body, encoding="utf-8")
            run(["julia", f"--project={julia_project}", str(script)], env)
        elif lang == "rust":
            work = Path(tempfile.mkdtemp())
            (work / "src").mkdir()
            (work / "src" / "main.rs").write_text(body, encoding="utf-8")
            cargo = ROOT / "examples" / "rust"
            (work / "Cargo.toml").write_text(
                (cargo / "Cargo.toml").read_text(encoding="utf-8"), encoding="utf-8"
            )
            lock = cargo / "Cargo.lock"
            if lock.is_file():
                (work / "Cargo.lock").write_text(lock.read_text(encoding="utf-8"), encoding="utf-8")
            run(
                ["cargo", "run", "--quiet", "--manifest-path", str(work / "Cargo.toml")],
                env,
            )
        else:
            sys.exit(lang)
    print(f"\n{len(examples())} examples passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
