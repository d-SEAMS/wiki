"""Figure style for the wiki. The series themselves come from the engine."""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

INK = "#0a1a2b"
MUTED = "#3e566e"
IH = "#e69f00"
WATER = "#56b4e9"
IFACE = "#e0cc18"
IC = "#0072b2"
CLATH = "#cc79a7"
ICLATH = "#009e73"

LABEL_COLOUR = {
    "cubic": IC,
    "hexagonal": IH,
    "water": WATER,
    "interfacial": IFACE,
    "clathrate": CLATH,
    "interClathrate": ICLATH,
    "reCubic": IC,
    "reHex": IH,
    "unclassified": MUTED,
}


def panel(width: float = 6.4, height: float = 4.2):
    fig, ax = plt.subplots(figsize=(width, height), facecolor="white")
    ax.set_facecolor("white")
    ax.tick_params(colors=INK, labelsize=9)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#d0e1f0")
    ax.spines["bottom"].set_color("#d0e1f0")
    ax.xaxis.label.set_color(INK)
    ax.yaxis.label.set_color(INK)
    ax.title.set_color(INK)
    return fig, ax


def save(fig, path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    fig.savefig(path, dpi=140)
    plt.close(fig)


def scatter(path, xyz, colours, title: str) -> None:
    fig = plt.figure(figsize=(5.4, 4.6), facecolor="white")
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(
        xyz[:, 0],
        xyz[:, 1],
        xyz[:, 2],
        c=colours,
        s=16,
        depthshade=False,
        linewidths=0,
    )
    ax.set_title(title, color=INK, fontsize=11)
    ax.set_xlabel("x (A)")
    ax.set_ylabel("y (A)")
    ax.set_zlabel("z (A)")
    ax.tick_params(colors=MUTED, labelsize=7)
    ax.xaxis.label.set_color(MUTED)
    ax.yaxis.label.set_color(MUTED)
    ax.zaxis.label.set_color(MUTED)
    save(fig, path)
