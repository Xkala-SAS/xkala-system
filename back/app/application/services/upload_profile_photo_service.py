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


class UploadProfilePhotoService:

    def __init__(self, repository, onboarding_sync_service):

        self.repository = repository

        self.onboarding_sync_service = (
            onboarding_sync_service
        )

    def execute(

        self,

        file: UploadFile,

        current_user=None,

        user_id: str = None

    ):

        # ==============================
        # VALIDAR ARCHIVO
        # ==============================

        FileValidator.validate_profile_photo(
            file
        )

        # ==============================
        # REINICIAR STREAM
        # ==============================

        file.file.seek(0)

        # ==============================
        # OBTENER USUARIO DESTINO
        # ==============================

        target_user_id = (
            user_id
            if user_id
            else current_user.id
        )

        # ==============================
        # GUARDAR ARCHIVO
        # ==============================

        path = save_file(
            file,
            "users/profile"
        )

        # ==============================
        # DESACTIVAR FOTO ANTERIOR
        # ==============================

        previous_photos = (

            self.repository
            .get_primary_profile_photos(
                target_user_id
            )
        )

        for photo in previous_photos:

            photo.is_primary = False

        # ==============================
        # NUEVA FOTO
        # ==============================

        user_file = UserFileModel(

            user_id=target_user_id,

            file_type="profile_photo",

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

        self.onboarding_sync_service.execute(
            target_user_id
        )

        return {

            "message":
                "Foto de perfil subida correctamente",

            "path":
                path,

            "file_type":
                "profile_photo"
        }