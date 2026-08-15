from app.core.security.password_hasher import (
    PasswordHasher
)


class ChangePasswordService:

    def __init__(
        self,
        repository
    ):
        self.repository = repository

    def execute(
        self,
        user_id: str,
        current_password: str,
        new_password: str
    ):

        user = self.repository.get_by_id(
            user_id
        )

        if not user:
            raise Exception(
                "Usuario no encontrado"
            )

        is_valid = (
            PasswordHasher.verify(
                current_password,
                user.password_hash
            )
        )

        if not is_valid:
            raise Exception(
                "La contraseña actual es incorrecta"
            )

        hashed_password = (
            PasswordHasher.hash(
                new_password
            )
        )

        self.repository.update_password(
            user_id,
            hashed_password
        )

        return True