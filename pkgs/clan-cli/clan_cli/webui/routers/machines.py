# Logging setup
import logging
from typing import Annotated

from fastapi import APIRouter, Body

from ...config.machine import (
    config_for_machine,
    schema_for_machine,
    set_config_for_machine,
)
from ...flakes.types import FlakeName
from ...machines.create import create_machine as _create_machine
from ...machines.list import list_machines as _list_machines
from ..api_outputs import (
    ConfigResponse,
    Machine,
    MachineCreate,
    MachineResponse,
    MachinesResponse,
    SchemaResponse,
    Status,
)

log = logging.getLogger(__name__)
router = APIRouter()


@router.get("/api/{flake_name}/machines")
async def list_machines(flake_name: FlakeName) -> MachinesResponse:
    machines = []
    for m in _list_machines(flake_name):
        machines.append(Machine(name=m, status=Status.UNKNOWN))
    return MachinesResponse(machines=machines)


@router.post("/api/{flake_name}/machines", status_code=201)
async def create_machine(
    flake_name: FlakeName, machine: Annotated[MachineCreate, Body()]
) -> MachineResponse:
    out = await _create_machine(flake_name, machine.name)
    log.debug(out)
    return MachineResponse(machine=Machine(name=machine.name, status=Status.UNKNOWN))


@router.get("/api/machines/{name}")
async def get_machine(name: str) -> MachineResponse:
    log.error("TODO")
    return MachineResponse(machine=Machine(name=name, status=Status.UNKNOWN))


@router.get("/api/{flake_name}/machines/{name}/config")
async def get_machine_config(flake_name: FlakeName, name: str) -> ConfigResponse:
    config = config_for_machine(flake_name, name)
    return ConfigResponse(config=config)


@router.put("/api/{flake_name}/machines/{name}/config")
async def set_machine_config(
    flake_name: FlakeName, name: str, config: Annotated[dict, Body()]
) -> ConfigResponse:
    set_config_for_machine(flake_name, name, config)
    return ConfigResponse(config=config)


@router.get("/api/{flake_name}/machines/{name}/schema")
async def get_machine_schema(flake_name: FlakeName, name: str) -> SchemaResponse:
    schema = schema_for_machine(flake_name, name)
    return SchemaResponse(schema=schema)
