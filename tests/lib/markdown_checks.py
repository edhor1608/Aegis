from __future__ import annotations

import re
from pathlib import Path


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def has_heading(text: str, heading: str) -> bool:
    return re.search(rf"^##\s+{re.escape(heading)}\s*$", text, flags=re.MULTILINE) is not None


def contains_all(text: str, required_snippets: list[str]) -> tuple[bool, list[str]]:
    missing = [snippet for snippet in required_snippets if snippet not in text]
    return len(missing) == 0, missing


def normalize_markdown(text: str) -> str:
    lines = [line.rstrip() for line in text.splitlines()]
    normalized = "\n".join(lines).strip() + "\n"
    return normalized


def extract_section(text: str, heading: str) -> str:
    lines = text.splitlines()
    start_index = None

    for idx, line in enumerate(lines):
        if line.strip() == f"## {heading}":
            start_index = idx
            break

    if start_index is None:
        return ""

    end_index = len(lines)
    for idx in range(start_index + 1, len(lines)):
        if lines[idx].startswith("## "):
            end_index = idx
            break

    section = "\n".join(lines[start_index:end_index]).strip()
    return section + "\n"
