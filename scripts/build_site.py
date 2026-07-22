#!/usr/bin/env python3
"""Build the docs portal from the canonical readable GDD v17 source."""

from __future__ import annotations

import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "gdd-source" / "index.html"


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("Usage: build_site.py <site-dir>")

    site = Path(sys.argv[1])
    gdd = site / "gdd" / "index.html"
    html = SOURCE.read_text(encoding="utf-8")
    for expected in [
        "Game Design Document · v17",
        "<title>Idle Bud — Game Design Document v17</title>",
        "Idle Bud — Game Design Document v17</footer>",
    ]:
        if expected not in html:
            raise RuntimeError(f"Fonte canônica inválida: {expected}")

    gdd.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, gdd)
    from build_docs_portal import main as build_portal

    old_argv = sys.argv
    try:
        sys.argv = ["build_docs_portal.py", str(site), str(gdd)]
        build_portal()
    finally:
        sys.argv = old_argv

    (site / ".nojekyll").touch()


if __name__ == "__main__":
    main()
