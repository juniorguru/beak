# Beak …🐤
Analyzes text, returns tags.

## Name
Why Beak? Because beaks are good at sorting out the interesting bits in peck feeds.

## AI tags
Beside the technology tags, Beak detects how a text relates to AI. The tags are
hierarchical — the more specific ones are always emitted together with `chat`,
so filtering for `chat` catches everything and the others catch a sharper subset:

- **`chat`** — general AI awareness / chat-level use (the baseline): bare "AI",
  "umělá inteligence", ChatGPT, "AI nástroje", "AI-first", …
- **`agents`** — uses AI *coding agents*: named tools (Claude Code, Cursor,
  Codex, Copilot, …) and coding-agent phrasing. Bare "AI agent" is deliberately
  not mapped here — it usually means *building* agents, not using a coding
  assistant, so it only trips the general `AI` → `chat` rule, while "agentic
  architecture / systems" goes to `build`.
- **`build`** — *builds* AI / ML features: LLM, RAG, embeddings, prompt
  engineering, LangChain, vector databases, NLP, computer vision, and classic
  machine learning (machine learning, strojové učení, neural networks,
  TensorFlow, PyTorch, scikit-learn, MLOps, …).
- **`vibecoding`** — vibecoding as an attitude / way of working (implies
  `agents`): the many spellings of vibe/vajb + coding and the Czech verb
  forms, plus "vibe engineering" and "agentic engineering".

Individual products are intentionally *not* exposed as tags — ChatGPT and Claude
are an equivalent skill, Codex and Claude Code are an equivalent skill, and the
product names churn; what matters is the capability.

Two matching details worth knowing: the bare `AI`, `ML`, `LLM`, `RAG` and `NLP`
abbreviations are matched case-sensitively (a case-insensitive `ai` would match
unrelated lowercase substrings), and the tag boundaries come from a scrape and
analysis of ~300 tech job postings on jobs.cz and startupjobs.cz.

## License
[AGPL-3.0-only](LICENSE), copyright (c) 2024–2026 Jan Javorek, and contributors.
