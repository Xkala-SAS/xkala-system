def success_response(

    data=None,

    message="Operación exitosa",

    pagination=None
):

    response = {

        "success": True,

        "message": message,

        "data": data
    }

    if pagination:

        response["pagination"] = (
            pagination
        )

    return response


def error_response(

    error: str,

    status_code: int = 400
):

    return {

        "success": False,

        "error": error
    }