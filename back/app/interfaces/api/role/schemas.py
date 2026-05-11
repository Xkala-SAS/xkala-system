from pydantic import BaseModel


class CreateRoleRequest(BaseModel):
    nombre: str
    descripcion: str | None = None