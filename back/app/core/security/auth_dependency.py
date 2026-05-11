from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from sqlalchemy.orm import Session

from app.core.security.jwt_handler import JWTHandler

from app.infrastructure.database.dependencies import get_db
from app.infrastructure.repositories.user_repository_impl import UserRepositoryImpl


security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):

    token = credentials.credentials

    payload = JWTHandler.decode_token(token)

    if not payload:
        raise HTTPException(
            status_code=401,
            detail="Token inválido"
        )

    user_id = payload.get("sub")

    repository = UserRepositoryImpl(db)

    user = repository.get_by_id(user_id)

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Usuario no encontrado"
        )

    return user