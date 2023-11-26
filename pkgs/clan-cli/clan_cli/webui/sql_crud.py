from sqlalchemy.orm import Session

from . import sql_models, sql_schemas


def get_producers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(sql_models.Producer).offset(skip).limit(limit).all()

def create_producer(db: Session, producer: sql_schemas.ProducerCreate):
    jsonblob_init = {"test_repo":"jsonblob_create"}
    db_producer = sql_models.Producer(jsonblob=jsonblob_init)
    db.add(db_producer)
    db.commit()
    db.refresh(db_producer)
    return db_producer


def get_repositories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(sql_models.Repository).offset(skip).limit(limit).all()

def create_repository(db: Session, repository: sql_schemas.RepositoryCreate, producers_id: int):
    db_repository = sql_models.Repository(**repository.dict(), prod_id=producers_id)
    db.add(db_repository)
    db.commit()
    db.refresh(db_repository)
    return db_repository