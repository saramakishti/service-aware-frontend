import logging
import time
from datetime import datetime
from typing import List, Optional

import httpx
from fastapi import APIRouter, BackgroundTasks, Depends
from sqlalchemy.orm import Session

from ...errors import ClanError
from .. import sql_crud, sql_db, sql_models
from ..schemas import (
    Entity,
    EntityCreate,
    Resolution,
    Service,
    ServiceCreate,
)
from ..tags import Tags

router = APIRouter()

log = logging.getLogger(__name__)


#########################
#                       #
#        Service        #
#                       #
#########################
@router.post("/api/v1/service", response_model=Service, tags=[Tags.services])
def create_service(
    service: ServiceCreate, db: Session = Depends(sql_db.get_db)
) -> Service:
    # todo checken ob schon da ...
    return sql_crud.create_service(db=db, service=service)


@router.get("/api/v1/services", response_model=List[Service], tags=[Tags.services])
def get_all_services(
    skip: int = 0, limit: int = 100, db: Session = Depends(sql_db.get_db)
) -> List[sql_models.Service]:
    services = sql_crud.get_services(db, skip=skip, limit=limit)
    return services


@router.get(
    "/api/v1/{entity_did}/service", response_model=List[Service], tags=[Tags.services]
)
def get_service_by_did(
    entity_did: str = "did:sov:test:1234",
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(sql_db.get_db),
) -> List[sql_models.Service]:
    service = sql_crud.get_services_by_entity_did(db, entity_did=entity_did)
    return service


@router.delete("/api/v1/{entity_did}/service", tags=[Tags.services])
def delete_service(
    entity_did: str = "did:sov:test:1234",
    db: Session = Depends(sql_db.get_db),
) -> dict[str, str]:
    sql_crud.delete_service_by_entity_did(db, entity_did)
    return {"message": "service deleted"}


#########################
#                       #
#         Client        #
#                       #
#########################
@router.get(
    "/api/v1/{entity_did}/clients", response_model=List[Service], tags=[Tags.clients]
)
def get_all_clients(
    entity_did: str = "did:sov:test:1234",
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(sql_db.get_db),
) -> List[sql_models.Service]:
    clients = sql_crud.get_services_without_entity_id(
        db, entity_did, skip=skip, limit=limit
    )
    return clients


#########################
#                       #
#       REPOSITORY      #
#                       #
#########################


@router.get(
    "/api/v1/repositories",
    response_model=List[Service],
    tags=[Tags.repositories],
)
def get_all_repositories(
    skip: int = 0, limit: int = 100, db: Session = Depends(sql_db.get_db)
) -> List[sql_models.Service]:
    repositories = sql_crud.get_services(db, skip=skip, limit=limit)
    return repositories


#########################
#                       #
#        Entity         #
#                       #
#########################
@router.post("/api/v1/entity", response_model=Entity, tags=[Tags.entities])
def create_entity(
    entity: EntityCreate, db: Session = Depends(sql_db.get_db)
) -> EntityCreate:
    return sql_crud.create_entity(db, entity)


@router.get("/api/v1/entities", response_model=List[Entity], tags=[Tags.entities])
def get_all_entities(
    skip: int = 0, limit: int = 100, db: Session = Depends(sql_db.get_db)
) -> List[sql_models.Entity]:
    entities = sql_crud.get_entities(db, skip=skip, limit=limit)
    return entities


@router.get(
    "/api/v1/{entity_did}/entity", response_model=Optional[Entity], tags=[Tags.entities]
)
def get_entity_by_did(
    entity_did: str = "did:sov:test:1234",
    db: Session = Depends(sql_db.get_db),
) -> Optional[sql_models.Entity]:
    entity = sql_crud.get_entity_by_did(db, did=entity_did)
    return entity


@router.get(
    "/api/v1/attached_entities",
    response_model=List[Entity],
    tags=[Tags.entities],
)
def get_attached_entities(
    skip: int = 0, limit: int = 100, db: Session = Depends(sql_db.get_db)
) -> List[sql_models.Entity]:
    entities = sql_crud.get_attached_entities(db, skip=skip, limit=limit)
    return entities


@router.post("/api/v1/{entity_did}/detach", response_model=Entity, tags=[Tags.entities])
async def detach_entity(
    background_tasks: BackgroundTasks,
    entity_did: str = "did:sov:test:1234",
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(sql_db.get_db),
) -> sql_models.Entity:
    entity = sql_crud.set_attached_by_entity_did(db, entity_did, False)
    return entity


@router.post("/api/v1/{entity_did}/attach", tags=[Tags.entities])
async def attach_entity(
    background_tasks: BackgroundTasks,
    entity_did: str = "did:sov:test:1234",
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(sql_db.get_db),
) -> dict[str, str]:
    if sql_crud.get_entity_by_did(db, entity_did) is None:
        raise ClanError(f"Entity with did '{entity_did}' not found")

    background_tasks.add_task(attach_entity_loc, db, entity_did)
    return {"message": "Attaching in the background"}


def attach_entity_loc(db: Session, entity_did: str) -> None:
    db_entity = sql_crud.set_attached_by_entity_did(db, entity_did, True)
    try:
        while db_entity.attached:
            # query status endpoint
            # https://www.python-httpx.org/
            response = httpx.get(f"http://{db_entity.ip}", timeout=2)
            print(response)
            # test with:
            #  while true ; do printf 'HTTP/1.1 200 OK\r\n\r\ncool, thanks' | nc -l -N localhost 5555 ; done
            # client test (apt install python3-httpx):
            #  httpx http://localhost:5555
            # except not reached set false
            time.sleep(1)
    except Exception:
        log.warning(f"Entity {entity_did} not reachable. Setting attached to false")

        db_entity = sql_crud.set_attached_by_entity_did(db, entity_did, False)


@router.delete("/api/v1/{entity_did}/entity", tags=[Tags.entities])
def delete_entity(
    entity_did: str = "did:sov:test:1234",
    db: Session = Depends(sql_db.get_db),
) -> dict[str, str]:
    sql_crud.delete_entity_by_did_recursive(db, did=entity_did)
    return {"message": "Entity deleted and all relations to that entity"}


#########################
#                       #
#      Resolution       #
#                       #
#########################


@router.get(
    "/api/v1/resolutions", response_model=List[Resolution], tags=[Tags.resolutions]
)
def get_all_resolutions(
    skip: int = 0, limit: int = 100, db: Session = Depends(sql_db.get_db)
) -> List[Resolution]:
    # TODO: Get resolutions from DLG entity

    return [
        Resolution(
            requester_name="C1",
            requester_did="did:sov:test:1122",
            resolved_did="did:sov:test:1234",
            other={"test": "test"},
            timestamp=datetime.now(),
            id=1,
        )
    ]
