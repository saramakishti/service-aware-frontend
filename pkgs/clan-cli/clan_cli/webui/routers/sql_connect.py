from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import sql_crud, sql_db, sql_models
from ..schemas import Entity, EntityCreate
from ..tags import Tags

router = APIRouter()


# @router.get("/api/v1/get_producers", response_model=List[Producer], tags=[Tags.producers])
# def get_producers(
#     skip: int = 0, limit: int = 100, db: Session = Depends(sql_db.get_db)
# ) -> List[sql_models.Producer]:
#     producers = sql_crud.get_producers(db, skip=skip, limit=limit)
#     return producers


# @router.post("/api/v1/create_producer", response_model=Producer, tags=[Tags.producers])
# def create_producer(
#     producer: ProducerCreate, db: Session = Depends(sql_db.get_db)
# ) -> Producer:
#     # todo checken ob schon da ...
#     return sql_crud.create_producer(db=db, producer=producer)


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
