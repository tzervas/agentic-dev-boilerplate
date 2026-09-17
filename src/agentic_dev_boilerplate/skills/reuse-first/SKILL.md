---
name: reuse-first
description: Search this repo and named sibling surfaces before scaffolding a new module, agent forest, or template. Use at the start of any "we should have a standard for X" request. Prevents product 309.
license: MIT
---

# Reuse first

Named siblings (search before inventing):

| Surface | Job |
|---|---|
| tz-forge + tz-new | Birth product repos |
| house-pack | Diet overlay (PERSONAL / SESSION / thin AGENTS) |
| autodev-public house-rules.json | Machine gates |
| tz-forge skills-generic | Shared SKILL.md (commit-prep, pr-review, fleet-gap) |
| this repo skills/ | ADK + Copilot/Grok/Claude discovery |
| CogSynDelta / memory-gate | Live product patterns, not templates |
| python-adk-mcp-uv-template | ADK+MCP product template (bump pin separately) |
| agent-workflows g-job-brief | SESSION sibling; do not load PLAYBOOK.md |

## Steps

1. `rg` this repo for the thing.
2. Check the table above.
3. If it exists, stamp or vendor. Do not rewrite.
4. Only then propose a new file, and only inside SESSION in_scope.

## Do not

- Create a new GitHub repo to hold a markdown file.
- Copy csd-ops into .grok, .codex, and .agents as three bodies.
- Merge house-pack into tz-forge "while converting this repo."
