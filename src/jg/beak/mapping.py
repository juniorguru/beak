import re

from jg.beak.tags import AITag, TechLibTag, TechTag


MAPPING = {
    re.compile(r"\bpython\w*\b", re.I): [TechTag.python],
    re.compile(r"\bsql\b", re.I): [TechTag.database],
    re.compile(r"\bdatab[aá][sz]e\b", re.I): [TechTag.database],
    re.compile(r"\bphp\b", re.I): [TechTag.php],
    re.compile(r"\b(nette|laravel|symfony)\w*\b", re.I): [TechTag.php],
    re.compile(r"\bmysql\b", re.I): [TechTag.database, TechLibTag.mysql],
    re.compile(r"\bpostgre\w+\b", re.I): [TechTag.database, TechLibTag.postgresql],
    re.compile(r"\bkubernet\w*\b", re.I): [TechTag.docker, TechLibTag.kubernetes],
    re.compile(r"\bdocker\w*\b", re.I): [TechTag.docker],
    re.compile(r"\blinux\w*\b", re.I): [TechTag.linux],
    re.compile(r"\bswift\w*\b", re.I): [TechTag.swift],
    re.compile(r"\bdjang\w+\b", re.I): [TechLibTag.django],
    re.compile(r"\bflask\w*\b", re.I): [TechTag.python, TechLibTag.flask],
    re.compile(r"\bpandas\b", re.I): [TechTag.python, TechLibTag.pandas],
    re.compile(r"\bexcel\w*\b", re.I): [TechTag.excel],
    re.compile(r"\bpower ?bi\b", re.I): [TechTag.powerbi],
    re.compile(r"\bjavascript\w*\b", re.I): [TechTag.javascript],
    re.compile(r"\bJS\b"): [TechTag.javascript],
    re.compile(r"\btypescript\w*\b", re.I): [TechTag.javascript, TechTag.typescript],
    re.compile(r"\bTS\b"): [TechTag.javascript, TechTag.typescript],
    re.compile(r"\bHTML\b"): [TechTag.html],
    re.compile(r"\bCSS\b"): [TechTag.css],
    re.compile(r"\bfront\-?end\w*\b", re.I): [
        TechTag.html,
        TechTag.css,
        TechTag.javascript,
    ],
    re.compile(r"\bbootstrap\w*\b", re.I): [TechTag.css, TechLibTag.bootstrap],
    re.compile(r"\btailwind\w*\b", re.I): [TechTag.css, TechLibTag.tailwind],
    re.compile(r"\bC\#\W"): [TechTag.csharp],
    re.compile(r"\.NET\b", re.I): [TechTag.csharp],
    re.compile(r"\bdotne[tť]\w*\b", re.I): [TechTag.csharp],
    re.compile(r"\b(java|javy|javě|javu|javou)\b", re.I): [TechTag.java],
    re.compile(r"\bkotlin\w*\b", re.I): [TechTag.kotlin],
    re.compile(r"\bC\+\+\W"): [TechTag.cpp],
    re.compile(r"\breact\w*\b", re.I): [TechTag.javascript, TechLibTag.react],
    re.compile(r"\bvue(\.js)?\b", re.I): [TechTag.javascript, TechLibTag.vue],
    re.compile(r"\bangular\w*\b", re.I): [TechTag.javascript, TechLibTag.angular],
    re.compile(r"\.?js\b", re.I): [TechTag.javascript],
    re.compile(r"\bjquery\b", re.I): [TechTag.javascript],
    re.compile(r"\bAPI\b"): [TechTag.api],
    re.compile(r"\bFastAPI\b", re.I): [TechTag.api, TechTag.python],
    re.compile(r"\bruby\b", re.I): [TechTag.ruby],
    re.compile(r"\bRoR\b"): [TechTag.ruby],
    re.compile(r"\bruby\s*on\s*rails\b", re.I): [TechTag.ruby],
    re.compile(r"\bjazyk[au]\s+c\b(?![#+])", re.I): [TechTag.c],
    re.compile(r"\bcéčk\w\b", re.I): [TechTag.c],
    re.compile(r"\bc(/|\s+a\s+)c[\+p]{2}\b", re.I): [TechTag.c, TechTag.cpp],
    re.compile(r"\bhardwar\w+", re.I): [TechTag.hardware],
    re.compile(r"\btesting\b", re.I): [TechTag.testing],
    re.compile(r"\btestov\w+", re.I): [TechTag.testing],
    re.compile(r"\bgit\b", re.I): [TechTag.git],
    re.compile(r"\bsvelte(kit)?\b", re.I): [TechLibTag.svelte],
    re.compile(r"\bdatov\w+\s+anal[yý][sz]\w+", re.I): [TechTag.dataanalysis],
    re.compile(r"\bnode\.js\b", re.I): [TechTag.javascript, TechLibTag.node],
    re.compile(r"\bRust\b"): [TechTag.rust],
    re.compile(r"\bSpringBoot\b", re.I): [TechTag.java],
    re.compile(r"\bSpring\s*Framework\b", re.I): [TechTag.java],
    re.compile(r"\bRP[iI]\b"): [TechTag.hardware],
    re.compile(r"\brapsberr?ypi\b", re.I): [TechTag.hardware],
    re.compile(r"\barduin\w+", re.I): [TechTag.hardware],
    # --- AI: general awareness / chat-level use -> [ai] ---
    # NOTE: the bare "AI" / "A.I." / "ML"-style abbreviations are matched
    # case-sensitively on purpose; a case-insensitive \bai\b would match
    # unrelated lowercase substrings.
    re.compile(r"\bAI\b"): [AITag.ai],
    re.compile(r"\bA\.I\."): [AITag.ai],
    re.compile(r"\bum[ěe]l[áa]\w*\s+inteligenc\w+", re.I): [AITag.ai],
    re.compile(r"\bartificial intelligence\b", re.I): [AITag.ai],
    re.compile(r"\bchat\s?gpt\b", re.I): [AITag.ai],
    re.compile(r"\bgemini\b", re.I): [AITag.ai],
    re.compile(r"\bclaude\b", re.I): [AITag.ai],
    re.compile(r"\bAI[-\s]?n[áa]stroj\w+", re.I): [AITag.ai],
    re.compile(r"\bAI tools?\b", re.I): [AITag.ai],
    re.compile(
        r"\bAI[-\s](first|native|driven|powered|assisted|ready)\b", re.I
    ): [AITag.ai],
    # --- AI: uses AI coding agents -> [ai, aiagents] ---
    re.compile(r"\bclaude code\b", re.I): [AITag.ai, AITag.aiagents],
    re.compile(r"\bcursor\b", re.I): [AITag.ai, AITag.aiagents],
    re.compile(r"\bcodex\b", re.I): [AITag.ai, AITag.aiagents],
    re.compile(r"\bcopilot\b", re.I): [AITag.ai, AITag.aiagents],
    re.compile(
        r"\b(windsurf|opencode|aider|tabnine|codeium|supermaven)\b", re.I
    ): [AITag.ai, AITag.aiagents],
    re.compile(r"\bjetbrains ai\b", re.I): [AITag.ai, AITag.aiagents],
    re.compile(r"\b(ai\s+)?coding agent\w*\b", re.I): [AITag.ai, AITag.aiagents],
    re.compile(r"\bagentic (development|dev|coding|pm)\b", re.I): [
        AITag.ai,
        AITag.aiagents,
    ],
    # Vibecoding as an attitude / way of working. Covers English and Czech
    # phonetic spellings (vibe/vajb + coding/kóding/...), the Czech verb
    # (navajbit, vajbovat, ...) with its declension, and "vibe/agentic
    # engineering". Implies aiagents (and therefore ai).
    re.compile(
        r"\b(?:(?:na)?vajb\w*"
        r"|(?:vibe|vajb)[\s-]?(?:cod|kod|cód|kód)\w+"
        r"|(?:vibe|vajb)[\s-]?engineering\w*"
        r"|agentic[\s-]?engineering\w*)\b",
        re.I,
    ): [AITag.ai, AITag.aiagents, AITag.vibecoding],
    re.compile(r"\bpracovat agentn\w+", re.I): [AITag.ai, AITag.aiagents],
    # --- AI: builds AI/LLM features -> [ai, aibuild] ---
    re.compile(r"\bLLMs?\b"): [AITag.ai, AITag.aibuild],
    re.compile(r"\blarge language model\w*", re.I): [AITag.ai, AITag.aibuild],
    re.compile(r"\bRAG\b"): [AITag.ai, AITag.aibuild],
    re.compile(r"\bretrieval[-\s]augmented\b", re.I): [AITag.ai, AITag.aibuild],
    re.compile(r"\bembedding\w*", re.I): [AITag.ai, AITag.aibuild],
    re.compile(r"\bfine[-\s]?tun\w+", re.I): [AITag.ai, AITag.aibuild],
    re.compile(r"\bprompt engineer\w*", re.I): [AITag.ai, AITag.aibuild],
    re.compile(r"\b(langchain|llama[-\s]?index|semantic kernel)\b", re.I): [
        AITag.ai,
        AITag.aibuild,
    ],
    re.compile(r"\bvector\s?(database|db)\b", re.I): [AITag.ai, AITag.aibuild],
    re.compile(r"\bvektorov\w+\s+datab\w+", re.I): [AITag.ai, AITag.aibuild],
    re.compile(r"\b(pinecone|qdrant|weaviate)\b", re.I): [AITag.ai, AITag.aibuild],
    re.compile(r"\bmulti[-\s]?agent\w*\b", re.I): [AITag.ai, AITag.aibuild],
    re.compile(r"\bNLP\b"): [AITag.ai, AITag.aibuild],
    re.compile(r"\bcomputer vision\b", re.I): [AITag.ai, AITag.aibuild],
    re.compile(r"\bpo[čc][íi]ta[čc]ov\w+\s+vid[ěe]n\w+", re.I): [
        AITag.ai,
        AITag.aibuild,
    ],
}
