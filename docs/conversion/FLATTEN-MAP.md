# Flatten map — Copilot personas → ADK skills

Do not 1:1 map 16 `.agent.md` files to 16 ADK LlmAgents.

| Old Copilot persona | New surface |
|---|---|
| planner, project-manager, orchestrator | session-brief + plan-slice + one ADK root_agent |
| software-engineer, backend, frontend, fullstack, api, mobile | implement-change |
| tester | local-gate |
| debugger | diagnose |
| security | security-review |
| deployer, devops-specialist | ship-check |
| ai-engineer, ml-engineer, data-scientist | tz-forge skills-ml — do not copy |
| systems-engineer (IOMMU/VFIO) | fleet / autodev, not an ADK unit |

Workflow skills (house-rules that agents ignore):

| Skill | Rule |
|---|---|
| one-finding | one file / one gate failure per PR |
| reuse-first | search siblings before scaffolding |
| claim-gate | STATUS / lockfile / tests beat README |
| commit-prep | format + test + conventional commit with Refs/Closes |

ADK 2.x Workflow (Sequential/Parallel/Loop) replaces orchestrator.agent.md.
