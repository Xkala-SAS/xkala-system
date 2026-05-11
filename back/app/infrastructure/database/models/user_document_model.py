from uuid import uuid4

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from app.infrastructure.database.db import Base
from app.infrastructure.database.base.base_model import (
    BaseModelMixin
)


class UserDocumentModel(Base, BaseModelMixin):

    __tablename__ = "user_documents"

    user_id = Column(
        String(36),
        ForeignKey("users.id"),
        nullable=False
    )

    document_type_id = Column(
        String(36),
        ForeignKey("document_types.id"),
        nullable=False
    )

    numero_documento = Column(
        String(100),
        unique=True,
        nullable=False
    )

    document_type = relationship(
        "DocumentTypeModel"
    )

    user = relationship(
        "UserModel",
        back_populates="documents"
    )