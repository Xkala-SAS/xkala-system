from sqlalchemy.orm import Session

from app.infrastructure.database.models.position_model import (
    PositionModel
)


def seed_positions(db: Session):

    positions = [

        {
            "nombre": "Gerente de Proyecto",
            "descripcion": "Responsable de dirigir proyectos"
        },

        {
            "nombre": "Gerente de Gestión Integral",
            "descripcion": "Responsable del sistema de gestión integral"
        },

        {
            "nombre": "Asistente de Gestión Humana",
            "descripcion": "Apoyo al área de gestión humana"
        },

        {
            "nombre": "Asistente de Proyecto",
            "descripcion": "Apoyo administrativo y operativo de proyectos"
        },

        {
            "nombre": "Practicante Operativo",
            "descripcion": "Practicante del área operativa"
        },

        {
            "nombre": "Practicante Administrativo",
            "descripcion": "Practicante del área administrativa"
        },

        {
            "nombre": "Supervisor de Mantenimiento",
            "descripcion": "Supervisión de mantenimiento"
        },

        {
            "nombre": "Auxiliar de Mantenimiento",
            "descripcion": "Apoyo operativo en mantenimiento"
        }
    ]

    for item in positions:

        exists = db.query(PositionModel).filter(
            PositionModel.nombre == item["nombre"]
        ).first()

        if not exists:

            db.add(PositionModel(**item))

    db.commit()

    print("✅ Cargos insertados")