from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class Status(Enum):
    ONLINE = "online"
    OFFLINE = "offline"
    UNKNOWN = "unknown"


class Machine(BaseModel):
    name: str
    status: Status


#########################
#                       #
#        Service        #
#                       #
#########################
class ServiceBase(BaseModel):
    uuid: str = "8e285c0c-4e40-430a-a477-26b3b81e30df"
    service_name: str = "Carlos Printing"
    service_type: str = "3D Printing"
    endpoint_url: str = "http://127.0.0.1:8000"
    status: str = "unknown"
    other: dict = {"action": ["register", "deregister", "delete", "create"]}


class ServiceCreate(ServiceBase):
    entity_did: str = "did:sov:test:1234"


class Service(ServiceCreate):
    class Config:
        orm_mode = True


#########################
#                       #
#        Entity         #
#                       #
#########################
class EntityBase(BaseModel):
    did: str = "did:sov:test:1234"
    name: str = "C1"
    ip: str = "127.0.0.1"
    visible: bool = True
    other: dict = {
        "network": "Carlos Home Network",
        "roles": ["service repository", "service prosumer"],
    }


class EntityCreate(EntityBase):
    pass


class Entity(EntityCreate):
    attached: bool

    class Config:
        orm_mode = True


#########################
#                       #
#      Resolution       #
#                       #
#########################
class ResolutionBase(BaseModel):
    requester_name: str = "C1"
    requester_did: str = "did:sov:test:1122"
    resolved_did: str = "did:sov:test:1234"
    other: dict = {"test": "test"}


class ResolutionCreate(ResolutionBase):
    pass


class Resolution(ResolutionCreate):
    timestamp: datetime
    id: int

    class Config:
        orm_mode = True
