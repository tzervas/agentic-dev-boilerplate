---
name: plan-slice
description: Turn a goal into one in-scope change with a done_when command. Use when the user asks to plan, decompose, roadmap, or "figure out the approach" before coding. Do not open a new architecture.
license: MIT
---

# Plan a slice

Replaces the Copilot `planner` / `project-manager` / `orchestrator` encyclopedias.

## Steps

1. Read SESSION.md / the session-brief skill. Refuse to plan without `in_scope` and `done_when`.
2. Search this repo, then named siblings (tz-forge, house-pack, autodev-public), before proposing new files.
3. Write a plan that is at most one PR:
   - files that will change
   - files that will not change
   - the exact command that proves done
   - the first action
4. Stop. Do not implement until the user says so, unless the goal was "just fix it."

## Output

```text
slice: <one sentence>
files: <paths>
out: <paths not touched>
prove: <command>
first: <command or file to open>
risk: <one line or "none">
```

## Do not

- Produce a multi-sprint roadmap for a one-test fix.
- Spawn extra agents for roles that are now skills.
- Treat README claims as measured results.
