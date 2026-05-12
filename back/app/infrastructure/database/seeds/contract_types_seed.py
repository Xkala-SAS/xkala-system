from sqlalchemy.orm import Session

from app.infrastructure.database.models.contract_type_model import (
    ContractTypeModel
)


def seed_contract_types(db: Session):

    contract_types = [

        "Termino indefinido",
        "Termino fijo",
        "Obra o labor",
        "Prestación de servicios",
        "Aprendizaje"
    ]

    for nombre in contract_types:

        exists = db.query(ContractTypeModel).filter(
            ContractTypeModel.nombre == nombre
        ).first()

        if not exists:

            db.add(ContractTypeModel(nombre=nombre))

    db.commit()

    print("✅ Tipos de contrato insertados")