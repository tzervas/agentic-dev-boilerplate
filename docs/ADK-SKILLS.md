# ADK + SKILL.md conversion

This repo is no longer the default product scaffolder. `tz-new` births repos.
`house-pack` is the diet. `autodev-public` enforces gates.

This branch adds a **flat** ADK surface:

```
src/agentic_dev_boilerplate/
  agent.py                          # root_agent + SkillToolset
  skills/
    SKILLS.md                       # L1 index only (not the spec file)
    session-brief/SKILL.md
    plan-slice/SKILL.md
    implement-change/SKILL.md
    local-gate/SKILL.md
    diagnose/SKILL.md
    security-review/SKILL.md
    ship-check/SKILL.md
    commit-prep/SKILL.md
```

The spec file is **SKILL.md** ([agentskills.io](https://agentskills.io/specification),
ADK 1.25+ / 2.x). There is no official `SKILLS.md` format. The index is a courtesy.

## Persona collapse

| Old Copilot file | New surface |
|---|---|
| planner, project-manager, orchestrator | `session-brief` + `plan-slice` + ADK root agent |
| software-engineer, backend, frontend, fullstack, api, mobile | `implement-change` |
| tester | `local-gate` |
| debugger | `diagnose` |
| security | `security-review` |
| deployer, devops-specialist | `ship-check` |
| ai-engineer, ml-engineer, data-scientist | tz-forge `skills-ml` (not copied here) |
| systems-engineer | fleet/autodev, not an ADK unit |

`.github/agents/` and `.github/instructions/` stay until a follow-up moves them
to `docs/history/copilot-agents/`. Do not regenerate them.

## Run

```bash
uv sync --extra adk          # after pyproject extra lands
uv run pytest tests/test_skills_spec.py -q
# live:
uv run adk run src/agentic_dev_boilerplate
```

`test_skills_spec.py` does not need google-adk. It checks frontmatter only.

## Other modernization still open

- pyproject: ruff instead of black/isort/flake8 as runtime deps
- delete `tmp_manager.py.backup`, shrink `demo-output/`
- stamp `house-pack` (PERSONAL / SESSION / thin AGENTS)
- bump `python-adk-mcp-uv-template` google-adk pin separately
- generator CLI emits nothing new; retire or teach it to copy this skills/ tree
