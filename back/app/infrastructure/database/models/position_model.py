from uuid import uuid4

from sqlalchemy import Column, String

from app.infrastructure.database.base.base_class import Base

from app.infrastructure.database.base.base_model import (
    BaseModelMixin
)

class PositionModel(Base, BaseModelMixin):

    __tablename__ = "positions"


    nombre = Column(
        String(100),
        unique=True,
        nullable=False
    )

    descripcion = Column(
        String(255),
        nullable=True
    )