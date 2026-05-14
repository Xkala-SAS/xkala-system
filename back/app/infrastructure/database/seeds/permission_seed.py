from sqlalchemy.orm import Session

from app.infrastructure.database.models.permission_model import (
    PermissionModel
)


def seed_permissions(db: Session):

    permissions = [

        # =====================================
        # USERS
        # =====================================

        {
            "codigo": "create_user",
            "descripcion": "Crear usuarios"
        },

        {
            "codigo": "view_users",
            "descripcion": "Ver usuarios"
        },

        {
            "codigo": "view_user_detail",
            "descripcion": "Ver detalle de usuario"
        },

        {
            "codigo": "update_user",
            "descripcion": "Actualizar usuarios"
        },

        {
            "codigo": "delete_user",
            "descripcion": "Eliminar usuarios"
        },

        {
            "codigo": "change_user_status",
            "descripcion": "Cambiar estado usuario"
        },

        # =====================================
        # DOCUMENTS
        # =====================================

        {
            "codigo": "upload_documents",
            "descripcion": "Subir documentos"
        },

        {
            "codigo": "view_documents",
            "descripcion": "Ver documentos propios"
        },

        {
            "codigo": "view_any_document",
            "descripcion": "Ver documentos de cualquier usuario"
        },

        {
            "codigo": "delete_documents",
            "descripcion": "Eliminar documentos propios"
        },

        {
            "codigo": "delete_any_document",
            "descripcion": "Eliminar documentos de cualquier usuario"
        },

        # =====================================
        # FILES
        # =====================================

        {
            "codigo": "upload_profile_photo",
            "descripcion": "Subir foto de perfil"
        },

        {
            "codigo": "upload_signature",
            "descripcion": "Subir firma"
        },

        # =====================================
        # ROLES
        # =====================================

        {
            "codigo": "manage_roles",
            "descripcion": "Administrar roles"
        },

        {
            "codigo": "view_roles",
            "descripcion": "Ver roles"
        },

        # =====================================
        # PERMISSIONS
        # =====================================

        {
            "codigo": "manage_permissions",
            "descripcion": "Administrar permisos"
        },

        {
            "codigo": "view_permissions",
            "descripcion": "Ver permisos"
        },

        # =====================================
        # AUDIT
        # =====================================

        {
            "codigo": "view_audit_logs",
            "descripcion": "Ver auditoria"
        }
    ]

    for item in permissions:

        exists = db.query(
            PermissionModel
        ).filter(
            PermissionModel.codigo == item["codigo"]
        ).first()

        if not exists:

            db.add(
                PermissionModel(**item)
            )

    print("✅ Permisos insertados")