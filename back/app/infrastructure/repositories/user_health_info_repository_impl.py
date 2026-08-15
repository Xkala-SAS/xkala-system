from sqlalchemy.orm import Session

from app.domain.user.repositories.user_health_info_repository import (
    UserHealthInfoRepository
)

from app.infrastructure.database.models.user_health_info_model import (
    UserHealthInfoModel
)


class UserHealthInfoRepositoryImpl(
    UserHealthInfoRepository
):

    def __init__(
        self,
        db: Session
    ):
        self.db = db

    def create(

        self,

        user_id: str,

        eps_id: str,

        arl_id: str,

        pension_fund_id: str,

        severance_fund_id: str
    ):

        health_info = UserHealthInfoModel(

            user_id=user_id,

            eps_id=eps_id,

            arl_id=arl_id,

            pension_fund_id=pension_fund_id,

            severance_fund_id=severance_fund_id
        )

        self.db.add(
            health_info
        )

        self.db.commit()

        self.db.refresh(
            health_info
        )

        return health_info