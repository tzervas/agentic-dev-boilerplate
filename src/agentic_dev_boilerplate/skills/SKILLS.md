# Skills index (L1 catalog)

Not a spec file. The spec file is `SKILL.md` inside each directory
(https://agentskills.io/specification, ADK 1.25+/2.x).

| name | when to load |
|---|---|
| session-brief | start of every development chat |
| plan-slice | break a goal into one in-scope change |
| implement-change | write or edit code in named paths |
| local-gate | run the repo's own tests / linters |
| diagnose | a test or CI job failed |
| security-review | secrets, auth, SAST, accepted findings |
| ship-check | before opening or merging a PR |
| commit-prep | format, test, write the commit message |

Load on demand. Do not paste every skill into the system prompt.
