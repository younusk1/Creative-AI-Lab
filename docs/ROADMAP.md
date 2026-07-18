# Roadmap

The roadmap favors completed, demonstrable workflows over adding tools quickly.

## v0.1 — Local creative workflow foundation

- [x] Define local-first, 16 GB laptop architecture.
- [x] Add Compose services for PostgreSQL, Adminer, Ollama, Open WebUI, and n8n.
- [x] Add setup, design, and decision documentation.
- [ ] Start the stack and pull `gemma2:2b`.
- [ ] Validate Open WebUI access to Ollama.
- [ ] Record the first prompt-quality experiment.

**Exit criterion:** A local user can chat with the selected model and save a simple creative-workflow record in the stack.

## v0.2 — Creative Brief workflow

- [ ] Define a structured creative brief schema.
- [ ] Build a Python workflow that turns a brief into campaign concept, messaging, visual direction, and initial prompts.
- [ ] Store prompt versions and workflow run metadata in PostgreSQL.
- [ ] Add basic tests for structured outputs.

**Exit criterion:** A brief produces a reproducible campaign-planning package.

## v0.3 — Storyboard and prompt library

- [ ] Add reusable prompt templates for image, video, copywriting, and presentations.
- [ ] Generate storyboards and shot lists from approved concepts.
- [ ] Document prompt evaluation criteria.
- [ ] Create the first campaign case study.

**Exit criterion:** One campaign folder demonstrates brief-to-storyboard traceability.

## v0.4 — Automation and review

- [ ] Create an n8n workflow for a controlled creative handoff.
- [ ] Add review checklist and approval status.
- [ ] Package campaign outputs for presentation.

**Exit criterion:** An approved brief can trigger a reviewable, auditable workflow.

## Later, only when justified

- Optional Metabase reporting.
- Local image-generation integration.
- Video and audio workflow integrations.
- Additional model comparisons.
- More specialized agents.
