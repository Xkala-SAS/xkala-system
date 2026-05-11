from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.interfaces.api.role.schemas import CreateRoleRequest

from app.infrastructure.database.dependencies import get_db

from app.infrastructure.repositories.role_repository_impl import RoleRepositoryImpl

from app.application.role.use_cases.create_role import CreateRoleUseCase


router = APIRouter(
    prefix="/roles",
    tags=["Roles"]
)


@router.post("/")
def create_role(
    request: CreateRoleRequest,
    db: Session = Depends(get_db)
):

    try:

        repository = RoleRepositoryImpl(db)

        use_case = CreateRoleUseCase(repository)

        role = use_case.execute(
            nombre=request.nombre,
            descripcion=request.descripcion
        )

        return {
            "message": "Rol creado correctamente",
            "role_id": role.id
        }

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )