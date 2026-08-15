from abc import ABC, abstractmethod


class UserContactRepository(ABC):

    @abstractmethod
    def create(
        self,
        user_id: str,
        contact_type: str,
        contact_value: str,
        is_primary: bool
    ):
        pass