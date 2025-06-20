from fastapi import HTTPException
from sqlmodel import select
from app.databases import SessionDep
from app.router.items.dto import ItemDto
from app.router.items.model import Item


def create_item_service(item: ItemDto, session: SessionDep):
    new_item = Item(name=item.name, description=item.description, price=item.price)
    session.add(new_item)
    session.commit()
    session.refresh(new_item)
    return new_item


def read_items_services(
    session: SessionDep,
    skip: int = 0,
    limit: int = 10,
):
    query = select(Item).offset(skip).limit(limit)
    items = session.exec(query).all()
    return items


def read_item_services(item_id: int, session: SessionDep):
    statement = select(Item).where(Item.id == item_id)
    item = session.exec(statement).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


def update_item_services(item_id: int, item: ItemDto, session: SessionDep):
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


def delete_item_services(item_id: int, session: SessionDep):
    statement = select(Item).where(Item.id == item_id)
    db_item = session.exec(statement).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")

    session.delete(db_item)
    session.commit()

    return db_item
