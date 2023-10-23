from enum import Enum

from pydantic import BaseModel


class Status(Enum):
    ONLINE = "online"
    OFFLINE = "offline"
    UNKNOWN = "unknown"


class Machine(BaseModel):
    name: str
    status: Status
