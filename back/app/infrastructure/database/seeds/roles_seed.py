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
            "descripcion": "Acceso gerencial y estrategico"
        },

        {
            "nombre": "Gestion Humana",
            "descripcion": "Gestion de empleados y RRHH"
        },

        {
            "nombre": "Supervisor",
            "descripcion": "Supervision operativa"
        },

        {
            "nombre": "Empleado",
            "descripcion": "Acceso basico del empleado"
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

    existing_roles = {

        role.nombre

        for role in db.query(RoleModel).all()
    }

    new_roles = []

    for item in roles:

        if item["nombre"] not in existing_roles:

            new_roles.append(
                RoleModel(**item)
            )

    if new_roles:

        db.add_all(new_roles)

        print(
            f"✅ {len(new_roles)} roles insertados"
        )

    else:

        print(
            "ℹ️ Roles ya existentes"
        )