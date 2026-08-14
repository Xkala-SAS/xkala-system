from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.interfaces.api.role.schemas import (
    CreateRoleRequest
)

from app.infrastructure.database.dependencies import (
    get_db
)

from app.infrastructure.repositories.role_repository_impl import (
    RoleRepositoryImpl
)

from app.application.role.use_cases.create_role import (
    CreateRoleUseCase
)

from app.core.security.permission_dependency import (
    require_permission
)

from app.core.responses.response_handler import (
    success_response
)

from app.core.exceptions.base_exception import (
    AppException
)

from app.infrastructure.repositories.permission_repository import (
    PermissionRepository
)


router = APIRouter(

    prefix="/roles",

    tags=["Roles"]
)


# ==========================================
# CREATE ROLE
# ==========================================

@router.post("/")
def create_role(

    request: CreateRoleRequest,

    current_user = Depends(
        require_permission(
            "manage_roles"
        )
    ),

    db: Session = Depends(get_db)
):

    try:

        repository = RoleRepositoryImpl(db)

        use_case = CreateRoleUseCase(
            repository
        )

        role = use_case.execute(

            nombre=request.nombre,

            descripcion=request.descripcion
        )

        return success_response(

            data={
                "role_id": role.id
            },

            message="Rol creado correctamente"
        )

    except ValueError as e:

        raise AppException(

            message=str(e),

            status_code=400,

            error_code="ROLE_ERROR"
        )


# ==========================================
# LIST ROLES
# ==========================================

@router.get("")
def list_roles(

    current_user = Depends(
        require_permission(
            "view_roles"
        )
    ),

    db: Session = Depends(get_db)
):

    repository = RoleRepositoryImpl(db)

    roles = repository.get_all()

    return success_response(

        data=roles,

        message="Roles obtenidos"
    )

# ==========================================
# ROLE DETAIL
# ==========================================

@router.get("/{role_id}")
def get_role_detail(

    role_id: str,

    current_user = Depends(
        require_permission(
            "view_roles"
        )
    ),

    db: Session = Depends(get_db)
):

    repository = RoleRepositoryImpl(db)

    role = repository.get_role_detail(
        role_id
    )

    return success_response(

        data=role,

        message="Rol obtenido correctamente"
    )