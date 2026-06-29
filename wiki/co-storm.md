---
title: "Co-STORM: Collaborative STORM"
type: concept
date: 2026-06-29
sources: 1
tags: [knowledge-curation, human-in-the-loop, collaborative-ai]
source_url: https://arxiv.org/abs/2408.15232
captured: none (pointer)
---

# Co-STORM

**Co-STORM** (Collaborative STORM) extends [[storm]] with human-in-the-loop
collaboration for knowledge curation. Published at EMNLP 2024.

## Key additions over STORM

- **Collaborative discourse protocol** with turn management between three
  participant types:
  - **LLM experts** — answer questions grounded in external sources, raise
    follow-ups.
  - **Moderator** — generates thought-provoking questions from information found
    but not yet discussed.
  - **Human user** — can observe passively or actively steer the conversation.
- **Dynamic mind map** — a hierarchical concept structure that organizes
  collected information, creating a shared conceptual space between human and
  system. Reduces cognitive load during long research sessions.

## API

```python
costorm_runner.warm_start()         # build shared conceptual space
conv_turn = costorm_runner.step()   # observe
costorm_runner.step(user_utterance="...")  # steer
article = costorm_runner.generate_report()
```

## Related

- [[storm]]
- [[perspective-guided-question-asking]]
- [[simulated-conversation]]
