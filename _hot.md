# Hot cache

## Active threads
- **[[deep-research-agent]] ingested (Elvis Saravia / @omarsar).** Claude Agent SDK + **Exa** research agent — 3 Exa tools (`search` w/ date filters, `get_contents`, `find_similar`), broad-search→deep-dive→find-similar→synthesize loop. Reference architecture for my [[my-find-research-papers-skill]]; **Exa's `find_similar` + date filters** solve my arXiv-boolean + Semantic-Scholar-429 pain. Small demo repo (~9★, boilerplate README). See also [[elvis-saravia]].
- **[[token-efficiency]] concept page created** — synthesizes the 4-tool token landscape: input compression ([[headroom]]) vs output compression ([[caveman]]) vs context-via-KG ([[graphify]], unverified) vs measurement ([[codeburn]]). Load-bearing principle: **input tokens dominate** → input-side compression is highest-leverage; output-only tools cap ~14–21% session-level. Eval-rigor lesson: measure skill-vs-terse (not vs nothing) + fidelity (not just token delta) + provider billing; watch young-repo/high-stars.
- **AI design-quality / anti-slop cluster ingested (3 repos, 2026-07-09):** [[impeccable]] (Paul Bakaus/jQuery UI, 45k★, Apache-2.0 — 23 commands + 46 deterministic no-LLM detector rules), [[taste-skill]] (Leonxlnx, 61k★, MIT — style-specific skills + VARIANCE/MOTION/DENSITY dials; ships a `research/laziness/` writeup on *why* LLMs produce slop: training-data bias, RLHF, output limits), and [[emil-kowalski-skills]] (Emil Kowalski/animations.dev, 6.8k★, MIT — animation-first: review-animations+STANDARDS.md, animation-vocabulary, apple-design). All descend from Anthropic `frontend-design`; Emil sponsors taste-skill. Distinct from the token cluster. **Candidate concept page: anti-slop-design / agents-with-taste.** Concrete rules directly usable for my HTML digests.
- **[[headroom]] ingested (headroomlabs-ai, 58k★, Apache-2.0).** **Input/context** compression layer — compresses tool outputs/logs/RAG/files before the LLM. Content-aware compressors (SmartCrusher JSON / CodeCompressor AST / Kompress-v2-base prose), **reversible CCR** (originals cached, `headroom_retrieve` on demand), library/proxy/wrap/MCP, local-first. Honest differentiated claim: **60–95% JSON / 15–20% coding**; backed by an `agent-evals/` harness w/ judge (measures answer quality, not just token delta). Trust caveat: young repo (created 2026-01) + huge stars = graphify-style pattern, but far more rigorous. Input-side complement to [[caveman]]; highest-leverage per [[codeburn]] (input dominates). Token cluster now 4 pages (caveman/headroom/graphify/codeburn).
- **[[codeburn]] ingested (Agentseal, verified 8.5k★).** Local-first CLI tracking AI-coding token usage/cost across 31 tools by task/model/tool/project; reads on-disk session files, no egress, LiteLLM pricing. Key: `optimize` = 14 waste detectors (dup file reads, low Read:Edit, unused MCP, ghost skills, bloated CLAUDE.md) → A–F health grade + paste-ready fixes. The measurement/A-B tool [[caveman]] recommends; personally actionable on my own CC/Cursor setup.
- **[[caveman]] ingested (Julius Brussee, verified 87k★).** Output-token compression Claude Code skill. Real numbers: ~65% *output* cut (22–87%), 0% input, **adds ~1–1.5k input tokens/turn** → net-negative on terse Q&A / per-request billing; session-level only ~14–21%. Big takeaway = its **3-arm eval methodology** (baseline / terse / skill; honest delta = skill-vs-terse, not skill-vs-baseline) — the claim-vetting bar [[graphify]] failed.
- **[[graphify]] ingested — carries an unverified trust caveat.** Landing page badge says 3.7k+ GitHub stars; actual repo has 77,603 (>20x mismatch), repo is only 3 months old, package is named `graphifyy` not `graphify`. Nothing installed/executed — flagged to the human, treat as unverified until independently re-checked.
- Nemotron 3 Ultra ingested (landing page + tech report) — [[nemotron-3-ultra]], new domain for this wiki (LLM model releases, distinct from the STORM cluster)
- New concept page [[multi-teacher-on-policy-distillation]] (MOPD) extracted from the Nemotron report — watch for it recurring in future post-training paper ingests
- Co-STORM paper ingested (arXiv 2408.15232) — [[co-storm]] page fully captured
- Nate Herk STORM skill video ingested — [[storm-claude-skill-video]]
- Wiki has 6 captured sources: [[storm]], [[co-storm]], [[storm-claude-skill-video]], [[nemotron-3-ultra]] (2 raw docs), [[graphify]] (2 raw docs)

## Key numbers
- Nemotron 3 Ultra: 550B total / 55B active params, 20T pretrain tokens, 1M context
- Nemotron 3 Ultra throughput vs GLM-5.1/Kimi-K2.6/Qwen-3.5: 5.9x / 4.8x / 1.6x (8K/64K)
- Nemotron 3 Ultra quantization: 5.03 bits-per-element (NVFP4 + mixed FP8) selected
- Graphify: claims 71.5x token reduction on a 52-file mixed corpus vs. reading raw files; claimed vs actual GitHub stars: 3.7k+ (site) vs 77,603 (API)
- Co-STORM: 70% prefer over search engine, 78% over RAG chatbot (N=20)
- Moderator utterances: 89% rated as steering toward new/interesting direction
- STORM: +25% organization, +10% coverage vs oRAG; 84.83% citation recall
- Nate Herk skill: 5 fixed perspectives + 2-pass verification pipeline

## Next
- STORM GitHub repo README has implementation details worth capturing
- Consider ingesting a multi-agent systems survey for broader context
- Potential concept pages: [[mixed-initiative-interaction]], [[mind-map-for-llm]], [[latentmoe]]
- pymupdf4llm now installed in this environment — future PDF ingests (arXiv fallback, tech reports) can use it directly
- If revisiting [[graphify]]: check current GitHub star count/contributor history before recommending it for actual use, and compare its `--wiki` god-node/EXTRACTED-INFERRED-AMBIGUOUS edge tagging against this vault's own index conventions
