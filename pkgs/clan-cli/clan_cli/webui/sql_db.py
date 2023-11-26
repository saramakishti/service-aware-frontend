from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

URL = "sqlite:///./sql_app.db"

engine = create_engine(
    URL, connect_args={"check_same_thread":False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency to start a clean thread of the db
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
