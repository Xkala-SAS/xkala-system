from datetime import datetime
from uuid import uuid4
from app.domain.user.exceptions.user_validation_exceptions import (
    InvalidEmailException,
    MissingFirstNameException,
    MissingLastNameException,
    MissingDocumentException,
    MissingPasswordException,
    MissingRoleException
)

class User:
    def __init__(
    self,
    primer_nombre: str,
    segundo_nombre: str,
    primer_apellido: str,
    segundo_apellido: str,
    fecha_nacimiento: datetime,
    email: str,
    password_hash: str,
    numero_documento: str,
    role_id: str,
    id: str = None,
    estado: bool = True,
    created_at: datetime = None,
):
        self.id = id or str(uuid4())
        self.primer_nombre = primer_nombre
        self.segundo_nombre = segundo_nombre
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.email = email
        self.password_hash = password_hash
        self.numero_documento = numero_documento
        self.role_id = role_id
        self.estado = estado
        self.created_at = created_at or datetime.utcnow()

        self._validate()

    def _validate(self):
        if not self.primer_nombre:
            raise MissingFirstNameException()

        if not self.primer_apellido:
            raise MissingLastNameException()

        if "@" not in self.email:
            raise InvalidEmailException()

        if not self.numero_documento:
            raise MissingDocumentException()

        if not self.password_hash:
            raise MissingPasswordException()

        if not self.role_id:
            raise MissingRoleException()

    def is_active(self) -> bool:
        return self.estado

    def change_status(self, estado: bool):
        self.estado = estado

    def check_password(self, password_hash: str) -> bool:
        return self.password_hash == password_hash