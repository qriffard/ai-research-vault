---
title: AI Research — Overview
type: overview
date: 2026-06-29
sources: 1
tags: [overview, thesis]
---

# AI Research — Overview

This wiki tracks AI research papers, repositories, and approaches — with a
focus on how LLMs can automate knowledge curation, synthesis, and long-form
content generation.

## Evolving thesis

The most promising direction in LLM-powered knowledge work is **persistent,
compounding knowledge systems** — where the LLM doesn't just answer questions
from scratch each time, but incrementally builds and maintains structured
knowledge artifacts. Two patterns are emerging:

1. **Automated research + article generation** — systems like [[storm]] that
   decompose complex writing tasks into research (question asking, source
   gathering) and synthesis (outline creation, section generation). The key
   insight is that **question quality drives output quality**, and techniques
   like [[perspective-guided-question-asking]] and [[simulated-conversation]]
   dramatically improve research depth.

2. **Human-AI collaborative curation** — extensions like [[co-storm]] that keep
   the human in the loop, letting them steer the research process while the LLM
   handles the bookkeeping. This mirrors the LLM Wiki pattern itself.

## Open questions

- How to reduce **source bias transfer** from internet retrieval into generated
  content (neutrality problem).
- How to prevent **over-association** — LLMs fabricating connections between
  unrelated facts (beyond simple hallucination).
- How to extend these systems to **multi-modal** content (structured data,
  images, tables).
- How do these automated research approaches compare to **human expert
  workflows** at scale?

## Key areas tracked

- Knowledge curation and article generation ([[storm]], [[co-storm]])
- Evaluation methodologies ([[freshwiki]])
- Research groups ([[stanford-oval]])
