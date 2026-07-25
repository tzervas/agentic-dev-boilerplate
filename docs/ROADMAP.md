# Roadmap

Planned and proposed work derived from **measured gaps**, open issues, source `TODO`s, and
fleet policy—not from invented dates or progress percentages. Items marked **proposed, not
committed** are suggestions from this docs pass, not an approved delivery plan.

## Guiding preference (already decided)

New product repositories should use **[tz-forge](https://github.com/tzervas/tz-forge) `tz-new`**,
not this generator, for fleet-aware scaffolds. This package remains for **schema-driven
multi-agent instruction/workflow emit** and legacy shapes. Roadmap items below are about
making *that* role honest and installable—not competing with tz-forge.

---

## P0 — Restore installability and truthful “works” paths

### R1. Unblock dependency resolution (`chngbrgr`)

- **What:** `pyproject.toml` requires `chngbrgr>=0.1.0`, which is **not on PyPI** (404), so
  `uv pip install -e .`, lock, and sync fail on current `main`.
- **Why it matters:** Source install is the documented developer path; CI and `test-package.sh`
  cannot honestly pass while the resolver is unsatisfiable.
- **Unblocks when:** Either publish `chngbrgr` to the index, pin a **git/rev** dependency that
  resolves, or drop/relax the hard dep (code already has optional import + fallback).
- **Evidence:** [CURRENT-STATE.md](CURRENT-STATE.md) install/lock output.

### R2. Fix default template search path (regression vs PyPI 1.1.2)

- **What:** `main` loads Jinja templates from repo-root `templates/`, which lacks
  `agent_planner_instructions.md.j2` and peers present under
  `src/agentic_dev_boilerplate/templates/`. Default generate aborts.
- **Why it matters:** Primary CLI example in README/user-guide is broken on HEAD.
- **Unblocks when:** Path resolution prefers package-local templates (1.1.2 behavior) and/or
  root `templates/` is completed and tested; dual trees for bootdisk stay intentional.
- **Evidence:** TemplateNotFound on generate; path diff in CURRENT-STATE.

### R3. Align tests with post-P28c schema shape

- **What:** Unit fixtures use list-shaped `workflows`; generator expects dict
  (`.get("fleet_standards")`). Marker `slow` undeclared → collection errors.
- **Why it matters:** Suite reports red for preventable fixture/config drift, hiding real
  regressions.
- **Unblocks when:** Fixtures match `project-schema.yaml` dict form; `pytest` markers registered;
  integration tests assert real template locations.
- **Evidence:** 16 failed / 25 passed; AttributeError and TemplateNotFound.

### R4. Make CI a real gate or stop implying it is one

- **What:** `main` has **zero required status checks**; recent fleet-ci/security/CI/CD on `main`
  were **cancelled**; badges can still look authoritative.
- **Why it matters:** Fleet contract §6 — auto-merge / “green” without required checks merges
  unverified work.
- **Unblocks when:** Product jobs complete on trunk; ruleset requires the **actual** check
  context names; docs/badges match measured status.
- **Related in-flight:** open PR **#21** (reopen-issues YAML).

---

## P1 — Product honesty and CLI completeness

### R5. Open issue #1 — schema detail in help

- **What:** Richer help / schema documentation for project schema fields.
- **Why:** Users cannot discover fleet_standards and agent role expectations from `--help` alone.
- **Unblocks when:** Help or linked schema reference implemented; examples re-run on fixed
  generate path.

### R6. Open issue #2 — pedagogic `.env` helptext

- **What:** Intuitive documentation for environment variables if/when used by scripts.
- **Why:** Reduces footguns for generated projects and local scripts.
- **Unblocks when:** Actual env vars are inventoried from code (not invented) and documented.

### R7. Implement or delete prompt template generation

- **What:** `generate_prompts` is a TODO stub (“Skipping prompt templates”).
- **Why:** README multi-agent narrative implies more complete generation than exists.
- **Unblocks when:** Templates + tests land, **or** docs/CLI permanently mark the feature absent.
- **Status:** proposed if keeping feature; otherwise documentation-only closure is enough.

### R8. Optional templates currently warn-and-skip

- **What:** Missing `script_create_pr_local.py.j2`, `plan_template.md.j2`, `CONTRIBUTING.md.j2`, etc.
- **Why:** Generated trees are incomplete vs marketing language.
- **Unblocks when:** Templates added per template family, or generator stops advertising those files.

---

## P2 — Fleet / version policy

### R9. Semver and release alignment (human-gated)

- **What:** Tree at `1.1.4`, tags/release/PyPI at `1.1.2`, fleet policy prefers **0.x.x until a
  human authorizes 1.x**.
- **Why:** Version number implies maturity and registry state that are out of sync.
- **Unblocks when:** A human decides: stay on 1.x with honest changelog + publish, or renumber
  under `major_version_zero` with explicit authorization. **Agents must not cut 1.x.x policy
  changes as “done” without that human call.**

### R10. Publish cadence for generator + fleet pack

- **What:** Fleet-pack inject and `--template` exist on `main` but not on PyPI 1.1.2.
- **Why:** “pip install” users get an older generator without fleet injection.
- **Unblocks when:** R1–R3 green, then a deliberate registry publish (batch, not every merge).

### R11. Finish or archive long-term memory design

- **What:** [LONG_TERM_MEMORY.md](LONG_TERM_MEMORY.md) describes embeddenator-backed LTM; no code.
- **Why:** Design docs without status labels become believed features.
- **Unblocks when:** Implementation project exists, **or** doc marked deferred with no ship claim.
- **Status:** proposed, not committed.

---

## P3 — Quality and maintainability

### R12. Lint/format debt

- **What:** black would reformat 2 files; flake8 reported issues (unused imports, line length).
- **Unblocks when:** Format/lint applied in a non-docs PR with CI enforcement that actually runs.

### R13. Multi-agent solver packaging

- **What:** `multi_agent_solver.py` fails as `__main__` with relative import error; README still
  shows orchestrated sessions as a primary workflow.
- **Unblocks when:** Console script entry or absolute imports + a smoke test, **or** demote to
  experimental in front-matter docs (front docs already should not over-claim).

### R14. Placeholder package metadata

- **What:** authors/maintainers still `Your Name <your.email@example.com>`.
- **Unblocks when:** Real maintainer metadata in a packaging PR.

### R15. Root `CONTRIBUTING.md` link

- **What:** `pyproject.toml` `[project.urls] Contributing` points at missing root file.
- **Unblocks when:** Add root file or fix URL to `docs/contributing.md`.

---

## Explicitly out of scope for this docs PR

- Code, workflow, lockfile, or version bumps (docs-only constraint).
- Auto-merge arming (no required checks).
- Building tz-forge feature parity here.

## How to refresh this roadmap

1. Re-run the measurement commands in [CURRENT-STATE.md](CURRENT-STATE.md).  
2. Refresh open issues/PRs with `gh issue list` / `gh pr list` (no `gh search`).  
3. Move items only when evidence changes—not when optimism does.
