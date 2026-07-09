---
title: "Anti-slop design — giving AI agents taste"
type: concept
date: 2026-07-09
sources: 0
tags: [ai-design, anti-slop, frontend, agents-with-taste, skill]
---

# Anti-slop design — the "agents with taste" tooling landscape

A synthesis of the design-quality agent skills captured in this vault. They share
one premise: **AI coding agents produce generic "slop"** — every model trained on
the same SaaS templates emits the same tells — and a **skill that injects design
taste** fixes it. This page maps the cluster, the shared root cause, and the
common levers.

All three descend from **Anthropic's `frontend-design` skill** and form a
connected community (Emil Kowalski / animations.dev sponsors [[taste-skill]]).

## The cluster

| Skill | Author | Stars | Shape | Distinctive move |
|---|---|---|---|---|
| [[impeccable]] | Paul Bakaus (jQuery UI) | 45k, Apache-2.0 | Generalist: 1 skill / 23 commands | **46 deterministic detector rules** (CLI + browser, no LLM/API) |
| [[taste-skill]] | Leonxlnx | 61k, MIT | Menu of style-specific skills | **VARIANCE/MOTION/DENSITY dials** + a `research/laziness/` corpus |
| [[emil-kowalski-skills]] | Emil Kowalski (Vercel/Linear) | 6.8k, MIT | Specialist: animation-first | **`animation-vocabulary`** + rules-based review harness |

Read as: **impeccable** = the broad, tooling-heavy system; **taste-skill** = the
style-menu with a research backbone; **emil-kowalski-skills** = the deep,
expert-authored motion specialist.

## The shared root cause (why "slop" happens)

[[taste-skill]]'s `research/laziness/` articulates it: LLMs default to generic
output because of **training-data bias** (over-represented SaaS/Bootstrap
templates), **RLHF-and-compute pressure** (safe, average answers score well),
**output-length limits** (truncate → placeholder → boilerplate), and **cognitive
shortcuts** (reach for the most frequent pattern). The design skills are the
remediation layer. *(Candidate for its own [[llm-laziness]] concept page — the
mechanism generalizes beyond design to any generate-over-NL task.)*

## The recurring "tells" they all target

Inter for everything · purple→blue gradients · cards nested in cards · gray text
on colored backgrounds · the rounded-square icon tile above every heading ·
`ease-in`/bounce/elastic easing · pure black/gray (untinted) · uniform reveal
animation on every section · solid borders where a soft shadow belongs.

## Common levers (a practical checklist)

- **Capture design context up front** — impeccable's `PRODUCT.md`/`DESIGN.md`,
  taste-skill's brief inference; the brand-vs-product register split (design IS
  the product vs design SERVES it) changes all downstream guidance.
- **Tunable intensity** — taste-skill's VARIANCE/MOTION/DENSITY dials;
  impeccable's `bolder`/`quieter`/`distill`.
- **A controlled vocabulary** — emil's `animation-vocabulary`: say the exact word
  to get the exact output. Generalizes as a prompting pattern.
- **Deterministic / rules-based review** — impeccable's 46 no-LLM detector rules
  and emil's `review-animations` + `STANDARDS.md`: a *linter for design*, cheap
  and reproducible (the same "measure, don't trust the model" instinct behind
  [[caveman]]/[[codeburn]] in the token cluster).
- **Concrete rules worth stealing for my own artifacts:** contrast ≥4.5:1 body;
  line length 65–75ch; pair fonts on a contrast axis; display letter-spacing floor
  ≥ −0.04em; no bounce/elastic; mandatory `prefers-reduced-motion`; semantic
  z-index scale; never nest cards. Directly applicable to the HTML research
  digests / dashboards I generate (cf. the Zoox `visual-explainer` aesthetic).

## Relation to the other vault cluster

Orthogonal to [[token-efficiency]] (caveman/headroom/graphify/codeburn): that
cluster makes agents **cheaper**; this one makes their **output better**. Shared
DNA: both favor **deterministic measurement** over trusting the model's
self-assessment.
