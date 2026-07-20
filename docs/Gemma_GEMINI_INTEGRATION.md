# Workflow: Using Gemma 2 2B as the Primary Workhorse

This document explores a cross-model pattern: Gemma 2:2B handles the day-to-day work locally, and Gemini is used only when a task benefits from heavy lifting such as image processing, OCR, broad summarization, or other expensive preprocessing steps.

## Token ROI

The reason for this split is token ROI: keep the highest-volume, most iterative work on the cheapest practical path, and spend Gemini tokens only when the problem is large enough to justify the extra cost.

- Gemma should absorb the repeated prompt edits, local analysis, and short-form refinements that happen many times per task.
- Gemini should only be used when one expensive pass can replace many smaller, inefficient local passes.
- The workflow is better when the expensive model is a reducer or enhancer, not the default loop for every request.

This keeps the local workflow fast and predictable while preserving Gemini for the cases where its larger-context or multimodal strengths pay for themselves.

## Design Principle

Keep the fast, repetitive, and locally runnable work in Gemma. Escalate to Gemini only when the input is too large, too messy, or too multimodal for the local model to handle efficiently.

- Gemma handles most prompt drafting, rewrites, planning, analysis, and iterative refinement.
- Gemini receives only the tasks that need larger context, richer vision support, or high-cost preprocessing.
- The goal is to minimize round-trips to the heavier model and keep the local loop short.
- The goal is to maximize output per token by avoiding unnecessary escalation to the heavier model.

In practice, this means Gemma should be the default model in your shell, scripts, and review workflow.

## 1. Local Gemma First

Use Gemma for the majority of tasks through the local Ollama service.

```bash
# Start a direct local Gemma session through Docker Compose
docker compose exec ollama ollama run gemma2:2b
```

Examples of work that should stay local:

- Drafting and editing prompts.
- Summarizing brief text inputs.
- Rewriting campaign concepts.
- Producing structured checklists or JSON-like output.
- Iterating on wording until the result is ready.

## 2. Escalate Only Heavy Tasks to Gemini

When the task is expensive for Gemma, hand it off to Gemini first, then bring the distilled result back to Gemma for final shaping.

Typical heavy-lifting cases:

- Image understanding or OCR.
- Large image batches.
- Long noisy documents that need a first-pass reduction.
- Multimodal analysis that needs more capable preprocessing.
- Extracting a concise summary from complex reference material.

## 3. Example Workflow: Image Processing

Use Gemini to analyze or extract structured information from an image, then pass the result to Gemma for final refinement.

```bash
# Step 1: Send the image-heavy task to Gemini
gemini-cli "Extract the key text and visual observations from this image" --image ./assets/input.jpg > gemini_image_summary.md

# Step 2: Let Gemma turn that summary into the final deliverable
docker compose exec ollama ollama run gemma2:2b "Using this summary, write a concise creative brief note: $(cat gemini_image_summary.md)"
```

## 4. Example Workflow: Long-Form Reduction

If a reference document is too large or noisy, let Gemini compress it first and then use Gemma for the final output.

```bash
# Gemini handles the expensive reduction step
gemini-cli "Summarize this long reference document into the top 10 actionable points" --dir ./data/reference_material > reduced_context.md

# Gemma does the final composition locally
docker compose exec ollama ollama run gemma2:2b "Turn these points into a short action plan: $(cat reduced_context.md)"
```

## 5. Bash Alias Pattern

Make Gemma the default model and reserve Gemini for a dedicated heavy-lifting helper.

```bash
# Default local workhorse
gemma_local() {
  docker compose exec ollama ollama run gemma2:2b "$1"
}

# Heavy-lifting helper for image or large-context tasks
gemini_heavy() {
  local task="$1"
  shift
  gemini-cli "$task" "$@"
}

# Example usage:
# gemma_local "Rewrite this campaign message for clarity"
# gemini_heavy "Extract text from this image and summarize the design" --image ./assets/input.jpg
```

## 6. Decision Rule

Use Gemma unless at least one of these is true:

- The input is mostly visual or multimodal.
- The source material is too large to reduce comfortably in a local pass.
- The task is a preprocessing step that should happen once before local refinement.
- You need a stronger first-pass summary before Gemma takes over.
- The expected savings from one Gemini pass outweigh the cost of staying local.

If none of those apply, keep the task local and stay with Gemma.
