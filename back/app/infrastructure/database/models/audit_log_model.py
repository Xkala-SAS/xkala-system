from sqlalchemy import (
    Column,
    String,
    ForeignKey
)

from sqlalchemy.orm import (
    relationship
)

from app.infrastructure.database.db import (
    Base
)

from app.infrastructure.database.base.base_model import (
    BaseModelMixin
)


class AuditLogModel(

    Base,

    BaseModelMixin
):

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

    user = relationship(
        "UserModel"
    )