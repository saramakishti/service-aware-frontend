from pydantic import BaseModel, Field

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
        title='The Json',
        description='this is the value of json',
        gt=30,
        lt=50,
        list=[1,2,"3"],
    )

class Producer(ProducerBase):
    id: int
    repos: list[Repository] = []
    class Config:
        orm_mode = True
