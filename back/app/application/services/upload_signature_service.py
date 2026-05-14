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


class UploadSignatureService:

    def __init__(self, repository):

        self.repository = repository

    def execute(

        self,

        file: UploadFile,

        current_user

    ):

        # ==============================
        # VALIDAR ARCHIVO
        # ==============================

        FileValidator.validate_signature(
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

            "users/signatures"
        )

        # ==============================
        # DESACTIVAR FIRMAS PREVIAS
        # ==============================

        previous_signatures = (

            self.repository
            .get_files_by_type(

                current_user.id,

                "signature"
            )
        )

        for signature in previous_signatures:

            signature.is_primary = False

        # ==============================
        # CREAR NUEVO REGISTRO
        # ==============================

        user_file = UserFileModel(

            user_id=current_user.id,

            file_type="signature",

            file_path=path,

            uploaded_at=datetime.utcnow(),

            is_active=True,

            is_primary=True
        )

        # ==============================
        # GUARDAR EN DB
        # ==============================

        self.repository.save_user_file(
            user_file
        )

        return {

            "message":
                "Firma subida correctamente",

            "path":
                path,

            "file_type":
                "signature"
        }