from pathlib import Path

import pytest

from clan_cli.dirs import _get_clan_flake_toplevel
from clan_cli.errors import ClanError


def test_get_clan_flake_toplevel(
    monkeypatch: pytest.MonkeyPatch, temporary_dir: Path
) -> None:
    monkeypatch.chdir(temporary_dir)
    with pytest.raises(ClanError):
        print(_get_clan_flake_toplevel())
    (temporary_dir / ".git").touch()
    assert _get_clan_flake_toplevel() == temporary_dir

    subdir = temporary_dir / "subdir"
    subdir.mkdir()
    monkeypatch.chdir(subdir)
    (subdir / ".clan-flake").touch()
    assert _get_clan_flake_toplevel() == subdir
