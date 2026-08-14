from sqlalchemy import (
    Column,
    String,
    DateTime
)

from app.infrastructure.database.base.base_class import (
    Base
)

from app.infrastructure.database.base.base_model import (
    BaseModelMixin
)


class TokenBlacklistModel(
    Base,
    BaseModelMixin
):

    __tablename__ = "token_blacklist"

    jti = Column(

        String(255),

        unique=True,

        nullable=False
    )

    token_type = Column(

        String(50),

        nullable=False
    )

    expires_at = Column(

        DateTime,

        nullable=False
    )