---
name: implement-change
description: Edit or add code only in SESSION in_scope paths. Use when implementing a planned slice, fixing a test, or writing a small feature. Do not use to invent a new package layout or port Python to Rust.
license: MIT
---

# Implement a change

1. Stay inside in_scope.
2. Match existing style. Minimum diff.
3. Run done_when or local-gate.
4. On failure load diagnose. Do not expand scope.

Python: uv + ruff E,F,W,I,UP,B,SIM,RUF. Rust: clippy -D warnings.
