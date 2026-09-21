import itertools
import re
import tomllib
from importlib.resources import files
from pathlib import Path
from typing import cast

import pytest

from jg.beak import tags as tags_module
from jg.beak.core import beak
from jg.beak.mapping import MAPPING
from jg.beak.tags import AITag, Tag, TechLibTag, TechTag


def _toml_rules() -> list[dict]:
    toml = files("jg.beak").joinpath("mapping.toml").read_text("utf-8")
    return tomllib.loads(toml)["rule"]


fixtures = [
    pytest.param(
        path.read_text(),
        set(path.stem.removeprefix("tag_").split("_")),
        id=path.name,
    )
    for path in Path(__file__).parent.glob("tag_*.txt")
]


assert len(fixtures), "No fixtures found"


@pytest.mark.parametrize("text, expected", fixtures)
def test_beak(text: str, expected: set[str]) -> None:
    tags = beak(text)

    assert set(map(str, tags)) == expected


def test_all_tags_are_tested() -> None:
    tag_classes = [
        getattr(tags_module, member_name)
        for member_name in dir(tags_module)
        if member_name != "Tag" and member_name.endswith("Tag")
    ]
    all_tags = set(map(str, itertools.chain(*map(list, tag_classes))))
    tested_tags = set(
        itertools.chain.from_iterable(cast(set, param.values[1]) for param in fixtures)
    )
    assert tested_tags == all_tags


def test_mapping_loads_from_toml() -> None:
    assert MAPPING, "MAPPING is empty"
    for pattern, mapped_tags in MAPPING.items():
        assert isinstance(pattern, re.Pattern)
        assert mapped_tags, f"{pattern.pattern!r} has no tags"
        assert all(isinstance(tag, Tag) for tag in mapped_tags)


def test_rule_tags_are_unique() -> None:
    for pattern, mapped_tags in MAPPING.items():
        values = [str(tag) for tag in mapped_tags]
        assert len(values) == len(set(values)), (
            f"{pattern.pattern!r} has duplicate tags"
        )


def test_mapping_toml_is_sorted_by_pattern() -> None:
    patterns = [rule["pattern"] for rule in _toml_rules()]
    assert patterns == sorted(patterns, key=str.lower)


def test_tag_values_are_unambiguous() -> None:
    seen: dict[str, str] = {}
    for enum in (TechTag, TechLibTag, AITag):
        for tag in enum:
            value = str(tag)
            assert value not in seen, (
                f"{value!r} is in both {seen.get(value)} and {enum.__name__}"
            )
            seen[value] = enum.__name__


def test_custom_mapping_is_used() -> None:
    mapping = {re.compile(r"\bfoobar\b"): [TechTag.python]}

    assert beak("some foobar text", mapping=mapping) == {TechTag.python}
    assert beak("plain python text", mapping=mapping) == set()
