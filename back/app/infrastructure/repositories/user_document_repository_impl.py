from sqlalchemy.orm import Session

from app.infrastructure.database.models.user_document_model import (
    UserDocumentModel
)


class UserDocumentRepositoryImpl:

    def __init__(self, db: Session):

        self.db = db

    def save(self, user_document):

        model = UserDocumentModel(

            user_id=user_document.user_id,

            numero_documento=(
                user_document.numero_documento
            ),

            document_type_id=(
                user_document.document_type_id
            )
        )

        self.db.add(model)

        self.db.commit()

        self.db.refresh(model)

        return model

    def get_by_document(

        self,

        numero_documento: str
    ):

        return (

            self.db.query(UserDocumentModel)

            .filter(

                UserDocumentModel.numero_documento
                == numero_documento
            )

            .first()
        )