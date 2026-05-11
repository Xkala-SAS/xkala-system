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

    def get_primary_profile_photos(

        self,

        user_id: str
    ):

        return (

            self.db.query(UserFileModel)

            .filter(

                UserFileModel.user_id == user_id,

                UserFileModel.file_type ==
                "profile_photo",

                UserFileModel.is_primary == True
            )

            .all()
        )

    def save_user_file(

        self,

        user_file
    ):

        self.db.add(user_file)

        self.db.commit()

        self.db.refresh(user_file)

        return user_file