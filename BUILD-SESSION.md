# BUILD-SESSION — repurpose agentic-dev-boilerplate

This branch **is** the handoff pack. Kick a Grok Build from `feat/adk-handoff-pack`.
Read this file first.

```text
repo: tzervas/agentic-dev-boilerplate
branch: feat/adk-handoff-pack
base: main
goal: flatten the Copilot .agent.md forest into one ADK root_agent + SKILL.md skills, stamp house-pack diet, align pyproject with house-rules (ruff, not black/isort/flake8)
in_scope: src/agentic_dev_boilerplate/agent.py src/agentic_dev_boilerplate/skills/ tests/test_skills_spec.py pyproject.toml AGENTS.md PERSONAL.md SESSION.md docs/ADK-SKILLS.md docs/decisions/
out_of_scope: new GitHub repo, merging python-adk-mcp-uv-template, 16 ADK LlmAgents, regenerating .github/agents, language port, fleet-wide stamp
done_when: tests/test_skills_spec.py passes; every skills/<name>/SKILL.md has name+description matching its directory; agent.py does not hard-import google-adk at module load
reuse_first: this branch; house-pack; tz-forge skills-generic; PR 28
issue: #28
do_not: append diaries to AGENTS.md; copy SKILL.md into .grok/.claude/.github as separately edited bodies; make google-adk a hard import for the legacy generator
first_action: read BUILD-SESSION.md, PERSONAL.md, SESSION.md, docs/conversion/FLATTEN-MAP.md, then apply remaining pyproject ruff + extra adk
```

Desired end state: reference ADK + skills implementation, not a scaffolder.
tz-new births product repos. house-pack is the diet. autodev-public house-rules.json is the machine gate.

## Steps

1. Stay on `feat/adk-handoff-pack`. Never push trunk.
2. Skills and agent.py are already on this branch under `src/agentic_dev_boilerplate/`.
3. Stamp diet: PERSONAL.md and SESSION.md are at repo root. Keep AGENTS.md thin.
4. pyproject: drop black/isort/flake8 from runtime deps; add ruff E,F,W,I,UP,B,SIM,RUF; optional extra `adk = ["google-adk>=2,<3"]`. See `snippets/pyproject.adk.toml`.
5. Leave `.github/agents` in place this slice; do not regenerate them.
6. Delete `src/agentic_dev_boilerplate/tmp_manager.py.backup` if present.
7. Run `uv run pytest tests/test_skills_spec.py -q`.
8. Commit follow-ups on this branch with `Refs #28`.

## Skill set

Core: session-brief, plan-slice, implement-change, local-gate, diagnose, security-review, ship-check, commit-prep.
Workflow: one-finding, reuse-first, claim-gate.

Spec file is SKILL.md (singular). skills/SKILLS.md is only an L1 index.
