import sys

import click
import ujson as json


@click.command()
def tabbyj():
    """Flatten JSON passed in through stdin."""
    data = json.load(sys.stdin)
    print(data)