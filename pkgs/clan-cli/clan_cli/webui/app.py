# Imports
import logging

# Import FastAPI components and SQLAlchemy related modules
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRoute
from fastapi.staticfiles import StaticFiles
from sqlalchemy.exc import SQLAlchemyError

# Import configs
from ..config import cors_ports, cors_url

# Import custom modules and classes
from ..errors import ClanError
from . import sql_models
from .assets import asset_path
from .error_handlers import clan_error_handler, sql_error_handler
from .routers import endpoints, health, root
from .sql_db import engine
from .tags import tags_metadata

cors_whitelist = []
for u in cors_url:
    for p in cors_ports:
        cors_whitelist.append(f"{u}:{p}")

# Logging setup
log = logging.getLogger(__name__)


# Function to set up and configure the FastAPI application
def setup_app() -> FastAPI:
    # Uncomment the following line to drop existing tables during startup (if needed)
    # sql_models.Base.metadata.drop_all(engine)

    # Create tables in the database using SQLAlchemy
    sql_models.Base.metadata.create_all(bind=engine)

    # Initialize FastAPI application with lifespan management
    app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True})

    # Configure CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=cors_whitelist,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include routers for various endpoints and components
    app.include_router(health.router)
    app.include_router(endpoints.router)

    # Needs to be last in registration due to wildcard route
    app.include_router(root.router)

    # Add custom exception handlers
    app.add_exception_handler(ClanError, clan_error_handler)  # type: ignore
    app.add_exception_handler(SQLAlchemyError, sql_error_handler)  # type: ignore

    # Mount the "static" route for serving static files
    app.mount("/static", StaticFiles(directory=asset_path()), name="static")

    # Add tag descriptions to the OpenAPI schema
    app.openapi_tags = tags_metadata

    # Assign operation IDs to API routes
    for route in app.routes:
        if isinstance(route, APIRoute):
            route.operation_id = route.name  # in this case, 'read_items'
        log.debug(f"Registered route: {route}")

    # Log registered exception handlers
    for i in app.exception_handlers.items():
        log.debug(f"Registered exception handler: {i}")

    return app


# Create an instance of the FastAPI application
app = setup_app()
