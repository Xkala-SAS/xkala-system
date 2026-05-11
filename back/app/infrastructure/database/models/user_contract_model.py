from uuid import uuid4

from sqlalchemy import (
    Column,
    String,
    ForeignKey,
    DateTime,
    Boolean
)
from sqlalchemy.orm import relationship

from app.infrastructure.database.db import Base
from app.infrastructure.database.base.base_model import (
    BaseModelMixin
)


class UserContractModel(Base, BaseModelMixin):

    __tablename__ = "user_contracts"

    user_id = Column(
        String(36),
        ForeignKey("users.id"),
        nullable=False,
        unique=True
    )

    position_id = Column(
        String(36),
        ForeignKey("positions.id"),
        nullable=False
    )

    contract_type_id = Column(
        String(36),
        ForeignKey("contract_types.id"),
        nullable=False
    )

    fecha_ingreso = Column(
        DateTime,
        nullable=False
    )

    estado_laboral = Column(
        Boolean,
        default=True
    )

    user = relationship(
        "UserModel",
        back_populates="contract_info"
    )

    position = relationship(
        "PositionModel"
    )
    
    contract_type = relationship(
        "ContractTypeModel"
    )