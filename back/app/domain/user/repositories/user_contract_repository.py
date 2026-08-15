from abc import ABC, abstractmethod

from datetime import datetime


class UserContractRepository(ABC):

    @abstractmethod
    def create(

        self,

        user_id: str,

        position_id: str,

        contract_type_id: str,

        fecha_ingreso: datetime,

        remuneration_type: str,

        remuneration_value: float
    ):
        pass

    @abstractmethod
    def update(

        self,

        user_id: str,

        position_id: str,

        contract_type_id: str,

        fecha_ingreso,

        remuneration_type: str,

        remuneration_value: float,

        estado_laboral: bool
    ):
        pass

    @abstractmethod
    def get_by_user_id(
        self,
        user_id: str
    ):
        pass