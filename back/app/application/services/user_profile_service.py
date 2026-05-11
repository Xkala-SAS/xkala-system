from app.application.mappers.user_profile_mapper import (
    UserProfileMapper
)

class UserProfileService:

    def __init__(self, repository):

        self.repository = repository

    def execute(self, user_id: str):

        user = self.repository.get_profile_data(
            user_id
        )

        return UserProfileMapper.to_response(
            user
        )