from abc import ABC, abstractmethod


class UserFileRepository(ABC):

    @abstractmethod
    def get_primary_profile_photos(
        self,
        user_id: str
    ):
        pass

    @abstractmethod
    def save_user_file(
        self,
        user_file
    ):
        pass