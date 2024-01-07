import logging
from contextlib import asynccontextmanager
from typing import Any

# import for sql
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRoute
from fastapi.staticfiles import StaticFiles
from sqlalchemy.exc import SQLAlchemyError

from ..errors import ClanError
from . import sql_models
from .assets import asset_path
from .error_handlers import clan_error_handler, sql_error_handler
from .routers import endpoints, health, root, socket_manager2  # sql router hinzufügen
from .sql_db import engine
from .tags import tags_metadata

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://0.0.0.0:3000",
]
# Logging setup
log = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> Any:
    await socket_manager2.brd.connect()
    yield
    await socket_manager2.brd.disconnect()


def setup_app() -> FastAPI:
    # bind sql engine
    # TODO comment aut and add flag to run with pupulated data rm *.sql run pytest with marked then start clan webui
    # https://docs.pytest.org/en/7.1.x/example/markers.html
    # sql_models.Base.metadata.drop_all(engine)

    sql_models.Base.metadata.create_all(bind=engine)

    app = FastAPI(lifespan=lifespan, swagger_ui_parameters={"tryItOutEnabled": True})
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(health.router)
    # sql methodes
    app.include_router(endpoints.router)

    app.include_router(socket_manager2.router)

    # Needs to be last in register. Because of wildcard route
    app.include_router(root.router)
    app.add_exception_handler(ClanError, clan_error_handler)  # type: ignore
    app.add_exception_handler(SQLAlchemyError, sql_error_handler)  # type: ignore

    app.mount("/static", StaticFiles(directory=asset_path()), name="static")

    # Add tag descriptions to the OpenAPI schema
    app.openapi_tags = tags_metadata

    for route in app.routes:
        if isinstance(route, APIRoute):
            route.operation_id = route.name  # in this case, 'read_items'
        log.debug(f"Registered route: {route}")

    for i in app.exception_handlers.items():
        log.debug(f"Registered exception handler: {i}")

    return app


app = setup_app()
