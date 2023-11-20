import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRoute
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
from typing import Any

from ..errors import ClanError
from .assets import asset_path
from .error_handlers import clan_error_handler
from .routers import health, root, socket_manager, socket_manager2

origins = [
    "http://localhost:3000",
]
# Logging setup
log = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> Any:
    await socket_manager2.brd.connect()
    yield
    await socket_manager2.brd.disconnect()


def setup_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(health.router)

    app.include_router(socket_manager.router)
    app.include_router(socket_manager2.router)

    # Needs to be last in register. Because of wildcard route
    app.include_router(root.router)
    app.add_exception_handler(ClanError, clan_error_handler) # type: ignore

    app.mount("/static", StaticFiles(directory=asset_path()), name="static")

    for route in app.routes:
        if isinstance(route, APIRoute):
            route.operation_id = route.name  # in this case, 'read_items'
        log.debug(f"Registered route: {route}")

    for i in app.exception_handlers.items():
        log.debug(f"Registered exception handler: {i}")

    return app


app = setup_app()
