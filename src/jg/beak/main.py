import re
import sys
import tomllib
from functools import cache
from importlib.resources import files
from typing import TextIO

import click
from pydantic import BaseModel, TypeAdapter, field_validator

from jg.beak.tags import Tag, TechLibTag, TechTag


_TAGS_BY_VALUE: dict[str, Tag] = {
    str(tag): tag for enum in (TechTag, TechLibTag) for tag in enum
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


def _toml_rules() -> list[Rule]:
    toml = files("jg.beak").joinpath("mapping.toml").read_text("utf-8")
    return TypeAdapter(list[Rule]).validate_python(tomllib.loads(toml)["rule"])


@cache
def _load_mapping() -> dict[re.Pattern[str], list[Tag]]:
    return dict(rule.compile() for rule in _toml_rules())


@click.command()
@click.argument("text_file", type=click.File("r"), default=sys.stdin)
def main(text_file: TextIO) -> None:
    for tag in sorted(beak(text_file.read())):
        click.echo(tag.value)


def beak(
    text: str, mapping: dict[re.Pattern[str], list[Tag]] | None = None
) -> set[Tag]:
    if mapping is None:
        mapping = _load_mapping()
    tags = set()
    for pattern_re, pattern_tags in mapping.items():
        if pattern_re.search(text):
            tags.update(pattern_tags)
    return tags
