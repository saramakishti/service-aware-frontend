from enum import Enum
from typing import Dict, List

from pydantic import BaseModel, Field

from ..async_cmd import CmdOut
from ..task_manager import TaskStatus


class Status(Enum):
    ONLINE = "online"
    OFFLINE = "offline"
    UNKNOWN = "unknown"


class Machine(BaseModel):
    name: str
    status: Status



