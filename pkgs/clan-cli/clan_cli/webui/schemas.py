from datetime import datetime
from enum import Enum
from typing import List

from pydantic import BaseModel, Field


class Status(Enum):
    ONLINE = "online"
    OFFLINE = "offline"
    UNKNOWN = "unknown"


class Machine(BaseModel):
    name: str
    status: Status


#########################
#                       #
#        Entity         #
#                       #
#########################
class EntityBase(BaseModel):
    did: str = Field(..., example="did:sov:test:1234")
    name: str = Field(..., example="C1")
    ip: str = Field(..., example="127.0.0.1")
    visible: bool = Field(..., example=True)
    other: dict = Field(
        ...,
        example={
            "network": "Carlos Home Network",
            "roles": ["service repository", "service prosumer"],
        },
    )


class EntityCreate(EntityBase):
    pass


class Entity(EntityCreate):
    attached: bool = Field(...)
    stop_health_task: bool = Field(...)

    class Config:
        orm_mode = True


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
    entity_did: str = Field(..., example="did:sov:test:1234")


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
    resolved_did: str = Field(..., example="did:sov:test:1234")
    other: dict = Field(..., example={"test": "test"})


class ResolutionCreate(ResolutionBase):
    pass


class Resolution(ResolutionCreate):
    timestamp: datetime
    id: int

    class Config:
        orm_mode = True
