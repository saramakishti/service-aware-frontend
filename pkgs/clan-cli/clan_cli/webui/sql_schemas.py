from pydantic import BaseModel


class ProducerBase(BaseModel):
    title: str
    description: str | None = None


class ProducerCreate(ProducerBase):
    service_name: str
    service_type: str
    end_point: str
    usage_str: str
    status: str
    action: str


class Producer(ProducerBase):
    id: int

    class Config:
        orm_mode = True


class RepositoryBase(BaseModel):
    service_name: str


class RepositoryCreate(RepositoryBase):
    service_type: str
    end_point: str
    producer_did: str
    network: str


class Repository(RepositoryBase):
    id: int
    Producers: list[Producer] = []

    class Config:
        orm_mode = True
