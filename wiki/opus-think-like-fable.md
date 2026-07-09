---
title: "How I Make Opus Think Like Fable (Nate Herk video)"
type: source
date: 2026-07-09
sources: 1
tags: [prompt-engineering, model-routing, agent-methodology, claude-code, skill, video]
source_url: https://www.youtube.com/watch?v=XTBWVVcF3Pk
captured: 2026-07-09
---

# How I Make Opus Think Like Fable — Nate Herk (5 steps)

YouTube video (Nate Herk | AI Automation, 2026-07-07, ~10 min; transcript in
`raw/opus-think-like-fable.md`). Same practitioner as [[storm-claude-skill-video]].
Ingested at the human's request.

## Thesis — "the model isn't the moat"

Nate ran identical Claude Code dynamic workflows with **Fable orchestrating Fable
sub-agents** vs. Fable orchestrating Opus/Sonnet sub-agents and got roughly the
same results despite Fable costing far more. Conclusion: **you can't keep a
frontier model's intelligence (cost, availability, subscription risk), but you can
keep and transplant its _process_** — planning, verification, reasoning habits —
into cheaper models via prompting/skills. Framed as a hedge against Fable being
pulled to subscription-only, plus local/open-source models as a further hedge:
"we don't own the models… what we can own is our processes."

## The 5 techniques

1. **Reframe the strong model as teacher, not workhorse** — use Fable to extract
   and codify *how* it works, not just to grind out tasks.
2. **Model routing / right-size effort** — match task difficulty to model size and
   effort level; don't default to max — overthinking on high/max can be *worse*
   than a well-tuned lower setting.
3. **Reverse-engineer outputs you liked into a reusable process** — have the model
   analyze the winning session (what it thought, how it verified, what defined
   success) and document it as a skill.
4. **Package it as an installable "Fable mode" skill for Opus** — built on Fable's
   leaked system-prompt principles (verify assumptions, don't assume a file exists
   just because the prompt implies it, answer before asking ≤1 clarifying
   question, scale evidence-gathering to task size) around five gates: **scoping,
   evidence, attacking (adversarial reasoning), verifying, reporting**.
5. **Build a model-routing table for delegation** — give the orchestrator a
   reference table (cost / intelligence / taste per model) so it routes sub-tasks
   to the cheapest capable model (e.g. Opus orchestrator → Haiku scouts).

## Notable specifics

- **Opus-orchestrator + Haiku scouts ≈ 3× cheaper than all-Opus, same quality.**
- **Scoping = adversarial planning:** not "list steps and execute" but actively
  hunting failure modes/unknowns before executing — the habit worth transplanting.
- Leaked Fable cues cited: "partial recognition from training ≠ current knowledge";
  scale fact-checking to task (1 fact low-signal, 3–5 medium, 5–10 deep research).

## Why it matters here

- **Bridges [[token-efficiency]] and agent methodology** — "process over model" +
  the Haiku-scout routing is a concrete cost lever (cf. [[codeburn]]'s "input
  dominates", the whole token cluster).
- **Effort right-sizing** ↔ [[llm-laziness]] (more effort isn't always better).
- **Process-extraction-into-a-skill** is the same move behind the anti-slop design
  skills and my own `find-research-papers` — codify a good process once, reuse it.

Related: [[storm-claude-skill-video]] (same author), [[token-efficiency]],
[[llm-laziness]].
