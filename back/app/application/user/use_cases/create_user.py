from app.domain.user.entities.user import User
from app.domain.user.repositories.user_repository import UserRepository
from app.core.security.password_hasher import PasswordHasher
from app.domain.user.exceptions.user_validation_exceptions import (
    UserAlreadyExistsException
)


class CreateUserUseCase:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(
        self,
        primer_nombre: str,
        segundo_nombre: str,
        primer_apellido: str,
        segundo_apellido: str,
        fecha_nacimiento,
        email: str,
        password: str,
        numero_documento: str,
        role_id: str
    ) -> User:
        
       

        # 🔍 1. Validar si ya existe por documento (LOGIN)
        existing_user = self.user_repository.get_by_document(numero_documento)

        if existing_user:
            raise ValueError("El usuario ya existe con ese documento")

        # 🔍 2. Validar email único (opcional pero recomendado)
        existing_email = self.user_repository.get_by_email(email)

        if existing_email:
            raise UserAlreadyExistsException()
        
        # hashear contraseña
        hashed_password = PasswordHasher.hash(password)

        # 🧠 3. Crear entidad (dominio)
        user = User(
            primer_nombre=primer_nombre,
            segundo_nombre=segundo_nombre,
            primer_apellido=primer_apellido,
            segundo_apellido=segundo_apellido,
            fecha_nacimiento=fecha_nacimiento,
            email=email,
            password_hash=hashed_password,
            numero_documento=numero_documento,
            role_id=role_id
        )

        # 💾 4. Guardar
        return self.user_repository.save(user)