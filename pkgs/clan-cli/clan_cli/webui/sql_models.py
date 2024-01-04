from sqlalchemy import (
    JSON,
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .sql_db import Base

# Relationsship example
# https://dev.to/freddiemazzilli/flask-sqlalchemy-relationships-exploring-relationship-associations-igo


class Entity(Base):
    __tablename__ = "entities"

    ## Queryable body ##
    did = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    ip = Column(String, index=True)
    attached = Column(Boolean, index=True)
    visible = Column(Boolean, index=True)

    ## Non queryable body ##
    # In here we deposit: Network, Roles, Visible, etc.
    other = Column(JSON)

    ## Relations ##
    services = relationship("Service", back_populates="entity")
    clients = relationship("Client", back_populates="entity")
    repository = relationship("Repository", back_populates="entity")
    # TODO maby refactor to repositories


class ServiceAbstract(Base):
    __abstract__ = True

    # Queryable body
    uuid = Column(Text(length=36), primary_key=True, index=True)
    service_name = Column(String, index=True)
    service_type = Column(String, index=True)
    endpoint_url = Column(String, index=True)
    status = Column(String, index=True)

    ## Non queryable body ##
    # In here we deposit: Action
    other = Column(JSON)


class Service(ServiceAbstract):
    __tablename__ = "services"

    # Usage is the clients column

    ## Relations ##
    # One entity can have many services
    entity = relationship("Entity", back_populates="services")
    entity_did = Column(String, ForeignKey("entities.did"))

    # One service has many clients
    clients = relationship("Client", back_populates="service")


class Client(Base):
    __tablename__ = "clients"

    ## Queryable body ##
    id = Column(Integer, primary_key=True, index=True)

    ## Non queryable body ##
    other = Column(JSON)

    ## Relations ##
    # one entity can have many clients
    entity = relationship("Entity", back_populates="clients")
    entity_did = Column(String, ForeignKey("entities.did"))

    # one client has one service
    service = relationship("Service", back_populates="clients")
    service_uuid = Column(String, ForeignKey("services.uuid"))

    __table_args__ = (UniqueConstraint("service_uuid", "entity_did"),)


class Repository(ServiceAbstract):
    __tablename__ = "repositories"

    time_created = Column(DateTime(timezone=True), server_default=func.now())

    # one repository has one entity
    entity = relationship("Entity", back_populates="repository")
    entity_did = Column(Integer, ForeignKey("entities.did"))


# TODO: Ask how this works exactly
class Resolution(Base):
    __tablename__ = "resolutions"

    id = Column(Integer, primary_key=True)
    requester_name = Column(String, index=True)
    requester_did = Column(String, index=True)
    resolved_did = Column(String, index=True)
    other = Column(JSON)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
