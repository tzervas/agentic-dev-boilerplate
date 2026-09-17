# AGENTS.md — agentic-dev-boilerplate

Keep this file thin. Diaries go to `docs/decisions/`. Diet: [PERSONAL.md](PERSONAL.md). Session: [SESSION.md](SESSION.md).

This repo is a **reference ADK + SKILL.md implementation**, not the product scaffolder.

| Need | Surface |
|------|---------|
| Birth a product repo | [tz-forge](https://github.com/tzervas/tz-forge) `tz-new` |
| Diet overlay | [house-pack](https://github.com/tzervas/house-pack) |
| Machine gates | autodev-public `config/house-rules.json` |
| ADK skills (this repo) | `src/agentic_dev_boilerplate/skills/*/SKILL.md` |

`generate_boilerplate.py` is **legacy**. Do not teach it to emit 16 SKILL.md clones. Do not regenerate `.github/agents/`.

## Commands

```bash
uv run pytest tests/test_skills_spec.py -q
./scripts/check.sh --quick
uv sync --extra adk   # only if running the ADK agent
uv run adk run src/agentic_dev_boilerplate
```

## Layout

- `src/agentic_dev_boilerplate/agent.py` — deferred ADK root agent
- `src/agentic_dev_boilerplate/skills/` — spec file is SKILL.md
- `docs/conversion/FLATTEN-MAP.md` — Copilot persona collapse
- `docs/decisions/` — append-only

## Branch / PR

Never push trunk. Feature → `Refs #n`. Main → `Closes #n`. One finding per PR. No Copilot auto-review. Do not self-merge.

## Do not

- Invent toolchain versions that contradict lockfiles.
- Keep black / isort / flake8 as runtime deps (ruff is the gate).
- Treat skipped CI as green.
- Append wave diaries here.
