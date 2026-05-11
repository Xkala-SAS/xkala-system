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

    def __init__(self, repository):

        self.repository = repository

    def execute(

        self,

        file: UploadFile,

        current_user

    ):

        # validar archivo
        FileValidator.validate_profile_photo(
            file
        )

        # reiniciar stream
        file.file.seek(0)

        # guardar archivo físico
        path = save_file(
            file,
            "users/profile"
        )

        # buscar fotos principales previas
        previous_photos = (

            self.repository
            .get_primary_profile_photos(
                current_user.id
            )
        )

        # desactivar anteriores
        for photo in previous_photos:

            photo.is_primary = False

        # nueva foto
        user_file = UserFileModel(

            user_id=current_user.id,

            file_type="profile_photo",

            file_path=path,

            uploaded_at=datetime.utcnow(),

            is_active=True,

            is_primary=True
        )

        # guardar metadata
        self.repository.save_user_file(
            user_file
        )

        return {

            "message":
                "Archivo subido correctamente",

            "path":
                path,

            "file_type":
                "profile_photo"
        }