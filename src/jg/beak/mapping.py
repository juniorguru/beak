import re
import tomllib
from importlib.resources import files

from pydantic import BaseModel, TypeAdapter, field_validator

from jg.beak.tags import AITag, Tag, TechLibTag, TechTag


_TAGS_BY_VALUE: dict[str, Tag] = {
    str(tag): tag for enum in (TechTag, TechLibTag, AITag) for tag in enum
}


class Rule(BaseModel):
    pattern: str
    tags: list[str]
    case_sensitive: bool = False
    treat_as_word: bool = True

    @field_validator("tags")
    @classmethod
    def _validate_tags(cls, tags: list[str]) -> list[str]:
        if not tags:
            raise ValueError("rule has no tags")
        if unknown := [tag for tag in tags if tag not in _TAGS_BY_VALUE]:
            raise ValueError(f"unknown tags: {unknown}")
        return tags

    def compile(self) -> tuple[re.Pattern[str], list[Tag]]:
        # Plain spaces are a convenience for the common "two words" case and
        # expand to \s+ so patterns survive newlines/multiple spaces in the
        # scraped input. Use explicit \s*, \s? or \x20 when that is not wanted.
        pattern = re.sub(r" +", lambda _: r"\s+", self.pattern)
        # Rules match whole words by default; opt out with treat_as_word = false.
        if self.treat_as_word:
            pattern = rf"\b{pattern}\b"
        flags = re.NOFLAG if self.case_sensitive else re.IGNORECASE
        return re.compile(pattern, flags), [_TAGS_BY_VALUE[tag] for tag in self.tags]


def _load_mapping() -> dict[re.Pattern[str], list[Tag]]:
    toml = files("jg.beak").joinpath("mapping.toml").read_text("utf-8")
    rules = TypeAdapter(list[Rule]).validate_python(tomllib.loads(toml)["rule"])
    return dict(rule.compile() for rule in rules)


MAPPING = _load_mapping()
