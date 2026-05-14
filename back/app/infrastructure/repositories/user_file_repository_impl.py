from sqlalchemy.orm import Session

from app.domain.user.repositories.user_file_repository import (
    UserFileRepository
)

from app.infrastructure.database.models.user_file_model import (
    UserFileModel
)


class UserFileRepositoryImpl(
    UserFileRepository
):

    def __init__(

        self,

        db: Session
    ):

        self.db = db

    # ==================================
    # OBTENER ARCHIVOS POR TIPO
    # ==================================

    def get_files_by_type(

        self,

        user_id: str,

        file_type: str
    ):

        return (

            self.db.query(UserFileModel)

            .filter(

                UserFileModel.user_id == user_id,

                UserFileModel.file_type == file_type,

                UserFileModel.is_primary == True
            )

            .all()
        )

    # ==================================
    # FOTOS PRINCIPALES
    # ==================================

    def get_primary_profile_photos(

        self,

        user_id: str
    ):

        return self.get_files_by_type(

            user_id,

            "profile_photo"
        )

    # ==================================
    # GUARDAR ARCHIVO
    # ==================================

    def save_user_file(

        self,

        user_file
    ):

        self.db.add(user_file)

        self.db.commit()

        self.db.refresh(user_file)

        return user_file