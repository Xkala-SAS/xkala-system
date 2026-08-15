from fastapi import APIRouter
from fastapi import Depends

from app.core.responses.response_handler import (
    success_response
)

from app.core.security.permission_dependency import (
    require_permission
)

from app.application.dashboard.services.dashboard_ti_service import (
    DashboardTIService
)

from app.core.dependencies.dashboard_dependencies import (
    get_dashboard_ti_service
)

router = APIRouter(

    prefix="/dashboard",

    tags=["Dashboard"]
)


@router.get("/ti")
def dashboard_ti(

    current_user = Depends(
        require_permission(
            "view_dashboard"
        )
    ),

    service: DashboardTIService = Depends(
        get_dashboard_ti_service
    )
):

    result = service.execute()

    return success_response(

        data=result,

        message="Dashboard obtenido correctamente"
    )