from app.core.exceptions.base_exception import (
    AppException
)


class UserNotFoundException(AppException):

    def __init__(self):

        super().__init__(
            message="Usuario no encontrado",
            status_code=404
        )


class InvalidCredentialsException(AppException):

    def __init__(self):

        super().__init__(
            message="Credenciales inválidas",
            status_code=401
        )