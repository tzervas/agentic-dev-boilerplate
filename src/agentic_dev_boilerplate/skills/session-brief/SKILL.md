---
name: session-brief
description: Start every development session with a filled SESSION contract (repo, branch, one-sentence goal, in_scope paths, done_when command). Use at chat start, after a context reset, or when the user has not named a slice. Do not use for vision documents.
license: MIT
---

# Session brief

Require this contract before planning or editing.

```text
repo: tzervas/<name>
branch: <type>/<slug>
goal: <one sentence>
in_scope: <paths>
out_of_scope: new deps, new architecture, new repo, Rust port
done_when: <exact command>
reuse_first: searched <repos> for <thing>
do_not: append diaries to AGENTS.md; regenerate .github/agents
```

PERSONAL.md is human-authored. Do not rewrite it.
