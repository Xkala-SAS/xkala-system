from fastapi import (
    APIRouter,
    Depends,
    UploadFile,
    File,
    Query,
    Request
)

from typing import Optional

from app.core.responses.response_handler import (
    success_response
)

from app.interfaces.api.user.schemas import (
    LoginRequest
)

from app.interfaces.schemas.create_pre_registered_user_schema import (
    CreatePreRegisteredUserRequest
)

from app.interfaces.schemas.user_profile_schema import (
    UserProfileResponse
)

from app.interfaces.schemas.update_user_schema import (
    UpdateUserRequest
)

from app.interfaces.schemas.user_list_schema import (
    UserListResponseSchema
)

from app.core.security.auth_dependency import (
    get_current_user
)

from app.core.security.role_dependency import (
    require_role
)

from app.core.security.permission_dependency import (
    require_permission
)

from app.application.user.use_cases.update_user import (
    UpdateUserUseCase
)

from app.core.dependencies.user_dependencies import (
    get_update_user_use_case
)

from app.application.user.use_cases.create_user import (
    CreateUserUseCase
)

from app.application.user.use_cases.login_user import (
    LoginUserUseCase
)

from app.application.services.user_profile_service import (
    UserProfileService
)

from app.application.services.upload_profile_photo_service import (
    UploadProfilePhotoService
)

from app.application.services.list_user_service import (
    ListUsersService
)
from app.application.services.upload_signature_service import (
    UploadSignatureService
)

from app.application.services.upload_document_service import (
    UploadDocumentService
)
from app.application.services.list_user_documents_service import (
    ListUserDocumentsService
)
from app.application.services.delete_user_document_service import (
    DeleteUserDocumentService
)

from app.domain.user.enums.user_file_type import (
    UserFileType
)

from app.infrastructure.repositories.permission_repository import (
    PermissionRepository
)

from app.infrastructure.database.dependencies import (
    get_db
)

from app.application.services.list_user_audit_logs_service import (
    ListUserAuditLogsService
)

from app.application.services.get_onboarding_status_service import (
    GetOnboardingStatusService
)

from app.interfaces.schemas.save_user_address_schema import (
    SaveUserAddressRequest
)

from app.application.services.save_user_address_service import (
    SaveUserAddressService
)

from app.interfaces.schemas.save_user_contacts_schema import (
    SaveUserContactsRequest
)

from app.application.services.save_user_contacts_service import (
    SaveUserContactsService
)

from app.interfaces.schemas.save_user_health_info_schema import (
    SaveUserHealthInfoRequest
)

from app.application.services.save_user_health_info_service import (
    SaveUserHealthInfoService
)

from app.interfaces.schemas.save_user_contract_schema import (
    SaveUserContractRequest
)

from app.application.services.save_user_contract_service import (
    SaveUserContractService
)

from app.interfaces.schemas.save_user_size_schema import (
    SaveUserSizeRequest
)

from app.application.services.save_user_size_service import (
    SaveUserSizeService
)

from app.application.services.onboarding_sync_service import (
    OnboardingSyncService
)

from app.interfaces.schemas.update_user_contract_schema import (
    UpdateUserContractRequest
)

from app.application.services.update_user_contract_service import (
    UpdateUserContractService
)

from app.interfaces.schemas.user_contract_response_schema import (
    UserContractResponse
)

from app.interfaces.schemas.save_personal_info_schema import (
    SavePersonalInfoRequest
)

from app.application.services.get_user_contract_service import (
    GetUserContractService
)

from app.interfaces.schemas.change_password_schema import (
    ChangePasswordRequest
)

from app.application.services.change_password_service import (
    ChangePasswordService
)

from app.application.user.use_cases.create_pre_registered_user import (
    CreatePreRegisteredUserUseCase
)

from app.application.services.save_personal_info_service import (
    SavePersonalInfoService
)

from sqlalchemy.orm import Session

from app.core.dependencies.user_dependencies import (

    get_user_repository,

    get_login_use_case,

    get_profile_service,

    get_upload_profile_service,

    get_list_users_service,

    get_user_document_repository,

    get_upload_signature_service,

    get_upload_document_service,

    get_list_user_documents_service,

    get_delete_user_document_service,

    get_list_user_audit_logs_service,

    get_onboarding_status_service,

    get_onboarding_sync_service,

    get_save_user_address_service,

    get_save_user_contacts_service,

    get_save_user_health_info_service,

    get_save_user_contract_service,

    get_save_user_size_service,

    get_update_user_contract_service,

    get_user_contract_service,

    get_save_personal_info_service,

    get_change_password_service
)


router = APIRouter(

    prefix="/users",

    tags=["Users"]
)


# ==========================================
# CREATE PRE-REGISTERED USER
# ==========================================

@router.post("")
def create_user(

    request: CreatePreRegisteredUserRequest,

    current_user = Depends(
        require_permission("create_user")
    ),

    repository = Depends(
        get_user_repository
    ),

    user_document_repository = Depends(
        get_user_document_repository
    )
):

    use_case = CreatePreRegisteredUserUseCase(

        user_repository=repository,

        user_document_repository=user_document_repository
    )

    user = use_case.execute(

        numero_documento=request.numero_documento,

        document_type_id=request.document_type_id,

        role_id=request.role_id
    )

    return success_response(

        data={
            "user_id": user.id
        },

        message="Usuario preregistrado correctamente"
    )




# ==========================================
# PROFILE FULL
# ==========================================

@router.get(
    "/profile",
    response_model=UserProfileResponse
)
def get_profile(

    current_user = Depends(
        get_current_user
    ),

    service: UserProfileService = Depends(
        get_profile_service
    )
):

    return service.execute(
        current_user.id
    )

# ==========================================
# USER PROFILE BY ID
# ==========================================

@router.get("/{user_id}/profile")
def get_user_profile(

    user_id: str,

    current_user = Depends(
        require_permission(
            "view_users"
        )
    ),

    service: UserProfileService = Depends(
        get_profile_service
    )
):

    return service.execute(
        user_id
    )

# ==========================================
# UPLOAD PROFILE PHOTO
# ==========================================

@router.post("/upload/profile-photo")
def upload_profile_photo(

    file: UploadFile = File(...),

    current_user = Depends(
        require_permission(
            "upload_profile_photo"
        )
    ),

    service: UploadProfilePhotoService = Depends(
        get_upload_profile_service
    )
):

    result = service.execute(
        file,
        current_user
    )

    return success_response(

        data=result,

        message=
            "Archivo subido correctamente"
    )


# ==========================================
# UPLOAD USER PROFILE PHOTO
# ==========================================

@router.post("/{user_id}/profile-photo")
def upload_user_profile_photo(

    user_id: str,

    file: UploadFile = File(...),

    current_user = Depends(
        require_permission(
            "upload_profile_photo"
        )
    ),

    service: UploadProfilePhotoService = Depends(
        get_upload_profile_service
    )
):

    result = service.execute(

        file=file,

        user_id=user_id
    )

    return success_response(

        data=result,

        message=
            "Foto de perfil subida correctamente"
    )

# ==========================================
# UPLOAD SIGNATURE
# ==========================================

@router.post("/upload/signature")
def upload_signature(
    file: UploadFile = File(...),
    current_user = Depends(
        require_permission(
            "upload_signature"
        )
    ),
    service: UploadSignatureService = Depends(
        get_upload_signature_service
    )
):

    result = service.execute(
        file=file,
        user_id=current_user.id
    )

    return success_response(
        data=result,
        message="Firma subida correctamente"
    )

# ==========================================
# UPLOAD USER SIGNATURE
# ==========================================

@router.post("/{user_id}/signature")
def upload_user_signature(

    user_id: str,

    file: UploadFile = File(...),

    current_user = Depends(
        require_permission(
            "upload_signature"
        )
    ),

    service: UploadSignatureService = Depends(
        get_upload_signature_service
    )
):

    result = service.execute(

        file=file,

        user_id=user_id
    )

    return success_response(

        data=result,

        message="Firma subida correctamente"
    )


# ==========================================
# UPLOAD DOCUMENT
# ==========================================

@router.post("/upload/document")
def upload_document(

    document_type: UserFileType,

    file: UploadFile = File(...),

    current_user = Depends(
        require_permission(
            "upload_documents"
        )
    ),

    service: UploadDocumentService = Depends(
        get_upload_document_service
    )
):

    result = service.execute(

        file=file,

        document_type=document_type,

        current_user=current_user
    )

    return success_response(

        data=result,

        message=
            "Documento subido correctamente"
    )


@router.post("/{user_id}/documents")
def upload_user_document(

    user_id: str,

    document_type: str,

    file: UploadFile = File(...),

    current_user = Depends(
        require_permission(
            "upload_documents"
        )
    ),

    service: UploadDocumentService = Depends(
        get_upload_document_service
    )
):

    result = service.execute(

        file=file,

        document_type=document_type,

        user_id=user_id
    )

    return success_response(

        data=result,

        message=
            "Documento subido correctamente"
    )

# ==========================================
# MY DOCUMENTS
# ==========================================

@router.get("/my-documents")
def my_documents(

    current_user = Depends(
        require_permission(
            "view_documents"
        )
    ),

    service: ListUserDocumentsService = Depends(
        get_list_user_documents_service
    )
):

    result = service.execute(
        current_user.id
    )

    return success_response(

        data=result,

        message="Documentos obtenidos correctamente"
    )

# ==========================================
# USER DOCUMENTS
# ==========================================

@router.get("/{user_id}/documents")
def get_user_documents(

    user_id: str,

    current_user = Depends(
        require_permission(
            "view_documents"
        )
    ),

    service: ListUserDocumentsService = Depends(
        get_list_user_documents_service
    )
):

    result = service.execute(
        user_id
    )

    return success_response(

        data=result,

        message=
            "Documentos obtenidos correctamente"
    )


# ==========================================
# DELETE USER
# ==========================================

@router.delete("/{user_id}")
def delete_user(

    user_id: str,

    current_user = Depends(
        require_permission(
            "delete_user"
        )
    ),

    repository = Depends(
        get_user_repository
    )
):

    repository.delete(user_id)

    return success_response(

        data={
            "user_id": user_id
        },

        message=
            "Usuario eliminado correctamente"
    )


# ==========================================
# USER AUDIT LOGS
# ==========================================

@router.get("/{user_id}/audit-logs")
def get_user_audit_logs(

    user_id: str,

    current_user = Depends(
        require_permission(
            "view_users"
        )
    ),

    service: ListUserAuditLogsService = Depends(
        get_list_user_audit_logs_service
    )
):

    logs = service.execute(
        user_id
    )

    return success_response(

        data=[

            {
                "id": log.id,

                "action": log.action,

                "resource": log.resource,

                "description": log.description,

                "status_code": log.status_code,

                "created_at": log.created_at,

                "ip_address": log.ip_address
            }

            for log in logs
        ],

        message=
            "Historial obtenido correctamente"
    )

# ==========================================
# DELETE DOCUMENT
# ==========================================

@router.delete("/document/{document_id}")
def delete_document(

    document_id: str,

    current_user = Depends(
        require_permission(
            "delete_documents"
        )
    ),

    service: DeleteUserDocumentService = Depends(
        get_delete_user_document_service
    )
):

    result = service.execute(

        document_id,

        current_user
    )

    return success_response(

        data=result,

        message=
            "Documento eliminado correctamente"
    )

# ==========================================
# LIST USERS
# ==========================================

@router.get(
    "",
    response_model=UserListResponseSchema
)
def list_users(

    current_user = Depends(
        require_permission("view_users")
    ),

    page: int = Query(
        1,
        ge=1
    ),

    limit: int = Query(
        10,
        ge=1,
        le=100
    ),

    search: Optional[str] = None,

    estado: Optional[bool] = None,

    order_by: str = "created_at",

    direction: str = "desc",

    service: ListUsersService = Depends(
        get_list_users_service
    )
):

    result = service.execute(

        page,

        limit,

        search,

        estado,

        order_by,

        direction
    )

    return success_response(

        data=result["items"],

        message="Usuarios obtenidos",

        pagination=result["pagination"]
    )


# ==========================================
# ONBOARDING STATUS
# ==========================================

@router.get("/me/onboarding-status")
def onboarding_status(

    current_user = Depends(
        get_current_user
    ),

    service: GetOnboardingStatusService = Depends(
        get_onboarding_status_service
    )
):

    status = service.execute(
        current_user.id
    )

    return success_response(

        data={
            "status": status
        },

        message=
            "Estado onboarding obtenido"
    )

# ==========================================
# GET USER DETAIL
# ==========================================

@router.get("/{user_id}")
def get_user_detail(

    user_id: str,

    current_user = Depends(
        require_permission(
            "view_users"
        )
    ),

    repository = Depends(
        get_user_repository
    )
):

    user = repository.get_by_id(
        user_id
    )

    return success_response(

        data={
            "id": user.id,

            "primer_nombre":
                user.primer_nombre,

            "segundo_nombre":
                user.segundo_nombre,

            "primer_apellido":
                user.primer_apellido,

            "segundo_apellido":
                user.segundo_apellido,

            "fecha_nacimiento":
                user.fecha_nacimiento,

            "email":
                user.email,

            "role_id":
                user.role_id,

            "estado":
                user.estado,

            "onboarding_status":
                user.onboarding_status
        },

        message=
            "Usuario obtenido correctamente"
    )


# ==========================================
# UPDATE USER
# ==========================================

@router.put("/{user_id}")
def update_user(

    user_id: str,

    request: UpdateUserRequest,

    http_request: Request,

    current_user = Depends(
        require_permission("update_user")
    ),

    use_case: UpdateUserUseCase = Depends(
        get_update_user_use_case
    )
):

    result = use_case.execute(

        user_id=user_id,

        primer_nombre=request.primer_nombre,

        segundo_nombre=request.segundo_nombre,

        primer_apellido=request.primer_apellido,

        segundo_apellido=request.segundo_apellido,

        email=request.email,

        estado=request.estado,

        role_id=request.role_id,

        current_user_id=current_user.id,

        ip_address=http_request.client.host
    )

    return success_response(

        data={
            "user_id": result.id
        },

        message="Usuario actualizado correctamente"
    )

# ==========================================
# RESTORE USER
# ==========================================

@router.patch("/{user_id}/restore")
def restore_user(

    user_id: str,

    current_user = Depends(
        require_permission(
            "update_user"
        )
    ),

    repository = Depends(
        get_user_repository
    )
):

    repository.restore(
        user_id
    )

    return success_response(

        data={
            "user_id": user_id
        },

        message=
            "Usuario reactivado correctamente"
    )


# ==========================================
# SAVE MY PERSONAL INFO
# ==========================================

@router.post("/me/personal-info")
def save_my_personal_info(

    request: SavePersonalInfoRequest,

    current_user = Depends(
        get_current_user
    ),

    service: SavePersonalInfoService = Depends(
        get_save_personal_info_service
    )
):

    service.execute(

        user_id=current_user.id,

        primer_nombre=request.primer_nombre,

        segundo_nombre=request.segundo_nombre,

        primer_apellido=request.primer_apellido,

        segundo_apellido=request.segundo_apellido,

        fecha_nacimiento=request.fecha_nacimiento,

        email=request.email,

        password=request.password
    )

    return success_response(

        data=None,

        message="Información personal guardada correctamente"
    )

# ==========================================
# SAVE MY ADDRESS
# ==========================================

@router.post("/me/address")
def save_my_address(

    request: SaveUserAddressRequest,

    current_user = Depends(
        get_current_user
    ),

    service: SaveUserAddressService = Depends(
        get_save_user_address_service
    )
):

    address = service.execute(

        user_id=current_user.id,

        direccion=request.direccion,

        barrio=request.barrio,

        city_id=request.city_id
    )

    return success_response(

        data={
            "address_id": address.id
        },

        message=
            "Dirección guardada correctamente"
    )


# ==========================================
# SAVE MY CONTACTS
# ==========================================

@router.post("/me/contacts")
def save_my_contacts(

    request: SaveUserContactsRequest,

    current_user = Depends(
        get_current_user
    ),

    service: SaveUserContactsService = Depends(
        get_save_user_contacts_service
    )
):

    contacts = service.execute(

        user_id=current_user.id,

        contacts=request.contacts
    )

    return success_response(

        data={
            "total": len(contacts)
        },

        message=
            "Contactos guardados correctamente"
    )

# ==========================================
# SAVE MY HEALTH INFO
# ==========================================

@router.post("/me/health-info")
def save_my_health_info(

    request: SaveUserHealthInfoRequest,

    current_user = Depends(
        get_current_user
    ),

    service: SaveUserHealthInfoService = Depends(
        get_save_user_health_info_service
    )
):

    result = service.execute(

        user_id=current_user.id,

        eps_id=request.eps_id,

        arl_id=request.arl_id,

        pension_fund_id=request.pension_fund_id,

        severance_fund_id=request.severance_fund_id
    )

    return success_response(

        data={
            "health_info_id": result.id
        },

        message=
            "Información de salud guardada correctamente"
    )


# ==========================================
# SAVE MY SIZES
# ==========================================

@router.post("/me/sizes")
def save_my_sizes(

    request: SaveUserSizeRequest,

    current_user = Depends(
        get_current_user
    ),

    service: SaveUserSizeService = Depends(
        get_save_user_size_service
    ),

    onboarding_sync_service: OnboardingSyncService = Depends(
        get_onboarding_sync_service
    )
):

    size = service.execute(

        user_id=current_user.id,

        shirt_size=request.shirt_size,

        pants_size=request.pants_size,

        shoe_size=request.shoe_size
    )

    onboarding_sync_service.execute(
        current_user.id
    )

    return success_response(

        data={
            "size_id": size.id
        },

        message=
            "Tallas guardadas correctamente"
    )

# ==========================================
# SAVE MY CONTRACT INFO
# ==========================================

@router.post("/me/contract-info")
def save_my_contract_info(

    request: SaveUserContractRequest,

    current_user = Depends(
        get_current_user
    ),

    service: SaveUserContractService = Depends(
        get_save_user_contract_service
    )
):

    contract = service.execute(

        user_id=current_user.id,

        position_id=request.position_id,

        contract_type_id=request.contract_type_id,

        fecha_ingreso=request.fecha_ingreso,

        remuneration_type=request.remuneration_type,

        remuneration_value=request.remuneration_value
    )

    return success_response(

        data={
            "contract_id": contract.id
        },

        message=
            "Información contractual guardada correctamente"
    )

# ==========================================
# SAVE USER CONTRACT
# ==========================================

@router.post("/{user_id}/contract")
def save_user_contract(

    user_id: str,

    request: SaveUserContractRequest,

    current_user = Depends(
        require_permission(
            "manage_contracts"
        )
    ),

    service: SaveUserContractService = Depends(
        get_save_user_contract_service
    )
):

    contract = service.execute(

        user_id=user_id,

        position_id=request.position_id,

        contract_type_id=request.contract_type_id,

        fecha_ingreso=request.fecha_ingreso,

        remuneration_type=request.remuneration_type,

        remuneration_value=request.remuneration_value
    )

    return success_response(

        data={
            "contract_id": contract.id
        },

        message=
            "Contrato guardado correctamente"
    )

# ==========================================
# UPDATE USER CONTRACT
# ==========================================

@router.put("/{user_id}/contract")
def update_user_contract(

    user_id: str,

    request: UpdateUserContractRequest,

    current_user = Depends(
        require_permission(
            "manage_contracts"
        )
    ),

    service: UpdateUserContractService = Depends(
        get_update_user_contract_service
    )
):

    contract = service.execute(

        user_id=user_id,

        position_id=request.position_id,

        contract_type_id=request.contract_type_id,

        fecha_ingreso=request.fecha_ingreso,

        remuneration_type=request.remuneration_type,

        remuneration_value=request.remuneration_value,

        estado_laboral=request.estado_laboral
    )

    return success_response(

        data={
            "contract_id": contract.id
        },

        message=
            "Contrato actualizado correctamente"
    )

# ==========================================
# GET USER CONTRACT
# ==========================================

@router.get(
    "/{user_id}/contract",
    response_model=UserContractResponse
)
def get_user_contract(

    user_id: str,

    current_user = Depends(
        require_permission(
            "manage_contracts"
        )
    ),

    service: GetUserContractService = Depends(
        get_user_contract_service
    )
):

    contract = service.execute(
        user_id
    )

    return {

        "id":
            contract.id,

        "position_id":
            contract.position_id,

        "position_name":
            contract.position.nombre
            if contract.position else None,

        "contract_type_id":
            contract.contract_type_id,

        "contract_type_name":
            contract.contract_type.nombre
            if contract.contract_type else None,

        "fecha_ingreso":
            contract.fecha_ingreso,

        "remuneration_type":
            contract.remuneration_type,

        "remuneration_value":
            float(
                contract.remuneration_value
            ),

        "estado_laboral":
            contract.estado_laboral
    }

# ==========================================
# CHANGE PASSWORD
# ==========================================

@router.post(
    "/change-password"
)
def change_password(

    request: ChangePasswordRequest,

    current_user = Depends(
        get_current_user
    ),

    service: ChangePasswordService = Depends(
        get_change_password_service
    )
):

    service.execute(

        current_user.id,

        request.current_password,

        request.new_password
    )

    return success_response(

        data=None,

        message=
            "Contraseña actualizada correctamente"
    )