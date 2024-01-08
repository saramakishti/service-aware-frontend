from sqlalchemy import (
    JSON,
    Boolean,
    Column,
    ForeignKey,
    String,
    Text,
)
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
