from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import sql_crud, sql_db, sql_models
from ..api_outputs import Producer, ProducerCreate

router = APIRouter()


@router.get("/get_producers", response_model=List[Producer])
def get_producers(
    skip: int = 0, limit: int = 100, db: Session = Depends(sql_db.get_db)
) -> List[sql_models.Producer]:
    producers = sql_crud.get_producers(db, skip=skip, limit=limit)
    return producers


@router.post("/create_producers", response_model=Producer)
def create_producers(
    producer: ProducerCreate, db: Session = Depends(sql_db.get_db)
) -> Producer:
    # todo checken ob schon da ...
    return sql_crud.create_producer(db=db, producer=producer)
