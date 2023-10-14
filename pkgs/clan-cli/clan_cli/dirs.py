import os
import sys
from pathlib import Path
from typing import Optional

from .errors import ClanError


def _get_clan_flake_toplevel() -> Path:
    return find_toplevel([".clan-flake", ".git", ".hg", ".svn", "flake.nix"])


def find_git_repo_root() -> Optional[Path]:
    try:
        return find_toplevel([".git"])
    except ClanError:
        return None


def find_toplevel(top_level_files: list[str]) -> Path:
    """Returns the path to the toplevel of the clan flake"""
    for project_file in top_level_files:
        initial_path = Path(os.getcwd())
        path = Path(initial_path)
        while path.parent != path:
            if (path / project_file).exists():
                return path
            path = path.parent
    raise ClanError("Could not find clan flake toplevel directory")


def user_config_dir() -> Path:
    if sys.platform == "win32":
        return Path(os.getenv("APPDATA", os.path.expanduser("~\\AppData\\Roaming\\")))
    elif sys.platform == "darwin":
        return Path(os.path.expanduser("~/Library/Application Support/"))
    else:
        return Path(os.getenv("XDG_CONFIG_HOME", os.path.expanduser("~/.config")))


def user_data_dir() -> Path:
    if sys.platform == "win32":
        return Path(os.getenv("APPDATA", os.path.expanduser("~\\AppData\\Roaming\\")))
    elif sys.platform == "darwin":
        return Path(os.path.expanduser("~/Library/Application Support/"))
    else:
        return Path(os.getenv("XDG_DATA_HOME", os.path.expanduser("~/.local/state")))


def clan_data_dir() -> Path:
    path = user_data_dir() / "clan"
    if not path.exists():
        path.mkdir()
    return path.resolve()


def clan_config_dir() -> Path:
    path = user_config_dir() / "clan"
    if not path.exists():
        path.mkdir()
    return path.resolve()


def clan_flakes_dir() -> Path:
    path = clan_data_dir() / "flake"
    if not path.exists():
        path.mkdir()
    return path.resolve()


def specific_flake_dir(name: str) -> Path:
    flake_dir = clan_flakes_dir() / name
    if not flake_dir.exists():
        raise ClanError(f"Flake {name} does not exist")
    return flake_dir


def machines_dir(flake_name: str) -> Path:
    return specific_flake_dir(flake_name) / "machines"


def specific_machine_dir(flake_name: str, machine: str) -> Path:
    return machines_dir(flake_name) / machine


def machine_settings_file(flake_name: str, machine: str) -> Path:
    return specific_machine_dir(flake_name, machine) / "settings.json"


def module_root() -> Path:
    return Path(__file__).parent


def nixpkgs_flake() -> Path:
    return (module_root() / "nixpkgs").resolve()


def nixpkgs_source() -> Path:
    return (module_root() / "nixpkgs" / "path").resolve()


def unfree_nixpkgs() -> Path:
    return module_root() / "nixpkgs" / "unfree"
