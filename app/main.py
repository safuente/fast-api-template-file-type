from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from core.database import Base, engine
from core.logger import logger
from routers import item_router

# Initialize FastAPI application with metadata
app = FastAPI(
    title="FastAPI Template Starter",
    version="1.0",
    description="A project starter for FastAPI",
    docs_url="/",
)

# Create database tables
Base.metadata.create_all(bind=engine)
logger.info("Database tables created.")

# Include API routers
app.include_router(item_router, prefix="/items", tags=["Items"])
logger.info("API routers registered.")


@app.get("/redirect", include_in_schema=False)
def redirect_to_docs():
    """Redirect to the API documentation."""
    logger.info("Redirecting to /docs")
    return RedirectResponse(url="/docs")
