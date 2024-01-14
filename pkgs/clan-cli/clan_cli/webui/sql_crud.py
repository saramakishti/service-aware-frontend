from typing import List, Optional

from sqlalchemy import func
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import true

from ..errors import ClanError
from . import schemas, sql_models

#########################
#                       #
#       service         #
#                       #
#########################


def create_service(db: Session, service: schemas.ServiceCreate) -> sql_models.Service:
    db_service = sql_models.Service(**service.dict())
    db.add(db_service)
    db.commit()
    db.refresh(db_service)
    return db_service


def get_services(
    db: Session, skip: int = 0, limit: int = 100
) -> List[sql_models.Service]:
    return db.query(sql_models.Service).offset(skip).limit(limit).all()


def get_services_by_entity_did(
    db: Session, entity_did: str, skip: int = 0, limit: int = 100
) -> List[sql_models.Service]:
    return (
        db.query(sql_models.Service)
        .filter(sql_models.Service.entity_did == entity_did)
        .offset(skip)
        .limit(limit)
        .all()
    )


def delete_service_by_entity_did(db: Session, entity_did: str) -> None:
    db.query(sql_models.Service).filter(
        sql_models.Service.entity_did == entity_did
    ).delete()
    db.commit()


def get_services_without_entity_id(
    db: Session, entity_did: str, skip: int = 0, limit: int = 100
) -> List[sql_models.Service]:
    return (
        db.query(sql_models.Service)
        .filter(sql_models.Service.entity_did != entity_did)
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
    db_entity = sql_models.Entity(
        did=entity.did,
        name=entity.name,
        ip=entity.ip,
        network=entity.network,
        visible=entity.visible,
        other=entity.other,
        attached=False,
        stop_health_task=False,
    )

    db_roles = []
    for role in entity.roles:
        db_roles.append(sql_models.EntityRoles(role=role))

    db_entity.roles = db_roles
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


def get_entity_by_name_or_did(db: Session, name: str) -> Optional[sql_models.Entity]:
    return (
        db.query(sql_models.Entity)
        .filter((sql_models.Entity.name == name) | (sql_models.Entity.did == name))
        .first()
    )


def get_entity_by_role(
    db: Session, roles: List[schemas.Role]
) -> List[sql_models.Entity]:
    # create a subquery to count the matching roles for each entity
    subquery = (
        db.query(
            sql_models.EntityRoles.entity_did,
            func.count(sql_models.EntityRoles.role).label("role_count"),
        )
        .filter(sql_models.EntityRoles.role.in_(roles))
        .group_by(sql_models.EntityRoles.entity_did)
        .subquery()
    )
    # join the subquery with the entity table and filter by the role count
    return (
        db.query(sql_models.Entity)
        .join(subquery, sql_models.Entity.did == subquery.c.entity_did)
        .filter(subquery.c.role_count == len(roles))
        .all()
    )


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
def set_stop_health_task(db: Session, entity_did: str, value: bool) -> None:
    db_entity = get_entity_by_did(db, entity_did)
    if db_entity is None:
        raise ClanError(f"Entity with did '{entity_did}' not found")

    db_entity.stop_health_task = value  # type: ignore

    # save changes in db
    db.add(db_entity)
    db.commit()


def set_attached_by_entity_did(db: Session, entity_did: str, attached: bool) -> None:
    db_entity = get_entity_by_did(db, entity_did)
    if db_entity is None:
        raise ClanError(f"Entity with did '{entity_did}' not found")

    db_entity.attached = attached  # type: ignore

    # save changes in db
    db.add(db_entity)
    db.commit()


def delete_entity_by_did(db: Session, did: str) -> None:
    db.query(sql_models.Entity).filter(sql_models.Entity.did == did).delete()
    db.commit()


def delete_entity_by_did_recursive(db: Session, did: str) -> None:
    delete_service_by_entity_did(db, did)
    delete_entity_by_did(db, did)


#########################
#                       #
#      Eventmessage     #
#                       #
#########################


def create_eventmessage(
    db: Session, eventmsg: schemas.EventmessageCreate
) -> sql_models.Eventmessage:
    db_eventmessage = sql_models.Eventmessage(
        timestamp=eventmsg.timestamp,
        group=eventmsg.group,
        group_id=eventmsg.group_id,
        msg_type=eventmsg.msg_type,
        src_did=eventmsg.src_did,
        des_did=eventmsg.des_did,
        msg=eventmsg.msg,
    )
    db.add(db_eventmessage)
    db.commit()
    db.refresh(db_eventmessage)
    return db_eventmessage


def get_eventmessages(
    db: Session, skip: int = 0, limit: int = 100
) -> List[sql_models.Eventmessage]:
    return db.query(sql_models.Eventmessage).offset(skip).limit(limit).all()
