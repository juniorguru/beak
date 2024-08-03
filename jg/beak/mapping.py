import re

from jg.beak.tags import TechLibTag, TechTag


MAPPING = {
    re.compile(r"\bpython\w*\b", re.I): [TechTag.python],
    re.compile(r"\bsql\b", re.I): [TechTag.database],
    re.compile(r"\bdatab[aá][sz]e\b", re.I): [TechTag.database],
    re.compile(r"\bphp\b", re.I): [TechTag.php],
    re.compile(r"\b(nette|laravel|symfony)\w*\b", re.I): [TechTag.php],
    re.compile(r"\bmysql\b", re.I): [TechTag.database, TechLibTag.mysql],
    re.compile(r"\bmongo\w*\b", re.I): [TechTag.database, TechLibTag.mongo],
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
    re.compile(r"\bdatab(aá)ze\b"): [TechTag.database],
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
    re.compile(r"\b\.NET\b", re.I): [TechTag.csharp],
    re.compile(r"\b(java|javy|javě|javu|javou)\b", re.I): [TechTag.java],
    re.compile(r"\bkotlin\w*\b", re.I): [TechTag.kotlin],
    re.compile(r"\bC\+\+\W"): [TechTag.cpp],
    re.compile(r"\breact\w*\b", re.I): [TechTag.javascript, TechLibTag.react],
    re.compile(r"\bvue\b", re.I): [TechTag.javascript, TechLibTag.vue],
    re.compile(r"\bangular\w*\b", re.I): [TechTag.javascript, TechLibTag.angular],
    re.compile(r"\bnext\.?js\b", re.I): [TechTag.javascript, TechLibTag.next],
    re.compile(r"\bAPI\b"): [TechTag.api],
    re.compile(r"\bruby\b", re.I): [TechTag.ruby],
    re.compile(r"\bRoR\b"): [TechTag.ruby],
    re.compile(r"\bruby\s*on\s*rails\b", re.I): [TechTag.ruby],
    re.compile(r"\bjazyk[au]\s+c\b", re.I): [TechTag.c],
    re.compile(r"\bc(/|\s+a\s+)c[\+p]{2}\b", re.I): [TechTag.c, TechTag.cpp],
    re.compile(r"\bhardwar\w+", re.I): [TechTag.hardware],
}
