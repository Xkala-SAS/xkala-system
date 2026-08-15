from sqlalchemy.orm import Session

from app.domain.user.repositories.user_address_repository import (
    UserAddressRepository
)

from app.infrastructure.database.models.user_address_model import (
    UserAddressModel
)


class UserAddressRepositoryImpl(
    UserAddressRepository
):

    def __init__(
        self,
        db: Session
    ):
        self.db = db

    def create(

        self,

        user_id: str,

        direccion: str,

        barrio: str,

        city_id: str
    ):

        address = UserAddressModel(

            user_id=user_id,

            direccion=direccion,

            barrio=barrio,

            city_id=city_id
        )

        self.db.add(address)

        self.db.commit()

        self.db.refresh(address)

        return address