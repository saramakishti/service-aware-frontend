import logging
import time
from datetime import datetime
from typing import List, Optional
import asyncio

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
    ServicesByName,
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
    "/api/v1/service", response_model=List[Service], tags=[Tags.services]
)
def get_service_by_did(
    entity_did: str = "did:sov:test:1234",
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(sql_db.get_db),
) -> List[sql_models.Service]:
    service = sql_crud.get_services_by_entity_did(db, entity_did=entity_did)
    return service


@router.get(
    "/api/v1/services_without_entity",
    response_model=List[Service],
    tags=[Tags.services],
)
def get_services_without_entity(
    entity_did: str = "did:sov:test:1234",
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(sql_db.get_db),
) -> List[sql_models.Service]:
    service = sql_crud.get_services_without_entity_id(db, entity_did=entity_did)
    return service

@router.delete("/api/v1/service", tags=[Tags.services])
def delete_service(
    entity_did: str = "did:sov:test:1234",
    db: Session = Depends(sql_db.get_db),
) -> dict[str, str]:
    sql_crud.delete_service_by_entity_did(db, entity_did)
    return {"message": "service deleted"}


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


@router.get(
    "/api/v1/entity_by_name", response_model=Optional[Entity], tags=[Tags.entities]
)
def get_entity_by_name(
    entity_name: str, db: Session = Depends(sql_db.get_db)
) -> Optional[sql_models.Entity]:
    entity = sql_crud.get_entity_by_name(db, name=entity_name)
    return entity


@router.get("/api/v1/entities", response_model=List[Entity], tags=[Tags.entities])
def get_all_entities(
    skip: int = 0, limit: int = 100, db: Session = Depends(sql_db.get_db)
) -> List[sql_models.Entity]:
    entities = sql_crud.get_entities(db, skip=skip, limit=limit)
    return entities


@router.get(
    "/api/v1/entity", response_model=Optional[Entity], tags=[Tags.entities]
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

@router.get("/api/v1/is_attached", tags=[Tags.entities])
def is_attached(
    entity_did: str = "did:sov:test:1234",
    db: Session = Depends(sql_db.get_db)) -> dict[str, str]:

    entity = sql_crud.get_entity_by_did(db, did=entity_did)

    if entity is None:
        raise ClanError(f"Entity with did '{entity_did}' not found")

    timer = 0.0
    timeout = 2
    while not entity.attached:
        time.sleep(0.1)

        timer += 0.1
        if timer > timeout:
            url = f"http://{entity.ip}"
            raise ClanError(f"Entity at {url} not reachable")

    return {"message": f"Attached to {entity.name} successfully"}



@router.post("/api/v1/detach", tags=[Tags.entities])
def detach_entity(
    background_tasks: BackgroundTasks,
    entity_did: str = "did:sov:test:1234",
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(sql_db.get_db),
) -> dict[str, str]:
    sql_crud.stop_entity_health_task(db, entity_did)
    return {"message": f"Detached {entity_did} successfully"}


@router.post("/api/v1/attach", tags=[Tags.entities])
def attach_entity(
    background_tasks: BackgroundTasks,
    entity_did: str = "did:sov:test:1234",
    skip: int = 0,
    limit: int = 100
) -> dict[str, str]:
    # entity = sql_crud.get_entity_by_did(db, did=entity_did)
    # if entity is None:
    #     raise ClanError(f"Entity with did '{entity_did}' not found")
    #url = f"http://{entity.ip}"
    #log.info("Start health query at", url)
    background_tasks.add_task(attach_entity_loc, entity_did)
    return {"message": f"Started attachment task for {entity_did}"}


def attach_entity_loc(entity_did: str) -> None:
    with sql_db.SessionLocal() as db:
        entity = sql_crud.get_entity_by_did(db, did=entity_did)
        while entity.stop_health_task is False:
            entity = sql_crud.get_entity_by_did(db, did=entity_did)
            assert entity is not None
            log.warning(f"Stop health status task for {entity.stop_health_task}")
            time.sleep(1)
    # entity = sql_crud.get_entity_by_did(db, did=entity_did)
    # assert entity is not None
    # try:

    #     while True:


    #         if entity.stop_health_task:
    #             print(f"Stop health status task for {entity.name}")
    #             break

    #         url = f"http://{entity.ip}"
    #         response = httpx.get(url, timeout=2)
    #         #log.warning(f"Response {response.status_code} from {url}")
    #         print(f"{entity.name}: stop_health_task: {entity.stop_health_task}")
    #         if response.status_code != 200:
    #             raise ClanError(f"Entity with did '{entity_did}' returned {response.status_code}")

    #         if entity.attached is False:
    #             sql_crud.set_attached_by_entity_did(db, entity_did, True)
    #         if entity is None:
    #             raise ClanError(f"Entity with did '{entity_did}' has been deleted")

    #         time.sleep(1)
    # except Exception:
    #     log.warning(f"Entity {entity_did} not reachable at {url}")
    # finally:
    #     sql_crud.set_attached_by_entity_did(db, entity_did, False)


@router.delete("/api/v1/entity", tags=[Tags.entities])
async def delete_entity(
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
async def get_all_resolutions(
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
