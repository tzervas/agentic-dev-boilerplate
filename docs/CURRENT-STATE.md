# Current state

**Measured at:** 2026-07-25 (UTC)  
**Commit:** `ad83a3009cb77e60044f33644127185a7e486cc8` (`ad83a30`, branch tip of `main` at measure time)  
**Default branch:** `main`  
**Declared version in tree:** `1.1.4` (`pyproject.toml`)  
**Latest GitHub Release / tag:** `v1.1.2`  
**Latest PyPI:** `1.1.2` (does **not** include current `main` fleet-pack CLI work as a published artifact)

This document records what was **actually run** in the docs measurement pass. It is not a
product vision. Stale claims elsewhere in the repo are listed under [False or stale docs](#false-or-stale-docs).

## Capability matrix

| Capability | Status | Evidence (summary) |
|------------|--------|--------------------|
| Prefer / document tz-forge for new product repos | **VERIFIED** (docs + CLI banner) | README / AGENTS.md; generator prints tz-forge URL on generate |
| CLI `--help` (source / wheel entry) | **VERIFIED** | Help text shows `-s/-o/-t`, `--fleet-pack`, `--fleet-pack-path` |
| `uv pip install -e .` from this tree | **FAILS** | Resolver: `chngbrgr` not found on package index |
| `uv lock --dry-run` / `uv sync` | **FAILS** | Same `chngbrgr` unsatisfiable |
| `uv build --wheel` | **VERIFIED** | Built `dist/agentic_dev_boilerplate-1.1.4-py3-none-any.whl` |
| Default template generate (`project-schema.yaml`) on **this commit** | **FAILS** | `TemplateNotFound: agent_planner_instructions.md.j2` under repo-root `templates/` |
| Bootdisk template generate on **this commit** | **VERIFIED** (partial) | Completes; injects fleet pack; skips several missing optional templates |
| Fleet pack inject (`--fleet-pack` default path) | **VERIFIED** on bootdisk run | Copies `fleet-ci.yml`, `fleet-security.yml`, close/reopen workflows, `docs/FLEET_STANDARDS.md`, scripts |
| Prompt template generation | **UNVERIFIED / not implemented** | Code path prints skip + `TODO` |
| Multi-agent solver as usable product | **UNVERIFIED** | Module imports fail when run as script (`relative import`); no end-to-end run in this pass |
| `TmpManager` unit behavior | **VERIFIED** (tests) | `tests/test_tmp_manager.py` all passed |
| Full pytest suite green | **FAILS** | **16 failed, 25 passed** (with `slow` marker registered for collection) |
| `./test-package.sh` green | **FAILS** | **3/12** steps passed in this run |
| PyPI `1.1.2` install + default generate | **VERIFIED** (older artifact) | Installs; generates agents/workflows (package-local templates); **no** `--template` / fleet-pack flags of current main |
| GitHub Actions on `main` as green gate | **NOT a reliable green signal** | Recent `fleet-ci` / `fleet-security` / `CI/CD` on `main` **cancelled**; `reopen-issues` workflow **failure** on push; **zero required status checks** on `main` ruleset |
| Long-term memory system | **UNVERIFIED — design only** | `docs/LONG_TERM_MEMORY.md`; no implementation package on tree |
| Docker / docker-compose test path | **UNVERIFIED** | Not run in this measurement (resource/time); treat README claim as unproven here |
| GPG-signed commit enforcement as shipped feature | **UNVERIFIED** | Hooks/scripts exist; not exercised end-to-end in this pass |

## How this was measured

Environment: Linux, Python **3.12.3**, `uv 0.11.23`. Resource note: Python tests were not
parallelized beyond default pytest; no unbounded cargo/build farm.

### 1. Source install (fails)

```text
$ uv venv .venv && source .venv/bin/activate
$ uv pip install -e .
  × No solution found when resolving dependencies:
  ╰─▶ Because chngbrgr was not found in the package registry and
      agentic-dev-boilerplate==1.1.4 depends on chngbrgr>=0.1.0, we can
      conclude that agentic-dev-boilerplate==1.1.4 cannot be used.
```

Cross-check: `curl -sS -o /dev/null -w "%{http_code}" https://pypi.org/pypi/chngbrgr/json` → **404**.  
Repo `tzervas/chngbrgr` **does** exist on GitHub (API name/description returned).

### 2. Wheel build (succeeds)

```text
$ uv build --wheel
Building wheel...
Successfully built dist/agentic_dev_boilerplate-1.1.4-py3-none-any.whl
```

Wheel contains package-local `agentic_dev_boilerplate/templates/*` and `fleet_pack/*`
(inspected via `zipfile`).

### 3. Runtime deps without `chngbrgr` + pytest

Installed runtime/test tools with `uv pip install jinja2==3.1.6 pyyaml==6.0.3 click==8.4.2 pytest==9.1.1 …` then:

```text
$ export PYTHONPATH=src
$ python -m pytest tests/ -o "markers=slow: slow tests" --tb=no
… 
16 failed, 25 passed in 0.41s
```

Without registering the `slow` marker, collection **errors**:

```text
ERROR tests/test_integration.py - Failed: 'slow' not found in `markers` configuration option
Interrupted: 1 error during collection
```

**Failure classes (observed):**

1. **Unit tests / sample schema:** fixtures use `"workflows": [list…]`. Code does
   `self.schema.get("workflows", {}).get("fleet_standards", True)` →  
   `AttributeError: 'list' object has no attribute 'get'`  
   (P28c fleet flag assumes **dict** workflows; `project-schema.yaml` is a dict; tests are not.)
2. **Integration tests:** `jinja2.exceptions.TemplateNotFound: 'agent_planner_instructions.md.j2'`
   in search path `…/templates` (repo root), which lacks planner/debugger/deployer/… templates
   that **do** exist under `src/agentic_dev_boilerplate/templates/`.

`tests/test_tmp_manager.py` alone: all dots / pass.

### 4. CLI generation on this commit

**Default (fails):**

```text
$ python src/agentic_dev_boilerplate/generate_boilerplate.py \
    -s project-schema.yaml -o /tmp/pm-docs-gen-test
🚀 Generating agentic development boilerplate...
ℹ️  Prefer tz-forge `tz-new` …
🤖 Generating agent instructions...
❌ Error: 'agent_planner_instructions.md.j2' not found in search path: '…/templates'
Aborted!
```

**Bootdisk (succeeds with skips + fleet inject):**

```text
$ python src/agentic_dev_boilerplate/generate_boilerplate.py \
    --template bootdisk-agentic-structure \
    -s test-bootdisk-schema.yaml -o /tmp/pm-docs-bootdisk
… (warnings for missing optional script/doc templates) …
📦 Injecting fleet standards pack...
  + .github/workflows/close-issues-on-main.yml
  + .github/workflows/fleet-ci.yml
  + .github/workflows/fleet-security.yml
  + .github/workflows/reopen-issues-closed-off-main.yml
  + docs/FLEET_STANDARDS.md
  + scripts/close-linked-issues.sh
  + scripts/fleet-badge-block.md
  + .github/PULL_REQUEST_TEMPLATE.md
✅ Boilerplate generation complete!
```

File count under output: **20** files at measurement (including `.git` hooks written by generate).

### 5. `./test-package.sh`

```text
📊 Test Results: 3/12 tests passed
```

Failures included install (chngbrgr), generation, imports, `uv sync`.  
Passes observed included dependency-pinning grep and earlier lock/build steps as far as the
script progressed (lock step itself is unsatisfiable in current resolver output; treat the
script’s early “pass” lines as not a clean green suite—**re-run output above is authoritative
for the final 3/12**).

### 6. Lint (informational; not a merge gate here)

```text
$ black --check src tests
would reformat …/tests/test_generate_boilerplate.py
would reformat …/src/agentic_dev_boilerplate/generate_boilerplate.py
2 files would be reformatted, 7 files would be left unchanged.

$ flake8 src tests --count --max-line-length=88
… (F401 unused imports, E501, F541) …
31
```

(`black`/`flake8` exit codes in the measurement shell were not treated as CI truth; counts
are from the printed tool output.)

### 7. PyPI 1.1.2 smoke (isolated venv under `/tmp`)

```text
$ uv pip install --python /tmp/pypi-clean/bin/python 'agentic-dev-boilerplate==1.1.2'
$ /tmp/pypi-clean/bin/agentic-dev-boilerplate -s /tmp/schema.yaml -o /tmp/pypi-gen
✅ Boilerplate generation complete!
```

Produced 9 agent instruction files + pr-automation/ci-cd/agent-coordination workflows (22 files).  
Template resolution in **1.1.2**: `Path(__file__).parent / "templates"` (package-local).  
**1.1.2 has no `--template` option** (CLI error: `No such option: --template`).

### 8. CI via GitHub API

```text
$ gh api /repos/tzervas/agentic-dev-boilerplate/actions/runs?per_page=10
```

Representative recent rows (trimmed):

| Workflow | Branch / event | Conclusion |
|----------|----------------|------------|
| fleet-ci / fleet-security / CI/CD | PR `fix/reopen-issues-yaml-block-scalar` | **queued** at sample time |
| fleet-ci, fleet-security, CI/CD | `main` push `ad83a30` | **cancelled** |
| reopen-issues-closed-off-main.yml | `main` push `ad83a30` | **failure** |
| Dependabot graph / pip update | `main` / dynamic | **success** (not product test) |

`gh api /repos/tzervas/agentic-dev-boilerplate/rules/branches/main`: pull-request /
non-fast-forward / deletion rules present; **no required status checks** in the ruleset
payload. Auto-merge is intentionally unsafe here (fleet contract §6).

### 9. Open product signals

Open issues: **#1** schema detail in helpfile; **#2** pedagogic `.env` helptext.  
Open PRs at measure time: **#20** mypy bump; **#21** reopen-issues YAML fix (in flight).  
Source `TODO`: prompt template generation (`generate_boilerplate.py`).

## Known defects and gaps (do not fix in docs-only work)

1. **Hard dependency on unpublished `chngbrgr`** blocks `uv pip install -e .` / lock / sync.  
2. **Default template path on `main`** points at incomplete repo-root `templates/`; package-local
   templates are richer but unused for default path.  
3. **P28c `workflows` dict assumption** breaks unit fixtures that still use list-shaped
   `workflows`.  
4. **`slow` pytest marker** not declared in `pyproject.toml` → collection error without override.  
5. **Version / release drift:** tree `1.1.4` vs tag/PyPI `1.1.2`; authors field still placeholders.  
6. **Fleet CI on trunk** recently cancelled; not evidence of a green product gate.  
7. **`reopen-issues-closed-off-main`** reported **failure** on `main` (separate fix PR #21).  
8. Optional generation templates missing for several scripts/docs (warn-and-skip).  
9. **Semver policy debt:** 1.x line vs fleet **0.x.x until human says otherwise**.

## False or stale docs

| Document | Problem |
|----------|---------|
| [demo-validation.md](demo-validation.md) | Claims **12/12** `test-package.sh` passed and “Package is stable and ready.” **Measured: 3/12 failed suite.** |
| [README.md](../README.md) (pre-PM-suite) | “From PyPI (Recommended)” and full multi-agent / CI quality-gate narrative overstate what **current `main` source** can do; GPG-required commits, 80% coverage gate, etc. were not measured as active gates. |
| [user-guide.md](user-guide.md) / [api.md](api.md) | Install via `pip install -e .` and default generate examples do not match measured `main` install/generate failures. |
| [pyproject.toml] URLs | `Contributing` points at root `CONTRIBUTING.md` — **file missing** (guide is `docs/contributing.md`). |
| CI badge on README | SVG may show trunk workflow status; recent `main` product workflow conclusions were **cancelled**, not a clean pass story—read Actions history, not the badge alone. |

When in doubt, trust this file’s measurement block over narrative docs until re-measured.

## What still works for a careful user today

1. **Do not use this repo as the default new-project scaffold** — use
   [tz-forge](https://github.com/tzervas/tz-forge) `tz-new` (documented preference).  
2. **Published wheel 1.1.2** can still generate a default multi-agent instruction tree
   (verified in isolation).  
3. **Current tree + manual deps + `PYTHONPATH=src`** can run **bootdisk** generation and
   fleet-pack inject (verified).  
4. **Tmp manager tests** pass in isolation.  
5. Fleet standards content is vendored and copyable even when generation is partial.
