# Architecture Decisions

This log captures significant choices and their trade-offs. New entries should include a date, status, context, decision, and consequences.

## ADR-001: Use a local-first Compose stack

- **Date:** 2026-07-13
- **Status:** Accepted
- **Context:** The project needs low recurring cost, reproducibility, and room to learn agentic workflows without cloud infrastructure.
- **Decision:** Use Docker Compose to run PostgreSQL, Adminer, Ollama, Open WebUI, and n8n locally.
- **Consequences:** The environment is portable and private by default, but model performance is constrained by laptop hardware.

## ADR-002: Start with one local model

- **Date:** 2026-07-13
- **Status:** Accepted
- **Context:** Disk space and 16 GB RAM make a multi-model lab counterproductive at the outset.
- **Decision:** Start with Qwen 2.5 3B Instruct as the only local model.
- **Consequences:** The platform stays responsive enough for iterative work. Output quality will not equal larger models, so human review and structured workflows are important.

## ADR-003: Prioritize creative workflows over autonomous agents

- **Date:** 2026-07-13
- **Status:** Accepted
- **Context:** The portfolio should demonstrate AI-assisted creative production, not complexity for its own sake.
- **Decision:** Model the system around creative-brief, planning, prompting, storyboard, review, and packaging stages. Agents remain implementation details.
- **Consequences:** Early features are easier to test, explain, and demonstrate. Multi-agent patterns can be introduced later when a specific workflow needs them.

## ADR-004: Make Metabase optional

- **Date:** 2026-07-13
- **Status:** Accepted
- **Context:** Metabase is useful for reporting but consumes more memory than the core workflow services.
- **Decision:** Do not include Metabase in the default Compose file. Document it as a future optional component.
- **Consequences:** v0.1 remains lean. Reporting can be added when there is meaningful workflow data to visualize.
