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
