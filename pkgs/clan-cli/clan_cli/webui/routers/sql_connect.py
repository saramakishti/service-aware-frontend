import logging
import time
from typing import List, Optional

import httpx
from fastapi import APIRouter, BackgroundTasks, Depends
from sqlalchemy.orm import Session

from ...errors import ClanError
from .. import sql_crud, sql_db, sql_models
from ..schemas import (
    Client,
    ClientCreate,
    Entity,
    EntityCreate,
    Repository,
    RepositoryCreate,
    Resolution,
    ResolutionCreate,
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
@router.post("/api/v1/create_service", response_model=Service, tags=[Tags.services])
def create_service(
    service: ServiceCreate, db: Session = Depends(sql_db.get_db)
) -> Service:
    # todo checken ob schon da ...
    return sql_crud.create_service(db=db, service=service)


@router.get("/api/v1/get_services", response_model=List[Service], tags=[Tags.services])
def get_services(
    skip: int = 0, limit: int = 100, db: Session = Depends(sql_db.get_db)
) -> List[sql_models.Service]:
    services = sql_crud.get_services(db, skip=skip, limit=limit)
    return services


@router.get("/api/v1/get_service", response_model=List[Service], tags=[Tags.services])
def get_service(
    entity_did: str = "did:sov:test:1234",
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(sql_db.get_db),
) -> List[sql_models.Service]:
    service = sql_crud.get_services_by_entity_did(db, entity_did=entity_did)
    return service


@router.delete("/api/v1/delete_service", tags=[Tags.services])
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
@router.post("/api/v1/create_client", response_model=Client, tags=[Tags.clients])
def create_client(client: ClientCreate, db: Session = Depends(sql_db.get_db)) -> Client:
    # todo checken ob schon da ...
    return sql_crud.create_client(db=db, client=client)


@router.get("/api/v1/get_clients", response_model=List[Client], tags=[Tags.clients])
def get_clients(
    skip: int = 0, limit: int = 100, db: Session = Depends(sql_db.get_db)
) -> List[sql_models.Client]:
    clients = sql_crud.get_clients(db, skip=skip, limit=limit)
    return clients


@router.get("/api/v1/get_client", response_model=List[Client], tags=[Tags.clients])
def get_client(
    entity_did: str = "did:sov:test:1234",
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(sql_db.get_db),
) -> List[sql_models.Client]:
    client = sql_crud.get_client_by_entity_did(db, entity_did=entity_did)
    return client


@router.delete("/api/v1/delete_client", tags=[Tags.clients])
def delete_client(
    entity_did: str = "did:sov:test:1234",
    db: Session = Depends(sql_db.get_db),
) -> dict[str, str]:
    sql_crud.delete_client_by_entity_did(db, entity_did)
    return {"message": "client deleted"}


#########################
#                       #
#       REPOSITORY      #
#                       #
#########################
@router.post(
    "/api/v1/create_repository", response_model=Repository, tags=[Tags.repositories]
)
def create_repository(
    repository: RepositoryCreate, db: Session = Depends(sql_db.get_db)
) -> sql_models.Repository:
    # todo checken ob schon da ...
    return sql_crud.create_repository(db=db, repository=repository)


@router.get(
    "/api/v1/get_repositories",
    response_model=List[Repository],
    tags=[Tags.repositories],
)
def get_repositories(
    skip: int = 0, limit: int = 100, db: Session = Depends(sql_db.get_db)
) -> List[sql_models.Repository]:
    repositories = sql_crud.get_repositories(db, skip=skip, limit=limit)
    return repositories


@router.get(
    "/api/v1/get_repository", response_model=List[Repository], tags=[Tags.repositories]
)
def get_repository(
    entity_did: str = "did:sov:test:1234",
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(sql_db.get_db),
) -> List[sql_models.Repository]:
    repository = sql_crud.get_repository_by_entity_did(db, did=entity_did)
    return repository


@router.delete("/api/v1/delete_repository", tags=[Tags.repositories])
def delete_repository(
    entity_did: str = "did:sov:test:1234",
    db: Session = Depends(sql_db.get_db),
) -> dict[str, str]:
    sql_crud.delete_repository_by_entity_did(db, did=entity_did)
    return {"message": "Repository deleted"}


#########################
#                       #
#        Entity         #
#                       #
#########################
@router.post("/api/v1/create_entity", response_model=Entity, tags=[Tags.entities])
def create_entity(
    entity: EntityCreate, db: Session = Depends(sql_db.get_db)
) -> EntityCreate:
    return sql_crud.create_entity(db, entity)


@router.get("/api/v1/get_entities", response_model=List[Entity], tags=[Tags.entities])
def get_entities(
    skip: int = 0, limit: int = 100, db: Session = Depends(sql_db.get_db)
) -> List[sql_models.Entity]:
    entities = sql_crud.get_entities(db, skip=skip, limit=limit)
    return entities


@router.get("/api/v1/get_entity", response_model=Optional[Entity], tags=[Tags.entities])
def get_entity(
    entity_did: str = "did:sov:test:1234",
    db: Session = Depends(sql_db.get_db),
) -> Optional[sql_models.Entity]:
    entity = sql_crud.get_entity_by_did(db, did=entity_did)
    return entity


@router.get(
    "/api/v1/get_attached_entities",
    response_model=List[Entity],
    tags=[Tags.entities],
)
def get_attached_entities(
    skip: int = 0, limit: int = 100, db: Session = Depends(sql_db.get_db)
) -> List[sql_models.Entity]:
    entities = sql_crud.get_attached_entities(db, skip=skip, limit=limit)
    return entities


@router.post("/api/v1/detach", response_model=Entity, tags=[Tags.entities])
async def detach(
    background_tasks: BackgroundTasks,
    entity_did: str = "did:sov:test:1234",
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(sql_db.get_db),
) -> sql_models.Entity:
    entity = sql_crud.set_attached_by_entity_did(db, entity_did, False)
    return entity


@router.post("/api/v1/attach", tags=[Tags.entities])
async def attach(
    background_tasks: BackgroundTasks,
    entity_did: str = "did:sov:test:1234",
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(sql_db.get_db),
) -> dict[str, str]:
    if sql_crud.get_entity_by_did(db, entity_did) is None:
        raise ClanError(f"Entity with did '{entity_did}' not found")

    background_tasks.add_task(attach_entity, db, entity_did)
    return {"message": "Attaching in the background"}


def attach_entity(db: Session, entity_did: str) -> None:
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


@router.delete("/api/v1/delete_entity_recursive", tags=[Tags.entities])
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
@router.post(
    "/api/v1/create_resolution", response_model=Resolution, tags=[Tags.resolutions]
)
def create_resolution(
    resolution: ResolutionCreate,
    db: Session = Depends(sql_db.get_db),
) -> sql_models.Resolution:
    return sql_crud.create_resolution(db, resolution)


@router.get(
    "/api/v1/get_resolutions", response_model=List[Resolution], tags=[Tags.resolutions]
)
def get_resolutions(
    skip: int = 0, limit: int = 100, db: Session = Depends(sql_db.get_db)
) -> List[sql_models.Resolution]:
    resolutions = sql_crud.get_resolutions(db, skip=skip, limit=limit)
    return resolutions


@router.get(
    "/api/v1/get_resolution", response_model=List[Resolution], tags=[Tags.resolutions]
)
def get_resolution(
    requester_did: str = "did:sov:test:1122",
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(sql_db.get_db),
) -> List[sql_models.Resolution]:
    resolution = sql_crud.get_resolution_by_requester_did(
        db, requester_did=requester_did
    )
    return resolution


@router.delete("/api/v1/delete_resolution", tags=[Tags.resolutions])
def delete_resolution(
    requester_did: str = "did:sov:test:1122",
    db: Session = Depends(sql_db.get_db),
) -> dict[str, str]:
    sql_crud.delete_resolution_by_requester_did(db, requester_did=requester_did)
    return {"message": "Resolution deleted"}
