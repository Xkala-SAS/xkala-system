from sqlalchemy.orm import Session

from app.infrastructure.database.models.user_model import (
    UserModel
)

from app.infrastructure.database.models.role_model import (
    RoleModel
)

from app.infrastructure.database.models.user_document_model import (
    UserDocumentModel
)

from app.core.security.password_hasher import (
    PasswordHasher
)

from app.infrastructure.database.models.document_type_model import (
    DocumentTypeModel
)

from datetime import datetime


def seed_super_admin(db: Session):

    # =====================================
    # VALIDAR SI YA EXISTE
    # =====================================

    exists = db.query(UserModel).filter(
        UserModel.email == "admin@xkala.com"
    ).first()

    if exists:

        print("ℹ️ Super Admin ya existe")

        return

    # =====================================
    # OBTENER ROL
    # =====================================

    role = db.query(RoleModel).filter(
        RoleModel.nombre == "Super Admin"
    ).first()

    if not role:

        print("❌ Rol Super Admin no encontrado")

        return

    # =====================================
    # CREAR USUARIO
    # =====================================

    user = UserModel(

        primer_nombre="Super",

        segundo_nombre=None,

        primer_apellido="Admin",

        segundo_apellido=None,

        fecha_nacimiento=datetime(
            1999,
            1,
            1
        ),

        email="admin@xkala.com",

        password_hash=PasswordHasher.hash(
            "Admin123*"
        ),

        estado=True,

        role_id=role.id
    )

    db.add(user)

    db.flush()

    # =====================================
    # DOCUMENTO
    # =====================================

    document_type = db.query(
        DocumentTypeModel
    ).first()

    document = UserDocumentModel(

        user_id=user.id,

        numero_documento="1000000000",

        document_type_id=document_type.id
    )

    db.add(document)

    print("✅ Super Admin insertado")