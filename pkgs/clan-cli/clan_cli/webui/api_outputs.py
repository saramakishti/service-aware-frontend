from enum import Enum
from typing import Dict, List

from pydantic import BaseModel, Field

from ..async_cmd import CmdOut
from ..task_manager import TaskStatus
from ..vms.inspect import VmConfig


class Status(Enum):
    ONLINE = "online"
    OFFLINE = "offline"
    UNKNOWN = "unknown"


class Machine(BaseModel):
    name: str
    status: Status


class MachineCreate(BaseModel):
    name: str


class MachinesResponse(BaseModel):
    machines: list[Machine]


class MachineResponse(BaseModel):
    machine: Machine


class ConfigResponse(BaseModel):
    config: dict


class SchemaResponse(BaseModel):
    schema_: dict = Field(alias="schema")


class VmStatusResponse(BaseModel):
    error: str | None
    status: TaskStatus


class VmCreateResponse(BaseModel):
    uuid: str


class FlakeAttrResponse(BaseModel):
    flake_attrs: list[str]


class VmInspectResponse(BaseModel):
    config: VmConfig


class FlakeAction(BaseModel):
    id: str
    uri: str


class FlakeCreateResponse(BaseModel):
    cmd_out: Dict[str, CmdOut]


class FlakeResponse(BaseModel):
    content: str
    actions: List[FlakeAction]
