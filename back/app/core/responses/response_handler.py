from typing import Any


def success_response(

    data: Any = None,

    message: str = "Operación exitosa",

    pagination: dict | None = None
):

    return {

        "success": True,

        "message": message,

        "data": data,

        "pagination": pagination,

        "errors": None
    }


def error_response(

    message: str,

    errors=None,

    status_code: int = 400
):

    return {

        "success": False,

        "message": message,

        "data": None,

        "pagination": None,

        "errors": errors
    }