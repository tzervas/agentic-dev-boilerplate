# 2026-09-17 — Flatten Copilot personas into ADK skills

## Context

agentic-dev-boilerplate shipped 16 `.github/agents/*.agent.md` files plus matching
instruction encyclopedias. That is a stamp farm. tz-new already scaffolds products.
house-pack is the diet. autodev-public is the gate. This repo was emitting a fourth
copy of the same roles.

## Decision

- Live surface is `src/agentic_dev_boilerplate/skills/*/SKILL.md` + `agent.py`.
- Spec file is **SKILL.md** (agentskills.io / ADK). `skills/SKILLS.md` is only an index.
- Personas collapse: planner/orchestrator/PM → session-brief + plan-slice;
  implementer roles → implement-change; tester → local-gate; debugger → diagnose;
  security → security-review; deployer/devops → ship-check.
- Workflow extras: one-finding, reuse-first, claim-gate, commit-prep.
- frontend/mobile/fullstack/ml Copilot files are not ADK units. They stay in
  `.github/agents/` until a follow-up moves them to `docs/history/copilot-agents/`.
- `generate_boilerplate.py` is legacy. Do not teach it to emit 16 new SKILL.md clones.

## Landed on feat/adk-handoff-pack

- 11 SKILL.md trees + deferred `agent.py` (no hard google-adk import).
- pyproject: ruff E,F,W,I,UP,B,SIM,RUF; runtime no longer black/isort/flake8;
  optional extra `adk = ["google-adk>=2,<3"]`.
- Diet files PERSONAL.md + SESSION.md. Thin AGENTS.md.
- `scripts/check.sh` is the local gate.

## Still later

- Upgrade python-adk-mcp-uv-template's google-adk pin separately. Do not merge the two repos.
- Stamp house-pack onto CogSynDelta / memory-gate / autodev-public.
