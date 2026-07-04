# Hot cache

## Active threads
- Nemotron 3 Ultra ingested (landing page + tech report) — [[nemotron-3-ultra]], new domain for this wiki (LLM model releases, distinct from the STORM cluster)
- New concept page [[multi-teacher-on-policy-distillation]] (MOPD) extracted from the Nemotron report — watch for it recurring in future post-training paper ingests
- Co-STORM paper ingested (arXiv 2408.15232) — [[co-storm]] page fully captured
- Nate Herk STORM skill video ingested — [[storm-claude-skill-video]]
- Wiki has 5 captured sources: [[storm]], [[co-storm]], [[storm-claude-skill-video]], [[nemotron-3-ultra]] (2 raw docs)

## Key numbers
- Nemotron 3 Ultra: 550B total / 55B active params, 20T pretrain tokens, 1M context
- Nemotron 3 Ultra throughput vs GLM-5.1/Kimi-K2.6/Qwen-3.5: 5.9x / 4.8x / 1.6x (8K/64K)
- Nemotron 3 Ultra quantization: 5.03 bits-per-element (NVFP4 + mixed FP8) selected
- Co-STORM: 70% prefer over search engine, 78% over RAG chatbot (N=20)
- Moderator utterances: 89% rated as steering toward new/interesting direction
- STORM: +25% organization, +10% coverage vs oRAG; 84.83% citation recall
- Nate Herk skill: 5 fixed perspectives + 2-pass verification pipeline

## Next
- STORM GitHub repo README has implementation details worth capturing
- Consider ingesting a multi-agent systems survey for broader context
- Potential concept pages: [[mixed-initiative-interaction]], [[mind-map-for-llm]], [[latentmoe]]
- pymupdf4llm now installed in this environment — future PDF ingests (arXiv fallback, tech reports) can use it directly
