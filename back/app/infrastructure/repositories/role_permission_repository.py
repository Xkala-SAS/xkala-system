from sqlalchemy.orm import Session

from app.infrastructure.database.models.role_permission_model import (
    RolePermissionModel
)

from app.infrastructure.database.models.permission_model import (
    PermissionModel
)


class RolePermissionRepository:

    def __init__(self, db: Session):
        self.db = db

    def assign_permission(
        self,
        role_id: str,
        permission_id: str
    ):

        relation = RolePermissionModel(
            role_id=role_id,
            permission_id=permission_id
        )

        self.db.add(relation)

        self.db.commit()

    def role_has_permission(
        self,
        role_id: str,
        permission_code: str
    ) -> bool:

        permission = (
            self.db.query(PermissionModel)
            .join(
                RolePermissionModel,
                PermissionModel.id ==
                RolePermissionModel.permission_id
            )
            .filter(
                RolePermissionModel.role_id == role_id,
                PermissionModel.codigo == permission_code
            )
            .first()
        )

        return permission is not None