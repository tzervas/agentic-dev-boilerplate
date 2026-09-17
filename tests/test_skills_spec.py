"""Validate SKILL.md frontmatter without requiring google-adk at test time."""

from __future__ import annotations

import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "src" / "agentic_dev_boilerplate" / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def _skill_dirs() -> list[Path]:
    if not SKILLS.is_dir():
        return []
    return sorted(p for p in SKILLS.iterdir() if p.is_dir() and (p / "SKILL.md").is_file())


def test_at_least_one_skill() -> None:
    assert _skill_dirs(), f"no SKILL.md trees under {SKILLS}"


@pytest.mark.parametrize("skill_dir", _skill_dirs(), ids=lambda p: p.name)
def test_frontmatter(skill_dir: Path) -> None:
    text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    assert text.startswith("---\n"), f"{skill_dir.name}: missing YAML frontmatter"
    _, fm, body = text.split("---", 2)
    fields: dict[str, str] = {}
    for line in fm.splitlines():
        if ":" in line and not line.strip().startswith("#"):
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip().strip('"')
    name = fields.get("name", "")
    description = fields.get("description", "")
    assert NAME_RE.match(name), f"invalid name {name!r}"
    assert 1 <= len(name) <= 64
    assert skill_dir.name == name, "directory name must match frontmatter name"
    assert description, "description required"
    assert len(description) <= 1024
    assert body.strip(), "L2 instructions required"
