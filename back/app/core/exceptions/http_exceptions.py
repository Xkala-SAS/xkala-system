from app.core.exceptions.base_exception import (
    AppException
)


class BadRequestException(
    AppException
):

    def __init__(

        self,

        message="Bad request"
    ):

        super().__init__(

            message=message,

            status_code=400,

            error_code="BAD_REQUEST"
        )