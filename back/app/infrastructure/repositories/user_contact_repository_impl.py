from sqlalchemy.orm import Session

from app.domain.user.repositories.user_contact_repository import (
    UserContactRepository
)

from app.infrastructure.database.models.user_contact_model import (
    UserContactModel
)


class UserContactRepositoryImpl(
    UserContactRepository
):

    def __init__(
        self,
        db: Session
    ):
        self.db = db

    def create(

        self,

        user_id: str,

        contact_type: str,

        contact_value: str,

        is_primary: bool
    ):

        contact = UserContactModel(

            user_id=user_id,

            contact_type=contact_type,

            contact_value=contact_value,

            is_primary=is_primary
        )

        self.db.add(contact)

        self.db.commit()

        self.db.refresh(contact)

        return contact