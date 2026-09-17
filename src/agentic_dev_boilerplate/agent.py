"""ADK root agent that loads skills/ on demand.

This replaces the Copilot .github/agents/*.agent.md forest.
The generator CLI (generate_boilerplate.py) is legacy; tz-new births
product repos. This module is the runnable ADK surface.

Skills follow agentskills.io + ADK SkillToolset (L1 metadata, L2 body,
L3 references/scripts).
"""

from __future__ import annotations

from pathlib import Path

SKILLS_DIR = Path(__file__).resolve().parent / "skills"

INSTRUCTION = """You are the house development agent for a tzervas repo.

Require a SESSION brief (repo, branch, goal, in_scope, done_when) before editing.
Load skills on demand. Do not paste every skill into context.
Never rewrite PERSONAL.md. Never append diaries to AGENTS.md.
Never push trunk. One concern per change.
Search this repo and named siblings before scaffolding.
Local gate must match CI. Skipped checks are not success.
"""


def list_skill_dirs(root: Path | None = None) -> list[Path]:
    base = root or SKILLS_DIR
    if not base.is_dir():
        return []
    return sorted(
        p for p in base.iterdir() if p.is_dir() and (p / "SKILL.md").is_file()
    )


def build_root_agent():  # type: ignore[no-untyped-def]
    """Build the ADK root agent. Import is deferred so tests can run without ADK."""
    from google.adk import Agent
    from google.adk.skills import load_skill_from_dir
    from google.adk.tools import skill_toolset

    skills = [load_skill_from_dir(path) for path in list_skill_dirs()]
    tools = []
    if skills:
        tools.append(skill_toolset.SkillToolset(skills=skills))
    return Agent(
        name="house_dev_agent",
        model="gemini-flash-latest",
        description="House development agent. Skills load on demand.",
        instruction=INSTRUCTION,
        tools=tools,
    )


# ADK discovery name
root_agent = None


def _try_bind() -> None:
    global root_agent
    try:
        root_agent = build_root_agent()
    except Exception:
        root_agent = None


_try_bind()
