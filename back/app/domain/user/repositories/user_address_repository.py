from abc import ABC, abstractmethod


class UserAddressRepository(ABC):

    @abstractmethod
    def create(
        self,
        user_id: str,
        direccion: str,
        barrio: str,
        city_id: str
    ):
        pass