# Learning Journal

This is a concise, dated record of implementation lessons, experiments, and next steps. It is not a polished case study; completed campaign write-ups will live under `campaigns/`.

## 2026-07-13 — v0.1 foundation

**Focus:** Define a local-first Creative AI Lab that works on a 16 GB laptop.

**Decisions made:**

- Use Docker Compose for PostgreSQL, Adminer, Ollama, Open WebUI, and n8n.
- Start with one local model: Gemma 2 2B Instruct.
- Design around creative production stages rather than a collection of autonomous agents.
- Keep Metabase optional because it adds meaningful memory usage.

**Next:** Start the stack, pull the model, and validate a basic creative-brief prompt in Open WebUI.
