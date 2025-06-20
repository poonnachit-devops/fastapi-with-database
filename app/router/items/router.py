from fastapi import APIRouter

from app.databases import SessionDep
from app.router.items.dto import ItemDto
from app.router.items.model import Item
from app.router.items.services import (
    create_item_service,
    read_item_services,
    read_items_services,
    update_item_services,
)


router = APIRouter(prefix="/items", tags=["items"])


@router.post("/", response_model=Item)
def create_item(item: ItemDto, session: SessionDep):
    return create_item_service(item, session)


@router.get("/", response_model=list[Item])
def read_items(
    session: SessionDep,
    skip: int = 0,
    limit: int = 10,
):
    return read_items_services(session, skip, limit)


@router.get("/{item_id}", response_model=Item)
def read_item(item_id: int, session: SessionDep):
    return read_item_services(item_id, session)


@router.put("/{item_id}", response_model=Item)
def update_item(item_id: int, item: ItemDto, session: SessionDep):
    return update_item_services(item_id, item, session)


@router.delete("/{item_id}", response_model=Item)
def delete_item(item_id: int, session: SessionDep):
    return delete_item(item_id, session)
