from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, JSON
from sqlalchemy.orm import relationship
from .sql_db import Base

class Producer(Base):
    __tablename__ = "producers"

    id = Column(Integer, primary_key=True, index=True)
    jsonblob = Column(JSON)

    repos = relationship("Repository", back_populates="producer")

class Repository(Base):
    __tablename__ = "repositories"

    id = Column(Integer, primary_key=True, index=True)
    jsonblob = Column(JSON)
    prod_id = Column(Integer, ForeignKey("producers.id"))

    producer = relationship("Producer", back_populates="repos")