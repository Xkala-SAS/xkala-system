from uuid import uuid4

from datetime import datetime

from sqlalchemy import (
    Column,
    String,
    DateTime
)


class BaseModelMixin:

    id = Column(

        String(36),

        primary_key=True,

        default=lambda: str(uuid4())
    )

    created_at = Column(

        DateTime,

        default=datetime.utcnow
    )

    updated_at = Column(

        DateTime,
    
        default=datetime.utcnow,
    
        onupdate=datetime.utcnow
    )

    deleted_at = Column(

        DateTime,

        nullable=True
    )