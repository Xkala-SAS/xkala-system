from uuid import uuid4

from sqlalchemy import Column, String

from app.infrastructure.database.db import Base

from app.infrastructure.database.base.base_model import (
    BaseModelMixin
)

class PensionFundModel(Base, BaseModelMixin):

    __tablename__ = "pension_funds"

    nombre = Column(
        String(100),
        unique=True,
        nullable=False
    )