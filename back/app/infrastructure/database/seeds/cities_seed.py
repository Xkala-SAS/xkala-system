import json

from pathlib import Path

from sqlalchemy.orm import Session

from app.infrastructure.database.models.city_model import (
    CityModel
)


def seed_cities(db: Session):

    file_path = Path(
        "app/shared/data/colombia/cities.json"
    )

    with open(file_path, "r", encoding="utf-8") as file:

        departments = json.load(file)

    total_inserted = 0

    for department in departments:

        department_name = department["departamento"]

        for city_name in department["ciudades"]:

            exists = db.query(CityModel).filter(
                CityModel.nombre == city_name,
                CityModel.departamento == department_name
            ).first()

            if not exists:

                city = CityModel(
                    nombre=city_name,
                    departamento=department_name
                )

                db.add(city)

                total_inserted += 1

    db.commit()

    print(f"✅ {total_inserted} ciudades insertadas")