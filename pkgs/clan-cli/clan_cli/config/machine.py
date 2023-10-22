import json
import subprocess
import sys
from pathlib import Path

from fastapi import HTTPException

from clan_cli.dirs import (
    machine_settings_file,
    nixpkgs_source,
    specific_flake_dir,
    specific_machine_dir,
)
from clan_cli.git import commit_file, find_git_repo_root
from clan_cli.nix import nix_eval

from ..types import FlakeName


def config_for_machine(flake_name: FlakeName, machine_name: str) -> dict:
    # read the config from a json file located at {flake}/machines/{machine_name}/settings.json
    if not specific_machine_dir(flake_name, machine_name).exists():
        raise HTTPException(
            status_code=404,
            detail=f"Machine {machine_name} not found. Create the machine first`",
        )
    settings_path = machine_settings_file(flake_name, machine_name)
    if not settings_path.exists():
        return {}
    with open(settings_path) as f:
        return json.load(f)


def set_config_for_machine(
    flake_name: FlakeName, machine_name: str, config: dict
) -> None:
    # write the config to a json file located at {flake}/machines/{machine_name}/settings.json
    if not specific_machine_dir(flake_name, machine_name).exists():
        raise HTTPException(
            status_code=404,
            detail=f"Machine {machine_name} not found. Create the machine first`",
        )
    settings_path = machine_settings_file(flake_name, machine_name)
    settings_path.parent.mkdir(parents=True, exist_ok=True)
    with open(settings_path, "w") as f:
        json.dump(config, f)
    repo_dir = find_git_repo_root()

    if repo_dir is not None:
        commit_file(settings_path, repo_dir)


def schema_for_machine(flake_name: FlakeName, machine_name: str) -> dict:
    flake = specific_flake_dir(flake_name)

    # use nix eval to lib.evalModules .#nixosModules.machine-{machine_name}
    proc = subprocess.run(
        nix_eval(
            flags=[
                "--impure",
                "--show-trace",
                "--expr",
                f"""
                let
                    flake = builtins.getFlake (toString {flake});
                    lib = import {nixpkgs_source()}/lib;
                    options = flake.nixosConfigurations.{machine_name}.options;
                    clanOptions = options.clan;
                    jsonschemaLib = import {Path(__file__).parent / "jsonschema"} {{ inherit lib; }};
                    jsonschema = jsonschemaLib.parseOptions clanOptions;
                in
                    jsonschema
                """,
            ],
        ),
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        print(proc.stderr, file=sys.stderr)
        raise Exception(
            f"Failed to read schema for machine {machine_name}:\n{proc.stderr}"
        )
    return json.loads(proc.stdout)
