from app.domain.user.entities.user import User

from app.core.utils.audit_changes import (
    extract_changes
)


class UpdateUserUseCase:

    def __init__(

        self,

        repository,

        audit_service
    ):

        self.repository = repository

        self.audit_service = audit_service

    def execute(

        self,

        user_id: str,

        primer_nombre: str,

        segundo_nombre: str,

        primer_apellido: str,

        segundo_apellido: str,

        email: str,

        estado: bool,

        role_id: str,

        current_user_id: str,

        ip_address: str
    ):

        existing_user = (
            self.repository.get_by_id(user_id)
        )

        if not existing_user:
            return None

        # =====================================
        # OLD DATA
        # =====================================

        old_data = {

            "primer_nombre":
                existing_user.primer_nombre,

            "segundo_nombre":
                existing_user.segundo_nombre,

            "primer_apellido":
                existing_user.primer_apellido,

            "segundo_apellido":
                existing_user.segundo_apellido,

            "email":
                existing_user.email,

            "estado":
                existing_user.estado,

            "role_id":
                existing_user.role_id
        }

        # =====================================
        # NUEVA ENTIDAD
        # =====================================

        updated_user = User(
                
            id=existing_user.id,
        
            primer_nombre=primer_nombre,
        
            segundo_nombre=segundo_nombre,
        
            primer_apellido=primer_apellido,
        
            segundo_apellido=segundo_apellido,
        
            fecha_nacimiento=existing_user.fecha_nacimiento,
        
            email=email,
        
            password_hash=existing_user.password_hash,
        
            role_id=role_id,
        
            estado=estado,
        
            created_at=existing_user.created_at
        )

        # =====================================
        # NEW DATA
        # =====================================

        new_data = {

            "primer_nombre":
                updated_user.primer_nombre,

            "segundo_nombre":
                updated_user.segundo_nombre,

            "primer_apellido":
                updated_user.primer_apellido,

            "segundo_apellido":
                updated_user.segundo_apellido,

            "email":
                updated_user.email,

            "estado":
                updated_user.estado,

            "role_id":
                updated_user.role_id
        }

        # =====================================
        # EXTRAER CAMBIOS
        # =====================================

        changes = extract_changes(
            old_data,
            new_data
        )

        # =====================================
        # ACTUALIZAR
        # =====================================

        result = self.repository.update(
            updated_user
        )

        # =====================================
        # AUDITORÍA
        # =====================================

        self.audit_service.execute(

            user_id=current_user_id,

            action="UPDATE",

            resource="USER",

            method="PUT",

            endpoint=f"/users/{user_id}",

            ip_address=ip_address,

            status_code=200,

            description="Usuario actualizado",

            old_values=changes["old_values"],

            new_values=changes["new_values"]
        )

        return result