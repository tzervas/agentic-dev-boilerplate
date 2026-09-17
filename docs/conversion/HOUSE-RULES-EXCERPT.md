# House rules excerpt (from autodev-public config/house-rules.json)

Python: uv + pyproject.toml + uv.lock. Lint/format = ruff (E,F,W,I,UP,B,SIM,RUF) + ruff format.
Types = mypy (recommended, not required on day one). Test = `uv run pytest -q`.
Never bare pytest (src-layout imports fail). Collect test_*.py; do not allow-list-omit.

Rust: cargo + Cargo.lock + rust-toolchain.toml. clippy --all-targets --all-features -- -D warnings.
rustfmt --check. cargo test --all-features.

CI: self-hosted linux/x64/podman. Guard on github.repository_owner, never github.server_url.
Use github.api_url, never hardcode the public TLS edge. Token = secrets.GITHUB_TOKEN.
Parity required: local check.sh ≈ CI command.

Adoption: fail-fast, one_finding_per_pr. Order: toolchain-config → ci-workflow → gate-parity
→ lint-clean → format-clean → type-clean → test-present.

Branch/PR: never push a trunk. Conventional commits. WHY in the message.
Secrets via `secret exec VAR=name -- cmd`. Every file has the right extension.
