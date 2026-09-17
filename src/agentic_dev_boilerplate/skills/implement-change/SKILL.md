---
name: implement-change
description: Edit or add code only in SESSION in_scope paths. Use when implementing a planned slice, fixing a test, or writing a small feature. Do not use to invent a new package layout or port Python to Rust.
license: MIT
---

# Implement a change

Replaces Copilot `software-engineer`, `backend-developer`, `frontend-developer`, `fullstack-developer`, `api-developer`, `mobile-developer` personas. Those were role prompts, not capabilities.

## Steps

1. Confirm `in_scope`. If the edit is outside it, stop and say so.
2. Read the existing files. Match their style. Do not reformat the world.
3. Change the minimum. One concern.
4. Run the slice check from `done_when` or the local-gate skill.
5. If the gate fails, load `diagnose`. Do not expand scope to silence it.

## Language defaults (house-rules)

- Python: `uv`, hatchling, ruff `E,F,W,I,UP,B,SIM,RUF`. No black/isort/flake8.
- Rust: `cargo fmt`, `clippy -D warnings`, committed lock + `rust-toolchain.toml`.
- New files keep the extension that matches their shebang.

## Do not

- Add a dependency without a one-line justification.
- Create `.github/agents/*.agent.md`.
- Rewrite AGENTS.md as a diary.
