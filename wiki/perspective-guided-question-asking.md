---
title: Perspective-Guided Question Asking
type: concept
date: 2026-06-29
sources: 1
tags: [pre-writing, question-asking, multi-perspective-qa]
---

# Perspective-Guided Question Asking

A strategy introduced in [[storm]] for improving the depth and breadth of
questions during automated research. Rather than directly prompting an LLM to
generate questions (which yields shallow "What/When/Where" questions), the
system discovers **diverse perspectives** by surveying existing articles on
similar topics and then personifies the LLM with each perspective.

## How it works

1. Given topic $t$, retrieve related Wikipedia articles via the Wikipedia API.
2. Extract their tables of contents and concatenate them as context.
3. Prompt the LLM to identify $N$ perspectives that collectively cover the topic.
4. Add a default $p_0$ = "basic fact writer" to ensure baseline coverage.
5. Each perspective guides a separate [[simulated-conversation]].

## Why it matters

Grounded in stakeholder theory — different perspectives (e.g., event planner vs.
layperson for the 2022 Winter Olympics) surface different facets of a topic,
leading to more diverse and in-depth questions. Ablation in the STORM paper shows
removing perspective reduces unique references collected from ~100 to ~54.

## Related

- [[storm]]
- [[simulated-conversation]]
