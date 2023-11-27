from typing import List, Optional

from sqlalchemy.orm import Session

from . import schemas, sql_models

#########################
#                       #
#       Producer        #
#                       #
#########################


def create_producer(
    db: Session, producer: schemas.ProducerCreate
) -> sql_models.Producer:
    db_producer = sql_models.Producer(**producer.dict())
    db.add(db_producer)
    db.commit()
    db.refresh(db_producer)
    return db_producer


def get_producers(
    db: Session, skip: int = 0, limit: int = 100
) -> List[sql_models.Producer]:
    return db.query(sql_models.Producer).offset(skip).limit(limit).all()


def get_producers_by_entity_did(
    db: Session, entity_did: str, skip: int = 0, limit: int = 100
) -> List[sql_models.Producer]:
    return (
        db.query(sql_models.Producer)
        .filter(sql_models.Producer.entity_did == entity_did)
        .offset(skip)
        .limit(limit)
        .all()
    )


#########################
#                       #
#       Consumer        #
#                       #
#########################


def create_consumer(
    db: Session, consumer: schemas.ConsumerCreate
) -> sql_models.Consumer:
    db_consumer = sql_models.Consumer(**consumer.dict())
    db.add(db_consumer)
    db.commit()
    db.refresh(db_consumer)
    return db_consumer


def get_consumers(
    db: Session, skip: int = 0, limit: int = 100
) -> List[sql_models.Consumer]:
    return db.query(sql_models.Consumer).offset(skip).limit(limit).all()


def get_consumers_by_entity_did(
    db: Session, entity_did: str, skip: int = 0, limit: int = 100
) -> List[sql_models.Consumer]:
    return (
        db.query(sql_models.Consumer)
        .filter(sql_models.Consumer.entity_did == entity_did)
        .offset(skip)
        .limit(limit)
        .all()
    )


#########################
#                       #
#       REPOSITORY      #
#                       #
#########################
def create_repository(
    db: Session, repository: schemas.RepositoryCreate
) -> sql_models.Repository:
    db_repository = sql_models.Repository(**repository.dict())
    db.add(db_repository)
    db.commit()
    db.refresh(db_repository)
    return db_repository


def get_repositories(
    db: Session, skip: int = 0, limit: int = 100
) -> List[sql_models.Repository]:
    return db.query(sql_models.Repository).offset(skip).limit(limit).all()


def get_repository_by_uuid(db: Session, uuid: str) -> Optional[sql_models.Repository]:
    return (
        db.query(sql_models.Repository)
        .filter(sql_models.Repository.uuid == uuid)
        .first()
    )


def get_repository_by_did(
    db: Session, did: str, skip: int = 0, limit: int = 100
) -> List[sql_models.Repository]:
    return (
        db.query(sql_models.Repository)
        .filter(sql_models.Repository.entity_did == did)
        .offset(skip)
        .limit(limit)
        .all()
    )


#########################
#                       #
#        Entity         #
#                       #
#########################
def create_entity(db: Session, entity: schemas.EntityCreate) -> sql_models.Entity:
    db_entity = sql_models.Entity(**entity.dict())
    db.add(db_entity)
    db.commit()
    db.refresh(db_entity)
    return db_entity


def get_entities(
    db: Session, skip: int = 0, limit: int = 100
) -> List[sql_models.Entity]:
    return db.query(sql_models.Entity).offset(skip).limit(limit).all()


def get_entity_by_did(db: Session, did: str) -> Optional[sql_models.Entity]:
    return db.query(sql_models.Entity).filter(sql_models.Entity.did == did).first()
