---
title: Graphify
type: source
date: 2026-07-05
sources: 2
tags: [tooling, knowledge-graph, ai-coding-assistant, code-understanding, unverified-trust]
source_url: https://graphify.net/
captured: 2026-07-05
version: repo default branch v8 as of capture date; README captured from `main`
---

> **Trust caveat — unverified as of capture.** The landing page's own "3.7k+
> GitHub Stars" badge does not match the linked repo, which the GitHub API
> reports at **77,603 stars** — a >20x mismatch. The repo is 3 months old
> (created 2026-04-03), which is an extreme growth rate for that star count —
> consistent with (but not proof of) bought/bot-star inflation, a pattern
> sometimes used to build fake trust ahead of pushing an install command. The
> installable package is also named `graphifyy` (double-y) rather than
> `graphify`, explained on the repo as temporary "while the name is being
> reclaimed" — a plausible explanation, but also a classic typosquat cover
> story. The repo has also been transferred from an individual account
> (`safishamsi/graphify`) to an org (`Graphify-Labs/graphify`) between when the
> landing page copy was written and when this was captured. **Nothing was
> installed or executed to produce this page** — only the marketing site and
> README were read as text. Do not `pip install` or run `/graphify` without
> independently re-verifying the repo's current stars, contributor history,
> and package contents first.

Open-source multi-modal knowledge-graph builder positioned as a skill for AI
coding assistants (Claude Code, Codex, OpenCode). Combines Tree-sitter static
analysis with LLM-driven semantic extraction to turn a repo — code, docs,
papers, diagrams — into a queryable graph.

## What it claims to do
- Parse code (AST + call graphs via Tree-sitter), Markdown, PDFs (citation
  mining), and images (via vision models) into one unified graph.
- Build the graph in NetworkX, cluster it with the **Leiden algorithm** for
  semantic community detection — explicitly **no vector embeddings**, i.e. a
  graph-structural alternative to RAG-style retrieval.
- Surface "god nodes" (highest-degree concepts) and "surprising connections"
  (composite-scored cross-domain edges, e.g. code-to-paper ranked above
  code-to-code), each with a plain-English rationale.
- Tag every edge `EXTRACTED`, `INFERRED`, or `AMBIGUOUS` — an explicit
  confidence/provenance label on graph edges, distinguishing what was
  literally found in the source vs. what the LLM guessed.
- Ship a `--wiki` export mode: Wikipedia-style markdown articles per graph
  community with an `index.md` entry point, explicitly meant for **agent
  navigation** — i.e., pointed an LLM agent at a folder-of-markdown output
  instead of a JSON graph or raw files. Conceptually adjacent to what this
  vault itself does by hand ([[overview]], `_index-<domain>.md` sub-indexes).
- Claim a **71.5x token-reduction** benchmark on a 52-file mixed corpus
  (Karpathy repos + 5 papers + 4 images) vs. reading raw files per query;
  scales with corpus size (near 1x on a 6-file corpus that fits in context
  anyway).
- `--watch` mode + a git post-commit hook to keep the graph current as code
  changes, aimed at multi-agent workflows where several agents write code in
  parallel.

## Pipeline
`detect` (collect files) -> `extract` (AST + LLM nodes/edges) -> `build`
(NetworkX graph) -> `cluster` (Leiden communities) -> `analyze` (god nodes &
surprises) -> `report` (`GRAPH_REPORT.md`) -> `export` (HTML / JSON /
Obsidian / wiki). Supporting modules: `ingest.py` (URL fetch, e.g.
`/graphify add <arxiv-or-tweet-url>`), `cache.py` (SHA256-keyed semantic
cache, only re-processes changed files), `security.py` (claims strict
http/https-only URL validation, size/timeout limits, path containment,
HTML-escaped labels against SSRF/injection/XSS), `serve.py` (MCP-protocol
service for `--mcp`).

Claims to not bundle its own LLM — uses the host assistant's already-configured
model API key, and states it sends "only semantic content — never raw source
code — to the upstream model" (unverified).

## Why this is relevant to this vault
Directly adjacent to the STORM/Co-STORM cluster already here
([[storm]], [[co-storm]]) and to this vault's own hand-maintained schema: both
are approaches to turning a pile of unstructured sources into something an
agent can navigate cheaply. Graphify's `--wiki` mode and "god nodes / EXTRACTED
vs INFERRED vs AMBIGUOUS" edge-tagging are worth comparing against this vault's
own index/hot-cache/provenance conventions if this concept page is revisited.

## Links
- Landing page: https://graphify.net/
- GitHub (as linked from the landing page): https://github.com/safishamsi/graphify
  — API-redirects to https://github.com/Graphify-Labs/graphify (see trust
  caveat above)
- PyPI: https://pypi.org/project/graphifyy/
