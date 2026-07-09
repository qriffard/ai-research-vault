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
