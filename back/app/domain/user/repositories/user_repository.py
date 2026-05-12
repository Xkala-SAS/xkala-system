from abc import ABC, abstractmethod
from typing import Optional
from app.domain.user.entities.user import User


class UserRepository(ABC):

    @abstractmethod
    def save(self, user: User) -> User:
        pass

    @abstractmethod
    def get_by_id(self, user_id: str) -> Optional[User]:
        pass

    @abstractmethod
    def get_by_document(self, numero_documento: str) -> Optional[User]:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> Optional[User]:
        pass

    @abstractmethod
    def update(self, user: User) -> User:
        pass

    @abstractmethod
    def delete(self, user_id: str) -> None:
        pass

    @abstractmethod
    def get_profile_data(self, user_id: str):
        pass


    @abstractmethod
    def list_users(
        self,

        skip: int,
    
        limit: int,
    
        search: str = None,
    
        estado: bool = None,

        order_by: str= "created_at",

        direction: str= "desc"
    ):
        pass

    @abstractmethod
    def count_users(self):
        pass

    @abstractmethod
    def get_by_document(
        self,
        numero_documento: str
    ):
        pass