from uuid import uuid4

from sqlalchemy import Column, String

from app.infrastructure.database.db import Base
from app.infrastructure.database.base.base_model import (
    BaseModelMixin
)

class CityModel(Base,BaseModelMixin):

    __tablename__ = "cities"


    nombre = Column(
        String(100),
        nullable=False
    )

    departamento = Column(
        String(100),
        nullable=False
    )