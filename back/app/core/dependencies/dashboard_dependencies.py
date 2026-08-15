from app.application.dashboard.services.dashboard_ti_service import (
    DashboardTIService
)

from app.infrastructure.repositories.user_repository_impl import (
    UserRepositoryImpl
)

from app.infrastructure.repositories.user_file_repository_impl import (
    UserFileRepositoryImpl
)

from app.infrastructure.repositories.role_repository_impl import (
    RoleRepositoryImpl
)

from app.infrastructure.repositories.permission_repository import (
    PermissionRepository
)

from app.infrastructure.database.dependencies import get_db


def get_dashboard_ti_service():

    db = next(get_db())

    return DashboardTIService(

        user_repository=UserRepositoryImpl(db),

        user_file_repository=UserFileRepositoryImpl(db),

        role_repository=RoleRepositoryImpl(db),

        permission_repository=PermissionRepository(db)
    )