from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

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
)
from ..tags import Tags

router = APIRouter()


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
    repository = sql_crud.get_repository_by_did(db, did=entity_did)
    return repository


#########################
#                       #
#        Entity         #
#                       #
#########################
@router.post("/api/v1/create_entity", response_model=Entity, tags=[Tags.entities])
def create_entity(
    entity: EntityCreate, db: Session = Depends(sql_db.get_db)
) -> EntityCreate:
    # todo checken ob schon da ...
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
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(sql_db.get_db),
) -> Optional[sql_models.Entity]:
    entity = sql_crud.get_entity_by_did(db, did=entity_did)
    return entity
