# 2026-09-17 — Flatten Copilot personas into ADK skills

## Context

agentic-dev-boilerplate shipped 16 `.github/agents/*.agent.md` files plus matching
instruction encyclopedias. That is a stamp farm. tz-new already scaffolds products.
house-pack is the diet. autodev-public is the gate.

## Decision

- Live surface is `src/agentic_dev_boilerplate/skills/*/SKILL.md` + `agent.py`.
- Spec file is **SKILL.md**. `skills/SKILLS.md` is only an index.
- Personas collapse into eight skills, not sixteen ADK agents.
- `generate_boilerplate.py` is legacy. Do not teach it to emit 16 SKILL.md clones.

## Follow-up

- Point pyproject at ruff; drop black/isort/flake8 from runtime deps.
- Optional extra `adk` with `google-adk>=2,<3`.
- Stamp house-pack onto this repo.
- Upgrade python-adk-mcp-uv-template separately. Do not merge the two repos.
