from abc import ABC, abstractmethod


class UserSizeRepository(ABC):

    @abstractmethod
    def create(
        self,
        user_id: str,
        shirt_size: str,
        pants_size: str,
        shoe_size: str
    ):
        pass