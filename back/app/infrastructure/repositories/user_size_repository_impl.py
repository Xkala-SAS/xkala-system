from sqlalchemy.orm import Session

from app.domain.user.repositories.user_size_repository import (
    UserSizeRepository
)

from app.infrastructure.database.models.user_size_model import (
    UserSizeModel
)


class UserSizeRepositoryImpl(
    UserSizeRepository
):

    def __init__(
        self,
        db: Session
    ):
        self.db = db

    def create(

        self,

        user_id: str,

        shirt_size: str,

        pants_size: str,

        shoe_size: str
    ):

        size = UserSizeModel(

            user_id=user_id,

            shirt_size=shirt_size,

            pants_size=pants_size,

            shoe_size=shoe_size
        )

        self.db.add(size)

        self.db.commit()

        self.db.refresh(size)

        return size