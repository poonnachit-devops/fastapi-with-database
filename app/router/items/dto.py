from pydantic import BaseModel


class ItemDto(BaseModel):
    name: str
    description: str | None = None
    price: float
