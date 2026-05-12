from sqlalchemy.orm import Session

from app.infrastructure.database.models.severance_fund_model import (
    SeveranceFundModel
)


def seed_severance_funds(db: Session):

    funds = [

        "Porvenir",
        "Protección",
        "Colfondos",
        "Skandia"
    ]

    for nombre in funds:

        exists = db.query(SeveranceFundModel).filter(
            SeveranceFundModel.nombre == nombre
        ).first()

        if not exists:

            db.add(SeveranceFundModel(nombre=nombre))


    print("✅ Fondos de cesantías insertados")