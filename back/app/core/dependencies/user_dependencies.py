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


# ==========================================
# REPOSITORIES
# ==========================================

def get_user_repository(
    db: Session = Depends(get_db)
):

    return UserRepositoryImpl(db)


def get_user_file_repository(
    db: Session = Depends(get_db)
):

    return UserFileRepositoryImpl(db)


def get_audit_repository(
    db: Session = Depends(get_db)
):

    return AuditLogRepositoryImpl(db)


# ==========================================
# SERVICES
# ==========================================

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
    )
):

    return UploadProfilePhotoService(
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