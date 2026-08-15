from app.domain.user.entities.user import User

from app.domain.user.entities.user_document import (
    UserDocument
)

from app.core.security.password_hasher import (
    PasswordHasher
)

from app.domain.user.exceptions.user_validation_exceptions import (
    UserAlreadyExistsException,
    DocumentAlreadyExistsException
)

from app.domain.user.enums.onboarding_status import (
    OnboardingStatus
)


class CreateUserUseCase:

    def __init__(
        self,
        user_repository,
        user_document_repository
    ):

        self.user_repository = user_repository

        self.user_document_repository = (
            user_document_repository
        )

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
        document_type_id: str,
        role_id: str
    ):

        existing_user = (
            self.user_repository.get_by_email(email)
        )

        if existing_user:

            raise UserAlreadyExistsException()

        existing_document = (
            self.user_repository.get_by_document(
                numero_documento
            )
        )

        if existing_document:

            raise DocumentAlreadyExistsException()

        password_hash = PasswordHasher.hash(
            password
        )

        user = User(
            primer_nombre=primer_nombre,
            segundo_nombre=segundo_nombre,
            primer_apellido=primer_apellido,
            segundo_apellido=segundo_apellido,
            fecha_nacimiento=fecha_nacimiento,
            email=email,
            password_hash=password_hash,
            role_id=role_id,
            onboarding_status=OnboardingStatus.PENDING
        )

        saved_user = (
            self.user_repository.save(user)
        )

        user_document = UserDocument(
            user_id=saved_user.id,
            numero_documento=numero_documento,
            document_type_id=document_type_id
        )

        self.user_document_repository.save(
            user_document
        )

        return saved_user