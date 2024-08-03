import sys
from typing import Pattern, TextIO

import click

from jg.beak.mapping import MAPPING
from jg.beak.tags import Tag


@click.command()
@click.argument("text_file", type=click.File("r"), default=sys.stdin)
def main(text_file: TextIO) -> None:
    for tag in beak(text_file.read()):
        click.echo(tag.value)


def beak(text: str, mapping: dict[Pattern, list[Tag]] | None = None) -> set[Tag]:
    mapping = mapping or MAPPING
    tags = set()
    for pattern_re, pattern_tags in MAPPING.items():
        if pattern_re.search(text):
            tags.update(pattern_tags)
    return tags
