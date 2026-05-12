from app.core.security.password_hasher import (
    PasswordHasher
)

from app.core.security.jwt_handler import (
    JWTHandler
)

from app.core.logging.logger import (
    logger
)

from app.core.exceptions.auth_exceptions import (
    InvalidCredentialsException,
    InactiveUserException
)


class LoginUserUseCase:

    def __init__(
        self,
        repository,
        audit_service
    ):

        self.repository = repository

        self.audit_service = audit_service

    def execute(

        self,

        numero_documento: str,

        password: str
    ):

        logger.info(
            f"Intento login documento: "
            f"{numero_documento}"
        )

        user = self.repository.get_by_document(
            numero_documento
        )

        if not user:

            logger.warning(
                f"Usuario no encontrado: "
                f"{numero_documento}"
            )

            raise InvalidCredentialsException()

        valid_password = (
            PasswordHasher.verify(
                password,
                user.password_hash
            )
        )

        if not valid_password:

            logger.warning(
                f"Password incorrecto: "
                f"{numero_documento}"
            )

            raise InvalidCredentialsException()

        if not user.estado:

            raise InactiveUserException()

        # ======================================
        # AUDITORÍA SEGURA
        # ======================================

        try:

            self.audit_service.execute(

                user_id=user.id,

                action="LOGIN",

                resource="AUTH",

                method="POST",

                endpoint="/users/login",

                ip_address="127.0.0.1",

                status_code=200,

                description="Inicio de sesión exitoso",

                extra_data={

                    "numero_documento":
                        numero_documento
                }
            )

        except Exception as e:

            logger.error(
                f"Error registrando auditoría: {e}"
            )

        logger.info(
            f"Login exitoso usuario: "
            f"{user.id}"
        )

        token = JWTHandler.create_access_token({

            "sub": user.id,

            "role_id": user.role_id
        })

        return {

            "access_token": token,

            "token_type": "bearer"
        }