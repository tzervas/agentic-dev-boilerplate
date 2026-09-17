# PERSONAL.md — Tyler Zervas standing invariants

Human-authored. Load once per session. Do not paste repo history here.
Canonical copy: `tzervas/house-pack`. Last reviewed: 2026-09-17.

Machine gates live in `autodev-public/config/house-rules.json`.
This file is the diet. Do not regenerate it. Tyler edits it.

## Stack defaults

- Python: `uv` + hatchling. Never suggest pip / pipenv / poetry unless asked.
- Python gate: `uv run ruff check .` · `uv run ruff format --check .` · `uv run pytest -q`
- Ruff select: `E,F,W,I,UP,B,SIM,RUF`. Do not add flake8/black/isort.
- Rust: `rust-toolchain.toml` + `Cargo.lock` + `rustfmt.toml`.
- New product repos: `tz-forge` `tz-new`, then stamp house-pack. Not this generator.

## Language split

- Python first for prototypes, agents, glue.
- Rust only after the Python path is proven, or when the repo is already Rust.
- Do not propose a Rust port mid-session because "Rust is safer."

## Engineering bar

- No secrets in commits, logs, prompts, argv, or URLs.
- Tests are the gate. Skipped CI is not success.
- One finding per PR.
- Truth order: STATUS / decisions → lockfile → src → README last.
- Never push trunk. Feature → `Refs #n`. Main → `Closes #n`.
- Search this repo and siblings before scaffolding.
- Do not append diaries to AGENTS.md.
