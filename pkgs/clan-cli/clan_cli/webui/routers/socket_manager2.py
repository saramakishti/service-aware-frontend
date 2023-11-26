# Requires: `starlette`, `uvicorn`, `jinja2`
# Run with `uvicorn example:app`
import logging
import os

import anyio
from broadcaster import Broadcast
from fastapi import APIRouter, WebSocket
from fastapi.responses import HTMLResponse

log = logging.getLogger(__name__)
router = APIRouter()


brd = Broadcast("memory://")


@router.get("/ws2_example")
async def get() -> HTMLResponse:
    html = open(f"{os.getcwd()}/webui/routers/messenger.html").read()
    return HTMLResponse(html)


@router.websocket("/ws2")
async def chatroom_ws(websocket: WebSocket) -> None:
    await websocket.accept()

    async with anyio.create_task_group() as task_group:
        # run until first is complete
        async def run_chatroom_ws_receiver() -> None:
            await chatroom_ws_receiver(websocket=websocket)
            task_group.cancel_scope.cancel()

        task_group.start_soon(run_chatroom_ws_receiver)
        log.warning("Started chatroom_ws_sender")

        await chatroom_ws_sender(websocket)


async def chatroom_ws_receiver(websocket: WebSocket) -> None:
    async for message in websocket.iter_text():
        log.warning(f"Received message: {message}")
        await brd.publish(channel="chatroom", message=message)


async def chatroom_ws_sender(websocket: WebSocket) -> None:
    async with brd.subscribe(channel="chatroom") as subscriber:
        if subscriber is None:
            log.error("Subscriber is None")
            return
        async for event in subscriber:  # type: ignore
            await websocket.send_text(event.message)
