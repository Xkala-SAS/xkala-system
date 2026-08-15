from fastapi import Depends
from sqlalchemy.orm import Session

from app.infrastructure.database.dependencies import (
    get_db
)

from app.infrastructure.repositories.user_repository_impl import (
    UserRepositoryImpl
)

from app.infrastructure.repositories.user_file_repository_impl import (
    UserFileRepositoryImpl
)

from app.infrastructure.repositories.audit_log_repository_impl import (
    AuditLogRepositoryImpl
)

from app.application.user.use_cases.save_personal_info import (
    SavePersonalInfoUseCase
)

from app.application.services.save_personal_info_service import (
    SavePersonalInfoService
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

from app.application.services.audit_log_service import (
    AuditLogService
)

from app.application.user.use_cases.login_user import (
    LoginUserUseCase
)

from app.application.user.use_cases.update_user import (
    UpdateUserUseCase
)

from app.application.services.audit_log_service import (
    AuditLogService
)

from app.infrastructure.repositories.audit_log_repository_impl import (
    AuditLogRepositoryImpl
)
from app.infrastructure.repositories.user_document_repository_impl import (
    UserDocumentRepositoryImpl
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

from app.application.services.list_user_audit_logs_service import (
    ListUserAuditLogsService
)

from app.infrastructure.repositories.audit_log_repository_impl import (
    AuditLogRepositoryImpl
)

from app.application.services.get_onboarding_status_service import (
    GetOnboardingStatusService
)

from app.infrastructure.repositories.user_address_repository_impl import (
    UserAddressRepositoryImpl
)

from app.application.services.save_user_address_service import (
    SaveUserAddressService
)

from app.infrastructure.repositories.user_contact_repository_impl import (
    UserContactRepositoryImpl
)

from app.application.services.save_user_contacts_service import (
    SaveUserContactsService
)

from app.infrastructure.repositories.user_health_info_repository_impl import (
    UserHealthInfoRepositoryImpl
)

from app.application.services.save_user_health_info_service import (
    SaveUserHealthInfoService
)

from app.infrastructure.repositories.user_contract_repository_impl import (
    UserContractRepositoryImpl
)

from app.application.services.save_user_contract_service import (
    SaveUserContractService
)

from app.application.services.onboarding_sync_service import (
    OnboardingSyncService
)

from app.infrastructure.repositories.user_size_repository_impl import (
    UserSizeRepositoryImpl
)

from app.application.services.save_user_size_service import (
    SaveUserSizeService
)

from app.application.services.update_user_contract_service import (
    UpdateUserContractService
)

from app.application.services.get_user_contract_service import (
    GetUserContractService
)

from app.application.services.change_password_service import (
    ChangePasswordService
)




# ==========================================
# REPOSITORIES
# ==========================================

def get_user_repository(
    db: Session = Depends(get_db)
):

    return UserRepositoryImpl(db)

def get_user_document_repository(
    db: Session = Depends(get_db)
):

    return UserDocumentRepositoryImpl(db)

def get_user_file_repository(
    db: Session = Depends(get_db)
):

    return UserFileRepositoryImpl(db)

def get_audit_repository(
    db: Session = Depends(get_db)
):

    return AuditLogRepositoryImpl(db)

def get_user_contact_repository(

    db: Session = Depends(get_db)
):

    return UserContactRepositoryImpl(db)

def get_user_address_repository(

    db = Depends(get_db)
):

    return UserAddressRepositoryImpl(
        db
    )

def get_user_health_info_repository(

    db: Session = Depends(
        get_db
    )
):

    return UserHealthInfoRepositoryImpl(
        db
    )

def get_user_contract_repository(

    db: Session = Depends(
        get_db
    )
):

    return UserContractRepositoryImpl(
        db
    )

def get_user_size_repository(

    db: Session = Depends(
        get_db
    )
):

    return UserSizeRepositoryImpl(
        db
    )

# ==========================================
# SERVICES
# ==========================================

def get_onboarding_status_service(

    repository = Depends(
        get_user_repository
    )
):

    return GetOnboardingStatusService(
        repository
    )

def get_onboarding_sync_service(

    repository = Depends(
        get_user_repository
    )
):

    return OnboardingSyncService(
        repository
    )

def get_audit_service(

    repository = Depends(
        get_audit_repository
    )
):

    return AuditLogService(
        repository
    )


def get_profile_service(

    repository = Depends(
        get_user_repository
    )
):

    return UserProfileService(
        repository
    )

def get_upload_profile_service(

    repository = Depends(
        get_user_file_repository
    ),

    onboarding_sync_service = Depends(
        get_onboarding_sync_service
    )
):

    return UploadProfilePhotoService(

        repository,

        onboarding_sync_service
    )

def get_upload_signature_service(

    repository = Depends(
        get_user_file_repository
    )
):

    return UploadSignatureService(
        repository
    )

def get_upload_document_service(

    repository = Depends(
        get_user_file_repository
    )
):

    return UploadDocumentService(
        repository
    )

def get_list_user_documents_service(

    repository = Depends(
        get_user_file_repository
    )
):

    return ListUserDocumentsService(
        repository
    )

def get_delete_user_document_service(

    repository = Depends(
        get_user_file_repository
    )
):

    return DeleteUserDocumentService(
        repository
    )

def get_list_users_service(

    repository = Depends(
        get_user_repository
    )
):

    return ListUsersService(
        repository
    )

def get_audit_log_repository(
    db: Session = Depends(get_db)
):

    return AuditLogRepositoryImpl(
        db
    )


def get_list_user_audit_logs_service(

    repository = Depends(
        get_audit_log_repository
    )
):

    return ListUserAuditLogsService(
        repository
    )




def get_save_user_contacts_service(

    repository = Depends(
        get_user_contact_repository
    ),

    onboarding_sync_service = Depends(
        get_onboarding_sync_service
    )
):

    return SaveUserContactsService(

        repository,

        onboarding_sync_service
    )

def get_save_user_health_info_service(

    repository = Depends(
        get_user_health_info_repository
    ),

    onboarding_sync_service = Depends(
        get_onboarding_sync_service
    )
):

    return SaveUserHealthInfoService(

        repository,

        onboarding_sync_service
    )

def get_save_user_contract_service(

    repository = Depends(
        get_user_contract_repository
    )
):

    return SaveUserContractService(
        repository
    )



def get_save_user_address_service(

    repository = Depends(
        get_user_address_repository
    ),

    onboarding_sync_service = Depends(
        get_onboarding_sync_service
    )
):

    return SaveUserAddressService(

        repository,

        onboarding_sync_service
    )

def get_save_user_size_service(

    repository = Depends(
        get_user_size_repository
    )
):

    return SaveUserSizeService(
        repository
    )

def get_update_user_contract_service(

    repository = Depends(
        get_user_contract_repository
    )
):

    return UpdateUserContractService(
        repository
    )

def get_user_contract_service(

    repository = Depends(
        get_user_contract_repository
    )
):

    return GetUserContractService(
        repository
    )

def get_change_password_service(

    repository = Depends(
        get_user_repository
    )
):

    return ChangePasswordService(
        repository
    )


def get_save_personal_info_service(

    repository = Depends(
        get_user_repository
    )
):

    use_case = SavePersonalInfoUseCase(
        repository
    )

    return SavePersonalInfoService(
        use_case
    )

# ==========================================
# USE CASES
# ==========================================

def get_login_use_case(

    repository = Depends(
        get_user_repository
    ),

    audit_service = Depends(
        get_audit_service
    )
):

    return LoginUserUseCase(

        repository,

        audit_service
    )

def get_update_user_use_case(

    repository = Depends(
        get_user_repository
    ),

    db: Session = Depends(get_db)
):

    audit_repository = (
        AuditLogRepositoryImpl(db)
    )

    audit_service = (
        AuditLogService(audit_repository)
    )

    return UpdateUserUseCase(

        repository,

        audit_service
    )