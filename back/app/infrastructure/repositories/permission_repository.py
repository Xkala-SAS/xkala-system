from sqlalchemy.orm import Session

from app.infrastructure.database.models.permission_model import (
    PermissionModel
)

from app.infrastructure.database.models.role_permission_model import (
    RolePermissionModel
)


class PermissionRepository:

    def __init__(self, db: Session):

        self.db = db

    # ==========================================
    # GET PERMISSIONS BY ROLE
    # ==========================================

    def get_permissions_by_role_id(

        self,

        role_id: str
    ):

        permissions = (

            self.db.query(
                PermissionModel.codigo
            )

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

        return [

            permission.codigo
            for permission in permissions
        ]

    # ==========================================
    # GET ALL PERMISSIONS
    # ==========================================

    def get_all(self):

        permissions = (

            self.db
            .query(PermissionModel)
            .all()
        )

        return [

            {
                "id": permission.id,
                "codigo": permission.codigo,
                "descripcion": permission.descripcion
            }

            for permission in permissions
        ]

    def count_all(self):

        return (
            self.db
            .query(PermissionModel)
            .count()
        )

    def get_permissions_by_role(self, role_id: str):

        permissions = (

            self.db.query(
                PermissionModel
            )

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

        return [

            {
                "id": permission.id,
                "codigo": permission.codigo,
                "descripcion": permission.descripcion
            }

            for permission in permissions
        ]