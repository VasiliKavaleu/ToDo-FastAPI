from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker

import databases


SQLALCHEMY_DATABASE_URL = "postgresql://root:root@localhost:32700/todoapp"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

database = databases.Database(SQLALCHEMY_DATABASE_URL)
