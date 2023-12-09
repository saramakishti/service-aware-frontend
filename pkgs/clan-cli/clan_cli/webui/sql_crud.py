from typing import List, Optional

from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import true

from ..errors import ClanError
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


def delete_producer_by_entity_did(db: Session, entity_did: str) -> None:
    db.query(sql_models.Producer).filter(
        sql_models.Producer.entity_did == entity_did
    ).delete()
    db.commit()


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


def delete_consumer_by_entity_did(db: Session, entity_did: str) -> None:
    db.query(sql_models.Consumer).filter(
        sql_models.Consumer.entity_did == entity_did
    ).delete()
    db.commit()


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


def get_repository_by_entity_did(
    db: Session, did: str, skip: int = 0, limit: int = 100
) -> List[sql_models.Repository]:
    return (
        db.query(sql_models.Repository)
        .filter(sql_models.Repository.entity_did == did)
        .offset(skip)
        .limit(limit)
        .all()
    )


def delete_repository_by_entity_did(db: Session, did: str) -> None:
    db.query(sql_models.Repository).filter(
        sql_models.Repository.entity_did == did
    ).delete()
    db.commit()


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


# get attached
def get_attached_entities(
    db: Session, skip: int = 0, limit: int = 100
) -> List[sql_models.Entity]:
    return (
        db.query(sql_models.Entity)
        .filter(sql_models.Entity.attached == true())
        # https://stackoverflow.com/questions/18998010/flake8-complains-on-boolean-comparison-in-filter-clause
        .offset(skip)
        .limit(limit)
        .all()
    )


# Returns same entity if setting didnt changed something
def set_attached_by_entity_did(
    db: Session, entity_did: str, value: bool
) -> sql_models.Entity:
    db_entity = get_entity_by_did(db, entity_did)
    if db_entity is None:
        raise ClanError(f"Entity with did '{entity_did}' not found")

    setattr(db_entity, "attached", value)

    # save changes in db
    db.add(db_entity)
    db.commit()
    db.refresh(db_entity)
    return db_entity


def delete_entity_by_did(db: Session, did: str) -> None:
    db.query(sql_models.Entity).filter(sql_models.Entity.did == did).delete()
    db.commit()


def delete_entity_by_did_recursive(db: Session, did: str) -> None:
    delete_producer_by_entity_did(db, did)
    delete_consumer_by_entity_did(db, did)
    delete_repository_by_entity_did(db, did)
    delete_entity_by_did(db, did)


#########################
#                       #
#      Resolution       #
#                       #
#########################
def create_resolution(
    db: Session, resolution: schemas.ResolutionCreate
) -> sql_models.Resolution:
    db_resolution = sql_models.Resolution(**resolution.dict())
    db.add(db_resolution)
    db.commit()
    db.refresh(db_resolution)
    return db_resolution


def get_resolutions(
    db: Session, skip: int = 0, limit: int = 100
) -> List[sql_models.Resolution]:
    return db.query(sql_models.Resolution).offset(skip).limit(limit).all()


def get_resolution_by_requester_did(
    db: Session, requester_did: str, skip: int = 0, limit: int = 100
) -> List[sql_models.Resolution]:
    return (
        db.query(sql_models.Resolution)
        .filter(sql_models.Resolution.requester_did == requester_did)
        .offset(skip)
        .limit(limit)
        .all()
    )


def delete_resolution_by_requester_did(db: Session, requester_did: str) -> None:
    db.query(sql_models.Resolution).filter(
        sql_models.Resolution.requester_did == requester_did
    ).delete()
    db.commit()
