from fastapi import Depends, HTTPException

from app.core.security.auth_dependency import get_current_user


def require_role(required_role_id: str):

    def role_checker(
        current_user = Depends(get_current_user)
    ):

        if current_user.role_id != required_role_id:

            raise HTTPException(
                status_code=403,
                detail="No tienes permisos"
            )

        return current_user

    return role_checker