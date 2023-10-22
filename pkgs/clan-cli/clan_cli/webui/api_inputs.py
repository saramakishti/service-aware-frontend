import logging
from pathlib import Path
from typing import Any

from pydantic import AnyUrl, BaseModel, validator
from pydantic.tools import parse_obj_as

from ..dirs import clan_data_dir, clan_flakes_dir
from ..types import validate_path

DEFAULT_URL = parse_obj_as(AnyUrl, "http://localhost:8000")

log = logging.getLogger(__name__)


class ClanDataPath(BaseModel):
    dest: Path

    @validator("dest")
    def check_data_path(cls: Any, v: Path) -> Path:  # noqa
        return validate_path(clan_data_dir(), v)


class ClanFlakePath(BaseModel):
    dest: Path

    @validator("dest")
    def check_dest(cls: Any, v: Path) -> Path:  # noqa
        return validate_path(clan_flakes_dir(), v)


class FlakeCreateInput(ClanFlakePath):
    url: AnyUrl = DEFAULT_URL
