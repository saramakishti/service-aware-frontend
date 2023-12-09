import logging
import time
from typing import List, Optional

import httpx
from fastapi import APIRouter, BackgroundTasks, Depends
from sqlalchemy.orm import Session

from ...errors import ClanError
from .. import sql_crud, sql_db, sql_models
from ..schemas import (
    Consumer,
    ConsumerCreate,
    Entity,
    EntityCreate,
    Producer,
    ProducerCreate,
    Repository,
    RepositoryCreate,
    Resolution,
    ResolutionCreate,
)
from ..tags import Tags

router = APIRouter()

log = logging.getLogger(__name__)


#########################
#                       #
#       Producer        #
#                       #
#########################
@router.post("/api/v1/create_producer", response_model=Producer, tags=[Tags.producers])
def create_producer(
    producer: ProducerCreate, db: Session = Depends(sql_db.get_db)
) -> Producer:
    # todo checken ob schon da ...
    return sql_crud.create_producer(db=db, producer=producer)


@router.get(
    "/api/v1/get_producers", response_model=List[Producer], tags=[Tags.producers]
)
def get_producers(
    skip: int = 0, limit: int = 100, db: Session = Depends(sql_db.get_db)
) -> List[sql_models.Producer]:
    producers = sql_crud.get_producers(db, skip=skip, limit=limit)
    return producers


@router.get(
    "/api/v1/get_producer", response_model=List[Producer], tags=[Tags.producers]
)
def get_producer(
    entity_did: str = "did:sov:test:1234",
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(sql_db.get_db),
) -> List[sql_models.Producer]:
    producer = sql_crud.get_producers_by_entity_did(db, entity_did=entity_did)
    return producer


@router.delete("/api/v1/delete_producer", tags=[Tags.producers])
def delete_producer(
    entity_did: str = "did:sov:test:1234",
    db: Session = Depends(sql_db.get_db),
) -> dict[str, str]:
    sql_crud.delete_producer_by_entity_did(db, entity_did)
    return {"message": "Producer deleted"}


#########################
#                       #
#       Consumer        #
#                       #
#########################
@router.post("/api/v1/create_consumer", response_model=Consumer, tags=[Tags.consumers])
def create_consumer(
    consumer: ConsumerCreate, db: Session = Depends(sql_db.get_db)
) -> Consumer:
    # todo checken ob schon da ...
    return sql_crud.create_consumer(db=db, consumer=consumer)


@router.get(
    "/api/v1/get_consumers", response_model=List[Consumer], tags=[Tags.consumers]
)
def get_consumers(
    skip: int = 0, limit: int = 100, db: Session = Depends(sql_db.get_db)
) -> List[sql_models.Consumer]:
    consumers = sql_crud.get_consumers(db, skip=skip, limit=limit)
    return consumers


@router.get(
    "/api/v1/get_consumer", response_model=List[Consumer], tags=[Tags.consumers]
)
def get_consumer(
    entity_did: str = "did:sov:test:1234",
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(sql_db.get_db),
) -> List[sql_models.Consumer]:
    consumer = sql_crud.get_consumers_by_entity_did(db, entity_did=entity_did)
    return consumer


@router.delete("/api/v1/delete_consumer", tags=[Tags.consumers])
def delete_consumer(
    entity_did: str = "did:sov:test:1234",
    db: Session = Depends(sql_db.get_db),
) -> dict[str, str]:
    sql_crud.delete_consumer_by_entity_did(db, entity_did)
    return {"message": "Consumer deleted"}


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
