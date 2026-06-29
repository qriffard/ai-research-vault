---
title: "STORM: Synthesis of Topic Outlines through Retrieval and Multi-perspective Question Asking"
type: concept
date: 2026-06-29
sources: 1
tags: [knowledge-curation, pre-writing, multi-perspective-qa, article-generation, rag]
source_url: https://arxiv.org/abs/2402.14207
captured: 2026-06-29
---

# STORM

**STORM** (Synthesis of Topic Outlines through Retrieval and Multi-perspective
Question Asking) is an LLM-powered system from [[stanford-oval]] that writes
Wikipedia-like articles from scratch based on internet search. Published at
NAACL 2024.

## Core idea

The key insight is that **automatically coming up with good questions** is the
core of automating the research process. Direct prompting produces shallow
"What/When/Where" questions. STORM addresses this with two strategies:

1. **[[perspective-guided-question-asking]]** — discover diverse perspectives by
   surveying existing Wikipedia articles on similar topics, then personify the
   LLM with each perspective to ask deeper, more varied questions.
2. **[[simulated-conversation]]** — simulate multi-turn conversations between a
   "Wikipedia writer" (carrying a perspective) and a "topic expert" grounded in
   internet sources. The conversation history lets the LLM update its
   understanding and ask follow-up questions.

## Pipeline

STORM decomposes article generation into two stages:

### Pre-writing stage (research)
1. **Perspective discovery** — given topic $t$, retrieve related Wikipedia
   articles, extract their tables of contents, and prompt an LLM to identify $N$
   perspectives $\mathcal{P} = \{p_0, \ldots, p_N\}$ (plus a default "basic
   facts" perspective $p_0$).
2. **Simulated conversations** — for each perspective, simulate a multi-turn
   conversation (up to $M$ rounds). Questions are grounded: the LLM breaks each
   question into search queries, filters results by Wikipedia reliability
   guidelines, and synthesizes answers from trustworthy sources.
3. **Outline creation** — first generate a draft outline $\mathcal{O}_D$ from
   the LLM's parametric knowledge, then refine it using the simulated
   conversations to produce the final outline $\mathcal{O}$.

### Writing stage
4. **Section-by-section generation** — for each section, retrieve relevant
   documents from $\mathcal{R}$ via Sentence-BERT similarity, then generate
   with citations.
5. **Polish** — remove repeated information across sections, generate a lead
   section summary.

## Key results

- **FreshWiki dataset**: 100 high-quality recent Wikipedia articles (Feb 2022 –
  Sep 2023) to avoid data leakage.
- STORM outlines achieve higher heading soft recall and entity recall than
  Direct Gen, RAG, and RAG-expand baselines.
- Human evaluation (10 experienced Wikipedia editors, 500+ edits each):
  - **+25% absolute** in Organization (rating ≥ 4)
  - **+10% absolute** in Coverage (rating ≥ 4)
  - 26 vs 14 pairwise preference for STORM over oRAG
  - Editors unanimously agree STORM helps their pre-writing stage
- Citation quality: 84.83% recall, 85.18% precision (judged by Mistral 7B).

## Ablation findings

| Variant | Unique refs |$|\mathcal{R}|$|
|---------|------------|
| Full STORM | 99.83 |
| w/o Perspective | 54.36 |
| w/o Conversation | 39.56 |

Both perspective discovery and simulated conversation are critical — removing
conversation hurts most, confirming that iterative research drives question
quality.

## Limitations identified

- **Source bias transfer** — internet retrieval bias (promotional content,
  dominant viewpoints) propagates into generated articles. 7/10 editors noted
  articles sound "emotional" or "unneutral".
- **Over-association** — LLMs fabricate connections between unrelated facts
  (red herring fallacy), a verifiability issue beyond simple hallucination.
- **Text-only** — does not handle structured data or multi-modal content.
- Generated articles trail well-revised human Wikipedia articles.

## Implementation

- Built on [[dspy]]. Uses [[litellm]] for LLM integration.
- Multi-LM architecture: cheaper models for conversation simulation, stronger
  models for article generation.
- Supports multiple retrieval backends: You.com, Bing, Google, Tavily, Brave,
  DuckDuckGo, and custom vector stores.
- Open source: [github.com/stanford-oval/storm](https://github.com/stanford-oval/storm)
- Package: `pip install knowledge-storm`

## Related

- [[co-storm]] — collaborative extension with human-in-the-loop
- [[perspective-guided-question-asking]]
- [[simulated-conversation]]
- [[freshwiki]]
