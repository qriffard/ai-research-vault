---
title: "Creative frontend effects — WebGL/visual-craft building blocks"
type: concept
date: 2026-07-09
sources: 0
tags: [frontend, webgl, visual-effects, creative-coding, tools]
---

# Creative frontend effects — a toolkit for high-craft web visuals

A curated cluster of frontend libraries/tools for **distinctive visual effects**
(WebGL, animated gradients, glass/liquid materials). Captured as pointers at the
human's request. Where [[anti-slop-design]] says *what* good design looks like,
these are part of the *how* — the raw materials for output that stands out. Also
relevant to the visual craft of the HTML research digests / dashboards I build
(cf. [[dataviz]]-style artifacts).

## The tools (verified via GitHub API, 2026-07-09)

- **React Three Fiber** — pmndrs/react-three-fiber · **31,372 ★**, MIT · a React
  renderer for Three.js (declarative WebGL/3D in React). The **foundational
  substrate** the others plug into. Docs: r3f.docs.pmnd.rs /
  docs.pmnd.rs/react-three-fiber. Part of the poimandres (pmndrs) ecosystem
  (drei, react-spring, zustand).
- **liquid-glass-react** — rdev/liquid-glass-react · **5,527 ★**, MIT, TypeScript
  · Apple's "Liquid Glass" material effect for React (frosted/refractive glass UI).
- **ShaderGradient** — ruucm/shadergradient · **1,860 ★** · animated 3D
  gradients, authored visually and exported to **React / Framer / Figma**. Site:
  shadergradient.co.
- **liquid-logo** — collidingScopes/liquid-logo · **88 ★**, MIT, TypeScript · a
  free browser tool for real-time **animated liquid-metal logo** effects.

## Notes & why grouped

- **R3F is the anchor**; liquid-glass-react and ShaderGradient are effect layers
  that can render into a React/WebGL scene, and liquid-logo is a standalone
  generator. Together they're a palette for hero sections, backgrounds, brand
  moments, and "technically extraordinary" effects (cf. [[impeccable]]'s
  `overdrive` command, [[emil-kowalski-skills]]'s motion focus).
- **Maturity spread:** R3F is a large, actively-maintained ecosystem pillar;
  liquid-glass-react rode the 2025 "Liquid Glass" wave (moderately large, but last
  pushed 2025-06 — check maintenance before depending on it); ShaderGradient is a
  design-tool-scale project; liquid-logo is a small personal tool (88★, brief
  history) — fine as inspiration, verify before production use.
- These are **creative-coding tools, not AI research** — filed here because
  they're building blocks for the high-craft frontends the design cluster argues
  for, and useful reference when raising the visual ceiling on my own outputs.

Related: [[anti-slop-design]] (the taste/quality layer these serve).
