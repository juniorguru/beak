import itertools
from pathlib import Path
from typing import cast

import pytest

from jg.beak.core import beak
from jg.beak.tags import TechLibTag, TechTag


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
    all_tags = set(map(str, list(TechTag) + list(TechLibTag)))
    tested_tags = set(
        itertools.chain.from_iterable(cast(set, param.values[1]) for param in fixtures)
    )
    assert tested_tags == all_tags
