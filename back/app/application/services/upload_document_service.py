from datetime import datetime

from fastapi import UploadFile

from app.core.files.file_storage import (
    save_file
)

from app.infrastructure.database.models.user_file_model import (
    UserFileModel
)

from app.core.validators.file_validator import (
    FileValidator
)


class UploadDocumentService:

    def __init__(self, repository):

        self.repository = repository

    def execute(

        self,

        file: UploadFile,

        document_type: str,

        current_user=None,

        user_id: str = None

    ):

        # ==============================
        # VALIDAR ARCHIVO
        # ==============================

        FileValidator.validate_document(
            file
        )

        # ==============================
        # REINICIAR STREAM
        # ==============================

        file.file.seek(0)

        # ==============================
        # GUARDAR ARCHIVO
        # ==============================

        path = save_file(

            file,

            "users/documents"
        )

        # ==============================
        # USUARIO DESTINO
        # ==============================

        target_user_id = (
            user_id
            if user_id
            else current_user.id
        )

        # ==============================
        # CREAR REGISTRO
        # ==============================

        user_file = UserFileModel(

            user_id=target_user_id,

            file_type=document_type,

            file_path=path,

            uploaded_at=datetime.utcnow(),

            is_active=True,

            is_primary=False
        )

        # ==============================
        # GUARDAR EN DB
        # ==============================

        self.repository.save_user_file(
            user_file
        )

        return {

            "message":
                "Documento subido correctamente",

            "path":
                path,

            "file_type":
                document_type
        }