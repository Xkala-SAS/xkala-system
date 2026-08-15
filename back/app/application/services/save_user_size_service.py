class SaveUserSizeService:

    def __init__(
        self,
        repository
    ):
        self.repository = repository

    def execute(

        self,

        user_id: str,

        shirt_size: str,

        pants_size: str,

        shoe_size: str
    ):

        return self.repository.create(

            user_id=user_id,

            shirt_size=shirt_size,

            pants_size=pants_size,

            shoe_size=shoe_size
        )