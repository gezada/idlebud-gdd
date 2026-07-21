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
    """Replace a numbered subsection by structural heading boundaries."""
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


def rewrite_navigation_labels(gdd: str) -> str:
    """Set canonical menu labels; fall back to plain button text instead of failing on copy drift."""
    clickable = re.compile(
        r'<(?P<tag>a|button)\b(?P<attrs>[^>]*)>(?P<body>.*?)</(?P=tag)>',
        re.I | re.S,
    )
    candidates = [
        "Carry e formação de elenco",
        "Carry, Treinamento e Progressão PvE",
        "Carry, treinamento e PvE",
        "Carry e PvE",
        "Campo de Batalha, Formação e Posicionamento",
        "Campo de batalha e formação",
        "Campo de batalha",
    ]
    found = {target: 0 for target in canonical.NAV_LABELS}

    def repl(match: re.Match[str]) -> str:
        attrs = match.group("attrs")
        body = match.group("body")
        for target, label in canonical.NAV_LABELS.items():
            if not re.search(
                rf'(?:href|data-target|data-section)\s*=\s*["\']#?{re.escape(target)}["\']',
                attrs,
                re.I,
            ):
                continue
            found[target] += 1
            if label not in canonical.impl.visible_text(body):
                for candidate in candidates:
                    body, count = re.subn(
                        re.escape(candidate), label, body, count=1, flags=re.I
                    )
                    if count:
                        break
            if label not in canonical.impl.visible_text(body):
                point = 8 if target == "battlefield-formation" else 9
                body = f"{point}. {label}"
            break
        return f'<{match.group("tag")}{attrs}>{body}</{match.group("tag")}>'

    gdd = clickable.sub(repl, gdd)
    missing = [target for target, count in found.items() if count == 0]
    if missing:
        raise RuntimeError(f"Navegação estrutural ausente para: {missing}")
    return gdd


canonical.replace_subsection = replace_subsection
canonical.rewrite_navigation_labels = rewrite_navigation_labels


if __name__ == "__main__":
    canonical.main()
