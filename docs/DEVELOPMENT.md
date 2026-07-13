# Development Guide

## Development approach

Build one observable creative workflow at a time. Every workflow should have a defined input, structured output, human review point, and a small testable unit before automation is added.

## Recommended local workflow

1. Start PostgreSQL and Ollama.
2. Use Open WebUI to test and refine a prompt manually.
3. Record the prompt, expected structure, and evaluation notes.
4. Implement the smallest Python workflow.
5. Add tests for parsing, validation, and persistence.
6. Use n8n only after the workflow behaves predictably.

## Python environment

Python application code is planned for v0.2. When it is introduced:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Conventions

- Keep prompts version controlled and name them for their creative purpose.
- Keep credentials in `.env`, never source files.
- Use small, descriptive commits such as `docs: add creative brief schema`.
- Do not commit generated campaign output until it has been reviewed and is safe to publish.
- Treat model output as untrusted input: validate structure and review claims before delivery.

## Tests

Use `pytest` for deterministic parts of the application: schemas, prompt-template rendering, database repositories, and workflow transitions. Do not make tests depend on a specific model sentence or exact wording.
