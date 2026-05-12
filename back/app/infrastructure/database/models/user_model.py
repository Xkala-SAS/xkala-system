from sqlalchemy import Column, String, Boolean, DateTime,ForeignKey
from sqlalchemy.orm import relationship
from app.infrastructure.database.base.base_class import Base
from app.infrastructure.database.base.base_model import (
    BaseModelMixin
)
from uuid import uuid4



class UserModel(
    Base,
    BaseModelMixin
    
    ):
    __tablename__ = "users"

    primer_nombre = Column(String(100), nullable=False)
    segundo_nombre = Column(String(100), nullable=True)
    primer_apellido = Column(String(100), nullable=False)
    segundo_apellido = Column(String(100), nullable=True)
    fecha_nacimiento = Column(DateTime, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    estado = Column(Boolean, default=True)
    role_id = Column(
    String(36),
    ForeignKey("roles.id"),
    nullable=False
    )
    documents = relationship(
        "UserDocumentModel",
        back_populates="user"
    )
    addresses = relationship(
        "UserAddressModel",
        back_populates="user"
    )
    health_info = relationship(
        "UserHealthInfoModel",
        uselist=False,
        back_populates="user"
    )

    contract_info = relationship(
        "UserContractModel",
        uselist=False,
        back_populates="user"
    )

    sizes = relationship(
        "UserSizeModel",
        uselist=False,
        back_populates="user"
    )

    files = relationship(
        "UserFileModel",
        back_populates="user"
    )

    contacts = relationship(
        "UserContactModel",
        back_populates="user"
    )

    role = relationship("RoleModel")