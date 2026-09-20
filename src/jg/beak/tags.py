from enum import StrEnum, auto


class TechTag(StrEnum):
    api = auto()
    c = auto()
    cpp = auto()
    csharp = auto()
    css = auto()
    database = auto()
    docker = auto()
    excel = auto()
    git = auto()
    hardware = auto()
    html = auto()
    java = auto()
    javascript = auto()
    kotlin = auto()
    linux = auto()
    php = auto()
    powerbi = auto()
    python = auto()
    ruby = auto()
    swift = auto()
    testing = auto()
    typescript = auto()
    dataanalysis = auto()
    rust = auto()


class TechLibTag(StrEnum):
    angular = auto()
    bootstrap = auto()
    django = auto()
    flask = auto()
    kubernetes = auto()
    mysql = auto()
    node = auto()
    pandas = auto()
    postgresql = auto()
    react = auto()
    svelte = auto()
    tailwind = auto()
    vue = auto()


class AITag(StrEnum):
    # General AI awareness / chat-level use (umbrella tag). Also emitted
    # alongside the more specific AI tags below, so a job that mentions AI
    # coding agents or building AI is always tagged ``ai`` too.
    ai = auto()
    # Uses AI coding agents (Claude Code, Cursor, Codex, Copilot, ...).
    aiagents = auto()
    # Builds AI/LLM features (LLM, RAG, embeddings, prompt engineering, ...).
    aibuild = auto()


Tag = TechTag | TechLibTag | AITag
