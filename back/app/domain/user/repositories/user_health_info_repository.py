from abc import ABC, abstractmethod


class UserHealthInfoRepository(ABC):

    @abstractmethod
    def create(
        self,
        user_id: str,
        eps_id: str,
        arl_id: str,
        pension_fund_id: str,
        severance_fund_id: str
    ):
        pass