from pydantic import BaseModel

from typing import List


class UserItemSchema(BaseModel):

    id: str

    nombre: str

    email: str

    estado: bool


class PaginationSchema(BaseModel):

    page: int

    limit: int

    total: int

    pages: int


class UserListResponseSchema(BaseModel):

    success: bool

    message: str

    data: List[UserItemSchema]

    pagination: PaginationSchema