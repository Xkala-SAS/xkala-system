from sqlalchemy.orm import Session

from app.infrastructure.database.models.role_model import (
    RoleModel
)

from app.infrastructure.database.models.permission_model import (
    PermissionModel
)

from app.infrastructure.database.models.role_permission_model import (
    RolePermissionModel
)
from app.infrastructure.database.seeds.role_permissions_catalog import (
    ROLE_PERMISSIONS
)

from app.infrastructure.database.seeds.permissions_catalog import (
    PERMISSIONS
)



def assign_permissions(

    db: Session,

    role_name: str,

    permission_names: list
):

    role = db.query(
        RoleModel
    ).filter(
        RoleModel.nombre == role_name
    ).first()

    if not role:

        raise Exception(
            f"El rol '{role_name}' no existe."
        )

    permissions = db.query(
        PermissionModel
    ).filter(
        PermissionModel.codigo.in_(
            permission_names
        )
    ).all()

    found_permissions = {

        permission.codigo

        for permission in permissions

    }

    missing_permissions = set(permission_names) - found_permissions

    if missing_permissions:

        raise Exception(

            f"Los siguientes permisos no existen: "
            f"{', '.join(sorted(missing_permissions))}"

        )

    for permission in permissions:

        exists = db.query(
            RolePermissionModel
        ).filter(

            RolePermissionModel.role_id == role.id,

            RolePermissionModel.permission_id == permission.id

        ).first()

        if not exists:

            db.add(

                RolePermissionModel(

                    role_id=role.id,

                    permission_id=permission.id
                )
            )


def seed_role_permissions(db: Session):

    all_permission_codes = list(PERMISSIONS.keys())

    for role_name, permissions in ROLE_PERMISSIONS.items():

        if permissions == "__ALL__":

            permissions = all_permission_codes

        assign_permissions(

            db,

            role_name,

            permissions

        )

    print(
        "✅ Roles y permisos asignados"
    )