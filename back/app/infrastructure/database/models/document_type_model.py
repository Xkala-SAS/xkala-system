from uuid import uuid4

from sqlalchemy import Column, String

from app.infrastructure.database.base.base_class import Base
from app.infrastructure.database.base.base_model import (
    BaseModelMixin
)


class DocumentTypeModel(Base, BaseModelMixin):

    __tablename__ = "document_types"

    codigo = Column(
        String(20),
        unique=True,
        nullable=False
    )

    nombre = Column(
        String(100),
        nullable=False
    )