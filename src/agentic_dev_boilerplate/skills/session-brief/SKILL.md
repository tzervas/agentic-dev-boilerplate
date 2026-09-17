---
name: session-brief
description: Start every development session with a filled SESSION contract (repo, branch, one-sentence goal, in_scope paths, done_when command). Use at chat start, after a context reset, or when the user has not named a slice. Do not use for vision documents.
license: MIT
metadata:
  source: tzervas/house-pack
  compatibility: grok, copilot, claude, adk
---

# Session brief

Require this contract before planning or editing. If the user did not fill it, ask for the missing fields. Do not invent a vision document to compensate.

```text
repo: tzervas/<name>
branch: <type>/<slug>
goal: <one sentence>
in_scope: <paths>
out_of_scope: new deps, new architecture, new repo, Rust port, README rewrite
done_when: <exact command>
reuse_first: searched <repos> for <thing>
do_not: append diaries to AGENTS.md; regenerate .github/agents
first_action: read PERSONAL.md + AGENTS.md + in_scope files, then run the slice check
```

## Rules

- One goal. Named paths. A command that means done.
- Truth order: STATUS / lockfile / src → docs/decisions → README.
- End of session: one line in `docs/decisions/YYYY-MM-DD.md` and a next-task stub.
- PERSONAL.md is human-authored. Do not rewrite it.
