from sqlalchemy.orm import (Session, joinedload)

from app.domain.user.repositories.user_contract_repository import (
    UserContractRepository
)

from app.infrastructure.database.models.user_contract_model import (
    UserContractModel
)


class UserContractRepositoryImpl(
    UserContractRepository
):

    def __init__(
        self,
        db: Session
    ):
        self.db = db

    def create(

        self,

        user_id: str,

        position_id: str,

        contract_type_id: str,

        fecha_ingreso,

        remuneration_type: str,

        remuneration_value: float
    ):

        contract = UserContractModel(

            user_id=user_id,

            position_id=position_id,

            contract_type_id=contract_type_id,

            fecha_ingreso=fecha_ingreso,

            remuneration_type=remuneration_type,

            remuneration_value=remuneration_value,

            estado_laboral=True
        )

        self.db.add(
            contract
        )

        self.db.commit()

        self.db.refresh(
            contract
        )

        return contract

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

        contract = (

            self.db.query(
                UserContractModel
            )

            .filter(
                UserContractModel.user_id == user_id
            )

            .first()
        )

        if not contract:
            return None

        contract.position_id = (
            position_id
        )

        contract.contract_type_id = (
            contract_type_id
        )

        contract.fecha_ingreso = (
            fecha_ingreso
        )

        contract.remuneration_type = (
            remuneration_type
        )

        contract.remuneration_value = (
            remuneration_value
        )

        contract.estado_laboral = (
            estado_laboral
        )

        self.db.commit()

        self.db.refresh(
            contract
        )

        return contract

    def get_by_user_id(
        self,
        user_id: str
    ):

        return (

            self.db.query(
                UserContractModel
            )

            .options(

                joinedload(
                    UserContractModel.position
                ),

                joinedload(
                    UserContractModel.contract_type
                )
            )

            .filter(
                UserContractModel.user_id == user_id
            )

            .first()
        )