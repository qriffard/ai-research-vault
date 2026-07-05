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
