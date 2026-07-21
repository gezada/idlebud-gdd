#!/usr/bin/env python3
import re

import patch_point8_battlefield_v2 as canonical


def replace_subsection(
    section: str,
    point: int,
    current: int,
    following: int | None,
    replacement: str,
) -> str:
    """Replace a numbered subsection by heading boundaries, including the final subsection."""
    if following is None:
        pattern = re.compile(
            rf'<h3\b[^>]*>\s*{point}\.{current}\b.*?</h3>.*?\Z',
            re.I | re.S,
        )
    else:
        pattern = re.compile(
            rf'<h3\b[^>]*>\s*{point}\.{current}\b.*?</h3>.*?'
            rf'(?=<h3\b[^>]*>\s*{point}\.{following}\b)',
            re.I | re.S,
        )
    section, count = pattern.subn(replacement + "\n", section, count=1)
    if count != 1:
        raise RuntimeError(
            f"Subseção {point}.{current} ausente ou duplicada; transformação estrutural interrompida."
        )
    return section


canonical.replace_subsection = replace_subsection


if __name__ == "__main__":
    canonical.main()
