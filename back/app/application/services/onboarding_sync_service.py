from app.application.services.calculate_onboarding_status_service import (
    CalculateOnboardingStatusService
)


class OnboardingSyncService:

    def __init__(
        self,
        user_repository
    ):
        self.user_repository = user_repository

        self.calculate_service = (
            CalculateOnboardingStatusService()
        )

    def execute(
        self,
        user_id: str
    ):

        user = (
            self.user_repository
            .get_profile_data(user_id)
        )

        status = (
            self.calculate_service
            .execute(user)
        )

        self.user_repository.update_onboarding_status(
            user_id,
            status
        )

        return status