---
title: "Taste Skill (Leonxlnx) — anti-slop frontend framework for AI agents"
type: source
date: 2026-07-09
sources: 1
tags: [ai-design, anti-slop, frontend, claude-code, skill, llm-laziness, github-repo]
source_url: https://github.com/leonxlnx/taste-skill
captured: 2026-07-09
---

# Taste Skill — "gives your AI good taste; stops boring, generic slop"

An MIT-licensed collection of **portable agent skills** (by Leonxlnx) that upgrade
AI-built interfaces — stronger layout, typography, motion, spacing instead of
boilerplate UIs. Ingested at the human's request. Sibling to [[impeccable]] in the
vault's emerging "AI design-quality / anti-slop" cluster.

**Verified metadata (GitHub API, 2026-07-09):** 61,228 ★, 4,191 forks, MIT,
created 2026-02-19, active. Site tasteskill.dev. Install via
`npx skills add https://github.com/Leonxlnx/taste-skill` (uses vercel-labs
`agent-skills` CLI). *(Disclaimer on the repo: no official token/crypto — imposters
exist.)*

## What it ships

A menu of **single-job skills** (install by frontmatter `name:`), not one monolith:

- **`design-taste-frontend`** (default, "v2 experimental") — reads the brief,
  infers the design language, tunes **three dials: VARIANCE / MOTION / DENSITY**;
  design-system map, **hard em-dash ban**, canonical **GSAP** code skeletons,
  redesign-audit protocol, strict pre-flight check.
- Style variants: **`minimalist-ui`** (Notion/Linear), **`industrial-brutalist-ui`**
  (Swiss type, sharp contrast), **`high-end-visual-design`** (soft/premium, spring
  motion), **`stitch-design-taste`** (Google Stitch-compatible, `DESIGN.md` export).
- Workflow skills: **`redesign-existing-projects`** (audit-then-fix),
  **`image-to-code`** (generate references → analyze → implement),
  **`full-output-enforcement`** (stop half-finished work / placeholder comments).
- **Image-generation skills** for reference boards (web / mobile / brand kits) —
  pair with ChatGPT Images, hand frames to Codex/Cursor/Claude Code.

## The research angle (the vault-worthy part)

Ships a `research/laziness/` writeup on **why LLMs produce generic "slop"** —
root causes documented as: **training-data bias, RLHF-and-compute pressure,
output-length limits, cognitive shortcuts** — plus remediation
(architectural-patterns, parameter-tuning, prompt-engineering, reference-prompts)
and an empirical-results/references pair. This is a rare instance of a design tool
articulating the *mechanism* behind the failure it fixes.

## Why it matters here

- **Complements [[impeccable]]** — same anti-slop goal, different shape: a *menu of
  style-specific skills* + tunable dials vs. impeccable's *one skill / 23 commands
  / deterministic detector*. Worth comparing approaches if I codify a house style.
- **The `research/laziness/` corpus** is genuinely useful reading on LLM
  degeneration modes — relevant beyond design (any generate-over-NL task), and a
  candidate for its own concept page ([[llm-laziness]]) if it recurs.
- **Concrete anti-slop levers** (VARIANCE/MOTION/DENSITY dials, em-dash ban, GSAP
  skeletons) are a pragmatic checklist for the HTML artifacts I generate.

Related: [[impeccable]] and [[emil-kowalski-skills]] (siblings), Anthropic
`frontend-design` (shared lineage), and [[anti-slop-design]] (the cluster synthesis).
