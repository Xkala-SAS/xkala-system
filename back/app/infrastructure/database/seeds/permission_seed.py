from sqlalchemy.orm import Session

from app.infrastructure.database.models.permission_model import (
    PermissionModel
)
from app.infrastructure.database.seeds.permissions_catalog import (
    PERMISSIONS
)


def seed_permissions(db: Session):

    permissions = [

        {
            "codigo": codigo,
            "descripcion": descripcion
        }

        for codigo, descripcion in PERMISSIONS.items()

    ]

    for item in permissions:

        exists = (
            db.query(PermissionModel)
            .filter(
                PermissionModel.codigo == item["codigo"]
            )
            .first()
        )

        if not exists:

            db.add(
                PermissionModel(**item)
            )

    db.commit()

    print("✅ Permisos insertados")