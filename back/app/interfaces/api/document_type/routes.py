from fastapi import APIRouter

from sqlalchemy.orm import Session

from app.infrastructure.database.db import SessionLocal

from app.infrastructure.database.models.document_type_model import (
    DocumentTypeModel
)


router = APIRouter(
    prefix="/document-types",
    tags=["Document Types"]
)


@router.post("/seed")
def seed_document_types():

    db: Session = SessionLocal()

    document_types = [
        {
            "codigo": "CC",
            "nombre": "Cédula de ciudadanía"
        },
        {
            "codigo": "CE",
            "nombre": "Cédula extranjería"
        },
        {
            "codigo": "PASSPORT",
            "nombre": "Pasaporte"
        },
        {
            "codigo": "NIT",
            "nombre": "Número identificación tributaria"
        }
    ]

    for item in document_types:

        exists = (
            db.query(DocumentTypeModel)
            .filter(
                DocumentTypeModel.codigo ==
                item["codigo"]
            )
            .first()
        )

        if not exists:

            document_type = DocumentTypeModel(
                codigo=item["codigo"],
                nombre=item["nombre"]
            )

            db.add(document_type)

    db.commit()

    return {
        "message": "Tipos documento creados"
    }