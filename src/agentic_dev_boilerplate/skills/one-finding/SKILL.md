---
name: one-finding
description: Land exactly one concern per PR — one file when possible, one gate failure when adopting a linter. Use when the user or agent starts bundling lint, docs, and a feature in one diff. Encodes autodev-public house-rules adoption.one_finding_per_pr.
license: MIT
---

# One finding per PR

A batch of 86 ruff findings handed to an implementer produces a 3000-line
diff nobody can review. One finding produces a PR a reviewer can judge.

## Rule

1. Identify the first failing gate (toolchain-config → ci-workflow →
   gate-parity → lint-clean → format-clean → type-clean → test-present).
2. Change the minimum that makes that one failure green.
3. Open or update one PR. `Refs #n` on feature/dev.
4. Stop. Do not "while we're here" the next 85.

## Do not

- Mix a feature with a style sweep.
- Disable a rule to swallow the rest.
- Close the issue because half the files were touched.
