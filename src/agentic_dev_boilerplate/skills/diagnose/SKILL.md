---
name: diagnose
description: Debug a failing test, lint finding, or CI job. Use when a command returned non-zero or a test assertion failed. Do not use for greenfield design.
license: MIT
---

# Diagnose a failure

Replaces the Copilot `debugger` encyclopedia.

## Steps

1. Capture the exact command and the first failure. Ignore later noise.
2. Open the test or lint target named in that failure.
3. Form one hypothesis. Change one thing.
4. Re-run only the failing node.
5. If it still fails, write what you ruled out. Do not restart from architecture.

## Do not

- Disable the test to go green.
- Broaden ruff/clippy ignores without a documented reason.
- Treat a skipped workflow as passing.
