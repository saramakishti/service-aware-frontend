from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import sql_crud, sql_db, sql_schemas

router = APIRouter()

@router.get("/get_producers", response_model=list[sql_schemas.Producer])
def get_producers(skip: int = 0, limit: int = 100, db: Session = Depends(sql_db.get_db)):
    producers = sql_crud.get_producers(db, skip=skip, limit=limit)
    return producers

@router.post("/create_producers", response_model=sql_schemas.Producer)
def create_producers(producer: sql_schemas.ProducerCreate, db: Session = Depends(sql_db.get_db)):
    #todo checken ob schon da ...
    return sql_crud.create_producer(db=db, producer=producer)