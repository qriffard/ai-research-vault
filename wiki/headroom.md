---
title: "Headroom (headroomlabs-ai) — context/input compression layer"
type: source
date: 2026-07-09
sources: 1
tags: [token-reduction, context-compression, claude-code, mcp, rag, github-repo]
source_url: https://github.com/headroomlabs-ai/headroom
captured: 2026-07-09
---

# Headroom — the context compression layer for AI agents

An Apache-2.0 tool that **compresses everything an agent reads** — tool outputs,
logs, RAG chunks, files, conversation history — *before* it reaches the LLM,
claiming "same answers, fraction of the tokens." Ships as a **library, proxy,
agent-wrap, and MCP server**. Ingested at the human's request. This is the
**input/context** side of the vault's token-efficiency thread — the complement to
[[caveman]] (output), and arguably the higher-leverage side per [[codeburn]]'s
finding that input tokens dwarf output in agentic coding.

**Verified metadata (GitHub API, 2026-07-09):** 58,130 ★, 4,295 forks, Apache-2.0,
Python (+ TypeScript SDK + Rust), created **2026-01-07**, very active. Docs at
headroom-docs.vercel.app.

## What it does

- **Content-aware compressors** routed by a `ContentRouter`: **SmartCrusher**
  (JSON), **CodeCompressor** (AST), **Kompress-v2-base** (prose, a HuggingFace
  model). A `CacheAligner` stabilizes prefixes so provider KV caches still hit.
- **CCR (reversible compression):** originals cached locally; the LLM calls
  `headroom_retrieve` if it needs the full content back — so compression is lossy
  to the prompt but recoverable on demand.
- **Delivery modes:** `compress(messages)` library (Py/TS); a drop-in `proxy`
  (zero code change); `headroom wrap claude|cursor|codex|…`; MCP server
  (`headroom_compress` / `_retrieve` / `_stats`).
- **Extras:** cross-agent memory (shared store + dedup across Claude/Codex/Gemini),
  `headroom learn` (mines failed sessions → writes corrections to
  `CLAUDE.local.md`), and some output-token trimming too.
- **Local-first:** data stays on the machine.

## The claim — and its rigor

Headline is **differentiated, not blanket**: "**60–95% fewer tokens for JSON
data, 15–20% for coding agents**." That honesty (structured data compresses far
more than code/prose) is a good sign — contrast [[graphify]]'s single inflated
number. It's backed by a committed **`agent-evals/`** harness with the pieces that
matter: control **arms**, an LLM **judge**, **savings** metrics, a **scorecard**,
and **stats** — i.e. it measures *answer quality*, not just token delta, which is
the fidelity dimension [[caveman]]'s eval explicitly skipped.

**Trust context (verify before betting on it):** 58k★ on a repo created only
2026-01-07, under an org (`headroomlabs-ai`) created 2026-06-16 with 2 public
repos — the young-repo / high-stars pattern the vault flagged for [[graphify]].
Unlike graphify, though, it has a real eval harness, honest content-dependent
numbers, a public model card, and heavy CI. Nothing installed or executed here
(GitHub read-only via public API). Treat the JSON 60–95% as plausible-for-
structured-data, not a universal rate.

## Why it matters here

- **Highest-leverage token lever for my workloads.** [[codeburn]] showed input
  tokens dominate agentic coding cost; Headroom targets exactly that (tool outputs,
  logs, RAG chunks) — where output-only tools like [[caveman]] can't help.
- **Reversible compression (CCR) is the key design idea** — lossy-to-the-prompt
  but recoverable via a retrieve tool sidesteps the usual "compression drops the
  detail you needed" failure. Worth stealing conceptually for any large-context
  pipeline (e.g. feeding big eval logs / tables to an LLM judge).
- **Content-aware routing** (JSON vs AST vs prose) mirrors the right instinct for
  research/eval data: compress structured outputs hard, code/prose gently.
- Completes the vault's token cluster — [[caveman]] (output), Headroom (input,
  reversible), [[graphify]] (context via knowledge graph, unverified),
  [[codeburn]] (measurement). Four coherent pages now; if it grows, worth a
  `token-efficiency` concept page or sub-index.
