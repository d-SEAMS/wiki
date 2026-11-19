"""Write the small lattices the tutorials read.

The ice Ih dump, the hydrate cells, the interface, the brine frame, and
the three-frame nucleation dump are copies of the public seams-core
2.14.0 inputs. This script writes the three lattices that are not in
that tree, plus a coordinate-only XYZ of the ice Ih cell.
"""

from __future__ import annotations

import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "examples" / "inputs"


def dump(path: Path, points: list[tuple[float, float, float]], box: tuple[str, str, str]) -> None:
    lines = [
        "ITEM: TIMESTEP",
        "0",
        "ITEM: NUMBER OF ATOMS",
        str(len(points)),
        "ITEM: BOX BOUNDS pp pp pp",
        box[0],
        box[1],
        box[2],
        "ITEM: ATOMS id type x y z",
    ]
    for index, (x, y, z) in enumerate(points, start=1):
        lines.append(f"{index} 1 {x:.6f} {y:.6f} {z:.6f}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def ice_ic() -> None:
    # Diamond oxygen lattice of ice Ic. Conventional cube a = 6.358 angstrom,
    # repeated 2x2x2: 64 sites.
    a = 6.358
    basis = (
        (0.0, 0.0, 0.0),
        (0.5, 0.5, 0.0),
        (0.5, 0.0, 0.5),
        (0.0, 0.5, 0.5),
        (0.25, 0.25, 0.25),
        (0.75, 0.75, 0.25),
        (0.75, 0.25, 0.75),
        (0.25, 0.75, 0.75),
    )
    points = []
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for bx, by, bz in basis:
                    points.append(((bx + i) * a, (by + j) * a, (bz + k) * a))
    edge = f"0 {2 * a:.6f}"
    dump(OUT / "ice_ic.lammpstrj", points, (edge, edge, edge))


def nanotube() -> None:
    # Eight stacked squares, side 2.75 angstrom, axial step 2.80 angstrom.
    side = 2.75
    step = 2.80
    square = ((0.0, 0.0), (side, 0.0), (side, side), (0.0, side))
    points = []
    for layer in range(8):
        for x, y in square:
            points.append((x + 5.0, y + 5.0, layer * step + 2.0))
    length = 8 * step + 4.0
    dump(OUT / "nanotube.lammpstrj", points, ("0 15.000000", "0 15.000000", f"0 {length:.6f}"))


def monolayer() -> None:
    # 8x8 square sheet, spacing 2.75 angstrom, with a 0.15 angstrom
    # sinusoidal corrugation so the sheet has a thickness.
    spacing = 2.75
    points = []
    index = 0
    for i in range(8):
        for j in range(8):
            z = 10.0 + 0.15 * math.sin(index)
            points.append((i * spacing, j * spacing, z))
            index += 1
    edge = f"0 {8 * spacing:.6f}"
    dump(OUT / "monolayer.lammpstrj", points, (edge, edge, "0 20.000000"))


def ice_xyz() -> None:
    # Coordinate list only. No cell. The reader then takes the span of
    # the coordinates as the box.
    text = (OUT / "ice1h.lammpstrj").read_text(encoding="utf-8").splitlines()
    atoms: list[str] = []
    reading = False
    for line in text:
        if line.startswith("ITEM: ATOMS"):
            reading = True
            continue
        if line.startswith("ITEM:"):
            reading = False
            continue
        if reading:
            parts = line.split()
            atoms.append(f"O {parts[2]} {parts[3]} {parts[4]}")
    body = [str(len(atoms)), "ice Ih oxygens, coordinates only", *atoms]
    (OUT / "ice1h.xyz").write_text("\n".join(body) + "\n", encoding="utf-8")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    ice_ic()
    nanotube()
    monolayer()
    ice_xyz()


if __name__ == "__main__":
    main()
