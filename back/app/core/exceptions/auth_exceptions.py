from app.core.exceptions.base_exception import AppException


class InvalidCredentialsException(
    AppException
):

    def __init__(self):

        super().__init__(
            message="Credenciales inválidas",

            status_code=401,

            error_code="INVALID_CREDENTIALS"
        )


class InactiveUserException(
    AppException
):

    def __init__(self):

        super().__init__(
            message="Usuario inactivo",

            status_code=403,

            error_code="INACTIVE_USER"
        )