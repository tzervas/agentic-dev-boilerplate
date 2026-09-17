#!/usr/bin/env bash
# Local gate. Must match CI. From autodev-public house-rules.json.
set -euo pipefail
QUICK=0
if [[ "${1:-}" == "--quick" ]]; then
  QUICK=1
fi
uv run ruff check .
uv run ruff format --check .
if [[ $QUICK -eq 0 ]]; then
  uv run pytest -q
fi
echo "python gate ok"
