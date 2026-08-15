from pydantic import BaseModel, field_validator


class CreatePreRegisteredUserRequest(BaseModel):

    numero_documento: str

    document_type_id: str

    role_id: str

    @field_validator(
        "numero_documento",
        "document_type_id",
        "role_id"
    )
    @classmethod
    def validate_not_empty(cls, value: str):

        if not value or not value.strip():
            raise ValueError(
                "Este campo es obligatorio"
            )

        return value.strip()