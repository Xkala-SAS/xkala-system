from sqlalchemy import Column, String, ForeignKey

from app.infrastructure.database.base.base_class import Base



class RolePermissionModel(Base):

    __tablename__ = "role_permissions"

    role_id = Column(
        String(36),
        ForeignKey("roles.id"),
        primary_key=True
    )

    permission_id = Column(
        String(36),
        ForeignKey("permissions.id"),
        primary_key=True
    )