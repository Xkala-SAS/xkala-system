from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.infrastructure.database.dependencies import (
    get_db
)

from app.infrastructure.repositories.permission_repository import (
    PermissionRepository
)

from app.core.security.permission_dependency import (
    require_permission
)

from app.core.responses.response_handler import (
    success_response
)


router = APIRouter(

    prefix="/permissions",

    tags=["Permissions"]
)


# ==========================================
# LIST PERMISSIONS
# ==========================================

@router.get("/")
def list_permissions(

    current_user = Depends(
        require_permission(
            "view_permissions"
        )
    ),

    db: Session = Depends(get_db)
):

    repository = PermissionRepository(db)

    permissions = repository.get_all()

    return success_response(

        data=permissions,

        message="Permisos obtenidos"
    )