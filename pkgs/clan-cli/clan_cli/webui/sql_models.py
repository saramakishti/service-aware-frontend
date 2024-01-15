from sqlalchemy import JSON, Boolean, Column, Enum, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from .db_types import Role
from .sql_db import Base

# Relationsship example
# https://dev.to/freddiemazzilli/flask-sqlalchemy-relationships-exploring-relationship-associations-igo


class Entity(Base):
    __tablename__ = "entities"

    ## Queryable body ##
    did = Column(String, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    ip = Column(String, index=True)
    network = Column(String, index=True)
    attached = Column(Boolean, index=True)
    visible = Column(Boolean, index=True)
    stop_health_task = Column(Boolean)

    ## Non queryable body ##
    # In here we deposit: Not yet defined stuff
    other = Column(JSON)

    ## Relations ##
    services = relationship("Service", back_populates="entity")
    roles = relationship("EntityRoles", back_populates="entity")
    consumes = relationship("ServiceUsage", back_populates="consumer_entity")


class EntityRoles(Base):
    __tablename__ = "entity_roles"

    ## Queryable body ##
    id = Column(Integer, primary_key=True, autoincrement=True)
    entity_did = Column(String, ForeignKey("entities.did"))
    role = Column(Enum(Role), index=True, nullable=False)  # type: ignore

    ## Relations ##
    entity = relationship("Entity", back_populates="roles")


class ServiceUsage(Base):
    __tablename__ = "service_usage"

    ## Queryable body ##
    id = Column(Integer, primary_key=True, autoincrement=True)
    consumer_entity_did = Column(String, ForeignKey("entities.did"))
    consumer_entity = relationship("Entity", back_populates="consumes")
    times_consumed = Column(Integer, index=True, nullable=False)

    service_uuid = Column(String, ForeignKey("services.uuid"))
    service = relationship("Service", back_populates="usage")


class Service(Base):
    __tablename__ = "services"

    # Queryable body
    uuid = Column(Text(length=36), primary_key=True, index=True)
    service_name = Column(String, index=True)
    service_type = Column(String, index=True)
    endpoint_url = Column(String, index=True)

    ## Non queryable body ##
    # In here we deposit: Action
    other = Column(JSON)
    status = Column(JSON, index=True)
    action = Column(JSON, index=True)

    ## Relations ##
    # One entity can have many services
    entity = relationship("Entity", back_populates="services")
    entity_did = Column(String, ForeignKey("entities.did"))

    usage = relationship("ServiceUsage", back_populates="service")


class Eventmessage(Base):
    __tablename__ = "eventmessages"

    ## Queryable body ##
    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(Integer, unique=True, index=True)
    group = Column(Integer, index=True)
    group_id = Column(Integer, index=True)
    msg_type = Column(Integer, index=True)  # message type for the label
    src_did = Column(String, index=True)
    des_did = Column(String, index=True)

    ## Non queryable body ##
    # In here we deposit: Network, Roles, Visible, etc.
    msg = Column(JSON)

    ## Relations ##
    # One entity can send many messages
