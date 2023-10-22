import json
import tempfile
from pathlib import Path
from typing import Any, Optional

import pytest
from cli import Cli

from clan_cli import config
from clan_cli.config import parsing
from clan_cli.errors import ClanError
from fixtures_flakes import FlakeForTest

example_options = f"{Path(config.__file__).parent}/jsonschema/options.json"


# use pytest.parametrize
@pytest.mark.parametrize(
    "args,expected",
    [
        (["name", "DavHau"], {"name": "DavHau"}),
        (
            ["kernelModules", "foo", "bar", "baz"],
            {"kernelModules": ["foo", "bar", "baz"]},
        ),
        (["services.opt", "test"], {"services": {"opt": "test"}}),
        (["userIds.DavHau", "42"], {"userIds": {"DavHau": 42}}),
    ],
)
def test_set_some_option(
    args: list[str],
    expected: dict[str, Any],
    test_flake: FlakeForTest,
) -> None:
    # create temporary file for out_file
    with tempfile.NamedTemporaryFile() as out_file:
        with open(out_file.name, "w") as f:
            json.dump({}, f)
        cli = Cli()
        cli.run(
            [
                "config",
                "--quiet",
                "--options-file",
                example_options,
                "--settings-file",
                out_file.name,
            ]
            + args
            + [test_flake.name]
        )
        json_out = json.loads(open(out_file.name).read())
        assert json_out == expected


def test_configure_machine(
    test_flake: FlakeForTest,
    temporary_home: Path,
    capsys: pytest.CaptureFixture,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    cli = Cli()
    cli.run(["config", "-m", "machine1", "clan.jitsi.enable", "true", test_flake.name])
    # clear the output buffer
    capsys.readouterr()
    # read a option value
    cli.run(["config", "-m", "machine1", "clan.jitsi.enable", test_flake.name])
    # read the output
    assert capsys.readouterr().out == "true\n"


def test_walk_jsonschema_all_types() -> None:
    schema = dict(
        type="object",
        properties=dict(
            array=dict(
                type="array",
                items=dict(
                    type="string",
                ),
            ),
            boolean=dict(type="boolean"),
            integer=dict(type="integer"),
            number=dict(type="number"),
            string=dict(type="string"),
        ),
    )
    expected = {
        "array": list[str],
        "boolean": bool,
        "integer": int,
        "number": float,
        "string": str,
    }
    assert config.parsing.options_types_from_schema(schema) == expected


def test_walk_jsonschema_nested() -> None:
    schema = dict(
        type="object",
        properties=dict(
            name=dict(
                type="object",
                properties=dict(
                    first=dict(type="string"),
                    last=dict(type="string"),
                ),
            ),
            age=dict(type="integer"),
        ),
    )
    expected = {
        "age": int,
        "name.first": str,
        "name.last": str,
    }
    assert config.parsing.options_types_from_schema(schema) == expected


# test walk_jsonschema with dynamic attributes (e.g. "additionalProperties")
def test_walk_jsonschema_dynamic_attrs() -> None:
    schema = dict(
        type="object",
        properties=dict(
            age=dict(type="integer"),
            users=dict(
                type="object",
                additionalProperties=dict(type="string"),
            ),
        ),
    )
    expected = {
        "age": int,
        "users.<name>": str,  # <name> is a placeholder for any string
    }
    assert config.parsing.options_types_from_schema(schema) == expected


def test_type_from_schema_path_simple() -> None:
    schema = dict(
        type="boolean",
    )
    assert parsing.type_from_schema_path(schema, []) == bool


def test_type_from_schema_path_nested() -> None:
    schema = dict(
        type="object",
        properties=dict(
            name=dict(
                type="object",
                properties=dict(
                    first=dict(type="string"),
                    last=dict(type="string"),
                ),
            ),
            age=dict(type="integer"),
        ),
    )
    assert parsing.type_from_schema_path(schema, ["age"]) == int
    assert parsing.type_from_schema_path(schema, ["name", "first"]) == str


def test_type_from_schema_path_dynamic_attrs() -> None:
    schema = dict(
        type="object",
        properties=dict(
            age=dict(type="integer"),
            users=dict(
                type="object",
                additionalProperties=dict(type="string"),
            ),
        ),
    )
    assert parsing.type_from_schema_path(schema, ["age"]) == int
    assert parsing.type_from_schema_path(schema, ["users", "foo"]) == str


def test_map_type() -> None:
    with pytest.raises(ClanError):
        config.map_type("foo")
    assert config.map_type("string") == str
    assert config.map_type("integer") == int
    assert config.map_type("boolean") == bool
    assert config.map_type("attribute set of string") == dict[str, str]
    assert config.map_type("attribute set of integer") == dict[str, int]
    assert config.map_type("null or string") == Optional[str]


# test the cast function with simple types
def test_cast() -> None:
    assert config.cast(value=["true"], type=bool, opt_description="foo-option") is True
    assert (
        config.cast(value=["null"], type=Optional[str], opt_description="foo-option")
        is None
    )
    assert (
        config.cast(value=["bar"], type=Optional[str], opt_description="foo-option")
        == "bar"
    )


@pytest.mark.parametrize(
    "option,value,options,expected",
    [
        ("foo.bar", ["baz"], {"foo.bar": {"type": "str"}}, ("foo.bar", ["baz"])),
        ("foo.bar", ["baz"], {"foo": {"type": "attrs"}}, ("foo", {"bar": ["baz"]})),
        (
            "users.users.my-user.name",
            ["my-name"],
            {"users.users.<name>.name": {"type": "str"}},
            ("users.users.<name>.name", ["my-name"]),
        ),
        (
            "foo.bar.baz.bum",
            ["val"],
            {"foo.<name>.baz": {"type": "attrs"}},
            ("foo.<name>.baz", {"bum": ["val"]}),
        ),
        (
            "userIds.DavHau",
            ["42"],
            {"userIds": {"type": "attrs"}},
            ("userIds", {"DavHau": ["42"]}),
        ),
    ],
)
def test_find_option(option: str, value: list, options: dict, expected: tuple) -> None:
    assert config.find_option(option, value, options) == expected
