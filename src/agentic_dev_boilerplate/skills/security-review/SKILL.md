---
name: security-review
description: Review a diff for secrets, unsafe subprocesses, auth gaps, and unannotated scanner findings. Use on PRs, before merge, and when adding network or credential handling. Do not use as a general code-style review.
license: MIT
---

# Security review

Canonical policy: `autodev-public/config/security-policy.json`.

## Severity

- CRITICAL / HIGH: must fix. No annotation path.
- MEDIUM: fix for release unless architecturally unreachable, then `SEC-ACCEPTED`.
- LOW: acceptable day to day; annotate if kept.

Annotation requires `SEVERITY`, `REACHABLE`, `REVISIT`. REACHABLE is an architecture claim, not "the code is careful."

## Look for

- Secrets, tokens, or credentials in files, logs, argv, or URLs
- Subprocess + shell with untrusted input
- Missing auth on new endpoints
- Scanner reported absent treated as clean

## Scanners (when installed)

- gitleaks (any finding is critical)
- ruff `S` (Python bandit rules)
- cargo-audit on Rust
- osv-scanner on lockfiles

A missing scanner is reported absent. It is not a pass.
