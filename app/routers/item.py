from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas.item import ItemCreate, ItemRead
from services.item_service import ItemService

router = APIRouter(prefix="/items", tags=["items"])


@router.post("/", response_model=ItemRead)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    service = ItemService(db)
    return service.create_item(item)


@router.get("/{item_id}", response_model=ItemRead)
def read_item(item_id: int, db: Session = Depends(get_db)):
    service = ItemService(db)
    return service.get_item(item_id)
