import os
from typing import Annotated

from fastapi import Depends
from sqlmodel import SQLModel, Session, create_engine


DATABASE = {
    "HOST": os.getenv("DATABASE_HOST", "localhost"),
    "USERNAME": os.getenv("DATABASE_USER", "root"),
    "PASSWORD": os.getenv("DATABASE_PASSWORD", "rootpassword"),
    "DATABASE": os.getenv("DATABASE_NAME", "items"),
}

engine = create_engine(
    f"mysql+mysqlconnector://{DATABASE['USERNAME']}:{DATABASE['PASSWORD']}@{DATABASE['HOST']}/{DATABASE['DATABASE']}"
)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
