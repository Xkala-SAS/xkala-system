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

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        departments = json.load(file)

    existing_cities = {

        (
            city.nombre,
            city.departamento
        )

        for city in db.query(CityModel).all()
    }

    new_cities = []

    for department in departments:

        department_name = (
            department["departamento"]
        )

        for city_name in department["ciudades"]:

            key = (
                city_name,
                department_name
            )

            if key not in existing_cities:

                new_cities.append(

                    CityModel(

                        nombre=city_name,

                        departamento=department_name
                    )
                )

    if new_cities:

        db.add_all(new_cities)

        print(
            f"✅ {len(new_cities)} ciudades insertadas"
        )

    else:

        print(
            "ℹ️ Ciudades ya existentes")