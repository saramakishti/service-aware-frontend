import logging
from pathlib import Path
from typing import Annotated, Iterator
from uuid import UUID

from fastapi import APIRouter, Body, status
from fastapi.exceptions import HTTPException
from fastapi.responses import StreamingResponse
from pydantic import AnyUrl

from clan_cli.webui.routers.flake import get_attrs

from ...task_manager import get_task
from ...vms import create, inspect
from ..api_outputs import (
    VmConfig,
    VmCreateResponse,
    VmInspectResponse,
    VmStatusResponse,
)

log = logging.getLogger(__name__)
router = APIRouter()


# TODO: Check for directory traversal
@router.post("/api/vms/inspect")
async def inspect_vm(
    flake_url: Annotated[AnyUrl | Path, Body()], flake_attr: Annotated[str, Body()]
) -> VmInspectResponse:
    config = await inspect.inspect_vm(flake_url, flake_attr)
    return VmInspectResponse(config=config)


@router.get("/api/vms/{uuid}/status")
async def get_vm_status(uuid: UUID) -> VmStatusResponse:
    task = get_task(uuid)
    log.debug(msg=f"error: {task.error}, task.status: {task.status}")
    error = str(task.error) if task.error is not None else None
    return VmStatusResponse(status=task.status, error=error)


@router.get("/api/vms/{uuid}/logs")
async def get_vm_logs(uuid: UUID) -> StreamingResponse:
    # Generator function that yields log lines as they are available
    def stream_logs() -> Iterator[str]:
        task = get_task(uuid)

        yield from task.log_lines()

    return StreamingResponse(
        content=stream_logs(),
        media_type="text/plain",
    )


# TODO: Check for directory traversal
@router.post("/api/vms/create")
async def create_vm(vm: Annotated[VmConfig, Body()]) -> VmCreateResponse:
    flake_attrs = await get_attrs(vm.flake_url)
    if vm.flake_attr not in flake_attrs:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Provided attribute '{vm.flake_attr}' does not exist.",
        )
    task = create.create_vm(vm)
    return VmCreateResponse(uuid=str(task.uuid))
