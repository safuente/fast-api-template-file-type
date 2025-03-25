from pydantic import BaseModel
from typing import Optional


class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class ItemRead(ItemBase):
    id: int

    class Config:
        orm_mode = True
