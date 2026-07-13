---
title: AGENTS.md
type: concept
date: 2026-07-13
sources: 1
tags: [agent-context, coding-agents, conventions]
source_url: https://blog.buildbetter.ai/agents-md-complete-guide-for-engineering-teams-in-2026/
captured: 2026-07-13
---

**AGENTS.md** is a standardized markdown file at a repo root that gives AI coding agents instructions, context, and conventions for working in that codebase — a README written for LLMs rather than humans: imperative and command-oriented rather than narrative.

Formalized at *agents.md* in mid-2025, co-promoted by OpenAI, Google, Sourcegraph, Cursor, Factory, JetBrains, and Anthropic as a unified alternative to fragmented per-tool files (`.cursorrules`, `.clinerules`, `.github/copilot-instructions.md`, `CLAUDE.md`). OpenAI reported 28,000+ repos already had one at launch. As of 2026 it's read by Claude Code, OpenAI Codex CLI, Cursor, Aider, Devin, Sourcegraph Amp, Google Jules, Zed AI, Continue, Roo Code, Factory Droids, GitHub Copilot, Gemini CLI, Windsurf, and Amazon Q — many tools now read it as a fallback or primary alongside their proprietary format.

## Key characteristics
- Lives at repo root alongside `README.md` / `CONTRIBUTING.md`
- Plain markdown, no required schema — only a recommended set of sections
- Auto-loaded into the agent's context at session start
- **Walked hierarchically**: most agents load the nearest AGENTS.md to the file being edited, enabling per-package overrides in monorepos

## Recommended structure
Project Overview · Tech Stack (with version pins) · Setup Commands · Code Style · Testing Instructions · Architecture Notes · PR/Commit Guidelines · Security Considerations · Things to Avoid.

**Setup Commands is the highest-leverage section** — agents waste enormous context guessing how to build/test; documenting canonical commands is the fastest ROI.

## Best practices
- Be imperative and specific: "Use pnpm, not npm" beats "We prefer pnpm"
- Paste literal shell commands, not descriptions
- Keep it under ~500 lines (200–500 is the sweet spot) — it's loaded into context every session, so token economy matters
- Treat it as code: update in the same PR that changes the convention, assign an owner
- Use negative examples liberally ("DO NOT use class components in /web") — telling agents what *not* to do prevents recurring failure classes
- Pin tool versions, or agents drift toward whatever's most common in training data
- Add a Definition-of-Done checklist agents can self-verify against

## Monorepo pattern
Thin root AGENTS.md (org-wide: language versions, package manager, commit format, security, layout) + rich per-package AGENTS.md files (service/frontend/shared-specific) scales better than one giant root file, since agents load the nearest file to what they're editing. Document cross-service contracts in the package that owns them and link from consumers.

## vs README.md / CONTRIBUTING.md
| File | Audience | Purpose | Tone |
|---|---|---|---|
| README.md | Humans, new to project | Introduction, quickstart | Narrative |
| CONTRIBUTING.md | Human contributors | Process (issues, PRs, review) | Procedural |
| AGENTS.md | AI coding agents | Operational instructions for correct code | Imperative |

Decision rule: if an agent needs it to write correct code, it belongs in AGENTS.md; cross-reference rather than duplicate.

## Common mistakes
Copy-pasting README content · vague guidance ("write clean code") · letting it drift from actual conventions · omitting build/test commands · over-stuffing (crowds out working context — push detail into per-package files) · no negative examples.

## FAQ highlights
- Not an ISO/IETF standard — a community-driven open spec, but de facto convention across major tools by 2025–2026.
- Should be committed and version-controlled like source; reviewed like code.
- Doesn't replace engineering wikis — it's for code-level conventions/commands; RFCs, runbooks, architecture stay in the wiki (can link out).
- Update signal: when an agent repeatedly produces wrong output, that's a gap in AGENTS.md.

## Note on source
The source article (BuildBetter's blog) is vendor content promoting their own "BB-Skills" product (composable/conditional skill packs layered on top of AGENTS.md, plus a customer-evidence integration) — treat the AGENTS.md mechanics above as the reusable signal and the BB-Skills/BuildBetter CLI pitch as marketing, not verified independently.

Relevant to [[caveman]] / [[token-efficiency]] (context token economy) and the anti-slop cluster ([[impeccable]], [[taste-skill]]) — both concerned with steering agent output via committed convention files.
