from starlette.middleware.base import (
    BaseHTTPMiddleware
)

from fastapi import Request

from sqlalchemy.orm import Session

import time

from app.infrastructure.database.db import (
    SessionLocal
)

from app.application.services.audit_log_service import (
    AuditLogService
)

from app.infrastructure.repositories.audit_log_repository_impl import (
    AuditLogRepositoryImpl
)

from app.core.logging.logger import (
    logger
)

from app.core.exceptions.base_exception import (
    AppException
)


class AuditMiddleware(
    BaseHTTPMiddleware
):

    async def dispatch(

        self,

        request: Request,

        call_next
    ):

        start_time = time.time()

        response = None

        try:

            # ==========================================
            # EXECUTE REQUEST
            # ==========================================

            response = await call_next(
                request
            )

            return response

        except AppException:

            # 👈 deja pasar exceptions custom
            raise

        except Exception as e:

            logger.exception(
                f"Error interno middleware: {str(e)}"
            )

            raise

        finally:

            # ==========================================
            # AUDIT LOG
            # ==========================================

            try:

                duration = round(
                    time.time() - start_time,
                    4
                )

                db: Session = SessionLocal()

                repository = (
                    AuditLogRepositoryImpl(db)
                )

                service = AuditLogService(
                    repository
                )

                user_id = None

                if hasattr(
                    request.state,
                    "user"
                ):

                    user = request.state.user

                    if user:

                        user_id = user.id

                service.execute(

                    user_id=user_id,

                    action="REQUEST",

                    resource=request.url.path,

                    method=request.method,

                    endpoint=request.url.path,

                    ip_address=(

                        request.client.host
                        if request.client
                        else None
                    ),

                    user_agent=request.headers.get(
                        "user-agent"
                    ),

                    status_code=(

                        response.status_code
                        if response
                        else 500
                    ),

                    description=(

                        f"{request.method} "
                        f"{request.url.path}"
                    ),

                    extra_data={

                        "query_params":
                            dict(request.query_params),

                        "duration":
                            duration
                    }
                )

                db.close()

            except Exception as e:

                logger.error(

                    f"Error guardando auditoría: "
                    f"{str(e)}"
                )