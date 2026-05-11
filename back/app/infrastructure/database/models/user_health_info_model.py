from uuid import uuid4

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from app.infrastructure.database.db import Base
from app.infrastructure.database.base.base_model import (
    BaseModelMixin
)


class UserHealthInfoModel(Base, BaseModelMixin):

    __tablename__ = "user_health_info"

    user_id = Column(
        String(36),
        ForeignKey("users.id"),
        nullable=False,
        unique=True
    )

    eps_id = Column(
        String(36),
        ForeignKey("eps.id"),
        nullable=False
    )

    arl_id = Column(
        String(36),
        ForeignKey("arl.id"),
        nullable=False
    )

    pension_fund_id = Column(
        String(36),
        ForeignKey("pension_funds.id"),
        nullable=False
    )

    severance_fund_id = Column(
        String(36),
        ForeignKey("severance_funds.id"),
        nullable=False
    )

    user = relationship(
    "UserModel",
    back_populates="health_info"
    )

    eps = relationship("EPSModel")
    
    arl = relationship("ARLModel")
    
    pension_fund = relationship(
        "PensionFundModel"
    )
    
    severance_fund = relationship(
        "SeveranceFundModel"
    )