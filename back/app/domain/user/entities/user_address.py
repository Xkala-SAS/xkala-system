from uuid import uuid4


class UserAddress:

    def __init__(
        self,
        user_id: str,
        direccion: str,
        barrio: str,
        city_id: str,
        id: str = None
    ):

        self.id = id or str(uuid4())

        self.user_id = user_id

        self.direccion = direccion

        self.barrio = barrio

        self.city_id = city_id