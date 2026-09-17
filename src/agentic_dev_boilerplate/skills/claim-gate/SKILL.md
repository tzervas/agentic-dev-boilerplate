---
name: claim-gate
description: Treat STATUS.md, lockfiles, and tests as truth; treat README as marketing-adjacent. Use when docs claim a version, a 10x, a protocol, or "production-ready" that source does not prove. CogSynDelta scar - Python 3.14 badge vs pyproject >=3.12,<3.14.
license: MIT
---

# Claim gate

Truth order (do not invert):

1. STATUS.md / docs/session-handoff.md / latest docs/decisions/
2. pyproject.toml + uv.lock or Cargo.toml + rust-toolchain.toml
3. Live source in SESSION in_scope
4. docs/decisions/ and Tero ids
5. README last

## Flag

- Version floors that contradict requires-python / rust-toolchain
- Unsubstantiated 10x, quantum, VL-JEPA, production-ready
- "CI is green" when the job was skipped
- Agent-invented toolchain pins

Tag claims `[CONFIRMED]`, `[INFERRED]`, or `[UNVERIFIED]`.
Do not amplify a README claim you did not measure.
