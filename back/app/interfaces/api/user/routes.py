from fastapi import (
    APIRouter,
    Depends,
    UploadFile,
    File,
    Query,
    Request
)

from typing import Optional

from app.core.responses.response_handler import (
    success_response
)

from app.interfaces.api.user.schemas import (
    LoginRequest
)

from app.interfaces.schemas.create_user_schema import (
    CreateUserRequest
)

from app.interfaces.schemas.user_profile_schema import (
    UserProfileResponse
)

from app.interfaces.schemas.user_list_schema import (
    UserListResponseSchema
)

from app.core.security.auth_dependency import (
    get_current_user
)

from app.core.security.role_dependency import (
    require_role
)

from app.core.security.permission_dependency import (
    require_permission
)

from app.application.user.use_cases.update_user import (
    UpdateUserUseCase
)

from app.core.dependencies.user_dependencies import (
    get_update_user_use_case
)

from app.application.user.use_cases.create_user import (
    CreateUserUseCase
)

from app.application.user.use_cases.login_user import (
    LoginUserUseCase
)

from app.application.services.user_profile_service import (
    UserProfileService
)

from app.application.services.upload_profile_photo_service import (
    UploadProfilePhotoService
)

from app.application.services.list_user_service import (
    ListUsersService
)

from app.core.dependencies.user_dependencies import (

    get_user_repository,

    get_login_use_case,

    get_profile_service,

    get_upload_profile_service,

    get_list_users_service,

    get_user_document_repository
)


router = APIRouter(

    prefix="/users",

    tags=["Users"]
)


# ==========================================
# CREATE USER
# ==========================================

@router.post("/")
def create_user(

    request: CreateUserRequest,

    repository = Depends(
        get_user_repository
    ),

    user_document_repository = Depends(
        get_user_document_repository
    )
):

    use_case = CreateUserUseCase(
        user_repository = repository,
        user_document_repository = user_document_repository
    )

    user = use_case.execute(

        primer_nombre=request.primer_nombre,

        segundo_nombre=request.segundo_nombre,

        primer_apellido=request.primer_apellido,

        segundo_apellido=request.segundo_apellido,

        fecha_nacimiento=request.fecha_nacimiento,

        email=request.email,

        password=request.password,

        numero_documento=request.numero_documento,

        document_type_id=request.document_type_id,

        role_id=request.role_id
    )

    return success_response(

        data={

            "user_id": user.id
        },

        message=
            "Usuario creado correctamente"
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
# PROFILE BASIC
# ==========================================

@router.get("/me")
def profile(

    current_user = Depends(
        get_current_user
    )
):

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

            "role_id":
                current_user.role_id
        },

        message="Perfil obtenido"
    )


# ==========================================
# ADMIN ONLY
# ==========================================

@router.get("/admin-only")
def admin_only_route(

    current_user = Depends(
        require_role("admin")
    )
):

    return success_response(

        data={

            "user":
                current_user.primer_nombre
        },

        message=
            "Bienvenido administrador"
    )


# ==========================================
# SECURE DATA
# ==========================================

@router.get("/secure-data")
def secure_data(

    current_user = Depends(

        require_permission(
            "create_user"
        )
    )
):

    return success_response(

        data={

            "user":
                current_user.primer_nombre
        },

        message=
            "Tienes permiso create_user"
    )


# ==========================================
# PROFILE FULL
# ==========================================

@router.get(
    "/profile",
    response_model=UserProfileResponse
)
def get_profile(

    current_user = Depends(
        get_current_user
    ),

    service: UserProfileService = Depends(
        get_profile_service
    )
):

    return service.execute(
        current_user.id
    )


# ==========================================
# UPLOAD PROFILE PHOTO
# ==========================================

@router.post("/upload/profile-photo")
def upload_profile_photo(

    file: UploadFile = File(...),

    current_user = Depends(
        get_current_user
    ),

    service: UploadProfilePhotoService = Depends(
        get_upload_profile_service
    )
):

    result = service.execute(
        file,
        current_user
    )

    return success_response(

        data=result,

        message=
            "Archivo subido correctamente"
    )


# ==========================================
# LIST USERS
# ==========================================

@router.get(
    "/",
    response_model=UserListResponseSchema
)
def list_users(

    page: int = Query(
        1,
        ge=1
    ),

    limit: int = Query(
        10,
        ge=1,
        le=100
    ),

    search: Optional[str] = None,

    estado: Optional[bool] = None,

    order_by: str = "created_at",

    direction: str = "desc",

    service: ListUsersService = Depends(
        get_list_users_service
    )
):

    result = service.execute(

        page,

        limit,

        search,

        estado,

        order_by,

        direction
    )

    return success_response(

        data=result["items"],

        message="Usuarios obtenidos",

        pagination=result["pagination"]
    )

@router.put("/{user_id}")
def update_user(

    user_id: str,

    request: CreateUserRequest,

    http_request: Request,

    current_user = Depends(
        get_current_user
    ),

    use_case: UpdateUserUseCase = Depends(
        get_update_user_use_case
    )
):

    result = use_case.execute(

        user_id=user_id,

        primer_nombre=request.primer_nombre,

        segundo_nombre=request.segundo_nombre,

        primer_apellido=request.primer_apellido,

        segundo_apellido=request.segundo_apellido,

        email=request.email,

        estado=True,

        role_id=request.role_id,

        current_user_id=current_user.id,

        ip_address=http_request.client.host
    )

    return success_response(

        data={

            "user_id":
                result.id
        },

        message=
            "Usuario actualizado correctamente"
    )