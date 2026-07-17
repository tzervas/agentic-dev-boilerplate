# AGENTS.md — agentic-dev-boilerplate

Short house rules for AI coding assistants working in this generator repo.

## Prefer tz-forge for new projects

**New product repos should prefer [tz-forge](https://github.com/tzervas/tz-forge) `tz-new`**, not this generator:

```bash
git clone https://github.com/tzervas/tz-forge.git
cd tz-forge
python3 cli/tz_new.py --list
python3 cli/tz_new.py python-lib my-lib --assistant=solo-ai
# or: pip install -e . && tz-new rust-lib my-crate --assistant=fractal-swarm
```

| Need | Tool |
|------|------|
| Fleet-aware scaffold (kinds, assistant profiles, modules) | **`tz-new`** from [tz-forge](https://github.com/tzervas/tz-forge) |
| ADK + MCP + uv agent layout | [python-adk-mcp-uv-template](https://github.com/tzervas/python-adk-mcp-uv-template) |
| Multi-agent instruction/workflow generation (legacy) | **this** repo (`agentic-dev-boilerplate`) |

This package remains useful for schema-driven multi-agent instruction files and
legacy project shapes. When it still emits GitHub Actions, inject the
**fleet pack** (`--fleet-pack` / schema `workflows.fleet_standards`) so generated
repos match workstation fleet CI (see [docs/FLEET_STANDARDS.md](docs/FLEET_STANDARDS.md)).

## Local checks

```bash
uv pip install -e .
./test-package.sh
# or
uv run pytest -q
```

## Project map

```
src/agentic_dev_boilerplate/
  generate_boilerplate.py   # CLI entry (agentic-dev-boilerplate)
templates/                  # Jinja2 templates (default + bootdisk-…)
pack/fleet-standards/       # Vendored fleet workflows + docs (P28c)
project-schema.yaml         # Example schema
tests/
docs/
```

## PR flow

1. Feature/chore branch (never commit directly to `main`)
2. Small diffs; run tests
3. PR → `main` (or `dev` when present) with correct issue keywords:

| Target | Keywords |
|--------|----------|
| `dev` / feature | `Refs #n` only |
| `main` | `Closes #n` / `Fixes #n` |

## Safety

- No secrets in commits or logs
- Do **not** request automatic Copilot code review

## Further reading

- [README.md](README.md)
- [docs/FLEET_STANDARDS.md](docs/FLEET_STANDARDS.md)
- [tz-forge](https://github.com/tzervas/tz-forge) · `tz-new`
