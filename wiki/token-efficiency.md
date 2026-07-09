---
title: "Token efficiency for LLM agents — the tooling landscape"
type: concept
date: 2026-07-09
sources: 0
tags: [token-reduction, context-compression, cost-optimization, evaluation-methodology]
---

# Token efficiency for LLM agents

A synthesis page tying together the token-efficiency tools captured in this vault.
They attack the same cost problem — LLM agents burn tokens — from **four distinct
angles**. This page maps the space, the load-bearing principle, and the
evaluation lesson that separates a real win from a marketing number.

## The four levers

| Lever | What it touches | Tool | Verified | Honest about limits? |
|---|---|---|---|---|
| **Compress the input** | tool outputs, logs, RAG chunks, files, history — *before* the LLM reads them | [[headroom]] | 58k★, Apache-2.0 | Yes — 60–95% JSON vs 15–20% coding; eval harness w/ judge |
| **Compress the output** | what the model *writes back* (terse "caveman speak") | [[caveman]] | 87k★, MIT | Yes — `HONEST-NUMBERS.md`; net-negative cases stated |
| **Compress the context via structure** | a knowledge graph over a code/doc corpus | [[graphify]] | ⚠ unverified (stars mismatch, young repo) | No — single inflated number |
| **Measure it** | actual per-tool/model/task token & $ usage on disk | [[codeburn]] | 8.5k★, MIT | Yes — reads real session files, local-first |

## The load-bearing principle: input dominates

[[codeburn]]'s (and [[caveman]]'s) key finding: **in agentic coding, input tokens
dwarf output tokens.** Consequences:

- **Output-only compression has a ceiling.** [[caveman]] cuts ~65% of *output*
  but adds ~1–1.5k input tokens/turn and nets only ~14–21% at session level (below
  zero on terse workloads / per-request billing).
- **Input/context compression is the higher-leverage lever** — which is why
  [[headroom]] (and, in principle, [[graphify]]) target what the model *reads*.
- **You can't optimize what you don't measure** — [[codeburn]] is the A/B tool
  that tells you whether any of the above actually helped *on your workload*.

## The evaluation lesson

Token-reduction claims are easy to inflate; the vault holds one verified-honest
example and one unverified one. The bar to apply:

- **Measure the right delta.** [[caveman]]'s three-arm design (baseline / "be
  terse" / skill) shows the honest number is **skill-vs-terse**, not skill-vs-
  nothing — comparing to no-instruction conflates the tool with the generic
  terseness effect.
- **Measure fidelity, not just token delta.** A tool that answers `k` to
  everything "wins" on tokens and fails on correctness. [[headroom]]'s
  `agent-evals/` adds an LLM judge for answer quality; [[caveman]]'s eval
  explicitly skips fidelity (a noted gap).
- **Session-level totals, on your own traffic, from the provider's billing** —
  the only number that outranks a repo's README. Use [[codeburn]] or a manual A/B.
- **Watch the young-repo / high-stars pattern** ([[graphify]], and to a lesser
  degree [[headroom]]) — high stars on a months-old repo warrant checking the
  eval harness before trusting the headline.

## Design ideas worth stealing

- **Reversible compression** ([[headroom]] CCR): compress lossily into the prompt
  but cache originals + expose a retrieve tool — sidesteps "I compressed away the
  detail I needed." Directly useful for feeding big eval logs/tables to an LLM.
- **Content-aware routing:** compress structured data (JSON) hard, code/prose
  gently — the compression ceiling is content-type-dependent.
- **An honest-numbers doc** ([[caveman]]): a page that tells you when *not* to use
  the tool is a credibility signal worth emulating.
