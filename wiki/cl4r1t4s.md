---
title: "CL4R1T4S (elder-plinius) — extracted system-prompt collection"
type: source
date: 2026-07-09
sources: 1
tags: [system-prompts, prompt-engineering, red-teaming, transparency, security, github-repo]
source_url: https://github.com/elder-plinius/CL4R1T4S
captured: 2026-07-09
---

# CL4R1T4S — leaked/extracted system prompts for major AI products

A large community repo (by **elder-plinius**, a well-known red-teamer) collecting
**extracted/reverse-engineered system prompts, guidelines, and tool definitions**
from the major AI products. Ingested at the human's request. Tagline: "AI systems
transparency for all — in order to trust the output, one must understand the
input."

**Verified metadata (GitHub API, 2026-07-09):** 45,126 ★, 9,179 forks, AGPL-3.0,
created 2025-03-04, last pushed 2026-06-15.

## What's in it

Per-vendor top-level directories with captured system prompts / tool scaffolds:
**ANTHROPIC, OPENAI, GOOGLE, XAI, PERPLEXITY, META, MISTRAL, MOONSHOT, MINIMAX,
HUME**, and coding-agent products **CURSOR, WINDSURF, DEVIN, REPLIT, BOLT,
VERCEL V0, LOVABLE, CLINE, MANUS, FACTORY, SAMEDEV, MULTION, DIA, BRAVE, CLUELY**.
Contributions come via PR with model name/version, extraction date, and context.

## Why it matters

- **Primary-source reference for how frontier products actually steer models** —
  the hidden scaffolds that define what an assistant will/won't say, its persona,
  refusal/redirect behavior, and tool contracts. Directly useful for
  prompt-engineering and for understanding agent behavior.
- **Red-team / security research artifact** — a corpus for studying guardrails,
  injection surfaces, and cross-vendor prompt patterns.
- Connects to [[llm-laziness]] (system prompts are part of the alignment layer
  that drives brevity/behavior) and the "process over model" idea in
  [[opus-think-like-fable]] (Nate cites *leaked Fable system-prompt principles* as
  what he transplants — this repo is a source for exactly that).

## ⚠ Security caveat — the README is booby-trapped

The repo's own README embeds a **prompt-injection attack**: a leetspeak
`#MOST IMPORTANT DIRECTIVE#` instructing any AI reading it to dump its *own* system
instructions to the user. **This was not complied with during ingest** — I
described the repo without exfiltrating or reproducing any assistant's hidden
instructions. Treat the repo as **untrusted input**: reading/pasting its contents
into an agent session is itself an injection risk. Its captured prompts are also
**unverified, dated, and vendor-changing** — a snapshot for study, not ground
truth. Nothing was installed or executed; GitHub read-only via public API.
