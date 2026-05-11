from fastapi import APIRouter

from sqlalchemy.orm import Session

from app.infrastructure.database.db import SessionLocal

from app.infrastructure.database.models.city_model import (
    CityModel
)


router = APIRouter(
    prefix="/cities",
    tags=["Cities"]
)


@router.post("/seed")
def seed_cities():

    db: Session = SessionLocal()

    cities = [
        {
            "nombre": "Barranquilla",
            "departamento": "Atlántico"
        },
        {
            "nombre": "Bogotá",
            "departamento": "Cundinamarca"
        },
        {
            "nombre": "Medellín",
            "departamento": "Antioquia"
        },
        {
            "nombre": "Cali",
            "departamento": "Valle del Cauca"
        },
        {
            "nombre": "Cartagena",
            "departamento": "Bolívar"
        },
        {
            "nombre": "Bucaramanga",
            "departamento": "Santander"
        },
        {
            "nombre": "Pereira",
            "departamento": "Risaralda"
        },
        {
            "nombre": "Santa Marta",
            "departamento": "Magdalena"
        },
        {
            "nombre": "Ibagué",
            "departamento": "Tolima"
        },
        {
            "nombre": "Cúcuta",
            "departamento": "Norte de Santander"
        },
        {
            "nombre": "Manizales",
            "departamento": "Caldas"
        },
        {
            "nombre": "Villavicencio",
            "departamento": "Meta"
        },
        {
            "nombre": "Pasto",
            "departamento": "Nariño"
        },
        {
            "nombre": "Montería",
            "departamento": "Córdoba"
        },
        {
            "nombre": "Neiva",
            "departamento": "Huila"
        }
    ]

    for item in cities:

        exists = (
            db.query(CityModel)
            .filter(
                CityModel.nombre ==
                item["nombre"]
            )
            .first()
        )

        if not exists:

            city = CityModel(
                nombre=item["nombre"],
                departamento=item["departamento"]
            )

            db.add(city)

    db.commit()

    return {
        "message": "Ciudades creadas"
    }