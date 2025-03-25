from typing import Type, TypeVar, List, Dict
from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy.sql import text
from pydantic import BaseModel
from core.logger import logger

ModelType = TypeVar("ModelType")


class BaseService:
    def __init__(self, db: Session, model: Type[ModelType]) -> None:
        """Initialize the service with a database session and a model."""
        self.db = db
        self.model = model
        logger.info(f"Service initialized for model {self.model.__name__}")

    def create_item(self, item_data: BaseModel) -> ModelType:
        """Create a new item in the database."""
        item = self.model(**item_data.dict())
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        logger.info(
            f"Created {self.model.__name__} with ID {getattr(item, f'{self.model.__name__.lower()}_id')}"
        )
        return item

    def list_items(self, order_by: str | None = None) -> List[ModelType]:
        """Retrieve a list of all items, optionally ordered by a field."""
        order_by = (
            text(f"{self.model.__name__.lower()}_id")
            if order_by is None
            else text(order_by)
        )
        items = self.db.query(self.model).order_by(order_by).all()
        logger.info(f"Retrieved {len(items)} {self.model.__name__}(s)")
        return items

    def get_item(self, item_id: int) -> ModelType:
        """Retrieve a single item by its ID."""
        primary_key_field = getattr(self.model, f"{self.model.__name__.lower()}_id")
        item = self.db.query(self.model).filter(primary_key_field == item_id).first()
        if not item:
            raise HTTPException(
                status_code=404,
                detail=f"{self.model.__name__} with ID {item_id} not found",
            )
        logger.info(f"Retrieved {self.model.__name__} with ID {item_id}")
        return item

    def update_item(self, item_id: int, item_data: BaseModel) -> ModelType:
        """Update an existing item with new data."""
        item = (
            self.db.query(self.model)
            .filter(getattr(self.model, f"{self.model.__name__.lower()}_id") == item_id)
            .first()
        )
        if not item:
            logger.warning(f"{self.model.__name__} with ID {item_id} not found")
            raise HTTPException(
                status_code=404,
                detail=f"{self.model.__name__} with ID {item_id} not found",
            )

        for key, value in item_data.dict(exclude_unset=True).items():
            setattr(item, key, value)

        self.db.commit()
        self.db.refresh(item)
        return item

    def delete_item(self, item_id: int) -> Dict[str, str]:
        """Delete an item from the database."""
        item = (
            self.db.query(self.model)
            .filter(getattr(self.model, f"{self.model.__name__.lower()}_id") == item_id)
            .first()
        )
        if not item:
            logger.warning(
                f"{self.model.__name__} with ID {item_id} not found for deletion"
            )
            raise HTTPException(
                status_code=404,
                detail=f"{self.model.__name__} with ID {item_id} not found",
            )

        self.db.delete(item)
        self.db.commit()
        logger.info(f"Deleted {self.model.__name__} with ID {item_id}")
        return {
            "message": f"{self.model.__name__} with ID {item_id} deleted successfully"
        }
