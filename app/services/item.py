from models.item import Item
from services.base import BaseService
from sqlalchemy.orm import Session


class ItemService(BaseService):
    def __init__(self, db: Session):
        super().__init__(db=db, model=Item)