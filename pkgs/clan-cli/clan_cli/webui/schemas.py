# Imports
import logging
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field, validator

from . import sql_models
from .db_types import Role, Status

# Set logger
log = logging.getLogger(__name__)


# create basemodel
class Machine(BaseModel):
    name: str
    status: Status


### Create database schema for sql
# each section will represent an own table
#   Entity, Service, Resolution, Eventmessages
# The relation between them is as follows:
#   one Entity can have many Services


#########################
#                       #
#        Entity         #
#                       #
#########################
class EntityRolesBase(BaseModel):
    role: Role = Field(..., example=Role("service_prosumer"))


class EntityRolesCreate(EntityRolesBase):
    id: int = Field(...)
    entity_did: str = Field(...)


class EntityRoles(EntityRolesBase):
    class Config:
        orm_mode = True


class EntityBase(BaseModel):
    did: str = Field(..., example="did:sov:test:120")
    name: str = Field(..., example="C1")
    ip: str = Field(..., example="127.0.0.1")
    network: str = Field(..., example="255.255.0.0")
    visible: bool = Field(..., example=True)
    other: dict = Field(
        ...,
        example={
            "network": "Carlos Home Network",
        },
    )


class EntityCreate(EntityBase):
    roles: List[Role] = Field(..., example=[Role("service_prosumer"), Role("AP")])


class Entity(EntityBase):
    attached: bool = Field(...)
    stop_health_task: bool = Field(...)
    roles: List[Role]

    class Config:
        orm_mode = True

    # define a custom getter function for roles
    @validator("roles", pre=True)
    def get_roles(cls, v: List[sql_models.EntityRoles | Role]) -> List[Role]:
        if (
            isinstance(v, list)
            and len(v) > 0
            and isinstance(v[0], sql_models.EntityRoles)
        ):
            return [x.role for x in v]  # type: ignore
        else:
            return v  # type: ignore


#########################
#                       #
#        Service        #
#                       #
#########################
class ServiceUsageBase(BaseModel):
    times_consumed: int = Field(..., example=2)


class ServiceUsageCreate(ServiceUsageBase):
    consumer_entity_did: str = Field(..., example="did:sov:test:120")


class ServiceUsage(ServiceUsageCreate):
    class Config:
        orm_mode = True


class ServiceBase(BaseModel):
    uuid: str = Field(..., example="bdd640fb-0667-1ad1-1c80-317fa3b1799d")
    service_name: str = Field(..., example="Carlos Printing")
    service_type: str = Field(..., example="3D Printing")
    endpoint_url: str = Field(..., example="http://127.0.0.1:8000")
    other: dict = Field(..., example={"test": "test"})
    entity_did: str = Field(..., example="did:sov:test:120")
    status: dict = Field(..., example={"data": ["draft", "registered"]})
    action: dict = Field(
        ...,
        example={
            "data": [
                {"name": "register", "path": "/register"},
                {"name": "deregister", "path": "/deregister"},
            ]
        },
    )


class ServiceCreate(ServiceBase):
    usage: List[ServiceUsageCreate]


class Service(ServiceBase):
    usage: List[ServiceUsage]

    class Config:
        orm_mode = True


class ServicesByName(BaseModel):
    services: List[Service]

    class Config:
        orm_mode = True


#########################
#                       #
#      Resolution       #
#                       #
#########################
class ResolutionBase(BaseModel):
    requester_name: str = Field(..., example="C1")
    requester_did: str = Field(..., example="did:sov:test:1122")
    resolved_did: str = Field(..., example="did:sov:test:120")
    other: dict = Field(..., example={"test": "test"})


class ResolutionCreate(ResolutionBase):
    pass


class Resolution(ResolutionCreate):
    timestamp: datetime

    class Config:
        orm_mode = True


#########################
#                       #
#      Eventmessage     #
#                       #
#########################
class EventmessageBase(BaseModel):
    timestamp: int = Field(..., example=1234123413)
    group: int = Field(..., example=1)  # event group type (for the label)
    group_id: int = Field(
        ..., example=12345
    )  # specific to one group needed to enable visually nested groups
    msg_type: int = Field(..., example=1)  # message type for the label
    src_did: str = Field(..., example="did:sov:test:121")
    des_did: str = Field(..., example="did:sov:test:120")


class EventmessageCreate(EventmessageBase):
    msg: dict = Field(..., example={"optinal": "values"})  # optional


class Eventmessage(EventmessageCreate):
    id: int = Field(...)
    des_name: Optional[str] = Field(default=None, example="C2")
    src_name: Optional[str] = Field(default=None, example="C1")
    msg_type_name: Optional[str] = Field(default=None, example="Request Send")
    group_name: Optional[str] = Field(default=None, example="Presentation")

    class Config:
        orm_mode = True
