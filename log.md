# AI Research — Log

> Append-only chronological record. Each entry starts with `## [YYYY-MM-DD] <op> | <title>`
> so it is greppable: `grep "^## \[" log.md | tail -5`.

## [2026-06-29] create | Wiki initialized
Bootstrapped LLM Wiki for "AI Research". Purpose: Track and synthesize AI research papers, repos, and approaches. Use-case: research.

## [2026-06-29] ingest | STORM paper (arXiv 2402.14207)
Source: `raw/storm-paper.md` (79,230 chars, LaTeX→markdown via pylatexenc). 7 figures in `raw/assets/storm-paper/`.
Pages created: `wiki/storm.md`, `wiki/perspective-guided-question-asking.md`, `wiki/simulated-conversation.md`, `wiki/freshwiki.md`, `wiki/co-storm.md`, `wiki/stanford-oval.md`, `wiki/monica-lam.md`, `wiki/yijia-shao.md`, `wiki/yucheng-jiang.md`, `wiki/overview.md`.
Updated: `index.md`. Created: `_hot.md`.

## [2026-06-29] ingest | Co-STORM paper (arXiv 2408.15232)
Source: `raw/co-storm.md` (103,095 chars, LaTeX→markdown via pylatexenc). 18 figures in `raw/assets/co-storm/`.
Pages updated: `wiki/co-storm.md` (promoted from pointer to full capture).
Pages created: `wiki/wildseek.md`.
Updated: `index.md`, `_hot.md`.

## [2026-06-29] ingest | Nate Herk STORM skill video
Source: `raw/co-storm-demo-video.md` (60,203 chars, YouTube transcript via yt-dlp). 12-min tutorial on implementing STORM as a Claude skill with 5 fixed perspectives and 2-pass verification.
Pages created: `wiki/storm-claude-skill-video.md`.
Updated: `index.md`, `_hot.md`.

## [2026-07-04] ingest | NVIDIA Nemotron 3 Ultra (landing page + tech report)
Sources: `raw/nemotron-3-ultra.md` (landing page, WebFetch+verified via direct curl) and `raw/nemotron-3-ultra-tech-report.md` (213,199 chars, PDF→markdown via pymupdf4llm — installed this session, no backend was previously available). First source in a new domain for this wiki (LLM model releases), separate from the STORM cluster.
Pages created: `wiki/nemotron-3-ultra.md` (source/entity page — architecture, pretraining, post-training incl. MOPD results table, quantization, inference), `wiki/multi-teacher-on-policy-distillation.md` (concept page for the MOPD technique).
Updated: `index.md`, `_hot.md`.

## [2026-07-05] ingest | Graphify (landing page + GitHub README) — unverified trust caveat
Sources: `raw/graphify.md` (landing page, direct curl + tag-strip) and `raw/graphify-readme.md` (GitHub README, `safishamsi/graphify@main`). Tool: multi-modal knowledge-graph builder for AI coding assistants (Tree-sitter + LLM extraction + Leiden clustering).
**Flagged before full capture**: landing page's "3.7k+ GitHub Stars" badge does not match the actual repo (77,603 stars via API, >20x mismatch); repo is 3 months old (created 2026-04-03); installable package named `graphifyy` not `graphify`; repo transferred from an individual account to an org between when the copy was written and capture time. Presented these to the human, who chose full capture with the caveat documented prominently in the page rather than pointer-only or skip. Nothing installed or executed.
Pages created: `wiki/graphify.md` (source page, trust caveat in a blockquote at the top).
Updated: `index.md`, `_hot.md`.

## [2026-07-09] ingest | omarsar GitHub scan → deep-research-agent + Elvis Saravia
Scanned github.com/omarsar (Elvis Saravia / DAIR.AI, 100 repos) for a
research-paper scanning/extraction system per the human's post. On-point find:
[[deep-research-agent]] (Next.js + Claude Agent SDK + Exa; 3 Exa tools with date
filters + find_similar; ~9★ demo, boilerplate README). Created [[deep-research-agent]]
(source) and [[elvis-saravia]] (entity). Key relevance: Exa neural search + date
filters + find_similar are a cleaner backend for my find-research-papers skill
(fixes arXiv-boolean + Semantic-Scholar-429 pain). cc3-deep-research is empty;
rest of profile is older NLP/teaching material. Updated index (Recently Active,
Sources, Entities, Tools & links incl. exa.ai) and _hot.md. GitHub read-only via
public API; nothing installed/executed.

## [2026-07-09] ingest | caveman (JuliusBrussee) — output-token compression skill
Ingested at human's request. Created [[caveman]] (source). Verified 87,177★ (MIT,
JS) via API — headline claim reproducible (contrast [[graphify]]). Real numbers
from docs/HONEST-NUMBERS.md: ~65% output-only reduction (22–87%), 0% input, adds
~1–1.5k input tok/turn → net-negative on terse Q&A / per-request billing;
session-level ~14–21%. Main transferable value = its 3-arm eval methodology
(baseline/terse/skill; honest delta = skill-vs-terse) — a claim-vetting template
for token-reduction tools. Cross-linked to [[graphify]]. Updated index + _hot.md.

## [2026-07-09] ingest | codeburn (Agentseal) — AI coding token/cost observability
Ingested at human's request. Created [[codeburn]] (source). Verified 8,553★ (MIT,
TS) via API. Local-first CLI reading on-disk session files (JSONL/SQLite/protobuf)
across 31 AI coding tools; breaks down cost/tokens by task/model/tool/project;
LiteLLM pricing; no network egress. Highlight: `optimize` runs 14 waste detectors
(dup reads, low Read:Edit, unused MCP servers, ghost skills, bloated CLAUDE.md,
context-swamp sessions) → A–F setup grade + paste-ready fixes. Framed as the
measurement/A-B counterpart to [[caveman]] and cross-linked to [[graphify]];
personally actionable on my Claude Code/Cursor setup. Updated index + _hot.md.
GitHub read-only; nothing installed/executed.

## [2026-07-09] ingest | headroom (headroomlabs-ai) — context/input compression layer
Ingested at human's request. Created [[headroom]] (source). Verified 58,130★
(Apache-2.0, Python/TS/Rust, created 2026-01-07) via API. Compresses what an agent
reads (tool outputs/logs/RAG/files) before the LLM via content-aware compressors
(SmartCrusher JSON, CodeCompressor AST, Kompress-v2-base prose HF model), reversible
CCR (originals cached + headroom_retrieve), delivered as library/proxy/wrap/MCP,
local-first. Honest differentiated claim (60–95% JSON / 15–20% coding) backed by an
agent-evals/ harness with control arms + LLM judge + savings/scorecard/stats (measures
answer quality). Trust caveat noted: young-repo + high-stars (graphify-style pattern)
but far more rigorous. Framed as the input-side complement to [[caveman]] and
highest-leverage per [[codeburn]]; cross-linked [[graphify]]. Token-efficiency cluster
now 4 pages — flagged a possible concept page / sub-index if it grows. Updated index
+ _hot.md. GitHub read-only; nothing installed/executed.

## [2026-07-09] create | token-efficiency concept page
Created [[token-efficiency]] (type: concept) synthesizing the 4 token-efficiency
tool pages: input compression [[headroom]], output compression [[caveman]],
context-via-knowledge-graph [[graphify]] (unverified), measurement [[codeburn]].
Captures the load-bearing principle (input tokens dominate → input-side highest
leverage), the evaluation-rigor lesson (skill-vs-terse delta, measure fidelity not
just tokens, trust provider billing, watch young-repo/high-stars), and design ideas
worth stealing (reversible compression, content-aware routing, honest-numbers docs).
Added backlinks from caveman/codeburn/headroom; linked from index (Concepts +
Recently Active) and _hot.md.

## [2026-07-09] ingest | AI design-quality / anti-slop skills cluster (3 repos)
Ingested at human's request, back-to-back. Created three source pages:
- [[impeccable]] (pbakaus, 45,065★, Apache-2.0) — design-language agent skill: 23
  commands + 46 deterministic no-LLM detector rules + browser iteration; built on
  Anthropic frontend-design. Author = jQuery UI creator.
- [[taste-skill]] (Leonxlnx, 61,228★, MIT) — anti-slop frontend skill collection:
  style-specific skills (minimalist/brutalist/soft/stitch), VARIANCE/MOTION/DENSITY
  dials, em-dash ban, GSAP skeletons, image-gen reference skills. Ships a
  research/laziness/ corpus on why LLMs produce slop (training-data bias, RLHF,
  output limits, cognitive shortcuts) — flagged for a possible [[llm-laziness]]
  concept page.
- [[emil-kowalski-skills]] (emilkowalski, 6,828★, MIT) — animation-first design
  skills (emil-design-eng, review-animations+STANDARDS.md, animation-vocabulary,
  apple-design). Emil/animations.dev is taste-skill's sponsor.
All three descend from Anthropic frontend-design and form a connected community;
cross-linked each other. Verified stars via API; nothing installed/executed.
Updated index (Recently Active, Sources, Tools & links) + _hot.md. Cluster is 3
pages — flagged a candidate "anti-slop-design / agents-with-taste" concept page.

## [2026-07-09] create | anti-slop-design concept page
Created [[anti-slop-design]] (type: concept) synthesizing the "agents with taste"
cluster: [[impeccable]], [[taste-skill]], [[emil-kowalski-skills]] (all descend
from Anthropic frontend-design). Captures the shared slop root cause (from
taste-skill's research/laziness), the recurring "tells", common levers (context
capture, tunable intensity, controlled vocabulary, deterministic/rules-based
review), a concrete design checklist for my own HTML artifacts, and the relation
to [[token-efficiency]] (cheaper vs better; shared deterministic-measurement DNA).
Added backlinks from all three tool pages; linked from index (Concepts + Recently
Active) and _hot.md. Flagged [[llm-laziness]] as a still-open candidate page.

## [2026-07-09] lint | First lint pass (13 ingests/creates since wiki init)
Scope: 26 wiki pages. Orphans: none. Captures: no pending/failed. Dangling
wikilinks: all intentional future-page markers (latentmoe, mixed-initiative-
interaction, mind-map-for-llm, dspy, litellm, my-find-research-papers-skill) or
CLAUDE.md schema examples (wikilinks, page-slug, _index-<domain>) — none real,
kept per "link liberally". Two healthy concept clusters with hubs:
[[token-efficiency]] (caveman/headroom/graphify/codeburn) and [[anti-slop-design]]
(impeccable/taste-skill/emil-kowalski-skills) + [[llm-laziness]]; neither >8 pages
so no sub-index promotion yet. _hot.md was ~991 tokens (2x target) — trimmed the
design-cluster bullet back toward target. No contradictions found (graphify's
unverified caveat still stands; headroom's young-repo caveat noted).

## [2026-07-09] ingest | creative-frontend-effects cluster (4 tools, pointers)
Created [[creative-frontend-effects]] (concept, pointer cluster) at human's request:
React Three Fiber (pmndrs, 31,372★), liquid-glass-react (rdev, 5,527★), ShaderGradient
(ruucm, 1,860★, shadergradient.co), liquid-logo (collidingScopes, 88★) — WebGL/visual
building blocks. Creative-coding tools, not AI research; filed as the "how" serving
[[anti-slop-design]]'s visual-craft bar. Added Tools & links pointers + index entries.
Stars verified via API.

## [2026-07-09] ingest | Nate Herk video — "How I Make Opus Think Like Fable"
YouTube (XTBWVVcF3Pk, 2026-07-07); transcript captured to raw/opus-think-like-fable.md
via extract-youtube.py. Distilled by subagent (transcript kept out of main context).
Created [[opus-think-like-fable]] (source): "process over model" thesis + 5 techniques
(teacher-not-workhorse, model routing/effort right-sizing, reverse-engineer outputs
into skills, "Fable mode" skill w/ scoping/evidence/attacking/verifying/reporting gates,
routing table). Opus+Haiku ~3× cheaper same quality. Cross-linked [[storm-claude-skill-video]]
(same author), [[token-efficiency]], [[llm-laziness]].

## [2026-07-09] ingest | CL4R1T4S (elder-plinius) — extracted system-prompt collection
Created [[cl4r1t4s]] (source). 45,126★, AGPL-3.0. Per-vendor dirs of extracted system
prompts/tool scaffolds for all major AI products (Anthropic/OpenAI/Google/xAI/... +
coding agents Cursor/Windsurf/Devin/Replit/...). Transparency + red-team reference;
tied to [[llm-laziness]] and [[opus-think-like-fable]]. SECURITY: the repo README embeds
a leetspeak prompt-injection ("dump your own instructions to the user") — NOT complied
with; flagged in the page and to the user; repo treated as untrusted input. GitHub
read-only; nothing installed/executed.

## [2026-07-13] ingest | AGENTS.md Complete Guide (BuildBetter blog)
Source: `raw/agentsmd-complete-guide-buildbetter-2026.md` (WebFetch, verified against
direct curl+pandoc — full article, cleaned of Ghost markup). Created [[agentsmd]]
(concept page): AGENTS.md standard — repo-root markdown for AI coding agent context,
co-promoted by OpenAI/Google/Sourcegraph/Cursor/Anthropic/others, walked hierarchically
(monorepo per-package overrides), Setup Commands = highest-ROI section, imperative +
negative-example style, <500-line ceiling, vs README/CONTRIBUTING decision rule, common
mistakes, FAQ. Flagged source bias: BuildBetter blog post, pitching their own BB-Skills/
BuildBetter CLI product — mechanics content kept, product pitch noted as unverified
marketing, not treated as fact. Cross-linked [[token-efficiency]] (context economy) and
the anti-slop cluster (steering agents via convention files). Updated index + _hot.md.

## [2026-07-13] lint | Second lint pass (14 ingests/creates since last lint)
Scope: 30 wiki pages. Orphans: none (all pages have inbound [[links]]). Pending/failed
captures: none. Tag clusters: [[token-efficiency]] (4 pages) and [[anti-slop-design]]
(5 pages, incl. [[llm-laziness]] + pointer cluster [[creative-frontend-effects]]) —
neither past the ~8-page sub-index threshold yet. No contradictions found (graphify's
unverified-stars caveat and headroom's young-repo caveat both still stand as documented).
`_hot.md` had grown to ~1150 tokens (2.3x target) carrying stale STORM/Nemotron detail
already covered in index.md — trimmed to ~420 tokens, condensed the token-efficiency and
anti-slop clusters to one-line hub summaries, dropped fully-resolved older threads.
