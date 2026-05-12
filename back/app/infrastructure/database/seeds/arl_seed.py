from sqlalchemy.orm import Session

from app.infrastructure.database.models.arl_model import (
    ARLModel
)


def seed_arl(db: Session):

    arls = [

        "SURA",
        "Positiva",
        "Colmena",
        "Bolivar",
        "AXA Colpatria"
    ]

    for nombre in arls:

        exists = db.query(ARLModel).filter(
            ARLModel.nombre == nombre
        ).first()

        if not exists:

            db.add(ARLModel(nombre=nombre))

    db.commit()

    print("✅ ARL insertadas")