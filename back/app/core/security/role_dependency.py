from fastapi import (
    Depends
)

from app.core.security.auth_dependency import (
    get_current_user
)

from app.core.exceptions.base_exception import (
    AppException
)


def require_role(
    role_name: str
):

    def role_checker(

        current_user = Depends(
            get_current_user
        )
    ):

        user_role = (
            current_user.role.nombre
            if current_user.role
            else None
        )

        if not user_role:

            raise AppException(

                message="El usuario no tiene rol asignado",

                status_code=403,

                error_code="ROLE_NOT_ASSIGNED"
            )

        if user_role.lower() != role_name.lower():

            raise AppException(

                message="No tienes permisos para acceder",

                status_code=403,

                error_code="INSUFFICIENT_ROLE"
            )

        return current_user

    return role_checker