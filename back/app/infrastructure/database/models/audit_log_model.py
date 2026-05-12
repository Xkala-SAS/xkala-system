from sqlalchemy import (
    Column,
    String,
    Text,
    ForeignKey,
    Integer,
    JSON
)
from app.infrastructure.database.base.base_class import Base
from app.infrastructure.database.base.base_model import BaseModelMixin

from sqlalchemy.orm import relationship

class AuditLogModel(Base, BaseModelMixin):

    __tablename__ = "audit_logs"

    user_id = Column(
        String(36),
        ForeignKey("users.id"),
        nullable=True
    )

    action = Column(
        String(100),
        nullable=False
    )

    resource = Column(
        String(100),
        nullable=False
    )

    method = Column(
        String(10),
        nullable=False
    )

    endpoint = Column(
        String(255),
        nullable=False
    )

    ip_address = Column(
        String(50),
        nullable=True
    )

    user_agent = Column(
        String(500),
        nullable=True
    )

    status_code = Column(
        Integer,
        nullable=True
    )

    description = Column(
        Text,
        nullable=True
    )

    old_values = Column(
        JSON,
        nullable=True
    )

    new_values = Column(
        JSON,
        nullable=True
    )

    extra_data = Column(
        JSON,
        nullable=True
    )

    user = relationship("UserModel")