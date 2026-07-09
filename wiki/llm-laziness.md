---
title: "LLM laziness — output truncation & brevity bias"
type: concept
date: 2026-07-09
sources: 1
tags: [llm-laziness, output-truncation, brevity-bias, rlhf, prompt-engineering]
source_url: https://github.com/leonxlnx/taste-skill/tree/main/research/laziness
captured: 2026-07-09
---

# LLM laziness — why models truncate, and how to override it

Synthesis of the `research/laziness/` corpus shipped in [[taste-skill]] (a
structured writeup, itself citing 2025 studies, Microsoft Research, LazyBench, and
the ERC — **secondary synthesis, citations not independently verified here**).
It's the *mechanism* page behind [[anti-slop-design]]: the same behavioral drivers
that make agents emit generic UI make them truncate code and skip work.

**Core claim (from the empirical section):** laziness is **not** a failure of
memory, context processing, or capability — it's a **behavioral artifact**. A
Dec-2025 controlled study found truncation is a *deliberate* choice, not decoding
suboptimality (greedy output matched the model's own highest-confidence answer)
and not context degradation (models stayed resilient over 200-turn tests). It's
triggered by instruction complexity exceeding effort thresholds, aggressive
stopping pressure, and economics baked into the alignment layer.

## Four root causes

1. **Training-data bias (placeholder propagation).** Stack Overflow / GitHub /
   tutorials are full of abbreviated code (`# implement auth here`, `...`,
   "similarly for the remaining cases"). The model learns placeholder insertion
   is a *legitimate professional format*, so it assigns high probability to
   truncation tokens; the tutorial-style pattern out-votes an explicit "write it
   all" instruction.
2. **RLHF & compute economics.** Token generation costs money at fleet scale, so
   post-training rewards short, confident summaries over exhaustive analysis
   ("brevity bias"). Autoregressive models have no innate completion signal, so
   training adds **stopping pressure** — calibrated aggressively in recent models
   → skipped JSON/markdown fields, "let me know if you want me to continue",
   "think about it". **Dynamic throttling** shortens outputs further under peak
   load.
3. **Output limits.** Context asymmetry (e.g. ~2M input tokens but ~8k output cap)
   → the model pre-emptively compresses when it estimates the full answer won't
   fit. **Consumer middleware** (web apps) adds silent history capping (~32k),
   context pruning, and retrieval-based recall that drops earlier instructions —
   whereas **direct API / dev platforms / CLI tools** (Claude Code, AI Studio)
   bypass that middleware and get full, unabridged output.
4. **Cognitive shortcuts (LazyBench).** When a task *looks* easy or the context is
   long, frontier models reduce internal effort and emit a surface summary despite
   retaining the info. Compounded by **error-avoidance** (shorter output = smaller
   surface for hallucination) and even **seasonal** effects (Dec brevity from
   holiday-skewed training data; stating "It is May" measurably lengthened output).

## What reliably counteracts it (findings + remediation)

- **Prompt stimuli work, reproducibly** (Microsoft Research figures): financial
  framing ("$200 tip") +45% length/quality; "take a deep breath" step-by-step 34%→80%
  on logic; stakes framing +10%; combined up to **+115%**. Effects stem from
  training-data correlations between stakes language and high-effort human output.
- **Remediation ladder** (taste-skill's framing): parameter tuning (temperature,
  top-p, thinking level) → prompt engineering (syntax binding, XML frameworks,
  verification loops) → architectural (MCP, lazy-loaded skills, **direct API/CLI
  over consumer web**) → ready-made "full output, no placeholders" reference
  prompts.

## Why it matters here

- **The root-cause layer under [[anti-slop-design]]** — "slop" (generic UI) and
  "laziness" (truncated code) are the same behavioral economics seen on two axes;
  the design skills' `full-output-enforcement` / pre-flight checks are direct
  remediations.
- **Ties to [[token-efficiency]]** — explains *why* [[caveman]]'s output numbers
  behave as they do (models already fight to be short), and why [[headroom]]'s
  input compression matters (output cap asymmetry).
- **Actionable for my own agent use:** prefer **API/CLI (Claude Code) over
  consumer web** to dodge middleware truncation; use explicit full-output prompts
  + verification loops on long generations (e.g. large eval reports, clearance
  docs) where silent truncation would be dangerous.
