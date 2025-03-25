import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from typing import Generator

# Define the database file path and connection URL
DB_PATH: str = os.path.join("database.sqlite")
SQLALCHEMY_DATABASE_URL: str = f"sqlite:///{DB_PATH}"

# Create the database engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Configure the session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define the base class for ORM models
Base = declarative_base()


def get_db() -> Generator[Session, None, None]:
    """Dependency that provides a database session and ensures proper cleanup."""
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
