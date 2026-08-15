from datetime import datetime

from app.domain.user.entities.user import User
from app.domain.user.entities.user_document import UserDocument

from app.core.security.password_hasher import PasswordHasher

from app.domain.user.exceptions.user_validation_exceptions import (
    UserAlreadyExistsException,
    DocumentAlreadyExistsException
)

from app.domain.user.enums.onboarding_status import (
    OnboardingStatus
)


class CreatePreRegisteredUserUseCase:

    def __init__(
        self,
        user_repository,
        user_document_repository
    ):
        self.user_repository = user_repository

        self.user_document_repository = user_document_repository

    def execute(

        self,

        numero_documento: str,

        document_type_id: str,

        role_id: str

    ):

        existing_document = (
            self.user_repository.get_by_document(
                numero_documento
            )
        )

        if existing_document:
            raise DocumentAlreadyExistsException()

        password_hash = PasswordHasher.hash(
            numero_documento
        )

        email = (
            f"{numero_documento}@pending.xkala.local"
        )

        existing_email = (
            self.user_repository.get_by_email(
                email
            )
        )

        if existing_email:
            raise UserAlreadyExistsException()

        user = User(

            primer_nombre="PENDIENTE",

            segundo_nombre="",

            primer_apellido="PENDIENTE",

            segundo_apellido="",

            fecha_nacimiento=datetime(
                1900,
                1,
                1
            ),

            email=email,

            password_hash=password_hash,

            role_id=role_id,

            onboarding_status=OnboardingStatus.PENDING
        )

        saved_user = (
            self.user_repository.save(user)
        )

        document = UserDocument(

            user_id=saved_user.id,

            numero_documento=numero_documento,

            document_type_id=document_type_id
        )

        self.user_document_repository.save(
            document
        )

        return saved_user