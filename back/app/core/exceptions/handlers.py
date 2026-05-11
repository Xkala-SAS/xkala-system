from fastapi import FastAPI, Request

from fastapi.responses import JSONResponse

from app.core.exceptions.auth_exceptions import (

    InvalidCredentialsException,

    InactiveUserException
)
from app.core.exceptions.file_exceptions import (

    InvalidFileExtensionException,

    FileTooLargeException
)

from app.core.logging.logger import (
    logger
)


def register_exception_handlers(
    app: FastAPI
):

    # ======================================
    # INVALID CREDENTIALS
    # ======================================

    @app.exception_handler(
        InvalidCredentialsException
    )
    async def invalid_credentials_handler(
        request: Request,
        exc: InvalidCredentialsException
    ):

        return JSONResponse(

            status_code=401,

            content={

                "success": False,

                "error": exc.message
            }
        )

    # ======================================
    # INACTIVE USER
    # ======================================

    @app.exception_handler(
        InactiveUserException
    )
    async def inactive_user_handler(
        request: Request,
        exc: InactiveUserException
    ):

        return JSONResponse(

            status_code=403,

            content={

                "success": False,

                "error": exc.message
            }
        )

    # ======================================
    # GENERIC EXCEPTION
    # ======================================

    @app.exception_handler(Exception)
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
    
            content={
            
                "success": False,
    
                "error":
                    "Internal server error"
            }
        )
    

    @app.exception_handler(
    InvalidFileExtensionException
    )
    async def invalid_extension_handler(
        request: Request,
        exc: InvalidFileExtensionException
    ):

        return JSONResponse(

            status_code=400,

            content={

                "success": False,

                "error": exc.message
            }
        )
    
    @app.exception_handler(
        FileTooLargeException
    )
    async def file_too_large_handler(
        request: Request,
        exc: FileTooLargeException
    ):

        return JSONResponse(

            status_code=400,

            content={

                "success": False,

                "error": exc.message
            }
        )