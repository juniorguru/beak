# Beak …🐤
Analyzes text, returns tags.

## Name
Why Beak? Because beaks are good at sorting out the interesting bits in peck feeds.

## AI tags
Beside the technology tags, Beak detects how a job posting relates to AI. The
tags are hierarchical — the more specific ones are always emitted together with
`ai`, so filtering for `ai` catches everything and the others catch a sharper
subset:

- **`ai`** — general AI awareness / chat-level use (the umbrella): bare "AI",
  "umělá inteligence", ChatGPT, "AI nástroje", "AI-first", …
- **`aiagents`** — uses AI *coding agents*: named tools (Claude Code, Cursor,
  Codex, Copilot, …) and coding-agent phrasing. Note that bare "AI agent" /
  "agentic" usually describes *building* agents, so it feeds `aibuild`, not this.
- **`aibuild`** — *builds* AI/LLM features: LLM, RAG, embeddings, prompt
  engineering, LangChain, vector databases, NLP, computer vision, …
- **`vibecoding`** — vibecoding as an attitude / way of working (implies
  `aiagents`): the many spellings of vibe/vajb + coding and the Czech verb
  forms, plus "vibe engineering" and "agentic engineering".

Individual products are intentionally *not* exposed as tags — ChatGPT and Claude
are an equivalent skill, Codex and Claude Code are an equivalent skill, and the
product names churn; what matters is the capability. A generic machine-learning
tag is skipped on purpose too, as it is low-volume and not relevant for juniors.

Two matching details worth knowing: the bare `AI`, `LLM`, `RAG` and `NLP`
abbreviations are matched case-sensitively (a case-insensitive `ai` would match
unrelated lowercase substrings), and the tag boundaries come from a scrape and
analysis of ~300 tech job postings on jobs.cz and startupjobs.cz.

## License
[AGPL-3.0-only](LICENSE), copyright (c) 2024–2026 Jan Javorek, and contributors.
