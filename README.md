# Beak …🐤
Analyzes text, returns tags.

## Name
Why Beak? Because beaks are good at sorting out the interesting bits in peck feeds.

## AI tags
The technology tags include tags for how a text relates to AI. These tags are
hierarchical — the more specific ones are always emitted together with `ai`,
so filtering for `ai` catches everything and the others catch a sharper subset:

- **`ai`** — general AI awareness / chat-level use (the baseline): bare "AI",
  "umělá inteligence", ChatGPT, "AI nástroje", "AI-first", …
- **`agenticengineering`** — uses AI *coding agents*: named tools (Claude Code, Cursor,
  Codex, Copilot, …) and coding-agent phrasing. Bare "AI agent" is deliberately
  not mapped here — it usually means *building* agents, not using a coding
  assistant, so it only trips the general `AI` → `ai` rule, while "agentic
  architecture / systems" goes to `buildingai`.
- **`buildingai`** — *builds* AI / ML features: LLM, RAG, embeddings, prompt
  engineering, LangChain, vector databases, NLP, computer vision, and classic
  machine learning (machine learning, strojové učení, neural networks,
  TensorFlow, PyTorch, scikit-learn, MLOps, …).
- **`vibecoding`** — vibecoding as an attitude / way of working (implies
  `agenticengineering`): the many spellings of vibe/vajb + coding and the Czech verb
  forms, plus "vibe engineering" and "agentic engineering".

Individual products are intentionally *not* exposed as tags — ChatGPT and Claude
are an equivalent skill, Codex and Claude Code are an equivalent skill, and the
product names churn; what matters is the capability.

Two matching details worth knowing: the bare `AI`, `ML`, `LLM`, `RAG` and `NLP`
abbreviations are matched case-sensitively (a case-insensitive `ai` would match
unrelated lowercase substrings), and the tag boundaries come from a scrape and
analysis of ~300 tech job postings on jobs.cz and startupjobs.cz.

## Adding or editing rules
The matching rules live in [`src/jg/beak/mapping.toml`](src/jg/beak/mapping.toml)
as a list of `[[rule]]` entries — no Python needed. Each rule is a regex plus
the tags it produces:

```toml
[[rule]]
pattern = 'claude code'
tags = ["ai", "agenticengineering"]
```

Conventions applied when the file is loaded:

- Matching is **case-insensitive** by default; set `case_sensitive = true` to
  turn it off (e.g. for `AI`, `ML` — a case-insensitive `ai` would match
  unrelated substrings).
- A plain space between words expands to `\s+`, so `claude code` also matches
  `claude  code` and `claude\ncode`. Use explicit `\s*` / `\s?` / `\x20` when
  you need something other than "one or more whitespace".
- The pattern is wrapped in `\b…\b` (whole-word match) automatically; set
  `treat_as_word = false` to match anywhere.
- Every tag is validated against the enums in `tags.py` on load, so a typo
  fails fast.

## License
[AGPL-3.0-only](LICENSE), copyright (c) 2024–2026 Jan Javorek, and contributors.
