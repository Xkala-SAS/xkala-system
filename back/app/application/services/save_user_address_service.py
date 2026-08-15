class SaveUserAddressService:

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

        direccion: str,

        barrio: str,

        city_id: str
    ):

        address = self.repository.create(

            user_id=user_id,

            direccion=direccion,

            barrio=barrio,

            city_id=city_id
        )

        self.onboarding_sync_service.execute(
            user_id
        )

        return address