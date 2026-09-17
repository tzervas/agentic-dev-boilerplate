---
name: ship-check
description: Pre-PR and pre-merge checklist. Use before opening a pull request, before merging to main, and when asking "is this ready." Do not use as a substitute for local-gate.
license: MIT
---

# Ship check

Replaces Copilot `deployer` / `devops-specialist` as a standing persona.
CI and deploy stay in fleet workflows / autodev. This skill is the human/agent checklist.

## Before opening a PR

- [ ] `local-gate` passed on this branch
- [ ] Diff is one concern
- [ ] No secrets
- [ ] Conventional commit that names the failure that motivated the change
- [ ] Feature → `dev`: `Refs #n`. Delivery → `main`: `Closes #n`
- [ ] SESSION `done_when` command is green
- [ ] One line appended to `docs/decisions/`

## Do not

- Request automatic Copilot review
- Merge your own PR unless asked
- Push trunk
- Treat skipped jobs as green
