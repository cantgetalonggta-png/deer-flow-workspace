# Learned Knowledge Tree

Updated: 2026-10-10T13:43:47.390147Z

- Learned Knowledge
  - Cross-Domain Patterns
    - Skill progressive disclosure (metadata → body → resources)
    - Extension-first evaluation before core edits
    - Gateway as single LangGraph runtime + IM channels
    - skill_manage persistence vs sandbox write_file
    - Version lockstep: pyproject + package.json + helm chart
  - Known Gaps
    - Full monorepo not runnable in this sandbox without Docker + API keys
    - gog CLI not installed; Drive via connected tools only
    - Catalog has 4344 skills — need selective install, not bulk
    - Vercel deploy needs project binding and secrets
  - Abstractions
    - SuperAgent harness = lead agent + skills + subagents + sandbox + memory
    - Ontology: Skills ⊂ Capabilities, Tools ⊂ Actions, Plugins ⊂ Extensions
    - Knowledge graph: Skill --uses--> Tool --served_by--> Service --exposes--> API