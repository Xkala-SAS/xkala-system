from fastapi import (
    FastAPI,
    Request,
    HTTPException
)

from fastapi.responses import (
    JSONResponse
)

from fastapi.exceptions import (
    RequestValidationError
)

from app.core.exceptions.base_exception import (
    AppException
)

from app.core.logging.logger import (
    logger
)

from app.core.responses.response_handler import (
    error_response
)


def register_exception_handlers(
    app: FastAPI
):

    # ==========================================
    # APP EXCEPTION
    # ==========================================

    @app.exception_handler(
        AppException
    )
    async def app_exception_handler(

        request: Request,

        exc: AppException
    ):

        return JSONResponse(

            status_code=exc.status_code,

            content=error_response(

                message=exc.message,

                errors={

                    "code":
                    exc.error_code
                }
            )
        )

    # ==========================================
    # HTTP EXCEPTION
    # ==========================================

    @app.exception_handler(
        HTTPException
    )
    async def http_exception_handler(

        request: Request,

        exc: HTTPException
    ):

        return JSONResponse(

            status_code=exc.status_code,

            content=error_response(

                message=str(exc.detail),

                errors={

                    "code":
                    "HTTP_EXCEPTION"
                }
            )
        )

    # ==========================================
    # VALIDATION
    # ==========================================

    @app.exception_handler(
        RequestValidationError
    )
    async def validation_exception_handler(

        request: Request,

        exc: RequestValidationError
    ):

        formatted_errors = []

        for error in exc.errors():

            formatted_errors.append({

                "field":

                ".".join(

                    map(
                        str,
                        error["loc"]
                    )
                ),

                "message":
                    error["msg"]
            })

        return JSONResponse(

            status_code=422,

            content=error_response(

                message=
                    "Validation error",

                errors=
                    formatted_errors
            )
        )

    # ==========================================
    # GENERIC
    # ==========================================

    @app.exception_handler(
        Exception
    )
    async def generic_exception_handler(

        request: Request,

        exc: Exception
    ):

        logger.exception(

            f"Unhandled exception "
            f"{request.method} "
            f"{request.url.path}"
        )

        return JSONResponse(

            status_code=500,

            content=error_response(

                message=
                    "Internal server error",

                errors={

                    "code":
                    "INTERNAL_SERVER_ERROR"
                }
            )
        )