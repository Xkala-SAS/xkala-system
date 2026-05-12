from app.core.exceptions.base_exception import (
    AppException
)


class InvalidEmailException(AppException):

    def __init__(self):

        super().__init__(
            message="El email proporcionado no es válido",
            status_code=400,
            error_code="INVALID_EMAIL"
        )


class MissingFirstNameException(AppException):

    def __init__(self):

        super().__init__(
            message="El primer nombre es obligatorio",
            status_code=400,
            error_code="MISSING_FIRST_NAME"
        )


class MissingLastNameException(AppException):

    def __init__(self):

        super().__init__(
            message="El primer apellido es obligatorio",
            status_code=400,
            error_code="MISSING_LAST_NAME"
        )


class MissingDocumentException(AppException):

    def __init__(self):

        super().__init__(
            message="El número de documento es obligatorio",
            status_code=400,
            error_code="MISSING_DOCUMENT"
        )


class MissingPasswordException(AppException):

    def __init__(self):

        super().__init__(
            message="La contraseña es obligatoria",
            status_code=400,
            error_code="MISSING_PASSWORD"
        )


class MissingRoleException(AppException):

    def __init__(self):

        super().__init__(
            message="El rol es obligatorio",
            status_code=400,
            error_code="MISSING_ROLE"
        )


class UserAlreadyExistsException(AppException):

    def __init__(self):

        super().__init__(
            message="El email ya está registrado",
            status_code=409,
            error_code="USER_ALREADY_EXISTS"
        )