---
title: "Stanford's Method Turns Claude Into a PhD Level Research Team (Nate Herk)"
type: source
date: 2026-06-29
sources: 1
tags: [storm, multi-agent, practitioner-implementation, claude-skill, verification]
source_url: https://www.youtube.com/watch?v=Tj3018n5MVg
captured: 2026-06-29
---

# Stanford's Method Turns Claude Into a PhD Level Research Team

A 12-minute YouTube tutorial by **Nate Herk** (AI Automation channel) demonstrating
a Claude skill that operationalizes [[storm]] principles for everyday research.

## Key implementation details

The author builds a `.claude/` skill (a master prompt) implementing STORM's
multi-perspective research as a repeatable workflow:

### Five fixed perspectives
Rather than auto-generating perspectives per-topic (as STORM does), the skill
uses a fixed set: **practitioner, academic, skeptic, economist, historian**.
Each finds "holes that the other angles miss" — the same unknown-unknowns
principle from [[co-storm]].

### Two-pass verification pipeline
1. **V1** — Each perspective researches the topic, generates findings, and
   assembles a single self-contained HTML report.
2. **V2** — The system adversarially peer-reviews its own output, verifying
   every citation against its primary source. Sources are marked as
   **confirmed**, **corrected**, or **demoted**.

### Output format
A self-contained HTML briefing with:
- 60-second summary
- Key findings ranked by reliability
- Per-section perspective analysis
- Source verification audit at the bottom

### Comparison with Claude's native deep research
The author contrasts the skill with Claude's built-in "deep research" (dynamic
workflows, ~103 agents), noting that native deep research produces solid output
but the STORM skill adds structured multi-perspective coverage and explicit
source verification that deep research lacks.

## Broader takeaways (author's framing)

- The value is less in this specific skill and more in the principle: **more
  perspectives + adversarial contradiction = more holistic research**.
- "If you don't have subject matter expertise, see if you can borrow it" — use
  agents as a council with diverse knowledge.
- Encourages customization: add domain-specific lenses (e.g., "beginner in AI",
  "content creator") tailored to your use case.

## Portability

The skill works across Claude (desktop/VS Code), Codex, or any agent that reads
prompt files from a config directory (`.claude/`, `.codex/`, `.agents/`).

## Related

- [[storm]] — the academic system this skill is based on
- [[co-storm]] — the collaborative extension (more sophisticated multi-agent orchestration)
- [[perspective-guided-question-asking]] — the core technique adapted here
