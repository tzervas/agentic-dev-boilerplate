# Development path

How `agentic-dev-boilerplate` got to its current shape. Reconstructed from git history,
merged PRs, tags/releases, and in-repo design notes. Where a claim is inference rather
than a direct citation, it is marked.

## Origin (2025-12)

| Evidence | What landed |
|----------|-------------|
| `49552cf` *Initial commit: Templatized agentic development boilerplate* | Schema-driven generator idea: YAML project schema → agent instructions, workflows, scripts via Jinja2 |
| `7cef5ec` *Add solid agentic guardrails… /tmp directories* | Workspace tmp layout and pruning as first-class tooling |
| `c35a000` *Refactor into installable Python package with src layout* | Package form: `src/agentic_dev_boilerplate/`, console entry `agentic-dev-boilerplate` |
| `beb264d` / tags `v1.1.0`–`v1.1.1` | Packaging, tests, Docker test harness, UV lockfile era |

Early product identity: **a multi-agent development boilerplate generator** aimed at
GitHub Copilot-style instruction files, PR automation, and task tracking—not a general
application framework.

## Version line and packaging choices

- Tags present: `v1.1.0`, `v1.1.1`, `v1.1.2` (only `v1.1.2` is a GitHub Release).
- PyPI publishes **`agentic-dev-boilerplate==1.1.2`** (measured 2026-07-25 via
  `https://pypi.org/pypi/agentic-dev-boilerplate/json`).
- Repo `pyproject.toml` reports **`version = "1.1.4"`** (no matching tag/release at
  measurement). Under fleet policy, repos stay **0.x.x until a human authorizes 1.x.x**
  (operator `BRANCH-AND-RELEASE-CONTRACT` §3). This repo is already on a 1.x line
  historically; treating that as a **policy debt** item rather than rewriting history in
  this docs-only change.

**Inferred:** the 1.x numbering predated fleet-wide `major_version_zero` discipline and was
not walked back when fleet standards landed.

## Multi-agent surface and Copilot alignment

| Evidence | Decision |
|----------|----------|
| `650e4d5`, `cfed88b` / PR **#4** *align all agent files with official GitHub Copilot schema* | Agent instruction and handoff shapes aligned to Copilot customizations |
| Agent role expansion in schema + templates | Roles beyond the original planner/tester/debugger set (software-engineer, ai-engineer, security, …) |

**Rejected / deferred (evidence in code, not a formal ADR):** prompt template generation
is still a stub (`generate_prompts` → “Skipping prompt templates (not implemented)…” and a
`TODO` in `generate_boilerplate.py`).

## Bootdisk template (late 2025-12)

| Evidence | Decision |
|----------|----------|
| `445a590` *feat: add bootdisk-agentic-structure template* | Second template family under `templates/bootdisk-agentic-structure/` |
| `2f76bec` *feat: implement bootdisk agentic structure template* | Wire-through in generator (`--template` / role map for swe + test_engineer) |
| PR **#3** (merged to `dev`) *Optimize Copilot Customizations…* | Bootdisk / Copilot optimization path existed on a `dev` integration branch |

**Trade-off (inferred from dual template trees):** keep a “default” multi-agent instruction
set and a more product-shaped bootdisk layout rather than forcing one structure.

## Changelog extraction (`chngbrgr`)

| Evidence | Decision |
|----------|----------|
| `231b9c1` *feat: integrate chngbrgr changelog generator* | Optional import of `ChangelogGenerator`; fallback if missing |
| CHANGELOG / design notes | Standalone package at `tzervas/chngbrgr` |

Hard dependency `chngbrgr>=0.1.0` was added to `pyproject.toml` while the generator still
tolerates ImportError at runtime. **Measured later:** `chngbrgr` is **not on PyPI** (HTTP
404), so source install via the lock/resolver fails. See [CURRENT-STATE.md](CURRENT-STATE.md).

## Fleet integration (2026-07) — the strategic turn

This is the largest product decision after packaging: **stop treating this generator as the
default way to create new fleet product repos.**

| Evidence | Decision |
|----------|----------|
| PR **#13** `feat/self-hosted-podman-fleet` | CI jobs use `[self-hosted, linux, x64, podman]` |
| `de1050f` *ci: convert workflows to workflow_dispatch-only* then PR **#13** restores push/PR on primary CI | Manual-only experiment, then fleet routing with real triggers |
| PR **#14** / **#16** *P26 fleet standards* | Badges, issue close-on-main policy, fleet-security/ci pack application |
| PR **#15** *P28c prefer tz-new; inject fleet pack* (`da5a573`) | Document **tz-forge `tz-new` as preferred**; when this generator still emits CI, inject vendored `pack/fleet-standards` / package `fleet_pack` via `--fleet-pack` (default on) and `workflows.fleet_standards` |
| `AGENTS.md` | Same preference table for AI assistants |

**Alternatives rejected (stated in PR #15 body and README):**

| Alternative | Why not for new product repos |
|-------------|-------------------------------|
| Keep this generator as primary scaffold | Fleet kinds, assistant profiles, and modules live in **tz-forge** |
| Always fail if fleet pack missing | Soft-fail + shell-out note so generation still completes |
| Emit only legacy workflows | Inject fleet CI/security + issue close/reopen so new trees match workstation standards |

Related pointers: [FLEET_STANDARDS.md](FLEET_STANDARDS.md),
[tz-forge](https://github.com/tzervas/tz-forge).

## Template path change (regression vector)

PyPI **1.1.2** resolves templates as:

```text
Path(__file__).parent / "templates"   # package-local
```

Current `main` (`ad83a30`) resolves:

```text
Path(__file__).parent.parent.parent / "templates"[/template_type]
```

i.e. **repository-root** `templates/`, not the fuller set under
`src/agentic_dev_boilerplate/templates/`.

**Inferred from code + measurement (not a documented ADR):** bootdisk support and dual trees
required a repo-root path; the root `templates/` tree was never completed to match the
package-local agent templates, so **default** generation on current `main` fails while
**bootdisk** can succeed. Details and commands: [CURRENT-STATE.md](CURRENT-STATE.md).

## Dependency maintenance

Merged Dependabot PRs on `main` (examples): **#5–#6** (Sphinx), **#10–#12**, **#17–#19**
(pytest, black, click, …). These keep the declared pins moving but do not by themselves
restore installability when a hard dep is unpublished.

## Design that was written but not shipped

| Doc / commit | Status at measurement |
|--------------|------------------------|
| [LONG_TERM_MEMORY.md](LONG_TERM_MEMORY.md); commit `b45202f` | Design only — no `long_term_memory/` package tree on `main` |
| `tasking/tracker.yaml` | Empty task list (`tasks: []`) |
| Prompt generation TODO | Still unimplemented |

## Timeline (compressed)

```text
2025-12  Initial generator → package → tmp manager → v1.1.x tags / PyPI 1.1.2
2025-12  Bootdisk template + Copilot schema alignment (#3/#4)
2025-12  chngbrgr integration (optional import, hard dep in pyproject)
2026-07  Self-hosted fleet CI (#13), P26 standards (#14/#16), P28c tz-new + fleet pack (#15)
2026-07  Dependabot bumps (#17–#19); HEAD 1.1.4 untagged
```

## How to extend this history

Prefer new evidence from merged PRs and commits over README archaeology. When behavior
changes, update [CURRENT-STATE.md](CURRENT-STATE.md) with a re-measurement, not only this
narrative.
