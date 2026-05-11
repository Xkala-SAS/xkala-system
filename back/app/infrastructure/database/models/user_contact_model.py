from uuid import uuid4

from sqlalchemy import (
    Column,
    String,
    ForeignKey,
    Boolean
)

from sqlalchemy.orm import relationship

from app.infrastructure.database.db import Base

from app.infrastructure.database.base.base_model import (
    BaseModelMixin
)


class UserContactModel(Base, BaseModelMixin):

    __tablename__ = "user_contacts"

    user_id = Column(
        String(36),
        ForeignKey("users.id"),
        nullable=False
    )

    contact_type = Column(
        String(50),
        nullable=False
    )

    contact_value = Column(
        String(100),
        nullable=False
    )

    is_primary = Column(
        Boolean,
        default=False
    )

    user = relationship(
        "UserModel",
        back_populates="contacts"
    )