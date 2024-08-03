from enum import Enum, StrEnum
from importlib import import_module
import itertools
from pathlib import Path
from typing import cast

import pytest

from jg.beak.core import beak
from jg.beak import tags as tags_module


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
    assert beak(text) == expected


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
