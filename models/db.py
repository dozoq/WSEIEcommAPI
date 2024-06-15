from sqlalchemy import create_engine, Column, Integer, String
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel

import config

DATABASE_URL = config.Settings.DATABASE_URL
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = sqlalchemy.orm.declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




