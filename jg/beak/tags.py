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
    windows = auto()


class TechLibTag(StrEnum):
    angular = auto()
    bootstrap = auto()
    django = auto()
    flask = auto()
    kubernetes = auto()
    mongo = auto()
    mysql = auto()
    next = auto()
    node = auto()
    pandas = auto()
    postgresql = auto()
    react = auto()
    svelte = auto()
    tailwind = auto()
    vue = auto()


Tag = TechTag | TechLibTag
