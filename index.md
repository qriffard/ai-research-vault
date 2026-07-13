# AI Research — Master Index

> Created 2026-06-29 — Track and synthesize AI research papers, repos, and approaches
> Catalog of the wiki. Read this *after* `_hot.md` when the hot cache isn't
> enough. For a large domain, drill into its `_index-<domain>.md` rather than
> scanning everything here. The LLM updates this on every ingest.

## Recently Active
- [[agentsmd]] — AGENTS.md standard: repo-root markdown for AI coding agent context/conventions; structure, best practices, monorepo pattern, vs README/CONTRIBUTING (2026-07-13)
- [[cl4r1t4s]] — elder-plinius's extracted-system-prompt collection (45k★) across all major AI products; ⚠ README contains a prompt-injection (not complied with) (2026-07-09)
- [[opus-think-like-fable]] — Nate Herk video: "process over model" — transplant Fable's process to cheaper Opus via routing + skill extraction (2026-07-09)
- [[creative-frontend-effects]] — pointer cluster: WebGL/visual-craft building blocks (React Three Fiber, liquid-glass-react, ShaderGradient, liquid-logo) for high-craft frontends (2026-07-09)
- [[llm-laziness]] — why LLMs truncate/produce brevity (behavioral artifact, not capability): 4 root causes + remediation; mechanism behind [[anti-slop-design]] (2026-07-09)
- [[anti-slop-design]] — synthesis of the "agents with taste" cluster (impeccable/taste-skill/emil-kowalski-skills): shared slop root cause, common levers, deterministic-review theme (2026-07-09)
- [[emil-kowalski-skills]] — animation-first design skills for AI agents (Emil Kowalski, animations.dev): review-animations, animation-vocabulary, apple-design (2026-07-09)
- [[impeccable]] — design-language agent skill (Paul Bakaus): 23 commands + 46 deterministic detector rules; anti-slop design guidance for AI coding agents (2026-07-09)
- [[taste-skill]] — anti-slop frontend skill collection (Leonxlnx): style-specific skills + VARIANCE/MOTION/DENSITY dials; ships a research/laziness writeup on LLM slop (2026-07-09)
- [[token-efficiency]] — synthesis of the token-efficiency tooling landscape (input vs output compression, measurement, eval-rigor lesson) tying [[headroom]]/[[caveman]]/[[graphify]]/[[codeburn]] (2026-07-09)
- [[headroom]] — context/input compression layer (JSON/AST/prose compressors, reversible CCR, proxy/MCP); 60–95% JSON / 15–20% coding token cut; input-side complement to [[caveman]] (2026-07-09)
- [[codeburn]] — local-first AI-coding token/cost observability CLI (31 tools); 14-detector `optimize` waste scanner; the A/B measurement tool [[caveman]] recommends (2026-07-09)
- [[caveman]] — viral (87k★, verified) Claude Code token-compression skill; ~65% *output*-only cut, honest net-negative cases, reusable 3-arm eval methodology (2026-07-09)
- [[deep-research-agent]] — Elvis Saravia's Claude Agent SDK + Exa research agent; reference architecture for my [[my-find-research-papers-skill]] (2026-07-09)
- [[elvis-saravia]] — @omarsar / DAIR.AI entity page; profile scanned for paper-scanning tooling (2026-07-09)
- [[graphify]] — knowledge-graph skill for AI coding assistants; **unverified trust caveat** (stars mismatch, young repo, typosquat-pattern package name) (2026-07-05)
- [[nemotron-3-ultra]] — NVIDIA's 550B/55B MoE hybrid Mamba-Attention model, landing page + tech report ingested (2026-07-04)
- [[multi-teacher-on-policy-distillation]] — new concept page, MOPD post-training technique from Nemotron 3 Ultra (2026-07-04)
- [[storm-claude-skill-video]] — practitioner STORM implementation as Claude skill (2026-06-29)
- [[co-storm]] — full paper ingest from arXiv 2408.15232 (2026-06-29)
- [[wildseek]] — new entity page, evaluation dataset from Co-STORM (2026-06-29)
- [[storm]] — STORM system page, first ingest (2026-06-29)
- [[overview]] — evolving thesis initialized (2026-06-29)

## Domain sub-indexes
<!-- [[_index-<domain>]] — one-liner. Auto-created when a tag-cluster grows past ~8 pages. -->

## Overview
- [[overview]] — high-level summary and current thesis

## Sources
- [[agentsmd]] — BuildBetter blog: AGENTS.md Complete Guide for Engineering Teams (2026-07-13)
- [[storm]] — Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models (2026-06-29)
- [[co-storm]] — Into the Unknown Unknowns: Engaged Human Learning through Participation in LM Agent Conversations (2026-06-29)
- [[storm-claude-skill-video]] — Nate Herk: Stanford's Method Turns Claude Into a PhD Level Research Team (2026-06-29)
- [[opus-think-like-fable]] — Nate Herk: "How I Make Opus Think Like Fable" (process-over-model, model routing) (2026-07-09)
- [[cl4r1t4s]] — elder-plinius: extracted system prompts across major AI products (⚠ injection in README) (2026-07-09)
- [[nemotron-3-ultra]] — NVIDIA Nemotron 3 Ultra tech report, 550B/55B MoE hybrid Mamba-Attention model (2026-07-04)
- [[graphify]] — knowledge-graph skill for AI coding assistants — **unverified trust caveat** (2026-07-05)
- [[deep-research-agent]] — Claude Agent SDK + Exa deep-research web app (Elvis Saravia / omarsar) (2026-07-09)
- [[caveman]] — output-token compression Claude Code skill + honest eval harness (Julius Brussee) (2026-07-09)
- [[codeburn]] — local-first token/cost observability CLI across 31 AI coding tools (Agentseal) (2026-07-09)
- [[headroom]] — context/input compression layer for AI agents; library/proxy/MCP, reversible (headroomlabs-ai) (2026-07-09)
- [[impeccable]] — design language for AI coding agents; 23 commands + deterministic detector (Paul Bakaus) (2026-07-09)
- [[taste-skill]] — anti-slop frontend skill collection + LLM-laziness research (Leonxlnx) (2026-07-09)

## Entities
- [[stanford-oval]] — Stanford Open Virtual Assistant Lab
- [[elvis-saravia]] — @omarsar, founder of DAIR.AI; author of [[deep-research-agent]]
- [[monica-lam]] — Professor at Stanford, director of OVAL
- [[yijia-shao]] — PhD student, lead author of STORM
- [[yucheng-jiang]] — PhD student, lead author of Co-STORM
- [[freshwiki]] — Benchmark dataset of 100 high-quality recent Wikipedia articles
- [[wildseek]] — In-the-wild information-seeking dataset for evaluating complex search tools

## Concepts
- [[storm]] — LLM system for automated Wikipedia-like article generation
- [[co-storm]] — Collaborative extension of STORM with human-in-the-loop
- [[perspective-guided-question-asking]] — Multi-perspective question strategy
- [[simulated-conversation]] — Grounded multi-turn conversation simulation
- [[multi-teacher-on-policy-distillation]] — Dense token-level distillation from specialized teachers into one student (MOPD)
- [[token-efficiency]] — the token-efficiency tooling landscape: input vs output compression, measurement, eval-rigor lesson (ties headroom/caveman/graphify/codeburn)
- [[anti-slop-design]] — the "agents with taste" landscape: why LLMs slop, common anti-slop levers, deterministic design review (ties impeccable/taste-skill/emil-kowalski-skills)
- [[llm-laziness]] — output truncation & brevity bias: root causes (training bias, RLHF/compute, output limits, cognitive shortcuts) + remediation
- [[creative-frontend-effects]] — WebGL/visual-effects building blocks (R3F, liquid-glass-react, ShaderGradient, liquid-logo) for high-craft frontends

## Tools & links
- https://github.com/stanford-oval/storm — STORM source code [knowledge-curation, article-generation]
- https://storm.genie.stanford.edu/ — STORM live demo [knowledge-curation]
- https://huggingface.co/datasets/EchoShao8899/FreshWiki — FreshWiki dataset [dataset, evaluation]
- https://github.com/omarsar — Elvis Saravia / DAIR.AI GitHub profile [person, ai-agents]
- https://github.com/omarsar/deep-research-agent — Claude Agent SDK + Exa research agent [ai-agents, research-tooling]
- https://github.com/JuliusBrussee/caveman — output-token compression skill + eval harness [token-reduction, skill]
- https://github.com/getagentseal/codeburn — local token/cost observability CLI for AI coding tools [cost-tracking, observability]
- https://github.com/headroomlabs-ai/headroom — context/input compression layer (library/proxy/MCP) [token-reduction, context-compression]
- https://github.com/pbakaus/impeccable — design-language skill for AI coding agents [ai-design, anti-slop]
- https://github.com/leonxlnx/taste-skill — anti-slop frontend skill collection for AI agents [ai-design, anti-slop]
- https://github.com/emilkowalski/skills — animation-first design-engineer skills for AI agents [ai-design, animation]
- https://github.com/pmndrs/react-three-fiber — React renderer for Three.js (WebGL) [frontend, webgl] · see [[creative-frontend-effects]]
- https://github.com/rdev/liquid-glass-react — Apple Liquid Glass effect for React [frontend, visual-effects]
- https://shadergradient.co — animated 3D gradients for React/Framer/Figma (ruucm/shadergradient) [frontend, visual-effects]
- https://github.com/collidingScopes/liquid-logo — animated liquid-metal logo tool [frontend, visual-effects]
- https://exa.ai — Exa neural search API (search / get_contents / find_similar; date filters) [search, research-tooling]
