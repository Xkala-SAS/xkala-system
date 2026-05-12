from uuid import uuid4

from datetime import datetime
from app.infrastructure.database.base.base_model import (
    BaseModelMixin
)

from sqlalchemy import (
    Column,
    String,
    ForeignKey,
    DateTime,
    Boolean
)
from sqlalchemy.orm import relationship

from app.infrastructure.database.base.base_class import Base


class UserFileModel(
    Base,
    BaseModelMixin
    ):

    __tablename__ = "user_files"

   

    user_id = Column(
        String(36),
        ForeignKey("users.id"),
        nullable=False
    )

    file_type = Column(
        String(50),
        nullable=False
    )

    is_active = Column(
    Boolean,
    default=True
    )

    is_primary = Column(
        Boolean,
        default=False
    )

    file_path = Column(
        String(255),
        nullable=False
    )

    uploaded_at = Column(
        DateTime,
        default=datetime.utcnow
    )
    user = relationship(
        "UserModel",
        back_populates="files"
    )