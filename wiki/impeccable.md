---
title: "Impeccable (Paul Bakaus) — design language for AI coding agents"
type: source
date: 2026-07-09
sources: 1
tags: [ai-design, anti-slop, frontend, claude-code, skill, github-repo]
source_url: https://github.com/pbakaus/impeccable
captured: 2026-07-09
---

# Impeccable — "the design language that makes your AI harness better at design"

An Apache-2.0 **agent skill** by **Paul Bakaus** (creator of jQuery UI; at Google)
that gives AI coding agents design taste for frontend work. Ingested at the
human's request. Part of an emerging "AI design-quality / anti-slop" cluster in
this vault alongside [[taste-skill]] — both descend from Anthropic's
`frontend-design` skill.

**Verified metadata (GitHub API, 2026-07-09):** 45,065 ★, 2,608 forks, Apache-2.0,
JavaScript, created 2025-11-16, active. Site impeccable.style. Install via
`npx impeccable install` then `/impeccable init`.

## What it is

**1 skill, 23 commands, 46 deterministic detector rules**, plus live browser
iteration. Explicitly built on top of Anthropic's `frontend-design` skill.

- **`/impeccable init`** writes `PRODUCT.md` (+ optional `DESIGN.md`) capturing
  audience, brand/product lane, voice, anti-references, colors, type, components
  — read by every later command. A **register** split drives guidance: *brand*
  (design IS the product: marketing/landing/portfolio) vs *product* (design SERVES
  it: app/dashboard/tool).
- **23 commands** = a shared design vocabulary with the agent: `craft`, `shape`,
  `critique`, `audit`, `polish`, `bolder`, `quieter`, `distill`, `harden`,
  `onboard`, `animate`, `colorize`, `typeset`, `layout`, `delight`, `overdrive`,
  `clarify`, `adapt`, `optimize`, `live`, `document`, `extract`, `init`.
- **46 deterministic detector rules** (a CLI + browser extension) run with **no
  LLM / no API key** — catching design anti-patterns statically (CSS cascade,
  contrast, fonts, etc.) — complemented by LLM-only critique checks.
- Platform-aware: native iOS (HIG) / Android (Material 3) reference variants.

## The anti-slop thesis

Its reason to exist: every model trained on the same SaaS templates, so skipping
design guidance yields the same "tells" — **Inter for everything, purple→blue
gradients, cards nested in cards, gray text on colored backgrounds, the rounded-
square icon tile above every heading.** The skill encodes concrete rules against
these: verify contrast (≥4.5:1 body), cap line length 65–75ch, pair fonts on a
contrast axis, display letter-spacing floor ≥ −0.04em, no bounce/elastic easing,
mandatory `prefers-reduced-motion`, semantic z-index scale, "cards are the lazy
answer / nested cards always wrong."

## Why it matters here

- **A structured, opinionated design-quality layer for coding agents** — the same
  family of "make the agent better at X" skills as the vault's other tooling, but
  for *taste/craft* rather than tokens.
- **Deterministic detector rules (no LLM)** are the interesting engineering idea:
  a static + browser rule engine for design anti-patterns, analogous to a linter
  — cheap, reproducible, no API cost. Pairs conceptually with [[caveman]]'s
  "measure, don't trust" rigor.
- **Credible author** (jQuery UI) and a documented before/after case study.
- Directly usable for the [[headroom]]-style HTML digests / dashboards I build —
  the concrete rules (contrast, type pairing, motion, z-index) are a ready
  checklist. See also the Zoox `visual-explainer` aesthetic already in use.

Related: [[taste-skill]] (sibling anti-slop skill collection), and Anthropic's
`frontend-design` (shared ancestor).
