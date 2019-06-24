import sys
from typing import Dict, Any, List

import click
import ujson as json

def process_value(data: Any, *, location: str=".") -> None:
    if isinstance(data, dict):
        process_dict(data, location)
    elif isinstance(data, list):
        process_list(data, location)
    else:
        print(f"{location} = {data}")

def process_dict(data: Dict[str, Any], location: str) -> None:
    for key, value in data.items():
        process_value(value, location=f"{location}.{key}")

def process_list(data: List[Any], location: str) -> None:
    for index, value in enumerate(data):
        process_value(value, location=f"{location}[{index}]")

@click.command()
def tabbyj():
    """Flatten JSON passed in through stdin."""
    data = json.load(sys.stdin)
    process_value(data)
