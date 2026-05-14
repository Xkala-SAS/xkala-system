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

        return

    permissions = db.query(
        PermissionModel
    ).filter(
        PermissionModel.codigo.in_(
            permission_names
        )
    ).all()

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

    # =====================================
    # SUPER ADMIN
    # =====================================

    all_permissions = db.query(
        PermissionModel
    ).all()

    assign_permissions(

        db,

        "Super Admin",

        [
            p.codigo
            for p in all_permissions
        ]
    )

    # =====================================
    # GESTION HUMANA
    # =====================================

    assign_permissions(

        db,

        "Gestion Humana",

        [

            # USERS
            "create_user",
            "view_users",
            "view_user_detail",
            "update_user",
            "change_user_status",

            # DOCUMENTS
            "upload_documents",
            "view_documents",
            "view_any_document",
            "delete_documents",
            "delete_any_document",

            # FILES
            "upload_profile_photo",
            "upload_signature"
        ]
    )

    # =====================================
    # EMPLEADO
    # =====================================

    assign_permissions(

        db,

        "Empleado",

        [

            # DOCUMENTS
            "upload_documents",
            "view_documents",
            "delete_documents",

            # FILES
            "upload_profile_photo",
            "upload_signature"
        ]
    )

    # =====================================
    # AUDITOR
    # =====================================

    assign_permissions(

        db,

        "Auditor",

        [

            "view_users",
            "view_user_detail",

            "view_documents",
            "view_any_document",

            "view_audit_logs"
        ]
    )

    # =====================================
    # SUPERVISOR
    # =====================================

    assign_permissions(

        db,

        "Supervisor",

        [

            "view_users",
            "view_user_detail",

            "view_documents",
            "view_any_document"
        ]
    )

    # =====================================
    # GERENCIA
    # =====================================

    assign_permissions(

        db,

        "Gerencia",

        [

            "view_users",
            "view_user_detail",

            "view_documents",
            "view_any_document",

            "view_audit_logs"
        ]
    )

    # =====================================
    # PRACTICANTE
    # =====================================

    assign_permissions(

        db,

        "Practicante",

        [

            "upload_documents",
            "view_documents"
        ]
    )

    print(
        "✅ Roles y permisos asignados"
    )