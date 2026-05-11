from app.domain.role.entities.role import Role
from app.domain.role.repositories.role_repository import RoleRepository


class CreateRoleUseCase:

    def __init__(
        self,
        role_repository: RoleRepository
    ):
        self.role_repository = role_repository

    def execute(
        self,
        nombre: str,
        descripcion: str = None
    ):

        existing_role = (
            self.role_repository.get_by_name(nombre)
        )

        if existing_role:
            raise ValueError("El rol ya existe")

        role = Role(
            nombre=nombre,
            descripcion=descripcion
        )

        return self.role_repository.save(role)