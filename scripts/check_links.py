#!/usr/bin/env python3
"""Check that local Markdown links and heading anchors in this repo resolve.

Stdlib only - no dependencies beyond what ships with Python, so it can run
as `make lint` without installing anything.
"""

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")


def slugify(heading: str) -> str:
    heading = re.sub(r"[`*_]", "", heading)
    heading = heading.strip().lower()
    heading = re.sub(r"[^\w\s-]", "", heading)
    heading = re.sub(r"[\s]+", "-", heading)
    return heading


def anchors_in(path: Path) -> set[str]:
    slugs: dict[str, int] = {}
    anchors = set()
    for line in path.read_text().splitlines():
        match = HEADING_RE.match(line)
        if not match:
            continue
        slug = slugify(match.group(2))
        if slug in slugs:
            slugs[slug] += 1
            slug = f"{slug}-{slugs[slug]}"
        else:
            slugs[slug] = 0
        anchors.add(slug)
    return anchors


def check_file(path: Path, errors: list[str]) -> None:
    text = path.read_text()
    for match in LINK_RE.finditer(text):
        target = match.group(1)
        if target.startswith(("http://", "https://", "mailto:")):
            continue
        file_part, _, anchor = target.partition("#")
        if not file_part:
            # Same-file anchor, e.g. [x](#some-heading)
            if anchor and anchor not in anchors_in(path):
                errors.append(f"{path}: broken anchor '#{anchor}' (same file)")
            continue
        target_path = (path.parent / file_part).resolve()
        if not target_path.exists():
            errors.append(f"{path}: links to missing file '{file_part}'")
            continue
        if anchor and target_path.suffix == ".md":
            if anchor not in anchors_in(target_path):
                errors.append(
                    f"{path}: links to '{file_part}#{anchor}', "
                    f"but no heading in {target_path.name} slugifies to '{anchor}'"
                )


def main() -> int:
    errors: list[str] = []
    for path in sorted(REPO_ROOT.rglob("*.md")):
        if ".git" in path.parts:
            continue
        check_file(path, errors)

    if errors:
        print("Broken local links found:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print("All local Markdown links and anchors resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
