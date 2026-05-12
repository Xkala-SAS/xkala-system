from uuid import uuid4

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from app.infrastructure.database.base.base_class import Base
from app.infrastructure.database.base.base_model import (
    BaseModelMixin
)

class UserAddressModel(Base, BaseModelMixin):

    __tablename__ = "user_addresses"

    

    user_id = Column(
        String(36),
        ForeignKey("users.id"),
        nullable=False
    )

    direccion = Column(
        String(255),
        nullable=False
    )

    barrio = Column(
        String(100),
        nullable=False
    )

    city_id = Column(
        String(36),
        ForeignKey("cities.id"),
        nullable=False
    )

    user = relationship(
        "UserModel",
        back_populates="addresses"
    )

    city = relationship("CityModel")