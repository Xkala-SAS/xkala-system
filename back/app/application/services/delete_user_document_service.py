from app.core.exceptions.http_exceptions import (
    BadRequestException
)


class DeleteUserDocumentService:

    def __init__(self, repository):

        self.repository = repository

    def execute(

        self,

        document_id,

        current_user
    ):

        document = (
            self.repository
            .get_by_id(document_id)
        )

        # ==============================
        # VALIDAR EXISTENCIA
        # ==============================

        if not document:

            raise BadRequestException(
                "Documento no encontrado"
            )

        if not document.is_active:

            raise BadRequestException(
                "El documento ya fue eliminado"
            )

        document.is_active = False

        self.repository.commit()

        # ==============================
        # SOFT DELETE
        # ==============================

        document.is_active = False

        self.repository.commit()

        return {

            "message":
                "Documento eliminado correctamente"
        }