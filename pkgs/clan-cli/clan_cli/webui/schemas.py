import logging
from datetime import datetime
from typing import List

from pydantic import BaseModel, Field, validator

from . import sql_models
from .db_types import Role, Status

log = logging.getLogger(__name__)


class Machine(BaseModel):
    name: str
    status: Status


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
class ServiceBase(BaseModel):
    uuid: str = Field(..., example="8e285c0c-4e40-430a-a477-26b3b81e30df")
    service_name: str = Field(..., example="Carlos Printing")
    service_type: str = Field(..., example="3D Printing")
    endpoint_url: str = Field(..., example="http://127.0.0.1:8000")
    status: str = Field(..., example="unknown")
    other: dict = Field(
        ..., example={"action": ["register", "deregister", "delete", "create"]}
    )


class ServiceCreate(ServiceBase):
    entity_did: str = Field(..., example="did:sov:test:120")


class Service(ServiceCreate):
    entity: Entity

    class Config:
        orm_mode = True


class ServicesByName(BaseModel):
    entity: Entity
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
    src_did: str = Field(..., example="did:sov:test:2234")
    des_did: str = Field(..., example="did:sov:test:120")


class EventmessageCreate(EventmessageBase):
    msg: dict = Field(..., example={"optinal": "values"})  # optional


class Eventmessage(EventmessageCreate):
    id: int = Field(...)

    class Config:
        orm_mode = True
