def test_tabbyj_help(command_runner):
    result = command_runner(["--help"])
    assert result.exit_code == 0
    assert (
        result.output
        == """\
Usage: tabbyj [OPTIONS]

  Flattens a user-provided JSON object.

Options:
  --file TEXT      File to read from.
  --encoding TEXT  Encoding to use to read the provided file.
  --help           Show this message and exit.
"""
    )


def test_tabbyj_no_input(command_runner):
    result = command_runner()
    assert result.exit_code == 1
    assert (
        result.output
        == "Either no JSON was provided, or the JSON provided was malformed.\n"
    )


def test_tabbyj_malformed_input(command_runner, malformed_json):
    result = command_runner(input=malformed_json)
    assert result.exit_code == 1
    assert (
        result.output
        == "Either no JSON was provided, or the JSON provided was malformed.\n"
    )


def test_tabbyj_no_file_input(command_runner, empty_json_file):
    result = command_runner(["--file", empty_json_file])
    assert result.exit_code == 1
    assert (
        result.output
        == "Either no JSON was provided, or the JSON provided was malformed.\n"
    )


def test_tabbyj_malformed_file_input(command_runner, malformed_json_file):
    result = command_runner(["--file", malformed_json_file])
    assert result.exit_code == 1
    assert (
        result.output
        == "Either no JSON was provided, or the JSON provided was malformed.\n"
    )


def test_tabbyj_valid_input(command_runner, valid_json_string):
    result = command_runner(input=valid_json_string)
    assert result.exit_code == 0
    assert (
        result.output
        == """\
.array[0] = 1
.array[1] = 2
.array[2] = 3
.boolean = true
.null = null
.number = 123
.object.a = 1
.object.b = 2
.object.c = 3
.string = 'String'
"""
    )


def test_tabbyj_valid_file_input(command_runner, valid_json_file):
    result = command_runner(["--file", valid_json_file])
    assert result.exit_code == 0
    assert (
        result.output
        == """\
.array[0] = 1
.array[1] = 2
.array[2] = 3
.boolean = true
.null = null
.number = 123
.object.a = 1
.object.b = 2
.object.c = 3
.string = 'String'
"""
    )


def test_tabbyj_nonexistent_file(command_runner):
    result = command_runner(["--file", "nonexistent.json"])
    assert result.exit_code == 1
    assert result.output == "The specified file could not be found.\n"


def test_tabbyj_invalid_encoding(command_runner, valid_json_file):
    result = command_runner(["--file", valid_json_file, "--encoding", "fakeencoding"])
    assert result.exit_code == 1
    assert result.output == "The specified encoding is invalid.\n"
