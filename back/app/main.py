import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from sqlalchemy import text

from app.core.middleware.request_logger import (
    RequestLoggingMiddleware
)

from app.core.settings import settings

from app.core.exceptions.handlers import (
    register_exception_handlers
)

from app.infrastructure.database.db import engine

from app.interfaces.api.health.routes import (
    router as health_router
)

from app.interfaces.api.user.routes import (
    router as user_router
)

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

# ==========================================
# CREATE UPLOADS DIRECTORY
# ==========================================

os.makedirs(
    "uploads",
    exist_ok=True
)

# ==========================================
# FASTAPI APP
# ==========================================

app = FastAPI(
    title="Xkala System API"
)

# ==========================================
# EXCEPTION HANDLERS
# ==========================================

register_exception_handlers(app)

# ==========================================
# MIDDLEWARES
# ==========================================

app.add_middleware(
    CORSMiddleware,

    allow_origins=[settings.CORS_ORIGINS],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)

app.add_middleware(
    RequestLoggingMiddleware
)

# ==========================================
# STATIC FILES
# ==========================================

app.mount(
    "/uploads",

    StaticFiles(directory="uploads"),

    name="uploads"
)

# ==========================================
# ROUTERS
# ==========================================

app.include_router(health_router)

app.include_router(user_router)

app.include_router(role_router)

app.include_router(permission_router)

app.include_router(document_type_router)

app.include_router(city_router)

app.include_router(hr_router)

# ==========================================
# ROOT
# ==========================================

@app.get("/")
def root():

    return {
        "message": "Xkala System API"
    }

# ==========================================
# HEALTH CHECK
# ==========================================

@app.get("/health")
def health_check():

    database_status = "ok"

    try:

        with engine.connect() as connection:

            connection.execute(
                text("SELECT 1")
            )

    except Exception:

        database_status = "error"

    return {

        "app": settings.APP_NAME,

        "environment": settings.APP_ENV,

        "status": "running",

        "database": database_status
    }