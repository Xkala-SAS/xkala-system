from datetime import datetime

from pydantic import (
    BaseModel,
    EmailStr,
    field_validator
)


class LoginRequest(BaseModel):

    numero_documento: str
    password: str

    @field_validator(
        "numero_documento",
        "password"
    )
    @classmethod
    def validate_not_empty(
        cls,
        value: str
    ):

        if not value or not value.strip():
            raise ValueError(
                "Este campo es obligatorio"
            )

        return value.strip()


class CreateUserRequest(BaseModel):

    primer_nombre: str
    segundo_nombre: str | None = None

    primer_apellido: str
    segundo_apellido: str | None = None

    fecha_nacimiento: datetime

    email: EmailStr

    password: str

    numero_documento: str

    document_type_id: str

    role_id: str

    @field_validator(
        "primer_nombre",
        "primer_apellido",
        "password",
        "numero_documento",
        "document_type_id",
        "role_id"
    )
    @classmethod
    def validate_not_empty(
        cls,
        value: str
    ):

        if not value or not value.strip():
            raise ValueError(
                "Este campo es obligatorio"
            )

        return value.strip()