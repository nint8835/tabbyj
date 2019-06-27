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
            value, location=f"{location}[{click.style(str(index), fg='yellow')}]"
        )


@click.command()
@click.option("--file", default=None, help="File to read from.")
@click.option(
    "--encoding", default="utf-8", help="Encoding to use to read the provided file."
)
def tabbyj(file, encoding):
    """Flattens a user-provided JSON object."""
    if file is not None:
        with open(file, encoding=encoding) as f:
            data = json.load(f)
    else:
        data = json.load(sys.stdin)
    process_value(data)
