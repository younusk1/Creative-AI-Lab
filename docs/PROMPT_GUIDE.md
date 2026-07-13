# Prompt Guide

## Goal

Prompts are production inputs. Store the intent, constraints, version, and review notes alongside the prompt text so a campaign can be reproduced and improved.

## Creative-brief prompt pattern

Use this structure for planning prompts:

```text
Role: You are a creative planning assistant.

Objective: [what the campaign needs to achieve]
Audience: [who it is for]
Channel and format: [for example, Instagram Reel, 9:16]
Tone: [for example, optimistic, premium, concise]
Mandatory elements: [messages, CTA, product facts]
Constraints: [brand, legal, cultural, budget, accessibility]

Return: campaign concept, key message, visual direction, assumptions,
three initial prompt options, and open questions.
```

## Image and video prompt pattern

Specify only details that matter to the output:

1. Subject and action
2. Setting and visual style
3. Composition, camera, or aspect ratio
4. Lighting and mood
5. Brand-safe constraints and exclusions
6. Delivery format

Example skeleton:

```text
[Subject] in [setting], conveying [message].
Visual style: [style]. Composition: [framing], [aspect ratio].
Lighting and mood: [details]. Include: [approved elements].
Avoid: [unwanted elements]. Output for: [channel].
```

## Versioning and review

- Name prompts with a campaign, purpose, and version: `fintech-launch_image-hero_v01`.
- Record the model, date, input brief, prompt, output reference, reviewer, and outcome.
- Change one meaningful variable at a time when evaluating alternatives.
- Never include private client data, unlicensed reference material, or credentials in a prompt.

## Evaluation checklist

- Does the output address the campaign objective and audience?
- Are required messages and format constraints respected?
- Is the tone appropriate and consistent?
- Are assumptions clear and safe?
- Does the output require factual, brand, legal, or cultural review?
