from sqlalchemy import JSON, Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from .sql_db import Base

# Relationsship example
# https://dev.to/freddiemazzilli/flask-sqlalchemy-relationships-exploring-relationship-associations-igo


class Entity(Base):
    __tablename__ = "entities"

    ## Queryable body ##
    did = Column(String, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    ip = Column(String, index=True)
    attached = Column(Boolean, index=True)
    visible = Column(Boolean, index=True)
    stop_health_task = Column(Boolean)

    ## Non queryable body ##
    # In here we deposit: Network, Roles, Visible, etc.
    other = Column(JSON)

    ## Relations ##
    services = relationship("Service", back_populates="entity")


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

    ## Relations ##
    # One entity can have many services
    entity = relationship("Entity", back_populates="services")
    entity_did = Column(String, ForeignKey("entities.did"))


class Eventmessage(Base):
    __tablename__ = "eventmessages"

    ## Queryable body ##
    id = Column(Integer, primary_key=True, index=True)
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
