---
title: "caveman (JuliusBrussee) — output-token compression skill"
type: source
date: 2026-07-09
sources: 1
tags: [token-reduction, prompt-engineering, claude-code, skill, evaluation-methodology, github-repo]
source_url: https://github.com/JuliusBrussee/caveman
captured: 2026-07-09
---

# caveman — "why use many token when few token do trick"

A viral Claude Code / multi-agent **skill** by Julius Brussee that instructs the
model to answer in terse "caveman-speak," cutting **output** tokens while keeping
code/commands/errors byte-exact. Ingested at the human's request. Notable less
for the meme than for its unusually **honest evaluation methodology** — a useful
contrast to [[graphify]], whose token-reduction claim we flagged as unverified.

**Verified metadata (GitHub API, 2026-07-09):** 87,177 ★, 4,874 forks, MIT,
created 2026-04-04, JavaScript, homepage caveman.so. Claims here are matched by a
committed eval harness — so unlike [[graphify]], the headline number is
reproducible, though narrower than the marketing implies (see below).

## The honest numbers (`docs/HONEST-NUMBERS.md`)

The mechanism is *only* a system-prompt style instruction — it shortens what the
model **says**, not its input, context, files, or thinking tokens.

- **65% average output reduction** (range 22–87%), measured on real Claude API
  token counts over 10 prompts.
- **0% input reduction**; the skill *adds* **~1–1.5k input tokens per turn**
  (the ~5 KB SKILL.md injected into context).
- **Net-negative cases**, stated plainly: terse coding Q&A (short replies save
  less than the ~1k/turn overhead), and agents billed **per request/credit**
  (Copilot) rather than per token.
- **Session-level total savings land ~14–21%** on output-heavy workloads (input
  tokens dwarf output in agentic coding) — and below zero on terse ones.
- Rule of thumb: replies >~1.5–2k output tokens → probably saves money; shorter,
  or per-request billing → probably costs money.

## The reusable idea — a claim-evaluation framework (`evals/README.md`)

The eval design is the transferable takeaway for this vault: a **three-arm**
comparison —

| Arm | System prompt |
|---|---|
| `__baseline__` | none |
| `__terse__` | `Answer concisely.` |
| `<skill>` | `Answer concisely.` + `SKILL.md` |

**The honest delta is `<skill>` vs `__terse__`**, not skill-vs-baseline —
comparing to the no-prompt baseline conflates the skill with the generic
"be terse" effect and inflates numbers (their earlier harness did this). Snapshot
committed to git for deterministic/free CI; tokens counted with tiktoken
`o200k_base` (approximate for Claude — ratios meaningful, absolutes not).
Explicitly **does not** measure fidelity, latency/cost, cross-model behavior, or
statistical significance.

## Why it matters here

- **Token efficiency for LLM pipelines** — relevant to running large evaluation /
  research workloads cost-effectively.
- **A rigorous template for vetting "X% token reduction" claims** — the
  control-arm design and the "compare to the right baseline" lesson are exactly
  what was missing when we assessed [[graphify]]. Any future token-reduction tool
  in this vault should be held to this bar.
- Meta-point: a repo can be viral *and* honest — the `HONEST-NUMBERS.md` pattern
  (a page that tells you when NOT to use the tool) is worth emulating.

See also [[graphify]] (other token-reduction tool in this vault; unverified), and [[token-efficiency]] for how this fits the broader landscape.
