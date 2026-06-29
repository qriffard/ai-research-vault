---
title: Simulated Conversation
type: concept
date: 2026-06-29
sources: 1
tags: [pre-writing, question-asking, multi-perspective-qa]
---

# Simulated Conversation

A technique introduced in [[storm]] where the LLM simulates a multi-turn
conversation between a **Wikipedia writer** (carrying a specific perspective)
and a **topic expert** grounded in internet sources.

## Mechanism

In round $i$:
1. The writer generates question $q_i$ based on topic $t$, perspective $p$, and
   conversation history $\{q_1, a_1, \ldots, q_{i-1}, a_{i-1}\}$.
2. The LLM breaks $q_i$ into search queries.
3. Retrieved results are filtered by Wikipedia reliability guidelines.
4. The expert synthesizes trustworthy sources into answer $a_i$.
5. Sources are added to the reference set $\mathcal{R}$.

Conversations are limited to $M$ rounds per perspective.

## Why it matters

The conversation history lets the LLM **iteratively update its understanding**
and ask follow-up questions — mirroring how human researchers deepen their
knowledge. Ablation shows removing conversation drops unique references from
~100 to ~40, the largest single-component degradation in STORM.

## Related

- [[storm]]
- [[perspective-guided-question-asking]]
