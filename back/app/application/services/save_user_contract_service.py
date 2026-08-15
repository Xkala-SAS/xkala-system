class SaveUserContractService:

    def __init__(
        self,
        repository
    ):
        self.repository = repository

    def execute(

        self,

        user_id: str,

        position_id: str,

        contract_type_id: str,

        fecha_ingreso,

        remuneration_type: str,

        remuneration_value: float
    ):

        return self.repository.create(

            user_id=user_id,

            position_id=position_id,

            contract_type_id=contract_type_id,

            fecha_ingreso=fecha_ingreso,

            remuneration_type=remuneration_type,

            remuneration_value=remuneration_value
        )