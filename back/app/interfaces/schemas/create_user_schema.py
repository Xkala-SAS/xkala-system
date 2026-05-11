from pydantic import (
    BaseModel,
    EmailStr
)

from datetime import datetime

from typing import Optional


class CreateUserRequest(BaseModel):

    primer_nombre: str

    segundo_nombre: Optional[str] = None

    primer_apellido: str

    segundo_apellido: Optional[str] = None

    fecha_nacimiento: datetime

    email: EmailStr

    password: str

    numero_documento: str

    role_id: str