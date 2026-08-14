from sqlalchemy import Column, String

from app.infrastructure.database.base.base_class import Base

from uuid import uuid4

from app.infrastructure.database.base.base_model import (
    BaseModelMixin
)

from sqlalchemy.orm import relationship

from app.infrastructure.database.models.role_permission_model import (
    RolePermissionModel
)


class RoleModel(Base, BaseModelMixin):

    __tablename__ = "roles"

    nombre = Column(String(100), unique=True, nullable=False)

    descripcion = Column(String(255), nullable=True)

    permissions = relationship(
        "PermissionModel",
        secondary="role_permissions",
        lazy="joined"
    )