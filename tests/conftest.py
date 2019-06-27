from functools import partial

from click.testing import CliRunner
import pytest
import ujson as json

from tabbyj.__main__ import tabbyj


@pytest.fixture()
def runner():
    runner = CliRunner()
    with runner.isolated_filesystem():
        yield runner


@pytest.fixture()
def command_runner(runner):
    return partial(runner.invoke, tabbyj)


@pytest.fixture()
def valid_json():
    return {
        "array": [1, 2, 3],
        "boolean": True,
        "null": None,
        "number": 123,
        "object": {"a": 1, "b": 2, "c": 3},
        "string": "String",
    }


@pytest.fixture()
def valid_json_file(runner, valid_json):
    with open("valid.json", "w", encoding="utf-8") as f:
        json.dump(valid_json, f)
    return "valid.json"


@pytest.fixture()
def valid_json_string(valid_json):
    return json.dumps(valid_json)


@pytest.fixture()
def malformed_json():
    return "There is no world in which this would be valid json."


@pytest.fixture()
def malformed_json_file(malformed_json):
    with open("malformed.json", "w", encoding="utf-8") as f:
        f.write(malformed_json)
    return "malformed.json"


@pytest.fixture()
def empty_json_file():
    with open("empty.json", "w", encoding="utf-8") as f:
        f.write("")
    return "empty.json"
