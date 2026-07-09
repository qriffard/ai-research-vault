---
title: "Skills for Design Engineers (Emil Kowalski)"
type: source
date: 2026-07-09
sources: 1
tags: [ai-design, anti-slop, animation, frontend, claude-code, skill, github-repo]
source_url: https://github.com/emilkowalski/skills
captured: 2026-07-09
---

# Skills for Design Engineers — Emil Kowalski

An MIT-licensed set of **agent skills** by **Emil Kowalski** (design engineer,
ex-Vercel/Linear; creator of animations.dev, Sonner, Vaul) focused on giving AI
agents **animation and design taste**. Ingested at the human's request. Third
entry in the vault's "AI design-quality / anti-slop" cluster with [[impeccable]]
and [[taste-skill]] — and notably, Emil/animations.dev is the **sponsor listed in
[[taste-skill]]'s README**, so the cluster is a connected community.

**Verified metadata (GitHub API, 2026-07-09):** 6,828 ★, 403 forks, MIT, created
2026-03-16, active. Site emilkowal.ski/skill. Install via
`npx skills@latest add emilkowalski/skills`.

## What it ships

Four skills, animation-first, distilled from domain expertise (not generic):

- **`emil-design-eng`** — the main skill: mostly animation, some general design
  advice.
- **`review-animations`** — strict, rules-based animation review (backed by a
  `STANDARDS.md`).
- **`animation-vocabulary`** — get better animations by telling the AI *exactly*
  what you want using the right terms (precise motion vocabulary).
- **`apple-design`** — Apple's interface & fluid-motion principles, distilled from
  WWDC design talks and translated for the web.

## The thesis

Same "agents don't have great taste" premise as its siblings, but sharper on
**animation**: agents pick the wrong ingredients — `ease-in` for an enter
animation that wants `ease-out`, a solid border where a semi-transparent shadow
belongs — and these little errors compound. The skills enumerate the specific
mistakes and their fixes. Framed (in Emil's "Agents with Taste" essay) as
expertise *amplified* by AI, not replaced — the skills are "a side-effect of
domain expertise."

## Why it matters here

- **The specialist counterpart** to the generalist [[impeccable]] / [[taste-skill]]:
  narrow, deep, animation-focused, from a recognized practitioner — the highest
  signal-to-noise of the three on motion specifically.
- **`animation-vocabulary` is a reusable idea** — a controlled vocabulary that
  lets you specify motion precisely to an agent; the "say the right words to get
  the right output" pattern generalizes beyond animation.
- **`review-animations` + `STANDARDS.md`** is a rules-based review harness (a
  design-review analogue to a linter), echoing [[impeccable]]'s deterministic
  detector approach.
- Concrete, expert motion rules (easing choice, reduced-motion, semi-transparent
  shadows over solid borders) directly improve the HTML artifacts I generate.

Related: [[impeccable]], [[taste-skill]] (the anti-slop design cluster); Anthropic
`frontend-design` (shared lineage of the whole cluster).
