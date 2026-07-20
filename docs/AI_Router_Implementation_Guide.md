# AI Router Implementation Guide

**Project:** Creative AI Lab\
**Version:** 1.0\
**Status:** Planning & Initial Implementation

---

# 1. Purpose

This document provides the implementation roadmap for building the **AI
Router**, a lightweight orchestration layer that intelligently routes
requests between:

- **Gemma 2:2B (Ollama)** --- Local, fast, inexpensive workhorse
- **Gemini** --- Cloud-based model used only for tasks that justify
  additional capability

This guide intentionally avoids introducing orchestration frameworks
such as LangChain or LangGraph during the initial implementation. The
goal is to understand and control every component of the system before
introducing abstraction layers.

---

# 2. Objectives

The AI Router should:

- Route every request through a single entry point.
- Decide which model should handle the request.
- Keep the routing logic transparent and easy to modify.
- Log every decision.
- Be reusable across future AI projects.
- Integrate cleanly with Docker, Ollama, Gemini CLI, and later n8n.

---

# 3. Guiding Principles

1.  Keep the architecture simple.
2.  Keep responsibilities separated.
3.  Prefer explicit code over framework magic.
4.  Optimize for maintainability rather than cleverness.
5.  Introduce additional frameworks only when they solve a real problem.

---

# 4. High-Level Architecture

```text
                User
                  │
                  ▼
           ai_router.py
                  │
        ┌─────────┴─────────┐
        │                   │
        ▼                   ▼
Gemma (Local)          Gemini (Cloud)
        │                   │
        └─────────┬─────────┘
                  ▼
            Final Response
```

The router is the only component that knows about both models. Neither
model should know the other exists.

---

# 5. Project Structure

```text
Creative-AI-Lab/
├── ai-router/
│   ├── config.py
│   ├── router.py
│   ├── decision.py
│   ├── gemma.py
│   ├── gemini.py
│   ├── logger.py
│   ├── utils.py
│   ├── requirements.txt
│   ├── README.md
│   ├── tests/
│   ├── logs/
│   └── prompts/
```

---

# 6. Component Responsibilities

## router.py

- Accept user requests
- Call the Decision Engine
- Invoke the selected model
- Return the final response
- Record logs

## decision.py

- Inspect the request
- Estimate complexity
- Choose Gemma or Gemini
- Explain the routing decision

## gemma.py

- Communicate with Ollama
- Execute local prompts
- Handle Gemma-specific errors

## gemini.py

- Execute Gemini CLI
- Handle cloud-related errors

## config.py

Store model names, thresholds, timeouts, log paths, and retry settings.

## logger.py

Record routing decisions, timing, errors, and debug information.

## utils.py

Reusable helpers such as token estimation, MIME detection, chunking, and
prompt cleaning.

---

# 7. Request Lifecycle

```text
Receive Request
      ↓
Analyse Request
      ↓
Decision Engine
      ↓
Select Model
      ↓
Execute Model
      ↓
Return Response
      ↓
Log Decision
```

---

# 8. Initial Routing Rules

Condition Model

---

Image input Gemini
OCR required Gemini
Very large document Gemini
Long-context preprocessing Gemini
Everything else Gemma

---

# 9. Logging Strategy

Capture:

- Timestamp
- Prompt length
- Estimated tokens
- Selected model
- Routing reason
- Execution time
- Status

---

# 10. Milestones

1.  Create project structure.
2.  Verify Python → Docker → Ollama → Gemma.
3.  Verify Python → Gemini CLI.
4.  Build a Gemma-only router.
5.  Add Gemini support.
6.  Implement routing logic.
7.  Add logging.
8.  Support additional file types.
9.  Integrate with n8n.
10. Introduce LangGraph when stateful orchestration becomes necessary.

---

# 11. Testing Strategy

Test each component independently before integration:

- Gemma invocation
- Gemini invocation
- Decision engine
- Logging
- Error handling

---

# 12. Future Enhancements

- Token estimation
- Cost estimation
- Prompt caching
- Conversation memory
- Streaming responses
- RAG
- MCP integration
- PostgreSQL logging
- REST API
- Dashboard
- LangGraph orchestration

---

# 13. Success Criteria

Version 1 is complete when:

- Requests enter through one router.
- Routing decisions are automatic and deterministic.
- Both Gemma and Gemini can be invoked successfully.
- Every execution is logged.
- The router is reusable across projects and automation workflows.
