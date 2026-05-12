from uuid import uuid4

from sqlalchemy import Column, String

from app.infrastructure.database.base.base_class import Base
from app.infrastructure.database.base.base_model import (
    BaseModelMixin
)

class ContractTypeModel(Base, BaseModelMixin ):

    __tablename__ = "contract_types"

    nombre = Column(
        String(100),
        unique=True,
        nullable=False
    )