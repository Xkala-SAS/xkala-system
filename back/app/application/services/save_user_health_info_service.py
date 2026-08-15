class SaveUserHealthInfoService:

    def __init__(
        self,
        repository,
        onboarding_sync_service
    ):
        self.repository = repository

        self.onboarding_sync_service = (
            onboarding_sync_service
        )

    def execute(

        self,

        user_id: str,

        eps_id: str,

        arl_id: str,

        pension_fund_id: str,

        severance_fund_id: str
    ):

        health_info = self.repository.create(

            user_id=user_id,

            eps_id=eps_id,

            arl_id=arl_id,

            pension_fund_id=pension_fund_id,

            severance_fund_id=severance_fund_id
        )

        self.onboarding_sync_service.execute(
            user_id
        )

        return health_info