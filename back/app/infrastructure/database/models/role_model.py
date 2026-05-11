from sqlalchemy import Column, String

from app.infrastructure.database.db import Base

from uuid import uuid4

from app.infrastructure.database.base.base_model import (
    BaseModelMixin
)


class RoleModel(Base, BaseModelMixin):

    __tablename__ = "roles"

    nombre = Column(String(100), unique=True, nullable=False)

    descripcion = Column(String(255), nullable=True)