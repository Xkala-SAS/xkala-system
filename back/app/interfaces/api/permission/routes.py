from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.infrastructure.database.dependencies import get_db

from app.infrastructure.database.db import SessionLocal

from app.infrastructure.database.models.permission_model import PermissionModel

from app.infrastructure.repositories.role_permission_repository import (
    RolePermissionRepository
)


router = APIRouter(
    prefix="/permissions",
    tags=["Permissions"]
)


@router.post("/seed")
def seed_permissions():

    db: Session = SessionLocal()

    permissions = [
        "create_user",
        "edit_user",
        "delete_user",
        "view_users",
        "create_quote",
        "approve_quote",
        "view_reports"
    ]

    for code in permissions:

        exists = (
            db.query(PermissionModel)
            .filter(PermissionModel.codigo == code)
            .first()
        )

        if not exists:

            permission = PermissionModel(
                codigo=code,
                descripcion=code
            )

            db.add(permission)

    db.commit()

    return {
        "message": "Permisos creados"
    }


@router.post("/assign")
def assign_permission(
    role_id: str,
    permission_code: str,
    db: Session = Depends(get_db)
):

    permission = (
        db.query(PermissionModel)
        .filter(
            PermissionModel.codigo == permission_code
        )
        .first()
    )

    if not permission:
        return {
            "error": "Permiso no encontrado"
        }

    repository = RolePermissionRepository(db)

    repository.assign_permission(
        role_id,
        permission.id
    )

    return {
        "message": "Permiso asignado"
    }