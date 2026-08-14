from sqlalchemy.orm import Session

from app.domain.role.entities.role import Role
from app.domain.role.repositories.role_repository import RoleRepository

from app.infrastructure.database.models.role_model import RoleModel

from app.infrastructure.database.models.permission_model import (
    PermissionModel
)

from app.infrastructure.database.models.role_permission_model import (
    RolePermissionModel
)



class RoleRepositoryImpl(RoleRepository):

    def __init__(self, db: Session):
        self.db = db

    def save(self, role: Role) -> Role:

        db_role = RoleModel(
            id=role.id,
            nombre=role.nombre,
            descripcion=role.descripcion
        )

        self.db.add(db_role)

        self.db.commit()

        self.db.refresh(db_role)

        return role

    def get_by_id(self, role_id: str):

        db_role = (
            self.db.query(RoleModel)
            .filter(RoleModel.id == role_id)
            .first()
        )

        return self._to_domain(db_role)

    def get_by_name(self, nombre: str):

        db_role = (
            self.db.query(RoleModel)
            .filter(RoleModel.nombre == nombre)
            .first()
        )

        return self._to_domain(db_role)

    def _to_domain(self, db_role: RoleModel):

        if not db_role:
            return None

        return Role(
            id=db_role.id,
            nombre=db_role.nombre,
            descripcion=db_role.descripcion
        )

    def get_all(self):

        roles = (

            self.db
            .query(RoleModel)
            .all()
        )

        return [

            {
                "id": role.id,
                "nombre": role.nombre,
                "descripcion": role.descripcion
            }

            for role in roles
        ]

    def count_all(self):

        return (
            self.db
            .query(RoleModel)
            .count()
        )

    def get_role_detail(
        self,
        role_id: str
    ):

        role = (
            self.db
            .query(RoleModel)
            .filter(
                RoleModel.id == role_id
            )
            .first()
        )

        if not role:
            return None

        permissions = (

            self.db

            .query(PermissionModel)

            .join(

                RolePermissionModel,

                RolePermissionModel.permission_id
                == PermissionModel.id
            )

            .filter(
                RolePermissionModel.role_id == role_id
            )

            .all()
        )

        return {

            "id": role.id,

            "nombre": role.nombre,

            "descripcion": role.descripcion,

            "permissions": [

                {
                    "id": permission.id,

                    "codigo": permission.codigo,

                    "descripcion": permission.descripcion
                }

                for permission in permissions
            ]
        }