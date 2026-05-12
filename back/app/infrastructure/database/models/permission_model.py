from sqlalchemy import Column, String

from app.infrastructure.database.base.base_class import Base

from uuid import uuid4

from app.infrastructure.database.base.base_model import (
    BaseModelMixin
)


class PermissionModel(Base, BaseModelMixin):

    __tablename__ = "permissions"
    
    codigo = Column(
        String(100),
        unique=True,
        nullable=False
    )

    descripcion = Column(
        String(255),
        nullable=True
    )