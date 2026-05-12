from sqlalchemy.orm import Session

from app.infrastructure.database.models.document_type_model import (
    DocumentTypeModel
)


def seed_document_types(db: Session):

    document_types = [

        {"codigo": "CC", "nombre": "Cedula de ciudadania"},

        {"codigo": "TI", "nombre": "Tarjeta de identidad"},

        {"codigo": "CE", "nombre": "Cedula de extranjeria"},

        {"codigo": "PAS", "nombre": "Pasaporte"},

        {"codigo": "NIT", "nombre": "Numero de identificacion tributaria"},

        {"codigo": "PEP", "nombre": "Permiso especial de permanencia"}
    ]

    existing_codes = {

        item.codigo

        for item in db.query(DocumentTypeModel).all()
    }

    new_items = []

    for item in document_types:

        if item["codigo"] not in existing_codes:

            new_items.append(
                DocumentTypeModel(**item)
            )

    if new_items:

        db.add_all(new_items)

        print(
            f"✅ {len(new_items)} tipos de documento insertados"
        )

    else:

        print(
            "ℹ️ Tipos de documento ya existentes")