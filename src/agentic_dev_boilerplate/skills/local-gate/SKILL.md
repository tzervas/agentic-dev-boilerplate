---
name: local-gate
description: Run the repository's own lint, format, and test commands so local and CI mean the same thing. Use before claiming work is done, before commit, and when CI disagrees with a laptop. Prefer scripts/check.sh when present.
license: MIT
---

# Local gate

```bash
./scripts/check.sh
uv run ruff check . && uv run ruff format --check . && uv run pytest -q
cargo clippy --all-targets --all-features -- -D warnings && cargo test --all-features
```

Collect test_*.py. Never use python_files as an allow-list. Skipped CI is not success.
