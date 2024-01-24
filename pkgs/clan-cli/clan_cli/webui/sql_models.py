from sqlalchemy import JSON, Boolean, Column, Enum, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from .db_types import Role
from .sql_db import Base


# SQLAlchemy model for the "entities" table
class Entity(Base):
    __tablename__ = "entities"

    ## Queryable body ##
    # Primary Key
    did = Column(String, primary_key=True, index=True)
    # Indexed Columns
    name = Column(String, index=True, unique=True)
    ip = Column(String, index=True)
    network = Column(String, index=True)
    attached = Column(Boolean, index=True)
    visible = Column(Boolean, index=True)
    stop_health_task = Column(Boolean)

    ## Non queryable body ##
    # JSON field for additional non-queryable data
    other = Column(JSON)

    ## Relations ##
    # One-to-Many relationship with "services" table
    services = relationship("Service", back_populates="entity")
    # One-to-Many relationship with "entity_roles" table
    roles = relationship("EntityRoles", back_populates="entity")
    # One-to-Many relationship with "service_usage" table
    consumes = relationship("ServiceUsage", back_populates="consumer_entity")


# SQLAlchemy model for the "entity_roles" table
class EntityRoles(Base):
    __tablename__ = "entity_roles"

    ## Queryable body ##
    # Primary Key
    id = Column(Integer, primary_key=True, autoincrement=True)
    # Foreign Key
    entity_did = Column(String, ForeignKey("entities.did"))
    # Enum field for role
    role = Column(Enum(Role), index=True, nullable=False)  # type: ignore

    ## Relations ##
    # Many-to-One relationship with "entities" table
    entity = relationship("Entity", back_populates="roles")


# SQLAlchemy model for the "service_usage" table
class ServiceUsage(Base):
    __tablename__ = "service_usage"

    ## Queryable body ##
    # Primary Key
    id = Column(Integer, primary_key=True, autoincrement=True)
    # Foreign Key
    consumer_entity_did = Column(String, ForeignKey("entities.did"))
    # Many-to-One relationship with "entities" table
    consumer_entity = relationship("Entity", back_populates="consumes")
    times_consumed = Column(Integer, index=True, nullable=False)

    service_uuid = Column(String, ForeignKey("services.uuid"))
    # Many-to-One relationship with "services" table
    service = relationship("Service", back_populates="usage")


# SQLAlchemy model for the "services" table
class Service(Base):
    __tablename__ = "services"

    # Queryable body
    # Primary Key
    uuid = Column(Text(length=36), primary_key=True, index=True)
    service_name = Column(String, index=True)
    service_type = Column(String, index=True)
    endpoint_url = Column(String, index=True)

    ## Non queryable body ##
    # JSON fields for additional non-queryable data
    other = Column(JSON)
    status = Column(JSON, index=True)
    action = Column(JSON, index=True)

    ## Relations ##
    # One-to-Many relationship with "entities" table
    entity = relationship("Entity", back_populates="services")
    entity_did = Column(String, ForeignKey("entities.did"))

    # One-to-Many relationship with "service_usage" table
    usage = relationship("ServiceUsage", back_populates="service")


# SQLAlchemy model for the "eventmessages" table
class Eventmessage(Base):
    __tablename__ = "eventmessages"

    ## Queryable body ##
    # Primary Key
    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(Integer, index=True)
    group = Column(Integer, index=True)
    group_id = Column(Integer, index=True)
    msg_type = Column(Integer, index=True)  # message type for the label
    src_did = Column(String, index=True)
    des_did = Column(String, index=True)

    ## Non queryable body ##
    # JSON field for additional non-queryable data
    msg = Column(JSON)

    ## Relations ##
    # One-to-Many relationship with "entities" table
    # One entity can send many messages
    # (Note: The comment is incomplete and can be extended based on the relationship)
