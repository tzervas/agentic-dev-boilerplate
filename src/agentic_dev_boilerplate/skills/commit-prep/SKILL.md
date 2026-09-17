---
name: commit-prep
description: Prepare a commit by running the local gate and drafting a conventional commit message that explains why. Use when the user is ready to commit or asks for a commit message. Do not commit unless asked.
license: MIT
metadata:
  source: tz-forge/modules/agents/skills-generic/commit-prep
---

# Commit preparation

## Steps

1. `git status` and `git diff`
2. Run `./scripts/check.sh` or the local-gate skill
3. Stage named paths only
4. Draft the message:

```text
type(scope): summary

Why this change exists. Name the failure that motivated it.

Refs #n
```

`Refs #n` on feature/dev. `Closes #n` / `Fixes #n` only on delivery to main.

## Do not

- `git add .` when artifacts or secrets may be present
- Commit to `main`
- Use subject "WIP" / "update" / "fixes"
