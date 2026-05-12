from sqlalchemy.orm import Session

from app.infrastructure.database.models.document_type_model import (
    DocumentTypeModel
)


def seed_document_types(db: Session):

    document_types = [

        {"codigo": "CC", "nombre": "Cédula de ciudadanía"},

        {"codigo": "TI", "nombre": "Tarjeta de identidad"},

        {"codigo": "CE", "nombre": "Cédula de extranjería"},

        {"codigo": "PAS", "nombre": "Pasaporte"},

        {"codigo": "NIT", "nombre": "Número de identificación tributaria"},

        {"codigo": "PEP", "nombre": "Permiso especial de permanencia"}
    ]

    for item in document_types:

        exists = db.query(DocumentTypeModel).filter(
            DocumentTypeModel.codigo == item["codigo"]
        ).first()

        if not exists:

            db.add(DocumentTypeModel(**item))

    db.commit()

    print("✅ Tipos de documento insertados")