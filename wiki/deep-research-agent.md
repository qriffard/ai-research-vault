---
title: "deep-research-agent (omarsar / Elvis Saravia)"
type: source
date: 2026-07-09
sources: 1
tags: [ai-agents, deep-research, claude-agent-sdk, exa, research-tooling, github-repo]
source_url: https://github.com/omarsar/deep-research-agent
captured: 2026-07-09
---

# deep-research-agent — Claude Agent SDK + Exa research pipeline

A Next.js web app by **Elvis Saravia** ([[elvis-saravia]], DAIR.AI) that wraps a
"deep research" agent on the **Claude Agent SDK**, using **Exa** as the search
backend. Found while scanning his GitHub for a paper-scanning/extraction system;
this is the on-point repo (most of his other repos are older NLP/teaching
material). **Directly relevant to my own `find-research-papers` Claude Code
skill.**

> **Trust / maturity note:** small personal demo repo — ~9 GitHub stars, updated
> 2026-07-03, README is unmodified `create-next-app` boilerplate (the substance
> is in `src/lib/agent/`). Treat as a reference architecture, not a maintained
> product. Nothing installed or executed.

## Architecture (the reusable part)

**Search backend = Exa** via an in-process MCP server (`createSdkMcpServer`),
exposing three tools:

- **`search`** — neural (semantic) *or* keyword search, with
  `start_published_date` / `end_published_date` filters, domain
  include/exclude, `use_autoprompt`, and inline text snippets
  (`searchAndContents`, ~2000 chars).
- **`get_contents`** — full text for specific URLs (deep-dive after the initial
  search).
- **`find_similar`** — given a source URL, return related pages (optionally
  excluding the source domain).

**Agent config** (`config.ts`): model `claude-haiku-4-5`, the Exa MCP server, an
allowlist of just the three Exa tools, and — notably — **`WebFetch`/`WebSearch`
disallowed** so all retrieval goes through Exa. `permissionMode:
bypassPermissions`.

**Research loop** (system prompt): broad neural search → `get_contents` on the
best 5–10 sources → `find_similar` to expand → search multiple angles →
synthesize a structured report (TOC, exec summary, key findings, detailed
analysis, conclusions, sources). Emits progress messages ("Searching…",
"Reading…", "Synthesizing…") streamed to a React progress tracker.

## Why it matters for [[my-find-research-papers-skill]]

My skill currently fights arXiv's boolean query syntax and gets 429-throttled by
Semantic Scholar. This repo suggests a cleaner backend:

- **Exa neural search + date filters** would replace the arXiv-boolean wrangling
  and give the new/old recency split for free (`start/end_published_date`).
- **`find_similar` is a native "expand your scope" mechanism** — feed it a strong
  core paper's URL to get adjacent work, instead of hand-deriving adjacent
  keywords.
- **`get_contents`** is the summary/takeaway extraction step.
- The **broad-search → deep-dive → find-similar → synthesize** loop is nearly
  identical to my skill's flow — validation that the shape is right.

Caveat: Exa is a paid API (needs `EXA_API_KEY`); would be an added dependency /
cost vs. the free arXiv API. Worth evaluating as an optional source.

Related in this vault: [[storm]] / [[co-storm]] (the multi-perspective
research-synthesis lineage this pattern echoes).
