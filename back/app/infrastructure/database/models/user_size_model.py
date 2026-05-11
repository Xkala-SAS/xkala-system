from uuid import uuid4

from sqlalchemy import (
    Column,
    String,
    ForeignKey
)
from sqlalchemy.orm import relationship

from app.infrastructure.database.db import Base
from app.infrastructure.database.base.base_model import (
    BaseModelMixin
)


class UserSizeModel(Base,BaseModelMixin):

    __tablename__ = "user_sizes"

    user_id = Column(
        String(36),
        ForeignKey("users.id"),
        nullable=False,
        unique=True
    )

    shirt_size = Column(
        String(10),
        nullable=False
    )

    pants_size = Column(
        String(10),
        nullable=False
    )

    shoe_size = Column(
        String(10),
        nullable=False
    )

    user = relationship(
        "UserModel",
        back_populates="sizes"
    )   