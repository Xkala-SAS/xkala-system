from pydantic import BaseModel

from typing import Any, Optional


class SuccessResponseSchema(
    BaseModel
):

    success: bool = True

    message: str

    data: Optional[Any] = None


class ErrorResponseSchema(
    BaseModel
):

    success: bool = False

    error: str