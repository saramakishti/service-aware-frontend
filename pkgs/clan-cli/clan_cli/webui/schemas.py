from enum import Enum

from pydantic import BaseModel, Field


class Status(Enum):
    ONLINE = "online"
    OFFLINE = "offline"
    UNKNOWN = "unknown"


class Machine(BaseModel):
    name: str
    status: Status


class EntityBase(BaseModel):
    did: str = "did:sov:test:1234"
    name: str = "C1"
    ip: str = "127.0.0.1"
    attached: bool = False
    other: dict = {"test": "test"}


class Entity(EntityBase):
    class Config:
        orm_mode = True


class EntityCreate(EntityBase):
    pass


class RepositoryBase(BaseModel):
    title: str
    description: str | None = None


class RepositoryCreate(RepositoryBase):
    pass


class Repository(RepositoryBase):
    id: int
    prod_id: str

    class Config:
        orm_mode = True


class ProducerBase(BaseModel):
    id: int


class ProducerCreate(ProducerBase):
    jsonblob: int = Field(
        42,
        title="The Json",
        description="this is the value of json",
        gt=30,
        lt=50,
        list=[1, 2, "3"],
    )


class Producer(ProducerBase):
    id: int
    repos: list[Repository] = []

    class Config:
        orm_mode = True
