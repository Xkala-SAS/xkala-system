from fastapi import (
    APIRouter,
    Depends,
    Request
)

from sqlalchemy.orm import Session

from app.interfaces.api.auth.schemas import (
    LoginRequest,
    RefreshTokenRequest
)

from app.core.responses.response_handler import (
    success_response
)

from app.core.security.auth_dependency import (
    get_current_user
)

from app.core.security.jwt_handler import (
    JWTHandler
)

from app.application.user.use_cases.login_user import (
    LoginUserUseCase
)

from app.core.dependencies.user_dependencies import (
    get_login_use_case
)

from app.infrastructure.database.dependencies import (
    get_db
)

from app.infrastructure.repositories.permission_repository import (
    PermissionRepository
)


router = APIRouter(

    prefix="/auth",

    tags=["Auth"]
)


# ==========================================
# LOGIN
# ==========================================

@router.post("/login")
def login(

    request: LoginRequest,

    use_case: LoginUserUseCase = Depends(
        get_login_use_case
    )
):

    result = use_case.execute(

        numero_documento=
            request.numero_documento,

        password=
            request.password
    )

    return success_response(

        data=result,

        message="Login exitoso"
    )


# ==========================================
# ME
# ==========================================

@router.get("/me")
def me(

    current_user = Depends(
        get_current_user
    ),

    db: Session = Depends(get_db)
):

    permission_repository = (
        PermissionRepository(db)
    )

    permissions = (

        permission_repository
        .get_permissions_by_role_id(
            current_user.role_id
        )
    )

    return success_response(

        data={

            "id":
                current_user.id,

            "primer_nombre":
                current_user.primer_nombre,

            "primer_apellido":
                current_user.primer_apellido,

            "email":
                current_user.email,

            "estado":
                current_user.estado,

            "role": {

                "id":
                    current_user.role.id,

                "nombre":
                    current_user.role.nombre
            },

            "permissions":
                permissions
        },

        message="Perfil obtenido"
    )


# ==========================================
# LOGOUT
# ==========================================

@router.post("/logout")
def logout(

    request: Request,

    current_user = Depends(
        get_current_user
    )
):

    return success_response(

        data={

            "user_id":
                current_user.id
        },

        message="Sesión cerrada correctamente"
    )


# ==========================================
# REFRESH TOKEN
# ==========================================

@router.post("/refresh")
def refresh_token(

    request: RefreshTokenRequest
):

    payload = JWTHandler.decode_token(

        request.refresh_token
    )

    JWTHandler.verify_token_type(

        payload,

        "refresh"
    )

    new_access_token = (
        JWTHandler.create_access_token({

            "sub":
                payload.get("sub"),

            "role_id":
                payload.get("role_id")
        })
    )

    return success_response(

        data={

            "access_token":
                new_access_token,

            "token_type":
                "bearer"
        },

        message="Token refrescado correctamente"
    )