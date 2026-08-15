from app.core.security.password_hasher import (
    PasswordHasher
)


class SavePersonalInfoUseCase:

    def __init__(
        self,
        user_repository
    ):
        self.user_repository = user_repository

    def execute(
        self,
        user_id: str,
        primer_nombre: str,
        segundo_nombre: str,
        primer_apellido: str,
        segundo_apellido: str,
        fecha_nacimiento,
        email: str,
        password: str
    ):

        password_hash = PasswordHasher.hash(
            password
        )

        return self.user_repository.update_personal_info(
            user_id=user_id,

            primer_nombre=primer_nombre,

            segundo_nombre=segundo_nombre,

            primer_apellido=primer_apellido,

            segundo_apellido=segundo_apellido,

            fecha_nacimiento=fecha_nacimiento,

            email=email,

            password_hash=password_hash
        )