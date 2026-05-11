from abc import ABC, abstractmethod
from typing import Optional

from app.domain.role.entities.role import Role


class RoleRepository(ABC):

    @abstractmethod
    def save(self, role: Role) -> Role:
        pass

    @abstractmethod
    def get_by_id(self, role_id: str) -> Optional[Role]:
        pass

    @abstractmethod
    def get_by_name(self, nombre: str) -> Optional[Role]:
        pass