import logging

from fastapi import Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError

from ..errors import ClanError

log = logging.getLogger(__name__)


def sql_error_handler(request: Request, exc: SQLAlchemyError) -> JSONResponse:
    log.exception(exc)
    detail = [
        {
            "loc": [],
            "msg": exc._message(),
        }
    ]
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder(dict(detail=detail)),
    )


def clan_error_handler(request: Request, exc: ClanError) -> JSONResponse:
    log.exception(exc)
    detail = [
        {
            "loc": [],
            "msg": str(exc),
        }
    ]
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder(dict(detail=detail)),
    )
