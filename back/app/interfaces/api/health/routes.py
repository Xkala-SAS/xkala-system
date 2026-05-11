from fastapi import APIRouter
from sqlalchemy import text

from app.infrastructure.database.db import engine
from app.core.settings import settings

router = APIRouter()


@router.get("/health")
def health_check():

    database_status = "ok"

    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

    except Exception:
        database_status = "error"

    return {
        "app": settings.APP_NAME,
        "environment": settings.APP_ENV,
        "status": "running",
        "database": database_status
    }