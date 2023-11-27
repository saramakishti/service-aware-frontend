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

    ## Non queryable body ##
    # In here we deposit: Network, Roles, Visible, etc.
    other = Column(JSON)

    ## Relations ##
    producers = relationship("Producer", back_populates="entity")
    consumers = relationship("Consumer", back_populates="entity")
    repository = relationship("Repository", uselist=False, back_populates="entity")


class ProducerAbstract(Base):
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


class Producer(ProducerAbstract):
    __tablename__ = "producers"

    # Usage is the consumers column

    ## Relations ##
    # One entity can have many producers
    entity = relationship("Entity", back_populates="producers")
    entity_did = Column(String, ForeignKey("entities.did"))

    # One producer has many consumers
    consumers = relationship("Consumer", back_populates="producer")


class Consumer(Base):
    __tablename__ = "consumers"

    ## Queryable body ##
    id = Column(Integer, primary_key=True, index=True)

    ## Non queryable body ##
    other = Column(JSON)

    ## Relations ##
    # one entity can have many consumers
    entity = relationship("Entity", back_populates="consumers")
    entity_did = Column(String, ForeignKey("entities.did"))

    # one consumer has one producer
    producer = relationship("Producer", back_populates="consumers")
    producer_uuid = Column(String, ForeignKey("producers.uuid"))

    __table_args__ = (UniqueConstraint("producer_uuid", "entity_did"),)


class Repository(ProducerAbstract):
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
    timestamp = Column(DateTime, index=True)
