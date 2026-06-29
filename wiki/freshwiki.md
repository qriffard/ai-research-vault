---
title: FreshWiki Dataset
type: entity
date: 2026-06-29
sources: 1
tags: [dataset, evaluation, article-generation]
source_url: https://huggingface.co/datasets/EchoShao8899/FreshWiki
captured: none (pointer)
---

# FreshWiki

A benchmark dataset of **100 high-quality Wikipedia articles** curated for
evaluating long-form article generation systems. Introduced in the [[storm]]
paper (NAACL 2024).

## Design

- Focuses on the **most-edited pages** from February 2022 to September 2023
  (rather than creation date) to select actively maintained, high-quality
  articles.
- Filters for articles predicted to be **B-class quality or above** (~3% of all
  Wikipedia pages meet this bar).
- Mitigates data leakage by selecting articles created/heavily edited after LLM
  training cutoffs.
- The curation pipeline is reproducible at future dates for new LLMs.

## Evaluation criteria

- **Heading soft recall** — measures outline coverage against human outlines.
- **Entity recall** — measures whether key entities are mentioned.
- **LLM evaluator** — rates interest, relevance, coverage on a Likert scale.
- **Citation quality** — recall and precision judged by Mistral 7B-Instruct.

## Availability

[HuggingFace: EchoShao8899/FreshWiki](https://huggingface.co/datasets/EchoShao8899/FreshWiki)

## Related

- [[storm]]
