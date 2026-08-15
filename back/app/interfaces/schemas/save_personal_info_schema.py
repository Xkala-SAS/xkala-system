from datetime import datetime

from pydantic import (
    BaseModel,
    EmailStr
)

from typing import Optional


class SavePersonalInfoRequest(BaseModel):

    primer_nombre: str

    segundo_nombre: Optional[str] = None

    primer_apellido: str

    segundo_apellido: Optional[str] = None

    fecha_nacimiento: datetime

    email: EmailStr

    password: str