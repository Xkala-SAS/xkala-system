from sqlalchemy.orm import Session

from app.infrastructure.database.models.eps_model import (
    EPSModel
)


def seed_eps(db: Session):

    eps_list = [

        "Nueva EPS",
        "SURA",
        "Sanitas",
        "Coosalud",
        "Famisanar",
        "Salud Total",
        "Compensar",
        "Mutual Ser"
    ]

    for nombre in eps_list:

        exists = db.query(EPSModel).filter(
            EPSModel.nombre == nombre
        ).first()

        if not exists:

            db.add(EPSModel(nombre=nombre))

    db.commit()

    print("✅ EPS insertadas")