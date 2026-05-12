from sqlalchemy.orm import Session

from app.infrastructure.database.models.pension_fund_model import (
    PensionFundModel
)


def seed_pension_funds(db: Session):

    funds = [

        "Colpensiones",
        "Porvenir",
        "Protección",
        "Colfondos",
        "Skandia"
    ]

    for nombre in funds:

        exists = db.query(PensionFundModel).filter(
            PensionFundModel.nombre == nombre
        ).first()

        if not exists:

            db.add(PensionFundModel(nombre=nombre))

    db.commit()

    print("✅ Fondos de pensión insertados")