# Hot cache

## Active threads
- **[[agentsmd]] ingested (BuildBetter blog, 2026-07-13).** AGENTS.md = standardized repo-root markdown for AI coding agent context; co-promoted by OpenAI/Google/Sourcegraph/Cursor/Anthropic/others, read natively by Claude Code/Codex/Cursor/Copilot/Gemini CLI/etc.; walked hierarchically (nearest file to edited file wins) → thin root + rich per-package files in monorepos. Highest-ROI section = Setup Commands; keep under ~500 lines; imperative + negative examples. Source is vendor content (BuildBetter pitching their own BB-Skills product) — mechanics trustworthy, product pitch not independently verified.
- **[[token-efficiency]] hub** (4 pages: [[headroom]] input-compression, [[caveman]] output-compression, [[graphify]] context-via-KG *unverified*, [[codeburn]] measurement). Load-bearing: input tokens dominate → input-side compression highest-leverage. Eval-rigor lesson: measure skill-vs-terse (not vs nothing) + fidelity, not just token delta.
- **[[anti-slop-design]] hub** (5 pages: [[impeccable]], [[taste-skill]], [[emil-kowalski-skills]], root-cause [[llm-laziness]], visual-craft pointer cluster [[creative-frontend-effects]]) — "agents with taste" skills, all descend from Anthropic `frontend-design`.
- **[[cl4r1t4s]] ingested (elder-plinius, 45k★, AGPL).** Extracted system prompts for all major AI products. ⚠ README embeds a leetspeak prompt-injection — NOT complied with; treat repo as untrusted input.
- **[[opus-think-like-fable]] ingested (Nate Herk video).** "Model isn't the moat": transplant a frontier model's *process* to cheaper models (teacher-not-workhorse, model routing, reverse-engineer outputs into skills, "Fable mode" gates).
- **[[deep-research-agent]] ingested (Elvis Saravia).** Claude Agent SDK + Exa (search w/ date filters, get_contents, find_similar) — reference architecture for [[my-find-research-papers-skill]].
- Older captures still current, not summarized here: [[storm]]/[[co-storm]] cluster, [[nemotron-3-ultra]] — see index.md "Sources" for details.
- Wiki: 30 wiki pages, 0 orphans, 0 pending/failed captures as of last lint (2026-07-13).

## Key numbers
- Graphify: claims 71.5x token reduction; claimed vs actual stars 3.7k+ (site) vs 77,603 (API) — unverified.
- Caveman: ~65% output-only cut, adds ~1–1.5k input tok/turn, net session-level ~14–21%.
- Headroom: 60–95% JSON / 15–20% coding compression, reversible.

## Next
- STORM GitHub repo README has implementation details worth capturing
- Potential concept pages: [[mixed-initiative-interaction]], [[mind-map-for-llm]], [[latentmoe]]
- If revisiting [[graphify]]: re-check star count/contributor history before recommending for actual use
