from sqlalchemy import or_
from sqlalchemy.orm import (Session, joinedload )
from datetime import datetime
from app.domain.user.entities.user import User
from app.domain.user.repositories.user_repository import UserRepository

from app.infrastructure.database.models.user_model import UserModel
from app.infrastructure.database.models.user_document_model import (
    UserDocumentModel
)
from app.infrastructure.database.models.user_address_model import (
    UserAddressModel
)

from app.infrastructure.database.models.user_health_info_model import (
    UserHealthInfoModel
)

from app.infrastructure.database.models.user_contract_model import (
    UserContractModel
)

from app.core.utils.audit_changes import (
    extract_changes
)

from app.infrastructure.database.models.audit_log_model import (
    AuditLogModel
)



class UserRepositoryImpl(UserRepository):

    def __init__(self, db: Session):
        self.db = db

    def save(self, user: User) -> User:

        db_user = UserModel(
            id=user.id,
            primer_nombre=user.primer_nombre,
            segundo_nombre=user.segundo_nombre,
            primer_apellido=user.primer_apellido,
            segundo_apellido=user.segundo_apellido,
            fecha_nacimiento=user.fecha_nacimiento,
            email=user.email,
            password_hash=user.password_hash,
            role_id=user.role_id,
            estado=user.estado,
            created_at=user.created_at
        )

        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)

        return user

    def get_by_id(self, user_id: str):

        db_user = (

            self.db.query(UserModel)
            .filter(
                UserModel.id == user_id,
                UserModel.deleted_at == None
            )  
            .first()
        )

        return self._to_domain(db_user)

    def get_by_document(
    self,
    numero_documento: str
):

        db_user = (
        
            self.db.query(UserModel)
    
            .join(
                UserDocumentModel,
                UserDocumentModel.user_id == UserModel.id
            )
    
            .filter(
                UserDocumentModel.numero_documento == numero_documento,
                UserModel.deleted_at == None
            )
    
            .first()
        )
    
        return self._to_domain(db_user)
    
    def get_by_email(self, email: str):

            db_user = (

                self.db.query(UserModel)
                .filter(
                    UserModel.email == email,
                    UserModel.deleted_at == None
                )
                .first()
            )

            return self._to_domain(db_user)

    def update(self, user: User):

        db_user = (
        
            self.db.query(UserModel)
    
            .filter(
                UserModel.id == user.id
            )
    
            .first()
        )
    
        if not db_user:
            return None
    
        db_user.primer_nombre = (
            user.primer_nombre
        )
    
        db_user.segundo_nombre = (
            user.segundo_nombre
        )
    
        db_user.primer_apellido = (
            user.primer_apellido
        )
    
        db_user.segundo_apellido = (
            user.segundo_apellido
        )
    
        db_user.email = (
            user.email
        )
    
        db_user.estado = (
            user.estado
        )
    
        db_user.role_id = (
            user.role_id
        )
    
        self.db.commit()
    
        self.db.refresh(db_user)
    
        return self._to_domain(db_user)

    def delete(self, user_id: str):

        db_user = (
            self.db.query(UserModel)
            .filter(UserModel.id == user_id)
            .first()
        )

        if db_user:

            db_user.estado = False

            db_user.deleted_at = (
                datetime.utcnow()
            )

            self.db.commit()
            
    def _to_domain(
    self,
    db_user: UserModel
    ):

        if not db_user:
            return None
    
        return User(
        
            id=db_user.id,
    
            primer_nombre=db_user.primer_nombre,
    
            segundo_nombre=db_user.segundo_nombre,
    
            primer_apellido=db_user.primer_apellido,
    
            segundo_apellido=db_user.segundo_apellido,
    
            fecha_nacimiento=db_user.fecha_nacimiento,
    
            email=db_user.email,
    
            password_hash=db_user.password_hash,
    
            role_id=db_user.role_id,
    
            role=db_user.role,
    
            estado=db_user.estado,
    
            created_at=db_user.created_at
        )

    def get_profile_data(self, user_id: str):

        return (

            self.db.query(UserModel)

            .options(
            
                joinedload(UserModel.role),

                joinedload(UserModel.documents)
                .joinedload(
                    UserDocumentModel.document_type
                ),

                joinedload(UserModel.addresses)
                .joinedload(
                    UserAddressModel.city
                ),

                joinedload(UserModel.health_info)
                .joinedload(
                    UserHealthInfoModel.eps
                ),

                joinedload(UserModel.health_info)
                .joinedload(
                    UserHealthInfoModel.arl
                ),

                joinedload(UserModel.health_info)
                .joinedload(
                    UserHealthInfoModel.pension_fund
                ),

                joinedload(UserModel.health_info)
                .joinedload(
                    UserHealthInfoModel.severance_fund
                ),

                joinedload(UserModel.contract_info)
                .joinedload(
                    UserContractModel.position
                ),

                joinedload(UserModel.contract_info)
                .joinedload(
                    UserContractModel.contract_type
                ),

                joinedload(UserModel.contacts),

                joinedload(UserModel.files),

                joinedload(UserModel.sizes)
            )

            .filter(
                UserModel.id == user_id,
                UserModel.deleted_at == None
            )

            .first()
        )

    def list_users(

        self,

        skip: int,

        limit: int,

        search: str = None,

        estado: bool = None,

        order_by: str= "created_at",

        direction: str= "desc"


    ):

        query = (

            self.db.query(UserModel)

            .filter(
                UserModel.deleted_at == None
            )
        )

        # =====================
        # SEARCH
        # =====================

        if search:

            query = query.filter(

                or_(

                    UserModel.primer_nombre.ilike(
                        f"%{search}%"
                    ),

                    UserModel.primer_apellido.ilike(
                        f"%{search}%"
                    ),

                    UserModel.email.ilike(
                        f"%{search}%"
                    )
                )
            )

        # =====================
        # ESTADO
        # =====================

        if estado is not None:

            query = query.filter(
                UserModel.estado == estado
            )

        allowed_order_fields = {

            "created_at":
                UserModel.created_at,

            "primer_nombre":
                UserModel.primer_nombre,

            "email":
                UserModel.email
        }

        order_column = (
            allowed_order_fields.get(
                order_by,
                UserModel.created_at
            )
        )

        if direction == "asc":

            query = query.order_by(
                order_column.asc()
            )
        
        else:
        
            query = query.order_by(
                order_column.desc()
            )
        
        return (

            query

            .offset(skip)

            .limit(limit)

            .all()
        )
    
    def count_users(

        self,
    
        search: str = None,
    
        estado: bool = None
    ):
    
        query = (
        
            self.db.query(UserModel)
    
            .filter(
                UserModel.deleted_at == None
            )
        )
    
        if search:
        
            query = query.filter(
            
                or_(
                
                    UserModel.primer_nombre.ilike(
                        f"%{search}%"
                    ),
    
                    UserModel.primer_apellido.ilike(
                        f"%{search}%"
                    ),
    
                    UserModel.email.ilike(
                        f"%{search}%"
                    )
                )
            )
    
        if estado is not None:
        
            query = query.filter(
                UserModel.estado == estado
            )
    
        return query.count()
