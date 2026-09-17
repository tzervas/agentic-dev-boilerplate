---
name: local-gate
description: Run the repository's own lint, format, and test commands so local and CI mean the same thing. Use before claiming work is done, before commit, and when CI disagrees with a laptop. Prefer scripts/check.sh when present.
license: MIT
---

# Local gate

Replaces most of the Copilot `tester` persona. Tests are the gate, not a role.

## Command preference

```bash
# 1. repo-declared
./scripts/check.sh --quick
./scripts/check.sh

# 2. Python house-rules
uv run ruff check .
uv run ruff format --check .
uv run pytest -q

# 3. Rust house-rules
cargo fmt --all --check
cargo clippy --all-targets --all-features -- -D warnings
cargo test --all-features
```

## Rules

- Collect `test_*.py`. Never use pytest `python_files` as an allow-list.
- Skipped CI is not success.
- Local command must match CI. If they diverge, that is the bug.
- One finding per fix cycle when adopting a linter.

## Output

```text
gate: <command>
result: pass | fail
first_failure: <file:line or none>
```
