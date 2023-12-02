from datetime import datetime
from enum import Enum
from typing import List

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
#       Producer        #
#                       #
#########################
class ProducerBase(BaseModel):
    uuid: str = "8e285c0c-4e40-430a-a477-26b3b81e30df"
    service_name: str = "Carlo's Printing"
    service_type: str = "3D Printing"
    endpoint_url: str = "http://127.0.0.1:8000"
    status: str = "unknown"
    other: dict = {"test": "test"}


class ProducerCreate(ProducerBase):
    entity_did: str = "did:sov:test:1234"


class Producer(ProducerCreate):
    class Config:
        orm_mode = True


#########################
#                       #
#       Consumer        #
#                       #
#########################
class ConsumerBase(BaseModel):
    entity_did: str = "did:sov:test:1234"
    producer_uuid: str = "8e285c0c-4e40-430a-a477-26b3b81e30df"
    other: dict = {"test": "test"}


class ConsumerCreate(ConsumerBase):
    pass


class Consumer(ConsumerCreate):
    id: int

    class Config:
        orm_mode = True


#########################
#                       #
#       REPOSITORY      #
#                       #
#########################
class RepositoryBase(ProducerBase):
    pass


class RepositoryCreate(RepositoryBase):
    entity_did: str = "did:sov:test:1234"


class Repository(RepositoryCreate):
    time_created: datetime

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
    attached: bool = False
    other: dict = {"test": "test"}


class EntityCreate(EntityBase):
    pass


class Entity(EntityCreate):
    producers: List[Producer] = []
    consumers: List[Consumer] = []
    repository: List[Repository] = []

    class Config:
        orm_mode = True
