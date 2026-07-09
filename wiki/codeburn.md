---
title: "CodeBurn (Agentseal) — AI coding token/cost observability"
type: source
date: 2026-07-09
sources: 1
tags: [token-usage, cost-tracking, observability, claude-code, developer-tools, github-repo]
source_url: https://github.com/getagentseal/codeburn
captured: 2026-07-09
---

# CodeBurn — "see where your AI spend goes"

A free, **local-first** CLI (by the **Agentseal** org — agent probes/testing/
observability, agentseal.org) that tracks AI-coding token usage and cost across
**31 tools/agents** (Claude Code, Cursor, Codex, Gemini, Grok…), broken down by
**task, model, tool, and project**. Ingested at the human's request. It's the
*measurement* counterpart to [[caveman]]'s *reduction* — and directly actionable
for my own daily Claude Code / Cursor use.

**Verified metadata (GitHub API, 2026-07-09):** 8,553 ★, 675 forks, MIT,
TypeScript, created 2026-04-13, active (pushed 2026-07-08), homepage
codeburn.app. Run with `npx codeburn`.

## What it does

Reads the **session files your tools already write to disk** (JSONL / SQLite /
protobuf) — no wrapper, proxy, or API keys; **nothing leaves the machine**.
Pricing from [LiteLLM](https://github.com/BerriAI/litellm), refreshed daily.
Dedups turns that surface in two providers (e.g. Claude logs vs. Cursor mirror)
via a shared `seenKeys` set. Surfaces: `overview` (copy-pasteable spend
summary), interactive Ink TUI dashboard, `compare` (two models side by side),
`export` (CSV/JSON), a macOS menubar app, and `optimize`.

## `codeburn optimize` — 14 waste detectors (the useful part)

Scans sessions + your `~/.claude/` setup and returns ranked findings with a
ready-to-paste fix and estimated token/$ savings, rolled into an **A–F setup
health grade** (repeat runs mark findings new / improving / resolved):

- Files re-read across sessions (same content, over and over)
- **Low Read:Edit ratio** (editing without reading → retries → wasted tokens)
- Uncapped `BASH_MAX_OUTPUT_LENGTH` / trailing bash noise
- **Unused MCP servers** still paying tool-schema overhead every session
- **Ghost agents/skills/slash-commands** defined in `~/.claude/` but never invoked
- **Bloated `CLAUDE.md`** (with `@-import` expansion counted)
- Cache-creation overhead, junk directory reads (`node_modules`, `.git`, `dist`)
- Context-heavy sessions where input/cache tokens swamp output
- Low-worth expensive sessions with no edit turns / repeated retries and no
  observed `git`/`gh` delivery

## Why it matters here

- **The A/B measurement tool [[caveman]] tells you to use.** CodeBurn reads real
  provider token counts locally — exactly the "measure it on your own workload"
  step that separates a real token-reduction win from a marketing number.
- **Personally actionable:** several detectors target *my* setup — a large
  `CLAUDE.md`, many configured MCP servers (Jira/Confluence/Todoist/Playwright…),
  and lots of skills/commands. `optimize` would quantify the per-session overhead.
- **Cost discipline at eval scale** — the by-model/by-task breakdown is the kind
  of accounting that matters when running large evaluation/research workloads on
  a constrained budget.
- Complements the vault's token-efficiency thread: [[caveman]] (reduce output),
  [[graphify]] (compress context — unverified), CodeBurn (measure everything).
  See [[token-efficiency]] for the full landscape.

**Trust note:** local-first, no network egress of session data — low-risk to run.
Nothing installed or executed during this ingest (GitHub read-only via public API).
