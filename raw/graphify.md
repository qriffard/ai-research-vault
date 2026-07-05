# Graphify — landing page

Source: https://graphify.net/
Captured: 2026-07-05 (direct curl + manual tag-stripping, cross-checked
against WebFetch summary)

Graphify — Open-Source Knowledge Graph Skill for AI Coding Assistants

## What is Graphify?
Graphify is a multi-modal knowledge graph builder created for AI coding
assistants such as Claude Code, OpenAI Codex and OpenCode. By combining
Tree-sitter static analysis with LLM-driven semantic extraction, Graphify
turns an entire repository — including source code, documentation, research
papers and diagrams — into an interactive graph that explains both what the
code does and why it was designed that way. The project is maintained by Safi
Shamsi, released under the permissive MIT license, and built on widely-trusted
libraries including NetworkX and Tree-sitter.

Badges shown on the page: "3.7k+ GitHub Stars", "MIT License", "71.5x Token
Reduction", "Python 3.10+ Runtime".

Install line shown: `pip install graphifyy`

## Core Capabilities
- **Multi-Modal Extraction** — Parses code (.py, .js, .go, .java, …),
  Markdown, PDFs and images. Tree-sitter extracts ASTs, call graphs and
  docstrings; LLMs extract concepts from prose; vision models read diagrams.
- **Knowledge Graph Build** — Merges all extracted nodes and edges into a
  NetworkX graph and applies the Leiden algorithm for semantic community
  detection — no vector embeddings required.
- **God Nodes & Surprises** — Identifies the highest-degree "god nodes" at the
  heart of the system and flags unexpected cross-file or cross-domain
  connections worth investigating.
- **Interactive Outputs** — Exports an interactive `graph.html`, a queryable
  `graph.json`, and a human-readable `GRAPH_REPORT.md` audit report.
- **Assistant Integration** — Ships with `/graphify`, `/graphify query`,
  `/graphify path` and `/graphify explain` commands for Claude Code, Codex,
  OpenCode and more.
- **Secure by Design** (as claimed) — Strict input validation: only http/https
  URLs, size and timeout limits, path containment, HTML-escaped node labels —
  defending against SSRF, injection and XSS.

## Architecture & Pipeline
Multi-stage pipeline, each stage an isolated module:
`detect` (collect files) -> `extract` (AST + LLM nodes/edges) -> `build`
(NetworkX graph) -> `cluster` (Leiden communities) -> `analyze` (god nodes &
surprises) -> `report` (GRAPH_REPORT.md) -> `export` (HTML / JSON / Obsidian).

Supporting modules: `ingest.py` (URL fetching), `cache.py` (semantic caching),
`security.py` (input validation), `watch.py` (live updates), `serve.py`
(MCP-protocol service).

Per the page, Graphify does not bundle an LLM — it uses the model API key
already configured by the host AI coding assistant, and claims to send "only
semantic content — never raw source code — to the upstream model."

## Worked examples (as advertised)
- httpx (small): 6 Python files -> 144 nodes, 330 edges, 6 communities.
- Karpathy repos + 5 papers + 4 images: 52 files -> 71.5x token reduction.
- graphify source + Transformer paper: 4 files -> 5.4x token reduction.

## Links
- GitHub: https://github.com/safishamsi/graphify (API redirects to
  `Graphify-Labs/graphify`, see caution note in the wiki page)
- PyPI: https://pypi.org/project/graphifyy/
- SECURITY.md: https://github.com/safishamsi/graphify/blob/v3/SECURITY.md
