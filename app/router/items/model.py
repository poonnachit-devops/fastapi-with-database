from sqlmodel import Field, SQLModel


class Item(SQLModel, table=True):
    item_id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str | None = None
    price: float
