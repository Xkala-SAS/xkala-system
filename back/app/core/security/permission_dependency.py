from fastapi import Depends, HTTPException

from sqlalchemy.orm import Session

from app.core.security.auth_dependency import (
    get_current_user
)

from app.infrastructure.database.dependencies import (
    get_db
)

from app.infrastructure.repositories.role_permission_repository import (
    RolePermissionRepository
)


def require_permission(permission_code: str):

    def permission_checker(
        current_user = Depends(get_current_user),
        db: Session = Depends(get_db)
    ):

        repository = (
            RolePermissionRepository(db)
        )

        has_permission = (
            repository.role_has_permission(
                current_user.role_id,
                permission_code
            )
        )

        if not has_permission:

            raise HTTPException(
                status_code=403,
                detail="Permiso denegado"
            )

        return current_user

    return permission_checker