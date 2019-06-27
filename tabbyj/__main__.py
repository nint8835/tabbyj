import sys
from typing import Dict, Any, List

import click
import ujson as json


def get_json_repr(obj: Any) -> str:
    if obj is None:
        return click.style("null", fg="red")
    elif isinstance(obj, bool):
        return click.style(repr(obj).lower(), fg="red")
    elif isinstance(obj, str):
        return click.style(repr(obj), fg="cyan")
    else:
        return click.style(repr(obj), fg="yellow")


def process_value(data: Any, *, location: str = "") -> None:
    if isinstance(data, dict):
        process_dict(data, location)
    elif isinstance(data, list):
        process_list(data, location)
    else:
        click.echo(f"{location} = {get_json_repr(data)}")


def process_dict(data: Dict[str, Any], location: str) -> None:
    for key, value in data.items():
        process_value(value, location=f"{location}.{key}")


def process_list(data: List[Any], location: str) -> None:
    for index, value in enumerate(data):
        process_value(
            value,
            location=f"{location}[{click.style(str(index), fg='yellow')}]"
        )


@click.command()
def tabbyj():
    """Flatten JSON passed in through stdin."""
    data = json.load(sys.stdin)
    process_value(data)
