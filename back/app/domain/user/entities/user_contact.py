from uuid import uuid4


class UserContact:

    def __init__(
        self,
        user_id: str,
        contact_type: str,
        contact_value: str,
        is_primary: bool = False,
        id: str = None
    ):

        self.id = id or str(uuid4())

        self.user_id = user_id

        self.contact_type = contact_type

        self.contact_value = contact_value

        self.is_primary = is_primary