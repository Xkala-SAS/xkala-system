from sqlalchemy.orm import Session

from app.infrastructure.database.models.role_model import (
    RoleModel
)


def seed_roles(db: Session):

    roles = [

        {
            "nombre": "Super Admin",
            "descripcion": "Acceso total al sistema"
        },

        {
            "nombre": "Gerencia",
            "descripcion": "Acceso gerencial y estratégico"
        },

        {
            "nombre": "Gestion Humana",
            "descripcion": "Gestión de empleados y RRHH"
        },

        {
            "nombre": "Supervisor",
            "descripcion": "Supervisión operativa"
        },

        {
            "nombre": "Empleado",
            "descripcion": "Acceso básico del empleado"
        },

        {
            "nombre": "Practicante",
            "descripcion": "Acceso limitado para practicantes"
        },

        {
            "nombre": "Auditor",
            "descripcion": "Acceso de auditoría y consulta"
        }
    ]

    for item in roles:

        exists = db.query(RoleModel).filter(
            RoleModel.nombre == item["nombre"]
        ).first()

        if not exists:

            db.add(
                RoleModel(**item)
            )

    db.commit()

    print("✅ Roles insertados")