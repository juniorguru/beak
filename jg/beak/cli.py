import logging

import click


@click.command()
@click.option("-d", "--debug", default=False, is_flag=True, help="Show debug logs.")
def main(debug: bool):
    logging.basicConfig(level=logging.DEBUG if debug else logging.INFO)
    print("Hello, world!")
