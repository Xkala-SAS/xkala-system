from app.application.services.calculate_onboarding_status_service import (
    CalculateOnboardingStatusService
)

class GetOnboardingStatusService:

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

        return (
            self.calculate_service
            .execute(user)
        )