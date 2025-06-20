from contextlib import asynccontextmanager
import os
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from sqlmodel import Field, Session, SQLModel, create_engine, select


class Item(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str | None = None
    price: float


class ItemDto(BaseModel):
    name: str
    description: str | None = None
    price: float


print("Creating database tables...")

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


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield
    # Cleanup if needed
    print("Shutting down application...")


app = FastAPI(lifespan=lifespan)


@app.post("/items/", response_model=Item, tags=["items"])
def create_item(item: ItemDto, session: SessionDep):
    new_item = Item(name=item.name, description=item.description, price=item.price)
    session.add(new_item)
    session.commit()
    session.refresh(new_item)
    return new_item


@app.get("/items/", response_model=list[Item], tags=["items"])
def read_items(
    session: SessionDep,
    skip: int = 0,
    limit: int = 10,
):
    query = select(Item).offset(skip).limit(limit)
    items = session.exec(query).all()
    return items


@app.get("/items/{item_id}", response_model=Item, tags=["items"])
def read_item(item_id: int, session: SessionDep):
    statement = select(Item).where(Item.id == item_id)
    item = session.exec(statement).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.put("/items/{item_id}", response_model=Item, tags=["items"])
def update_item(item_id: int, item: ItemDto, session: SessionDep):
    statement = select(Item).where(Item.id == item_id)
    db_item = session.exec(statement).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")

    db_item.name = item.name
    db_item.description = item.description
    db_item.price = item.price

    session.add(db_item)
    session.commit()
    session.refresh(db_item)

    return db_item


@app.delete("/items/{item_id}", response_model=Item, tags=["items"])
def delete_item(item_id: int, session: SessionDep):
    statement = select(Item).where(Item.id == item_id)
    db_item = session.exec(statement).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")

    session.delete(db_item)
    session.commit()

    return db_item


@app.get("/", tags=["root"])
def read_root():
    return {"message": "Welcome to the FastAPI application with MySQL!"}
