import math

from app.application.mappers.user_list_mapper import (
    UserListMapper
)


class ListUsersService:

    def __init__(self, repository):

        self.repository = repository

    def execute(

        self,

        page: int,

        limit: int,

        search: str = None,

        estado: bool = None,

        order_by: str= "created_at",

        direction: str="desc"
    ):

        skip = (
            (page - 1) * limit
        )

        users = (

            self.repository.list_users(

                skip,

                limit,

                search,

                estado,

                order_by,

                direction
            )
        )

        total = (

            self.repository.count_users(

                search,

                estado
            )
        )

        total_pages = math.ceil(
            total / limit
        )

        return {

            "items":

                UserListMapper.to_response(
                    users
                ),

            "pagination": {

                "page": page,

                "limit": limit,

                "total": total,

                "pages": total_pages
            }
        }