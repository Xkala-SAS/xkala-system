from fastapi import (
    Depends,
    Request
)

from fastapi.security import (
    HTTPBearer,
    HTTPAuthorizationCredentials
)

from sqlalchemy.orm import Session

from app.core.security.jwt_handler import (
    JWTHandler
)

from app.infrastructure.database.dependencies import (
    get_db
)

from app.infrastructure.repositories.user_repository_impl import (
    UserRepositoryImpl
)

from app.core.exceptions.base_exception import (
    AppException
)

security = HTTPBearer()


def get_current_user(

    request: Request,

    credentials: HTTPAuthorizationCredentials = Depends(
        security
    ),

    db: Session = Depends(get_db)
):

    token = credentials.credentials

    payload = JWTHandler.decode_token(
        token
    )

    # ======================================
    # VALIDATE TOKEN TYPE
    # ======================================

    token_type = payload.get(
        "token_type"
    )

    if token_type != "access":

        raise AppException(

            message="Token inválido",

            status_code=401,

            error_code="INVALID_TOKEN_TYPE"
        )

    user_id = payload.get("sub")

    if not user_id:

        raise AppException(

            message="Token inválido",

            status_code=401,

            error_code="INVALID_TOKEN"
        )

    repository = UserRepositoryImpl(db)

    user = repository.get_by_id(
        user_id
    )

    if not user:

        raise AppException(

            message="Usuario no encontrado",

            status_code=401,

            error_code="USER_NOT_FOUND"
        )

    # ======================================
    # VALIDATE ACTIVE USER
    # ======================================

    if not user.estado:

        raise AppException(

            message="Usuario inactivo",

            status_code=403,

            error_code="USER_INACTIVE"
        )

    # ======================================
    # SAVE USER IN REQUEST
    # ======================================

    request.state.user = user

    return user