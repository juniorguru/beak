import itertools
import re
from pathlib import Path
from typing import cast
from unittest.mock import Mock

import pytest

from jg.beak import main, tags as tags_module
from jg.beak.main import _load_mapping, _toml_rules, beak
from jg.beak.tags import AITag, Tag, TechLibTag, TechTag


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
    mapping = _load_mapping()

    assert mapping, "Mapping is empty"
    assert all(isinstance(pattern, re.Pattern) for pattern in mapping)
    assert all(mapping.values()), "A rule has no tags"
    assert all(isinstance(tag, Tag) for tags in mapping.values() for tag in tags)


@pytest.mark.parametrize("pattern, mapped_tags", _load_mapping().items())
def test_rule_tags_are_unique(pattern: re.Pattern[str], mapped_tags: list[Tag]) -> None:
    values = [str(tag) for tag in mapped_tags]

    assert len(values) == len(set(values)), f"{pattern.pattern!r} has duplicate tags"


def test_mapping_toml_is_sorted_by_pattern() -> None:
    patterns = [rule.pattern for rule in _toml_rules()]

    assert patterns == sorted(patterns, key=str.lower)


def test_tag_values_are_unambiguous() -> None:
    values = [str(tag) for enum in (TechTag, TechLibTag, AITag) for tag in enum]

    assert len(values) == len(set(values))


@pytest.mark.parametrize(
    "text, expected",
    [("some foobar text", {TechTag.python}), ("plain python text", set())],
)
def test_custom_mapping_is_used(text: str, expected: set[Tag]) -> None:
    mapping = {re.compile(r"\bfoobar\b"): [TechTag.python]}

    assert beak(text, mapping=mapping) == expected


@pytest.mark.parametrize("mapping", [{}, {re.compile("foobar"): [TechTag.python]}])
def test_custom_mapping_does_not_load_defaults(
    monkeypatch: pytest.MonkeyPatch, mapping: dict[re.Pattern[str], list[Tag]]
) -> None:
    loader = Mock(side_effect=AssertionError("Default mapping must not load"))
    monkeypatch.setattr(main, "_load_mapping", loader)
    result = beak("python", mapping=mapping)

    assert result == set()
    assert loader.call_count == 0


def test_default_mapping_is_cached(monkeypatch: pytest.MonkeyPatch) -> None:
    loader = Mock(wraps=_toml_rules)
    monkeypatch.setattr(main, "_toml_rules", loader)
    _load_mapping.cache_clear()
    try:
        first = beak("python")
        second = beak("python")
    finally:
        _load_mapping.cache_clear()

    assert first == second == {TechTag.python}
    assert loader.call_count == 1
