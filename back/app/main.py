import os
from fastapi import FastAPI

from app.interfaces.api.user.routes import router as user_router
from app.interfaces.api.role.routes import (
    router as role_router
)
from app.interfaces.api.permission.routes import (
    router as permission_router
)
from app.interfaces.api.document_type.routes import (
    router as document_type_router
)
from app.interfaces.api.city.routes import (
    router as city_router
)
from app.interfaces.api.hr.routes import (
    router as hr_router
)
from fastapi.staticfiles import StaticFiles
from app.core.exceptions.base_exception import (
    AppException
)

from app.core.handlers.global_exception_handler import (
    app_exception_handler
)
from app.core.middleware.request_logger import (
    RequestLoggingMiddleware
)
from fastapi.middleware.cors import CORSMiddleware
from app.core.settings import settings
from app.core.exceptions.handlers import (
    register_exception_handlers
)
from app.interfaces.api.health.routes import router as health_router
from app.infrastructure.database.db import engine
from sqlalchemy import text

os.makedirs("uploads", exist_ok=True)

app = FastAPI(
    title="Xkala System API"
)
app.include_router(health_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_exception_handlers(app)
app.add_middleware(
    RequestLoggingMiddleware
)
app.add_exception_handler(
    AppException,
    app_exception_handler
)
app.mount(
    "/uploads",
    StaticFiles(directory="uploads"),
    name="uploads"
)

app.include_router(user_router)
app.include_router(role_router)
app.include_router(permission_router)
app.include_router(document_type_router)
app.include_router(city_router)
app.include_router(hr_router)


@app.get("/")
def root():
    return {"message": "CAMBIO"}

@app.get("/health")
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