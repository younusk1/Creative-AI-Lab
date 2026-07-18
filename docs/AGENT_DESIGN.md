# Agent Design

## Design principle

Creative AI Lab uses focused, reviewable workflows. “Agent” refers to a bounded capability with a clear goal, defined tools, structured output, and a human approval point—not an unrestricted autonomous actor.

## v0.2: Creative Brief Assistant

| Item | Design |
| --- | --- |
| Purpose | Convert a creator's brief into a structured campaign-planning draft. |
| Inputs | Objective, audience, channel, tone, mandatory messages, constraints. |
| Outputs | Campaign concept, key message, visual direction, draft deliverables, assumptions, and initial prompts. |
| Model | Gemma 2 2B through Ollama. |
| Tools | Prompt template, output schema, optional PostgreSQL persistence. |
| Human checkpoint | Approve or revise campaign direction before downstream generation. |
| Failure handling | Return missing-information questions or clearly label assumptions; never invent brand facts. |

## v0.3: Prompt and Storyboard Assistant

| Item | Design |
| --- | --- |
| Purpose | Create reusable image, video, copy, and storyboard prompts from an approved concept. |
| Inputs | Approved campaign concept, visual style, channel, aspect ratio, brand constraints. |
| Outputs | Versioned prompts, shot list, scene descriptions, negative constraints, and review checklist. |
| Tools | Prompt library and structured templates. |
| Human checkpoint | Validate brand fit and practical production feasibility. |
| Failure handling | Flag ambiguity and produce alternatives rather than silently selecting a visual direction. |

## Later: Creative Review Assistant

This capability will compare planned deliverables against a brief and checklist. It may flag missing messages, inconsistent format, or unaddressed constraints, but a human remains accountable for final quality, safety, and brand approval.

## Non-goals for v0.1

- Autonomous browser or desktop control.
- Unsupervised external publishing.
- Automatic claims of legal, brand, or cultural compliance.
- Multi-agent orchestration without a demonstrated workflow need.
