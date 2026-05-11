from uuid import uuid4

from sqlalchemy import Column, String

from app.infrastructure.database.db import Base

from app.infrastructure.database.base.base_model import (
    BaseModelMixin
)


class EPSModel(Base, BaseModelMixin):

    __tablename__ = "eps"

    id = Column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4())
    )

    nombre = Column(
        String(100),
        unique=True,
        nullable=False
    )