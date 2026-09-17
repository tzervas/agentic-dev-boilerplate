# Fleet surfaces — do not invent a fourth scaffolder

| Surface | Job |
|---|---|
| tz-forge tz-new | Births product repos (python-lib, rust-lib, python-mcp, …) |
| house-pack | Diet overlay: PERSONAL.md + SESSION.md + thin AGENTS.md + stamp.sh |
| autodev-public config/house-rules.json | Machine gates (uv, ruff E/F/W/I/UP/B/SIM/RUF, clippy -D warnings, never push trunk, one_finding_per_pr) |
| tz-forge modules/agents/skills-generic | Shared SKILL.md source (commit-prep, pr-review, fleet-gap, unsafe-review, cargo-check) |
| agentic-dev-boilerplate (this conversion) | Reference ADK app + skill set. Not the scaffolder |
| python-adk-mcp-uv-template | ADK+MCP product template. Bump google-adk>=2,<3 in its own PR. Do not merge |
| tzervas/autodev @ feat/bootstrap | Private / Forgejo live autodev. Public subset is autodev-public |
| agent-workflows g-job-brief.md | SESSION sibling. Unify schemas; do not load PLAYBOOK.md (40k) every session |

Live GitHub:
- https://github.com/tzervas/house-pack (private)
- https://github.com/tzervas/agentic-dev-boilerplate/pull/28 (draft feat/adk-skills)
- https://github.com/tzervas/autodev-public
- https://github.com/tzervas/tz-forge
