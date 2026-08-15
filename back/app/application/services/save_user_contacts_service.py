from app.domain.user.repositories.user_contact_repository import (
    UserContactRepository
)


class SaveUserContactsService:

    def __init__(
        self,
        repository: UserContactRepository,
        onboarding_sync_service
    ):
        self.repository = repository

        self.onboarding_sync_service = (
            onboarding_sync_service
        )

    def execute(

        self,

        user_id: str,

        contacts: list
    ):

        results = []

        for contact in contacts:

            result = self.repository.create(

                user_id=user_id,

                contact_type=contact.contact_type,

                contact_value=contact.contact_value,

                is_primary=contact.is_primary
            )

            results.append(result)

        self.onboarding_sync_service.execute(
            user_id
        )

        return results