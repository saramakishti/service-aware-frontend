from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .sql_db import Base

class Repository(Base):
    __tablename__ = "repositories"

    id = Column(Integer, primary_key=True, index=True)
    service_name = Column(String, unique=True, index=True)
    service_type = Column(String, unique=True, index=True)
    end_point = Column(String, unique=True, index=True)
    producer = Column(String)
    producer_did = Column(String)
    network = Column(String)

class Producer(Base):
    __tablename__ = "producers"

    id = Column(Integer, primary_key=True, index=True)
    service_name = Column(String, unique=True, index=True)
    service_type = Column(String, unique=True, index=True)
    end_point = Column(String, unique=True, index=True)
    usage = Column(String) # TODO enum?
    status = Column(String)
    action = Column(String)
