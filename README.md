# Agentic Dev Boilerplate

<!-- FLEET-BADGES:BEGIN -->
[![CI](https://github.com/tzervas/agentic-dev-boilerplate/actions/workflows/fleet-ci.yml/badge.svg?branch=main)](https://github.com/tzervas/agentic-dev-boilerplate/actions/workflows/fleet-ci.yml?query=branch%3Amain)
[![Security](https://github.com/tzervas/agentic-dev-boilerplate/actions/workflows/fleet-security.yml/badge.svg?branch=main)](https://github.com/tzervas/agentic-dev-boilerplate/actions/workflows/fleet-security.yml?query=branch%3Amain)
<!-- FLEET-BADGES:END -->

Schema-driven generator for **agent instruction files**, GitHub workflow stubs, and related
scaffolding for multi-agent development layouts.

**Prefer [tz-forge](https://github.com/tzervas/tz-forge) `tz-new` for new product repositories.**
This package is the specialized / legacy path when you need schema-driven multi-agent instruction
emit and optional fleet workflow injection.

| Need | Prefer |
|------|--------|
| Fleet modules, project kinds, assistant profiles | **`tz-new`** ([tz-forge](https://github.com/tzervas/tz-forge)) |
| ADK + MCP + uv agent template | [python-adk-mcp-uv-template](https://github.com/tzervas/python-adk-mcp-uv-template) |
| Schema-driven multi-agent instruction/workflow emit | **this** package |

Measured truth (install, tests, what actually generates): **[docs/CURRENT-STATE.md](docs/CURRENT-STATE.md)**.  
History and roadmap: [docs/DEVELOPMENT-PATH.md](docs/DEVELOPMENT-PATH.md) · [docs/ROADMAP.md](docs/ROADMAP.md) · [docs/README.md](docs/README.md).

## Status snapshot (read before installing)

As of the last docs measurement (`main` @ `ad83a30`):

- **Source install** (`uv pip install -e .`) **fails** — hard dependency `chngbrgr` is not on PyPI.
- **Default** template generation on current `main` **fails** (incomplete repo-root template tree).
- **Bootdisk** template generation + **fleet pack inject** **work** from a checkout with runtime deps.
- **PyPI `1.1.2`** still installs and can generate a default instruction tree (older CLI; no fleet-pack flags).

Do not treat CI badges alone as a green product gate; see CURRENT-STATE for Actions samples.

## Quickstart (< 1 minute)

### Option A — new product repo (recommended)

```bash
git clone https://github.com/tzervas/tz-forge.git
cd tz-forge
python3 cli/tz_new.py --list
python3 cli/tz_new.py python-lib my-lib --assistant=solo-ai
```

### Option B — PyPI artifact (last published generator)

Measured: installs and completes default generate.

```bash
uv venv .venv && source .venv/bin/activate
uv pip install 'agentic-dev-boilerplate==1.1.2'
agentic-dev-boilerplate --help
agentic-dev-boilerplate -s /path/to/schema.yaml -o ./my-project
```

Use a schema shaped like the repo’s `project-schema.yaml` (`project`, `languages`, `agents`,
`workflows` as a **map** of flags).

### Option C — this checkout, bootdisk + fleet pack (current `main`)

Measured working path when full `uv pip install -e .` is blocked:

```bash
git clone https://github.com/tzervas/agentic-dev-boilerplate
cd agentic-dev-boilerplate
uv venv .venv && source .venv/bin/activate
uv pip install jinja2 pyyaml click
export PYTHONPATH=src
python src/agentic_dev_boilerplate/generate_boilerplate.py \
  --template bootdisk-agentic-structure \
  -s test-bootdisk-schema.yaml \
  -o ./out-bootdisk
```

Expect fleet workflows under `out-bootdisk/.github/workflows/` (`fleet-ci.yml`, …).  
Default (`project-schema.yaml` without `--template`) is **broken on current main** until the
template-path defect is fixed (see roadmap).

### CLI flags (current tree)

```text
agentic-dev-boilerplate -s SCHEMA -o OUT
  -t / --template TEXT
  --fleet-pack / --no-fleet-pack
  --fleet-pack-path PATH
```

Agent rules for assistants: [AGENTS.md](AGENTS.md). Fleet pack notes: [docs/FLEET_STANDARDS.md](docs/FLEET_STANDARDS.md).

## Prerequisites

- Python 3.11+
- [uv](https://docs.astral.sh/uv/) recommended
- Git

## Development checks

```bash
# Prefer after install is fixed; today lock/install fail on chngbrgr — see CURRENT-STATE
uv pip install -e .    # currently FAILS on main
./test-package.sh      # measured 3/12 at last docs run
# Workaround used in measurement:
uv pip install jinja2 pyyaml click pytest
PYTHONPATH=src python -m pytest tests/ -o "markers=slow: slow tests"
```

## Project layout (short)

```text
src/agentic_dev_boilerplate/   # generator, tmp manager, packaged templates + fleet_pack
templates/                     # repo-root templates (bootdisk + partial default)
pack/fleet-standards/          # vendored fleet workflows/docs
project-schema.yaml            # example schema
tests/
docs/                          # PM suite + guides
```

## License

MIT — see [LICENSE](LICENSE).
